#!/usr/bin/env python3
"""Read-only deterministic checks for the authorized N4 content closeout."""

import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


repo = Path(__file__).resolve().parents[4]
run = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


head = subprocess.check_output(
    ["git", "rev-parse", "HEAD"], cwd=repo, text=True
).strip()
origin = subprocess.check_output(
    ["git", "rev-parse", "origin/main"], cwd=repo, text=True
).strip()
assert head == origin == "88e7590d3664d4f1daf91bed2a8899bda0748b92"
subprocess.run(
    [
        "git",
        "merge-base",
        "--is-ancestor",
        "d7acbbff8d2bdb4913a8e7727f9f8cbc8787d943",
        head,
    ],
    cwd=repo,
    check=True,
)

# Every structured RunID artifact parses.
json_paths = sorted(run.rglob("*.json"))
csv_paths = sorted(run.rglob("*.csv"))
for path in json_paths:
    json.loads(path.read_text(encoding="utf-8"))
for path in csv_paths:
    with path.open(newline="", encoding="utf-8") as handle:
        list(csv.DictReader(handle))

# The immutable N3 basis stays current except for the authorized append to the
# Root receipt ledger. Its accepted pre-N4 receipt identity remains reproducible
# from HEAD, and every other file hash remains exact.
with (run / "N3_BASIS_MANIFEST.csv").open(newline="", encoding="utf-8") as handle:
    basis = list(csv.DictReader(handle))
assert len(basis) == 22
for row in basis:
    if row["path"].startswith("git:") or row["id"] == "ROOT_RECEIPTS":
        continue
    assert sha(repo / row["path"]) == row["sha256"], row["id"]
receipt_row = next(row for row in basis if row["id"] == "ROOT_RECEIPTS")
head_receipts = subprocess.check_output(
    ["git", "show", f"HEAD:{receipt_row['path']}"], cwd=repo
)
assert hashlib.sha256(head_receipts).hexdigest() == receipt_row["sha256"]
assert sha(repo / receipt_row["path"]) != receipt_row["sha256"]

# Root receipt format is legacy prose and has no dedicated contract wrapper;
# check the bounded structural properties N4 depends on directly.
receipt_text = (repo / receipt_row["path"]).read_text(encoding="utf-8")
headings = re.findall(
    r"^### Receipt (\d+) — (\d{4}-\d{2}-\d{2}) — (.+)$",
    receipt_text,
    re.MULTILINE,
)
ids = [int(item[0]) for item in headings]
assert ids[-2:] == [90, 91]
assert ids.count(91) == 1
receipt_91 = receipt_text[receipt_text.rfind("### Receipt 91") :]
assert "**Parent and authority:** Receipt 90" in receipt_91
assert "No owner decision" in receipt_91
assert "TM-PIP-032 remains unfired" in receipt_91

# Direct Root Task Management state and preserved hashes.
tm = repo / "execution/_Coordination/_TaskManagement"
with (tm / "REGISTER.csv").open(newline="", encoding="utf-8") as handle:
    live = list(csv.DictReader(handle))
with (tm / "REGISTER_CLOSED.csv").open(newline="", encoding="utf-8") as handle:
    closed = list(csv.DictReader(handle))
assert Counter(row["Status"] for row in live) == {"OPEN": 16, "DEFERRED": 11}
assert Counter(row["Status"] for row in closed) == {"CLOSED": 95}
assert sha(tm / "REGISTER.csv") == (
    "1b9634934d35de8facc32dcb1881bd61a2559b1b4fa72b6da9cee21a6b06144f"
)
assert sha(tm / "REGISTER_CLOSED.csv") == (
    "3b6e9ff3b89135cab119b8343b6fbfed66655d3d7c4370eeea6a22197c96f775"
)
assert sha(repo / "runtime/packages/daemon/src/runtime-daemon.ts") == (
    "a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46"
)

print(
    "N4_CLOSEOUT_VALIDATION_PASS "
    f"receipt=91 parent=90 json={len(json_paths)} csv={len(csv_paths)} "
    "basis=22 authorized_basis_drift=ROOT_RECEIPTS_ONLY "
    "live=27(open=16,deferred=11) archived=95"
)
