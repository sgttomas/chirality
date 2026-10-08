"""I103: B3b-A's source edit (applied after B2-A's commit). Run from PP's manifest dir."""
import pathlib

p = pathlib.Path('src/retained_memory.rs'); t = p.read_text()
def rep(old, new, count=1):
    global t
    assert t.count(old) == count, (old[:90], t.count(old)); t = t.replace(old, new)

rep('''    /// L3 (B3a): schema 0.3.0 with the `legacy_pressure_v1` contract, version 1.0.0.
    LegacyPressure,
}''', '''    /// L3 (B3a): schema 0.3.0 with the `legacy_pressure_v1` contract, version 1.0.0.
    LegacyPressure,
    /// E (B3b): schema 0.3.0 with the `exact_straight_pressure_v2` contract, version 2.0.0.
    /// Its own D1.4 and D1.5 clauses apply (B3-D §4.2).
    Exact,
}''')
rep('''        ("0.3.0", Some(c)) if contract_is(c, "1.0.0", "legacy_pressure_v1") => Ok(NamespaceBranch::LegacyPressure),
''', '''        ("0.3.0", Some(c)) if contract_is(c, "1.0.0", "legacy_pressure_v1") => Ok(NamespaceBranch::LegacyPressure),
        ("0.3.0", Some(c)) if contract_is(c, "2.0.0", "exact_straight_pressure_v2") => Ok(NamespaceBranch::Exact),
''')
rep('''    // D1.3: the namespace branch, decided once from (schema, contract) (B3-D §4.1, §4.3):
    // branch L, 0.1.0 or 0.2.0 with no pressure contract; or branch L3 (B3a), 0.3.0 with
    // exactly `{version "1.0.0", mode "legacy_pressure_v1"}`. A schema in no branch refuses
    // with `SchemaVersion`, a contract that does not match its schema's branch with
    // `PressureContract`. Then, on every branch, no sections (S-4).
    match namespace_branch(m) {
        Ok(NamespaceBranch::Legacy | NamespaceBranch::LegacyPressure) => {}
        Err(fact) => return refuse(C::Namespace, fact),
    }''', '''    // D1.3: the namespace branch, decided once from (schema, contract) (B3-D §4.1–§4.3):
    // branch L, 0.1.0 or 0.2.0 with no pressure contract; branch L3 (B3a), 0.3.0 with
    // exactly `{version "1.0.0", mode "legacy_pressure_v1"}`; or branch E (B3b), 0.3.0 with
    // exactly `{version "2.0.0", mode "exact_straight_pressure_v2"}` (0.4.0 stays out). A
    // schema in no branch refuses with `SchemaVersion`, a contract that does not match its
    // schema's branch with `PressureContract`. Then, on every branch, no sections (S-4).
    let exact = match namespace_branch(m) {
        Ok(branch) => branch == NamespaceBranch::Exact,
        Err(fact) => return refuse(C::Namespace, fact),
    };''')
rep('''    if m.load_cases.is_empty() || m.load_cases.len() > caps::LOAD_CASES {
        return refuse(C::Invocation, F::LoadCases);
    }
    if m.combinations.iter().any(''', '''    if m.load_cases.is_empty() || m.load_cases.len() > caps::LOAD_CASES {
        return refuse(C::Invocation, F::LoadCases);
    }
    // D1.4's exact clause (B3-D §4.2; RR "I95's B3-S: …", ruling 4): no combination on the
    // exact route, which the ordinary route also blocks, so its forms never price
    // combination text. B2-C's combination clauses apply on L and L3 only.
    if exact && !m.combinations.is_empty() {
        return refuse(C::Invocation, F::Combinations);
    }
    if m.combinations.iter().any(''')
rep('''    // D1.5 (B1 SA): every case, in request order.
    for case in &m.load_cases {
        if case.pressure_regions.is_some() {
            return refuse(C::Case, F::PressureRegions);
        }''', '''    // D1.5 (B1 SA): every case, in request order. B3b (B3-D §4.2): on branch E every case's
    // `pressure_regions` is explicitly empty (`Some([])`, as physics-source-1 requires); absent
    // or non-empty refuses. On L and L3 it is absent.
    for case in &m.load_cases {
        let regions_in_domain = match &case.pressure_regions {
            Some(regions) => exact && regions.is_empty(),
            None => !exact,
        };
        if !regions_in_domain {
            return refuse(C::Case, F::PressureRegions);
        }''')
rep('''    /// B2-A: no longer a D1.4 refusal on L and L3 (combinations are counted by D1.9); kept for
    /// the exact route's D1.4 clause (B3b-A, B3-D §4.2).
    #[allow(dead_code)]
    Combinations,''', '''    /// B3b-A (B3-D §4.2; RR "I95's B3-S: …", ruling 4): the exact route's D1.4 clause. On L and
    /// L3 combinations are counted by D1.9 (B2-A).
    Combinations,''')
p.write_text(t)

p = pathlib.Path('src/retained_memory_law_tests.rs'); t = p.read_text()
rep('''        ("0.3.0, the exact contract (B3b)", "0.3.0", json!({"version": "2.0.0", "mode": "exact_straight_pressure_v2"}), F::PressureContract),
''', '')
rep('''    assert_eq!(contract("0.3.0", legacy.clone()), None);
''', '''    assert_eq!(contract("0.3.0", legacy.clone()), None);
    // B3b: the exact contract is branch E, whose D1.5 needs explicitly empty regions.
    assert_eq!(contract("0.3.0", json!({"version": "2.0.0", "mode": "exact_straight_pressure_v2"})), family(C::Case, F::PressureRegions));
''')
t += '''
// ---- B3b-A: D1.3, D1.4 and D1.5 for the exact route (B3-D §4.2; provisional on B1's M) ---

/// `raw` authored as 0.3.0 exact: I99's `exact` (B3-W's `m3x` when `raw` is the milestone):
/// the exact contract, the common E/ν basis with E = 2e11 Pa and ν = 0.25 and no shear
/// modulus, and explicitly empty pressure regions on every case.
fn exact3(mut raw: Value) -> Value {
    let m = &mut raw["model"];
    m["schema_version"] = json!("0.3.0");
    m["pressure_contract"] = json!({"version": "2.0.0", "mode": "exact_straight_pressure_v2"});
    for material in m["materials"].as_array_mut().unwrap() {
        material.as_object_mut().unwrap().remove("shear_modulus");
        material["constitutive_basis"] = json!("homogeneous_isotropic_E_nu_v1");
        material["poisson_ratio"] = json!({"value": 0.25, "unit": "1"});
    }
    for case in m["load_cases"].as_array_mut().unwrap() {
        case["pressure_regions"] = json!([]);
    }
    raw
}
/// The committed physics-source requests n05 and n06 (B3b's coexistence pins).
const N05: &str = include_str!("../../../fixtures/product_preview/physics_source/n05.request.json");
const N06: &str = include_str!("../../../fixtures/product_preview/physics_source/n06.request.json");

/// B3-D §4.2's law tests: 0.3.0 exact with `[]` on every case is inside D1 (alone, with C cases,
/// and as B3-W's mixed base `m3x_mix_anchor`), with a permit in the registered build; refused:
/// regions absent or with one region (`PressureRegions`), on any case; one combination
/// (`Combinations`); 0.4.0 exact (`SchemaVersion`); 0.3.0 without a contract
/// (`PressureContract`); a point basis (`ModulusBasisRef`).
#[test]
fn b3b_d1_admits_the_exact_route_with_empty_regions() {
    use D1Clause as C;
    use FamilyFact as F;
    let registered = COMPILED_IDENTITY == Some(REGISTERED_PROFILES[0].identity);
    let mut mix = milestone();
    mix["model"]["load_cases"].as_array_mut().unwrap().push(json!({"id": "case:b", "label": "I99 B3-W second case (anchor)",
        "kind": "primitive_user_load", "primitive_loads": [{"id": "load:b:0", "category": "concentrated_force", "target": {"type": "node", "node": "N0"},
        "direction": "global_x", "magnitude": {"value": 1.0, "unit": "N"}, "dimension": "force"}]}));
    for (label, raw) in [("m3x", exact3(milestone())), ("C cases", exact3(milestone_cases(caps::LOAD_CASES))), ("m3x_mix_anchor", exact3(mix))] {
        for mode in MODES {
            let (request, capture) = CapturedInvocation::parse(raw.clone(), mode).unwrap();
            assert_eq!(namespace_branch(&request.model), Ok(NamespaceBranch::Exact), "{label}");
            let admitted = admit(&capture, &request, Entry::Direct);
            let report = match &admitted {
                Ok((_, report)) | Err(report) => *report,
            };
            assert_eq!(report.law().domain, None, "{label} {mode:?}: branch E is inside D1");
            assert_eq!(admitted.is_ok(), registered, "{label} {mode:?}");
        }
    }
    let with = |change: &dyn Fn(&mut Value)| {
        let mut raw = exact3(milestone_cases(caps::LOAD_CASES));
        change(&mut raw);
        domain(raw)
    };
    let last = caps::LOAD_CASES - 1;
    for case in [0, last] {
        assert_eq!(with(&|r| { r["model"]["load_cases"][case].as_object_mut().unwrap().remove("pressure_regions"); }),
            family(C::Case, F::PressureRegions), "case {case}: regions absent");
        assert_eq!(with(&|r| r["model"]["load_cases"][case]["pressure_regions"] = json!([{"id": "region", "member_pipe_ids": ["M1"],
            "pressure_basis": "gauge", "pressure": {"value": 0.0, "unit": "Pa"}}])), family(C::Case, F::PressureRegions), "case {case}: one region");
        assert_eq!(with(&|r| r["model"]["load_cases"][case]["pressure_regions"] = Value::Null), family(C::Case, F::PressureRegions), "case {case}: null");
        assert_eq!(with(&|r| r["model"]["load_cases"][case]["modulus_basis_ref"] = json!("T0")), family(C::Case, F::ModulusBasisRef), "case {case}: a point basis");
    }
    assert_eq!(with(&|r| r["model"]["combinations"] = json!([{"id": "combination", "basis": "mechanics", "terms": [{"load_case": "case-1", "factor": 1.0}]}])),
        family(C::Invocation, F::Combinations), "ruling 4: no combination on the exact route");
    assert_eq!(with(&|r| r["model"]["combinations"] = json!([{"id": "case-1", "basis": "mechanics", "terms": [{"load_case": "case-1", "factor": 1.0}]}])),
        family(C::Invocation, F::Combinations), "the exact clause first");
    assert_eq!(with(&|r| r["model"]["schema_version"] = json!("0.4.0")), family(C::Namespace, F::SchemaVersion), "0.4.0 stays out");
    assert_eq!(with(&|r| r["model"]["pressure_contract"] = Value::Null), family(C::Namespace, F::PressureContract));
    assert_eq!(with(&|r| r["model"]["pressure_contract"]["version"] = json!("2.0.1")), family(C::Namespace, F::PressureContract));
    assert_eq!(with(&|r| r["model"]["pressure_contract"]["mode"] = json!("legacy_pressure_v1")), family(C::Namespace, F::PressureContract),
        "2.0.0 with the legacy mode");
    assert_eq!(with(&|r| r["model"]["schema_version"] = json!("0.2.0")), family(C::Namespace, F::PressureContract));
    // A combination on L or L3 is still inside D1 (B2-C's clauses apply there only).
    let mut l3 = legacy3(milestone());
    l3["model"]["combinations"] = json!([{"id": "combination", "basis": "mechanics", "terms": [{"load_case": "case", "factor": 1.0}]}]);
    assert_eq!(domain(l3), None);
    // The committed physics-source requests n05 and n06 (B3b's coexistence pins) are on branch E.
    for (name, text) in [("n05", N05), ("n06", N06)] {
        assert_eq!(domain(serde_json::from_str(text).unwrap()), None, "{name}");
    }
}

/// B3b-A's Direct-entry oracle (no producer change yet: PP `permitted_run` sends a permitted
/// exact model to the unchanged ordinary route, `W1Fallback::Domain`). m3x and the coexistence
/// pins n05 and n06 publish exactly the ordinary value route's bytes in both modes, admitted
/// in the registered build.
#[test]
fn b3b_direct_entry_keeps_the_exact_ordinary_bytes() {
    let registered = COMPILED_IDENTITY == Some(REGISTERED_PROFILES[0].identity);
    let read = |text: &str| -> Value { serde_json::from_str(text).unwrap() };
    for (label, raw) in [("m3x", exact3(milestone())), ("n05", read(N05)), ("n06", read(N06))] {
        for mode in MODES {
            let plain = serde_json::to_vec(&crate::run_linear_static_preview_value_with_mode(raw.clone(), mode).unwrap()).unwrap();
            let direct = crate::run_linear_static_preview_value_with_retained_direct(raw.clone(), mode).unwrap();
            let report = direct.admission().unwrap();
            assert_eq!(report.law().domain, None, "{label} {mode:?}");
            if registered {
                assert_eq!(report.law().refusal, None, "{label} {mode:?}: admitted");
                assert!(matches!(direct.retained(), Some(Err(crate::W1Fallback::Domain))), "{label} {mode:?}: {:?}", direct.retained());
            } else {
                assert_eq!(report.law().refusal, d1_1_refusal(), "{label} {mode:?}");
            }
            assert!(direct.successor().is_none(), "{label} {mode:?}");
            assert_eq!(serde_json::to_vec(direct.envelope()).unwrap(), plain, "{label} {mode:?}: the exact ordinary bytes");
        }
    }
}
'''
p.write_text(t)
print('ok')
