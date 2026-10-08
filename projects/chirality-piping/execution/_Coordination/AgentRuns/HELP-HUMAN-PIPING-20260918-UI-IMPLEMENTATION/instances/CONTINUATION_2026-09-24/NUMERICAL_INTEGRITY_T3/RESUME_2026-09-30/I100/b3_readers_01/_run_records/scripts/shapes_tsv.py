"""I100 B3: one line per shape: id, base, PY's bound, unbound and transport verdicts (gate:code or pass:standing).
Usage: shapes_tsv.py <shapes.json> <py.jsonl> <out.tsv>"""
import json
import sys

shapes = {s["id"]: s for s in json.load(open(sys.argv[1]))["shapes"]}


def v(x):
    return "pass:" + x["ok"]["standing"] if "ok" in x else f'{x["err"]["gate"]}:{x["err"]["code"]}' if "err" in x else "ESCAPE"


with open(sys.argv[3], "w") as f:
    f.write("id\tbase\tdefinition_sha256\tbound\tunbound\ttransport\n")
    for line in map(json.loads, open(sys.argv[2])):
        s = shapes[line["id"]]
        f.write(f'{line["id"]}\t{s["base"]}\t{s["definition_sha256"][:8]}\t{v(line["bound"])}\t{v(line["unbound"])}\t{v(line["transport"])}\n')
print("ok")
