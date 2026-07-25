#!/usr/bin/env python3
"""PEC advisory blocker-state report (D-PEC-63 packet-local; report-only).

Advisory visibility only — never work assignment (PROJECT_SETUP invariants;
consistent with PEC-K-06's spirit). Reads deliverable-local Dependencies.csv
v3.1 registers + _STATUS.md lifecycle states; mutates nothing
(SatisfactionStatus refresh is explicitly deferred to a later
TASK + dependency-extract packet).

Usage (run from {REPO_ROOT}):
  python3 projects/pec/execution/_Coordination/WAVE_D-PEC-63/report_blocker_state.py \
      projects/pec/execution [--output <path>] [--json]

Rules (per D-PEC-62 ruled semantics):
- Edges considered: DependencyClass=EXECUTION, Direction=UPSTREAM, Status=ACTIVE.
- ANCHOR rows excluded (counted).
- Edges targeting a C-08 STANDING node are excluded (counted): standing
  nodes gate releases, not successors.
- Edge satisfied iff lifecycle(target) >= RequiredMaturity on the order
  OPEN < INITIALIZED < SEMANTIC_READY < IN_PROGRESS < CHECKING < ISSUED.
  An out-of-vocabulary RequiredMaturity is a hard parse failure (exit 2).
- Lifecycle read strictly from the `**Current State:**` line (never a
  whole-file substring scan — the _STATUS.md History block retains prior
  state names).
- Full row accounting is printed and asserted: ANCHOR + EXECUTION + other
  == total rows read.
- Exit 0 on a completed report; exit 2 on any IO/parse failure. A non-zero
  exit is a halt signal, never a blocker verdict.
"""
import argparse, csv, json, re, sys
from collections import defaultdict
from pathlib import Path

ORDER = {"OPEN": 0, "INITIALIZED": 1, "SEMANTIC_READY": 2,
         "IN_PROGRESS": 3, "CHECKING": 4, "ISSUED": 5}
STANDING = {"DEL-01-05", "DEL-03-04", "DEL-10-02", "DEL-10-03", "DEL-10-10"}
STATE_RE = re.compile(r"^\*\*Current State:\*\*\s*(\S+)", re.M)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("execution_root")
    ap.add_argument("--output")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = Path(args.execution_root)
    reg_paths = sorted(root.glob("PKG-*/1_Working/DEL-*/Dependencies.csv"))
    if not reg_paths:
        print(f"ERROR: no Dependencies.csv under {root}", file=sys.stderr)
        sys.exit(2)

    states, rows_by_del = {}, {}
    counts = defaultdict(int)
    for reg in reg_paths:
        ddir = reg.parent
        del_id = ddir.name.split("_")[0]
        try:
            m = STATE_RE.search((ddir / "_STATUS.md").read_text())
        except OSError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            sys.exit(2)
        if not m or m.group(1) not in ORDER:
            print(f"ERROR: unparseable _STATUS.md state in {ddir}", file=sys.stderr)
            sys.exit(2)
        states[del_id] = m.group(1)
        try:
            with open(reg, newline="") as f:
                rows_by_del[del_id] = list(csv.DictReader(f))
        except (OSError, csv.Error) as exc:
            print(f"ERROR: {reg}: {exc}", file=sys.stderr)
            sys.exit(2)
        counts["total_rows"] += len(rows_by_del[del_id])

    results = []
    for del_id in sorted(states):
        active, satisfied, blockers, blocking_edges = 0, 0, [], []
        unresolved = []
        for r in rows_by_del[del_id]:
            if r.get("DependencyClass") == "ANCHOR":
                counts["anchor_rows"] += 1
                continue
            if r.get("DependencyClass") != "EXECUTION":
                counts["other_rows"] += 1
                continue
            counts["execution_rows"] += 1
            if r.get("Direction") != "UPSTREAM" or r.get("Status") != "ACTIVE":
                counts["inactive_or_downstream"] += 1
                continue
            target = r.get("TargetDeliverableID", "").strip()
            if target in STANDING:
                counts["standing_edges_excluded"] += 1
                continue
            req = r.get("RequiredMaturity", "").strip()
            if req in ("", "NOT_APPLICABLE"):
                counts["no_maturity_excluded"] += 1
                continue
            if req not in ORDER:
                print(f"ERROR: {del_id} {r.get('DependencyID','?')}: "
                      f"out-of-vocabulary RequiredMaturity {req!r}", file=sys.stderr)
                sys.exit(2)
            active += 1
            if target not in states:
                unresolved.append(target)
                blockers.append(target)
                blocking_edges.append(r.get("DependencyID", "?"))
                continue
            if ORDER[states[target]] >= ORDER[req]:
                satisfied += 1
            else:
                blockers.append(target)
                blocking_edges.append(r.get("DependencyID", "?"))
        counts["unresolved_targets"] += len(unresolved)
        results.append({
            "DeliverableID": del_id,
            "NodeClass": "STANDING" if del_id in STANDING else "NORMAL",
            "LifecycleState": states[del_id],
            "ActiveUpstreamCount": active,
            "SatisfiedUpstreamCount": satisfied,
            "BlockingUpstreamCount": len(blockers),
            "BlockerState": "BLOCKED" if blockers else "UNBLOCKED",
            "BlockingUpstream": ";".join(blockers),
            "BlockingEdgeIDs": ";".join(blocking_edges),
        })

    blocked = sum(1 for r in results if r["BlockerState"] == "BLOCKED")
    unblocked = len(results) - blocked

    lines = [
        "# PEC blocker-state advisory report",
        "",
        "**Advisory visibility only — never work assignment. Report-only;",
        "no register mutation; SatisfactionStatus refresh deferred.**",
        "",
        f"- Registers read: {len(reg_paths)}; total rows: {counts['total_rows']}",
        f"- ANCHOR rows excluded: {counts['anchor_rows']}",
        f"- EXECUTION rows: {counts['execution_rows']} (non-UPSTREAM/ACTIVE among them: {counts['inactive_or_downstream']})",
        f"- Rows of other DependencyClass: {counts['other_rows']}",
        f"- Standing-target edges excluded (C-08 {sorted(STANDING)}): {counts['standing_edges_excluded']}",
        f"- Edges without maturity: {counts['no_maturity_excluded']}; unresolved targets: {counts['unresolved_targets']}",
        f"- **BLOCKED: {blocked} / UNBLOCKED: {unblocked}**",
        "",
        "| Deliverable | Class | State | Active | Satisfied | Blocking | Verdict | Blocking upstream |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        lines.append(
            f"| {r['DeliverableID']} | {r['NodeClass']} | {r['LifecycleState']} | "
            f"{r['ActiveUpstreamCount']} | {r['SatisfiedUpstreamCount']} | "
            f"{r['BlockingUpstreamCount']} | {r['BlockerState']} | {r['BlockingUpstream']} |")
    report = "\n".join(lines) + "\n"

    accounted = counts["anchor_rows"] + counts["execution_rows"] + counts["other_rows"]
    if accounted != counts["total_rows"]:
        print(f"ERROR: row accounting failure: ANCHOR {counts['anchor_rows']} + "
              f"EXECUTION {counts['execution_rows']} + other {counts['other_rows']} "
              f"!= total {counts['total_rows']}", file=sys.stderr)
        sys.exit(2)

    if args.output:
        try:
            Path(args.output).write_text(report)
        except OSError as exc:
            print(f"ERROR: cannot write {args.output}: {exc}", file=sys.stderr)
            sys.exit(2)
        print(f"written: {args.output}")
    print(f"BLOCKED {blocked} / UNBLOCKED {unblocked} "
          f"(registers {len(reg_paths)}, rows {counts['total_rows']} = "
          f"ANCHOR {counts['anchor_rows']} + EXECUTION {counts['execution_rows']} + "
          f"other {counts['other_rows']}; standing-excluded {counts['standing_edges_excluded']}, "
          f"non-upstream-active {counts['inactive_or_downstream']})")
    if args.json:
        print(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
