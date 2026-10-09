"""Build T4's simulated edit tree on C (main ec5d397359 + U3 1e9724fb94, import conflict resolved).

Every line T4-U1/T4-U3 plan to touch is "edited" by appending a marker; editing every
line of a range is, for 3-way conflict detection, equivalent to replacing or deleting it.
Writes loose objects only (hash-object -w, write-tree) through a scratch index.
Usage: python3 -I t4sim.py <variant A|B> <C tree> <scratch dir>
"""
import os, re, subprocess, sys

variant, C, S = sys.argv[1], sys.argv[2], sys.argv[3]
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_INDEX_FILE=os.path.join(S, f"idx_T4{variant}"))

def git(*a, inp=None):
    return subprocess.run(["git", *a], env=env, input=inp, capture_output=True, check=True).stdout

KEY = "component_user_stiffness_macro_element_count"
PAT = re.compile(r"curved|Curved|CURVED|user_stiffness|UserStiffness|USER_STIFFNESS|user_element|UserTie|"
                 r"TieRefusal|expansion_joint|ExpansionJoint|EXPANSION_JOINT|JOINT_ELEMENT|\bcenter\b|"
                 r"bend_plane_orientation|\busers\b|user_matrix|add_relative_dof_stiffness")

def lines_matching(text, h4_holds):
    out = set()
    for i, line in enumerate(text.split("\n"), 1):
        probe = line.replace(KEY, "") if h4_holds else line
        if h4_holds:
            probe = probe.replace("component_user_stiffness_macro_element_review", "")
        if PAT.search(probe):
            out.add(i)
    return out

def win(*specs, pad=3):
    s = set()
    for spec in specs:
        a, b = (spec, spec) if isinstance(spec, int) else spec
        s.update(range(a - pad, b + pad + 1))
    return s

# Planned edit set: (path, explicit windows in C numbering). Pattern marking applies to all.
L = lambda n: n + 2  # PP lib.rs: U3 (I3) numbering -> C numbering (+2 after the import block)
PLAN = {
    # ---- T4-U1 (curved formation) and T4-U3 (joint deletion), production
    P+"core/solver/curved_bend/src/lib.rs": set(),
    P+"core/solver/curved_bend/src/s11k_tests.rs": set(),
    P+"core/solver/curved_bend/README.md": set(),
    P+"core/solver/frame_kernel/src/lib.rs": set(),
    P+"core/solver/frame_kernel/src/rigid_body.rs": win((261, 263), (327, 361)),
    P+"core/solver/frame_kernel/src/structural.rs": set(),
    P+"core/solver/frame_kernel/src/structural/formation_check.rs": win((47, 60), (637, 668)),
    P+"core/solver/frame_kernel/src/structural/sparse.rs": win(40, (503, 553), (592, 640)),
    P+"core/solver/nonlinear_integration/src/lib.rs": win(243, (581, 603), 1310, (1110, 1120), (3580, 3610)),
    P+"core/solver/nonlinear_integration/src/structural_adapter.rs": win((47, 118), (496, 548), (1085, 1160), (1369, 1450), (1576, 1589), (1731, 1744), (2036, 2041)),
    P+"core/solver/nonlinear_integration/README.md": set(),
    P+"core/solver/performance_harness/src/k6/staged.rs": win(289),
    P+"validation/benchmarks/nonlinear/src/lib.rs": set(),
    P+"validation/benchmarks/mechanics/src/lib.rs": win(3345, 3650),
    P+"core/product_physics/src/lib.rs": win(L(49), L(51), (L(1240), L(1246)), L(1455), (L(1556), L(1557)), L(2048),
                                             (L(2777), L(2779)), L(3539), (L(3757), L(3770)), L(4433), L(5756), L(6102),
                                             L(6136), L(6257), (L(6383), L(6447)), (L(7335), L(7336)), L(7415),
                                             (L(7480), L(7593)), (L(11904), L(12003)), (L(14319), L(14321)),
                                             (L(15222), L(15240)), (L(17391), L(17600))),
    P+"core/product_physics/src/preview_physics.rs": win((106, 211)),
    P+"core/product_physics/src/validation.rs": win((1147, 1162), (1317, 1400), (1771, 1865), 1567),
    P+"core/product_physics/src/retained_product.rs": win((1558, 1558), pad=0),
    P+"core/product_physics/src/source_recovery.rs": win((579, 585), pad=0),
    P+"core/product_physics/src/source_receipt.rs": win((312, 318), pad=0),
    P+"core/product_physics/src/source_receipt/source.rs": win(376, pad=0),
    P+"core/product_physics/src/formation_guard.rs": win(83, pad=0),
    # ---- tests
    P+"core/solver/frame_kernel/src/structural/formation_check_tests.rs": win((69, 145), (276, 296)),
    P+"core/solver/frame_kernel/src/structural/sparse/tests.rs": win((238, 312), (409, 445)),
    P+"core/solver/frame_kernel/tests/k2b_force_scaling.rs": win((159, 213), (288, 345), (536, 583)),
    P+"core/solver/frame_kernel/tests/k5_constrained_bodies.rs": win(895, (909, 1059)),
    P+"core/solver/frame_kernel/tests/k1_k2a_interaction.rs": win(21, 83),
    P+"core/solver/frame_kernel/tests/s11_site_table.rs": win(194, (275, 283), (82, 92)),
    P+"core/solver/nonlinear_integration/src/structural_adapter/k1_tests.rs": win((183, 197), 336, (816, 851), (1028, 1034), (1153, 1170), 1313, 1490),
    P+"core/solver/nonlinear_integration/src/structural_adapter/k2b_tests.rs": win((40, 53), 1312, 1403),
    P+"core/solver/nonlinear_integration/src/structural_adapter/k5_tests.rs": win((75, 80), 189, 219, (233, 307), 506, (937, 980), 1078, 1106, 1203, 1225),
    P+"core/solver/nonlinear_integration/src/structural_adapter/kd5_tests.rs": win((54, 148), (378, 530), (567, 642)),
    P+"core/solver/nonlinear_integration/src/structural_adapter/kd5_models.rs": set(range(1, 100000)),  # regenerated
    P+"core/solver/nonlinear_integration/src/s11k_tests.rs": win(861),
    P+"core/solver/sparse_direct/src/structural/k1_tests.rs": win((17, 312), pad=0),
    P+"core/product_physics/tests/formation_check_runtime.rs": win((250, 286), (358, 400)),
    P+"core/product_physics/tests/k5_curved_mechanism_runtime.rs": win((148, 260)),
    P+"core/product_physics/src/s11g_tests.rs": win(1747, 2380, (2605, 2612)),
    P+"core/product_physics/src/s11f_tests.rs": win(1600, 1605, 1650, 1688),
    P+"core/product_physics/src/f1b_tests.rs": win((2217, 2260)),
    P+"core/product_physics/src/source_receipt/tests.rs": win(24),
    P+"core/product_physics/tests/preview_physics_runtime.rs": win((854, 920), (1032, 1077)),
    P+"core/product_physics/tests/f1b_w2_runtime.rs": win((702, 710)),
    # s11f_site_test: the whole PP/lib.rs block may be re-listed (506-538); CB scan 141; curved rows 166-168, 219
    P+"core/product_physics/tests/s11f_site_test.rs": set(range(506, 539)) | win(141, (166, 168), 219, pad=0),
    # ---- other crates, readers, TS
    P+"core/runner/headless/src/lib.rs": win((1139, 1141)),
    P+"core/runner/headless/src/result_envelope_binding.rs": win((448, 490)),
    P+"core/runner/headless/tests/preview_physics_admission.rs": win((249, 280)),
    P+"core/reporting/result_export/tests/preview_physics_contract.rs": win(606, pad=2),
    P+"apps/desktop/src/services/previewService.ts": win((340, 383), pad=0),
    P+"apps/desktop/src/features/report/ReportPanel.tsx": win((334, 371), (405, 443), (500, 511), (728, 731)),
    P+"apps/desktop/src/features/component-creation/componentIntent.ts": win(3, (210, 227), (341, 351), (371, 394)),
}
if variant == "B":  # H-4 reversed: the key renamed and the row kind removed now, by T4-U3
    PLAN[P+"core/product_physics/src/retained_product_tests.rs"] = set()
    PLAN[P+"apps/desktop/src/features/results/retainedPrecision.ts"] = win(110, pad=0)
    PLAN[P+"core/analysis_runs/retained_precision.py"] = win(1150, pad=0)
    PLAN[P+"core/reporting/result_export/src/retained_precision.rs"] = win((2500, 2503), pad=0)

git("read-tree", C)
report = []
for path, explicit in sorted(PLAN.items()):
    try:
        text = git("show", f"{C}:{path}").decode()
    except subprocess.CalledProcessError:
        report.append(f"MISSING {path}")
        continue
    lines = text.split("\n")
    marked = (lines_matching(text, variant == "A") | explicit) & set(range(1, len(lines) + 1))
    if text.endswith("\n"):
        marked.discard(len(lines))  # the empty tail after the final newline
    for i in marked:
        lines[i - 1] = lines[i - 1] + " T4SIM"
    blob = git("hash-object", "-w", "--stdin", inp="\n".join(lines).encode()).decode().strip()
    git("update-index", "--cacheinfo", f"100644,{blob},{path}")
    report.append(f"{len(marked):6d} lines  {path}")
tree = git("write-tree").decode().strip()
print("\n".join(report))
print(f"T4{variant}_TREE={tree}")
