"""T4-RV3: build a case from the inputs block of T4-I7's u2_reference_cases.json and solve it by the
transfer-matrix method of rv3_lib.  Returns a result tree shaped like the reference's `expected` block.
Coordinates and y_reference strings are parsed to binary64 first (what a test and the product read),
then taken exactly (Decimal(float))."""
from decimal import Decimal as D
import rv3_lib as L
from rv3_lib import ZERO, ONE, add, sub, mul, dot, cross, norm, to_global, to_local

STATIONS = [("end_i", D(0)), ("quarter_1", D("0.25")), ("midspan", D("0.5")), ("quarter_3", D("0.75")),
            ("end_j", D(1))]


def b64(s, exact_decimal=False):
    return D(s) if exact_decimal else D(float(s))


class Case:
    def __init__(self, inp, exact_decimal_coords=False, mutation=None):
        mutation = mutation or {}
        self.mut = mutation
        g = inp["geometry"]
        self.coords = {nid: tuple(b64(c, exact_decimal_coords) for c in xyz)
                       for nid, xyz in g["node_coordinates_binary64_exact"].items()}
        self.order = list(g["traversal_order"])
        sec = inp["section"]
        self.sec = L.Section(sec["outside_diameter"], sec["wall_thickness"], sec["mill_tolerance"])
        mat = inp["material"]
        self.mat = L.Material(mat["E"], mat["nu"], mat["alpha_per_degC"])
        self.p = D(inp["pressure"]["p_Pa"])
        self.P = self.p * self.sec.Ai
        self.dT = D(inp["thermal"]["delta_T_degC"])
        self.w = D(inp["self_weight"]["w_N_per_m"])
        self.tA = inp["pressure"]["terminal_A"] == "transfers_to_wall"
        self.tD = inp["pressure"]["terminal_D"] == "transfers_to_wall"
        sup = inp["supports"]
        self.anchorD = any(s.startswith("support:D anchor") for s in sup)
        assert any(s.startswith("support:A anchor at " + self.order[0]) for s in sup)
        mems = []
        for m in g["members"]:
            yref = tuple(b64(c, exact_decimal_coords) for c in m["y_reference_binary64_exact"])
            xi, xj = self.coords[m["authored_from"]], self.coords[m["authored_to"]]
            if m["kind"] == "straight":
                mems.append(L.Member(m["pipe"], "straight", m["authored_from"], m["authored_to"], xi, xj, yref))
            else:
                mems.append(L.Member(m["pipe"], "arc", m["authored_from"], m["authored_to"], xi, xj, yref,
                                     R=m["bend_radius"], k=m["flexibility_factor_k"]))
        # order members along the traversal
        self.mems = []
        for n in range(len(self.order) - 1):
            a, b = self.order[n], self.order[n + 1]
            for m in mems:
                if (m.a_from, m.a_to) == (a, b):
                    m.set_traversal(True)
                    break
                if (m.a_from, m.a_to) == (b, a):
                    m.set_traversal(False)
                    break
            else:
                raise ValueError("no member between %s and %s" % (a, b))
            self.mems.append(m)
        E, nu = self.mat.E, self.mat.nu
        self.eps_nu = -2 * nu * self.P / (E * self.sec.As)
        self.eps_th = self.mat.alpha * self.dT

    # tangents along the traversal
    def t_start(self, m):
        return self.mems[m].frame0[0]

    def t_end(self, m):
        mem = self.mems[m]
        return mem.frame_at(mem.L)[0]

    def point_loads(self):
        n = len(self.order)
        pts = {i: [] for i in range(n)}
        P = self.P
        if self.tA:
            pts[0].append(mul(-P, self.t_start(0)))
        if self.tD:
            pts[n - 1].append(mul(P, self.t_end(len(self.mems) - 1)))
        for i in range(1, n - 1):
            if i in self.mut.get("remove_kink_at", ()):
                continue
            kf = mul(P, sub(self.t_end(i - 1), self.t_start(i)))
            pts[i].append(kf)
        for i, f in self.mut.get("extra_point_loads", []):
            pts[i].append(f)
        return pts

    def solve(self):
        sec, mat = self.sec, self.mat
        self.pts = self.point_loads()
        nn = len(self.order)
        # per member system matrices and quarter-step exponentials
        self.E = []
        for mem in self.mems:
            eps0 = self.eps_th
            if mem.kind == "straight" or not self.mut.get("arc_no_poisson"):
                eps0 += self.eps_nu
            wall = not self.mut.get("arc_no_wall")
            A = mem.system_matrix(sec, mat, self.w, self.P, eps0, wall=wall)
            Eq = L.expm(A, mem.L / 4)
            E2 = L.matmul(Eq, Eq)
            E3 = L.matmul(E2, Eq)
            E4 = L.matmul(E2, E2)
            self.E.append([None, Eq, E2, E3, E4])
        g = L.gdir_global()

        def run(y0, particular):
            starts, ends = [], []
            y = y0
            for m, mem in enumerate(self.mems):
                starts.append(y)
                ye = L.matvec(self.E[m][4], y)
                fr = mem.frame_at(mem.L)
                blocks = [to_global(fr, ye[3 * b:3 * b + 3]) for b in range(5)]
                one = ye[15]
                ends.append((blocks, one))
                if m + 1 < len(self.mems):
                    if particular:
                        for f in self.pts[m + 1]:
                            blocks[0] = sub(blocks[0], f)
                    nf = self.mems[m + 1].frame0
                    y = []
                    for b in range(5):
                        y += list(to_local(nf, blocks[b]))
                    y.append(one)
            return starts, ends

        g0 = to_local(self.mems[0].frame0, g)
        yp = [ZERO] * 12 + list(g0) + [ONE]
        _, endp = run(yp, True)
        cols = []
        for k in range(6):
            yk = [ZERO] * 16
            yk[k] = ONE
            _, endk = run(yk, False)
            cols.append(endk[-1][0])
        bp = endp[-1][0]
        fD = V = (ZERO, ZERO, ZERO)
        for f in self.pts[nn - 1]:
            fD = add(fD, f)
        if self.anchorD:
            rows_p = list(bp[2]) + list(bp[3])
            Amat = [[(list(cols[k][2]) + list(cols[k][3]))[r] for k in range(6)] for r in range(6)]
        else:
            rows_p = list(sub(bp[0], fD)) + list(bp[1])
            Amat = [[(list(cols[k][0]) + list(cols[k][1]))[r] for k in range(6)] for r in range(6)]
        c = L.solve(Amat, [-x for x in rows_p])
        y0 = yp[:]
        for k in range(6):
            y0[k] += c[k]
        self.starts, self.ends = run(y0, True)
        fr0 = self.mems[0].frame0
        FA = to_global(fr0, y0[0:3])
        MA = to_global(fr0, y0[3:6])
        fA = (ZERO, ZERO, ZERO)
        for f in self.pts[0]:
            fA = add(fA, f)
        self.R_A = list(mul(-ONE, add(FA, fA))) + list(mul(-ONE, MA))
        blocksD = self.ends[-1][0]
        self.R_D = (list(sub(blocksD[0], fD)) + list(blocksD[1])) if self.anchorD else None
        return self

    # j-side action (authored) at authored fraction f, global vectors
    def jside(self, m, f):
        mem = self.mems[m]
        s_frac = f if mem.forward else 1 - f
        q = int((s_frac * 4).to_integral_value())
        assert q * D("0.25") == s_frac
        y0 = self.starts[m]
        y = y0 if q == 0 else L.matvec(self.E[m][q], y0)
        fr = mem.frame_at(mem.L * s_frac)
        F = to_global(fr, y[0:3])
        M = to_global(fr, y[3:6])
        if not mem.forward:
            F, M = mul(-ONE, F), mul(-ONE, M)
        return F, M

    def node_motion(self):
        out = {self.order[0]: [ZERO] * 6}
        for m in range(len(self.mems)):
            blocks, _ = self.ends[m]
            out[self.order[m + 1]] = list(blocks[2]) + list(blocks[3])
        return out

    def results(self):
        sec, P = self.sec, self.P
        res = {"nodes": {}, "supports": {}, "members": {}, "terminals": {}}
        for nid, vals in self.node_motion().items():
            res["nodes"][nid] = dict(zip(["ux", "uy", "uz", "rx", "ry", "rz"], vals))
        res["supports"]["support:A"] = dict(zip(["Fx", "Fy", "Fz", "Mx", "My", "Mz"], self.R_A))
        if self.anchorD:
            res["supports"]["support:D"] = dict(zip(["Fx", "Fy", "Fz", "Mx", "My", "Mz"], self.R_D))
        nlast = len(self.mems) - 1
        for node, transfer, outward in ((self.order[0], self.tA, mul(-P, self.t_start(0))),
                                        (self.order[-1], self.tD, mul(P, self.t_end(nlast)))):
            t = {"closure_pressure_load_global": dict(zip(["Fx", "Fy", "Fz"], outward)),
                 "pipe_cap_transfer_global": dict(zip(["Fx", "Fy", "Fz"], outward if transfer else (ZERO,) * 3)),
                 "remote_closure_support_reaction_global":
                     None if transfer else dict(zip(["Fx", "Fy", "Fz"], mul(-ONE, outward)))}
            res["terminals"][node] = t
        for m, mem in enumerate(self.mems):
            md = {"stations": {}, "end_rows": {}}
            acts = {}
            for name, f in STATIONS:
                F, M = self.jside(m, f)
                acts[name] = (F, M)
                fr = mem.authored_frame(f)
                N, Vy, Vz = (dot(F, e) for e in fr)
                T, My, Mz = (dot(M, e) for e in fr)
                md["stations"][name] = dict(N_w=N, S=N - P, sigma_m=N / sec.As, V_y=Vy, V_z=Vz, T=T, M_y=My,
                                            M_z=Mz, sigma_b_y=My / sec.Z, sigma_b_z=Mz / sec.Z,
                                            tau_t=T * sec.ro / sec.J)
            for name, f, sgn in (("end_i", D(0), -ONE), ("end_j", D(1), ONE)):
                F, M = acts[name]
                frames = [("element_local", mem.authored_frame(f))] if mem.kind == "straight" else \
                    [("tangent_frame", mem.authored_frame(f)), ("chord_frame", mem.chord_frame)]
                dd = {}
                for fname, fr in frames:
                    comps = [sgn * dot(F, e) for e in fr] + [sgn * dot(M, e) for e in fr]
                    d = dict(zip(["F_x", "F_y", "F_z", "M_x", "M_y", "M_z"], comps))
                    if fname != "chord_frame":
                        d["wall_axial_end_action"] = comps[0]
                    dd[fname] = d
                md["end_rows"][name] = dd
            if mem.kind == "straight":
                md["frame"] = {"x": list(mem.chord_frame[0]), "y": list(mem.chord_frame[1]),
                               "z": list(mem.chord_frame[2])}
                md["length"] = mem.L
                md["lame_surface"] = {"inner_radial": -self.p, "outer_radial": ZERO,
                                      "inner_hoop": 2 * P / sec.As + self.p, "outer_hoop": 2 * P / sec.As}
            else:
                md["arc"] = {"R": mem.R, "included_angle": mem.Phi, "arc_length": mem.L, "centre": list(mem.c),
                             "tangent_i": list(mem.authored_frame(D(0))[0]),
                             "tangent_j": list(mem.authored_frame(D(1))[0]),
                             "plane_normal_z": list(mem.zhat), "k": mem.k,
                             "chord_frame": {"x": list(mem.chord_frame[0]), "y": list(mem.chord_frame[1]),
                                             "z": list(mem.chord_frame[2])}}
            res["members"][mem.pid] = md
        return res

    def kinks(self):
        out = []
        for i in range(1, len(self.order) - 1):
            a, b = self.t_end(i - 1), self.t_start(i)
            out.append((self.order[i], L.atan2(norm(cross(a, b)), dot(a, b))))
        return out
