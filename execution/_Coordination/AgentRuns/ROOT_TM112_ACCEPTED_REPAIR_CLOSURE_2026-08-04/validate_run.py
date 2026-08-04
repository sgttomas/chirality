#!/usr/bin/env python3
"""Validate exact Root TM-ROOT-112 closure and archive relocation."""

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
    "execution/_Coordination/AgentRuns/"
    "ROOT_TM112_IMPLEMENTATION_ACCEPTANCE_2026-08-04/"
    "OWNER_RETURN_TRANSCRIPT_2026-08-04.txt"
)
MANIFEST_REL = (
    "execution/_Coordination/AgentRuns/"
    "ROOT_TM112_IMPLEMENTATION_ACCEPTANCE_2026-08-04/BASIS_MANIFEST.sha256"
)
AUTHORITY_SHA = (
    "a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046"
)
MANIFEST_SHA = (
    "73ae77fe496731987ea49170fad45a9d1297bc263c5ba1d8050631da58efcea2"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(text: str) -> dict[str, dict[str, str]]:
    return {row["ActionItemID"]: row for row in csv.DictReader(io.StringIO(text))}


def path_rows(rel: str) -> dict[str, dict[str, str]]:
    return rows((REPO / rel).read_text(encoding="utf-8"))


def head_text(rel: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"HEAD:{rel}"], cwd=REPO, text=True
    )


def main() -> None:
    assert sha(REPO / AUTHORITY_REL) == AUTHORITY_SHA
    assert sha(REPO / MANIFEST_REL) == MANIFEST_SHA
    expected_files = {
        "projects/chirality-app-dev/execution/_Coordination/"
        "NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md":
            "4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656",
        "docs/SPEC.md":
            "647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f",
        "runtime/packages/daemon/src/runtime-daemon.ts":
            "224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2",
        "runtime/tests/daemon.test.ts":
            "c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352",
    }
    for rel, expected in expected_files.items():
        assert sha(REPO / rel) == expected, rel

    before_live = rows(head_text(LIVE_REL))
    before_archive = rows(head_text(ARCHIVE_REL))
    after_live = path_rows(LIVE_REL)
    after_archive = path_rows(ARCHIVE_REL)
    assert "TM-ROOT-112" in before_live
    assert "TM-ROOT-112" not in before_archive
    assert set(after_live) == set(before_live) - {"TM-ROOT-112"}
    assert set(after_archive) == set(before_archive) | {"TM-ROOT-112"}
    for action_id, row in after_live.items():
        assert row == before_live[action_id], action_id
    for action_id, row in after_archive.items():
        if action_id != "TM-ROOT-112":
            assert row == before_archive[action_id], action_id

    old = before_live["TM-ROOT-112"]
    closed = after_archive["TM-ROOT-112"]
    changed = {key for key in old if old[key] != closed[key]}
    assert changed == {
        "Status", "Disposition", "EvidenceRef", "EvidenceSha",
        "EvidenceQuote", "LastReviewed", "Closed", "Notes",
    }, changed
    assert closed["Status"] == "CLOSED"
    assert closed["Disposition"] == "RESOLVED_WITH_CHANGE"
    assert closed["EvidenceRef"] == AUTHORITY_REL
    assert closed["EvidenceSha"] == AUTHORITY_SHA
    assert closed["LastReviewed"] == closed["Closed"] == "2026-08-04"
    for phrase in (
        "647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f",
        "224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2",
        "c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352",
        "Node 22.19 execution remains an explicit unexecuted compatibility gap",
        "D-APP-88 and TM-APP-036's mandatory non-blocking parity-rerun rider",
        "no claim of App R2 causality, process/SIGTERM proof, App parity acceptance",
        AUTHORITY_SHA,
    ):
        assert phrase in closed["Notes"], phrase

    status_counts = {key: 0 for key in ("OPEN", "DEFERRED", "ELEVATED", "CLOSED")}
    for row in after_live.values():
        status_counts[row["Status"]] += 1
    assert status_counts == {"OPEN": 12, "DEFERRED": 11, "ELEVATED": 0, "CLOSED": 0}
    assert len(after_archive) == 99

    for foreign_rel in (
        "projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv",
        "projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv",
        "_DomainEngines/pec/_TaskManagement/REGISTER.csv",
    ):
        assert (REPO / foreign_rel).read_text(encoding="utf-8") == head_text(foreign_rel)

    receipts = (REPO / "execution/_Coordination/LOOP_RECEIPTS.md").read_text(
        encoding="utf-8"
    )
    assert receipts.count("### Receipt 96 —") == 1
    assert receipts.rfind("### Receipt 96 —") > receipts.rfind("### Receipt 95 —")
    subprocess.run(["git", "diff", "--check"], cwd=REPO, check=True)
    print("ROOT_TM112_ACCEPTED_REPAIR_CLOSURE validation PASS")
    print("only TM-ROOT-112 closed RESOLVED_WITH_CHANGE and moved to archive")
    print("live: OPEN=12 DEFERRED=11 ELEVATED=0 CLOSED=0; archive=99")
    print(f"live_sha256={sha(REPO / LIVE_REL)}")
    print(f"archive_sha256={sha(REPO / ARCHIVE_REL)}")


if __name__ == "__main__":
    main()
