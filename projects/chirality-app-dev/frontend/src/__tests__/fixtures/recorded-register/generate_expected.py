#!/usr/bin/env python3
"""Expected results for the App recorded-register parity test, from the Root tools.

Each folder under `cases/` is an execution root. For each one this script runs
the Root reference implementation on it and writes `expected/<case>.json`:

- `tools/coordination/dependency_evidence.py`: `project_registers` (the
  recorded register of every unit: `parse_declarations` and `union_register`)
  and, when `_DAG/_LATEST.md` names a version, `resolve_accepted_dag` and
  `check_currency`;
- `tools/coordination/build_dev001_blocker_queue.py`: `build_project_queue`
  in project mode without `--evidence`, so each arc is judged by its
  supplier's `_STATUS.md` state.

The Root tools take the default maturity threshold as `--default-maturity`.
The App reads it from `_Coordination/_COORDINATION.md`; this script reads it
with the same rule (below) and passes it to `build_project_queue`.

`src/__tests__/lib/recorded-register-parity.test.ts` runs the TypeScript
module on the same cases and compares its results with these files.

Usage, from the repository root:

    python3 projects/chirality-app-dev/frontend/src/__tests__/fixtures/recorded-register/generate_expected.py
    python3 projects/chirality-app-dev/frontend/src/__tests__/fixtures/recorded-register/generate_expected.py --check

`--check` writes nothing and exits 1 when a committed file differs from what
the Root tools now produce.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[6]
sys.path.insert(0, str(REPO_ROOT / "tools" / "coordination"))
sys.path.insert(0, str(REPO_ROOT / "tools" / "evaluation"))

import build_dev001_blocker_queue as queue_tool  # noqa: E402
import dependency_evidence as de  # noqa: E402

FALLBACK = "INITIALIZED"


def default_maturity(root: Path) -> dict[str, str]:
    """`**Default maturity threshold ...:** <STATE>` in `_COORDINATION.md`, else INITIALIZED."""
    fallback = {"value": FALLBACK, "source": "FALLBACK"}
    path = root / "_Coordination" / "_COORDINATION.md"
    if not path.is_file():
        return fallback
    line = re.search(r"default maturity threshold[^:\n]*:([^\n]*)", path.read_text(encoding="utf-8"), re.IGNORECASE)
    if not line:
        return fallback
    states = set(re.findall(r"\b(" + "|".join(de.LIFECYCLE_ORDER) + r")\b", line.group(1)))
    if len(states) != 1:
        return fallback
    return {"value": states.pop(), "source": "COORDINATION_RECORD"}


def entry(item: de.DeclaredEntry) -> dict[str, str]:
    data = asdict(item)
    return {
        "direction": data["direction"],
        "targetId": data["target_id"],
        "targetName": data["target_name"],
        "reason": data["reason"],
        "requiredMaturity": data["required_maturity"],
        "location": data["location"],
        "heading": data["heading"],
        "raw": data["raw"],
    }


def register(item: de.RecordedRegister) -> dict[str, object]:
    return {
        "deliverableId": item.deliverable_id,
        "mode": item.mode,
        "csvPresent": item.csv_present,
        "declarationsPresent": item.declarations_present,
        "entries": [entry(value) for value in item.entries],
        "rows": item.rows,
        "declaredOnly": item.declared_only,
        "disagreements": item.disagreements,
        "unread": item.unread,
    }


def currency(root: Path, registers: dict[str, de.RecordedRegister]) -> dict[str, object] | None:
    dag = de.resolve_accepted_dag(root)
    if dag is None:
        return None
    data = de.check_currency(dag, registers).as_dict()
    return {
        "result": data["result"],
        "dagPendingCount": data["dag_pending_count"],
        "dagPending": data["dag_pending"],
        "addedArcs": data["added_arcs"],
        "removedArcs": data["removed_arcs"],
        "addedDeliverables": data["added_deliverables"],
        "removedDeliverables": data["removed_deliverables"],
    }


def expected(root: Path) -> dict[str, object]:
    registers = de.project_registers(root)
    default = default_maturity(root)
    summary = queue_tool.build_project_queue(root, None, default["value"])
    accepted = summary["accepted_dag"]
    return {
        "defaultMaturity": default,
        "registers": {key: register(value) for key, value in registers.items()},
        "currency": currency(root, registers),
        "queue": {
            "blockerSource": summary["blocker_source"],
            "acceptedDagVersion": accepted["version"] if accepted else None,
            "gatingArcCount": summary["gating_arc_count"],
            "heldArcCount": summary["held_arc_count"],
            "declaredOnlyCount": summary["declared_only_count"],
            "declaredDisagreements": summary["declared_disagreements"],
            "unblockedCount": summary["unblocked_count"],
            "blockedCount": summary["blocked_count"],
            "dagPendingCount": summary["dag_pending_count"],
            "notTrackedCount": summary["not_tracked_count"],
            "queueRows": summary["queue_rows"],
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="compare with the committed files; write nothing")
    args = parser.parse_args(argv)
    out_dir = HERE / "expected"
    drift: list[str] = []
    for case in sorted(path for path in (HERE / "cases").iterdir() if path.is_dir()):
        text = json.dumps(expected(case), indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        target = out_dir / f"{case.name}.json"
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != text:
                drift.append(case.name)
            continue
        out_dir.mkdir(exist_ok=True)
        target.write_text(text, encoding="utf-8")
    if drift:
        print("expected results differ from the Root tools for: " + ", ".join(drift), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
