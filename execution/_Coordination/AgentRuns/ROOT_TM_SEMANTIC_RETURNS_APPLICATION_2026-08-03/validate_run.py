#!/usr/bin/env python3
"""Validate the Root Task Management semantic-return register echoes."""

from __future__ import annotations

import csv
import hashlib
import io
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
LIVE_REL = "execution/_Coordination/_TaskManagement/REGISTER.csv"
ARCHIVE_REL = "execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv"
AUTHORITY_REL = (
    "execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/"
    "OWNER_RETURN_TRANSCRIPT_2026-08-03.txt"
)
AUTHORITY_SHA = (
    "6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows_from_text(text: str) -> dict[str, dict[str, str]]:
    return {row["ActionItemID"]: row for row in csv.DictReader(io.StringIO(text))}


def rows_from_path(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["ActionItemID"]: row for row in csv.DictReader(handle)}


def git_text(rel: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"HEAD:{rel}"], cwd=REPO, text=True
    )


def exact_notes_only(
    before: dict[str, dict[str, str]],
    after: dict[str, dict[str, str]],
    targets: set[str],
) -> None:
    assert set(after) == set(before)
    observed: set[str] = set()
    for action_id, row in after.items():
        changed = {key for key in row if row[key] != before[action_id][key]}
        if changed:
            assert changed == {"Notes"}, (action_id, changed)
            observed.add(action_id)
    assert observed == targets, observed


def main() -> None:
    assert sha(REPO / AUTHORITY_REL) == AUTHORITY_SHA

    live_before = rows_from_text(git_text(LIVE_REL))
    live_after = rows_from_path(REPO / LIVE_REL)
    archive_before = rows_from_text(git_text(ARCHIVE_REL))
    archive_after = rows_from_path(REPO / ARCHIVE_REL)
    exact_notes_only(live_before, live_after, {"TM-ROOT-111", "TM-ROOT-112"})
    exact_notes_only(archive_before, archive_after, {"TM-ROOT-109"})

    statuses = {"OPEN": 0, "DEFERRED": 0, "ELEVATED": 0, "CLOSED": 0}
    for row in live_after.values():
        statuses[row["Status"]] += 1
    assert statuses == {"OPEN": 13, "DEFERRED": 11, "ELEVATED": 0, "CLOSED": 0}
    assert len(archive_after) == 98

    tm111 = live_after["TM-ROOT-111"]
    for phrase in (
        "priority evidence only",
        "30876341235 / job 91888465477",
        "2b6d53027ea10374dd515a4a5a203f8ed4cf2f04",
        "30877532946 / job 91891904563 passed",
        "hosted CI remains authoritative",
    ):
        assert phrase in tm111["Notes"], phrase
    assert tm111["Status"] == live_before["TM-ROOT-111"]["Status"] == "OPEN"
    assert tm111["Priority"] == live_before["TM-ROOT-111"]["Priority"]

    tm112 = live_after["TM-ROOT-112"]
    for phrase in (
        "accepted candidate clauses N-STOP-1 through N-STOP-7",
        "G2 + C1 + F1",
        "exact 2000 ms grace",
        "selected 2500 ms total connection bound",
        "row remains OPEN",
        "App notice remains conditional on an accepted repair landing",
    ):
        assert phrase in tm112["Notes"], phrase
    assert tm112["Status"] == "OPEN"

    tm109 = archive_after["TM-ROOT-109"]
    for phrase in (
        "2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489",
        "design semantics only",
        "Recorded non-selections remain blockers",
        "no contract bytes ruled at closure",
        "remains App-local",
    ):
        assert phrase in tm109["Notes"], phrase
    assert tm109["Status"] == "CLOSED"
    assert tm109["Disposition"] == "RESOLVED_BY_DECISION"
    assert tm109["EvidenceRef"] == archive_before["TM-ROOT-109"]["EvidenceRef"]
    assert tm109["EvidenceSha"] == archive_before["TM-ROOT-109"]["EvidenceSha"]

    for foreign_rel in (
        "projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv",
        "projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv",
        "_DomainEngines/pec/_TaskManagement/REGISTER.csv",
    ):
        assert (REPO / foreign_rel).read_text(encoding="utf-8") == git_text(foreign_rel)

    subprocess.run(["git", "diff", "--check"], cwd=REPO, check=True)
    print("ROOT_TM_SEMANTIC_RETURNS_APPLICATION validation PASS")
    print("changed Notes only: TM-ROOT-111, TM-ROOT-112, TM-ROOT-109")
    print("live: OPEN=13 DEFERRED=11 ELEVATED=0 CLOSED=0; archive=98")
    print(f"live_sha256={sha(REPO / LIVE_REL)}")
    print(f"archive_sha256={sha(REPO / ARCHIVE_REL)}")


if __name__ == "__main__":
    main()
