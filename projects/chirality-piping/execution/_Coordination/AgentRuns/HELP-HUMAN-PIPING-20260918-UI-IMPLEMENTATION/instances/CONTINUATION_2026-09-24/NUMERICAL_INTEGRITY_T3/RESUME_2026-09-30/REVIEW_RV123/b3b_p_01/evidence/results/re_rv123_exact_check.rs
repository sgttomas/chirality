//! RV123 (RV-P2 round 1): independent checks of B3b-P's exact successor fixtures, outside PP:
//! the receipt, publication, preparation (route H) and source-identity hashes recomputed with
//! RE's own domain hash; today's RS outcome; and G7's projection to physics-1 through physics-1's
//! base validator. Scratch only; not part of the candidate.
use open_pipe_stress_result_export::{retained_precision as rp, rv123_exact_reader as xr, semantic_contract as sc, source_blocks::domain_hash};
use serde_json::{json, Value};

const FIX: [(&str, &str); 2] = [
    ("sparse_interactive", include_str!("../../../../fixtures/results/retained_precision_exact_successor_sparse_interactive.json")),
    ("dense_scrutiny", include_str!("../../../../fixtures/results/retained_precision_exact_successor_dense_scrutiny.json")),
];
const MILESTONE: [(&str, &str); 2] = [
    ("sparse_interactive", include_str!("../../../../fixtures/results/retained_precision_milestone_successor_sparse_interactive.json")),
    ("dense_scrutiny", include_str!("../../../../fixtures/results/retained_precision_milestone_successor_dense_scrutiny.json")),
];
const DEF_E: &str = include_str!("../../../../fixtures/results/retained_precision_prepared_exact_v1.json");
const DEF_O: &str = include_str!("../../../../fixtures/results/retained_precision_prepared_ordinary_v1.json");

fn prep_payload(a: &Value, h: &str) -> Value {
    let members: Vec<Value> = a["preparation"]["members"].as_array().unwrap().iter().map(|m| json!({
        "member":m["member"],"old_source":m["old_source"],"old_facts":m["old_facts"],"section":m["result"]["section"]})).collect();
    json!({"definition_id":a["definition_id"],"definition_sha256":h,"owner_ref":a["owner_ref"],"ordinary_attempt_ref":a["ordinary_attempt_ref"],
        "material_basis_ref":a["material_basis_ref"],"members":members})
}

fn project_to_physics_1(src: &Value) -> Value {
    let mut p = src.clone();
    p.as_object_mut().unwrap().remove("retained_precision");
    p["producer"]["semantic_contract_id"] = json!("openpipestress.result_semantics/0.3.0/physics-1");
    p["formulation_basis"]["profile_id"] = json!("exact_straight_pressure_v2");
    for r in p["results"].as_array_mut().unwrap() {
        r.as_object_mut().unwrap().remove("recovery_method");
    }
    p
}

#[test]
fn rv123_exact_fixture_checks() {
    let def_e: Value = serde_json::from_str(DEF_E).unwrap();
    let def_o: Value = serde_json::from_str(DEF_O).unwrap();
    let he = domain_hash("retained_precision_formation_v1", &def_e).unwrap();
    let ho = domain_hash("retained_precision_formation_v1", &def_o).unwrap();
    println!("RV123_H DEF-E {he} DEF-O {ho}");
    assert_eq!(he, "5a3bac430df9bbc77484d5419c75880ad40ae209b439e5f928374458025281af");
    assert_eq!(ho, "a7ed7ca0bf0bba6e8b821ca4befa00a0fa9541a83694be8b28ac63e39b1d0349");
    for (name, text) in FIX {
        let doc: Value = serde_json::from_str(text).unwrap();
        let (src, inv) = (&doc["source"], &doc["invocation"]);
        let r = &src["retained_precision"];
        let body = &r["body"];
        let receipt = domain_hash("retained_precision_receipt_mp_v2", body).unwrap();
        assert_eq!(receipt, r["receipt_sha256"].as_str().unwrap(), "{name} receipt");
        let mut public = src.clone();
        public.as_object_mut().unwrap().remove("retained_precision");
        let publication = domain_hash("retained_precision_publication_mp_v2", &public).unwrap();
        assert_eq!(publication, body["publication_sha256"].as_str().unwrap(), "{name} publication");
        let mut preps = 0;
        for s in body["sources"].as_array().unwrap() {
            let a = &body["product_attempts"][s["preparation"]["attempt_ref"].as_u64().unwrap() as usize];
            let with_e = domain_hash("retained_precision_preparation_v1", &prep_payload(a, &he)).unwrap();
            let with_o = domain_hash("retained_precision_preparation_v1", &prep_payload(a, &ho)).unwrap();
            assert_eq!(s["preparation"]["sha256"].as_str().unwrap(), with_e, "{name} preparation with DEF-E's H");
            assert_ne!(with_e, with_o);
            preps += 1;
        }
        let mut idents = 0;
        for c in body["cases"].as_array().unwrap() {
            if let Some(h) = c.get("source_identity_sha256") {
                let mut x = body["sources"][c["source_ref"].as_u64().unwrap() as usize].clone();
                x.as_object_mut().unwrap().remove("index");
                assert_eq!(domain_hash("retained_precision_source_mp_v2", &x).unwrap(), h.as_str().unwrap(), "{name} source identity");
                idents += 1;
            }
        }
        // Today's RS (no <physics-retained> branch yet).
        let today = rp::validate(src, Some(inv)).err().map(|e| (e.gate, e.code));
        // G7's projection through physics-1's base validator.
        let projected = project_to_physics_1(src);
        let base = sc::for_source(&projected).map(|(_, id)| id.to_owned());
        let bases: Vec<Value> = inv["request"]["model"]["load_cases"].as_array().unwrap().iter().map(|c| json!({"ref_type":"load_case","ref_id":c["id"]})).collect();
        let standing = sc::numerical_use_standing_with_context(&projected, &bases, Some(inv));
        println!("RV123_EXACT {name} receipt={receipt} publication={publication} preparations={preps} identities={idents} rs_today={today:?} physics1_base={base:?} standing={standing}");
        assert_eq!(today, Some(("G0", "SOURCE_PRODUCER_CONTRACT_UNSUPPORTED".to_owned())), "{name}");
        assert!(base.is_ok(), "{name}: physics-1's base validator: {base:?}");
        // RV123 scratch: today's RS gates with only the identity, table, definition and the G7
        // projection switched to the exact route's (no exact-specific gate added): G0-G7 without
        // the invocation, then with it (G8 is expected to refuse on the preview-only predicates).
        let without = xr::validate(src, None).map(|v| (v.numerical_eligible, v.classifications.len())).map_err(|e| (e.gate, e.code, e.detail));
        let with = xr::validate(src, Some(inv)).map(|v| v.numerical_eligible).map_err(|e| (e.gate, e.code, e.detail));
        println!("RV123_PATCHED_RS {name} without_invocation={without:?} with_invocation={with:?}");
    }
    // Control: the preview milestone successor validates in RS today.
    for (name, text) in MILESTONE {
        let doc: Value = serde_json::from_str(text).unwrap();
        let v = rp::validate(&doc["source"], Some(&doc["invocation"]));
        println!("RV123_MILESTONE {name} rs={:?}", v.as_ref().map(|v| v.numerical_eligible).map_err(|e| (e.gate, e.code.clone())));
        assert!(v.is_ok());
    }
}
