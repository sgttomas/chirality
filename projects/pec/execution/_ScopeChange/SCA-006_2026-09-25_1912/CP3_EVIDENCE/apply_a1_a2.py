#!/usr/bin/env python3
"""B6 Lane A1 + A2 application for SCA-006 checkpoint-3 preparation.

A1: decomposition candidate with the two pre-acceptance front-matter lines and
    its application-date slots filled; four register postimages byte for byte;
    PRD v2.4 candidate with S1-S4 and the group-2 token at their 2026-09-25
    act-date values (byte for byte).
A2: the three _CONTEXT.md mirrors, applying the plan's A2 hunks as exact string
    replacements to the live preimages and asserting the planned postimages.
Every preimage and postimage hash is asserted; any mismatch aborts before write.
Usage: apply_a1_a2.py [--dry-run]
"""
import hashlib, pathlib, sys, json
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
P = R / "projects/pec"
E = P / "execution"
D = E / "_Decomposition"
C = E / "_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE"
APP = "2026-09-26"   # application date (local, America/Edmonton)
DRY = "--dry-run" in sys.argv
def sha(b): return hashlib.sha256(b).hexdigest()
def need(label, got, exp):
    if got != exp:
        sys.exit(f"ABORT {label}: {got} != {exp}")
out = {}
writes = []

# ---------- A1.1 decomposition ----------
live = (D / "SOFTWARE_DECOMP.md").read_bytes()
need("decomp preimage", sha(live), "dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660")
cand = (C / "_Decomposition/SOFTWARE_DECOMP.md").read_bytes()
need("decomp candidate", sha(cand), "4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71")
t = cand.decode("utf-8")
L = t.split("\n")
ACC = "accepted: 2026-09-25 (original Gate 7 owner ruling under D-PEC-60; revision 1.6 successor accepted through SCA-006 under the owner's checkpoint-group-3 audited-poststate acceptance)"
need("line5 status", L[4], "status: current_basis")
need("line8 accepted", L[7], ACC)
L[4] = "status: candidate_pending_checkpoint_3"
L[7] = "accepted: not yet accepted — revision 1.6 applied during SCA-006 checkpoint-3 preparation; revision 1.5 (accepted 2026-09-25) remains the accepted basis until the owner's checkpoint-3 acceptance"
pre = "\n".join(L)
need("pre-acceptance variant at slot defaults", sha(pre.encode()), "3ad0de686616f895c5fc63cceccef15dca3cd45ba1ca154d9797c2b9551f8a8b")
# application-date slots (Amendment_Preview.md "Acceptance-bound tokens"):
slots = [
    (6, "date: 2026-09-25", f"date: {APP}"),
    (None, "| Revision | 1.6, 2026-09-25 (SCA-006) |", f"| Revision | 1.6, {APP} (SCA-006) |"),
    (None, "| DL-21 | 2026-09-25 | SCA-006,", f"| DL-21 | {APP} | SCA-006,"),
]
L = pre.split("\n")
slot_log = []
for idx, old, new in slots:
    hits = [i for i, x in enumerate(L) if (x == old if idx is not None else x.startswith(old))]
    if len(hits) != 1: sys.exit(f"ABORT slot {old!r}: {len(hits)} hits")
    i = hits[0]
    if idx is not None and i != idx: sys.exit(f"ABORT slot {old!r} at line {i+1}")
    L[i] = L[i].replace(old, new, 1)
    slot_log.append({"line": i + 1, "default": old, "applied": new})
decomp_post = "\n".join(L).encode()
# reverse proof: substituting the defaults back yields the pre-acceptance variant
back = decomp_post.decode()
for s in slot_log:
    back = back.replace(s["applied"], s["default"], 1)
need("reverse slot proof", sha(back.encode()), "3ad0de686616f895c5fc63cceccef15dca3cd45ba1ca154d9797c2b9551f8a8b")
# and restoring the two accepted lines at defaults yields the accepted candidate
bl = back.split("\n"); bl[4] = "status: current_basis"; bl[7] = ACC
need("accepted-candidate proof", sha("\n".join(bl).encode()), "4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71")
# slot-substituted accepted hash (what the accepted candidate hashes to with the application-date slots filled)
al = decomp_post.decode().split("\n"); al[4] = "status: current_basis"; al[7] = ACC
out["decomp"] = {"preimage": sha(live), "accepted_candidate": sha(cand),
    "pre_acceptance_variant_default": "3ad0de686616f895c5fc63cceccef15dca3cd45ba1ca154d9797c2b9551f8a8b",
    "accepted_candidate_slot_substituted": sha("\n".join(al).encode()),
    "written_postimage": sha(decomp_post), "slots": slot_log}
writes.append((D / "SOFTWARE_DECOMP.md", decomp_post))

# ---------- A1.2 registers ----------
regs = {
 "ScopeLedger.csv": ("83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df", "1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e"),
 "Deliverables.csv": ("b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a", "94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805"),
 "ContextBudgetQA.csv": ("2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df", "93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c"),
 "Companion_Inventory.csv": ("7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8", "1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662"),
}
for n, (pre_h, post_h) in regs.items():
    need(f"{n} preimage", sha((D / n).read_bytes()), pre_h)
    b = (C / "_Decomposition" / n).read_bytes()
    need(f"{n} candidate", sha(b), post_h)
    out[n] = {"preimage": pre_h, "postimage": post_h}
    writes.append((D / n, b))

# ---------- A1.3 PRD ----------
need("PRD preimage", sha((P / "docs/PRD.md").read_bytes()), "fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32")
prd = (C / "docs/PRD.md").read_bytes()
need("PRD candidate", sha(prd), "ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe")
pl = prd.decode().split("\n")
assert pl[5] == "| **Date** | 2026-09-25 |", pl[5]
assert "**Adopted 2026-09-25** by owner acceptance of SCA-006 checkpoint group 2 (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`)" in pl[6]
assert "adopted on 2026-09-25 by owner acceptance of SCA-006 checkpoint group 2" in pl[20], pl[20]
assert (E / "_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md").exists()
out["PRD"] = {"preimage": "fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32",
              "postimage": sha(prd),
              "slots": {"S1": "2026-09-25 (L6)", "S2": "2026-09-25 (L7)", "S3": "SCA-006_GROUP-2_2026-09-25 (L7)", "S4": "2026-09-25 (L21)"}}
writes.append((P / "docs/PRD.md", prd))

# ---------- A2 contexts ----------
PROV_OLD = "then by revision 1.5 (`current_basis`, SCA-005 successor)."
PROV_NEW = "then by revision 1.5 (`current_basis`, SCA-005 successor),\nthen by revision 1.6 (`current_basis`, SCA-006 successor)."
ctx = [
 ("DEL-04-03", E/"PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md",
  "a505c2686af7c6d51fe4d1d8dad25bcadd3a5d9c59372c3f9226d31fed2263da", "b28ada4674662515ed7f975cb59c1ee2c2f9cac3c4bcf0d919ced22af79a7b22",
  [("| CoversScopeItems | SOW-006;SOW-007 |", "| CoversScopeItems | SOW-006;SOW-007;SOW-097 |"),
   ("## Description\n\nPer-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness).",
    "## Description\n\nPer-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness), with the reliance envelope (pin, per-feed coverage and limitations, per-claim trust tier, file-fallback signal)."),
   (PROV_OLD, PROV_NEW)]),
 ("DEL-08-01", E/"PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md",
  "151e1e34330a58467ef0f9aa28a3283b50b84bf5f563b03039f5c6bcd9273985", "74b12e7358a71000b8cd544f2db8a736289e7ca4b1e3f94dbadbf98154292d22",
  [("## Description\n\nLocal-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.",
    "## Description\n\nLocal-only Unix-socket binding with token-scoped access classes (owner, harness, agent, admin; agent is read-only query for tool calls); auth-reuse choice tracked by OI-006."),
   (PROV_OLD, PROV_NEW)]),
 ("DEL-08-03", E/"PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md",
  "4644758f07a93eb203bce19533916fbf4e55d52e867895f2a87a5b99b4aec73d", "95fa815a31a38e59c001dd3596bc47053508cd3ff59c9d3eae67d64ba9d037b5",
  [("| ContextEnvelope | S |", "| ContextEnvelope | M |"),
   ("| CoversScopeItems | SOW-043 |", "| CoversScopeItems | SOW-043;SOW-098 |"),
   ("## Description\n\nMachine-first response envelope carrying citations.",
    "## Description\n\nMachine-first response envelope carrying citations. Responses are bounded by declared size budgets met by pagination or continuation, with any truncation stated."),
   ("## Envelope notes\n\n(none)",
    "## Envelope notes\n\nM under SCA-006: declared response-size budgets met by pagination or continuation, with stated truncation, join the compact citation-bearing format (SOW-043, SOW-098); kept one cohesive format slice"),
   (PROV_OLD, PROV_NEW)]),
]
for name, path, pre_h, post_h, reps in ctx:
    b = path.read_bytes(); need(f"{name} ctx preimage", sha(b), pre_h)
    for sib in ("_MEMORY.md", "MEMORY.md"):
        if (path.parent / sib).exists(): sys.exit(f"ABORT {name}: sibling {sib} present (paired read required)")
    s = b.decode()
    for old, new in reps:
        c = s.count(old)
        if c != 1: sys.exit(f"ABORT {name}: {c} hits for {old[:50]!r}")
        s = s.replace(old, new, 1)
    need(f"{name} ctx postimage", sha(s.encode()), post_h)
    out[name] = {"path": str(path.relative_to(R)), "preimage": pre_h, "postimage": post_h, "hunks": len(reps)}
    writes.append((path, s.encode()))

if not DRY:
    for p, b in writes:
        p.write_bytes(b)
    for p, b in writes:
        need(f"reread {p.name}", sha(p.read_bytes()), sha(b))
out["mode"] = "dry-run" if DRY else "written"
out["files"] = len(writes)
print(json.dumps(out, indent=1))
