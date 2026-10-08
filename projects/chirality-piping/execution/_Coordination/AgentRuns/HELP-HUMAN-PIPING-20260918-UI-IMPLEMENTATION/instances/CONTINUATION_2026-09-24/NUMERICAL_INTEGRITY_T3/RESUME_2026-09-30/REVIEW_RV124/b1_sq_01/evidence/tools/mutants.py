"""RV124: mutants on SQ's new gate bounds, re-pins and guards, in a copy of the registered scratch copy.
Each mutant is exact string replacements (each must match exactly once); the file is restored after.
Usage: mutants.py list | mutants.py apply <id> | mutants.py restore <id>
"""
import json, os, shutil, sys

ROOT = "WT/scratch/rv124_rvq/mut/projects/chirality-piping"
PP = ROOT + "/core/product_physics"
RM = PP + "/src/retained_memory.rs"
LT = PP + "/src/retained_memory_law_tests.rs"
WTS = PP + "/src/retained_memory_witness_tests.rs"
CH = PP + "/tests/retained_memory_challenge.rs"
S11 = PP + "/tests/s11f_site_test.rs"
RP = PP + "/src/retained_product.rs"
RUN = ROOT + "/core/runner/headless/tests/retained_precision_admission.rs"

LAW = "retained_memory::law_tests"
M = {
    # id: (description, [(file, old, new)], test selector)
    "M00": ("baseline + DEF-O failing-row kinds probe (test code only)", [(WTS,
        '            let first = verdicts.iter().find(|v| !v.passed)',
        '            let fails: Vec<String> = verdicts.iter().filter(|v| !v.passed).map(|v| format!("{}:{}", v.row, kind(v.row))).collect();\n'
        '            println!("RV124_DEF_O_FAILS {label} {mode:?} case={case_id} {fails:?}");\n'
        '            let first = verdicts.iter().find(|v| !v.passed)')], "law"),
    "M01": ("G-B bound reverts to the SF-1 defect: T11 - T11_late_capture", [(RM,
        "profile_bytes(profile::F_T11_LATE_CAPTURE) / c)],", "profile_bytes(profile::F_T11_LATE_CAPTURE))],")], "law"),
    "M02": ("G-B bound divides by 2, not C", [(RM,
        "profile_bytes(profile::F_T11_LATE_CAPTURE) / c)],", "profile_bytes(profile::F_T11_LATE_CAPTURE) / 2)],")], "law"),
    "M03": ("G-B bound is T11 (no late subtraction)", [(RM,
        "profile_bytes(profile::F_T11).saturating_sub(profile_bytes(profile::F_T11_LATE_CAPTURE) / c)],",
        "profile_bytes(profile::F_T11)],")], "law"),
    "M04": ("registered threshold one byte low", [(RM, "threshold_bytes: 11_274_289_152,", "threshold_bytes: 11_274_289_151,")], "law"),
    "M05": ("registered threshold at 12 GiB", [(RM, "threshold_bytes: 11_274_289_152,", "threshold_bytes: 12_884_901_888,")], "law"),
    "M06": ("block: Text(diag_env) + 1", [(RM, "pub(crate) const TEXT_TEXT_DIAG_ENV: u64 = 175409684;", "pub(crate) const TEXT_TEXT_DIAG_ENV: u64 = 175409685;")], "law"),
    "M07": ("block: D_env - 1", [(RM, "pub(crate) const TEXT_D_ENV: u64 = 22911;", "pub(crate) const TEXT_D_ENV: u64 = 22910;")], "law"),
    "M08": ("block: L_DIAGID + 1", [(RM, "pub(crate) const L_DIAGID: u64 = 2330;", "pub(crate) const L_DIAGID: u64 = 2331;")], "law"),
    "M09": ("block: a T11_late_capture coefficient not a multiple of C", [(RM,
        'Form { name: "T11_late_capture", constant: 49536, terms: &[(136, 576),',
        'Form { name: "T11_late_capture", constant: 49536, terms: &[(136, 577),')], "law"),
    "M10": ("block: N-5's parked-slot term removed from T11", [(RM,
        "(63, 1), (85, 3), (86, 2), (115, 8)", "(63, 1), (85, 3), (115, 8)")], "law"),
    "M11": ("block: s(CaseSlot) bound to 0 in-build", [(RM,
        "(size_of::<crate::retained_product::CaseSlot>()) as u64, // s(CaseSlot)", "(0) as u64, // s(CaseSlot)")], "law"),
    "M12": ("block: N-5's batch-source term removed from T13", [(RM,
        "(145, 12), (154, 3), (163, 12288)", "(145, 12), (163, 12288)")], "law"),
    "M13": ("challenge: CAP_BYTES 15 GiB", [(CH, "const CAP_BYTES: usize = 16 << 30;", "const CAP_BYTES: usize = 15 << 30;")], "law"),
    "M14": ("challenge: MAX_PHASE_BYTES dense + 1", [(CH, "const MAX_PHASE_BYTES: [u64; 2] = [9_733_567_302, 9_792_698_646];",
        "const MAX_PHASE_BYTES: [u64; 2] = [9_733_567_302, 9_792_698_647];")], "law"),
    "M15": ("challenge: W1_PHASE_BYTES sparse - 1", [(CH, "const W1_PHASE_BYTES: [u64; 2] = [5_069_321_390, 5_128_452_734];",
        "const W1_PHASE_BYTES: [u64; 2] = [5_069_321_389, 5_128_452_734];")], "law"),
    "M16": ("challenge: N1 text not the notice's", [(CH, 'const N1_NOTICE: &str = "Retained-precision recovery is unavailable for this load case.";',
        'const N1_NOTICE: &str = "Retained-precision recovery is not available for this load case.";')], "law"),
    "M17": ("challenge: W1 work read from the successor only (A1-S-1's notice ignored)", [(CH,
        "(outcome, successor.is_some() || notices > 0, rows)", "(outcome, successor.is_some(), rows)")], "chal"),
    "M18": ("runner: C_PLUS_ONE literal 5", [(RUN, "const C_PLUS_ONE: usize = 4;", "const C_PLUS_ONE: usize = 5;")], "law"),
    "M19": ("G04: the parked-slot reader folds the first slot only", [(RM,
        "capture.parked_cases().iter().fold(own,", "capture.parked_cases().iter().take(1).fold(own,")], "law"),
    "M20": ("s11f: retained_product.rs dropped from RULE8_FILES (E-12 reverted)", [(S11,
        '    "PP/retained_product.rs",\n    "PP/self_weight.rs",', '    "PP/self_weight.rs",')], "s11f"),
    "M21": ("retained_product.rs: a new float accumulation (rule 8 must fail)", [(RP,
        "    fn capture_entry(&self, event: AdapterEvent) -> Result<(), CaptureError> {\n",
        "    fn capture_entry(&self, event: AdapterEvent) -> Result<(), CaptureError> {\n        let mut rv124_acc = 0.0f64; for rv124_x in [1.0f64] { rv124_acc += rv124_x; } let _ = rv124_acc;\n")], "s11f"),
    "M22": ("phase_caps late bound divides by LOAD_CASES - 1", [(RM,
        "profile_bytes(profile::F_T11_LATE_CAPTURE) / c)],", "profile_bytes(profile::F_T11_LATE_CAPTURE) / (c - 1))],")], "law"),
}

def apply(mid):
    desc, edits, _ = M[mid]
    for f, old, new in edits:
        bak = f + ".rv124orig"
        if not os.path.exists(bak):
            shutil.copy2(f, bak)
        t = open(f).read()
        k = t.count(old)
        if k != 1:
            raise SystemExit(f"{mid}: expected 1 match in {f}, found {k}")
        open(f, "w").write(t.replace(old, new))
    print(f"{mid} applied: {desc}")

def restore(mid):
    for f, _, _ in M[mid][1]:
        bak = f + ".rv124orig"
        if os.path.exists(bak):
            shutil.move(bak, f)
    print(f"{mid} restored")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "list":
        for k, (d, _, sel) in M.items():
            print(k, sel, d, sep="\t")
    elif cmd == "apply":
        apply(sys.argv[2])
    elif cmd == "restore":
        restore(sys.argv[2])
    elif cmd == "json":
        json.dump({k: {"desc": d, "selector": s, "edits": [(f.replace(ROOT + "/", "P/"), o, n) for f, o, n in e]} for k, (d, e, s) in M.items()}, sys.stdout, indent=1)
