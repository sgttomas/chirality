#!/usr/bin/env python3
"""Validate the exact SCA-APP-008 Gate-3 transaction blocks in memory."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[8]
PACKAGE = REPO / "projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Gate3/GATE3_AMENDMENT_PACKAGE.md"
DECOMP = REPO / "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
CONTRACT = REPO / "projects/chirality-app-dev/docs/CONTRACT.md"

EXPECTED = {
    "decomposition_pre": "dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83",
    "contract_pre": "6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section(text: str, transaction: str) -> str:
    start_marker = f"## Transaction {transaction} —"
    start = text.index(start_marker)
    next_marker = text.find("\n## Transaction ", start + len(start_marker))
    if next_marker < 0:
        next_marker = text.find("\n## D-APP-103", start + len(start_marker))
    if next_marker < 0:
        next_marker = len(text)
    return text[start:next_marker]


def block(section_text: str, label: str) -> str:
    marker = f"### {label}\n\n```text\n"
    start = section_text.index(marker) + len(marker)
    end = section_text.index("\n```", start)
    return section_text[start:end] + "\n"


def replace_once(image: str, before: str, after: str, label: str) -> str:
    count = image.count(before)
    if count != 1:
        raise SystemExit(f"{label}: expected one pre-image, found {count}")
    return image.replace(before, after, 1)


def insert_after_once(image: str, anchor: str, insertion: str, label: str) -> str:
    count = image.count(anchor)
    if count != 1:
        raise SystemExit(f"{label}: expected one anchor, found {count}")
    return image.replace(anchor, anchor + insertion, 1)


package = PACKAGE.read_text(encoding="utf-8")
decomp_bytes = DECOMP.read_bytes()
contract_bytes = CONTRACT.read_bytes()

if sha(decomp_bytes) != EXPECTED["decomposition_pre"]:
    raise SystemExit("decomposition pre-image SHA mismatch")
if sha(contract_bytes) != EXPECTED["contract_pre"]:
    raise SystemExit("contract pre-image SHA mismatch")

decomp = decomp_bytes.decode("utf-8")
contract = contract_bytes.decode("utf-8")

for tx in ("D-01", "D-02", "D-03", "D-04"):
    tx_section = section(package, tx)
    decomp = replace_once(
        decomp,
        block(tx_section, "PRE-IMAGE"),
        block(tx_section, "POST-IMAGE"),
        tx,
    )

d05 = section(package, "D-05")
decomp = insert_after_once(
    decomp,
    block(d05, "DECISION PRE-IMAGE ANCHOR"),
    block(d05, "DECISION POST-IMAGE INSERTION"),
    "D-05 decision",
)
decomp = insert_after_once(
    decomp,
    block(d05, "CHANGE-LOG PRE-IMAGE ANCHOR"),
    block(d05, "CHANGE-LOG POST-IMAGE INSERTION"),
    "D-05 change log",
)

for tx in ("C-01", "C-02", "C-03", "C-04", "C-05", "C-06", "C-07"):
    tx_section = section(package, tx)
    contract = replace_once(
        contract,
        block(tx_section, "PRE-IMAGE"),
        block(tx_section, "POST-IMAGE"),
        tx,
    )

c08 = section(package, "C-08")
contract = insert_after_once(
    contract,
    block(c08, "APPLICATION ANCHOR AFTER C-04"),
    block(c08, "POST-IMAGE INSERTION"),
    "C-08",
)

for tx in ("C-09", "C-10", "C-11"):
    tx_section = section(package, tx)
    contract = insert_after_once(
        contract,
        block(tx_section, "PRE-IMAGE ANCHOR"),
        block(tx_section, "POST-IMAGE INSERTION"),
        tx,
    )

original_deliverables = set(re.findall(r"^\| (DEL-\d{2}-\d{2}) \|", decomp_bytes.decode("utf-8"), re.MULTILINE))
candidate_deliverables = set(re.findall(r"^\| (DEL-\d{2}-\d{2}) \|", decomp, re.MULTILINE))
original_packages = set(re.findall(r"^\| (PKG-\d{2}) \|", decomp_bytes.decode("utf-8"), re.MULTILINE))
candidate_packages = set(re.findall(r"^\| (PKG-\d{2}) \|", decomp, re.MULTILINE))

if original_deliverables != candidate_deliverables or len(candidate_deliverables) != 51:
    raise SystemExit("deliverable topology changed")
if original_packages != candidate_packages or len(candidate_packages) != 10:
    raise SystemExit("package topology changed")

required_contract_ids = {
    "K-CONTROL-1",
    "K-ROLE-2",
    "K-NET-1",
    "K-KEY-1",
    "K-EVENT-3",
    "K-EVENT-4",
    "K-EVENT-6",
    "K-CONSENT-1",
    "K-UNTYPED-1",
}
for invariant_id in required_contract_ids:
    count = len(re.findall(rf"^\| \*\*{re.escape(invariant_id)}\*\* \|", contract, re.MULTILINE))
    if count != 1:
        raise SystemExit(f"candidate contract {invariant_id} count is {count}, expected 1")

if "What is the exact live Root session path, including its accepted schema/version identity?" not in contract:
    raise SystemExit("K-EVENT-4 open question missing")

result = {
    "verdict": "PASS",
    "decompositionPreSHA256": EXPECTED["decomposition_pre"],
    "decompositionPostSHA256": sha(decomp.encode("utf-8")),
    "contractPreSHA256": EXPECTED["contract_pre"],
    "contractPostSHA256": sha(contract.encode("utf-8")),
    "packageCount": len(candidate_packages),
    "deliverableCount": len(candidate_deliverables),
    "requiredContractCandidateCount": len(required_contract_ids),
    "kEvent4QuestionUnresolved": True,
}
print(json.dumps(result, indent=2, sort_keys=True))
