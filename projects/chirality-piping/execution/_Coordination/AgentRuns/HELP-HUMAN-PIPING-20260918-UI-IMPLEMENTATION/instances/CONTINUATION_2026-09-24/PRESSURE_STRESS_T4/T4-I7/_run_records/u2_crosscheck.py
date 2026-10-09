"""T4-I7 cross-checks (not references): the plan's H-2 ledger (F1), the uniform-eigenstrain form
Sigma K_m u_free(eps_p) (F2), product-style recovery (arc stations from the elastic end force plus
the +pAi membrane), and the thermal analogue, each compared with the frozen direct-method values
in u2_reference_cases.json.

    python -I u2_crosscheck.py <dir containing u2_reference_cases.json>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_engine as E  # noqa: E402
import u2_generate as G  # noqa: E402
from u2_engine import D, ZERO, ONE, v, add, sub, scl, dot, cross, norm  # noqa: E402


def skew(r):
    return [[ZERO, -r[2], r[1]], [r[2], ZERO, -r[0]], [-r[1], r[0], ZERO]]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def unit_act(xe, X, a):
    if a < 3:
        e = E.EAX[a]
        return e, cross(sub(xe, X), e)
    return E.VZERO, E.EAX[a - 3]


def member_matrices(mem, P, wvec, wall):
    """Traversal-oriented element: K (12x12, global), and the fixed-end load vector of the member's own
    distributed loads (wall if requested, and weight)."""
    EA = mem.mat.E * mem.sec.As
    GJ = mem.mat.G * mem.sec.J
    EI = mem.mat.E * mem.sec.I
    k = mem.k
    xs, xe = mem.start_point(), mem.end_point()
    pts = []
    for s, w in mem.gl_points():
        X = mem.pos(s)
        t = mem.tan(s)
        F, M = mem.partial(s, P, wvec, wall)
        pts.append((w, X, t, F, M))

    def bil(Fa, Ma, Fb, Mb, t):
        Na, Nb, Ta, Tb = dot(Fa, t), dot(Fb, t), dot(Ma, t), dot(Mb, t)
        return Na * Nb / EA + Ta * Tb / GJ + k * (dot(Ma, Mb) - Ta * Tb) / EI

    Fl = [[ZERO] * 6 for _ in range(6)]
    d0 = [ZERO] * 6
    for w, X, t, F, M in pts:
        ua = [unit_act(xe, X, a) for a in range(6)]
        for a in range(6):
            d0[a] += w * bil(ua[a][0], ua[a][1], F, M, t)
            for b in range(a, 6):
                Fl[a][b] += w * bil(ua[a][0], ua[a][1], ua[b][0], ua[b][1], t)
    for a in range(6):
        for b in range(a):
            Fl[a][b] = Fl[b][a]
    Kjj = E.inverse(Fl)
    r = sub(xe, xs)
    T = [[ONE if i == j else ZERO for j in range(6)] for i in range(6)]
    S = skew(r)
    for i in range(3):
        for j in range(3):
            T[3 + i][j] = S[i][j]
    TK = matmul(T, Kjj)
    TKTt = matmul(TK, transpose(T))
    KTt = matmul(Kjj, transpose(T))
    K = [[ZERO] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            K[i][j] = TKTt[i][j]
            K[i][6 + j] = -TK[i][j]
            K[6 + i][j] = -KTt[i][j]
            K[6 + i][6 + j] = Kjj[i][j]
    X = [-sum(Kjj[a][b] * d0[b] for b in range(6)) for a in range(6)]
    Fw, Mw = mem.partial(ZERO, P, wvec, wall)  # about xs
    Wi = list(Fw) + list(Mw)
    TX = [sum(T[a][b] * X[b] for b in range(6)) for a in range(6)]
    p = [TX[a] + Wi[a] for a in range(6)] + [-x for x in X]
    return K, p, r


def ufree(r, eps):
    return [ZERO] * 6 + [eps * r[0], eps * r[1], eps * r[2], ZERO, ZERO, ZERO]


def kvec(K, u):
    return [sum(K[i][j] * u[j] for j in range(12)) for i in range(12)]


def stiffness_solution(case, form):
    chain, sec, mat = G.build_chain(case)
    lc = G.load_case(case, sec)
    P = lc.p * sec.Ai
    wvec = scl(lc.w, lc.gdir)
    nn = len(chain.node_ids)
    ndof = 6 * nn
    Kg = [[ZERO] * ndof for _ in range(ndof)]
    Fg = [ZERO] * ndof
    elem = []
    tans = chain.trav_tangents()
    eps_p = (1 - 2 * mat.nu) * P / (mat.E * sec.As)
    eps_th = mat.alpha * lc.dT
    for mi, mem in enumerate(chain.members):
        K, pw, r = member_matrices(mem, ZERO, wvec, False)  # weight-only fixed-end vector
        t0, t1 = tans[mi]
        pe = list(pw)
        th = kvec(K, ufree(r, eps_th))
        pe = [a + b for a, b in zip(pe, th)]
        if form == "F1":
            if mem.kind == "straight":
                pois = list(scl(2 * mat.nu * P, t0)) + [ZERO] * 3 + list(scl(-2 * mat.nu * P, t1)) + [ZERO] * 3
            else:
                kuf = kvec(K, ufree(r, eps_p))
                cb = list(scl(-P, t0)) + [ZERO] * 3 + list(scl(P, t1)) + [ZERO] * 3
                pois = [a - b for a, b in zip(kuf, cb)]
            pe = [a + b for a, b in zip(pe, pois)]
        else:  # F2: K u_free(eps_p) on every member; caps are then member-owned
            pe = [a + b for a, b in zip(pe, kvec(K, ufree(r, eps_p)))]
        idx = list(range(6 * mi, 6 * mi + 12))
        for a in range(12):
            Fg[idx[a]] += pe[a]
            for b in range(12):
                Kg[idx[a]][idx[b]] += K[a][b]
        elem.append((K, pe, idx))
    # nodal pressure terms
    if form == "F1":
        if lc.transfer_A:
            for a in range(3):
                Fg[a] += -P * tans[0][0][a]
        if lc.transfer_D:
            for a in range(3):
                Fg[6 * (nn - 1) + a] += P * tans[-1][1][a]
        for m in range(len(chain.members) - 1):
            if chain.members[m].kind == "arc" or chain.members[m + 1].kind == "arc":
                for a in range(3):
                    Fg[6 * (m + 1) + a] += P * (tans[m][1][a] - tans[m + 1][0][a])
    else:
        if not lc.transfer_A:
            for a in range(3):
                Fg[a] -= -P * tans[0][0][a]
        if not lc.transfer_D:
            for a in range(3):
                Fg[6 * (nn - 1) + a] -= P * tans[-1][1][a]
    fixed = set(range(6))
    if lc.anchor_D:
        fixed |= set(range(6 * (nn - 1), 6 * nn))
    free = [i for i in range(ndof) if i not in fixed]
    sol = E.solve([[Kg[i][j] for j in free] for i in free], [Fg[i] for i in free])
    d = [ZERO] * ndof
    for i, x in zip(free, sol):
        d[i] = x
    Kd = [sum(Kg[i][j] * d[j] for j in range(ndof)) for i in range(ndof)]
    reac = {"support:A": [Kd[i] - Fg[i] for i in range(6)]}
    if lc.anchor_D:
        reac["support:D"] = [Kd[i] - Fg[i] for i in range(6 * (nn - 1), 6 * nn)]
    ends = []
    for (K, pe, idx), mem in zip(elem, chain.members):
        de = [d[i] for i in idx]
        q = [a - b for a, b in zip(kvec(K, de), pe)]
        ends.append(q)
    return chain, sec, mat, lc, P, d, reac, ends


def rel(x, ref, scale):
    return abs(D(x) - D(ref)) / max(abs(D(ref)), D(scale))


def compare(case, rec, form):
    chain, sec, mat, lc, P, d, reac, ends = stiffness_solution(case, form)
    exp = rec["expected"]
    zs = rec["zero_scale"]
    worst = {}

    def upd(key, x, ref, grp):
        r = rel(x, ref, zs[grp]["zero_scale"])
        if r > worst.get(key, ZERO):
            worst[key] = r

    for ni, nid in enumerate(chain.node_ids):
        for a, k in enumerate(["ux", "uy", "uz", "rx", "ry", "rz"]):
            upd("displacements", d[6 * ni + a], exp["nodes"][nid][k], G.GROUP_OF[k])
    for sid, R in reac.items():
        for a, k in enumerate(["Fx", "Fy", "Fz", "Mx", "My", "Mz"]):
            upd("reactions", R[a], exp["supports"][sid][k], ("support_force" if a < 3 else "support_moment") + "@" + sid)
    wvec = scl(lc.w, lc.gdir)
    if form == "F2":
        return worst  # F2's member end forces are not wall actions; solution-level comparison only
    for mi, mem in enumerate(chain.members):
        q = ends[mi]
        qt = (q[0:6], q[6:12])  # traversal start, end (node-on-element)
        auth = {"end_i": qt[0] if mem.forward else qt[1], "end_j": qt[1] if mem.forward else qt[0]}
        for name, f in (("end_i", "0"), ("end_j", "1")):
            Fq = tuple(auth[name][0:3])
            Mq = tuple(auth[name][3:6])
            frame = mem.frame_at_authored(f)
            ref = exp["members"][mem.pid]["end_rows"][name]
            ref = ref["element_local"] if mem.kind == "straight" else ref["tangent_frame"]
            fname = "element_local" if mem.kind == "straight" else "tangent_frame"
            for a, k in enumerate(["F_x", "F_y", "F_z"]):
                upd("end_rows_" + mem.kind, dot(Fq, frame[a]), ref[k], G.end_group(k, fname))
            for a, k in enumerate(["M_x", "M_y", "M_z"]):
                upd("end_rows_" + mem.kind, dot(Mq, frame[a]), ref[k], G.end_group(k, fname))
        # product-style station recovery from the authored j-end action
        Fj = tuple(auth["end_j"][0:3])
        Mj = tuple(auth["end_j"][3:6])
        xj = mem.xj
        if mem.kind == "arc" and form == "F1":
            tj = mem.authored_tangent("1")
            Fel = sub(Fj, scl(P, tj))  # elastic end force: remove c_b at j
        else:
            Fel = Fj
        for name, f in G.STATIONS:
            if mem.kind == "arc":
                th = D(f) * mem.Phi
                Dl = mem.Phi - th
                er = add(scl(E.cos(th), mem.xhat), scl(E.sin(th), mem.yhat))
                X = add(mem.centre, scl(mem.R, er))
                Er = add(scl(E.sin(mem.Phi) - E.sin(th), mem.xhat), scl(E.cos(th) - E.cos(mem.Phi), mem.yhat))
                F = add(Fel, scl(mem.R * Dl, wvec))
                M = add(add(Mj, cross(sub(xj, X), Fel)), cross(scl(mem.R * mem.R, sub(Er, scl(Dl, er))), wvec))
                if form == "F1":
                    F = add(F, scl(P, mem.authored_tangent(f)))  # +pAi membrane along t(theta)
            else:
                s = D(f) * mem.length
                X = add(mem.xi, scl(s, mem.ex))
                rr = mem.length - s
                F = add(Fel, scl(rr, wvec))
                M = add(add(Mj, cross(sub(xj, X), Fel)), cross(scl(rr / 2, mem.ex), scl(rr, wvec)))
            frame = mem.frame_at_authored(f)
            st = exp["members"][mem.pid]["stations"][name]
            vals = dict(N_w=dot(F, frame[0]), V_y=dot(F, frame[1]), V_z=dot(F, frame[2]), T=dot(M, frame[0]),
                        M_y=dot(M, frame[1]), M_z=dot(M, frame[2]))
            vals["S"] = vals["N_w"] - P
            for k, x in vals.items():
                upd("stations_" + mem.kind, x, st[k], G.GROUP_OF[k])
    return worst


def thermal_analogue(case, rec):
    chain, sec, mat = G.build_chain(case)
    lc0 = G.load_case(case, sec)
    P = lc0.p * sec.Ai
    eps_p = (1 - 2 * mat.nu) * P / (mat.E * sec.As)
    lc = E.LoadCase(p="0", dT=eps_p / mat.alpha, w="0", anchor_D=True)
    sol = E.analyse(chain, lc)
    worst = ZERO
    exp = rec["expected"]["supports"]
    zs = rec["zero_scale"]
    for sid, R in (("support:A", sol.R_A), ("support:D", sol.R_D)):
        for a, k in enumerate(["Fx", "Fy", "Fz", "Mx", "My", "Mz"]):
            worst = max(worst, rel(R[a], exp[sid][k], zs[("support_force" if a < 3 else "support_moment") + "@" + sid]
                                   ["zero_scale"]))
    return worst


def main(d):
    ref = json.load(open(os.path.join(d, "u2_reference_cases.json")))
    cases = {c["id"]: c for c in G.case_list()}
    overall = {}
    print("F1 = plan H-2 ledger; F2 = Sigma K_m u_free(eps_p); both with curved-element stiffness from the same "
          "unit-load flexibility (cross-checks only)")
    for cid, rec in ref["cases"].items():
        for form in ("F1", "F2"):
            w = compare(cases[cid], rec, form)
            for k, x in w.items():
                key = form + ":" + k
                if x > overall.get(key, (ZERO, ""))[0]:
                    overall[key] = (x, cid)
    for k in sorted(overall):
        print("max normwise rel diff %-26s %s  (worst case %s)" % (k, format(overall[k][0], ".3e"), overall[k][1]))
    worst = (ZERO, "")
    for cid, c in cases.items():
        if c["anchorD"] and c["tA"] and c["tD"] and D(c["dT"]) == 0 and not c["weight"] and "KINK" not in cid:
            x = thermal_analogue(c, ref["cases"][cid])
            if x > worst[0]:
                worst = (x, cid)
    print("thermal analogue (reactions of the eps_p thermal problem vs pressure-only reference): max %s (%s)"
          % (format(worst[0], ".3e"), worst[1]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
