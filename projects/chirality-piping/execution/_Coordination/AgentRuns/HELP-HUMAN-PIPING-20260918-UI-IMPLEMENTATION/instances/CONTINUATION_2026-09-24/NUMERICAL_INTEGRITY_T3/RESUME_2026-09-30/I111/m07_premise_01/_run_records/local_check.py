"""Exact (Fraction) transcription of frame_kernel user_stiffness_local_matrix
(NUM PP/../solver/frame_kernel/src/lib.rs:1739-1758) and its rigid/equilibrium checks
in the element's local frame (x along the element, length L)."""
from fractions import Fraction as F
UX, UY, UZ, RX, RY, RZ = range(6)
def local(ka, kl, kang, kt):
    K = [[F(0)] * 12 for _ in range(12)]
    for dof, k in ((UX, ka), (UY, kl), (UZ, kl), (RX, kt), (RY, kang), (RZ, kang)):
        o = dof + 6
        K[dof][dof] += k; K[o][o] += k; K[dof][o] -= k; K[o][dof] -= k
    return K
def mul(K, d): return [sum(K[r][c] * d[c] for c in range(12)) for r in range(12)]
L = F(22, 10)
K = local(F(3200000), F(900000), F(480000), F(620000))
th = F(1, 1000)
# rigid rotation theta about local z through node i: u_j,y = theta*L, both RZ = theta
d = [F(0)] * 12; d[RZ] = th; d[6 + UY] = th * L; d[6 + RZ] = th
f = mul(K, d)
print("rigid rotation about local z, theta=1e-3: nonzero end actions", {i: float(v) for i, v in enumerate(f) if v})
# relative lateral displacement delta at node j (local y); moment of end actions about node i (z component)
delta = F("299.28943672347367") / F(900000)
d = [F(0)] * 12; d[6 + UY] = delta
f = mul(K, d)
mz = f[RZ] + f[6 + RZ] + L * f[6 + UY]   # x_j - x_i = L ex; (L ex x F_j)_z = L*F_j,y
print("delta =", float(delta), "end Fy_i, Fy_j =", float(f[UY]), float(f[6 + UY]), "Mz_i, Mz_j =", float(f[RZ]), float(f[6 + RZ]))
print("net moment about node i (z) =", float(mz), "N*m  (k*delta*L =", float(F(900000) * delta * L), ")")
print("cited 900000*3.3254e-4*2.2 =", float(F(900000) * F("3.3254e-4") * L))
# control: lateral = 0 passes the rigid rotation test
K0 = local(F(3200000), F(0), F(480000), F(620000))
d = [F(0)] * 12; d[RZ] = th; d[6 + UY] = th * L; d[6 + RZ] = th
print("control lateral=0 rigid rotation max|f| =", max(abs(v) for v in mul(K0, d)))
