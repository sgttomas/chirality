//! U4 G5: the admission law's tests, through pure functions and the actual G-A
//! census. No profile and no permit is constructed here (decision 7): the
//! registered-identity list stays empty, and every check that needs a matched
//! build passes its inputs to the pure function directly.
use super::*;
use crate::source_receipt::CapturedInvocation;
use crate::PreviewSolverMode;
use serde_json::json;

const MILESTONE: &str = include_str!("../../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json");
const MODES: [PreviewSolverMode; 2] = [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny];
const M: u64 = 4_026_531_840;

fn milestone() -> Value {
    serde_json::from_str(MILESTONE).unwrap()
}
/// The actual G-A over a raw request: parse once, as the dispatch does, then admit.
fn admitted(raw: Value) -> RetainedAdmissionReport {
    let (request, capture) = CapturedInvocation::parse(raw, PreviewSolverMode::SparseInteractive).unwrap();
    assess(&capture, &request, Entry::Direct)
}
/// G-A over a typed request changed after the parse (capacity rows).
fn admitted_typed(raw: Value, change: impl FnOnce(&mut LinearStaticPreviewRequest)) -> RetainedAdmissionReport {
    let (mut request, capture) = CapturedInvocation::parse(raw, PreviewSolverMode::SparseInteractive).unwrap();
    change(&mut request);
    assess(&capture, &request, Entry::Direct)
}
fn domain(raw: Value) -> Option<AdmissionRefusal> {
    admitted(raw).law().domain
}
fn cap(fact: CapFact) -> impl Fn(Option<AdmissionRefusal>) -> bool {
    move |r| matches!(r, Some(AdmissionRefusal::Cap { fact: f, .. }) if f == fact)
}
fn model(r: &mut Value) -> &mut serde_json::Map<String, Value> {
    r["model"].as_object_mut().unwrap()
}
fn family(clause: D1Clause, fact: FamilyFact) -> Option<AdmissionRefusal> {
    Some(AdmissionRefusal::Family(clause, fact))
}
fn text(prefix: &str, len: usize) -> String {
    let mut s = String::from(prefix);
    while s.len() < len {
        s.push('x');
    }
    s.truncate(len);
    s
}

/// A cap-maximal D1 request (STACK_INVENTORY.md §3 W2's counts at `l ≤ 128`):
/// 32 nodes, a 32-member ring, 32 supports with 6 restraints each (r = 192) and a
/// scalar spring on each (s = 32), 128 nodal loads, 4 + 4 materials with 16
/// temperature points each, and one 128-byte identifier.
pub(super) fn cap_maximal() -> Value {
    let p = "invented_t3_g5_cap_maximal_input_no_library_data";
    let nodes: Vec<Value> = (0..32).map(|i| json!({"id": format!("N{i}"), "position": {"x": i as f64, "y": 0.0, "z": 0.0}, "provenance": p})).collect();
    let pipes: Vec<Value> = (0..32)
        .map(|i| json!({"id": format!("M{i}"), "from": format!("N{i}"), "to": format!("N{}", (i + 1) % 32), "material": "mat:0",
            "section": {"outside_diameter": {"value": 0.2, "unit": "m"}, "wall_thickness": {"value": 0.01, "unit": "m"}}, "provenance": p}))
        .collect();
    let supports: Vec<Value> = (0..32)
        .map(|i| json!({"id": format!("S{i}"), "node": format!("N{i}"), "restraints": ["UX", "UY", "UZ", "RX", "RY", "RZ"],
            "stiffness": {"dof": "UY", "value": {"value": 1.0e6, "unit": "N/m"}}, "provenance": p}))
        .collect();
    let loads: Vec<Value> = (0..128)
        .map(|i| json!({"id": format!("L{i}"), "category": "concentrated_force", "target": {"type": "node", "node": format!("N{}", i % 32)},
            "direction": "FY", "magnitude": {"value": 1.0, "unit": "N"}, "dimension": if i % 2 == 0 { "force" } else { "moment" }, "provenance": p}))
        .collect();
    let points: Vec<Value> = (0..16).map(|i| json!({"id": format!("T{i}"), "provenance": p})).collect();
    let materials: Vec<Value> = (0..4)
        .map(|i| json!({"id": format!("mat:{i}"), "elastic_modulus": {"value": 2.0e11, "unit": "Pa"}, "shear_modulus": {"value": 8.0e10, "unit": "Pa"},
            "temperature_points": points, "provenance": p}))
        .collect();
    json!({
        "model": {
            "schema_version": "0.1.0",
            "document_kind": "openpipestress.preview_model",
            "analysis_status": {"mechanics": "preview", "rule_check": "not_run", "professional_acceptance": "not_accepted"},
            "project": {"id": text("project:", 128), "units": {"length": "m", "force": "N"}},
            "nodes": nodes,
            "pipe_segments": pipes,
            "materials": materials,
            "supports": supports,
            "load_cases": [{"id": "case", "primitive_loads": loads, "provenance": p}],
            "combinations": []
        },
        "materials": materials
    })
}

// ---- D-6 -------------------------------------------------------------------

#[test]
fn encoder_roundtrip_covers_every_byte() {
    use build_identity::*;
    for byte in 0..=255u8 {
        let mut encoded = String::new();
        encode_identity_value(&[byte], &mut encoded);
        assert!(encoded.bytes().all(|b| identity_byte_is_plain(b) || b == b'%'), "{byte:#04x}: {encoded}");
        assert!(!encoded.contains([';', '=', ' ']) && encoded.bytes().all(|b| (0x21..0x7F).contains(&b)), "{byte:#04x}");
        assert_eq!(decode_identity_value(&encoded), Some(vec![byte]), "{byte:#04x}");
        assert_eq!(encoded.len(), if identity_byte_is_plain(byte) { 1 } else { 3 });
    }
    let all: Vec<u8> = (0..=255).collect();
    let mut encoded = String::new();
    encode_identity_value(&all, &mut encoded);
    assert_eq!(decode_identity_value(&encoded), Some(all));
    // Outside the encoder's image: lowercase, short, non-hex, escaped plain bytes, raw space.
    for bad in ["%3b", "%3", "%G0", "%41", "a b", "a;b", "a=b"] {
        assert_eq!(decode_identity_value(bad), None, "{bad}");
    }
    // An empty value is a value.
    let empty: [&[u8]; 16] = [b""; 16];
    let text = encode_identity(&empty);
    assert_eq!(decode_identity(&text), Some(vec![Vec::new(); 16]));
    assert_eq!(text.matches(';').count(), 16);
}

#[test]
fn identity_carries_every_key_in_order() {
    use build_identity::*;
    let compiled = COMPILED_IDENTITY.expect("build.rs sets the identity");
    assert_eq!(option_env!("OPS_RETAINED_BUILD_IDENTITY"), Some(compiled));
    assert_ne!(compiled, IDENTITY_UNAVAILABLE, "every key is readable on this host");
    assert!(!compiled.contains(['\n', ' ']), "one line");
    let tokens: Vec<&str> = compiled.split(';').collect();
    assert_eq!(tokens[0], IDENTITY_VERSION);
    let keys: Vec<&str> = tokens[1..].iter().map(|t| t.split_once('=').unwrap().0).collect();
    assert_eq!(keys, IDENTITY_KEYS, "every key, in order, no extras");
    let values = decode_identity(compiled).expect("decodes");
    let borrowed: [&[u8]; 16] = std::array::from_fn(|i| values[i].as_slice());
    assert_eq!(encode_identity(&borrowed), compiled, "re-encoding reproduces the text");
    let value = |key: &str| String::from_utf8(values[IDENTITY_KEYS.iter().position(|k| *k == key).unwrap()].clone()).unwrap();
    assert_eq!(value("debug_assertions"), cfg!(debug_assertions).to_string());
    assert_eq!(value("target.pointer_width"), (usize::BITS).to_string());
    assert_eq!(value("pkg"), format!("{}@{}", env!("CARGO_PKG_NAME"), env!("CARGO_PKG_VERSION")));
    assert_eq!(value("target.endian"), if cfg!(target_endian = "little") { "little" } else { "big" });
    assert_eq!(value("target.os"), std::env::consts::OS);
    assert_eq!(value("target.arch"), std::env::consts::ARCH);
    assert_eq!(value("panic"), if cfg!(panic = "unwind") { "unwind" } else { "abort" });
    assert_eq!(value("profile"), if cfg!(debug_assertions) { "debug" } else { "release" });
    // G6 registers the qualified build's text, printed by the same encoder.
    println!("I65_G5_IDENTITY {compiled}");
}

#[test]
fn identity_matching_is_missing_stale_or_exact() {
    use build_identity::IDENTITY_UNAVAILABLE;
    let none: [&str; 0] = [];
    assert_eq!(identity_match(Some("v1;a=b"), none.into_iter()), Err(ProfileStatus::Missing), "nothing registered");
    assert_eq!(identity_match(None, none.into_iter()), Err(ProfileStatus::Missing));
    let registered = ["v1;a=b", "v1;a=c"];
    assert_eq!(identity_match(None, registered.into_iter()), Err(ProfileStatus::Stale), "absent is Stale");
    assert_eq!(identity_match(Some(IDENTITY_UNAVAILABLE), registered.into_iter()), Err(ProfileStatus::Stale));
    assert_eq!(identity_match(Some("v1;a=d"), registered.into_iter()), Err(ProfileStatus::Stale));
    assert_eq!(identity_match(Some("v1;a=b;"), registered.into_iter()), Err(ProfileStatus::Stale), "byte-exact, no prefix");
    assert_eq!(identity_match(Some("v1;a=c"), registered.into_iter()), Ok(1));
    let unavailable = [IDENTITY_UNAVAILABLE];
    assert_eq!(identity_match(Some(IDENTITY_UNAVAILABLE), unavailable.into_iter()), Err(ProfileStatus::Stale), "never matches");
}

#[test]
fn bindings_need_witnesses_inputs_and_reader_layouts() {
    let layouts = READER_LAYOUTS;
    assert!(bindings_hold(true, Some("v1;x"), "v1;x", &layouts, &layouts));
    assert!(!bindings_hold(false, Some("v1;x"), "v1;x", &layouts, &layouts), "a false layout witness");
    assert!(!bindings_hold(true, None, "v1;x", &layouts, &layouts), "no reviewed-input record");
    assert!(!bindings_hold(true, Some("v1;y"), "v1;x", &layouts, &layouts), "a changed lock or static");
    let mut moved = layouts;
    moved[2].size += 8;
    assert!(!bindings_hold(true, Some("v1;x"), "v1;x", &layouts, &moved), "a changed reader layout");
    assert!(LAYOUT_WITNESSES, "this build's std and serde_json layouts are the ones the formulas assume");
    for (name, layout) in READER_LAYOUT_NAMES.iter().zip(READER_LAYOUTS) {
        println!("I65_G5_READER_LAYOUT {name} size={} align={}", layout.size, layout.align);
    }
}

#[test]
fn sha256_matches_the_sha2_dependency() {
    use sha2::{Digest, Sha256};
    let mut data = Vec::new();
    for len in 0..=300usize {
        let expected: [u8; 32] = Sha256::digest(&data).into();
        assert_eq!(build_identity::sha256(&data), expected, "length {len}");
        data.push((len * 31 % 251) as u8);
    }
    assert_eq!(build_identity::sha256(b"abc")[..4], [0xba, 0x78, 0x16, 0xbf]);
}

#[test]
fn reviewed_inputs_bind_the_lock_and_the_reader_statics() {
    use sha2::{Digest, Sha256};
    // G4 NOTES §3 and ORIGINS.json `statics`: the reviewed hashes at NUM b1f80234dc.
    const REVIEWED: [&str; 14] = [
        "4f494db6d8a6eca87e7a16d8561197f20b1951a033bd3a6c424acfff5613475b",
        "3bb969555d5616af6eefdb68788ee4a74a8a3681c42fe9aae577a5d25a51ac5c",
        "07951edacfedd410c153929ee75bb5bada15dbd222369ec63240c678b233b61c",
        "3e0779a45a74cf0bb3a4ed08ed3a6b44347aea8a3c33b59e9dd92130426ee296",
        "c74742ce6a936384e00986006e6a0b2e6bb11f190451e876eed9ffa11903c6a8",
        "4d6886d19e304db897e5e9f8f0054cbee91ba7795868f9698e2bbe070bde94da",
        "d75aacee175e178dbdeb256d89a65f4b375265f7da077725ee635af33df51d7e",
        "9a2cf6268b57bd5265a1a115497c07450819dd4d03cd5ab618097bd9d19da8cc",
        "44bc41c06f589fab6ce931ac0eaa5344765ff64fd5f880cc2dd69ecb839c4f4d",
        "d1628194a7730f427843b00228dd233cf92b8e7d26f3bc31c660a3ea59e28337",
        "ae55503d44a4750714a35c423623e38cf4132099134097193024d1635bfbc88a",
        "ba13f2aefd7a38bd725e5f111e6ec30144bc8776aa957c6278ee7b1178298ba1",
        "5f299065f15a157bbedf9467a598994ae684c4ecb3f851bbcb291981ec550a9f",
        "544e196d2f7bef27276acc160aa19ab738a4f7949e846d2e8871328d2208129c",
    ];
    // The same files, read here at compile time (test-only), by the sha2 dependency.
    let files: [&[u8]; 14] = [
        include_bytes!("../Cargo.lock"),
        include_bytes!("../../../schemas/physics_source_recovery.schema.json"),
        include_bytes!("../../../schemas/retained_precision_mp_v2.schema.json"),
        include_bytes!("../../../fixtures/results/retained_precision_prepared_ordinary_v1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_preview_physics_retained_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_2.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_precision_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_physics_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_load_reference_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_load_reference_source_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_preview_physics_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_physics_source_1.json"),
        include_bytes!("../../../fixtures/results/semantic_contract_v0_3_source_blocks_1.json"),
        include_bytes!("../../../schemas/source_block_recovery.schema.json"),
    ];
    let compiled = COMPILED_REVIEWED_INPUTS.expect("build.rs sets the reviewed inputs");
    assert_eq!(option_env!("OPS_RETAINED_REVIEWED_INPUTS"), Some(compiled));
    let mut tokens = compiled.split(';');
    assert_eq!(tokens.next(), Some("v1"));
    for (i, token) in tokens.by_ref().take(14).enumerate() {
        let (path, hex) = token.split_once('=').unwrap();
        assert_eq!(path, build_identity::REVIEWED_INPUTS[i]);
        assert_eq!(hex, format!("{:x}", Sha256::digest(files[i])), "{path}: build.rs's digest");
        assert_eq!(hex, REVIEWED[i], "{path}: G4's reviewed record");
    }
    assert_eq!(tokens.next(), None);
    println!("I65_G5_REVIEWED_INPUTS {compiled}");
    // Each reviewed static is the reader's own input: result_export names it.
    let reader = [
        include_str!("../../reporting/result_export/src/retained_precision.rs"),
        include_str!("../../reporting/result_export/src/physics_source.rs"),
        include_str!("../../reporting/result_export/src/semantic_contract.rs"),
        include_str!("../../reporting/result_export/src/source_blocks.rs"),
    ]
    .concat();
    for path in &build_identity::REVIEWED_INPUTS[1..] {
        let name = path.rsplit('/').next().unwrap();
        assert!(reader.contains(&format!("{name}\"")), "{name} is an include_str! input of the reader");
    }
}

#[test]
fn no_profile_or_permit_is_constructible() {
    assert!(REGISTERED_PROFILES.is_empty(), "decision 7: nothing is registered until G6");
    assert_eq!(build_status(), Err(ProfileStatus::Missing));
    let source = include_str!("retained_memory.rs");
    let production = &source[..source.find("#[cfg(test)]\n#[path = \"retained_memory_law_tests.rs\"]").unwrap()];
    assert!(production.contains("static REGISTERED_PROFILES: &[RegisteredProfile] = &[];"));
    assert_eq!(production.matches("RegisteredProfile {").count(), 1, "the definition only: no literal");
    assert_eq!(production.matches("CapturePermit { _profile").count(), 1, "admission's one construction");
    assert!(production.contains("(None, Some(profile)) => Ok(CapturePermit { _profile: profile }),"));
    // A forged registration index cannot mint a permit while the list is empty.
    let mut report = admitted(milestone());
    report.law.refusal = None;
    report.law.registered = Some(0);
    assert!(admission(report).is_err());
}

// ---- The census --------------------------------------------------------------

#[test]
fn raw_text_census_reads_lengths_and_control_bytes() {
    let mut map = serde_json::Map::new();
    map.insert("k\u{1f}ey".into(), json!(["a", "b\u{7f}c", "\u{0}", " ~"]));
    map.insert(text("long", 40), json!(text("v", 77)));
    let f = raw_text_census(&Value::Object(map));
    assert_eq!(f.status, CensusStatus::Complete);
    assert_eq!((f.max_key_bytes, f.max_string_bytes, f.control_bytes), (40, 77, 3));
    let mut deep = Value::Null;
    for _ in 0..DEPTH_LIMIT + 2 {
        deep = Value::Array(vec![deep]);
    }
    assert_eq!(raw_text_census(&deep).status, CensusStatus::DepthLimit);
    assert_eq!(raw_text_census(&Value::Array(vec![Value::Null; VALUE_LIMIT])).status, CensusStatus::ValueLimit);
    assert_eq!(raw_text_census(&Value::Array(vec![Value::Null; VALUE_LIMIT - 1])).status, CensusStatus::Complete);
}

#[test]
fn nested_typed_census_reads_the_roster() {
    let raw = cap_maximal();
    let request: LinearStaticPreviewRequest = serde_json::from_value(raw).unwrap();
    let f = nested_typed_census(&request);
    assert_eq!(f.status, CensusStatus::Complete);
    assert_eq!((f.restraints, f.springs, f.primitive_loads.length), (192, 32, 128));
    assert_eq!(f.max_temperature_points.length, 16);
    assert_eq!(f.max_string_bytes, 128, "the project id");
    assert!(f.max_string_capacity >= 128 && f.string_capacity_bytes >= f.strings);
    assert_eq!(f.units.values, 3);
    // Strings are counted once each: 32 nodes × 2 + 32 pipes × 7 + 32 supports × 11 + …
    let mut fewer = request.clone();
    fewer.model.nodes[0].provenance = None;
    assert_eq!(nested_typed_census(&fewer).strings + 1, f.strings);
    let milestone: LinearStaticPreviewRequest = serde_json::from_value(milestone()).unwrap();
    let m = nested_typed_census(&milestone);
    assert_eq!((m.status, m.primitive_loads.length, m.restraints), (CensusStatus::Complete, 3, 6));
}

// ---- D1 --------------------------------------------------------------------

#[test]
fn milestone_and_cap_maximal_inputs_are_inside_d1() {
    for raw in [milestone(), cap_maximal()] {
        for mode in MODES {
            let (request, capture) = CapturedInvocation::parse(raw.clone(), mode).unwrap();
            let report = assess(&capture, &request, Entry::Direct);
            assert_eq!(report.law().domain, None, "inside D1");
            assert_eq!(report.law().refusal, Some(AdmissionRefusal::Profile(ProfileStatus::Missing)), "D1.1 refuses: no profile");
            assert_eq!(report.profile, ProfileStatus::Missing);
            assert_eq!(report.law().raw_text.control_bytes, 0);
            let invocation = json!({"request": raw, "solver_mode": mode.as_str()});
            let id = String::from("g5");
            let headless = assess(&capture, &request, Entry::Headless(RetainedHeadlessContext::from_borrowed_roots(&raw, &invocation, &id)));
            assert_eq!(headless.law().refusal, Some(AdmissionRefusal::Caller(RetainedCaller::Headless)), "D1.0 first: Headless is refused");
            assert_eq!(headless.law().refusal.unwrap().precondition().as_str(), "caller");
        }
    }
}

#[test]
fn every_family_clause_refuses_with_its_fact() {
    use D1Clause as C;
    use FamilyFact as F;
    let with = |change: &dyn Fn(&mut Value)| {
        let mut raw = milestone();
        change(&mut raw);
        domain(raw)
    };
    assert_eq!(with(&|r| r["model"]["schema_version"] = json!("0.3.0")), family(C::Namespace, F::SchemaVersion));
    assert_eq!(with(&|r| r["model"]["schema_version"] = json!("0.2.0")), None, "0.2.0 is in the namespace");
    assert_eq!(with(&|r| r["model"]["pressure_contract"] = json!({})), family(C::Namespace, F::PressureContract));
    assert_eq!(with(&|r| r["model"]["reference_configurations"] = Value::Null), family(C::Namespace, F::ReferenceConfigurations));
    assert_eq!(with(&|r| r["model"]["materials"][0]["expansion_laws"] = Value::Null), family(C::Namespace, F::MaterialExpansionLaw));
    assert_eq!(with(&|r| r["materials"] = json!([{"id": "m", "elastic_modulus": {"value": 1.0, "unit": "Pa"}, "expansion_laws": null}])),
        family(C::Namespace, F::RequestExpansionLaws));
    assert_eq!(with(&|r| r["model"]["sections"] = json!([{"id": "s", "name": "s", "section_type": "pipe", "properties": {}, "provenance": null}])),
        family(C::Namespace, F::Sections));
    assert_eq!(with(&|r| r["model"]["pipe_segments"][0]["section_ref"] = json!("s")), family(C::Namespace, F::SectionRef));
    assert_eq!(with(&|r| { let case = r["model"]["load_cases"][0].clone(); r["model"]["load_cases"].as_array_mut().unwrap().push(case) }),
        family(C::Invocation, F::LoadCases));
    assert_eq!(with(&|r| r["model"]["load_cases"] = json!([])), family(C::Invocation, F::LoadCases));
    assert_eq!(with(&|r| r["model"]["combinations"] = json!([{"id": "c", "basis": "mechanics", "terms": [{"load_case": "case", "factor": 1.0}]}])),
        family(C::Invocation, F::Combinations));
    assert_eq!(with(&|r| r["model"]["components"] = json!([{"id": "k", "kind": "elbow", "node": "N0"}])), family(C::Invocation, F::Components));
    let case = |field: &'static str, value: Value| move |r: &mut Value| r["model"]["load_cases"][0][field] = value.clone();
    assert_eq!(with(&case("pressure_regions", json!([]))), family(C::Case, F::PressureRegions));
    assert_eq!(with(&case("equivalent_static", json!({}))), family(C::Case, F::EquivalentStatic));
    assert_eq!(with(&case("modulus_basis_ref", json!("T0"))), family(C::Case, F::ModulusBasisRef));
    assert_eq!(with(&case("modulus_basis_temperature", json!({"value": 20.0, "unit": "degC"}))), family(C::Case, F::ModulusBasisTemperature));
    assert_eq!(with(&case("analysis_state", Value::Null)), family(C::Case, F::AnalysisState));
    let support = |field: &'static str, value: Value| move |r: &mut Value| r["model"]["supports"][1][field] = value.clone();
    assert_eq!(with(&support("hanger", json!({}))), family(C::Supports, F::Hanger));
    assert_eq!(with(&support("nonlinear", json!({"behavior": "gap", "dof": "UY"}))), family(C::Supports, F::Nonlinear));
    assert_eq!(with(&support("family", json!(" anchor"))), family(C::Supports, F::SupportFamily), "exact strings, no trim");
    for family_name in ["anchor", "guide", "line_stop", "vertical_support", "spring"] {
        assert_eq!(with(&support("family", json!(family_name))), None, "{family_name}");
    }
    let load = |field: &'static str, value: Value| move |r: &mut Value| r["model"]["load_cases"][0]["primitive_loads"][2][field] = value.clone();
    assert_eq!(with(&load("target", json!({"type": "element", "pipe": "M1"}))), family(C::Loads, F::LoadTarget));
    assert_eq!(with(&load("dimension", json!("pressure"))), family(C::Loads, F::LoadDimension));
    assert_eq!(with(&load("dimension", json!("force"))), None);
    // D1.10, after D1.9: an object provenance, with or without leading ASCII whitespace.
    for provenance in ["{\"method\":\"pipe_mass_per_length_times_explicit_axis_acceleration\"}", " \t{", "{"] {
        assert_eq!(with(&load("provenance", json!(provenance))), family(C::Provenance, F::ObjectProvenance), "{provenance:?}");
    }
    for provenance in ["x{", "[{}]", "\"{\"", ""] {
        assert_eq!(with(&load("provenance", json!(provenance))), None, "{provenance:?}");
    }
    // D1.8 restates D1.4 (straight members only when no components exist).
    assert!(include_str!("retained_memory.rs").contains("return refuse(C::Members, F::Components);"));
    for clause in [C::Namespace, C::Invocation, C::Case, C::Supports, C::Loads, C::Members, C::Provenance] {
        assert_eq!(AdmissionRefusal::Family(clause, F::Components).precondition().as_str(), "source_family");
    }
}

#[test]
fn every_cap_row_admits_its_cap_and_refuses_cap_plus_one() {
    let report = admitted(cap_maximal());
    let law = report.law();
    let facts = DomainFacts {
        raw: &report.raw,
        raw_text: &law.raw_text,
        typed: &report.typed,
        nested: &law.nested,
        headless: None,
        digest: &report.captured_digest,
    };
    let rows = cap_rows(&facts);
    assert_eq!(first_cap_violation(&rows), Ok(()));
    for i in 0..CAP_ROWS {
        assert_eq!(rows.iter().filter(|r| r.fact == rows[i].fact).count(), 1, "{:?} once", rows[i].fact);
        let mut at = rows;
        at[i].observed = at[i].cap;
        assert_eq!(first_cap_violation(&at), Ok(()), "{:?} at its cap", rows[i].fact);
        let mut over = rows;
        over[i].observed = over[i].cap + 1;
        assert_eq!(first_cap_violation(&over), Err(AdmissionRefusal::Cap { fact: rows[i].fact, observed: rows[i].cap + 1, cap: rows[i].cap }));
        let refusal = AdmissionRefusal::Cap { fact: rows[i].fact, observed: 1, cap: 0 };
        let clause = if rows[i].fact == CapFact::ControlBytes { D1Clause::ControlBytes } else { D1Clause::Caps };
        assert_eq!((refusal.clause(), refusal.precondition().as_str()), (Some(clause), "resource_admission"));
    }
    // The cap-maximal input sits at the count caps.
    let at = |fact| rows.iter().find(|r| r.fact == fact).map(|r| (r.observed, r.cap)).unwrap();
    for fact in [CapFact::Nodes, CapFact::Members, CapFact::Supports, CapFact::Restraints, CapFact::Loads, CapFact::ModelMaterials,
        CapFact::RequestMaterials, CapFact::TemperaturePoints, CapFact::TypedTextBytes] {
        let (observed, cap) = at(fact);
        assert_eq!(observed, cap, "{fact:?}");
    }
    assert_eq!(at(CapFact::LoadsCapacity).1, 128, "l ≤ 128 (RR \"U4 G4\")");
}

#[test]
fn actual_inputs_map_each_cap_fact() {
    let over = |change: &dyn Fn(&mut Value)| {
        let mut raw = cap_maximal();
        change(&mut raw);
        domain(raw)
    };
    assert!(cap(CapFact::Nodes)(over(&|r| { let n = r["model"]["nodes"][0].clone(); model(r)["nodes"].as_array_mut().unwrap().push(n) })));
    assert!(cap(CapFact::Members)(over(&|r| { let p = r["model"]["pipe_segments"][0].clone(); model(r)["pipe_segments"].as_array_mut().unwrap().push(p) })));
    assert!(cap(CapFact::Supports)(over(&|r| {
        let mut s = r["model"]["supports"][0].clone();
        s["restraints"] = json!([]);
        model(r)["supports"].as_array_mut().unwrap().push(s)
    })));
    assert!(cap(CapFact::Restraints)(over(&|r| r["model"]["supports"][0]["restraints"].as_array_mut().unwrap().push(json!("UX")))));
    assert!(cap(CapFact::Loads)(over(&|r| {
        let l = r["model"]["load_cases"][0]["primitive_loads"][0].clone();
        r["model"]["load_cases"][0]["primitive_loads"].as_array_mut().unwrap().push(l)
    })));
    assert!(cap(CapFact::ModelMaterials)(over(&|r| { let m = r["model"]["materials"][0].clone(); model(r)["materials"].as_array_mut().unwrap().push(m) })));
    assert!(cap(CapFact::RequestMaterials)(over(&|r| { let m = r["materials"][0].clone(); r["materials"].as_array_mut().unwrap().push(m) })));
    assert!(cap(CapFact::TemperaturePoints)(over(&|r| {
        let p = r["model"]["materials"][1]["temperature_points"][0].clone();
        r["model"]["materials"][1]["temperature_points"].as_array_mut().unwrap().push(p)
    })));
    assert!(cap(CapFact::TypedTextBytes)(over(&|r| r["model"]["nodes"][3]["provenance"] = json!(text("p", 129)))));
    // A raw-only string (an unknown field) is bounded by the raw text row.
    assert!(cap(CapFact::RawTextBytes)(over(&|r| model(r).insert("unknown".into(), json!(text("u", 129))).map(drop).unwrap_or(()))));
    assert!(cap(CapFact::RawKeyTextBytes)(over(&|r| model(r).insert(text("k", 129), json!(1)).map(drop).unwrap_or(()))));
    assert!(cap(CapFact::ControlBytes)(over(&|r| r["model"]["nodes"][3]["provenance"] = json!("tab\there"))));
    assert_eq!(over(&|r| r["model"]["nodes"][3]["provenance"] = json!("quote\" and \\backslash")), None, "escapes are not control bytes");
    // Raw depth 16 is admitted, 17 is not (the census counts the root as 0).
    let nested = |levels: usize| {
        let mut v = json!(1);
        for _ in 0..levels {
            v = json!([v]);
        }
        v
    };
    // `model.deep` sits at depth 2, so `levels` arrays put its scalar at depth levels + 2.
    assert_eq!(over(&|r| model(r).insert("deep".into(), nested(14)).map(drop).unwrap_or(())), None, "depth 16");
    assert!(cap(CapFact::RawDepth)(over(&|r| model(r).insert("deep".into(), nested(15)).map(drop).unwrap_or(()))));
    // Raw totals: string bytes and key bytes.
    assert!(cap(CapFact::RawStringBytes)(over(&|r| {
        model(r).insert("bulk".into(), Value::Array((0..520).map(|i| json!(text(&format!("b{i}"), 128))).collect())).map(drop).unwrap_or(())
    })));
    assert!(cap(CapFact::RawKeyBytes)(over(&|r| {
        let keys: serde_json::Map<String, Value> = (0..520).map(|i| (text(&format!("k{i}"), 128), json!(0))).collect();
        model(r).insert("keys".into(), Value::Object(keys)).map(drop).unwrap_or(())
    })));
    // Raw value count: past 16,384 the census itself stops (D1.2).
    let report = admitted({
        let mut raw = cap_maximal();
        model(&mut raw).insert("many".into(), Value::Array(vec![json!(0); VALUE_LIMIT]));
        raw
    });
    assert_eq!(report.law().domain, Some(AdmissionRefusal::Census(CensusPart::Raw, CensusStatus::ValueLimit)));
    // Raw capacities: owners with spare capacity in an unknown field.
    let spare = |value: Value| {
        let mut raw = cap_maximal();
        model(&mut raw).insert("spare".into(), value);
        domain(raw)
    };
    let mut big = String::with_capacity(131_073);
    big.push('s');
    assert!(cap(CapFact::RawStringCapacity)(spare(Value::String(big))));
    let mut array = Vec::with_capacity(32_769);
    array.push(Value::Null);
    assert!(cap(CapFact::RawArrayCapacity)(spare(Value::Array(array))));
    let mut key = String::with_capacity(131_073);
    key.push('k');
    let mut map = serde_json::Map::new();
    map.insert(key, Value::Null);
    assert!(cap(CapFact::RawKeyCapacity)(spare(Value::Object(map))));
}

#[test]
fn typed_capacity_and_units_rows_read_the_actual_owners() {
    type Change = Box<dyn Fn(&mut LinearStaticPreviewRequest)>;
    let rows: Vec<(CapFact, Change)> = vec![
        (CapFact::NodesCapacity, Box::new(|r| r.model.nodes.reserve_exact(1))),
        (CapFact::MembersCapacity, Box::new(|r| r.model.pipe_segments.reserve_exact(1))),
        (CapFact::SupportsCapacity, Box::new(|r| r.model.supports.reserve_exact(1))),
        (CapFact::RestraintCapacity, Box::new(|r| {
            r.model.supports[0].restraints.reserve_exact(200);
        })),
        (CapFact::LoadsCapacity, Box::new(|r| r.model.load_cases[0].primitive_loads.reserve_exact(1))),
        (CapFact::ModelMaterialsCapacity, Box::new(|r| r.model.materials.reserve_exact(1))),
        (CapFact::RequestMaterialsCapacity, Box::new(|r| r.materials.reserve_exact(1))),
        (CapFact::TemperaturePointsCapacity, Box::new(|r| r.model.materials[0].temperature_points.reserve_exact(1))),
        (CapFact::LoadCasesCapacity, Box::new(|r| r.model.load_cases.reserve_exact(1))),
        (CapFact::SectionsCapacity, Box::new(|r| r.model.sections.reserve_exact(1))),
        (CapFact::ComponentsCapacity, Box::new(|r| r.model.components.reserve_exact(1))),
        (CapFact::CombinationsCapacity, Box::new(|r| r.model.combinations.reserve_exact(1))),
        (CapFact::RequestExpansionLawsCapacity, Box::new(|r| r.model.request_material_expansion_laws.reserve_exact(1))),
        (CapFact::MaterialExpansionLawsCapacity, Box::new(|r| r.model.material_expansion_laws.reserve_exact(1))),
        (CapFact::TypedTextCapacity, Box::new(|r| r.model.nodes[0].id.reserve_exact(200))),
        (CapFact::UnitsDepth, Box::new(|r| {
            let mut v = Value::Null;
            for _ in 0..17 {
                v = Value::Array(vec![v]);
            }
            r.model.project.units = v;
        })),
        (CapFact::UnitsTextBytes, Box::new(|r| r.model.project.units = json!(text("u", 129)))),
        (CapFact::UnitsKeyTextBytes, Box::new(|r| {
            let mut map = serde_json::Map::new();
            map.insert(text("k", 129), json!(1));
            r.model.project.units = Value::Object(map);
        })),
        (CapFact::UnitsStringCapacity, Box::new(|r| {
            let mut big = String::with_capacity(131_073);
            big.push('u');
            r.model.project.units = Value::String(big);
        })),
    ];
    for (fact, change) in rows {
        let report = admitted_typed(cap_maximal(), |r| change(r));
        assert!(cap(fact)(report.law().domain), "{fact:?}: {:?}", report.law().domain);
    }
    // A units Value past the census limits is D1.2, before its cap rows.
    let report = admitted_typed(cap_maximal(), |r| r.model.project.units = Value::Array(vec![Value::Null; caps::RAW_VALUES]));
    assert_eq!(report.law().domain, Some(AdmissionRefusal::Census(CensusPart::TypedNested, CensusStatus::ValueLimit)));
    let report = admitted_typed(cap_maximal(), |r| {
        let mut v = Value::Null;
        for _ in 0..DEPTH_LIMIT + 1 {
            v = Value::Array(vec![v]);
        }
        r.model.project.units = v;
    });
    assert_eq!(report.law().domain, Some(AdmissionRefusal::Census(CensusPart::TypedNested, CensusStatus::DepthLimit)));
}

#[test]
fn unknown_stale_overflow_and_partial_refusals_keep_every_fact() {
    let report = admitted(milestone());
    let law = report.law();
    let with_text = |raw: BorrowedValueFacts, text: RawTextFacts, typed: BorrowedRequestFacts, nested: NestedTypedFacts, headless: Option<HeadlessRootFacts>| {
        let request: LinearStaticPreviewRequest = serde_json::from_value(milestone()).unwrap();
        domain_clauses(
            &DomainFacts { raw: &raw, raw_text: &text, typed: &typed, nested: &nested, headless: headless.as_ref(), digest: &report.captured_digest },
            &request,
        )
    };
    let base = |raw, typed, nested, headless| with_text(raw, law.raw_text, typed, nested, headless);
    for status in [CensusStatus::DepthLimit, CensusStatus::ValueLimit, CensusStatus::ArithmeticOverflow] {
        let mut raw = report.raw;
        raw.status = status;
        assert_eq!(base(raw, report.typed, law.nested, None), Err(AdmissionRefusal::Census(CensusPart::Raw, status)));
        // The raw-text walk shares the raw census's cursor and limits, so in practice it is
        // incomplete only together with it; D1.2 still checks it on its own.
        let mut text = law.raw_text;
        text.status = status;
        assert_eq!(with_text(report.raw, text, report.typed, law.nested, None), Err(AdmissionRefusal::Census(CensusPart::RawText, status)));
        let mut typed = report.typed;
        typed.dof_upper = Err(status);
        assert_eq!(base(report.raw, typed, law.nested, None), Err(AdmissionRefusal::Census(CensusPart::TypedDof, status)));
        let mut nested = law.nested;
        nested.status = status;
        assert_eq!(base(report.raw, report.typed, nested, None), Err(AdmissionRefusal::Census(CensusPart::TypedNested, status)));
        let partial = HeadlessRootFacts { payload: report.raw, invocation: BorrowedValueFacts { status, ..report.raw }, request_id: report.captured_digest, payload_and_invocation_alias: false };
        assert_eq!(base(report.raw, report.typed, law.nested, Some(partial)), Err(AdmissionRefusal::Census(CensusPart::Headless, status)));
    }
    // The ordinary route is unchanged by every refusal, and the report keeps its facts.
    let mut deep = milestone();
    let mut child = Value::Null;
    for _ in 0..70 {
        child = Value::Array(vec![child]);
    }
    deep["unknown_admission_depth"] = child;
    for (raw, expected) in [
        (deep, Some(AdmissionRefusal::Census(CensusPart::Raw, CensusStatus::DepthLimit))),
        ({ let mut r = milestone(); r["model"]["supports"][1]["family"] = json!(" anchor"); r }, family(D1Clause::Supports, FamilyFact::SupportFamily)),
        ({ let mut r = milestone(); r["model"]["nodes"][0]["provenance"] = json!(text("p", 129)); r }, Some(AdmissionRefusal::Cap { fact: CapFact::TypedTextBytes, observed: 129, cap: 128 })),
    ] {
        for mode in MODES {
            let plain = serde_json::to_vec(&crate::run_linear_static_preview_value_with_mode(raw.clone(), mode).unwrap()).unwrap();
            let output = crate::run_linear_static_preview_value_with_retained_direct(raw.clone(), mode).unwrap();
            assert_eq!(serde_json::to_vec(output.envelope()).unwrap(), plain, "ordinary bytes");
            let report = output.admission().unwrap();
            assert_eq!(report.law().domain, expected);
            assert_eq!(report.law().refusal, Some(AdmissionRefusal::Profile(ProfileStatus::Missing)));
            assert!(output.successor().is_none());
        }
    }
}

#[test]
fn law_order_reports_the_first_failing_clause() {
    use std::cell::Cell;
    let called = Cell::new(false);
    let bound = |result: Result<u64, BoundRefusal>| {
        let called = &called;
        move |_index: usize| {
            called.set(true);
            result
        }
    };
    let family = Err(AdmissionRefusal::Family(D1Clause::Loads, FamilyFact::LoadTarget));
    assert_eq!(law_order(RetainedCaller::Headless, Ok(0), Ok(()), bound(Ok(1))), Err(AdmissionRefusal::Caller(RetainedCaller::Headless)));
    assert_eq!(law_order(RetainedCaller::Direct, Err(ProfileStatus::Missing), family, bound(Ok(1))), Err(AdmissionRefusal::Profile(ProfileStatus::Missing)));
    assert_eq!(law_order(RetainedCaller::Direct, Err(ProfileStatus::Stale), Ok(()), bound(Ok(1))), Err(AdmissionRefusal::Profile(ProfileStatus::Stale)));
    assert!(!called.get(), "the bound is not evaluated before D1 holds");
    assert_eq!(law_order(RetainedCaller::Direct, Ok(0), family, bound(Ok(1))), family.map(|_| 0));
    assert!(!called.get());
    assert_eq!(law_order(RetainedCaller::Direct, Ok(2), Ok(()), bound(Err(BoundRefusal::Unpriced))), Err(AdmissionRefusal::Bound(BoundRefusal::Unpriced)));
    assert!(called.get());
    assert_eq!(law_order(RetainedCaller::Direct, Ok(2), Ok(()), bound(Ok(7))), Ok(2));
    assert_eq!(AdmissionRefusal::Bound(BoundRefusal::Overflow).precondition().as_str(), "resource_admission");
    assert_eq!(AdmissionRefusal::Profile(ProfileStatus::Stale).clause(), Some(D1Clause::Build));
    assert_eq!(cap_priced_maximum(PreviewSolverMode::SparseInteractive), Err(BoundRefusal::Unpriced), "fail-closed until priced");
}

#[test]
fn bound_admits_at_m_and_refuses_above() {
    let r = RESERVED_STACK_BYTES as u64;
    assert_eq!(r, 67_108_864);
    assert_eq!(bound_admits(M - r - 1, r, M), Ok(M - 1));
    assert_eq!(bound_admits(M - r, r, M), Ok(M), "at M");
    assert_eq!(bound_admits(M - r + 1, r, M), Err(BoundRefusal::Exceeds { required: M + 1, threshold: M }));
    assert_eq!(bound_admits(u64::MAX, 1, M), Err(BoundRefusal::Overflow));
    assert_eq!(bound_admits(u64::MAX - r, r, u64::MAX), Ok(u64::MAX));
}

#[test]
fn refusal_kinds_are_the_schema_preconditions() {
    let schema = include_str!("../../../schemas/retained_precision_mp_v2.schema.json");
    let start = schema.find("\"const\": \"unavailable_precondition\"").unwrap();
    let block = &schema[start..start + 400];
    for kind in [UnavailablePrecondition::Caller, UnavailablePrecondition::SourceFamily, UnavailablePrecondition::ResourceAdmission] {
        assert!(block.contains(&format!("\"{}\"", kind.as_str())), "{kind:?}");
    }
    assert_eq!(STACK_RESERVATION_PRECONDITION.as_str(), "resource_admission");
    assert_eq!(AdmissionRefusal::Census(CensusPart::Raw, CensusStatus::ValueLimit).precondition().as_str(), "resource_admission");
    let ids: Vec<&str> = [D1Clause::Caller, D1Clause::Build, D1Clause::Census, D1Clause::Namespace, D1Clause::Invocation, D1Clause::Case,
        D1Clause::Supports, D1Clause::Loads, D1Clause::Members, D1Clause::Caps, D1Clause::Provenance, D1Clause::ControlBytes]
        .map(D1Clause::id)
        .to_vec();
    assert_eq!(ids, ["D1.0", "D1.1", "D1.2", "D1.3", "D1.4", "D1.5", "D1.6", "D1.7", "D1.8", "D1.9", "D1.10", "D1.11"]);
}

// ---- G-B and G-C -------------------------------------------------------------

#[test]
fn every_phase_fact_admits_its_cap_and_refuses_cap_plus_one() {
    let caps = phase_caps();
    let late: [PhaseFact; LATE_FACTS] = [PhaseFact::BuiltNodes, PhaseFact::BuiltMembers, PhaseFact::BuiltFrameElements, PhaseFact::BuiltSupports,
        PhaseFact::CaseLoads, PhaseFact::Restrained, PhaseFact::Springs, PhaseFact::Materials, PhaseFact::LateObservationBytes];
    let observed = |facts: &[PhaseFact], values: &[u64]| facts.iter().zip(values).map(|(f, v)| PhaseObservation { fact: *f, observed: *v }).collect::<Vec<_>>();
    let at: [PhaseObservation; LATE_FACTS] = observed(&late, &caps.late).try_into().unwrap();
    assert_eq!(check_phase(PhaseGate::Late, &at, &caps.late), Ok(()));
    for i in 0..LATE_FACTS {
        let mut over = at;
        over[i].observed += 1;
        assert_eq!(check_phase(PhaseGate::Late, &over, &caps.late),
            Err(PhaseRefusal { gate: PhaseGate::Late, fact: late[i], observed: caps.late[i] + 1, cap: caps.late[i] }));
    }
    assert_eq!(caps.late[..8], [32, 32, 32, 32, 128, 192, 192, 8], "D1's counts: n, m, m, g, l, k = min(6n, r), s, 4 + 4");
    assert_eq!(P_FINAL, 2_115);
    assert_eq!(caps.complete[2], 2 * 2_115 * 11_474, "2·P_final·Text(row)");
    assert_eq!(caps.complete[5], 137_419_080, "2·Text(diag_env) at l ≤ 128 (API_G4.md, S-6(d))");
    assert_eq!((caps.complete[6], caps.complete[7]), (2_599_962, 2_330), "L_PUB (RV84 C-N1) and L_DIAGID (RV87 N-3)");
    assert_eq!(caps.complete[17], 97 * 16_384, "(3m + 1)·Text(err)");
    let complete_facts: Vec<PhaseFact> = complete_observations_of_milestone().iter().map(|o| o.fact).collect();
    let at: [PhaseObservation; COMPLETE_FACTS] = observed(&complete_facts, &caps.complete).try_into().unwrap();
    assert_eq!(check_phase(PhaseGate::Complete, &at, &caps.complete), Ok(()));
    for i in 0..COMPLETE_FACTS {
        let mut over = at;
        over[i].observed += 1;
        assert_eq!(check_phase(PhaseGate::Complete, &over, &caps.complete).unwrap_err().fact, complete_facts[i]);
    }
}
fn complete_observations_of_milestone() -> [PhaseObservation; COMPLETE_FACTS] {
    let raw = milestone();
    let mode = PreviewSolverMode::SparseInteractive;
    let (request, capture) = CapturedInvocation::parse(raw, mode).unwrap();
    let mut observer = crate::retained_product::ProductCapture::prepared_probe();
    let ordinary = crate::run_linear_static_preview_observed(request, mode, Some(&capture), &mut crate::SourceRecoveryBudget::default(), Some(&mut observer));
    complete_observations(&CompleteFacts { ordinary: &ordinary, capture: &observer })
}

#[test]
fn complete_facts_read_the_actual_owners() {
    let raw = milestone();
    for mode in MODES {
        let (request, capture) = CapturedInvocation::parse(raw.clone(), mode).unwrap();
        let mut observer = crate::retained_product::ProductCapture::prepared_probe();
        let ordinary = crate::run_linear_static_preview_observed(request, mode, Some(&capture), &mut crate::SourceRecoveryBudget::default(), Some(&mut observer));
        let o = complete_observations(&CompleteFacts { ordinary: &ordinary, capture: &observer });
        let get = |fact| o.iter().find(|x| x.fact == fact).unwrap().observed;
        assert_eq!(get(PhaseFact::EnvelopeResults), ordinary.results.len() as u64);
        assert_eq!(get(PhaseFact::EnvelopeDiagnostics), ordinary.diagnostics.len() as u64);
        // Independent sums of every String the rows and diagnostics own.
        let cap = |s: &String| s.capacity();
        let vec_text = |v: &Vec<String>| v.capacity() * std::mem::size_of::<String>() + v.iter().map(cap).sum::<usize>();
        let rows: usize = ordinary.results.iter().map(|r| {
            [&r.id, &r.kind, &r.unit, &r.entity_ref].map(cap).iter().sum::<usize>() + vec_text(&r.source_result_refs)
                + r.basis_ref.as_ref().map_or(0, |b| cap(&b.ref_type) + cap(&b.ref_id))
                + r.metadata.as_ref().map_or(0, |m| [&m.component, &m.coordinate_system, &m.location, &m.basis, &m.sign_convention].map(cap).iter().sum())
        }).sum();
        assert_eq!(get(PhaseFact::EnvelopeResultTextBytes), rows as u64);
        let diagnostics: usize = ordinary.diagnostics.iter().map(|d| {
            [&d.id, &d.code, &d.severity, &d.message].map(cap).iter().sum::<usize>() + d.source.as_ref().map_or(0, cap) + vec_text(&d.affected_refs)
        }).sum();
        assert_eq!(get(PhaseFact::EnvelopeDiagnosticTextBytes), diagnostics as u64);
        let longest = ordinary.results.iter().flat_map(|r| [&r.id, &r.kind, &r.unit, &r.entity_ref]).chain(ordinary.diagnostics.iter().flat_map(|d| [&d.id, &d.code, &d.severity, &d.message]))
            .map(String::len).max().unwrap();
        assert!(get(PhaseFact::EnvelopeMaxStringBytes) >= longest as u64);
        let message = ordinary.diagnostics.iter().map(|d| d.message.len()).max().unwrap();
        assert!(get(PhaseFact::EnvelopeMaxStringBytes) >= message as u64 && message > 0);
        assert_eq!(get(PhaseFact::DiagnosticIdMaxBytes), ordinary.diagnostics.iter().map(|d| d.id.len()).max().unwrap() as u64);
        assert_eq!(get(PhaseFact::EnvelopeResultCapacity), ordinary.results.capacity() as u64);
        assert_eq!(get(PhaseFact::EnvelopeDiagnosticCapacity), ordinary.diagnostics.capacity() as u64);
        let census = borrowed_value_census(ordinary.contract_evidence.as_ref().unwrap());
        assert_eq!((get(PhaseFact::ContractEvidenceArrayElements), get(PhaseFact::ContractEvidenceObjects), get(PhaseFact::ContractEvidenceEntries),
            get(PhaseFact::ContractEvidenceStringBytes), get(PhaseFact::ContractEvidenceKeyBytes)),
            (census.array_capacity_elements as u64, census.objects as u64, census.object_entries as u64, census.string_capacity_bytes as u64, census.key_capacity_bytes as u64));
        let seeds = observer.ordinary.capacity() * std::mem::size_of::<crate::retained_product::OrdinarySeed>()
            + observer.ordinary.iter().map(|s| s.case.capacity() + s.d5_diagnostic_ref.as_ref().map_or(0, cap)).sum::<usize>();
        assert_eq!(get(PhaseFact::OrdinarySeedBytes), seeds as u64);
        // A source-block recovery present at G-C is observed (permitted_run checks it first).
        let mut selected = ordinary.clone();
        selected.source_block_recovery = Some(json!({}));
        let s = complete_observations(&CompleteFacts { ordinary: &selected, capture: &observer });
        assert_eq!(s.iter().find(|x| x.fact == PhaseFact::SourceBlockRecovery).unwrap().observed, 1);
        // An incomplete preview-tree census is observed as such.
        let mut deep = ordinary.clone();
        let mut v = Value::Null;
        for _ in 0..DEPTH_LIMIT + 1 {
            v = Value::Array(vec![v]);
        }
        deep.contract_evidence = Some(v);
        let d = complete_observations(&CompleteFacts { ordinary: &deep, capture: &observer });
        assert_eq!(d.iter().find(|x| x.fact == PhaseFact::ContractEvidenceStatus).unwrap().observed, 1);
        // An association error's text is retained error text (C-N4).
        let mut failed = crate::retained_product::ProductCapture::prepared_probe();
        failed.error = Some(crate::retained_product::CaptureError::Association(String::with_capacity(40)));
        failed.observable_error = Some(crate::retained_product::CaptureError::Association(String::with_capacity(9)));
        let e = complete_observations(&CompleteFacts { ordinary: &ordinary, capture: &failed });
        assert_eq!(e.iter().find(|x| x.fact == PhaseFact::RetainedErrorTextBytes).unwrap().observed, 49);
        assert_eq!(get(PhaseFact::SourceBlockRecovery), 0);
        assert_eq!(get(PhaseFact::ContractEvidenceStatus), 0);
        assert!(get(PhaseFact::ContractEvidenceEntries) > 0, "the preview tree");
        assert!(get(PhaseFact::ObservationBytes) > 0, "the capture's own tally");
        assert!(get(PhaseFact::OrdinarySeedBytes) >= std::mem::size_of::<crate::retained_product::OrdinarySeed>() as u64);
        assert_eq!(get(PhaseFact::RetainedErrorTextBytes), 0);
        // The count and text facts sit well inside their bounds for the milestone.
        let caps = phase_caps().complete;
        for (x, cap) in o.iter().zip(caps) {
            if cap != UNPRICED || x.observed == 0 {
                assert!(x.observed <= cap, "{:?}: {} > {}", x.fact, x.observed, cap);
            }
        }
    }
}

// ---- S1 and the budgets --------------------------------------------------------

#[test]
fn reserved_stack_is_r_with_a_test_override() {
    assert_eq!((RESERVED_STACK_BYTES, STACK_WITNESS_DIVISOR), (64 << 20, 16));
    assert_eq!(reserved_stack(), RESERVED_STACK_BYTES);
    RESERVED_STACK_OVERRIDE.with(|c| c.set(Some(RESERVED_STACK_BYTES / STACK_WITNESS_DIVISOR)));
    assert_eq!(reserved_stack(), 4 << 20);
    RESERVED_STACK_OVERRIDE.with(|c| c.set(None));
    assert_eq!(reserved_stack(), RESERVED_STACK_BYTES);
}

#[test]
fn structural_budgets_are_u3s() {
    let b = PHASE_BUDGETS;
    assert_eq!((b.ordinary_runs, b.parses_per_invocation, b.fallible_allocations_after_first_mutation, b.fallback_new_allocations), (1, 1, 0, 0));
    assert_eq!(b.reserved_stack_bytes, RESERVED_STACK_BYTES as u64);
    assert_eq!(b.thread_heap_bytes, 8192 + std::mem::size_of::<crate::RetainedPreviewOutput>() as u64);
    let diagnostic = std::mem::size_of::<crate::Diagnostic>() as u64;
    assert!(b.notice_reserve_bytes >= diagnostic + 196, "the slot and the 196-byte message reservation");
    assert!(b.notice_reserve_bytes <= 2_048, "G4's push-growth figure tightened to grant 1b's exact reservation");
}

#[test]
fn late_facts_read_the_actual_owners() {
    let raw = milestone();
    let mode = PreviewSolverMode::SparseInteractive;
    let (request, capture) = CapturedInvocation::parse(raw, mode).unwrap();
    let mut diagnostics = Vec::new();
    // The dispatch builds with the model's materials when the request supplies none.
    let built = crate::build_model(&request.model, &request.model.materials, &mut diagnostics).expect("the milestone builds");
    let mut observer = crate::retained_product::ProductCapture::prepared_probe();
    let model = request.model.clone();
    let _ = crate::run_linear_static_preview_observed(request, mode, Some(&capture), &mut crate::SourceRecoveryBudget::default(), Some(&mut observer));
    let restrained = [0usize, 1, 2, 3, 4, 5, 6];
    let springs: [crate::SpringEntry; 0] = [];
    let materials = &model.materials;
    let o = late_observations(&LateFacts {
        model: &model,
        built: &built,
        materials,
        case: &model.load_cases[0],
        restrained: &restrained,
        springs: &springs,
        capture: &observer,
    });
    let get = |fact| o.iter().find(|x| x.fact == fact).unwrap().observed;
    assert_eq!(get(PhaseFact::BuiltNodes), built.nodes.len() as u64);
    assert_eq!(get(PhaseFact::BuiltMembers), built.pipes.len() as u64);
    assert_eq!(get(PhaseFact::BuiltFrameElements), built.frame_elements.len() as u64);
    assert_eq!(get(PhaseFact::BuiltSupports), built.supports.len() as u64);
    assert_eq!(get(PhaseFact::CaseLoads), 3);
    assert_eq!(get(PhaseFact::Restrained), 7);
    assert_eq!(get(PhaseFact::Springs), 0);
    assert_eq!(get(PhaseFact::Materials), materials.len() as u64);
    assert!(get(PhaseFact::LateObservationBytes) > 0);
    assert_eq!(get(PhaseFact::LateObservationBytes),
        observer.adapter.counts.get()[crate::retained_product::AdapterEvent::RustCapacityBytes as usize]);
    // The milestone's distinct counts tell the readers apart.
    assert_eq!((built.nodes.len(), built.pipes.len(), built.frame_elements.len(), built.supports.len()), (2, 1, 1, 4), "pipes and frame elements coincide in D1 (straight members)");
    assert_eq!(check_phase(PhaseGate::Late, &o, &{ let mut c = phase_caps().late; c[LATE_FACTS - 1] = u64::MAX; c }), Ok(()));
}
