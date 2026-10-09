"""T4-RV3: negative controls.

1. Re-derive every wrong_result_discriminators row of T4-I7 with the transfer-matrix solver under the
   stated mutation and compare with T4-I7's wrong value; recompute each row's distance in tolerances
   and list rows that do not discriminate (distance < 1e3).
2. Extra plausible mutants not in T4-I7's list (coverage): the best distance any case in the file gives.

    python -I rv3_controls.py <u2_reference_cases.json>
"""
import json
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_lib as L  # noqa: E402
import rv3_solve as S  # noqa: E402
import rv3_check as C  # noqa: E402
from rv3_lib import ZERO, ONE, mul, add, sub, dot  # noqa: E402


def get(tree, ptr):
    cur = tree
    for p in ptr.strip("/").split("/")[1:]:  # drop leading 'expected'
        cur = cur[p]
    return D(cur)


def wall_segment_action(case, mem, f):
    """authored j-side action at authored fraction f of the arc's own wall load alone on [f, 1]
    (zero action at authored j), by the transfer matrix."""
    save = mem.forward
    mem.set_traversal(True)
    A = mem.system_matrix(case.sec, case.mat, ZERO, case.P, ZERO, wall=True)
    s0 = mem.L * f
    h = mem.L - s0
    E = L.expm(A, h) if h != 0 else None
    fr0 = mem.frame_at(s0)
    mem.set_traversal(save)
    if E is None:
        return (ZERO,) * 3, (ZERO,) * 3, fr0
    yp = [ZERO] * 15 + [ONE]
    ypL = L.matvec(E, yp)
    Amat = [[E[r][k] for k in range(6)] for r in range(6)]
    cvec = L.solve(Amat, [-ypL[r] for r in range(6)])
    return L.to_global(fr0, cvec[0:3]), L.to_global(fr0, cvec[3:6]), fr0


def mutate_case(case_json, mut):
    return S.Case(case_json["inputs"], mutation=mut).solve().results()


def cb_extra(c):
    idx = {n: i for i, n in enumerate(c.order)}
    out = []
    for m in c.mems:
        if m.kind != "arc":
            continue
        out.append((idx[m.a_from], mul(-2 * c.P, m.authored_frame(D(0))[0])))
        out.append((idx[m.a_to], mul(2 * c.P, m.authored_frame(D(1))[0])))
    return out


def recovery_mutant(c, res, ctrl_id, ptr):
    parts = ptr.strip("/").split("/")
    # /expected/members/<pid>/stations/<name>/<key>
    pid, name, key = parts[2], parts[4], parts[5]
    st = res["members"][pid]["stations"][name]
    if ctrl_id == "caps_subtracted_in_recovery":
        return st["S"]
    if ctrl_id == "wall_load_double_count_wall_end_force":
        return st["N_w"] + c.P
    if ctrl_id == "wall_load_double_count_elastic_end_force":
        mem = [m for m in c.mems if m.pid == pid][0]
        f = dict(S.STATIONS)[name]
        Fw, Mw, _ = wall_segment_action(c, mem, f)
        fr = mem.authored_frame(f)
        add_ = {"N_w": dot(Fw, fr[0]), "V_y": dot(Fw, fr[1]), "V_z": dot(Fw, fr[2]), "T": dot(Mw, fr[0]),
                "M_y": dot(Mw, fr[1]), "M_z": dot(Mw, fr[2])}[key]
        return st[key] + add_
    raise KeyError(ctrl_id)


def part1(data):
    print("== T4-I7 negative controls re-derived ==")
    weak = []
    worst_agree = D(0)
    for cid, case in data["cases"].items():
        ctrls = case.get("wrong_result_discriminators")
        if not ctrls:
            continue
        base = S.Case(case["inputs"]).solve()
        res0 = base.results()
        zs = {g: D(v["zero_scale"]) for g, v in case["zero_scale"].items()}
        for ctrl in ctrls:
            cidl = ctrl["id"]
            mut = {"bend_term_omitted": {"arc_no_wall": True, "arc_no_poisson": True},
                   "c_b_added_not_subtracted": {"extra_point_loads": cb_extra(base)},
                   "poisson_term_missing_on_arc": {"arc_no_poisson": True},
                   "interior_remainder_omitted": {"remove_kink_at": [2]}}.get(cidl)
            resm = mutate_case(case, mut) if mut is not None else None
            mx_agree = D(0)
            dists = []
            for row in ctrl["discriminating_values"]:
                ptr = row["pointer"]
                path = ptr.strip("/").split("/")[1:]
                g = C.group_of(path)
                ref = D(row["reference_value"])
                if resm is not None:
                    mine = get(resm, ptr)
                else:
                    mine = recovery_mutant(base, res0, cidl, ptr)
                scale = max(abs(ref), zs[g])
                agree = abs(mine - D(row["wrong_value"])) / scale
                mx_agree = max(mx_agree, agree)
                dist = abs(mine - ref) / (D("1e-9") * scale)
                dists.append(dist)
                if dist < D(1000):
                    weak.append((cid, cidl, ptr, row["wrong_value"], row["reference_value"],
                                 row["distance_in_tolerances"], dist))
            worst_agree = max(worst_agree, mx_agree)
            print("%-40s %-42s rows %d  max|mine-I7 wrong|/scale %.1e  distance min %.2e max %.2e" % (
                cid, cidl, len(dists), mx_agree, min(dists), max(dists)))
    print("worst agreement with T4-I7's wrong values: %.2e" % worst_agree)
    print("rows that do not discriminate (distance < 1e3 tolerances): %d" % len(weak))
    for w in weak:
        print("   %s | %s | %s | wrong %s ref %s | I7 distance %s | recomputed %.3e" % w)


EXTRA = [
    ("k_scales_torsion_too", "k also scales the arc's torsion term"),
    ("k_in_plane_only", "k scales only in-plane bending (out-of-plane k = 1)"),
    ("poisson_sign_flipped", "eigenstrain +2 nu pAi/(E As) on every member"),
    ("wall_load_inward", "arc wall load toward the centre"),
    ("weight_per_chord_on_arc", "arc self-weight per unit chord length (w*chord/arc per unit arc)"),
    ("separate_closure_still_capped", "a separately supported terminal still caps the pipe"),
    ("caps_along_chord", "terminal caps and kink remainders built from member chords, not end tangents"),
]


def extra_mutant_results(case_json, mid):
    inp = json.loads(json.dumps(case_json["inputs"]))
    c = S.Case(inp)
    if mid == "separate_closure_still_capped":
        inp["pressure"]["terminal_A"] = "transfers_to_wall"
        inp["pressure"]["terminal_D"] = "transfers_to_wall"
        return S.Case(inp).solve().results()
    if mid == "poisson_sign_flipped":
        c.eps_nu = -c.eps_nu
        return c.solve().results()
    if mid == "wall_load_inward":
        c.P_wall_sign = -1
        orig = c.mems[0].__class__.system_matrix

        def sm(self, sec, mat, w, P, eps0, wall=True):
            return orig(self, sec, mat, w, -P, eps0, wall)
        for m in c.mems:
            m.system_matrix = sm.__get__(m)
        return c.solve().results()
    if mid == "weight_per_chord_on_arc":
        orig = c.mems[0].__class__.system_matrix
        for m in c.mems:
            if m.kind == "arc":
                ratio = m.chord_len / m.L

                def sm(self, sec, mat, w, P, eps0, wall=True, ratio=ratio):
                    return orig(self, sec, mat, w * ratio, P, eps0, wall)
                m.system_matrix = sm.__get__(m)
        return c.solve().results()
    if mid in ("k_scales_torsion_too", "k_in_plane_only"):
        orig = c.mems[0].__class__.system_matrix
        for m in c.mems:
            if m.kind != "arc":
                continue

            def sm(self, sec, mat, w, P, eps0, wall=True, mid=mid):
                A = orig(self, sec, mat, w, P, eps0, wall)
                EI, GJ = mat.E * sec.I, mat.G * sec.J
                if mid == "k_scales_torsion_too":
                    A[9][3] = self.k / GJ
                else:
                    A[10][4] = ONE / EI
                return A
            m.system_matrix = sm.__get__(m)
        return c.solve().results()
    if mid == "caps_along_chord":
        # replace end tangents by chord directions in the point loads
        def chord_dir(m, at_end):
            d = sub(m.xj, m.xi) if m.forward else sub(m.xi, m.xj)
            return mul(ONE / L.norm(d), d)
        c.t_start = lambda m: chord_dir(c.mems[m], False)
        c.t_end = lambda m: chord_dir(c.mems[m], True)
        return c.solve().results()
    raise KeyError(mid)


def part2(data):
    print("== extra mutants (coverage): best distance in tolerances over nodes, supports and stations ==")
    for mid, desc in EXTRA:
        best = (D(0), None, None)
        for cid, case in data["cases"].items():
            if case.get("transform") is not None:
                continue
            try:
                resm = extra_mutant_results(case, mid)
            except Exception as e:  # noqa: BLE001
                print("   %s on %s failed: %r" % (mid, cid, e))
                continue
            leaves = []
            C.walk(case["expected"], resm, [], leaves)
            zs = {g: D(v["zero_scale"]) for g, v in case["zero_scale"].items()}
            for path, ref, mine, _ in leaves:
                if ref in ("MISSING", "EXTRA"):
                    continue
                g = C.group_of(path)
                if not g or path[0] == "terminals":
                    continue
                dist = abs(mine - ref) / (D("1e-9") * max(abs(ref), zs[g]))
                if dist > best[0]:
                    best = (dist, cid, "/".join(path))
        print("%-32s %-70s best %.2e in %s at %s" % (mid, desc, best[0], best[1], best[2]))


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    part1(data)
    part2(data)
