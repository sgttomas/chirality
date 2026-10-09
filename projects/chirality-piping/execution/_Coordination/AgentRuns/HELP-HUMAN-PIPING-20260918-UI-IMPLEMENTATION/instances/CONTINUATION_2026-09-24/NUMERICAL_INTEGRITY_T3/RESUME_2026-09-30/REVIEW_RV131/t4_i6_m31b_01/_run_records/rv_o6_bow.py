"""RV131 O6: for each curved member in kd5_models.rs (code basis) and rv5_models.rs.txt, the side and plane of the
committed y_reference against the arc the committed centre describes; and T4-I6's regenerated y (JSON).
usage: python -I rv_o6_bow.py KD5_MODELS RV5_MODELS U1_JSON"""
import sys, re, ast, json
from decimal import Decimal as D, getcontext
getcontext().prec = 50
MEM = re.compile(r"MemberData \{ i: (\d+), j: (\d+), y_reference: (\[[^\]]*\]), bend: (None|Some\(\((\[[^\]]*\]), ([^)]*)\)\)) \}")
def models(path):
    out = {}
    for name, body in re.findall(r"pub\(super\) const (\w+): ModelData = ModelData \{(.*?)\n\};", open(path).read(), re.S):
        nodes = ast.literal_eval(re.search(r"nodes: &(\[.*?\]\]),", body).group(1))
        mems = [(int(m.group(1)), int(m.group(2)), ast.literal_eval(m.group(3)), ast.literal_eval(m.group(5)) if m.group(4) != "None" else None) for m in MEM.finditer(body)]
        out[name] = (nodes, mems)
    return out
def sub(a, b): return [a[k] - b[k] for k in range(3)]
def dot(a, b): return sum(a[k] * b[k] for k in range(3))
def nrm(a): return dot(a, a).sqrt()
def perp(v, dh): t = dot(v, dh); return [v[k] - t * dh[k] for k in range(3)]
regen = {}
for m in json.load(open(sys.argv[3]))["t3_models"]:
    for r in m.get("regenerated_bend_inputs", []):
        regen[(m["model"], tuple(r["member"]))] = r["y_reference"]
for path in sys.argv[1:3]:
    for name, (nodes, mems) in models(path).items():
        for (i, j, y, c) in mems:
            if c is None:
                continue
            xi, xj, cc = ([D(v) for v in nodes[i]], [D(v) for v in nodes[j]], [D(v) for v in c])
            d = sub(xj, xi); dh = [v / nrm(d) for v in d]
            bow = sub([(xi[k] + xj[k]) / 2 for k in range(3)], cc)
            bp = perp(bow, dh)
            yp = perp([D(v) for v in y], dh)
            cosang = dot(yp, bp) / (nrm(yp) * nrm(bp))
            ry = regen.get((name, (i, j)))
            rc = None
            if ry is not None:
                ryp = perp([D(v) for v in ry], dh)
                rc = dot(ryp, bp) / (nrm(ryp) * nrm(bp))
            print("%-26s member %d-%d  committed y %-52s cos(y_perp, bow) %+.6f  %s | T4-I6 regenerated y cos %s" % (
                name, i, j, str(y), float(cosang), "OK (same plane, same side)" if cosang > 1 - D("1e-12") else ("OPPOSITE SIDE" if cosang < -1 + D("1e-12") else "DIFFERENT PLANE"),
                "-" if rc is None else "%+.15f" % float(rc)))
