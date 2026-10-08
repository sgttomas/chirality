"""I100 B3 addendum 01: the three readers' bound, unbound and transport readings of each probe, side by side.
Usage: add1_table.py <run dir> <out.tsv>"""
import json
import sys

d = sys.argv[1]
rows = {r: [json.loads(l) for l in open(f"{d}/{r}.jsonl")] for r in ("py", "rs", "ts")}


def v(x):
    return ("pass:eligible" if x["ok"]["numerical_eligible"] else "pass:not_eligible") if "ok" in x else f'{x["err"]["gate"]}:{x["err"]["code"].replace("RETAINED_PRECISION_", "")}' if "err" in x else "ESCAPE:" + str(x)[:60]


with open(sys.argv[2], "w") as f:
    f.write("id\treading\tpy\trs\tts\tagree\n")
    disagree = 0
    for i, p in enumerate(rows["py"]):
        assert rows["rs"][i]["id"] == rows["ts"][i]["id"] == p["id"]
        # Each harness hashes its own serialization of the input, so input_sha256 is per language; the materialized
        # statement is compared through the publication digest of every passing reading instead.
        pubs = {rows[r][i][k]["ok"]["publication_sha256"] for r in ("py", "rs", "ts") for k in ("bound", "unbound", "transport") if "ok" in rows[r][i][k]}
        assert len(pubs) <= 1, p["id"]
        for k in ("bound", "unbound", "transport"):
            vals = [v(rows[r][i][k]) for r in ("py", "rs", "ts")]
            same = len(set(vals)) == 1
            disagree += not same
            f.write(f'{p["id"]}\t{k}\t' + "\t".join(vals) + f'\t{"yes" if same else "NO"}\n')
print(len(rows["py"]), "probes;", disagree, "readings differ")
