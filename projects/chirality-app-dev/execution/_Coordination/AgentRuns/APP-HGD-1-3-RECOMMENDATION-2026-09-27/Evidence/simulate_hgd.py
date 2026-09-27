#!/usr/bin/env python3
"""HGD-1, HGD-3 and FC-1..FC-3 graph simulations over the current App registers (read-only on deliverables).

Run from the repository root:

    python3 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP-HGD-1-3-RECOMMENDATION-2026-09-27/Evidence/simulate_hgd.py

Method. For each scenario the script copies every live unit's `Dependencies.csv`, `_DEPENDENCIES.md` and `_STATUS.md`
(`PKG-*/1_Working/DEL-*`, the inventory the DepClosure snapshots use) into a temporary execution root, applies the
scenario's moves from `SCENARIOS.json` to the copied registers, and then runs, unchanged:

- `tools/coordination/analyze_dep_closure.py` with the arguments of
  `_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739/closure_run.py` (the 51 current units;
  ACTIVE EXECUTION rows with DELIVERABLE targets; declared entries included), compared with that snapshot's summary;
- `tools/coordination/build_dev001_blocker_queue.py --execution-root` (project mode, no accepted DAG: blockers from the
  recorded register, each arc judged by the supplier's `_STATUS.md` state against the arc's `RequiredMaturity`,
  default `INITIALIZED` because `_Coordination/_COORDINATION.md` records no threshold; arcs inside an SCC are held).

Scenarios: BASE (no move), every subset of the five decision moves (S1, S2, FC1, FC2, FC3), and three controls. Outputs
are written under `runs/` next to this script, with the temporary root replaced by `<SIM_ROOT>`; the summary is
`SIMULATION_RESULTS.json` / `.csv`, the reachability witnesses `REACHABILITY.json`, and the input hashes
`INPUT_HASHES.json`. The live registers are hashed before and after; the script fails if any changed.
"""
from __future__ import annotations

import csv
import glob
import hashlib
import io
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
EX = "projects/chirality-app-dev/execution"
AN = "tools/coordination/analyze_dep_closure.py"
BQ = "tools/coordination/build_dev001_blocker_queue.py"
DE = "tools/coordination/dependency_evidence.py"
BASIS_SNAPSHOT = f"{EX}/_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739"
PRIOR = f"{BASIS_SNAPSHOT}/Evidence/closure_summary.json"
EXEMPT = {"DEL-00-01", "DEL-00-02", "DEL-09-07"}
FIXED = ["--filter-active-only", "true", "--normalize-ids", "true", "--dependency-class", "EXECUTION", "--target-type",
         "DELIVERABLE", "--hub-threshold", "20", "--max-cycles", "10000", "--include-declared", "true"]
COPIED = ("Dependencies.csv", "_DEPENDENCIES.md", "_STATUS.md")
FOCUS = ["DEL-02-02", "DEL-02-05", "DEL-03-02", "DEL-05-03", "DEL-08-02"]
KEPT_CLOSURE_FILES = ("closure_summary.json", "scc_summary.csv", "bidirectional_pairs.csv", "cycles_sample.csv")

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "coordination"))
import dependency_evidence as de  # noqa: E402


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def units():
    found = {}
    for folder in sorted(glob.glob(f"{EX}/PKG-*/1_Working/DEL-*")):
        found[re.match(r"(DEL-\d{2}-\d{2})", os.path.basename(folder)).group(1)] = folder
    return found


def input_hashes(unit_map):
    out = {}
    for folder in unit_map.values():
        for name in COPIED:
            path = f"{folder}/{name}"
            if os.path.exists(path):
                out[path] = sha(path)
    return out


def apply_moves(sim_ex, unit_map, moves):
    """Apply update/add moves to the copied registers; return the rows touched, for the record."""
    touched = []
    by_carrier = {}
    for move in moves:
        by_carrier.setdefault(move["carrier"], []).append(move)
    for carrier, items in sorted(by_carrier.items()):
        path = os.path.join(sim_ex, os.path.relpath(unit_map[carrier], EX), "Dependencies.csv")
        with open(path, encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            header, rows = reader.fieldnames, list(reader)
        for move in items:
            if move["op"] == "update":
                hits = [r for r in rows if r["DependencyID"] == move["DependencyID"]]
                if len(hits) != 1:
                    raise SystemExit(f"{move['DependencyID']}: expected one row in {carrier}, found {len(hits)}")
                before = {k: hits[0][k] for k in move["set"]}
                hits[0].update(move["set"])
                touched.append({"op": "update", "DependencyID": move["DependencyID"], "before": before, "after": move["set"]})
            elif move["op"] == "add":
                if any(r["DependencyID"] == move["row"]["DependencyID"] for r in rows):
                    raise SystemExit(f"{move['row']['DependencyID']} already exists in {carrier}")
                if set(move["row"]) != set(header):
                    raise SystemExit(f"{move['row']['DependencyID']}: row fields differ from the register header")
                rows.append(dict(move["row"]))
                touched.append({"op": "add", "DependencyID": move["row"]["DependencyID"]})
            else:
                raise SystemExit(f"unknown op {move['op']}")
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=header, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(buf.getvalue())
    return touched


def strict_arcs(sim_ex):
    """Consumer->supplier arcs of ACTIVE EXECUTION rows with DELIVERABLE targets over the recorded registers."""
    arcs = {}
    for unit_id, register in de.project_registers(__import__("pathlib").Path(sim_ex)).items():
        for row in register.union_rows:
            if de.clean(row.get("Status")) != "ACTIVE":
                continue
            item = de.arc(row)
            if item:
                arcs.setdefault(item, set()).add(de.clean(row.get("DependencyID")) or f"DECLARED:{unit_id}")
    return {k: sorted(v) for k, v in arcs.items()}


def shortest_path(arcs, start, goal):
    graph = {}
    for (a, b) in arcs:
        graph.setdefault(a, set()).add(b)
    prev, seen, queue = {}, {start}, deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            path = [goal]
            while path[-1] != start:
                path.append(prev[path[-1]])
            return list(reversed(path))
        for nxt in sorted(graph.get(node, ())):
            if nxt not in seen:
                seen.add(nxt)
                prev[nxt] = node
                queue.append(nxt)
    return None


def sanitize(folder, tmp):
    for dirpath, _dirs, files in os.walk(folder):
        for name in files:
            path = os.path.join(dirpath, name)
            data = open(path, "rb").read()
            # As closure_run.py does: strip the local root and write LF line endings.
            new = data.replace(tmp.encode(), b"<SIM_ROOT>").replace((os.getcwd() + "/").encode(), b"").replace(b"\r\n", b"\n")
            if new != data:
                open(path, "wb").write(new)


def run_scenario(name, moves, unit_map, current, runs_dir):
    tmp = tempfile.mkdtemp(prefix="hgd-sim-")
    try:
        sim_ex = os.path.join(tmp, "execution")
        for folder in unit_map.values():
            dest = os.path.join(sim_ex, os.path.relpath(folder, EX))
            os.makedirs(dest)
            for fname in COPIED:
                if os.path.exists(f"{folder}/{fname}"):
                    shutil.copyfile(f"{folder}/{fname}", os.path.join(dest, fname))
        touched = apply_moves(sim_ex, unit_map, moves)
        out = os.path.join(runs_dir, name)
        if os.path.exists(out):
            shutil.rmtree(out)
        os.makedirs(out)
        full = os.path.join(tmp, "closure")
        r = subprocess.run([sys.executable, "-B", AN, sim_ex, "--output-dir", full, "--scope"] + current + FIXED
                           + ["--prior-summary", PRIOR], capture_output=True, text=True)
        if r.returncode not in (0, 1):
            raise SystemExit(f"{name}: analyzer exit {r.returncode}: {r.stderr}")
        for fname in KEPT_CLOSURE_FILES:
            shutil.copyfile(os.path.join(full, fname), os.path.join(out, fname))
        summary = json.load(open(os.path.join(full, "closure_summary.json")))
        queue_json = os.path.join(tmp, "queue.json")
        q = subprocess.run([sys.executable, "-B", BQ, "--execution-root", sim_ex, "--json-out", queue_json,
                            "--csv-out", os.path.join(out, "blocker_queue.csv"), "--generated-date", "2026-09-27"],
                           capture_output=True, text=True)
        if q.returncode != 0:
            raise SystemExit(f"{name}: blocker queue exit {q.returncode}: {q.stderr}")
        queue = json.load(open(queue_json))
        with open(os.path.join(out, "blocker_queue_stdout.txt"), "w", encoding="utf-8") as fh:
            fh.write(q.stdout)
        arcs = strict_arcs(sim_ex)
        sccs = list(csv.DictReader(open(os.path.join(full, "scc_summary.csv"), encoding="utf-8")))
        sanitize(out, tmp)
        return {"summary": summary, "queue": queue, "arcs": arcs, "sccs": sccs, "touched": touched,
                "analyzer_exit": r.returncode}
    finally:
        shutil.rmtree(tmp)


def main():
    spec = json.load(open(os.path.join(HERE, "SCENARIOS.json"), encoding="utf-8"))
    unit_map = units()
    current = sorted(u for u in unit_map if u not in EXEMPT)
    before = input_hashes(unit_map)
    moves = spec["moves"]
    scenarios = [("BASE", [])]
    decision = spec["decision_moves"]
    for size in range(1, len(decision) + 1):
        for combo in itertools.combinations(decision, size):
            scenarios.append(("+".join(combo), list(combo)))
    for cname, combo in spec["controls"].items():
        scenarios.append((cname, list(combo)))
    runs_dir = os.path.join(HERE, "runs")
    if os.path.exists(runs_dir):
        shutil.rmtree(runs_dir)
    os.makedirs(runs_dir)
    results = {}
    for name, combo in scenarios:
        results[name] = run_scenario(name, [moves[m] for m in combo], unit_map, current, runs_dir)
        results[name]["moves"] = combo
    after = input_hashes(unit_map)
    if before != after:
        raise SystemExit("live registers changed during the run")

    base = results["BASE"]
    base_rows = {row["DeliverableID"]: row for row in base["queue"]["queue_rows"]}
    table, full = [], {}
    for name, combo in scenarios:
        res = results[name]
        added = {f"{a}->{b}": ids for (a, b), ids in sorted(res["arcs"].items()) if (a, b) not in base["arcs"]}
        removed = {f"{a}->{b}": ids for (a, b), ids in sorted(base["arcs"].items()) if (a, b) not in res["arcs"]}
        changed = {}
        for row in res["queue"]["queue_rows"]:
            ref = base_rows.get(row["DeliverableID"], {})
            diff = {k: [ref.get(k, ""), row[k]] for k in ("BlockerState", "BlockingEdgeIDs", "HeldEdgeIDs", "ActiveUpstreamCount")
                    if ref.get(k, "") != row[k]}
            if diff:
                changed[row["DeliverableID"]] = diff
        s = res["summary"]
        scc_text = " | ".join(f"{x['SCC_ID']}({x['Size']}): {x['Nodes']}" for x in res["sccs"]) or "none"
        verdict_changes = {d: v["BlockerState"] for d, v in changed.items() if "BlockerState" in v}
        entry = {
            "scenario": name, "moves": combo, "graph_edges": s["graph_edges"], "scc_count": s["scc_count"],
            "scc_sizes": s["scc_sizes"], "sccs": res["sccs"], "bidirectional_pair_count": s["bidirectional_pair_count"],
            "subject_status": s["subject_status"], "circular_dependencies": s["checks"]["circular_dependencies"],
            "edges_added_vs_base": added, "edges_removed_vs_base": removed,
            "blocker_counts": {k: res["queue"][k] for k in ("unblocked_count", "blocked_count", "not_tracked_count",
                                                            "held_arc_count", "gating_arc_count")},
            "blocker_verdict_changes_vs_base": verdict_changes, "queue_row_changes_vs_base": changed,
            "rows_touched": res["touched"], "analyzer_exit": res["analyzer_exit"],
        }
        full[name] = entry
        table.append([name, ";".join(combo) or "-", s["graph_edges"], s["scc_count"], scc_text,
                      "; ".join(f"{k} [{','.join(v)}]" for k, v in added.items()) or "-",
                      "; ".join(f"{k} [{','.join(v)}]" for k, v in removed.items()) or "-",
                      res["queue"]["blocked_count"], res["queue"]["held_arc_count"],
                      "; ".join(f"{d}: {v[0]}->{v[1]}" for d, v in verdict_changes.items()) or "none",
                      "; ".join(f"{d}: held {v['HeldEdgeIDs'][1]}" for d, v in changed.items() if "HeldEdgeIDs" in v) or "-"])
    with open(os.path.join(HERE, "SIMULATION_RESULTS.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["Scenario", "Moves", "GraphEdges", "SCCCount", "SCCs", "EdgesAddedVsBase", "EdgesRemovedVsBase",
                    "BlockedCount", "HeldArcCount", "BlockerVerdictChanges", "NewlyHeldArcs"])
        w.writerows(table)
    json.dump(full, open(os.path.join(HERE, "SIMULATION_RESULTS.json"), "w", encoding="utf-8"), indent=1, sort_keys=True)

    reach = {}
    for name in ("BASE", "S1"):
        arcs = results[name]["arcs"]
        reach[name] = {
            "to_DEL-02-01": {n: shortest_path(arcs, n, "DEL-02-01") for n in FOCUS},
            "from_DEL-02-01": {n: shortest_path(arcs, "DEL-02-01", n) for n in FOCUS},
            "DEL-02-01_out_arcs": {f"{a}->{b}": ids for (a, b), ids in sorted(arcs.items()) if a == "DEL-02-01"},
            "DEL-02-01_in_arcs": {f"{a}->{b}": ids for (a, b), ids in sorted(arcs.items()) if b == "DEL-02-01"},
        }
    reach["convention"] = "consumer->supplier (UPSTREAM rows as written; DOWNSTREAM rows reversed), as analyze_dep_closure.py and build_dev001_blocker_queue.py read them"
    json.dump(reach, open(os.path.join(HERE, "REACHABILITY.json"), "w", encoding="utf-8"), indent=1, sort_keys=True)

    # Basis check: the BASE run must reproduce the DepClosure snapshot it is compared with.
    basis_summary = json.load(open(PRIOR, encoding="utf-8"))
    base_summary = json.load(open(os.path.join(runs_dir, "BASE", "closure_summary.json"), encoding="utf-8"))
    drop = ("comparison",)
    reproduces = {k: v for k, v in base_summary.items() if k not in drop} == {k: v for k, v in basis_summary.items() if k not in drop}
    tool_run = json.load(open(f"{BASIS_SNAPSHOT}/Tool_Run.json", encoding="utf-8"))
    basis_inputs = {item["path"]: item["sha256"] for item in tool_run["accepted_input_basis"]}
    same_inputs = all(before.get(p) == h for p, h in basis_inputs.items())
    basis_check = {"basis_snapshot": BASIS_SNAPSHOT,
                   "base_closure_summary_equals_basis_except_comparison": reproduces,
                   "base_comparison_deltas": base_summary.get("comparison", {}).get("deltas"),
                   "basis_input_files": len(basis_inputs),
                   "basis_input_hashes_match_current_registers": same_inputs}
    json.dump(basis_check, open(os.path.join(HERE, "BASIS_CHECK.json"), "w", encoding="utf-8"), indent=1, sort_keys=True)
    if not (reproduces and same_inputs):
        raise SystemExit(f"BASE does not reproduce the basis snapshot: {basis_check}")

    tools = {p: sha(p) for p in (AN, BQ, DE, "tools/coordination/materialize_local_dependencies.py",
                                 "tools/evaluation/audit_common.py", PRIOR,
                                 os.path.relpath(os.path.join(HERE, "SCENARIOS.json")),
                                 os.path.relpath(os.path.abspath(__file__)))}
    json.dump({"schema": "app-hgd-simulation-inputs/v1", "basis_snapshot": BASIS_SNAPSHOT, "tools_and_specs": tools,
               "registers": dict(sorted(before.items())), "registers_stable": before == after,
               "current_units": current, "exempt_units": sorted(EXEMPT)},
              open(os.path.join(HERE, "INPUT_HASHES.json"), "w", encoding="utf-8"), indent=1, sort_keys=True)
    for row in table:
        print(" | ".join(str(x) for x in row))


if __name__ == "__main__":
    main()
