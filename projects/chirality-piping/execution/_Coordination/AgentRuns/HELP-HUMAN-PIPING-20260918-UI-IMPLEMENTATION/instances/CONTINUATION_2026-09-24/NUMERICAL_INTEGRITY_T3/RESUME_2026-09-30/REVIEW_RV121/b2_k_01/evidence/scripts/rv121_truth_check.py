"""RV121's independent re-derivation of a subset of the B2-K combination oracle (standard library only).
Reads the committed fixture (argv[1]) as data. Independent of the generator: its own K4LED encoder, its own
directed 1024-bit rounding, closed-form cantilever flexibility (no stiffness matrix or elimination), an Euler
pi bracket (atan 1/2 + atan 1/3, alternating-series bounds) instead of Machin, and closed statics."""
import sys, re, struct, hashlib, json, math
from fractions import Fraction as F
txt = open(sys.argv[1]).read()
def f64(b): return struct.unpack('>d', struct.pack('>Q', b))[0]
def tokval(t):
    if t == 'Z+': return F(0)
    sign = -1 if t[0] == '-' else 1
    h, e = t[1:].split('p')
    return sign * int(h.ljust(256, '0'), 16) * F(2) ** (int(e) - 1023)
sec = [int(x, 16) for x in re.search(r'SECTION: \[u64; 5\] = \[([^\]]*)\]', txt).group(1).split(', ')]
AK, IK, JK, ZK, C = (F(f64(b)) for b in sec)
ops = {}
for name, body in re.findall(r'\("(\w+)", &\[((?:\(\d+, \d+, 0x[0-9a-f]+\)(?:, )?)*)\]\),', txt.split('COMBINATIONS')[0]):
    ops[name] = [(int(n), int(c), F(f64(int(v, 16)))) for n, c, v in re.findall(r'\((\d+), (\d+), 0x([0-9a-f]+)\)', body)]
combos = {}
for m in re.finditer(r'    \("(C\d)", &\[(.*?)\],\n     "([0-9a-f]+)",\n     &\[(.*?)\],\n     &\[\n(.*?)     \]\),', txt, re.S):
    name = m.group(1)
    terms = [(F(f64(int(f, 16))), o, p == 'true') for f, o, p in re.findall(r'\(0x([0-9a-f]+), "(\w+)", (true|false)\)', m.group(2))]
    nets = [(int(g), a, b, c) for g, a, b, c in re.findall(r'\((\d+), "([^"]+)", "([^"]+)", "([^"]+)"\)', m.group(4))]
    rows = {k: ((a, b), (c, d)) for k, a, b, c, d in re.findall(r'\("([^"]+)", \("([^"]+)", "([^"]+)"\), \("([^"]+)", "([^"]+)"\)\)', m.group(5))}
    combos[name] = (terms, m.group(3), nets, rows)
assert len(combos) == 9, sorted(combos)
# ---- exact nets and my own K4LED encoder
def nets_of(terms):
    n = {}
    for c, o, _ in terms:
        for node, comp, v in ops[o]:
            g = node * 6 + comp; n[g] = n.get(g, F(0)) + c * v
    return dict(sorted(n.items()))
def k4led(n):
    out = b'K4LED\x01' + struct.pack('<I', len(n))
    for g, v in n.items():
        node, comp = divmod(g, 6)
        if v == 0: neg, mag, e = 0, 0, 0
        else:
            neg = int(v < 0); a = abs(v); e = 0
            num, den = a.numerator, a.denominator
            assert den & (den - 1) == 0
            e = -(den.bit_length() - 1)
            tz = (num & -num).bit_length() - 1
            mag, e = num >> tz, e + tz
        limbs = []
        while mag: limbs.append(mag & (2 ** 64 - 1)); mag >>= 64
        out += struct.pack('<I', node) + bytes([comp, neg]) + struct.pack('<q', e) + struct.pack('<I', len(limbs))
        out += b''.join(struct.pack('<Q', l) for l in limbs)
    return out
def dirround(x, mode):  # 1024 significant bits; mode in ('d','u','n')
    if x == 0: return F(0)
    s = 1 if x > 0 else -1; a = abs(x)
    e = a.numerator.bit_length() - a.denominator.bit_length()
    if F(2) ** e > a: e -= 1
    q = a / F(2) ** (e - 1023)          # in [2^1023, 2^1024)
    fl = q.numerator // q.denominator; exact = fl * q.denominator == q.numerator
    if mode == 'n':
        r = q - fl; m = fl + (1 if (r > F(1, 2) or (r == F(1, 2) and fl % 2)) else 0)
    elif (mode == 'u') == (s > 0): m = fl + (0 if exact else 1)
    else: m = fl
    return s * m * F(2) ** (e - 1023)
# ---- Euler pi bracket: pi/4 = atan(1/2) + atan(1/3); alternating partial sums bracket each atan
def atan_bracket(q, K):
    s = F(0); prev = None
    for k in range(K):
        prev = s; s += F((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
    return (min(s, prev), max(s, prev))
a2, a3 = atan_bracket(2, 1400), atan_bracket(3, 1400)
PI = (4 * (a2[0] + a3[0]), 4 * (a2[1] + a3[1]))
assert PI[1] - PI[0] < F(1, 2 ** 1200) and PI[0] < F(355, 113) < PI[1] + 1
E, G = F(210e9), F(80e9)
D = F(0.1); T = F(0.005); c = D / 2; ri = c - T
p_ = c * c - ri * ri; g_ = c ** 4 - ri ** 4           # A = pi p_, I = pi g_/4, J = 2I
assert C == c
def tip(load, ea, gj, ei):
    Fx, Fy, Fz, Mx, My, Mz = load
    return [Fx / ea, Fy / (3 * ei) + Mz / (2 * ei), Fz / (3 * ei) - My / (2 * ei), Mx / gj,
            -Fz / (2 * ei) + My / ei, Fy / (2 * ei) + Mz / ei]
def law_g(pi): return (E * pi * p_, G * 2 * pi * g_ / 4, E * pi * g_ / 4)
law_k = (E * AK, G * JK, E * IK)
def inside(tok, lo, hi=None):
    hi = lo if hi is None else hi
    return tokval(tok[0]) <= lo and hi <= tokval(tok[1])
report = {}
for name, (terms, led_hex, netl, rows) in combos.items():
    n = nets_of(terms); checks = 0
    led = k4led(n)
    assert led.hex() == led_hex, (name, 'K4LED')
    for g, rd, ru, rn in netl:
        v = n[g]; assert v != 0
        assert (tokval(rd), tokval(ru), tokval(rn)) == (dirround(v, 'd'), dirround(v, 'u'), dirround(v, 'n')), (name, g)
        checks += 1
    assert len(netl) == sum(1 for v in n.values() if v != 0)
    load = [n.get(6 + k, F(0)) for k in range(6)]; root = [n.get(k, F(0)) for k in range(6)]
    uk = tip(load, *law_k)
    ug = [tip(load, *law_g(PI[0])), tip(load, *law_g(PI[1]))]
    for k in range(6):
        assert inside(rows[f'u1.{k}'][0], uk[k]), (name, 'u1 K', k)
        lo, hi = min(ug[0][k], ug[1][k]), max(ug[0][k], ug[1][k])
        assert inside(rows[f'u1.{k}'][1], lo, hi), (name, 'u1 G', k)
        assert rows[f'u0.{k}'] == (('Z+', 'Z+'), ('Z+', 'Z+'))
        checks += 3
    # root internal actions (End I as a section) and reactions, closed statics, L = 1
    N_, Vy, Vz, Tq = load[0], load[1], load[2], load[3]
    My, Mz = load[4] - load[2], load[5] + load[1]
    react = [-load[0] - root[0], -load[1] - root[1], -load[2] - root[2], -load[3] - root[3],
             -(load[4] - load[2]) - root[4], -(load[5] + load[1]) - root[5]]
    for k in range(6):
        assert inside(rows[f'r0.{k}'][0], react[k]) and inside(rows[f'r0.{k}'][1], react[k]), (name, 'r0', k)
        checks += 2
    sf2 = sum(v * v for v in react[:3]); sm2 = sum(v * v for v in react[3:])
    for key, s2 in (('sf3', sf2), ('sm3', sm2)):
        lo, hi = tokval(rows[key][0][0]), tokval(rows[key][0][1])
        assert lo >= 0 and lo * lo <= s2 <= hi * hi, (name, key); checks += 1
    m2 = sum(v * v for v in uk[:3]); lo, hi = tokval(rows['m1'][0][0]), tokval(rows['m1'][0][1])
    assert lo >= 0 and lo * lo <= m2 <= hi * hi, (name, 'm1 K'); checks += 1
    # stresses at End I: axial, bending y, bending z, torsion (SI)
    zk = (min(IK / c, ZK), max(IK / c, ZK))
    for k, (mom, kk) in enumerate(((None, None), (My, 1), (Mz, 2))):
        if k == 0:
            assert inside(rows['z7.I.0'][0], N_ / AK)
            gl = [N_ / (PI[0] * p_), N_ / (PI[1] * p_)]
            assert inside(rows['z7.I.0'][1], min(gl), max(gl)); checks += 2; continue
        kv = [mom / zk[0], mom / zk[1]]
        assert inside(rows[f'z7.I.{kk}'][0], min(kv), max(kv)), (name, 'z K', kk)
        gv = [mom * c / (PI[0] * g_ / 4), mom * c / (PI[1] * g_ / 4)]
        assert inside(rows[f'z7.I.{kk}'][1], min(gv), max(gv)), (name, 'z G', kk); checks += 2
    assert inside(rows['z7.I.3'][0], Tq * c / JK)
    tg = [Tq * c / (2 * PI[0] * g_ / 4), Tq * c / (2 * PI[1] * g_ / 4)]
    assert inside(rows['z7.I.3'][1], min(tg), max(tg)); checks += 2
    report[name] = {'k4led_sha256': hashlib.sha256(led).hexdigest(), 'checks': checks,
                    'nonzero_nets': len(netl), 'rows': len(rows)}
# discriminators
p_row = F(float((1 + F(2) ** -60) / law_k[0])); q_row = F(float(-1 / law_k[0]))
c3 = combos['C3'][3]['u1.0'][0]
report['C3_operand_row_sum'] = str(p_row + q_row)
report['C3_truth_excludes_0'] = tokval(c3[0]) > 0
n6 = nets_of(combos['C6'][0])[7]
report['C6_bits'] = (n6 * F(2) ** 600).numerator.bit_length()
report['C6_rn_excludes'] = dirround(n6, 'n') < n6 < dirround(n6, 'u')
c8 = nets_of(combos['C8'][0])
report['C8_net_fz'] = str(c8[8]); report['C8_needs_bits'] = (c8[8] * 2 ** 60).numerator.bit_length()
report['C8_differs_from_fl'] = c8[8] != F(0.1 * 3)
print(json.dumps(report, indent=1))
