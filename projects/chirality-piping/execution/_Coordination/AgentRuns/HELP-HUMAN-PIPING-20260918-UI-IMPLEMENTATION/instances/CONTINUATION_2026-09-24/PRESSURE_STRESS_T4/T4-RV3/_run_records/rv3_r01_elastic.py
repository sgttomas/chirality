"""T4-RV3 addendum 01: check T4-I7's chord_frame_elastic rows as the curved element's elastic end action
K_b (d - u_free(eps_p + eps_th)) - p_w, formed in Decimal from my own pieces:
  K_b  - the 12x12 arc stiffness from the inverse of my transfer-matrix tip flexibility, assembled by rigid
         transfer over the chord;
  d    - my transfer-matrix node motions;
  u_free - the homothety (eps_p + eps_th)(x - x_i) with zero rotation;
  p_w  - the clamped-clamped self-weight end actions from my transfer matrix.
This does not use the identity "wall minus c_b".

    python -I -B rv3_r01_elastic.py <round-01 u2_reference_cases.json>
"""
import json
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_lib as L  # noqa: E402
import rv3_solve as S  # noqa: E402
from rv3_lib import ZERO, ONE  # noqa: E402


def blk(rows):
    out = [[ZERO] * 6 for _ in range(6)]
    for b in range(2):
        for i in range(3):
            for j in range(3):
                out[3 * b + i][3 * b + j] = rows[i][j]
    return out


def inv(A):
    n = len(A)
    cols = [L.solve(A, [ONE if i == j else ZERO for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def arc_parts(case, mem):
    save = mem.forward
    mem.set_traversal(True)
    A0 = mem.system_matrix(case.sec, case.mat, ZERO, ZERO, ZERO, wall=False)
    E0 = L.expm(A0, mem.L)
    Aw = mem.system_matrix(case.sec, case.mat, case.w, ZERO, ZERO, wall=False)
    Ew = L.expm(Aw, mem.L)
    fr0, fr1 = mem.frame0, mem.frame_at(mem.L)
    mem.set_traversal(save)
    # tip flexibility (end-frame comps) -> global
    EFF = [[E0[r][c] for c in range(6)] for r in range(6)]
    EuF = [[E0[6 + r][c] for c in range(6)] for r in range(6)]
    Fl = L.matmul(EuF, inv(EFF))
    G = blk([list(e) for e in fr1])
    Gt = [list(r) for r in zip(*G)]
    Kjj = inv(L.matmul(Gt, L.matmul(Fl, G)))
    d = L.sub(mem.xj, mem.xi)
    Gam = [[ONE if i == j else ZERO for j in range(6)] for i in range(6)]
    dx = [[ZERO, -d[2], d[1]], [d[2], ZERO, -d[0]], [-d[1], d[0], ZERO]]
    for i in range(3):
        for j in range(3):
            Gam[i][3 + j] = -dx[i][j]
    GamT = [list(r) for r in zip(*Gam)]
    Kii = L.matmul(GamT, L.matmul(Kjj, Gam))
    Kij = [[-x for x in r] for r in L.matmul(GamT, Kjj)]
    Kji = [[-x for x in r] for r in L.matmul(Kjj, Gam)]
    K = [[ZERO] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            K[i][j], K[i][6 + j], K[6 + i][j], K[6 + i][6 + j] = Kii[i][j], Kij[i][j], Kji[i][j], Kjj[i][j]
    # clamped self-weight end actions
    pw = [ZERO] * 12
    if case.w != 0:
        g0 = L.to_local(fr0, L.gdir_global())
        yp = [ZERO] * 12 + list(g0) + [ONE]
        ypL = L.matvec(Ew, yp)
        Am = [[Ew[6 + r][k] for k in range(6)] for r in range(6)]
        c = L.solve(Am, [-ypL[6 + r] for r in range(6)])
        y0 = yp[:]
        for k in range(6):
            y0[k] += c[k]
        yL = L.matvec(Ew, y0)
        F0, M0 = L.to_global(fr0, y0[0:3]), L.to_global(fr0, y0[3:6])
        FL, ML = L.to_global(fr1, yL[0:3]), L.to_global(fr1, yL[3:6])
        pw = list(F0) + list(M0) + [-x for x in list(FL) + list(ML)]
    return K, pw


def main(path):
    data = json.load(open(path))
    worst_all = (D(0), None)
    worst_id = D(0)
    for cid, case in data["cases"].items():
        if case["expected"] is None:
            continue
        c = S.Case(case["inputs"]).solve()
        motion = c.node_motion()
        zs = {g: D(v["zero_scale"]) for g, v in case["zero_scale"].items()}
        eps = (1 - 2 * c.mat.nu) * c.P / (c.mat.E * c.sec.As) + c.eps_th
        worst = (D(0), None)
        for m in c.mems:
            if m.kind != "arc":
                continue
            K, pw = arc_parts(c, m)
            dvec = motion[m.a_from] + motion[m.a_to]
            uf = [ZERO] * 6 + list(L.mul(eps, L.sub(m.xj, m.xi))) + [ZERO] * 3
            fe = [sum(K[r][q] * (dvec[q] - uf[q]) for q in range(12)) - pw[r] for r in range(12)]
            ref = case["expected"]["members"][m.pid]["end_rows"]
            for end, sl in (("end_i", slice(0, 6)), ("end_j", slice(6, 12))):
                F, M = fe[sl][:3], fe[sl][3:]
                comps = [L.dot(F, e) for e in m.chord_frame] + [L.dot(M, e) for e in m.chord_frame]
                r = ref[end]["chord_frame_elastic"]
                for key, val in zip(["F_x", "F_y", "F_z", "M_x", "M_y", "M_z"], comps):
                    g = "elastic_end_force_chord_frame" if key.startswith("F") else "section_moment"
                    dn = abs(val - D(r[key])) / max(abs(D(r[key])), zs[g])
                    if dn > worst[0]:
                        worst = (dn, "%s/%s/%s" % (m.pid, end, key))
                # identity check: tangent-frame wall F_x minus the c_b axial term equals the elastic axial
                tf = ref[end]["tangent_frame"]
                fr = m.authored_frame(D(0) if end == "end_i" else D(1))
                el_t = L.dot(F, fr[0])
                wall_minus_cb = D(tf["F_x"]) + (c.P if end == "end_i" else -c.P)
                worst_id = max(worst_id, abs(el_t - wall_minus_cb) / max(abs(D(tf["F_x"])), zs["wall_axial_force"]))
        if worst[1] is not None:
            print("%-50s chord_frame_elastic vs K(d - u_free) - p_w: max norm diff %.2e at %s" % (cid, worst[0], worst[1]))
            if worst[0] > worst_all[0]:
                worst_all = (worst[0], cid + " " + worst[1])
    print("OVERALL chord_frame_elastic max normalized difference %.3e (%s)" % worst_all)
    print("tangent-frame identity N_el = N_w - pAi at arc ends: max normalized difference %.3e" % worst_id)


if __name__ == "__main__":
    main(sys.argv[1])
