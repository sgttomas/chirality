#!/usr/bin/env python3
"""B6 Lane A4 steps 1-3: projects/pec/AGENTS.md from the accepted candidate.

1. Start from CP2_CANDIDATE/AGENTS.candidate.md (49ce993a...070d).
2. Fill its application-date slot (front-matter `amended:` first token) with
   the application date; the group-2 folder token (L209) keeps its act-date
   value SCA-006_GROUP-2_2026-09-25.
3. Amendment 1: replace exactly candidate L261-270 with the drafted paragraph.
4. Assert the verification rule: the result equals the slot-filled candidate
   everywhere except that one hunk (line-level), then write over the live file.
Usage: apply_a4_agents.py [--dry-run]
"""
import hashlib, pathlib, sys, difflib, json
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
P = R / "projects/pec"
C = P / "execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate.md"
APP = "2026-09-26"
DRY = "--dry-run" in sys.argv
def sha(b): return hashlib.sha256(b).hexdigest()
def need(label, got, exp):
    if got != exp: sys.exit(f"ABORT {label}: {got} != {exp}")

live = (P / "AGENTS.md").read_bytes()
need("live preimage", sha(live), "c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a")
cand = C.read_bytes()
need("candidate", sha(cand), "49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d")
L = cand.decode("utf-8").split("\n")

# slot 1: amended: date (application-date slot, first token only)
old6 = "amended: 2026-09-25 (SCA-006 operational-reliance instruction tranche; earlier, shared development-loop adoption under D-PEC-94)"
need("L6", L[5], old6)
L[5] = old6.replace("amended: 2026-09-25 ", f"amended: {APP} ", 1)
# slot 2: group-2 folder token keeps the act-date value
assert "SCA-006_GROUP-2_2026-09-25" in L[208], L[208]
slot_filled = "\n".join(L)
slot_filled_sha = sha(slot_filled.encode())

BEFORE = L[260:270]
assert BEFORE[0].startswith("PEC's deliverable `_STATUS.md` `## Remaining` sections stay in place as"), BEFORE[0]
assert BEFORE[-1] == "as App and Piping did, is a separate owner-directed undertaking.", BEFORE[-1]
assert L[259] == "" and L[270] == "", (L[259], L[270])

AFTER = """PEC adds no new deliverable `_STATUS.md` `## Remaining` sections or entries
(owner direction of 2026-09-26, recorded as SCA-006 checkpoint group 2
amendment 1). No PEC feed profile reads them, so the coordination plane does
not scan them, and they are not a work-selection surface. Steering selects the
undertaking; record new open scope in its work graph and governing records.
Until any retirement ruling, the existing sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). A Remaining item's own gate markers still bind that item.
Update an item only under the packet that opens that `_STATUS.md`. If an
undertaking completes or affects an item without such a grant, record the
consequence in the graph and bring it to the owner. Retiring the sections, as
App and Piping did, is a separate owner-directed undertaking.""".split("\n")
for i, x in enumerate(AFTER):
    if len(x) > 79 or x != x.rstrip() or "\t" in x:
        sys.exit(f"ABORT after-line {i+1} format: {x!r}")

N = L[:260] + AFTER + L[270:]
post = "\n".join(N).encode()

# verification rule: slot-filled candidate vs postimage differ only in one hunk at L261-270
sm = difflib.SequenceMatcher(a=L, b=N, autojunk=False)
ops = [op for op in sm.get_opcodes() if op[0] != "equal"]
# difflib may split the replaced paragraph where a line coincides; every
# differing region must lie inside candidate L261-270 (0-based 260..270)
for op in ops:
    if not (op[1] >= 260 and op[2] <= 270): sys.exit(f"ABORT: region outside candidate L261-270: {op}")
tag = "+".join(o[0] for o in ops)
i1, i2 = ops[0][1], ops[-1][2]
j1, j2 = ops[0][3], ops[-1][4]
# the prefix L1-260 and the suffix from candidate L271 are byte-identical
assert N[:260] == L[:260] and N[260 + len(AFTER):] == L[270:]
# reverse proof: put BEFORE back -> slot-filled candidate
rev = N[:260] + BEFORE + N[260 + len(AFTER):]
need("reverse proof", sha("\n".join(rev).encode()), slot_filled_sha)
# and restoring the slot default -> accepted candidate
rev[5] = old6
need("accepted candidate proof", sha("\n".join(rev).encode()), "49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d")

udiff = "\n".join(difflib.unified_diff(L, N, "AGENTS.candidate.md (slot-filled)", "projects/pec/AGENTS.md (applied)", n=0, lineterm=""))
res = {"preimage": sha(live), "candidate": sha(cand), "candidate_slot_filled": slot_filled_sha,
       "postimage": sha(post), "candidate_lines": len(L), "postimage_lines": len(N),
       "hunk_candidate_lines": f"{i1+1}-{i2}", "hunk_postimage_lines": f"{j1+1}-{j2}",
       "opcode": tag, "mode": "dry-run" if DRY else "written"}
if not DRY:
    (P / "AGENTS.md").write_bytes(post)
    need("reread", sha((P / "AGENTS.md").read_bytes()), sha(post))
print(json.dumps(res, indent=1))
print("----- BEFORE (candidate L261-270) -----"); print("\n".join(BEFORE))
print("----- AFTER -----"); print("\n".join(AFTER))
print("----- unified diff (n=0) -----"); print(udiff)
