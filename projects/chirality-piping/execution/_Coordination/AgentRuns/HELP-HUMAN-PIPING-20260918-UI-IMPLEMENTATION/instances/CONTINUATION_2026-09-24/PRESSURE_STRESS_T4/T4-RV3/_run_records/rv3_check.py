"""T4-RV3: re-derive every value of T4-I7's u2_reference_cases.json from each case's inputs block by the
transfer-matrix method (rv3_lib, rv3_solve) and compare.

    python -I rv3_check.py <path to u2_reference_cases.json>

Prints, per case, the largest normalized difference |mine - ref| / max(|ref|, zero_scale(group)) over
every expected leaf, the leaf where it occurs, the tangency kinks of the case geometry, and summary
checks of the zero_scale block."""
import json
import sys
import os
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_solve as S  # noqa: E402
from rv3_lib import ZERO  # noqa: E402

GROUP_OF = {"ux": "displacement", "uy": "displacement", "uz": "displacement", "rx": "rotation", "ry": "rotation",
            "rz": "rotation", "N_w": "wall_axial_force", "S": "effective_axial_force", "sigma_m": "membrane_stress",
            "V_y": "shear_force", "V_z": "shear_force", "T": "section_moment", "M_y": "section_moment",
            "M_z": "section_moment", "sigma_b_y": "bending_torsion_stress", "sigma_b_z": "bending_torsion_stress",
            "tau_t": "bending_torsion_stress"}


def end_group(key, frame):
    if key in ("wall_axial_end_action", "F_x") and frame != "chord_frame":
        return "wall_axial_force"
    if key.startswith("F"):
        return "end_action_force_chord_frame" if frame == "chord_frame" else "shear_force"
    return "section_moment"


def group_of(path):
    if path[0] == "nodes":
        return GROUP_OF[path[-1]]
    if path[0] == "supports":
        return ("support_force" if path[-1].startswith("F") else "support_moment") + "@" + path[1]
    if path[0] == "terminals":
        return "remote_closure_force"
    if path[0] == "members":
        if path[2] == "stations":
            return GROUP_OF[path[-1]]
        if path[2] == "end_rows":
            return end_group(path[-1], path[4])
        if path[2] == "lame_surface":
            return "lame_stress"
        return None  # geometry
    return None


SKIP = {"fraction", "kind", "authored_from", "authored_to", "traversal_matches_authored", "closure_transfer"}


def walk(ref, mine, path, out):
    if isinstance(ref, dict):
        for k, v in ref.items():
            if k in SKIP:
                continue
            if mine is None or k not in mine:
                out.append((path + [k], "MISSING", None, None))
                continue
            walk(v, mine[k], path + [k], out)
    elif isinstance(ref, list):
        for i, v in enumerate(ref):
            walk(v, mine[i], path + [str(i)], out)
    elif ref is None:
        if mine is not None:
            out.append((path, "EXTRA", None, None))
    elif isinstance(ref, str):
        if ref == "withheld_on_arcs":
            return
        out.append((path, D(ref), D(mine), None))


def compare(case, res):
    zs = {g: D(v["zero_scale"]) for g, v in case["zero_scale"].items()}
    leaves = []
    walk(case["expected"], res, [], leaves)
    worst = (D(0), None)
    missing = []
    count = 0
    for path, ref, mine, _ in leaves:
        if ref in ("MISSING", "EXTRA"):
            missing.append("/".join(path) + ":" + ref)
            continue
        count += 1
        g = group_of(path)
        scale = max(abs(ref), zs[g]) if g else max(abs(ref), D(1))
        d = abs(mine - ref) / scale if scale != 0 else abs(mine - ref)
        if d > worst[0]:
            worst = (d, "/".join(path), ref, mine)
    return count, worst, missing


def zero_scale_check(case):
    """recompute the per-group maximum of |expected| and compare with the case's zero_scale block"""
    leaves = []
    walk(case["expected"], case["expected"], [], leaves)
    gmax = {}
    for path, ref, _, _ in leaves:
        if ref in ("MISSING", "EXTRA"):
            continue
        g = group_of(path)
        if g:
            gmax[g] = max(gmax.get(g, ZERO), abs(ref))
    bad = []
    for g, v in case["zero_scale"].items():
        zsv = D(v["zero_scale"])
        if gmax.get(g, ZERO) != 0 and gmax[g] != zsv:
            bad.append((g, gmax[g], zsv))
        if D(v["absolute_floor"]) != D("1e-9") * zsv:
            bad.append((g, "floor", v["absolute_floor"]))
    for g in gmax:
        if g not in case["zero_scale"]:
            bad.append((g, "no zero_scale"))
    zero_groups = [g for g in case["zero_scale"] if gmax.get(g, ZERO) == 0]
    return bad, zero_groups


def main(path):
    data = json.load(open(path))
    overall = D(0)
    for cid, case in data["cases"].items():
        c = S.Case(case["inputs"]).solve()
        res = c.results()
        n, worst, missing = compare(case, res)
        overall = max(overall, worst[0])
        kinks = c.kinks()
        kmax = max([k for _, k in kinks], default=D(0))
        bad, zero_groups = zero_scale_check(case)
        trav = all(case["expected"]["members"][m.pid]["traversal_matches_authored"] == m.forward for m in c.mems)
        print("%-50s leaves %4d  max_norm_diff %.2e  at %s" % (cid, n, worst[0], worst[1]))
        print("    max kink %.3e rad%s; traversal flags %s; zero_scale %s; identically-zero groups %s%s" % (
            kmax, (" at " + ",".join("%s=%.9e" % (nid, k) for nid, k in kinks if k > D("1e-12"))) if kmax > D("1e-12")
            else "", "ok" if trav else "MISMATCH", "ok" if not bad else bad, zero_groups,
            ("; MISSING " + str(missing)) if missing else ""))
    print("OVERALL max normalized difference over all cases and leaves: %.3e" % overall)


if __name__ == "__main__":
    main(sys.argv[1])
