#!/usr/bin/env python3
"""Validate the Root Task Management ruling-application tranche."""

from __future__ import annotations

import csv
import hashlib
import io
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
LIVE_REL = "execution/_Coordination/_TaskManagement/REGISTER.csv"
ARCHIVE_REL = "execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv"
RULING_REL = (
    "execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/"
    "OWNER_RULING_TRANSCRIPT_2026-08-03.md"
)
MAP_REL = (
    "execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/"
    "RULING_APPLICATION_MAP.md"
)
NOTICE_REL = (
    "execution/_Coordination/NOTICE_2026-08-03_"
    "ROOT_TM-ROOT-105_109_SUBSTANTIVE_RULINGS.md"
)
TARGETS = {"TM-ROOT-105", "TM-ROOT-109", "TM-ROOT-121"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows_from_text(text: str) -> dict[str, dict[str, str]]:
    return {
        row["ActionItemID"]: row
        for row in csv.DictReader(io.StringIO(text))
    }


def rows_from_path(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["ActionItemID"]: row for row in csv.DictReader(handle)}


def git_text(rel: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"HEAD:{rel}"], cwd=REPO, text=True
    )


def main() -> None:
    assert sha(REPO / RULING_REL) == (
        "66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06"
    )
    assert sha(REPO / MAP_REL) == (
        "87ccfdbe4cf2fb89adc275b330c958c0810973096c8a6749448f3bb8bbef12a5"
    )

    live_before = rows_from_text(git_text(LIVE_REL))
    archive_before = rows_from_text(git_text(ARCHIVE_REL))
    live_after = rows_from_path(REPO / LIVE_REL)
    archive_after = rows_from_path(REPO / ARCHIVE_REL)

    assert set(live_before) - set(live_after) == TARGETS
    assert set(live_after) == set(live_before) - TARGETS
    assert set(archive_after) - set(archive_before) == TARGETS
    assert set(archive_after) == set(archive_before) | TARGETS
    assert all(live_after[key] == live_before[key] for key in live_after)
    assert all(archive_after[key] == archive_before[key] for key in archive_before)
    assert live_after["TM-ROOT-112"] == live_before["TM-ROOT-112"]

    statuses = {"OPEN": 0, "DEFERRED": 0, "ELEVATED": 0, "CLOSED": 0}
    for row in live_after.values():
        statuses[row["Status"]] += 1
    assert statuses == {"OPEN": 13, "DEFERRED": 11, "ELEVATED": 0, "CLOSED": 0}
    assert len(archive_after) == 98
    assert all(row["Status"] == "CLOSED" for row in archive_after.values())

    common_required = [
        "preparation-posture only",
        "no contract bytes were ruled",
        "later semantic acceptance and implementation gates remain",
        "App TM-APP-027/028 sharpened triggers require closure WITH a ruled contract",
        "are not satisfied by this closure",
        "routing re-assessment remains for App's next deferral review",
    ]
    for action_id in ("TM-ROOT-105", "TM-ROOT-109"):
        row = archive_after[action_id]
        assert row["Status"] == "CLOSED"
        assert row["Disposition"] == "RESOLVED_BY_DECISION"
        assert row["EvidenceRef"] == RULING_REL
        assert row["EvidenceSha"] == sha(REPO / RULING_REL)
        assert row["Closed"] == "2026-08-03"
        for phrase in common_required:
            assert phrase in row["Notes"], (action_id, phrase)

    tm105 = archive_after["TM-ROOT-105"]
    tm109 = archive_after["TM-ROOT-109"]
    tm121 = archive_after["TM-ROOT-121"]
    assert "ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03" in tm105["Notes"]
    assert "ROOT_TM109_COMPARISON_BASIS_CANDIDATE_2026-08-03" in tm109["Notes"]
    assert "no cross-consumer compatibility claim is made" in tm109["Notes"]
    assert tm121["Status"] == "CLOSED"
    assert tm121["Disposition"] == "RESOLVED_BY_DECISION"
    assert tm121["EvidenceRef"] == RULING_REL
    assert tm121["EvidenceSha"] == sha(REPO / RULING_REL)
    assert "623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d" in tm121["EvidenceQuote"]
    assert "releases only separate semantic-candidate authoring and fresh refutation" in tm121["Notes"]
    assert "no semantic bytes or implementation are accepted" in tm121["Notes"]
    assert "ROOT_DEL0206_SEMANTIC_CANDIDATE_2026-08-03" in tm121["Notes"]

    notice = (REPO / NOTICE_REL).read_text(encoding="utf-8")
    for phrase in (
        "TM-PIP-032",
        "deb86275f851bac45d606f03df37c59a286ed8da4f34352e9c98e184f8939a2b",
        "No contract bytes were",
        "cross-consumer compatibility claim",
        "writes no Piping register",
        RULING_REL,
    ):
        assert phrase in notice, phrase

    for foreign_rel in (
        "projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv",
        "projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv",
        "_DomainEngines/pec/_TaskManagement/REGISTER.csv",
    ):
        assert (REPO / foreign_rel).read_text(encoding="utf-8") == git_text(foreign_rel)

    subprocess.run(["git", "diff", "--check"], cwd=REPO, check=True)
    print("ROOT_TM_RULING_APPLICATION validation PASS")
    print("changed rows: TM-ROOT-105, TM-ROOT-109, TM-ROOT-121 only")
    print("TM-ROOT-112: unchanged and OPEN")
    print("live: OPEN=13 DEFERRED=11 ELEVATED=0 CLOSED=0; archive=98")
    print(f"live_sha256={sha(REPO / LIVE_REL)}")
    print(f"archive_sha256={sha(REPO / ARCHIVE_REL)}")
    print(f"notice_sha256={sha(REPO / NOTICE_REL)}")


if __name__ == "__main__":
    main()
