"""I101 repair 01: RV120's four forgeries (forge_eg_inputs.jsonl) as edit lists on my exact bases (the 07e computed hashes
excluded; the test's own 07e rehash recomputes them), written as RS and TS literals. Every value is a string except the
evidence G_pa, given by its binary64 bits. Usage: gen_forgeries.py <forge inputs> <rs inputs dump> <out dir>"""
import json, struct, sys
F = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
B = {d["base"]: d for d in map(json.loads, open(sys.argv[2])) if d["name"] == "base"}
out = sys.argv[3]
HASHES = [("retained_precision", "receipt_sha256"), ("retained_precision", "body", "publication_sha256"), ("retained_precision", "body", "invocation", "value")]
def computed(p):
    p = tuple(p)
    return p in HASHES or (p[:3] == ("retained_precision", "body", "sources") and p[4:] == ("preparation", "sha256")) \
        or (p[:3] == ("retained_precision", "body", "cases") and p[4:] == ("source_identity_sha256",))
def diff(a, b, path=()):
    if computed(path): return []
    if type(a) is dict and type(b) is dict:
        assert set(a) == set(b), path
        return [e for k in b for e in diff(a[k], b[k], path + (k,))]
    if type(a) is list and type(b) is list:
        assert len(a) == len(b), path
        return [e for i, (x, y) in enumerate(zip(a, b)) for e in diff(x, y, path + (i,))]
    same = json.dumps(a) == json.dumps(b) and type(a) is type(b)
    return [] if same else [(list(path), b)]
rows = []
for f in F:
    base = f["name"].split("[")[1].rstrip("]")
    which = "E" if f["name"].startswith("forge E") else "G"
    assert f["invocation"] == B[base]["invocation"]
    rows.append({"which": which, "base": base, "edits": diff(B[base]["source"], f["source"])})
json.dump(rows, open(f"{out}/forgeries.json", "w"), indent=1)
def rs_value(v):
    if isinstance(v, str): return f'json!("{v}")'
    assert isinstance(v, float)
    return f"json!(f64::from_bits(0x{struct.unpack('>Q', struct.pack('>d', v))[0]:016x}))"
def ts_value(v):
    if isinstance(v, str): return f"'{v}'"
    return f"decodeBinary64('{struct.unpack('>Q', struct.pack('>d', v))[0]:016x}')"
def rs_path(p): return "json!([" + ", ".join(f'"{x}"' if isinstance(x, str) else str(x) for x in p) + "])"
def ts_path(p): return "[" + ", ".join(f"'{x}'" if isinstance(x, str) else str(x) for x in p) + "]"
rs, ts = [], []
for r in rows:
    label = f"RV120 F2: {'E' if r['which'] == 'E' else 'G-hat'} +1 ulp in every receipt copy, stiffness and native hashes resealed"
    rs.append(f'        ("{label}", "{r["base"]}", vec![\n' + "".join(f"            set({rs_path(p)}, {rs_value(v)}),\n" for p, v in r["edits"]) + "        ]),")
    ts.append(f"    [\"{label}\", '{r['base']}', [\n" + "".join(f"      set({ts_path(p)}, {ts_value(v)}),\n" for p, v in r["edits"]) + "    ]],")
open(f"{out}/rs_rows.txt", "w").write("\n".join(rs) + "\n")
open(f"{out}/ts_rows.txt", "w").write("\n".join(ts) + "\n")
print([(r["which"], r["base"], len(r["edits"])) for r in rows])
