"""RV113 (RV-R): a mutant schema for SR-RS repair 02 (6e3e4fe219), in the reviewer's own copy (WT/rv113/rs2-mut).

Each mutant is a source edit guarded by `mx("<id>")`, true only when RV113_MUT equals the id; with RV113_MUT unset the
copy behaves as the head (a control run checks it). One build serves every mutant. Each anchor must match exactly once.
Usage: python make_mutants_r2.py <RE dir> <manifest out>
"""
import json
import sys

re_dir, manifest_out = sys.argv[1], sys.argv[2]
path = f"{re_dir}/src/retained_precision.rs"
rs = open(path).read()
manifest = []

HELPER = '\nfn mx(id: &str) -> bool {\n    std::env::var("RV113_MUT").map_or(false, |v| v == id)\n}\n'
anchor = "const MAX_BITS: u64 = 0x7fef_ffff_ffff_ffff;\n"
assert rs.count(anchor) == 1
rs = rs.replace(anchor, anchor + HELPER)


def sub(old, new, mid, item, desc):
    global rs
    assert rs.count(old) == 1, (mid, rs.count(old), old[:90])
    rs = rs.replace(old, new)
    manifest.append({"id": mid, "item": item, "description": desc})


def also(mid, item, desc):
    manifest.append({"id": mid, "item": item, "description": desc})


# ---------------------------------------------------------------- item 1: G3
sub('''                && u(&s["index"]) == si as u64
                && owner["kind"] == "case"''',
    '''                && (mx("N01") || u(&s["index"]) == si as u64)
                && owner["kind"] == "case"''', "N01", "1 (f)", "G3: a source's index at its position dropped")
sub('''                && usize::try_from(u(&owner["case_index"]))
                    .ok()
                    .and_then(|ci| cs.get(ci))
                    .is_some_and(|c| c["basis_ref"]["ref_id"] == owner["case_id"]),''',
    '''                && (mx("N03") || usize::try_from(u(&owner["case_index"]))
                    .ok()
                    .and_then(|ci| cs.get(ci))
                    .is_some_and(|c| mx("N04") || c["basis_ref"]["ref_id"] == owner["case_id"])),''',
    "N03", "1 (f)", "G3: the owner's case binding dropped (index range and id)")
also("N04", "1 (f)", "G3: the owner's case id against the case at its index dropped (index range kept)")
sub('''            u(&mb["index"]) == mi as u64
                && list(&mb["case_indices"])
                    .iter()
                    .all(|ci| u(ci) < cs.len() as u64 && seen.insert(u(ci))),''',
    '''            (mx("N05") || u(&mb["index"]) == mi as u64)
                && list(&mb["case_indices"])
                    .iter()
                    .all(|ci| (mx("N06") || u(ci) < cs.len() as u64) && (mx("N07") || seen.insert(u(ci)))),''',
    "N05", "1 (f)", "G3: a material basis's index at its position dropped")
also("N06", "1 (f)", "G3: case_indices in range dropped")
also("N07", "1 (f)", "G3: case_indices unique dropped")
sub('''            .is_ok_and(|mb| list(&mb["case_indices"]).iter().any(|x| u(x) == i as u64)),
        )?;
        // D6a (checkpoint-A ruling)''',
    '''            .is_ok_and(|mb| mx("N09") || list(&mb["case_indices"]).iter().any(|x| u(x) == i as u64))
                || mx("N08"),
        )?;
        // D6a (checkpoint-A ruling)''', "N08", "1 G5", "G5 ordinary: the ordinary attempt's basis reference dropped")
also("N09", "1 G5", "G5 ordinary: the basis need only resolve (not list the case)")

# ---------------------------------------------------------------- item 2: G8 model scope
sub('''                .all(|k| model.get(*k).is_none_or(|v| v.as_array().is_some_and(Vec::is_empty)))''',
    '''                .all(|k| if (mx("N10") && *k == "combinations") || (mx("N11") && *k == "components") { list(&model[*k]).is_empty() } else { model.get(*k).is_none_or(|v| (mx("N12") && v.is_null()) || v.as_array().is_some_and(Vec::is_empty)) })''',
    "N10", "2 (g)", "G8: combinations back to the old list(..).is_empty() (null and non-arrays admitted)")
also("N11", "2 (g)", "G8: components back to the old list(..).is_empty()")
also("N12", "2 (g)", "G8: combinations and components may be null")
sub('''            && !model
                .as_object()
                .is_some_and(|m| m.contains_key("reference_configurations")),''',
    '''            && (mx("N13") || !model
                .as_object()
                .is_some_and(|m| m.contains_key("reference_configurations"))),''', "N13", "2 (g)", "G8: reference_configurations check dropped")
sub('''            && model["pressure_contract"].is_null()
            && ["combinations", "components"]''',
    '''            && (model["pressure_contract"].is_null() || (mx("N14") && model["pressure_contract"] == false))
            && ["combinations", "components"]''', "N14", "2 (g)", "G8: pressure_contract false admitted")

# ---------------------------------------------------------------- item 3: C2's cause table
sub('''        if c["status"] == "unavailable"
            && c["reason"]["cause"]["kind"] != "prepared_product_failure"
        {''',
    '''        if !mx("N15") && c["status"] == "unavailable"
            && (mx("N33") || c["reason"]["cause"]["kind"] != "prepared_product_failure")
        {''', "N15", "3 C2", "the whole C2 table dropped")
sub('''                    phase == "preparation"
                        && code == "source_unavailable"
                        && run.is_null()
                        && !decline.is_null()
                        && decline["error"] == cause["error"]''',
    '''                    (mx("N16") || phase == "preparation")
                        && (mx("N17") || code == "source_unavailable")
                        && (mx("N18") || run.is_null())
                        && !decline.is_null()
                        && (mx("N19") || decline["error"] == cause["error"])''', "N16", "3 C2", "source_error: phase dropped")
also("N17", "3 C2", "source_error: code dropped")
also("N18", "3 C2", "source_error: no Run dropped")
also("N19", "3 C2", "source_error: the decline's error equality dropped")
sub('''                    matches!(phase, "routing" | "preparation")
                        && run.is_null()
                        && match text(&cause["precondition"]) {''',
    '''                    (mx("N20") || matches!(phase, "routing" | "preparation"))
                        && (mx("N21") || run.is_null())
                        && (mx("N22") && matches!(code, "source_unavailable" | "resource_admission_not_available" | "upstream_no_wrap_not_established" | "caller_not_qualified") || !mx("N22") && match text(&cause["precondition"]) {''',
    "N20", "3 C2", "unavailable_precondition: phase dropped")
also("N21", "3 C2", "unavailable_precondition: no Run dropped")
also("N22", "3 C2", "unavailable_precondition: keying replaced by TS's present set (any of the four codes)")
sub('''                            "capture" | "source_family" => code == "source_unavailable",
                            _ => false,
                        }''',
    '''                            "capture" => code == "source_unavailable",
                            "source_family" => code == "source_unavailable" && !mx("N23"),
                            _ => mx("N24"),
                        })''', "N23", "3 C2", "unavailable_precondition: source_family's keyed code refused")
also("N24", "3 C2", "unavailable_precondition: an unknown precondition admitted")
sub('''                    phase == "receipt"
                        && matches!(
                            code,
                            "receipt_encoding"
                                | "publication_hash_range"
                                | "invocation_not_representable"
                        )''',
    '''                    (mx("N25") || phase == "receipt")
                        && (mx("N26") || matches!(
                            code,
                            "receipt_encoding"
                                | "publication_hash_range"
                        ) || (!mx("N27") && code == "invocation_not_representable"))''', "N25", "3 C2", "receipt_failure: phase dropped")
also("N26", "3 C2", "receipt_failure: code set dropped")
also("N27", "3 C2", "receipt_failure: invocation_not_representable removed from the set")
sub('''                    phase == "facade"
                        && code == "facade_certificate"
                        && run["kernel_terminal"]["kind"] == "selected"
                        && cause["owner_ref"] == json!({"kind": "case", "index": i})''',
    '''                    (mx("N28") || phase == "facade")
                        && (mx("N29") || code == "facade_certificate")
                        && (mx("N30") || run["kernel_terminal"]["kind"] == "selected")
                        && (mx("N31") || cause["owner_ref"] == json!({"kind": "case", "index": i}))''', "N28", "3 C2", "facade_failure: phase dropped")
also("N29", "3 C2", "facade_failure: code dropped")
also("N30", "3 C2", "facade_failure: selected Run dropped")
also("N31", "3 C2", "facade_failure: owner_ref dropped")
sub('''                    phase == "kernel"
                        && !run.is_null()
                        && code == format!("kernel_{}", text(&run["kernel_terminal"]["kind"]))
                        && *cause == run["kernel_terminal"]["reason"]''',
    '''                    (mx("N32") || phase == "kernel")
                        && (mx("N34") || !run.is_null())
                        && (mx("N35") || code == format!("kernel_{}", text(&run["kernel_terminal"]["kind"])))
                        && (mx("N36") || *cause == run["kernel_terminal"]["reason"])''', "N32", "3 C2", "kernel: phase dropped")
also("N33", "3 C2", "the table also applied to prepared_product_failure causes")
also("N34", "3 C2", "kernel: a Run present dropped")
also("N35", "3 C2", "kernel: code dropped")
also("N36", "3 C2", "kernel: cause equal to the terminal's reason dropped")

# ---------------------------------------------------------------- item 4: transport metadata at G7
sub('''    preview_physics_transport_metadata(&projected).map_err(base_error)?;''',
    '''    if !mx("N40") {
        preview_physics_transport_metadata(&projected).map_err(|e| if mx("N41") { ValidationError { gate: "G2", ..base_error(e) } } else { base_error(e) })?;
    }''', "N40", "4 T", "the metadata check not run")
also("N41", "4 T", "the metadata check reported at G2 instead of G7")
sub('''    fn demand(ok: bool, detail: &str) -> Result<(), String> {
        if ok {''',
    '''    fn demand(ok: bool, detail: &str) -> Result<(), String> {
        let skip = |id: &str, d: &str| mx(id) && detail == d;
        let ok = ok
            || skip("N42", "unsupported source namespace")
            || skip("N43", "formulation profile or limitations")
            || skip("N44", "transport evidence shape")
            || skip("N45", "preview case shape")
            || skip("N46", "preview case identity")
            || skip("N47", "maximum coverage values")
            || skip("N48", "maximum coverage overlap")
            || skip("N49", "maximum coverage completeness")
            || skip("N50", "support both attributed and withheld")
            || skip("N51", "withheld support values")
            || skip("N52", "extrema identity or basis")
            || skip("N53", "extrema fractions")
            || skip("N54", "extrema integers")
            || skip("N55", "extrema bounds")
            || skip("N56", "extrema member partition")
            || skip("N57", "intensified measure identity")
            || skip("N58", "intensified measure inputs")
            || skip("N59", "attribution sets differ between cases")
            || skip("N60", "duplicate evidence result binding")
            || skip("N61", "combination gate reason")
            || skip("N62", "combination gate identity")
            || skip("N63", "extrema shape")
            || skip("N64", "intensified measure shape")
            || skip("N65", "combination gate shape");
        if ok {''', "N42", "4 T", "metadata: the namespace demand dropped")
for mid, d in [("N43", "formulation profile or limitations"), ("N44", "transport evidence shape (both demands)"), ("N45", "preview case shape"),
               ("N46", "preview case identity"), ("N47", "maximum coverage values"), ("N48", "maximum coverage overlap"),
               ("N49", "maximum coverage completeness"), ("N50", "support both attributed and withheld"), ("N51", "withheld support values"),
               ("N52", "extrema identity or basis"), ("N53", "extrema fractions"), ("N54", "extrema integers"), ("N55", "extrema bounds"),
               ("N56", "extrema member partition"), ("N57", "intensified measure identity"), ("N58", "intensified measure inputs"),
               ("N59", "attribution sets differ between cases"), ("N60", "duplicate evidence result binding"), ("N61", "combination gate reason"),
               ("N62", "combination gate identity"), ("N63", "extrema shape"), ("N64", "intensified measure shape"), ("N65", "combination gate shape")]:
    also(mid, "4 T", "metadata: the demand '" + d + "' dropped")

open(path, "w").write(rs)
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
