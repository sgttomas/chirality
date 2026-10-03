//! Shared synthetic statement controls. These do not establish execution.
use open_pipe_stress_result_export::retained_precision as rp;
use serde_json::Value;
fn corpus() -> Value {
    serde_json::from_str(include_str!(
        "../../../../fixtures/results/retained_precision_cases.json"
    ))
    .unwrap()
}
fn decode(v: &Value) -> f64 {
    f64::from_bits(u64::from_str_radix(v.as_str().unwrap(), 16).unwrap())
}
#[test]
fn fixed_small_bound_vectors() {
    for row in corpus()["arithmetic"]["small_bounds"].as_array().unwrap() {
        assert_eq!(
            rp::absolute_bound(decode(&row["value"]), decode(&row["scale"]))
                .unwrap()
                .to_bits(),
            decode(&row["expected"]).to_bits(),
            "{}",
            row["id"]
        );
    }
}
#[test]
fn finite_product_vectors_and_ranges() {
    for row in corpus()["arithmetic"]["products"].as_array().unwrap() {
        let result = rp::upward_product(decode(&row["a"]), decode(&row["b"]));
        if row["expected"].is_null() {
            assert!(result.is_err());
        } else {
            assert_eq!(
                result.unwrap().to_bits(),
                decode(&row["expected"]).to_bits()
            );
        }
    }
    assert_eq!(
        rp::upward_small_sum(1.0, f64::from_bits(1))
            .unwrap()
            .to_bits(),
        0x3ff0000000000001
    );
    assert_eq!(rp::upward_product(-0.0, 1.0).unwrap().to_bits(), 0);
    for value in [f64::NAN, f64::INFINITY, f64::NEG_INFINITY, -1.0] {
        assert!(rp::upward_product(value, 1.0).is_err());
    }
}

fn rehash(source: &mut Value) {
    use open_pipe_stress_result_export::source_blocks::domain_hash;
    let b = &mut source["retained_precision"]["body"];
    let attempts = b["product_attempts"].clone();
    for s in b["sources"].as_array_mut().unwrap() {
        if let Some(ai) = s["preparation"]["attempt_ref"].as_u64() {
            let a = &attempts[ai as usize];
            if a["preparation"]["members"]
                .as_array()
                .unwrap()
                .iter()
                .all(|m| m["result"]["kind"] == "prepared")
            {
                let members: Vec<_> = a["preparation"]["members"].as_array().unwrap().iter().map(|m| serde_json::json!({"member":m["member"],"old_source":m["old_source"],"old_facts":m["old_facts"],"section":m["result"]["section"]})).collect();
                let payload = serde_json::json!({"definition_id":a["definition_id"],"definition_sha256":rp::DEFINITION_HASH,"owner_ref":a["owner_ref"],"ordinary_attempt_ref":a["ordinary_attempt_ref"],"material_basis_ref":a["material_basis_ref"],"members":members});
                s["preparation"]["sha256"] =
                    domain_hash("retained_precision_preparation_v1", &payload)
                        .unwrap()
                        .into();
            }
        }
    }
    let sources = b["sources"].clone();
    for c in b["cases"].as_array_mut().unwrap() {
        if c.get("source_identity_sha256").is_some() {
            let mut s = sources[c["source_ref"].as_u64().unwrap() as usize].clone();
            s.as_object_mut().unwrap().remove("index");
            c["source_identity_sha256"] = domain_hash("retained_precision_source_mp_v2", &s)
                .unwrap()
                .into();
        }
    }
    let mut public = source.clone();
    public.as_object_mut().unwrap().remove("retained_precision");
    source["retained_precision"]["body"]["publication_sha256"] =
        domain_hash("retained_precision_publication_mp_v2", &public)
            .unwrap()
            .into();
    source["retained_precision"]["receipt_sha256"] = domain_hash(
        "retained_precision_receipt_mp_v2",
        &source["retained_precision"]["body"],
    )
    .unwrap()
    .into();
}
fn edit(source: &mut Value, e: &Value) {
    let path = e["path"].as_array().unwrap();
    let mut parent = source;
    for p in &path[..path.len() - 1] {
        parent = if let Some(i) = p.as_u64() {
            &mut parent[i as usize]
        } else {
            &mut parent[p.as_str().unwrap()]
        };
    }
    let last = path.last().unwrap();
    if e["op"] == "remove" {
        parent
            .as_object_mut()
            .unwrap()
            .remove(last.as_str().unwrap());
    } else if let Some(i) = last.as_u64() {
        parent[i as usize] = e["value"].clone();
    } else {
        parent[last.as_str().unwrap()] = e["value"].clone();
    }
}
/// The reader's own expectation: `expected_by_reader.rust` when present (the
/// per-language G7 base code), else the shared `expected` (snapshot 06b format).
fn expected_for(m: &Value) -> &Value {
    m.get("expected_by_reader")
        .and_then(|e| e.get("rust"))
        .unwrap_or(&m["expected"])
}
/// Apply a shared mutation or must-pass entry exactly as SHARED_SNAPSHOT_06C
/// `format_change` specifies: edit a copy of the base source; edit a copy of
/// the base invocation; when invocation edits exist, bind the receipt's
/// invocation digest to the edited invocation; then rehash per `rehash`.
/// Returns the edited source and the invocation to validate against.
fn apply_entry(shared: &Value, entry: &Value) -> (Value, Value) {
    use open_pipe_stress_result_export::source_blocks::domain_hash;
    let case = shared["cases"]
        .as_array()
        .unwrap()
        .iter()
        .find(|c| c["id"] == entry["base"])
        .unwrap();
    let mut source = case["source"].clone();
    for e in entry["edits"].as_array().unwrap() {
        edit(&mut source, e);
    }
    let mut invocation = case["invocation"].clone();
    let invocation_edits = entry["invocation_edits"].as_array().cloned().unwrap_or_default();
    for e in &invocation_edits {
        edit(&mut invocation, e);
    }
    if !invocation_edits.is_empty() {
        source["retained_precision"]["body"]["invocation"]["value"] =
            domain_hash("source_blocks_invocation_v1", &invocation)
                .unwrap()
                .into();
    }
    if entry["rehash"] == "all" {
        rehash(&mut source);
    }
    (source, invocation)
}
#[test]
fn complete_synthetic_controls_keep_eligibility_held() {
    let shared = corpus();
    for case in shared["cases"].as_array().unwrap() {
        let got = rp::validate(&case["source"], Some(&case["invocation"]))
            .unwrap_or_else(|e| panic!("{}: {e:?}", case["id"]));
        assert!(got.invocation_bound);
        assert!(
            !got.numerical_eligible,
            "native summary coverage remains held"
        );
        assert_eq!(
            got.publication_sha256,
            case["source"]["retained_precision"]["body"]["publication_sha256"]
        );
        let expected = case["expected_classifications"].as_array().unwrap();
        assert_eq!(got.classifications.len(), expected.len());
        for (got, want) in got.classifications.iter().zip(expected) {
            assert_eq!(got.result_id, want["result_id"]);
            assert_eq!(got.basis_ref, want["basis_ref"]);
            assert_eq!(
                format!("{:016x}", got.normalized_bits),
                want["normalized_bits"]
            );
            assert_eq!(
                got.scale_bits.map(|b| format!("{b:016x}")),
                want["scale_bits"].as_str().map(str::to_owned)
            );
            let name = match got.class {
                rp::AccuracyClass::RelativeVerified => "relative_verified",
                rp::AccuracyClass::AbsoluteVerified { bound_bits } => {
                    assert_eq!(format!("{bound_bits:016x}"), want["bound_bits"]);
                    "absolute_verified"
                }
                rp::AccuracyClass::InputDerived => "input_derived",
                rp::AccuracyClass::NonQuantity => "non_quantity",
                rp::AccuracyClass::NotCovered => "not_covered",
            };
            assert_eq!(name, want["class"]);
        }
        let unbound = rp::validate(&case["source"], None).unwrap();
        assert!(!unbound.invocation_bound && !unbound.numerical_eligible);
        let transport = rp::validate_transport_metadata(&case["source"]).unwrap();
        assert!(
            !transport.invocation_bound
                && !transport.numerical_eligible
                && transport.classifications.is_empty()
        );
    }
}
#[test]
fn shared_rehashed_first_failure_mutations() {
    let shared = corpus();
    let mut failures = Vec::new();
    for mutation in shared["mutations"].as_array().unwrap() {
        let (source, invocation) = apply_entry(&shared, mutation);
        let expected = expected_for(mutation);
        match rp::validate(&source, Some(&invocation)) {
            Err(e) if e.gate == expected["gate"] && e.code == expected["code"] => {}
            Err(got) => failures.push(format!(
                "{} expected {} got {got:?}",
                mutation["id"], expected
            )),
            Ok(got) => failures.push(format!(
                "{} expected {} got admitted statement (eligible={})",
                mutation["id"], expected, got.numerical_eligible
            )),
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

/// Observe one slice of the shared mutations against this reader's own
/// expectation, print one outcome per mutation (visible with --nocapture) and
/// check the slice tally. Snapshot 06d holds 178 mutations in all.
fn slice_outcomes(tag: &str, range: std::ops::Range<usize>, want: &[(&str, usize)]) {
    use std::collections::BTreeMap;
    let shared = corpus();
    let mutations = shared["mutations"].as_array().unwrap();
    assert_eq!(mutations.len(), 178);
    let mut tally = BTreeMap::new();
    let mut matched = 0;
    for mutation in &mutations[range.clone()] {
        let observed = observe(&shared, mutation);
        let expected = expected_for(mutation);
        let ok = observed == *expected;
        matched += usize::from(ok);
        *tally
            .entry(format!(
                "{} {}",
                expected["gate"].as_str().unwrap(),
                expected["code"].as_str().unwrap()
            ))
            .or_insert(0) += 1;
        println!(
            "{tag} {}",
            serde_json::json!({"id":mutation["id"],"base":mutation["base"],"expected":expected,"observed":observed,"match":ok})
        );
    }
    let want: BTreeMap<String, usize> = want.iter().map(|(k, n)| (k.to_string(), *n)).collect();
    assert_eq!(tally, want, "{tag}");
    assert_eq!(matched, range.len(), "{tag}");
}

/// Snapshot-04 summary-coverage controls (I57 s4/s5), mutations 30..77.
#[test]
fn snapshot_04_coverage_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME",
        30..77,
        &[
            ("G1 RETAINED_PRECISION_RECEIPT_MISMATCH", 14),
            ("G2 RETAINED_PRECISION_ENCODING_MISMATCH", 4),
            ("G3 RETAINED_PRECISION_COVERAGE_MISMATCH", 6),
            ("G5 RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH", 2),
            ("G5 RETAINED_PRECISION_ATTEMPT_MISMATCH", 1),
            ("G5a RETAINED_PRECISION_SCALE_MISMATCH", 20),
        ],
    );
}

/// Snapshot-05a controls (I62 C1a), mutations 77..104.
#[test]
fn snapshot_05a_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME_05A",
        77..104,
        &[
            ("G3 RETAINED_PRECISION_COVERAGE_MISMATCH", 3),
            ("G5 RETAINED_PRECISION_ATTEMPT_MISMATCH", 1),
            ("G5 RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH", 5),
            ("G5 RETAINED_PRECISION_WORK_MISMATCH", 2),
            ("G5a RETAINED_PRECISION_SCALE_MISMATCH", 16),
        ],
    );
}

/// Snapshot-05b controls (I62 C1b, unchanged in 05c), mutations 104..121.
#[test]
fn snapshot_05b_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME_05B",
        104..121,
        &[
            ("G3 RETAINED_PRECISION_COVERAGE_MISMATCH", 2),
            ("G5 RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH", 1),
            ("G5a RETAINED_PRECISION_SCALE_MISMATCH", 13),
            ("G5b RETAINED_PRECISION_SCALE_MISMATCH", 1),
        ],
    );
}

/// Snapshot-06a checklist controls (I62 C2-1), mutations 121..150; 06b moved
/// `prefix_old_inputs_unbound` to the must-pass entries (P7 settlement), and
/// the G7 entry uses this reader's own base code (`expected_by_reader`).
#[test]
fn snapshot_06a_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME_06A",
        121..150,
        &[
            ("G2 RETAINED_PRECISION_ENCODING_MISMATCH", 1),
            ("G3 RETAINED_PRECISION_COVERAGE_MISMATCH", 3),
            ("G5 RETAINED_PRECISION_ATTEMPT_MISMATCH", 10),
            ("G5 RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH", 10),
            ("G5 RETAINED_PRECISION_WORK_MISMATCH", 2),
            ("G7 SOURCE_PREVIEW_PHYSICS_EXTREMA_BOUNDS", 1),
            ("G8 RETAINED_PRECISION_PREPARATION_MISMATCH", 2),
        ],
    );
}

/// Snapshot-06b settlements (I62 C2-2), mutations 150..163, with
/// `ceiling_before_last_slot` under its 06c name.
#[test]
fn snapshot_06b_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME_06B",
        150..163,
        &[
            ("G1 RETAINED_PRECISION_RECEIPT_MISMATCH", 1),
            ("G5 RETAINED_PRECISION_ATTEMPT_MISMATCH", 8),
            ("G5 RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH", 1),
            ("G8 RETAINED_PRECISION_PREPARATION_MISMATCH", 3),
        ],
    );
}

/// Snapshot-06c (I62 C2-3), mutations 163..173: WorkAccounting terminals
/// rejected, and the invocation-level G8 refusals through `invocation_edits`.
#[test]
fn snapshot_06c_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME_06C",
        163..173,
        &[
            ("G5 RETAINED_PRECISION_ATTEMPT_MISMATCH", 3),
            ("G8 RETAINED_PRECISION_PREPARATION_MISMATCH", 7),
        ],
    );
}


/// Snapshot-06d (I62 C2-5), mutations 173..178: R1-R3 at G5 WORK, and the
/// tightened idle sibling at the exhaustion rule.
#[test]
fn snapshot_06d_mutation_outcomes() {
    slice_outcomes(
        "I63_OUTCOME_06D",
        173..178,
        &[
            ("G5 RETAINED_PRECISION_ATTEMPT_MISMATCH", 1),
            ("G5 RETAINED_PRECISION_WORK_MISMATCH", 4),
        ],
    );
}

fn observe(shared: &Value, mutation: &Value) -> Value {
    let (source, invocation) = apply_entry(shared, mutation);
    match rp::validate(&source, Some(&invocation)) {
        Err(e) => serde_json::json!({"gate":e.gate,"code":e.code}),
        Ok(_) => serde_json::json!(null),
    }
}




fn attempt_mismatch(got: Result<(), rp::ValidationError>) -> bool {
    matches!(got, Err(e) if e.gate == "G5" && e.code == "RETAINED_PRECISION_ATTEMPT_MISMATCH")
}

/// Rust reader-logic controls mirroring I62's Python-only tests for checklist
/// N5, N6, N8 and N10, which have no native-faithful shared base yet (the
/// Ceiling, an idle/pre-schedule Run, a verification-pass terminal). They run
/// the same schedule replay `validate` uses, on one Run.
#[test]
fn schedule_replay_terminal_branches_reader_logic() {
    use serde_json::json;
    let shared = corpus();
    let schedule = rp::reader_logic::schedule;
    let run_of = |id: &str| {
        shared["cases"]
            .as_array()
            .unwrap()
            .iter()
            .find(|c| c["id"] == id)
            .unwrap()["source"]["retained_precision"]["body"]["cases"][0]["run"]
            .clone()
    };
    let selected = run_of("ordinary_prepared_synthetic");
    assert!(schedule(&selected).is_ok());
    let ceiling = json!({"kind":"unresolved","reason":{"space":"unresolved","tag":"ceiling"}});
    // N10: an idle (pre-schedule) Run has no records, no charge and a reasoned
    // non-selected terminal.
    let mut idle = selected.clone();
    idle["records"] = json!([]);
    idle["attempts"] = json!([]);
    idle["case_charge"] = json!(0);
    idle["invocation_increment"] = json!(0);
    idle["kernel_terminal"] =
        json!({"kind":"unresolved","reason":{"space":"unresolved","tag":"budget","scope":"invocation"}});
    assert!(schedule(&idle).is_ok());
    let mut bad = idle.clone();
    bad["kernel_terminal"] = json!({"kind":"selected","reason":null});
    assert!(attempt_mismatch(schedule(&bad)), "idle Run cannot select");
    let mut bad = idle.clone();
    bad["case_charge"] = json!(1);
    assert!(attempt_mismatch(schedule(&bad)), "idle Run carries no charge");
    // 06b/06c ruling: no WorkAccounting terminal is emitted, idle or not.
    let mut bad = idle.clone();
    bad["kernel_terminal"] = json!({"kind":"unresolved","reason":{"space":"unresolved","tag":"work_accounting","fault":"overflow"}});
    assert!(attempt_mismatch(schedule(&bad)), "idle WorkAccounting is not emitted");
    // N6: a rejected p128 candidate must hand its verification to a reused p256.
    let reason = json!({"space":"attempt","tag":"stop_rule","quantity":{"tag":"displacement","dof":{"node":1,"component":"UX"}},"body":0,"kind":"translation"});
    let mut rejected = selected.clone();
    rejected["attempts"][0]["outcome"] = json!({"kind":"rejected","reason":reason});
    rejected["records"][0]["outcome"] = json!({"kind":"rejected","reason":reason});
    rejected["records"][1]["outcome"] = json!({"kind":"solved"});
    rejected["kernel_terminal"] = ceiling.clone();
    assert!(attempt_mismatch(schedule(&rejected)), "rejected must continue");
    // N5: a non-escalating verification-pass failure is terminal.
    let stop = json!({"space":"attempt","tag":"stop","stop":{"space":"stop","tag":"structure"}});
    let mut vfail = selected.clone();
    let verification_failed = json!({"kind":"rejected","reason":{"space":"attempt","tag":"verification_failed"}});
    vfail["attempts"][0]["outcome"] = verification_failed.clone();
    vfail["records"][0]["outcome"] = verification_failed;
    vfail["attempts"][0]["verification"] =
        json!({"record":1,"precision":256,"phase":"failed","reason":stop});
    vfail["records"][1]["outcome"] = json!({"kind":"failed","reason":stop});
    vfail["kernel_terminal"] = json!({"kind":"refused","reason":{"space":"refusal","tag":"structure"}});
    assert!(schedule(&vfail).is_ok());
    let mut bad = vfail.clone();
    bad["kernel_terminal"] = json!({"kind":"selected","reason":null});
    assert!(attempt_mismatch(schedule(&bad)), "verification-pass failure cannot select");
    // N8: the Ceiling, when the reused p512 candidate is rejected and its p1024
    // verification only solved.
    let mut ladder = run_of("p512_ladder_synthetic");
    assert!(schedule(&ladder).is_ok());
    ladder["attempts"][2]["outcome"] = json!({"kind":"rejected","reason":reason});
    ladder["records"][2]["outcome"] = json!({"kind":"rejected","reason":reason});
    ladder["records"][3]["outcome"] = json!({"kind":"solved"});
    ladder["kernel_terminal"] = ceiling;
    assert!(schedule(&ladder).is_ok());
    let mut bad = ladder.clone();
    bad["kernel_terminal"] = json!({"kind":"refused","reason":{"space":"refusal","tag":"structure"}});
    assert!(attempt_mismatch(schedule(&bad)), "exhausted ladder is the Ceiling");
}

/// 06c WorkAccounting rejections fail in the schedule replay itself (the
/// emitted-terminal rule), not only through a later check on the same code:
/// the replay alone, without the statement, rejects each WorkAccounting Run.
#[test]
fn work_accounting_mutations_fail_at_the_terminal_rule() {
    let shared = corpus();
    for id in [
        "work_accounting_after_escalating_stop",
        "idle_work_accounting_run",
        "work_accounting_at_last_slot",
    ] {
        let mutation = shared["mutations"]
            .as_array()
            .unwrap()
            .iter()
            .find(|m| m["id"] == id)
            .unwrap();
        let (source, _) = apply_entry(&shared, mutation);
        let runs: Vec<&Value> = source["retained_precision"]["body"]["cases"]
            .as_array()
            .unwrap()
            .iter()
            .map(|c| &c["run"])
            .filter(|r| r["kernel_terminal"]["reason"]["tag"] == "work_accounting")
            .collect();
        assert_eq!(runs.len(), 1, "{id}");
        assert!(attempt_mismatch(rp::reader_logic::schedule(runs[0])), "{id}");
    }
}

/// Rust reader-logic control mirroring I62's Python-only test for checklist O5
/// (no native-faithful source_decline base yet).
#[test]
fn source_decline_relation_reader_logic() {
    use serde_json::json;
    let shared = corpus();
    let fixture = shared["cases"]
        .as_array()
        .unwrap()
        .iter()
        .find(|c| c["id"] == "two_case_preparation_failure_synthetic")
        .unwrap();
    let mut source = fixture["source"].clone();
    let decline = json!({
        "input_owner": {"case_index": 1, "case_id": "case:unavailable-row", "material_basis_ref": 0},
        "constructor_counts": {"nodes": 2, "members": 1, "springs": 0, "constraints": 6, "nodal_terms": 6, "stations": 3, "supports": 1, "id_utf8_bytes": 0, "directional_springs": 0},
        "error": {"tag": "no_nodes"}
    });
    source["retained_precision"]["body"]["cases"][1]["source_decline"] = decline.clone();
    assert!(rp::reader_logic::ordinary(&source).is_ok());
    let mut wrong = decline;
    wrong["input_owner"]["case_index"] = json!(0);
    source["retained_precision"]["body"]["cases"][1]["source_decline"] = wrong;
    assert!(attempt_mismatch(rp::reader_logic::ordinary(&source)));
}

/// Reader-local controls (not shared corpus) for checklist checks added in the
/// I63 audit that no shared mutation decides first: P2 (observables and G5a
/// enter together), P6 (a failed maxima merges its work) and P9 (an
/// unavailable error matches the first failed stage), each on a shared
/// must-pass base; and the G7 bare code with the Rust base code as detail.
#[test]
fn g5_audit_local_controls() {
    use serde_json::json;
    let shared = corpus();
    let entry = |id: &str| {
        shared["must_pass"]
            .as_array()
            .unwrap()
            .iter()
            .find(|m| m["id"] == id)
            .unwrap()
            .clone()
    };
    let attempt = json!(["retained_precision", "body", "product_attempts", 1]);
    let at = |tail: Value| {
        let mut p = attempt.as_array().unwrap().clone();
        p.extend(tail.as_array().unwrap().iter().cloned());
        Value::Array(p)
    };
    for (name, base, extra) in [
        (
            "P9: maxima failure reported as a proof error",
            "maxima_abandoned",
            vec![(
                at(json!(["result"])),
                json!({"kind":"unavailable","error":{"kind":"proof","cause":{"kind":"work_accounting","fault":"overflow"}}}),
            )],
        ),
        (
            "P6: failed maxima without merged completion",
            "maxima_abandoned",
            vec![(at(json!(["proof", "completion"])), json!({"kind":"not_entered"}))],
        ),
        (
            "P2: observables entered without G5a",
            "cert_failed_before_summary",
            vec![
                (at(json!(["stages", "observables"])), json!("failed")),
                (
                    at(json!(["proof", "checks", "observables"])),
                    json!({"kind":"failed","error":{"kind":"observable","cause":{"kind":"accounting","event":"map_write"}}}),
                ),
            ],
        ),
    ] {
        let mut mutation = entry(base);
        for (path, value) in extra {
            mutation["edits"]
                .as_array_mut()
                .unwrap()
                .push(json!({"path":path,"op":"set","value":value}));
        }
        mutation["expected"] = json!(null);
        assert_eq!(
            observe(&shared, &mutation),
            json!({"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}),
            "{name}"
        );
    }
    // G7: the bare base code is the error code.
    let g7 = shared["mutations"]
        .as_array()
        .unwrap()
        .iter()
        .find(|m| m["id"] == "g7_maximum_off_enclosure")
        .unwrap();
    let case = shared["cases"]
        .as_array()
        .unwrap()
        .iter()
        .find(|c| c["id"] == g7["base"])
        .unwrap();
    let mut source = case["source"].clone();
    for e in g7["edits"].as_array().unwrap() {
        edit(&mut source, e);
    }
    rehash(&mut source);
    let got = rp::validate(&source, Some(&case["invocation"])).unwrap_err();
    // G7 settlement (06b): this reader's own bare base code, detail separate.
    assert_eq!(
        (got.gate, got.code.as_str()),
        ("G7", "SOURCE_PREVIEW_PHYSICS_EXTREMA_BOUNDS")
    );
}

/// Snapshot-05a shared must-pass entries: each rehashed rewrite keeps every
/// public relation, so the reader admits it with the base case's
/// classifications; eligibility stays held.
#[test]
fn shared_must_pass_entries_validate() {
    let shared = corpus();
    let entries = shared["must_pass"].as_array().unwrap();
    // Snapshot 06d: 06c's 23, with six replaced by allocator-refusal causes,
    // one renamed and five retired or deferred.
    assert_eq!(entries.len(), 18);
    let mut failures = Vec::new();
    for entry in entries {
        assert_eq!(entry["expected"], "pass");
        assert_eq!(entry["rehash"], "all");
        let case = shared["cases"]
            .as_array()
            .unwrap()
            .iter()
            .find(|c| c["id"] == entry["base"])
            .unwrap();
        let (source, invocation) = apply_entry(&shared, entry);
        let got = match rp::validate(&source, Some(&invocation)) {
            Ok(got) => got,
            Err(e) => {
                failures.push(format!("{} rejected {e:?}", entry["id"]));
                continue;
            }
        };
        let expected = case["expected_classifications"].as_array().unwrap();
        let same = !got.numerical_eligible
            && got.invocation_bound
            && got.classifications.len() == expected.len()
            && got.classifications.iter().zip(expected).all(|(g, w)| {
                let class = match g.class {
                    rp::AccuracyClass::RelativeVerified => "relative_verified",
                    rp::AccuracyClass::AbsoluteVerified { bound_bits } => {
                        if format!("{bound_bits:016x}") != w["bound_bits"] {
                            return false;
                        }
                        "absolute_verified"
                    }
                    rp::AccuracyClass::InputDerived => "input_derived",
                    rp::AccuracyClass::NonQuantity => "non_quantity",
                    rp::AccuracyClass::NotCovered => "not_covered",
                };
                g.result_id == w["result_id"]
                    && g.basis_ref == w["basis_ref"]
                    && format!("{:016x}", g.normalized_bits) == w["normalized_bits"]
                    && g.scale_bits.map(|b| format!("{b:016x}"))
                        == w["scale_bits"].as_str().map(str::to_owned)
                    && class == w["class"]
            });
        println!("I63_MUST_PASS {} {}", entry["id"], same);
        if !same {
            failures.push(format!("{} classifications differ", entry["id"]));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

/// C1 G5b "same E/ê/Φ at p512" (FK/verify.rs:321-376). No p512 corpus base
/// exists until C1b, so the rounding is pinned directly. Expected bits were
/// derived independently as the least binary64 >= e·2^-438 with an exact
/// rational oracle (hand-checked for the subnormal ties).
#[test]
fn p512_floor_phi_follows_native_rounding() {
    for (input, expected) in [
        (0x0000000000000000u64, 0x0000000000000000u64),
        (0x3ff0000000000000, 0x2490000000000000), // 1 -> 2^-438 exactly
        (0x1a70000000000001, 0x0000001000000001), // 2^-600(1+2^-52): nearest is below, next up
        (0x7fefffffffffffff, 0x648fffffffffffff), // MAX scales exactly
        (0x0000000000000001, 0x0000000000000001), // underflows to 0, next up is 2^-1074
        (0x1838000000000000, 0x0000000000000002), // 1.5 ulp ties to even 2: not below
        (0x1844000000000000, 0x0000000000000003), // 2.5 ulp ties to even 2: below, next up
    ] {
        assert_eq!(
            rp::phi_512(f64::from_bits(input)).to_bits(),
            expected,
            "{input:016x}"
        );
    }
    assert_eq!(rp::e_hat([3.0, 0.0], 0.0), [3.0, 0.0]);
    assert_eq!(rp::e_hat([3.0, 0.0], 2.0), [3.0, 6.0]);
    assert_eq!(rp::e_hat([0.0, 8.0], 2.0), [4.0, 8.0]);
}

/// Reader-local synthetic controls (not shared corpus entries), mirroring the
/// three Python-only I62 checkpoint-B layout controls: G5a rederives the
/// canonical layout from the bound source maps, so a purported input-derived
/// force row, an unmarked constrained displacement or a nonzero prescription
/// (outside this C3 D=false scope) fails at G5a before the later G8 binding.
/// The fourth control is Rust-specific: the full canonical rebuild also rejects
/// a non-input kind relabel at G5a (the Python draft reaches G8 for it).
#[test]
fn coverage_layout_controls_fail_at_g5a() {
    use serde_json::json;
    let shared = corpus();
    let c = &shared["cases"][0];
    for (name, tail, value) in [
        (
            "reaction force row flagged input-derived",
            json!(["layout", 44, "input_derived"]),
            json!(true),
        ),
        (
            "constrained displacement not flagged input-derived",
            json!(["layout", 0, "input_derived"]),
            json!(false),
        ),
        (
            "nonzero prescription",
            json!(["constraints", 0, "value"]),
            json!("3ff0000000000000"),
        ),
        (
            "rust-specific: end-action force row relabelled translation",
            json!(["layout", 14, "kind"]),
            json!("translation"),
        ),
    ] {
        let mut path = json!(["retained_precision", "body", "sources", 0]);
        path.as_array_mut()
            .unwrap()
            .extend(tail.as_array().unwrap().iter().cloned());
        let mut source = c["source"].clone();
        edit(&mut source, &json!({"path":path,"op":"set","value":value}));
        rehash(&mut source);
        let got = rp::validate(&source, Some(&c["invocation"])).unwrap_err();
        assert_eq!(
            (got.gate, got.code.as_str()),
            ("G5a", "RETAINED_PRECISION_SCALE_MISMATCH"),
            "{name}"
        );
    }
}

/// I57 s4/s5 over-rejection guard, mirroring I62's Python-only controls: these
/// rewrites keep every public relation (feasibility, rederived estimate and
/// charge, exact rosters, record binding, direct data facts), so the reader must
/// admit them with the base classifications; only producer custody or replay
/// can catch such attested private flags. Eligibility stays held.
#[test]
fn publicly_consistent_coverage_attestations_are_not_rejected() {
    use serde_json::json;
    let shared = corpus();
    let zero = "0000000000000000";
    let coverage = json!(["retained_precision", "body", "product_attempts", 0, "proof", "summary_coverage", 0]);
    let selection = json!(["retained_precision", "body", "cases", 0, "selection"]);
    let verification = json!(["retained_precision", "body", "cases", 0, "run", "records", 1, "verification"]);
    let at = |base: &Value, tail: Value| {
        let mut p = base.as_array().unwrap().clone();
        p.extend(tail.as_array().unwrap().iter().cloned());
        Value::Array(p)
    };
    let four = json!(["translation", "rotation", "force", "moment"])
        .as_array()
        .unwrap()
        .iter()
        .map(|k| json!({"body":0,"kind":k,"value":zero}))
        .collect::<Vec<_>>();
    let variants = [
        (
            "loaded_stop_without_force_moment",
            "ordinary_prepared_synthetic",
            vec![
                (at(&coverage, json!(["stop"])), json!([true, true, false, false])),
                (at(&selection, json!(["stop_rule"])), json!(four[..2])),
            ],
        ),
        (
            "loaded_all_stop_false",
            "ordinary_prepared_synthetic",
            vec![
                (at(&coverage, json!(["stop"])), json!([false, false, false, false])),
                (at(&selection, json!(["stop_rule"])), json!([])),
            ],
        ),
        (
            "no_data_all_stop_true",
            "ordinary_prepared_no_data_synthetic",
            vec![
                (at(&coverage, json!(["stop"])), json!([true, true, true, true])),
                (at(&selection, json!(["stop_rule"])), json!(four)),
            ],
        ),
        (
            "no_data_attested_data_block",
            "ordinary_prepared_no_data_synthetic",
            vec![
                (at(&coverage, json!(["has_data"])), json!(true)),
                (
                    at(&selection, json!(["certified_bound"])),
                    json!([{"body":0,"value":"3ff0000000000000"}]),
                ),
                (
                    at(&verification, json!(["bound"])),
                    json!([{"body":0,"value":"3ff0000000000000"}]),
                ),
                (at(&verification, json!(["data_blocks"])), json!(1)),
            ],
        ),
    ];
    for (name, base, edits) in variants {
        let case = shared["cases"]
            .as_array()
            .unwrap()
            .iter()
            .find(|c| c["id"] == base)
            .unwrap();
        let mut source = case["source"].clone();
        for (path, value) in edits {
            edit(&mut source, &json!({"path":path,"op":"set","value":value}));
        }
        rehash(&mut source);
        let got = rp::validate(&source, Some(&case["invocation"]))
            .unwrap_or_else(|e| panic!("{name}: {e:?}"));
        assert!(!got.numerical_eligible, "{name}");
        let expected = case["expected_classifications"].as_array().unwrap();
        assert_eq!(got.classifications.len(), expected.len(), "{name}");
        for (got, want) in got.classifications.iter().zip(expected) {
            assert_eq!(got.result_id, want["result_id"], "{name}");
            assert_eq!(
                format!("{:016x}", got.normalized_bits),
                want["normalized_bits"],
                "{name}"
            );
            assert_eq!(
                got.scale_bits.map(|b| format!("{b:016x}")),
                want["scale_bits"].as_str().map(str::to_owned),
                "{name}"
            );
        }
    }
}

#[test]
fn canonical_zero_and_invalid_helper_operands() {
    for zero in [0.0, -0.0] {
        for value in [0.0, -0.0, 1.0, -1.0, f64::MAX, -f64::MAX] {
            assert_eq!(rp::absolute_bound(value, zero).unwrap().to_bits(), 0);
        }
        assert_eq!(rp::upward_product(zero, 1.0).unwrap().to_bits(), 0);
        assert_eq!(rp::upward_product(1.0, zero).unwrap().to_bits(), 0);
        assert_eq!(rp::upward_small_sum(zero, zero).unwrap().to_bits(), 1);
    }
    for bad in [f64::NAN, f64::INFINITY, f64::NEG_INFINITY, -1.0] {
        assert!(rp::absolute_bound(1.0, bad).is_err());
        assert!(rp::upward_small_sum(bad, 0.0).is_err());
        assert!(rp::upward_small_sum(0.0, bad).is_err());
        assert!(rp::upward_product(1.0, bad).is_err());
    }
    for bad in [f64::NAN, f64::INFINITY, f64::NEG_INFINITY] {
        assert!(rp::absolute_bound(bad, 1.0).is_err());
    }
    assert!(rp::upward_small_sum(f64::MAX, 0.0).is_err());
    assert!(rp::upward_small_sum(f64::MAX, f64::MAX).is_err());
}

// Expected values independently computed with Fraction and least-upper binary search.
// Every expected result and its immediate predecessor were checked in the rational oracle.
#[test]
fn independent_rational_product_and_single_round_sum_controls() {
    let cases: &[(u64, u64, Option<u64>, Option<u64>)] = &[
        (
            0x0000000000000000,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x0000000000000001),
        ),
        (
            0x0000000000000000,
            0x0000000000000001,
            Some(0x0000000000000000),
            Some(0x0000000000000002),
        ),
        (
            0x0000000000000000,
            0x0000000000000002,
            Some(0x0000000000000000),
            Some(0x0000000000000003),
        ),
        (
            0x0000000000000000,
            0x000fffffffffffff,
            Some(0x0000000000000000),
            Some(0x0010000000000000),
        ),
        (
            0x0000000000000000,
            0x0010000000000000,
            Some(0x0000000000000000),
            Some(0x0010000000000001),
        ),
        (
            0x0000000000000000,
            0x3ff0000000000000,
            Some(0x0000000000000000),
            Some(0x3ff0000000000001),
        ),
        (
            0x0000000000000000,
            0x3ff0000000000001,
            Some(0x0000000000000000),
            Some(0x3ff0000000000002),
        ),
        (
            0x0000000000000000,
            0x7fefffffffffffff,
            Some(0x0000000000000000),
            None,
        ),
        (
            0x0000000000000001,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x0000000000000002),
        ),
        (
            0x0000000000000001,
            0x0000000000000001,
            Some(0x0000000000000001),
            Some(0x0000000000000003),
        ),
        (
            0x0000000000000001,
            0x0000000000000002,
            Some(0x0000000000000001),
            Some(0x0000000000000004),
        ),
        (
            0x0000000000000001,
            0x000fffffffffffff,
            Some(0x0000000000000001),
            Some(0x0010000000000001),
        ),
        (
            0x0000000000000001,
            0x0010000000000000,
            Some(0x0000000000000001),
            Some(0x0010000000000002),
        ),
        (
            0x0000000000000001,
            0x3ff0000000000000,
            Some(0x0000000000000001),
            Some(0x3ff0000000000001),
        ),
        (
            0x0000000000000001,
            0x3ff0000000000001,
            Some(0x0000000000000002),
            Some(0x3ff0000000000002),
        ),
        (
            0x0000000000000001,
            0x7fefffffffffffff,
            Some(0x3ccfffffffffffff),
            None,
        ),
        (
            0x0000000000000002,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x0000000000000003),
        ),
        (
            0x0000000000000002,
            0x0000000000000001,
            Some(0x0000000000000001),
            Some(0x0000000000000004),
        ),
        (
            0x0000000000000002,
            0x0000000000000002,
            Some(0x0000000000000001),
            Some(0x0000000000000005),
        ),
        (
            0x0000000000000002,
            0x000fffffffffffff,
            Some(0x0000000000000001),
            Some(0x0010000000000002),
        ),
        (
            0x0000000000000002,
            0x0010000000000000,
            Some(0x0000000000000001),
            Some(0x0010000000000003),
        ),
        (
            0x0000000000000002,
            0x3ff0000000000000,
            Some(0x0000000000000002),
            Some(0x3ff0000000000001),
        ),
        (
            0x0000000000000002,
            0x3ff0000000000001,
            Some(0x0000000000000003),
            Some(0x3ff0000000000002),
        ),
        (
            0x0000000000000002,
            0x7fefffffffffffff,
            Some(0x3cdfffffffffffff),
            None,
        ),
        (
            0x000fffffffffffff,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x0010000000000000),
        ),
        (
            0x000fffffffffffff,
            0x0000000000000001,
            Some(0x0000000000000001),
            Some(0x0010000000000001),
        ),
        (
            0x000fffffffffffff,
            0x0000000000000002,
            Some(0x0000000000000001),
            Some(0x0010000000000002),
        ),
        (
            0x000fffffffffffff,
            0x000fffffffffffff,
            Some(0x0000000000000001),
            Some(0x001fffffffffffff),
        ),
        (
            0x000fffffffffffff,
            0x0010000000000000,
            Some(0x0000000000000001),
            Some(0x0020000000000000),
        ),
        (
            0x000fffffffffffff,
            0x3ff0000000000000,
            Some(0x000fffffffffffff),
            Some(0x3ff0000000000001),
        ),
        (
            0x000fffffffffffff,
            0x3ff0000000000001,
            Some(0x0010000000000000),
            Some(0x3ff0000000000002),
        ),
        (
            0x000fffffffffffff,
            0x7fefffffffffffff,
            Some(0x400ffffffffffffe),
            None,
        ),
        (
            0x0010000000000000,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x0010000000000001),
        ),
        (
            0x0010000000000000,
            0x0000000000000001,
            Some(0x0000000000000001),
            Some(0x0010000000000002),
        ),
        (
            0x0010000000000000,
            0x0000000000000002,
            Some(0x0000000000000001),
            Some(0x0010000000000003),
        ),
        (
            0x0010000000000000,
            0x000fffffffffffff,
            Some(0x0000000000000001),
            Some(0x0020000000000000),
        ),
        (
            0x0010000000000000,
            0x0010000000000000,
            Some(0x0000000000000001),
            Some(0x0020000000000001),
        ),
        (
            0x0010000000000000,
            0x3ff0000000000000,
            Some(0x0010000000000000),
            Some(0x3ff0000000000001),
        ),
        (
            0x0010000000000000,
            0x3ff0000000000001,
            Some(0x0010000000000001),
            Some(0x3ff0000000000002),
        ),
        (
            0x0010000000000000,
            0x7fefffffffffffff,
            Some(0x400fffffffffffff),
            None,
        ),
        (
            0x3ff0000000000000,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x3ff0000000000001),
        ),
        (
            0x3ff0000000000000,
            0x0000000000000001,
            Some(0x0000000000000001),
            Some(0x3ff0000000000001),
        ),
        (
            0x3ff0000000000000,
            0x0000000000000002,
            Some(0x0000000000000002),
            Some(0x3ff0000000000001),
        ),
        (
            0x3ff0000000000000,
            0x000fffffffffffff,
            Some(0x000fffffffffffff),
            Some(0x3ff0000000000001),
        ),
        (
            0x3ff0000000000000,
            0x0010000000000000,
            Some(0x0010000000000000),
            Some(0x3ff0000000000001),
        ),
        (
            0x3ff0000000000000,
            0x3ff0000000000000,
            Some(0x3ff0000000000000),
            Some(0x4000000000000001),
        ),
        (
            0x3ff0000000000000,
            0x3ff0000000000001,
            Some(0x3ff0000000000001),
            Some(0x4000000000000001),
        ),
        (
            0x3ff0000000000000,
            0x7fefffffffffffff,
            Some(0x7fefffffffffffff),
            None,
        ),
        (
            0x3ff0000000000001,
            0x0000000000000000,
            Some(0x0000000000000000),
            Some(0x3ff0000000000002),
        ),
        (
            0x3ff0000000000001,
            0x0000000000000001,
            Some(0x0000000000000002),
            Some(0x3ff0000000000002),
        ),
        (
            0x3ff0000000000001,
            0x0000000000000002,
            Some(0x0000000000000003),
            Some(0x3ff0000000000002),
        ),
        (
            0x3ff0000000000001,
            0x000fffffffffffff,
            Some(0x0010000000000000),
            Some(0x3ff0000000000002),
        ),
        (
            0x3ff0000000000001,
            0x0010000000000000,
            Some(0x0010000000000001),
            Some(0x3ff0000000000002),
        ),
        (
            0x3ff0000000000001,
            0x3ff0000000000000,
            Some(0x3ff0000000000001),
            Some(0x4000000000000001),
        ),
        (
            0x3ff0000000000001,
            0x3ff0000000000001,
            Some(0x3ff0000000000003),
            Some(0x4000000000000002),
        ),
        (0x3ff0000000000001, 0x7fefffffffffffff, None, None),
        (
            0x7fefffffffffffff,
            0x0000000000000000,
            Some(0x0000000000000000),
            None,
        ),
        (
            0x7fefffffffffffff,
            0x0000000000000001,
            Some(0x3ccfffffffffffff),
            None,
        ),
        (
            0x7fefffffffffffff,
            0x0000000000000002,
            Some(0x3cdfffffffffffff),
            None,
        ),
        (
            0x7fefffffffffffff,
            0x000fffffffffffff,
            Some(0x400ffffffffffffe),
            None,
        ),
        (
            0x7fefffffffffffff,
            0x0010000000000000,
            Some(0x400fffffffffffff),
            None,
        ),
        (
            0x7fefffffffffffff,
            0x3ff0000000000000,
            Some(0x7fefffffffffffff),
            None,
        ),
        (0x7fefffffffffffff, 0x3ff0000000000001, None, None),
        (0x7fefffffffffffff, 0x7fefffffffffffff, None, None),
        (
            0x1e14c1df32b7eb67,
            0x58f5a9f6bd147bdf,
            Some(0x371c1af4d22d76fc),
            Some(0x58f5a9f6bd147be0),
        ),
        (
            0x45a1bd06d6f37315,
            0x69dc42e529de3bce,
            Some(0x6f8f54f5c43d5caf),
            Some(0x69dc42e529de3bcf),
        ),
        (
            0x32ffc4f8841a1663,
            0x00758dfe049896e7,
            Some(0x0000000000000001),
            Some(0x32ffc4f8841a1664),
        ),
        (
            0x0f44b3af157d881f,
            0x69e910987501504d,
            Some(0x3940371d418648e8),
            Some(0x69e910987501504e),
        ),
        (
            0x59dafd6f66bb2720,
            0x7bdaf27a12034453,
            None,
            Some(0x7bdaf27a12034454),
        ),
        (
            0x3c085d7ec865e9bb,
            0x5d502e64cc7f5fdd,
            Some(0x5968a42514a87bce),
            Some(0x5d502e64cc7f5fde),
        ),
        (
            0x7379354794a89760,
            0x0890bd8e67b2714e,
            Some(0x3c1a5fed4e700641),
            Some(0x7379354794a89761),
        ),
        (
            0x790e76d10ab72b48,
            0x1a967111d5ad54f5,
            Some(0x53b55d544416b4ef),
            Some(0x790e76d10ab72b49),
        ),
        (
            0x47af280bbabd5668,
            0x1df0c52f6a03ee99,
            Some(0x25b054028f9dfe01),
            Some(0x47af280bbabd5669),
        ),
        (
            0x3555abfd56407372,
            0x0b1c4f0d8c08c319,
            Some(0x00832c07719aa2a5),
            Some(0x3555abfd56407373),
        ),
        (
            0x50b0a66a03cac061,
            0x5912f88f59c516a1,
            Some(0x69d3bddfdc3d2732),
            Some(0x5912f88f59c516a2),
        ),
        (
            0x54f8810202bf0b6b,
            0x40f703cfeaebab2f,
            Some(0x56019fa4c0926913),
            Some(0x54f8810202bf0b6c),
        ),
        (
            0x007756f928519d84,
            0x72cc29c001c3ee89,
            Some(0x33548a8d7da3a412),
            Some(0x72cc29c001c3ee8a),
        ),
        (
            0x0e72468450ddfafb,
            0x7a802b184971bb78,
            Some(0x490277bd92216cb4),
            Some(0x7a802b184971bb79),
        ),
        (
            0x130f0192f1925d73,
            0x2fee14a73fa050a2,
            Some(0x030d257ccc2d7f16),
            Some(0x2fee14a73fa050a3),
        ),
        (
            0x1cd97741ba5d4455,
            0x6ffd93d326ff751e,
            Some(0x4ce789b77036f0cb),
            Some(0x6ffd93d326ff751f),
        ),
        (
            0x2ae0cdbd939da8a2,
            0x14a94c27b30e8d35,
            Some(0x00001a91732cae9e),
            Some(0x2ae0cdbd939da8a3),
        ),
        (
            0x0ea67c3523d9183d,
            0x761964445d6b5c9a,
            Some(0x44d1d77db3a6f85c),
            Some(0x761964445d6b5c9b),
        ),
        (
            0x5c5d0bd8dad67520,
            0x481cee444497234f,
            Some(0x648a42a3d3c66f50),
            Some(0x5c5d0bd8dad67521),
        ),
        (
            0x7c00a178e98d4d09,
            0x59d31f8813d0a5a2,
            None,
            Some(0x7c00a178e98d4d0a),
        ),
        (
            0x263bbd3068423790,
            0x6bb0413a9a5064ad,
            Some(0x51fc2e46964190ea),
            Some(0x6bb0413a9a5064ae),
        ),
        (
            0x19b7b224d143a01a,
            0x0165f75fe299c99c,
            Some(0x0000000000000001),
            Some(0x19b7b224d143a01b),
        ),
        (
            0x58c28aaeb07713b7,
            0x34c5ff5d30c5acca,
            Some(0x4d997df386553534),
            Some(0x58c28aaeb07713b8),
        ),
        (
            0x2d3b3176f09ec037,
            0x1becffd5ce90505f,
            Some(0x0938a4afef211b6e),
            Some(0x2d3b3176f09ec038),
        ),
        (
            0x6549797e3d6a6a81,
            0x7b0537e3bbd836f7,
            None,
            Some(0x7b0537e3bbd836f8),
        ),
        (
            0x3b8bbfe507c4f700,
            0x76869f95022c94a1,
            Some(0x72239e5026bb17b7),
            Some(0x76869f95022c94a2),
        ),
        (
            0x36b01599fe419fd4,
            0x120289ac726e2bbc,
            Some(0x08c2a2b38fdafca6),
            Some(0x36b01599fe419fd5),
        ),
        (
            0x0800247f1281a7fa,
            0x44ed643569f39d0b,
            Some(0x0cfda7404f88e2c2),
            Some(0x44ed643569f39d0c),
        ),
        (
            0x7804a4d869e9f8dd,
            0x3b3934efaed29390,
            Some(0x735042ef92636f6b),
            Some(0x7804a4d869e9f8de),
        ),
        (
            0x5463e746c0715d9b,
            0x2dd5839525b71047,
            Some(0x424ac33bf889d840),
            Some(0x5463e746c0715d9c),
        ),
        (
            0x491b06f77cf06eca,
            0x0f8df37aec7fcf2e,
            Some(0x18b94bf502e58661),
            Some(0x491b06f77cf06ecb),
        ),
        (
            0x7169074ddfe7a1bb,
            0x136ce4aa9178cf47,
            Some(0x44e6993d975b4bc4),
            Some(0x7169074ddfe7a1bc),
        ),
        (
            0x675b4f86f0c4ded9,
            0x3d809336a53a79d3,
            Some(0x64ec4acedef84bff),
            Some(0x675b4f86f0c4deda),
        ),
        (
            0x7f373395edbad3ca,
            0x60934def1d9f089f,
            None,
            Some(0x7f373395edbad3cb),
        ),
        (
            0x0a4b341bdadc9113,
            0x4a070eed184bbb09,
            Some(0x14639a2460140bbd),
            Some(0x4a070eed184bbb0a),
        ),
        (
            0x1ba58a2050d87045,
            0x132176b02c8f040b,
            Some(0x0000000000000001),
            Some(0x1ba58a2050d87046),
        ),
        (
            0x044696ceeca9e87c,
            0x23a82c9f981c63e9,
            Some(0x0000000000000001),
            Some(0x23a82c9f981c63ea),
        ),
        (
            0x24e2f0b4be902c75,
            0x6cc7800493d19287,
            Some(0x51bbd18ee30c8334),
            Some(0x6cc7800493d19288),
        ),
        (
            0x31be23921ba29e40,
            0x4b473dd6511f23eb,
            Some(0x3d15e3ceacaa06ab),
            Some(0x4b473dd6511f23ec),
        ),
        (
            0x4ff3f108b47aac5d,
            0x6aa0d78ae01a34ee,
            Some(0x7aa4fdacafae14f1),
            Some(0x6aa0d78ae01a34ef),
        ),
        (
            0x1c6c501b45b372b2,
            0x01a48b91afde62af,
            Some(0x0000000000000001),
            Some(0x1c6c501b45b372b3),
        ),
        (
            0x22a05475fb83ade1,
            0x595ac6798ebcbe19,
            Some(0x3c0b53d0fd28efb1),
            Some(0x595ac6798ebcbe1a),
        ),
        (
            0x28439aa40bcb1e76,
            0x1307fe164a6e6ff1,
            Some(0x0000000000000001),
            Some(0x28439aa40bcb1e77),
        ),
        (
            0x34f06c9efed7f618,
            0x6b73f608142a485f,
            Some(0x60747d8b26315a3b),
            Some(0x6b73f608142a4860),
        ),
        (
            0x489f43e2559e4d15,
            0x520c1729a6c579ee,
            Some(0x5abb720787832214),
            Some(0x520c1729a6c579ef),
        ),
        (
            0x6c5d233d42db4c15,
            0x313d400eb7f55ba7,
            Some(0x5daaa24366083063),
            Some(0x6c5d233d42db4c16),
        ),
        (
            0x7a4b5d6de1e2e0fa,
            0x48b69fcdce093260,
            None,
            Some(0x7a4b5d6de1e2e0fb),
        ),
        (
            0x072bdf0fd674a571,
            0x4eee53d76e643698,
            Some(0x162a6a250cfa1197),
            Some(0x4eee53d76e643699),
        ),
        (
            0x415c1c6ddd1638c3,
            0x6f93e0107648a5e7,
            Some(0x710175b6b27062a1),
            Some(0x6f93e0107648a5e8),
        ),
        (
            0x4d674000a80223da,
            0x76d35940f3e72527,
            None,
            Some(0x76d35940f3e72528),
        ),
        (
            0x0815afd3c1eb0758,
            0x27c52fcb3aadec7f,
            Some(0x0000000000000001),
            Some(0x27c52fcb3aadec80),
        ),
        (
            0x08342bb3953f38c0,
            0x54e5da9bfdbca2ec,
            Some(0x1d2b8cf3c9f10440),
            Some(0x54e5da9bfdbca2ed),
        ),
        (
            0x14776c2e4838c43a,
            0x4c6897d24047e28c,
            Some(0x20f20043158c1368),
            Some(0x4c6897d24047e28d),
        ),
        (
            0x19f43e99520159ff,
            0x0c50b78289be9a30,
            Some(0x0000000000000001),
            Some(0x19f43e9952015a00),
        ),
        (
            0x20b3b14903307b17,
            0x17e03a1ca5cb7113,
            Some(0x0000000000000001),
            Some(0x20b3b14903307b18),
        ),
        (
            0x08ef2e045830e0e9,
            0x41a7871907eeed9a,
            Some(0x0aa6ecb5a5657379),
            Some(0x41a7871907eeed9b),
        ),
        (
            0x43c2720f29b1d4ad,
            0x2f13781dcab28a9e,
            Some(0x32e671ebcba53200),
            Some(0x43c2720f29b1d4ae),
        ),
        (
            0x1f14d4c069b24d7d,
            0x042a240fea98575a,
            Some(0x0000000000000001),
            Some(0x1f14d4c069b24d7e),
        ),
        (
            0x26bdd27ef6f335f1,
            0x494242d6993ea82b,
            Some(0x301104b18f480b0e),
            Some(0x494242d6993ea82c),
        ),
        (
            0x1679aa7860758b66,
            0x7e78facff51ee5f0,
            Some(0x55040904e01e60b6),
            Some(0x7e78facff51ee5f1),
        ),
        (
            0x2f27f35569148f18,
            0x7626f920f17d9aad,
            Some(0x656131c0d0ebd0f9),
            Some(0x7626f920f17d9aae),
        ),
        (
            0x02b8fef331f932e9,
            0x161744a438bbb1b5,
            Some(0x0000000000000001),
            Some(0x161744a438bbb1b6),
        ),
        (
            0x3f264fe9b297eb7a,
            0x13b03343d03c421c,
            Some(0x12e69766fc86b184),
            Some(0x3f264fe9b297eb7b),
        ),
        (
            0x7d42a9e9a20deee9,
            0x7f80203059681946,
            None,
            Some(0x7f802030596943e5),
        ),
        (
            0x3cff89f8637b6b63,
            0x3f7019b9dae50d21,
            Some(0x3c7fbcae525a335e),
            Some(0x3f7019b9dae52cab),
        ),
        (
            0x798d4764731a53aa,
            0x70d8ab12a99eb0cb,
            None,
            Some(0x798d4764731a53ab),
        ),
        (
            0x254b680bc66a8821,
            0x32272dbc557fe470,
            Some(0x1783d9f413aaad35),
            Some(0x32272dbc557fe471),
        ),
        (
            0x458f4e911a472b06,
            0x26b8a2c4a611ca00,
            Some(0x2c581a2af5fc2198),
            Some(0x458f4e911a472b07),
        ),
        (
            0x2091ddf2e1b3504d,
            0x3492cc77dc34ea7d,
            Some(0x1534fe04ef4cba0b),
            Some(0x3492cc77dc34ea7e),
        ),
        (
            0x2a99110bb4e7347d,
            0x063d43f35af9d728,
            Some(0x0000000000000001),
            Some(0x2a99110bb4e7347e),
        ),
        (
            0x4195dd912bb6f27d,
            0x559cef52c6638fb3,
            Some(0x5743c56669d18c7e),
            Some(0x559cef52c6638fb4),
        ),
        (
            0x62d788b7c1c6f2c1,
            0x3fac2238d89b3ab6,
            Some(0x6294b0cbdb5a8cab),
            Some(0x62d788b7c1c6f2c2),
        ),
        (
            0x530c07ab017c2eed,
            0x2edd8bc158e575aa,
            Some(0x41f9e15da444731d),
            Some(0x530c07ab017c2eee),
        ),
        (
            0x2502a8d101bf661b,
            0x6f2b2cd270774238,
            Some(0x543fb1265c97cd6f),
            Some(0x6f2b2cd270774239),
        ),
        (
            0x35d44331b54ed27d,
            0x23393fe1bca3aeda,
            Some(0x191ff9e41ed4e6f1),
            Some(0x35d44331b54ed27e),
        ),
        (
            0x69be8e05ce0e47fb,
            0x06e0cb2a4a82de6a,
            Some(0x30b009003d674fcc),
            Some(0x69be8e05ce0e47fc),
        ),
        (
            0x33c906276ad8821f,
            0x7e74cee6da78d8e9,
            Some(0x725045a4c79ae049),
            Some(0x7e74cee6da78d8ea),
        ),
        (
            0x3f04ac5c61624c5a,
            0x28427ee165a76fed,
            Some(0x2757e5d88038f43e),
            Some(0x3f04ac5c61624c5b),
        ),
        (
            0x2f29e8cd37c88e0d,
            0x5b9c064005dc6080,
            Some(0x4ad6b0c30da3302d),
            Some(0x5b9c064005dc6081),
        ),
        (
            0x2ca3f454236f95df,
            0x29fdfe6a8fc801d6,
            Some(0x16b2b4120ef5ab1b),
            Some(0x2ca3f454236f999f),
        ),
        (
            0x1a5a58292a12e8b4,
            0x049cdf322628936d,
            Some(0x0000000000000001),
            Some(0x1a5a58292a12e8b5),
        ),
        (
            0x022f314ff57d5c37,
            0x7de9e797fbca04f6,
            Some(0x40294046971f16b1),
            Some(0x7de9e797fbca04f7),
        ),
        (
            0x4bcbf7a7483b2a60,
            0x49ce869a0f2a1f3f,
            Some(0x55aaadd0854be1dd),
            Some(0x4bcbf7a74859b0fb),
        ),
        (
            0x37be91e7024a654f,
            0x1fa2e2231fc59290,
            Some(0x17720a19eeb8c6ed),
            Some(0x37be91e7024a6550),
        ),
        (
            0x3ff9aad67a26435c,
            0x164e08ae165ad7ce,
            Some(0x1658171f6afef1f0),
            Some(0x3ff9aad67a26435d),
        ),
        (
            0x1a9ca6b3b2722423,
            0x4559d50f457b1698,
            Some(0x200720ffabded818),
            Some(0x4559d50f457b1699),
        ),
        (
            0x71fe9de609f1343a,
            0x618ced671552302d,
            None,
            Some(0x71fe9de609f1343b),
        ),
        (
            0x0bea4d22585cc8b1,
            0x736061ccf40390f8,
            Some(0x3f5aede6e1288a59),
            Some(0x736061ccf40390f9),
        ),
        (
            0x712b888fd8ecb9c3,
            0x0954ae5d09cb0d4a,
            Some(0x3a91cb60830ea7f1),
            Some(0x712b888fd8ecb9c4),
        ),
        (
            0x018ac9dcff27c830,
            0x5521dc1d8f6be511,
            Some(0x16bde703ebd002d0),
            Some(0x5521dc1d8f6be512),
        ),
        (
            0x4e0655348b22bed2,
            0x217433eac7a3de61,
            Some(0x2f8c32f8fa2fd813),
            Some(0x4e0655348b22bed3),
        ),
        (
            0x730004d9a1f9a596,
            0x4ee90d54da62dab9,
            None,
            Some(0x730004d9a1f9a597),
        ),
        (
            0x13b641e174d4bdaa,
            0x3041de7d346986c2,
            Some(0x0408db7fcff15a94),
            Some(0x3041de7d346986c3),
        ),
        (
            0x09986c4f138daa1c,
            0x30146570995132d1,
            Some(0x0000000000000001),
            Some(0x30146570995132d2),
        ),
        (
            0x0e4763221e174bac,
            0x0fce64ce62412cf7,
            Some(0x0000000000000001),
            Some(0x0fce64ce79a44f16),
        ),
        (
            0x58c821e97a783236,
            0x62b626ea5c5d45c7,
            Some(0x7b90b4a98717373e),
            Some(0x62b626ea5c5d45c8),
        ),
    ];
    for &(a, b, product, total) in cases {
        assert_eq!(
            rp::upward_product(f64::from_bits(a), f64::from_bits(b))
                .ok()
                .map(f64::to_bits),
            product,
            "product {a:016x} {b:016x}"
        );
        assert_eq!(
            rp::upward_small_sum(f64::from_bits(a), f64::from_bits(b))
                .ok()
                .map(f64::to_bits),
            total,
            "single-round sum {a:016x} {b:016x}"
        );
    }
}

#[test]
fn audit_mutations_retain_native_and_product_first_failures() {
    use serde_json::json;
    let shared = corpus();
    let c = &shared["cases"][0];
    let mutations = [
        (
            "residual basis",
            json!([
                "retained_precision",
                "body",
                "cases",
                0,
                "run",
                "records",
                0,
                "residual_basis"
            ]),
            json!(128),
            "RETAINED_PRECISION_ATTEMPT_MISMATCH",
        ),
        (
            "refinement count",
            json!([
                "retained_precision",
                "body",
                "cases",
                0,
                "run",
                "records",
                0,
                "corrections"
            ]),
            json!(4),
            "RETAINED_PRECISION_ATTEMPT_MISMATCH",
        ),
        (
            "stop stage",
            json!([
                "retained_precision",
                "body",
                "cases",
                0,
                "run",
                "records",
                0,
                "work",
                "stop_rule_lme"
            ]),
            json!(0),
            "RETAINED_PRECISION_WORK_MISMATCH",
        ),
        (
            "missing entered lane",
            json!([
                "retained_precision",
                "body",
                "product_attempts",
                0,
                "proof",
                "lanes"
            ]),
            json!([]),
            "RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH",
        ),
        (
            "missing completed projection",
            json!([
                "retained_precision",
                "body",
                "product_attempts",
                0,
                "proof",
                "projection_outcomes"
            ]),
            json!([]),
            "RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH",
        ),
        (
            "unmerged completed values",
            json!([
                "retained_precision",
                "body",
                "product_attempts",
                0,
                "proof",
                "completion"
            ]),
            json!({"kind":"not_entered"}),
            "RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH",
        ),
    ];
    for (name, path, value, code) in mutations {
        let mut source = c["source"].clone();
        edit(&mut source, &json!({"path":path,"op":"set","value":value}));
        rehash(&mut source);
        let got = rp::validate(&source, Some(&c["invocation"])).unwrap_err();
        assert_eq!((got.gate, got.code.as_str()), ("G5", code), "{name}");
    }
    let mut source = c["source"].clone();
    source["retained_precision"]["body"]["product_attempts"][0]["preparation"]["members"][0]
        ["work"]["conversions"]["value"] = json!(8);
    source["retained_precision"]["body"]["product_attempts"][0]["proof"]["completion"] =
        json!({"kind":"not_entered"});
    rehash(&mut source);
    let got = rp::validate(&source, Some(&c["invocation"])).unwrap_err();
    assert_eq!(
        (got.gate, got.code.as_str()),
        ("G5", "RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"),
        "C3 association must precede earlier member work defect"
    );
}

#[test]
fn negative_zero_wire_scale_remains_g2() {
    let shared = corpus();
    let c = &shared["cases"][0];
    let mut source = c["source"].clone();
    source["retained_precision"]["body"]["cases"][0]["selection"]["body_scales"][0]
        ["translation"] = "8000000000000000".into();
    source["results"][0]["recovery_method"] = "wrong".into();
    rehash(&mut source);
    let got = rp::validate(&source, Some(&c["invocation"])).unwrap_err();
    assert_eq!(
        (got.gate, got.code.as_str()),
        ("G2", "RETAINED_PRECISION_ENCODING_MISMATCH")
    );
}
