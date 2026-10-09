"""T4-RV3 addendum 01: re-derive every value of T4-I7's round-01 u2_reference_cases.json (fa0b43f3c1) by
the transfer-matrix method of rv3_lib/rv3_solve (unchanged from round 00), adding the chord_frame_elastic
end rows, and check the refusal control's junction angle.

    python -I -B rv3_r01_check.py <round-01 u2_reference_cases.json>

chord_frame_elastic is formed here as the wall node-on-element action minus the bend's own cap pair
c_b = [-pAi t_i, +pAi t_j]; rv3_r01_elastic.py checks it separately as K(d - u_free) - p."""
import json
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_solve as S  # noqa: E402
import rv3_check as C  # noqa: E402
import rv3_lib as L  # noqa: E402
from rv3_lib import ZERO, mul, sub, dot  # noqa: E402

ALPHA = D("1e-3")
_orig_results = S.Case.results


def results_r01(self):
    res = _orig_results(self)
    for m in self.mems:
        if m.kind != "arc":
            continue
        er = res["members"][m.pid]["end_rows"]
        for end, f, cap in (("end_i", D(0), mul(-self.P, m.authored_frame(D(0))[0])),
                            ("end_j", D(1), mul(self.P, m.authored_frame(D(1))[0]))):
            F, M = self.jside([i for i, mm in enumerate(self.mems) if mm is m][0], f)
            wall = mul(D(-1), F) if end == "end_i" else F
            mom = mul(D(-1), M) if end == "end_i" else M
            el = sub(wall, cap)
            comps = [dot(el, e) for e in m.chord_frame] + [dot(mom, e) for e in m.chord_frame]
            er[end]["chord_frame_elastic"] = dict(zip(["F_x", "F_y", "F_z", "M_x", "M_y", "M_z"], comps))
    return res


S.Case.results = results_r01
_orig_end_group = C.end_group


def end_group_r01(key, frame):
    if frame == "chord_frame_elastic":
        return "elastic_end_force_chord_frame" if key.startswith("F") else "section_moment"
    return _orig_end_group(key, frame)


C.end_group = end_group_r01


def main(path):
    data = json.load(open(path))
    overall = D(0)
    total = 0
    for cid, case in data["cases"].items():
        c = S.Case(case["inputs"])
        if case["expected"] is None:
            ref = case["expected_refusal"]
            kinks = c.kinks()
            th = max(k for _, k in kinks)
            node = [n for n, k in kinks if k == th][0]
            print("%-50s refusal control: code %s; theta at %s = %.16e rad (ref %s); theta - alpha_tan = %.4e;"
                  " tan(theta) - alpha_tan = %.4e; matches ref node: %s" % (
                      cid, ref["code"], node, th, ref["theta_rad"], th - ALPHA, L.sincos(th)[0] / L.sincos(th)[1]
                      - ALPHA, node == ref["node"]))
            continue
        c.solve()
        res = c.results()
        n, worst, missing = C.compare(case, res)
        total += n
        overall = max(overall, worst[0])
        bad, zero_groups = C.zero_scale_check(case)
        ja = case["derived"].get("junction_angles_rad", {})
        kd = {nid: k for nid, k in c.kinks()}
        ja_dev = max([abs(D(v) - kd[nid]) for nid, v in ja.items()] or [D(0)])
        miss = [x for x in missing if not x.endswith("lame_surface:MISSING")]
        print("%-50s leaves %4d  max_norm_diff %.2e  at %s" % (cid, n, worst[0], worst[1]))
        print("    junction angles vs mine: max |diff| %.1e rad (max theta %.3e); zero_scale %s; zero groups %s%s" % (
            ja_dev, max(list(kd.values()) or [D(0)]), "ok" if not bad else bad, zero_groups, ("; MISSING " + str(miss)) if miss else ""))
    print("TOTAL leaves compared %d; OVERALL max normalized difference %.3e" % (total, overall))


if __name__ == "__main__":
    main(sys.argv[1])
