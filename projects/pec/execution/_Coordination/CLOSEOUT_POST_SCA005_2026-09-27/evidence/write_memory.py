import hashlib, pathlib, sys
repo = pathlib.Path(sys.argv[1])
ex = repo / "projects/pec/execution"
tmpl = (repo / "docs/templates/MEMORY_TEMPLATE.md").read_bytes()
assert hashlib.sha256(tmpl).hexdigest() == "5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a"
tmpl = tmpl.decode()
D = "2026-09-27"
RUN = "HELP-HUMAN-PEC-20260925-POST-SCA005"
REC = "[central receipt](../../../_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/RECEIPT.md)"
RUL = {
 "96": "D-PEC-96_RULING_2026-09-26.md", "98": "D-PEC-98_RULING_2026-09-26.md",
 "100": "D-PEC-100_RULING_2026-09-26.md", "102": "D-PEC-102_RULING_2026-09-26.md",
 "103": "D-PEC-103_RULING_2026-09-26.md", "104": "D-PEC-104_RULING_2026-09-27.md",
 "105": "D-PEC-105_RULING_2026-09-27.md", "106": "D-PEC-106_RULING_2026-09-27.md"}
PR = {"96": 950, "98": 958, "100": 979, "102": 998, "103": 992, "104": 1010, "105": 1007, "106": 1008}
WORK = {
 "98": "First Scope of Work contract written under D-PEC-98 (graph node S3).",
 "100": "Scope of Work rebuilt under D-PEC-100 (graph node S2).",
 "103": "First Scope of Work contract written under D-PEC-103 (graph node K2).",
 "102": "Scope of Work brought current under D-PEC-102 (graph node S4).",
 "104": "Scope of Work brought current under D-PEC-104 (graph node S1).",
 "105": "Premise-only amendment under D-PEC-105 (graph node D1).",
 "106": "P1 fixture suites committed under D-PEC-106 (graph node X1).",
}
def rlink(k): return f"[D-PEC-{k} ruling](../../../_Coordination/_DECISIONS/{RUL[k]})"
def row(k): return f"| {RUN} / {D} | {WORK[k]} | {REC}; PR #{PR[k]}; {rlink(k)} |\n"
# D-PEC-96 row: components from the D-PEC-96 proposal (run ID, date, text, PR, central receipt); no byte-exact row is tabled
row96 = f"| {RUN} / {D} | Schema version 2 source act under D-PEC-96 (graph node G1). | {REC}; PR #{PR['96']} |\n"
def folder(did):
    m = sorted(ex.glob(f"PKG-*/1_Working/{did}_*"))
    assert len(m) == 1, did
    return m[0]
plan = {}  # did -> list of packet keys in order (created files)
for d in ["DEL-02-08","DEL-02-09"]: plan[d] = ["98","106"]
for d in ["DEL-01-01","DEL-02-04","DEL-02-05","DEL-02-06","DEL-02-07"]: plan[d] = ["100"]
plan["DEL-02-03"] = ["100","106"]
for d in ["DEL-08-06","DEL-10-13"]: plan[d] = ["103"]
for d in ["DEL-04-01","DEL-04-02","DEL-04-03","DEL-08-01","DEL-08-03","DEL-08-04","DEL-03-04","DEL-10-03"]: plan[d] = ["102"]
for d in ["DEL-01-04","DEL-01-05","DEL-02-01","DEL-02-02","DEL-03-01","DEL-03-02","DEL-03-03","DEL-03-06","DEL-04-05","DEL-10-02","DEL-10-10"]: plan[d] = ["104"]
for d in ["DEL-00-01","DEL-00-03"]: plan[d] = ["105"]
assert len(plan) == 31
out = []
for did, keys in plan.items():
    p = folder(did) / "MEMORY.md"
    assert not p.exists(), p
    body = tmpl.replace("{{DEL-ID}}", did) + "".join(row(k) for k in keys)
    p.write_text(body, encoding="utf-8", newline="\n")
    out.append(p)
# DEL-01-06: append D-PEC-96 row then D-PEC-100 row
p = folder("DEL-01-06") / "MEMORY.md"
b = p.read_bytes(); assert hashlib.sha256(b).hexdigest() == "035ecb8686d72b18eb680531e1239ab4b2df4f5ae1b70811f6e4d667ccf30a3f"
p.write_bytes(b + (row96 + row("100")).encode()); out.append(p)
# DEL-01-03: append dated section
p = folder("DEL-01-03") / "MEMORY.md"
b = p.read_bytes(); assert hashlib.sha256(b).hexdigest() == "44b360c57b934c585befe2cf6a0741199d4cc4ac6b8fc64c04f7be33b88bdae6"
assert b.endswith(b"\n")
sec = f"\n## {D} — D-PEC-104 S1 Scope of Work currency (graph node S1)\n\n{REC}; PR #{PR['104']}; {rlink('104')}\n"
p.write_bytes(b + sec.encode()); out.append(p)
for p in out:
    print(hashlib.sha256(p.read_bytes()).hexdigest(), p.relative_to(repo))
