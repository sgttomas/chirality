#!/usr/bin/env python3
"""Behaviour-equivalence evaluator for Section 8 premerge summaries.

Given two or more `summary.json` files produced by
`frontend/scripts/validate-harness-section8.mjs` (directly, or copied to the
stable path `frontend/artifacts/harness/section8/latest/summary.json`), print
the behaviour-bearing projection of each and report whether they are equal.

The projection keeps exactly what the DEL-09-01 preservation contract asserts
(required IDs in REQUIRED_CHECK_ORDER, per-row status, per-row `details`,
overall status, testCount, stagedFromInstructionRoot) and drops what a fresh
run legitimately regenerates (generatedAt, durationMs, harnessBaseUrl, the
absolute project-root paths, per-run session and engine-session identifiers).

Exit status: 0 when every projection is identical and every file passes the
required-ID / legacy-ID checks and reports `pass` overall and per row (so two
identical *failing* summaries never compare as a preserved pass); 1 otherwise. Usage:

    python3 compare-section8-summaries.py A.json B.json [C.json ...]
"""
import json
import sys

REQUIRED_IDS = [
    "setup.server_reachable",
    "regression.session_crud",
    "section8.boot_error_taxonomy",
    "section8.smoke_stream",
    "section8.session_persistence_resume",
    "section8.permissions_dontask",
    "section8.interrupt_sigint",
    "section8.sdk_native_stream",
]
LEGACY_REMOVED_ID = "regression.api_chat_reachability"
RUN_SPECIFIC_DETAIL_KEYS = {"sessionId", "engineSessionId"}


def project(path):
    with open(path, encoding="utf-8") as handle:
        summary = json.load(handle)
    rows = []
    problems = []
    seen = [row.get("id") for row in summary.get("results", [])]
    for required in REQUIRED_IDS:
        if required not in seen:
            problems.append(f"missing required id {required}")
    if LEGACY_REMOVED_ID in seen:
        problems.append(f"contains legacy id {LEGACY_REMOVED_ID}")
    if seen != REQUIRED_IDS:
        problems.append(f"row order/inventory differs from REQUIRED_CHECK_ORDER: {seen}")
    if summary.get("status") != "pass":
        problems.append(f"summary status is {summary.get('status')!r}, expected 'pass'")
    for row in summary.get("results", []):
        if row.get("status") != "pass":
            problems.append(f"row {row.get('id')} status is {row.get('status')!r}, expected 'pass'")
    for row in summary.get("results", []):
        details = dict(row.get("details") or {})
        for key in RUN_SPECIFIC_DETAIL_KEYS:
            details.pop(key, None)
        rows.append(
            {
                "id": row.get("id"),
                "status": row.get("status"),
                "details": details,
                **({"error": row["error"]} if "error" in row else {}),
            }
        )
    projection = {
        "status": summary.get("status"),
        "testCount": summary.get("testCount"),
        "stagedFromInstructionRoot": summary.get("stagedFromInstructionRoot"),
        "results": rows,
    }
    return projection, problems


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    projections = []
    exit_code = 0
    for path in argv:
        projection, problems = project(path)
        projections.append(projection)
        canonical = json.dumps(projection, sort_keys=True, separators=(",", ":"))
        print(f"== {path}")
        print(f"   status={projection['status']} testCount={projection['testCount']} "
              f"staged={projection['stagedFromInstructionRoot']}")
        for row in projection["results"]:
            print(f"   {row['id']:40s} {row['status']:5s} {json.dumps(row['details'], sort_keys=True)}")
        if problems:
            exit_code = 1
            for problem in problems:
                print(f"   PROBLEM: {problem}")
        print(f"   projection-json={canonical}")
    first = json.dumps(projections[0], sort_keys=True)
    equal = all(json.dumps(p, sort_keys=True) == first for p in projections[1:])
    print(f"BEHAVIOUR_PROJECTIONS_EQUAL={'true' if equal else 'false'}")
    if not equal:
        exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
