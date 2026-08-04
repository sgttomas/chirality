#!/usr/bin/env python3
"""Apply the exact owner-directed Root Task Management Notes echoes."""

from __future__ import annotations

import csv
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
LIVE = REPO / "execution/_Coordination/_TaskManagement/REGISTER.csv"
ARCHIVE = REPO / "execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv"
AUTHORITY_REF = (
    "execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/"
    "OWNER_RETURN_TRANSCRIPT_2026-08-03.txt"
)
AUTHORITY_SHA = (
    "6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566"
)


LIVE_APPENDS = {
    "TM-ROOT-111": (
        "2026-08-03 owner-directed priority evidence only (no priority, "
        "status, owner, or disposition change): PR #510 failed the hosted "
        "candidate-whitespace gate at run 30876341235 / job 91888465477. "
        "The cosmetic whitespace findings and the two carried candidate_v2 "
        "prose-link repairs landed in commit "
        "2b6d53027ea10374dd515a4a5a203f8ed4cf2f04; rerun 30877532946 / "
        "job 91891904563 passed. This avoidable pre-push cheap-guard miss is "
        "exactly this row's subject and is recorded as priority evidence; "
        "hosted CI remains authoritative. Owner direction: "
        f"{AUTHORITY_REF} SHA-256 {AUTHORITY_SHA}."
    ),
    "TM-ROOT-112": (
        "2026-08-03 later semantic-acceptance echo: accountable human "
        "accepted candidate clauses N-STOP-1 through N-STOP-7 as the "
        "authoritative semantic basis for the already-authorized bounded "
        "implementation/test tranche, selecting G2 + C1 + F1: exact 2000 ms "
        "grace; immediate idempotent canonical interruption of active runtime "
        "SSE after admission closes; the pre-identity Agent-1 latch expires "
        "at force with identity-unavailable failure and no late interrupt; "
        "at grace expiry closeAllConnections follows close and every tracked "
        "residual server socket is destroyed; a product-policy 500 ms "
        "post-force settlement cap yields the selected 2500 ms total "
        "connection bound; cleanup, stop/restart concurrency, degraded/fail-"
        "closed states, and generation isolation follow the signed return. "
        "The row remains OPEN for the bounded repair, tests, and evidence. "
        "The App notice remains conditional on an accepted repair landing; "
        "no App R2 causality, process/SIGTERM behavior, foreign trigger, or "
        "App disposition is inferred. Owner ruling: "
        f"{AUTHORITY_REF} SHA-256 {AUTHORITY_SHA}."
    ),
}

ARCHIVE_APPENDS = {
    "TM-ROOT-109": (
        "2026-08-03 later contract-design semantic acceptance: accountable "
        "human accepted exact candidate package "
        "2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489 "
        "and each recorded candidate choice as identity/provenance-envelope "
        "design semantics only. Recorded non-selections remain blockers. The "
        "envelope records identity and provenance but performs and authorizes "
        "no equality, mapping, normalization, tolerance evaluation, semantic "
        "comparison, conformance, or compatibility; unit-system and "
        "tolerance-profile references remain opaque; consumer-local solver/"
        "rule, engineering, privacy, professional, and human-review meanings "
        "remain local. No implementation, affected-client acceptance, "
        "lifecycle, release, publication, or reliance is authorized. This "
        "later byte acceptance does not rewrite the historical closure basis: "
        "TM-ROOT-109 closed on the earlier preparation-only ruling, with no "
        "contract bytes ruled at closure. Whether any foreign App trigger "
        "fires on the later acceptance remains App-local; none is inferred or "
        "disposed here. Owner acceptance: "
        f"{AUTHORITY_REF} SHA-256 {AUTHORITY_SHA}."
    ),
}


def append_notes(path: Path, appends: dict[str, str]) -> None:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)
    assert fieldnames is not None
    by_id = {row["ActionItemID"]: row for row in rows}
    assert set(appends).issubset(by_id)
    for action_id, addition in appends.items():
        row = by_id[action_id]
        assert addition not in row["Notes"], action_id
        row["Notes"] = f'{row["Notes"]} | {addition}'
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    append_notes(LIVE, LIVE_APPENDS)
    append_notes(ARCHIVE, ARCHIVE_APPENDS)


if __name__ == "__main__":
    main()
