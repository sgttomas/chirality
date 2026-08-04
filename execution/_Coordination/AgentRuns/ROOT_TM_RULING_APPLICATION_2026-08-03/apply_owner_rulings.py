#!/usr/bin/env python3
"""Apply the exact owner-ruled Root Task Management row dispositions.

This is a deterministic, run-contained row-maintenance helper. It refuses
unless the three target rows are live OPEN rows and TM-ROOT-112 remains live
OPEN. Mechanical archiving is performed separately by taskmgmt.py.
"""

from __future__ import annotations

import csv
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
REGISTER = REPO / "execution/_Coordination/_TaskManagement/REGISTER.csv"
RULING_REF = (
    "execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/"
    "OWNER_RULING_TRANSCRIPT_2026-08-03.md"
)
RULING_SHA = "66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06"
DATE = "2026-08-03"


UPDATES = {
    "TM-ROOT-105": {
        "EvidenceQuote": (
            "TM105-A — AUTHORIZE EXACT GENERIC CONTRACT-CANDIDATE "
            "PREPARATION ONLY"
        ),
        "NotesAppend": (
            "2026-08-03 owner ruling TM105-A: CLOSED "
            "RESOLVED_BY_DECISION. The ruling is preparation-posture only; "
            "no contract bytes were ruled; later semantic acceptance and "
            "implementation gates remain. App TM-APP-027/028 sharpened "
            "triggers require closure WITH a ruled contract and therefore "
            "are not satisfied by this closure; their routing re-assessment "
            "remains for App's next deferral review. Separate active governed "
            "carrier launched by HELP_HUMAN: "
            "ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03; no candidate "
            "completion or acceptance is claimed here."
        ),
    },
    "TM-ROOT-109": {
        "EvidenceQuote": (
            "TM109-A — AUTHORIZE GENERIC IDENTITY/PROVENANCE ENVELOPE "
            "PREPARATION ONLY"
        ),
        "NotesAppend": (
            "2026-08-03 owner ruling TM109-A: CLOSED "
            "RESOLVED_BY_DECISION. The ruling is preparation-posture only; "
            "no contract bytes were ruled; later semantic acceptance and "
            "implementation gates remain. App TM-APP-027/028 sharpened "
            "triggers require closure WITH a ruled contract and therefore "
            "are not satisfied by this closure; their routing re-assessment "
            "remains for App's next deferral review. Consumer equality, "
            "mapping, normalization, tolerances, and engineering meaning "
            "remain local; no cross-consumer compatibility claim is made. "
            "Separate active governed carrier launched by HELP_HUMAN: "
            "ROOT_TM109_COMPARISON_BASIS_CANDIDATE_2026-08-03; no candidate "
            "completion or acceptance is claimed here."
        ),
    },
    "TM-ROOT-121": {
        "EvidenceQuote": (
            "DECIDE DEL-02-06 OWNER-SELECTION "
            "623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d "
            "D1-A D2-A D3-A D4-A D5-B D6-A D7-A D8-A D9-A TBD-001-A "
            "TBD-002-A TBD-003-A TBD-004-A TBD-005-A TBD-006-A TBD-007-A "
            "TBD-008-A TBD-009-A TBD-010-A TBD-011-A TBD-012-A TBD-013-A "
            "TBD-014-A TBD-015-A TBD-016-A CENSUS-A COMPAT-DELTA-A"
        ),
        "NotesAppend": (
            "2026-08-03 owner selection: CLOSED RESOLVED_BY_DECISION. The "
            "exact 27-option tuple bound to derivative identity "
            "623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d "
            "releases only separate semantic-candidate authoring and fresh "
            "refutation; no semantic bytes or implementation are accepted. "
            "Separate active governed carrier launched by HELP_HUMAN: "
            "ROOT_DEL0206_SEMANTIC_CANDIDATE_2026-08-03; no candidate "
            "completion or acceptance is claimed here."
        ),
    },
}


def main() -> None:
    with REGISTER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert fieldnames is not None
    by_id = {row["ActionItemID"]: row for row in rows}
    assert set(UPDATES).issubset(by_id)
    assert by_id["TM-ROOT-112"]["Status"] == "OPEN"
    assert by_id["TM-ROOT-112"]["Disposition"] == ""

    for action_id, update in UPDATES.items():
        row = by_id[action_id]
        assert row["Status"] == "OPEN", (action_id, row["Status"])
        assert row["Disposition"] == "", (action_id, row["Disposition"])
        assert row["EvidenceRef"] == "", (action_id, row["EvidenceRef"])
        assert row["EvidenceSha"] == "", (action_id, row["EvidenceSha"])
        assert row["Closed"] == "", (action_id, row["Closed"])
        row["Status"] = "CLOSED"
        row["Disposition"] = "RESOLVED_BY_DECISION"
        row["EvidenceRef"] = RULING_REF
        row["EvidenceSha"] = RULING_SHA
        row["EvidenceQuote"] = update["EvidenceQuote"]
        row["LastReviewed"] = DATE
        row["Closed"] = DATE
        row["Notes"] = f'{row["Notes"]} | {update["NotesAppend"]}'

    with REGISTER.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()

