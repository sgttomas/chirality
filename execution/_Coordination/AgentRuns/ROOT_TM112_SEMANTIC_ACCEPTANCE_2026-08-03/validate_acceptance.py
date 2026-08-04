#!/usr/bin/env python3
"""Validate exact TM112 authority, whitespace equivalence, and brief freeze."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parent
TRANSCRIPT = ROOT / "execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/OWNER_RETURN_TRANSCRIPT_2026-08-03.txt"
CLAUSE_PATH = "execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/CANDIDATE_NORMATIVE_CLAUSES.md"
PRE = "ba4678ca00c0cf9fb862ba36d1410d11ce1ff6ac"
POST = "2b6d53027ea10374dd515a4a5a203f8ed4cf2f04"


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"BLOCK: {message}")


required = [
    "AUTHORITY_BINDING.json",
    "ACCEPTANCE_RECORD.md",
    "IMPLEMENTATION_BRIEF.md",
    "HANDOFF_STATE.md",
    "MANAGER_RETURN.md",
    "RUN_RECORD.md",
    "VALIDATION.md",
    "FORMAT_NORMALIZATION.md",
]
for relative in required:
    if not (RUN / relative).is_file():
        fail(f"missing output: {relative}")

binding = json.loads((RUN / "AUTHORITY_BINDING.json").read_text())
transcript = TRANSCRIPT.read_bytes()
if sha(transcript) != binding["transcript"]["sha256"]:
    fail("transcript hash drift")
start = binding["transcript"]["signedBlockStartByte"]
end = binding["transcript"]["signedBlockEndByteExclusive"]
block = transcript[start:end]
if len(block) != 1843 or sha(block) != binding["transcript"]["signedBlockSha256"]:
    fail("signed TM112 block identity drift")
if not block.startswith(b"DECIDE ROOT-TM112-SEMANTICS-01 G2 C1 F1"):
    fail("signed block selection mismatch")
if not block.endswith(b"BEHAVIOR \xe2\x80\x94 Ryan Tufts 2026-08-03"):
    fail("signed block signature mismatch")

pre = subprocess.check_output(["git", "show", f"{PRE}:{CLAUSE_PATH}"], cwd=ROOT)
post = subprocess.check_output(["git", "show", f"{POST}:{CLAUSE_PATH}"], cwd=ROOT)
current = (ROOT / CLAUSE_PATH).read_bytes()
clause = binding["clauseBytes"]
if sha(pre) != clause["preWhitespaceSha256"] or len(pre) != 7796:
    fail("pre-whitespace clause drift")
if sha(post) != clause["postWhitespaceSha256"] or len(post) != 7792:
    fail("post-whitespace clause drift")
if current != post:
    fail("working clause is not the accepted post-whitespace blob")
changes = [(a, b) for a, b in zip(pre.splitlines(keepends=True), post.splitlines(keepends=True)) if a != b]
if changes != [
    (b"Status: `PROPOSAL \xe2\x80\x94 NON-AUTHORITATIVE UNTIL SIGNED OWNER RETURN`  \n", b"Status: `PROPOSAL \xe2\x80\x94 NON-AUTHORITATIVE UNTIL SIGNED OWNER RETURN`\n"),
    (b"Candidate set: `ROOT-TM112-SEMANTICS-01 / G2 + C1 + F1`  \n", b"Candidate set: `ROOT-TM112-SEMANTICS-01 / G2 + C1 + F1`\n"),
]:
    fail("clause drift exceeds exact Markdown hard-break normalization")
if pre.replace(b"  \n", b"\n") != post or not post.endswith(b"\n"):
    fail("normalized semantic equality or EOF invariant failed")

expected = {
    "docs/SPEC.md": "988c4b90287753d1249f53d01838819028ecb959a8fa1cbecf873e50c0fb62db",
    "runtime/packages/daemon/src/runtime-daemon.ts": "a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46",
    "runtime/tests/daemon.test.ts": "bbcfcabb48dd7c4b5c5e0645b14601efd89404e34a5cdde322a0bef5b22a693e",
    "runtime/package.json": "499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071",
    "runtime/package-lock.json": "4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f",
}
for relative, expected_sha in expected.items():
    preimage = subprocess.check_output(["git", "show", f"{POST}:{relative}"], cwd=ROOT)
    if sha(preimage) != expected_sha:
        fail(f"sealed pre-implementation basis drift: {relative}")

brief = (RUN / "IMPLEMENTATION_BRIEF.md").read_text()
if sha((RUN / "IMPLEMENTATION_BRIEF.md").read_bytes()) != "617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d":
    fail("normalized implementation brief identity drift")
for token in [
    "docs/SPEC.md", "runtime/packages/daemon/src/runtime-daemon.ts",
    "runtime/tests/daemon.test.ts", "2,000", "500", "STOPPED_DEGRADED",
    "STOP_FAILED_CLEANUP", "Pre-identity Agent 1", "Restart/generation",
    "App notice remains unshipped", "Do not implement signal handling"
]:
    if token not in brief:
        fail(f"implementation brief obligation missing: {token}")

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
remote = subprocess.check_output(
    ["git", "rev-parse", "origin/codex/root-owner-rulings-2026-08-03"], cwd=ROOT, text=True
).strip()
if head != POST or remote != POST:
    fail(f"whitespace prerequisite not current/pushed: HEAD={head} remote={remote}")

print("PASS: signed transcript and exact TM112 block identity")
print("PASS: pre/post clause hashes and exact Markdown hard-break normalization")
print("PASS: post-whitespace clause blob current; terminal newline unchanged")
print("PASS: sealed pre-implementation basis hashes valid at the recorded Git preimage")
print("PASS: implementation brief scope, semantics, tests, holds, and claim boundary")
print(f"PASS: prerequisite repair commit current and pushed at {POST}")
current_candidate = {
    p: sha((ROOT / p).read_bytes()) for p in [
        "docs/SPEC.md", "runtime/packages/daemon/src/runtime-daemon.ts", "runtime/tests/daemon.test.ts"
    ]
}
if any(current_candidate[p] != expected[p] for p in current_candidate):
    print("INFO: separate current implementation candidate recognized (not acceptance-validated): " + json.dumps(current_candidate, sort_keys=True))
