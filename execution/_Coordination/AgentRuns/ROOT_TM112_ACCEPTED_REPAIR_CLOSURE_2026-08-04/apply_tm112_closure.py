#!/usr/bin/env python3
"""Apply the exact owner-ruled TM-ROOT-112 closure before mechanical archive."""

from __future__ import annotations

import csv
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
REGISTER = REPO / "execution/_Coordination/_TaskManagement/REGISTER.csv"
AUTHORITY_REF = (
    "execution/_Coordination/AgentRuns/"
    "ROOT_TM112_IMPLEMENTATION_ACCEPTANCE_2026-08-04/"
    "OWNER_RETURN_TRANSCRIPT_2026-08-04.txt"
)
AUTHORITY_SHA = (
    "a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046"
)

CLOSURE_NOTE = (
    "2026-08-04 accepted-repair closure: accountable human accepted the exact "
    "TM-ROOT-112 G2+C1+F1 repair and the recorded Node 24 strict, adversarial "
    "2/2, daemon 15/15, full-runtime 74/74, build, and fresh-backcheck evidence. "
    "Exact accepted SHA-256 product identities: docs/SPEC.md "
    "647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f; "
    "runtime/packages/daemon/src/runtime-daemon.ts "
    "224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2; "
    "runtime/tests/daemon.test.ts "
    "c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352. "
    "Node 22.19 execution remains an explicit unexecuted compatibility gap. "
    "The ordinary Root-to-App notice is released for routing and must name "
    "D-APP-88 and TM-APP-036's mandatory non-blocking parity-rerun rider. "
    "Closure makes no claim of App R2 causality, process/SIGTERM proof, App "
    "parity acceptance, foreign-register disposition, lifecycle/reliance, or "
    "merge authority. Owner acceptance: "
    f"{AUTHORITY_REF} SHA-256 {AUTHORITY_SHA}."
)


def main() -> None:
    with REGISTER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)
    assert fieldnames is not None
    targets = [row for row in rows if row["ActionItemID"] == "TM-ROOT-112"]
    assert len(targets) == 1
    row = targets[0]
    assert row["Status"] == "OPEN"
    assert row["Disposition"] == ""
    assert row["EvidenceRef"] == row["EvidenceSha"] == ""
    assert row["Closed"] == ""
    assert CLOSURE_NOTE not in row["Notes"]

    row["Status"] = "CLOSED"
    row["Disposition"] = "RESOLVED_WITH_CHANGE"
    row["EvidenceRef"] = AUTHORITY_REF
    row["EvidenceSha"] = AUTHORITY_SHA
    row["EvidenceQuote"] = (
        "ACCEPT ROOT-TM112-IMPLEMENTATION-ACCEPTANCE-01 FINAL-HASH-REPAIR — "
        "ACCEPT THE TM-ROOT-112 G2+C1+F1 IMPLEMENTATION ... AS THE ACCEPTED "
        "ROOT GRACEFUL-STOP REPAIR"
    )
    row["LastReviewed"] = "2026-08-04"
    row["Closed"] = "2026-08-04"
    row["Notes"] = f'{row["Notes"]} | {CLOSURE_NOTE}'

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
