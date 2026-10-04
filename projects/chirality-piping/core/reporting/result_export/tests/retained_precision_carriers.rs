//! I66 U6a: the F2a preview successor carried through the Rust carriers
//! (dispatch, standing, binding refusal, classification summary and the
//! canonical derivative) and back out. The inputs are byte-identical copies of
//! PP's pinned milestone successor files (D-U6-5), checked by sha256 here. They
//! are producer test outputs, not native Current evidence. Eligibility stays
//! held, so standing is `needs_recompute` (D-U6-6); U7 owns the switch.
use open_pipe_stress_result_export::{
    derivative as d, retained_precision as rp, semantic_contract as s, source_blocks,
};
use serde_json::{json, Value};
use sha2::{Digest, Sha256};

const SPARSE: &str = include_str!(
    "../../../../fixtures/results/retained_precision_milestone_successor_sparse_interactive.json"
);
const DENSE: &str = include_str!(
    "../../../../fixtures/results/retained_precision_milestone_successor_dense_scrutiny.json"
);
/// PP's pins: retained_facade_tests.rs `PINNED` and retained_wire_tests.rs
/// `SUCCESSOR_SHA256` (file sha256, then receipt sha256), per mode.
const PINNED: [(&str, &str, &str, &str); 2] = [
    (
        "sparse_interactive",
        SPARSE,
        "ac6986b0680e0df9d88c33a5bf4635372fc3b83cbb9080da44e6d32dbdca59dc",
        "efc1a39bbe83840df6bd0761c932b8020285d3b8c005ba8fd0b45ba10d667494",
    ),
    (
        "dense_scrutiny",
        DENSE,
        "6cd1d249e5352aaffbd2b7d7349c74a1d0e0572df35500f66be49c3cad95c9b5",
        "3e26499f17caff8f5fc0d46406bbe54acf43e8cb16e761784aa5074413b0ac4a",
    ),
];
/// The milestone's validated class counts (R/I61 experiment 02; RV86 recount):
/// relative, absolute, input-derived, non-quantity.
const CLASSES: [(&str, [u64; 4]); 2] = [
    ("sparse_interactive", [25, 69, 3, 1]),
    ("dense_scrutiny", [25, 69, 3, 2]),
];

struct Milestone {
    mode: &'static str,
    source: Value,
    invocation: Value,
}
fn milestones() -> Vec<Milestone> {
    PINNED
        .iter()
        .map(|(mode, text, file_sha, receipt_sha)| {
            assert_eq!(
                format!("{:x}", Sha256::digest(text.as_bytes())),
                *file_sha,
                "{mode}: PP's pinned successor file bytes"
            );
            let doc: Value = serde_json::from_str(text).unwrap();
            assert_eq!(doc["source"]["retained_precision"]["receipt_sha256"], *receipt_sha);
            assert_eq!(doc["invocation"]["solver_mode"], *mode);
            assert_eq!(doc["source"]["producer"]["semantic_contract_id"], s::PREVIEW_PHYSICS_RETAINED_ID);
            Milestone {
                mode,
                source: doc["source"].clone(),
                invocation: doc["invocation"].clone(),
            }
        })
        .collect()
}
fn requested(invocation: &Value) -> Vec<Value> {
    invocation["request"]["model"]["load_cases"]
        .as_array()
        .unwrap()
        .iter()
        .map(|c| json!({"ref_type":"load_case","ref_id":c["id"]}))
        .collect()
}
fn derive_with(raw: &Value, mut base: Value) -> Result<Value, String> {
    let model = raw["model_ref"].as_str().unwrap();
    let carrier = d::checksum(
        raw,
        "attested_headless_producer_carrier",
        d::reference("test_carrier", "preview-physics-retained"),
    )?;
    let origin = json!({"origin_id":"retained-precision-carrier-test","origin_class":"attested_headless_producer","qualification_ref":d::reference("test_fixture","not-authentication"),"authentic_producer_available":true,"received_carrier_checksum":carrier,"original_producer_checksum":carrier,"origin_limit":"Pinned producer test bytes; carrier contract test only","actual_model_ref":d::reference("model_payload",model),"mechanics_run_ref":d::reference("mechanics_run",raw["run_id"].as_str().unwrap()),"request_model_ref":null,"request_run_ref":null,"request_alias_disclosure":null});
    base["result_envelope"]["envelope_id"] = json!("envelope:retained-precision-carrier-test");
    d::derive_document(base, &json!({"project":{"id":model}}), raw, origin, None)
}
fn base_document() -> Value {
    serde_json::from_str(include_str!(
        "../../../../fixtures/results/invented/tp_phys_015_canonical_solve_result_envelope.json"
    ))
    .unwrap()
}
fn derive(raw: &Value) -> Result<Value, String> {
    derive_with(raw, base_document())
}
/// Recompute the publication and receipt hashes after an edit (a forged but
/// hash-consistent statement), so the edit reaches the gate it targets.
fn rehash(mut raw: Value) -> Value {
    let mut public = raw.clone();
    public.as_object_mut().unwrap().remove("retained_precision");
    raw["retained_precision"]["body"]["publication_sha256"] =
        json!(source_blocks::domain_hash("retained_precision_publication_mp_v2", &public).unwrap());
    let body = raw["retained_precision"]["body"].clone();
    raw["retained_precision"]["receipt_sha256"] =
        json!(source_blocks::domain_hash("retained_precision_receipt_mp_v2", &body).unwrap());
    raw
}
/// The reader's G7 projection: the same document under the base identity.
fn projected_base(raw: &Value) -> Value {
    let mut base = raw.clone();
    base.as_object_mut().unwrap().remove("retained_precision");
    base["producer"]["semantic_contract_id"] = json!(s::PREVIEW_PHYSICS_ID);
    base["formulation_basis"]["profile_id"] = json!("product_preview_mechanics_v1");
    for row in base["results"].as_array_mut().unwrap() {
        row.as_object_mut().unwrap().remove("recovery_method");
    }
    base
}
fn disclosure_reasons(doc: &Value) -> Vec<(String, String)> {
    doc["result_envelope"]["row_disclosures"]
        .as_array()
        .unwrap()
        .iter()
        .map(|x| {
            (
                x["source_result_id"].as_str().unwrap().to_string(),
                x["reason_code"].as_str().unwrap().to_string(),
            )
        })
        .collect()
}
fn out_dir() -> Option<std::path::PathBuf> {
    std::env::var("I66_U6A_OUT").ok().map(std::path::PathBuf::from)
}

#[test]
fn u6a_dispatch_admits_the_successor_through_the_accepted_reader_only() {
    for m in milestones() {
        let (table, version) = s::for_source(&m.source).unwrap_or_else(|e| panic!("{}: {e}", m.mode));
        assert_eq!((table["semantic_contract_id"].as_str(), version), (Some(s::PREVIEW_PHYSICS_RETAINED_ID), "0.3.0"));
        assert!(std::ptr::eq(table, s::preview_physics_retained_contract()));
        let (meta, meta_version) = s::for_source_metadata(&m.source).unwrap();
        assert!(std::ptr::eq(meta, table) && meta_version == "0.3.0");
        assert!(s::is_fresh_identity(s::PREVIEW_PHYSICS_RETAINED_ID));
        assert_eq!(s::standing_reason(&m.source), None);
        // The dispatch is the reader's: a statement it refuses is refused here
        // with the reader's first code, raw and transport alike.
        let mut broken = m.source.clone();
        broken["retained_precision"]["receipt_sha256"] = json!("0".repeat(64));
        assert_eq!(s::for_source(&broken).unwrap_err(), "RETAINED_PRECISION_RECEIPT_MISMATCH");
        assert_eq!(s::for_source_metadata(&broken).unwrap_err(), "RETAINED_PRECISION_RECEIPT_MISMATCH");
        // A G7 failure keeps the base validator's own text (its detail).
        let mut evidence = m.source.clone();
        evidence["contract_evidence"]["combination_gates"] = json!("not-an-array");
        let evidence = rehash(evidence);
        let reader = rp::validate(&evidence, None).unwrap_err();
        assert_eq!(reader.gate, "G7", "{reader:?}");
        let error = s::for_source(&evidence).unwrap_err();
        assert_eq!(Some(error.clone()), reader.detail.clone().or(Some(reader.code.clone())));
        assert!(error.starts_with(&reader.code), "{error}");
        // A G7 failure with detail text keeps the whole text, not only the code.
        let mut unit = m.source.clone();
        let index = unit["results"].as_array().unwrap().iter().position(|r| r["kind"] == "linear_solver_mode_basis").unwrap();
        unit["results"][index]["unit"] = json!("m");
        let unit = rehash(unit);
        let reader = rp::validate(&unit, None).unwrap_err();
        assert_eq!(reader.gate, "G7", "{reader:?}");
        let detail = reader.detail.clone().expect("a detail-bearing base failure");
        assert_ne!(detail, reader.code);
        assert_eq!(s::for_source(&unit).unwrap_err(), detail);
        assert_eq!(s::numerical_use_standing(&unit, &requested(&m.invocation)), "unsupported");
    }
    let table = include_bytes!("../../../../fixtures/results/semantic_contract_v0_3_preview_physics_retained_1.json");
    assert_eq!(s::verify_preview_physics_retained_table(table).unwrap(), *s::preview_physics_retained_contract());
    // The same JSON value with other bytes is not the pinned table.
    let mut spaced = table.to_vec();
    spaced.push(b' ');
    assert_eq!(s::verify_preview_physics_retained_table(&spaced).unwrap_err(), "SOURCE_PREVIEW_PHYSICS_RETAINED_TABLE_HASH");
    assert_eq!(s::verify_preview_physics_retained_table(b"{}").unwrap_err(), "SOURCE_PREVIEW_PHYSICS_RETAINED_TABLE_HASH");
}

#[test]
fn u6a_standing_is_needs_recompute_and_comes_only_from_the_receipt() {
    for m in milestones() {
        let refs = requested(&m.invocation);
        assert_eq!(s::numerical_use_standing(&m.source, &refs), "needs_recompute");
        assert_eq!(
            s::numerical_use_standing_with_context(&m.source, &refs, Some(&m.invocation)),
            "needs_recompute",
            "{}: eligibility held",
            m.mode
        );
        let validation = rp::validate(&m.source, Some(&m.invocation)).unwrap();
        assert!(validation.invocation_bound && !validation.numerical_eligible);
        // An edited covered row or a foreign invocation is unsupported.
        let mut row = m.source.clone();
        row["results"][0]["value"] = json!(row["results"][0]["value"].as_f64().unwrap() * 2.0 + 1.0);
        assert_eq!(s::numerical_use_standing(&row, &refs), "unsupported");
        assert_eq!(s::numerical_use_standing_with_context(&row, &refs, Some(&m.invocation)), "unsupported");
        let mut foreign = m.invocation.clone();
        foreign["solver_mode"] = json!(if m.mode == "sparse_interactive" { "dense_scrutiny" } else { "sparse_interactive" });
        assert_eq!(s::numerical_use_standing_with_context(&m.source, &refs, Some(&foreign)), "unsupported");
        // numerical_quality never contributes: a hash-consistent statement whose
        // selected case claims checks_passed is refused by the reader (D6b), and
        // is never read by the ordinary branch (which would call it eligible).
        let mut claimed = m.source.clone();
        claimed["numerical_quality"]["status"] = json!("checks_passed");
        claimed["numerical_quality"]["cases"][0]["solve_quality"] = json!("checks_passed");
        claimed["numerical_quality"]["cases"][0]["structural_status"] = json!("passive_model_basis");
        claimed["numerical_quality"]["cases"][0]["model_matrix_fidelity"] = json!("represented_equations_retained");
        let claimed = rehash(claimed);
        assert!(rp::validate(&claimed, None).is_err());
        assert_eq!(s::numerical_use_standing(&claimed, &refs), "unsupported");
        assert_eq!(s::numerical_use_standing_with_context(&claimed, &refs, Some(&m.invocation)), "unsupported");
    }
}

/// The post-U7 rule, exercised now through the test seam with a validation
/// whose eligibility is set; the flags themselves are untouched.
#[test]
fn u6a_standing_rule_conjuncts_with_eligibility_set() {
    let m = &milestones()[0];
    let refs = requested(&m.invocation);
    let mut validation = rp::validate(&m.source, Some(&m.invocation)).unwrap();
    validation.numerical_eligible = true;
    assert_eq!(s::retained_standing_from(&validation, &m.source, &refs), "numerically_eligible");
    let held = rp::Validation { numerical_eligible: false, ..validation.clone() };
    assert_eq!(s::retained_standing_from(&held, &m.source, &refs), "needs_recompute");
    let unbound = rp::Validation { invocation_bound: false, ..validation.clone() };
    assert_eq!(s::retained_standing_from(&unbound, &m.source, &refs), "needs_recompute");
    assert_eq!(s::retained_standing_from(&validation, &m.source, &[]), "needs_recompute");
    let other = vec![json!({"ref_type":"load_case","ref_id":"other"})];
    assert_eq!(s::retained_standing_from(&validation, &m.source, &other), "needs_recompute");
    let mut extra = refs.clone();
    extra.push(json!({"ref_type":"load_case","ref_id":"other"}));
    assert_eq!(s::retained_standing_from(&validation, &m.source, &extra), "needs_recompute");
    let mut unsolved = m.source.clone();
    unsolved["status"]["mechanics"] = json!("MODEL_INCOMPLETE");
    assert_eq!(s::retained_standing_from(&validation, &unsolved, &refs), "needs_recompute");
    // A not_required case must be ordinarily eligible by the base rules (F-7).
    let mut not_required = m.source.clone();
    not_required["retained_precision"]["body"]["cases"][0]["status"] = json!("not_required");
    let q = &mut not_required["numerical_quality"]["cases"][0];
    q["solve_quality"] = json!("checks_passed");
    q["structural_status"] = json!("passive_model_basis");
    q["model_matrix_fidelity"] = json!("represented_equations_retained");
    q["accuracy_evidence"] = json!("not_claimed");
    assert!(q["evidence_refs"].as_array().is_some_and(|r| !r.is_empty()));
    assert_eq!(s::retained_standing_from(&validation, &not_required, &refs), "numerically_eligible");
    for (field, value) in [
        ("solve_quality", json!("sensitive")),
        ("structural_status", json!("numerically_unresolved")),
        ("model_matrix_fidelity", json!("assembly_uncertainty")),
        ("accuracy_evidence", json!("unresolved")),
        ("evidence_refs", json!([])),
        ("evidence_refs", json!(["diagnostic:absent"])),
        ("basis_ref", json!({"ref_type":"load_case","ref_id":"other"})),
    ] {
        let mut bad = not_required.clone();
        bad["numerical_quality"]["cases"][0][field] = value;
        assert_eq!(s::retained_standing_from(&validation, &bad, &refs), "needs_recompute", "{field}");
    }
    let mut duplicate = not_required.clone();
    let first = duplicate["results"][0].clone();
    duplicate["results"].as_array_mut().unwrap().push(first);
    assert_eq!(s::retained_standing_from(&validation, &duplicate, &refs), "needs_recompute");
    let mut short = not_required.clone();
    short["numerical_quality"]["cases"] = json!([]);
    assert_eq!(s::retained_standing_from(&validation, &short, &refs), "needs_recompute");
    // Any other case status (unavailable, or unknown) is never eligible.
    for status in ["unavailable", "other"] {
        let mut case = m.source.clone();
        case["retained_precision"]["body"]["cases"][0]["status"] = json!(status);
        assert_eq!(s::retained_standing_from(&validation, &case, &refs), "needs_recompute", "{status}");
    }
}

#[test]
fn u6a_derivative_carries_the_receipt_and_it_comes_back_out() {
    for m in milestones() {
        let doc = derive(&m.source).unwrap_or_else(|e| panic!("{}: {e}", m.mode));
        d::validate_document(&doc, &m.source).unwrap();
        let e = &doc["result_envelope"];
        // The receipt travels whole and byte-equal; the evidence and identity too.
        assert_eq!(e["retained_precision"], m.source["retained_precision"]);
        assert_eq!(
            serde_json::to_vec(&e["retained_precision"]).unwrap(),
            serde_json::to_vec(&m.source["retained_precision"]).unwrap()
        );
        assert_eq!(e["contract_evidence"], m.source["contract_evidence"]);
        assert_eq!(e["semantic_contract_ref"]["ref_id"], s::PREVIEW_PHYSICS_RETAINED_ID);
        for key in ["producer", "numerical_quality", "formulation_basis"] {
            assert_eq!(e[key], m.source[key]);
        }
        // Back out: the carried receipt authenticates the raw publication again,
        // with the invocation, and classifies every row exactly as before.
        let before = rp::validate(&m.source, Some(&m.invocation)).unwrap();
        let mut back = m.source.clone();
        back["retained_precision"] = e["retained_precision"].clone();
        let after = rp::validate(&back, Some(&m.invocation)).unwrap();
        assert_eq!(after, before);
        assert!(!after.numerical_eligible);
        // Transport: the derivative's metadata view is G0-G2 valid, never eligible.
        let view = json!({"schema_version":"0.2.0","producer":e["producer"],"numerical_quality":e["numerical_quality"],"formulation_basis":e["formulation_basis"],"contract_evidence":e["contract_evidence"],"retained_precision":e["retained_precision"]});
        let transport = rp::validate_transport_metadata(&view).unwrap();
        assert!(!transport.numerical_eligible && !transport.invocation_bound);
        assert_eq!(transport.publication_sha256, before.publication_sha256);
        assert!(s::for_source_metadata(&view).is_ok());
        // Every row's disposition is the base disposition, except that each
        // absolute_verified or not_covered row is disclosed with its class.
        let base = derive(&projected_base(&m.source)).unwrap();
        let reasons: std::collections::HashMap<_, _> = disclosure_reasons(&doc).into_iter().collect();
        let base_accounting = base["result_envelope"]["row_accounting"].as_array().unwrap();
        let accounting = e["row_accounting"].as_array().unwrap();
        assert_eq!(accounting.len(), m.source["results"].as_array().unwrap().len());
        let mut counts = [0u64; 4];
        for c in &before.classifications {
            let i = m.source["results"].as_array().unwrap().iter().position(|r| r["id"] == c.result_id.as_str()).unwrap();
            match c.class {
                rp::AccuracyClass::AbsoluteVerified { bound_bits } => {
                    counts[1] += 1;
                    assert_eq!(accounting[i]["disposition"], "disclosed");
                    assert_eq!(reasons[&c.result_id], d::RETAINED_ABSOLUTE_VERIFIED);
                    let x = doc["result_envelope"]["row_disclosures"].as_array().unwrap().iter().find(|x| x["source_result_id"] == c.result_id.as_str()).unwrap();
                    let message = x["message"].as_str().unwrap();
                    assert!(message.contains(&format!("{bound_bits:016x}")) && message.contains("absolute bound"), "{message}");
                    assert!(!message.contains("stop") && !message.contains("enclos"), "{message}");
                    assert_eq!(x["source_value"], m.source["results"][i]["value"]);
                }
                rp::AccuracyClass::NotCovered => panic!("the milestone has no not_covered row"),
                ref other => {
                    counts[match other { rp::AccuracyClass::RelativeVerified => 0, rp::AccuracyClass::InputDerived => 2, _ => 3 }] += 1;
                    assert_eq!(accounting[i]["disposition"], base_accounting[i]["disposition"], "{}", c.result_id);
                    if let Some(reason) = reasons.get(&c.result_id) {
                        assert!(!reason.starts_with("retained_precision_"), "{reason}");
                    }
                }
            }
        }
        let expected = CLASSES.iter().find(|(mode, _)| *mode == m.mode).unwrap().1;
        assert_eq!(counts, expected, "{}", m.mode);
        // Withholding never touches the received values: every disclosure keeps
        // the source value and unit.
        assert_eq!(
            reasons.values().filter(|r| r.as_str() == d::RETAINED_ABSOLUTE_VERIFIED).count() as u64,
            expected[1]
        );
        if let Some(dir) = out_dir() {
            std::fs::create_dir_all(&dir).unwrap();
            std::fs::write(dir.join(format!("derivative_{}.json", m.mode)), serde_json::to_vec_pretty(&doc).unwrap()).unwrap();
        }
    }
}

#[test]
fn u6a_receipt_binding_mismatches_are_refused() {
    for m in milestones() {
        let doc = derive(&m.source).unwrap();
        let mut dropped = doc.clone();
        dropped["result_envelope"].as_object_mut().unwrap().remove("retained_precision");
        assert_eq!(d::validate_document(&dropped, &m.source).unwrap_err(), d::RETAINED_PRECISION_RECEIPT_BINDING_MISMATCH);
        let mut altered = doc.clone();
        altered["result_envelope"]["retained_precision"]["body"]["work"]["charged"] = json!(1);
        assert_eq!(d::validate_document(&altered, &m.source).unwrap_err(), d::RETAINED_PRECISION_RECEIPT_BINDING_MISMATCH);
        let disclosures = |doc: &mut Value| -> Vec<Value> { doc["result_envelope"]["row_disclosures"].as_array().unwrap().clone() };
        let mut plain = doc.clone();
        let index = disclosures(&mut plain).iter().position(|x| x["reason_code"] == d::RETAINED_ABSOLUTE_VERIFIED).unwrap();
        // A class disclosure must state exactly its code and message.
        let mut code = doc.clone();
        code["result_envelope"]["row_disclosures"][index]["reason_code"] = json!("diagnostic_evidence_not_physical_quantity");
        assert_eq!(d::validate_document(&code, &m.source).unwrap_err(), "DISCLOSURE_SEMANTICS_MISMATCH");
        let mut message = doc.clone();
        message["result_envelope"]["row_disclosures"][index]["message"] = json!("relabelled");
        assert_eq!(d::validate_document(&message, &m.source).unwrap_err(), "DISCLOSURE_SEMANTICS_MISMATCH");
        let mut class = doc.clone();
        class["result_envelope"]["row_disclosures"][index]["reason_code"] = json!(d::RETAINED_NOT_COVERED);
        assert_eq!(d::validate_document(&class, &m.source).unwrap_err(), "DISCLOSURE_SEMANTICS_MISMATCH");
        // No other disclosure may claim a class code.
        let other = disclosures(&mut plain).iter().position(|x| !x["reason_code"].as_str().unwrap().starts_with("retained_precision_")).unwrap();
        for code in [d::RETAINED_ABSOLUTE_VERIFIED, d::RETAINED_NOT_COVERED] {
            let mut claim = doc.clone();
            claim["result_envelope"]["row_disclosures"][other]["reason_code"] = json!(code);
            assert_eq!(d::validate_document(&claim, &m.source).unwrap_err(), "DISCLOSURE_SEMANTICS_MISMATCH", "{code}");
        }
        // A document validated against a different statement fails before any row.
        let mut other_source = m.source.clone();
        other_source["retained_precision"]["receipt_sha256"] = json!("1".repeat(64));
        assert_eq!(d::validate_document(&doc, &other_source).unwrap_err(), "RETAINED_PRECISION_RECEIPT_MISMATCH");
    }
}

#[test]
fn u6a_downgrades_to_a_base_identity_are_refused() {
    for m in milestones() {
        // F-5: the successor offered as preview-physics-1, keeping its receipt.
        let mut relabelled = m.source.clone();
        relabelled["producer"]["semantic_contract_id"] = json!(s::PREVIEW_PHYSICS_ID);
        relabelled["formulation_basis"]["profile_id"] = json!("product_preview_mechanics_v1");
        assert_eq!(s::for_source(&relabelled).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
        assert_eq!(s::for_source_metadata(&relabelled).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
        assert_eq!(s::numerical_use_standing(&relabelled, &requested(&m.invocation)), "unsupported");
        assert_eq!(derive(&relabelled).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
        // ... with the receipt dropped but the method token kept on its rows.
        let mut tokens = relabelled.clone();
        tokens.as_object_mut().unwrap().remove("retained_precision");
        assert_eq!(s::for_source(&tokens).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
        assert_eq!(s::numerical_use_standing(&tokens, &requested(&m.invocation)), "unsupported");
        // ... and an absent-but-present member (null) is still a member.
        let mut null = projected_base(&m.source);
        null["retained_precision"] = Value::Null;
        assert_eq!(s::for_source(&null).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
        // The reader's own projection is the unchanged base document.
        let base = projected_base(&m.source);
        assert_eq!(s::for_source(&base).unwrap().0["semantic_contract_id"], s::PREVIEW_PHYSICS_ID);
        // A base derivative cannot be given a receipt, before or after derivation.
        let mut seeded = base_document();
        seeded["result_envelope"]["retained_precision"] = m.source["retained_precision"].clone();
        assert_eq!(derive_with(&base, seeded).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
        let mut doc = derive(&base).unwrap();
        d::validate_document(&doc, &base).unwrap();
        doc["result_envelope"]["retained_precision"] = m.source["retained_precision"].clone();
        assert_eq!(d::validate_document(&doc, &base).unwrap_err(), s::RETAINED_PRECISION_DOWNGRADE_FORBIDDEN);
    }
}

#[test]
fn u6a_binding_refusal_follows_the_validated_class_only() {
    for m in milestones() {
        let validation = rp::validate(&m.source, None).unwrap();
        let rows = m.source["results"].as_array().unwrap();
        for c in &validation.classifications {
            let row = rows.iter().find(|r| r["id"] == c.result_id.as_str()).unwrap();
            let expected = match c.class {
                rp::AccuracyClass::AbsoluteVerified { .. } => Some(s::RULE_QUANTITY_BELOW_VERIFIED_FLOOR),
                rp::AccuracyClass::NotCovered => Some(s::RULE_QUANTITY_NOT_COVERED),
                _ => None,
            };
            assert_eq!(s::rule_binding_refusal(&m.source, row), expected, "{}", c.result_id);
        }
        // A headline binds the row its result_ref names.
        for key in ["max_displacement", "max_open_formula_stress"] {
            let Some(id) = m.source["summary"][key]["result_ref"].as_str() else { continue };
            let row = rows.iter().find(|r| r["id"] == id).unwrap();
            let class = &validation.classifications.iter().find(|c| c.result_id == id).unwrap().class;
            let refused = matches!(class, rp::AccuracyClass::AbsoluteVerified { .. } | rp::AccuracyClass::NotCovered);
            assert_eq!(s::rule_binding_refusal(&m.source, row).is_some(), refused, "{key}");
        }
        // No validated class, no binding: a refused statement refuses every row.
        let mut broken = m.source.clone();
        broken["results"][0]["value"] = json!(12345.0);
        for row in rows {
            assert_eq!(s::rule_binding_refusal(&broken, row), Some(s::RULE_QUANTITY_NOT_COVERED));
        }
        // The base identity is unchanged: no row of the projection is refused.
        let base = projected_base(&m.source);
        for row in base["results"].as_array().unwrap() {
            assert_eq!(s::rule_binding_refusal(&base, row), None);
        }
    }
}

#[test]
fn u6a_classification_summary_counts_validated_classes() {
    for m in milestones() {
        let [relative, absolute, input, non_quantity] = CLASSES.iter().find(|(mode, _)| *mode == m.mode).unwrap().1;
        let case_id = &m.invocation["request"]["model"]["load_cases"][0]["id"];
        let expected = json!([{"case_id":case_id,"relative_verified":relative,"absolute_verified":absolute,
            "interval_bindable":0,"not_covered":0,"input_derived":input,"non_quantity":non_quantity,
            "withheld":relative + absolute + input}]);
        // Not Current (eligibility held): every quantity row is withheld.
        assert_eq!(json!(s::classification_summary(&m.source, Some(&m.invocation))), expected);
        assert_eq!(json!(s::classification_summary(&m.source, None)), expected);
        let mut broken = m.source.clone();
        broken["results"][0]["value"] = json!(12345.0);
        assert!(s::classification_summary(&broken, Some(&m.invocation)).is_empty());
        assert!(s::classification_summary(&projected_base(&m.source), None).is_empty());
        // After U7 (exercised through the seam): only absolute and not-covered
        // rows stay withheld, and only for the invocation's requested cases.
        let mut validation = rp::validate(&m.source, Some(&m.invocation)).unwrap();
        validation.numerical_eligible = true;
        let mut current = expected.clone();
        current[0]["withheld"] = json!(absolute);
        assert_eq!(json!(s::classification_summary_from(&validation, &m.source, Some(&m.invocation))), current);
        assert_eq!(json!(s::classification_summary_from(&validation, &m.source, None)), expected);
        let mut other = m.invocation.clone();
        other["request"]["model"]["load_cases"][0]["id"] = json!("other");
        assert_eq!(json!(s::classification_summary_from(&validation, &m.source, Some(&other))), expected);
        // A not_covered row (none exists in any validated statement here) is
        // withheld whether or not the envelope is Current.
        let relative = validation.classifications.iter().position(|c| c.class == rp::AccuracyClass::RelativeVerified).unwrap();
        validation.classifications[relative].class = rp::AccuracyClass::NotCovered;
        let mut uncovered = current.clone();
        uncovered[0]["relative_verified"] = json!(25 - 1);
        uncovered[0]["not_covered"] = json!(1);
        uncovered[0]["withheld"] = json!(absolute + 1);
        assert_eq!(json!(s::classification_summary_from(&validation, &m.source, Some(&m.invocation))), uncovered);
        validation.numerical_eligible = false;
        uncovered[0]["withheld"] = json!(relative_count(&expected) + absolute + input);
        assert_eq!(json!(s::classification_summary_from(&validation, &m.source, Some(&m.invocation))), uncovered);
    }
}

/// Every class's binding refusal and disclosure, including `not_covered`,
/// which no validated statement in the milestone or the shared corpus has.
#[test]
fn u6a_each_class_maps_to_its_refusal_and_disclosure() {
    use rp::AccuracyClass as C;
    let absolute = C::AbsoluteVerified { bound_bits: 0x3b58_df09_e8b2_978b };
    assert_eq!(s::class_binding_refusal(&absolute), Some(s::RULE_QUANTITY_BELOW_VERIFIED_FLOOR));
    assert_eq!(s::class_binding_refusal(&C::NotCovered), Some(s::RULE_QUANTITY_NOT_COVERED));
    for class in [C::RelativeVerified, C::InputDerived, C::NonQuantity] {
        assert_eq!(s::class_binding_refusal(&class), None);
        assert_eq!(d::class_disclosure("k", Some(&class)), None);
    }
    assert_eq!(d::class_disclosure("k", None), None);
    let (code, message) = d::class_disclosure("element_local_axial_force", Some(&absolute)).unwrap();
    assert_eq!(code, d::RETAINED_ABSOLUTE_VERIFIED);
    assert_eq!(message, format!("element_local_axial_force: retained_precision_absolute_verified; verified only to the receipt's absolute bound b = {:e} (binary64 3b58df09e8b2978b) in the SI unit of this quantity, below the relative accuracy floor; source value/unit and annotation retained; withheld from rule binding and reliance", f64::from_bits(0x3b58_df09_e8b2_978b)));
    // The bound's bits are printed in full, leading zeros included.
    let (_, tiny) = d::class_disclosure("k", Some(&C::AbsoluteVerified { bound_bits: 1 })).unwrap();
    assert!(tiny.contains("(binary64 0000000000000001)"), "{tiny}");
    let (code, message) = d::class_disclosure("pipe_axial_membrane_stress_v2", Some(&C::NotCovered)).unwrap();
    assert_eq!(code, d::RETAINED_NOT_COVERED);
    assert_eq!(message, "pipe_axial_membrane_stress_v2: retained_precision_not_covered; no verified accuracy for this quantity kind; source value/unit and annotation retained; withheld from rule binding and reliance");
}

/// The shared three-language standing-parity scenarios (U6b and U6d consume
/// the same file): the Rust carrier's standing and raw dispatch per case.
#[test]
fn u6a_shared_carrier_cases_rust() {
    let cases: Value = serde_json::from_str(include_str!(
        "../../../../fixtures/results/retained_precision_carrier_cases.json"
    ))
    .unwrap();
    assert_eq!(cases["format"], "I66-U6-CARRIER-CASES-v1");
    let fixtures: Vec<(String, Value)> = cases["fixtures"]
        .as_object()
        .unwrap()
        .iter()
        .map(|(id, f)| {
            let text = match f["path"].as_str().unwrap() {
                p if p.ends_with("sparse_interactive.json") => SPARSE,
                p if p.ends_with("dense_scrutiny.json") => DENSE,
                p => panic!("{p}"),
            };
            assert_eq!(format!("{:x}", Sha256::digest(text.as_bytes())), f["sha256"].as_str().unwrap());
            (id.clone(), serde_json::from_str(text).unwrap())
        })
        .collect();
    let mut n = 0;
    for c in cases["cases"].as_array().unwrap() {
        let doc = &fixtures.iter().find(|(id, _)| c["fixture"] == id.as_str()).unwrap().1;
        let (mut source, mut invocation) = (doc["source"].clone(), doc["invocation"].clone());
        for edit in c["edits"].as_array().unwrap() {
            assert_eq!(edit["op"], "set");
            let target = if edit["target"] == "source" { &mut source } else { &mut invocation };
            let mut at = target;
            for key in edit["path"].as_array().unwrap() {
                at = match key {
                    Value::String(k) => &mut at[k.as_str()],
                    Value::Number(i) => &mut at[i.as_u64().unwrap() as usize],
                    _ => panic!("path"),
                };
            }
            *at = edit["value"].clone();
        }
        let invocation = (!c["invocation"].is_null()).then_some(invocation);
        let requested = if c["requested"] == "invocation" { requested(&doc["invocation"]) } else { c["requested"].as_array().unwrap().clone() };
        assert_eq!(s::numerical_use_standing_with_context(&source, &requested, invocation.as_ref()), c["expected_standing"], "{}", c["id"]);
        let dispatch = match s::for_source(&source) { Ok(_) => "ok".to_string(), Err(e) => e };
        assert_eq!(dispatch, c["expected_dispatch"].as_str().unwrap(), "{}", c["id"]);
        n += 1;
    }
    assert_eq!(n, 14);
}

/// The relative count of a one-case expected summary.
fn relative_count(expected: &Value) -> u64 {
    expected[0]["relative_verified"].as_u64().unwrap()
}
