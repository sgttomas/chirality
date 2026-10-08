"""I104 SQ (B1_SQ item 1): what the published cap-maximal inputs leave below D1's caps. Typed counts from the
request JSON (I86's committed inputs); raw counts as this script defines them (every JSON value counted once;
depth with the root at 0; string bytes over values, key bytes over object keys). Usage: census_inputs.py <files...>"""
import json, sys, os
CAPS = dict(n=32, m=32, g=32, r=192, s=192, l=128, c=3, L=384, materials=4, points=16, text=128, values=16384, depth=16)
def walk(v, d=0):
    st = {"values": 1, "depth": d, "str": 0, "key": 0}
    if isinstance(v, dict):
        for k, x in v.items():
            s = walk(x, d + 1); st["key"] += len(k.encode())
            for f in ("values", "str", "key"): st[f] += s[f]
            st["depth"] = max(st["depth"], s["depth"])
    elif isinstance(v, list):
        for x in v:
            s = walk(x, d + 1)
            for f in ("values", "str", "key"): st[f] += s[f]
            st["depth"] = max(st["depth"], s["depth"])
    elif isinstance(v, str):
        st["str"] = len(v.encode())
    return st
def ids(v, out):
    if isinstance(v, dict):
        for k, x in v.items():
            if isinstance(x, str) and k in ("id", "node", "from", "to", "material", "label"):
                out.append(len(x.encode()))
            ids(x, out)
    elif isinstance(v, list):
        for x in v: ids(x, out)
    return out
rows = {}
for f in sys.argv[1:]:
    raw = json.load(open(f)); m = raw["model"]
    cases = m["load_cases"]
    c = dict(n=len(m["nodes"]), m=len(m["pipe_segments"]), g=len(m["supports"]),
             r=sum(len(s.get("restraints", [])) for s in m["supports"]), s=sum(1 for s in m["supports"] if "stiffness" in s),
             l=max(len(k["primitive_loads"]) for k in cases), c=len(cases), L=sum(len(k["primitive_loads"]) for k in cases),
             materials=max(len(m.get("materials", [])), len(raw.get("materials", []))),
             points=max([len(x.get("temperature_points", [])) for x in m.get("materials", [])] or [0]),
             text=max(ids(raw, [len(m["project"]["id"].encode())])))
    w = walk(raw); c.update(values=w["values"], depth=w["depth"], string_bytes=w["str"], key_bytes=w["key"])
    rows[os.path.basename(f)] = {k: (v, CAPS.get(k)) for k, v in c.items()}
print(json.dumps({"caps": CAPS, "inputs": rows}, indent=1))
