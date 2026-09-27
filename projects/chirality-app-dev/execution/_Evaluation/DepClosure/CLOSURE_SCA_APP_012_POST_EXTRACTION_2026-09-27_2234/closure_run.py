#!/usr/bin/env python3
"""audit-dep-closure after the SCA-APP-012 incremental setup's dependency re-extraction (read-only on deliverables).

project-setup INCREMENTAL Phase 5.6 (FULL_GRAPH), run APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27. Run from the repository
root with this one command. Writes only this snapshot folder. UPDATE_LATEST_POINTER=false.
Order: both analyzer runs rebuild Evidence/ from scratch, then this script runs edge_delta.py as its last step, so
Evidence/edge_delta.csv (against the 1923 snapshot's register basis, commit 63e5de1f2, whose registers hash-match 1923's
inputs) is always regenerated after the analyzer (running edge_delta.py alone afterwards is equivalent).
"""
import csv, glob, hashlib, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REL = os.path.relpath(HERE)
EX = "projects/chirality-app-dev/execution"
AN = "tools/coordination/analyze_dep_closure.py"
EXEMPT = {"DEL-00-01": ("CONTROL", "its _CONTEXT.md excludes product graph participation and intentionally omits Dependencies.csv"),
          "DEL-00-02": ("CONTROL", "its _CONTEXT.md excludes product graph participation and intentionally omits Dependencies.csv"),
          "DEL-09-07": ("RETIRED", "decomposition Deliverables row annotated [RETIRED] (SOW-080 OUT); folder and historical register kept")}
PRIOR_CUR = f"{EX}/_Evaluation/DepClosure/CLOSURE_HGD_FC_RULING_2026-09-27_1923/Evidence/closure_summary.json"
PRIOR_ALL = f"{EX}/_Evaluation/DepClosure/CLOSURE_HGD_FC_RULING_2026-09-27_1923/Evidence/ALL/closure_summary.json"
FIXED = ["--filter-active-only", "true", "--normalize-ids", "true", "--dependency-class", "EXECUTION", "--target-type", "DELIVERABLE",
         "--hub-threshold", "20", "--max-cycles", "10000", "--include-declared", "true"]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def sanitize(folder):
    root = os.getcwd() + "/"
    for dp, _, fs in os.walk(folder):
        for f in fs:
            p = os.path.join(dp, f)
            b = open(p, "rb").read()
            nb = b.replace(root.encode(), b"").replace(b"\r\n", b"\n")
            if nb != b:
                open(p, "wb").write(nb)


def run(scope, outdir, prior):
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    args = [EX, "--output-dir", outdir, "--scope"] + scope + FIXED + ["--prior-summary", prior]
    r = subprocess.run([sys.executable, "-B", AN] + args, capture_output=True, text=True)
    open(os.path.join(outdir, "analyzer_stdout.json"), "w").write(r.stdout)
    open(os.path.join(outdir, "analyzer_stderr.txt"), "w").write(r.stderr)
    sanitize(outdir)
    return r.returncode, args, json.load(open(os.path.join(outdir, "closure_summary.json")))


def main():
    units = sorted(re.match(r"(DEL-\d{2}-\d{2})", os.path.basename(p)).group(1) for p in glob.glob(f"{EX}/PKG-*/1_Working/DEL-*"))
    current = [u for u in units if u not in EXEMPT]
    inputs = {}
    for u in units:
        f = glob.glob(f"{EX}/PKG-*/1_Working/{u}_*")[0]
        for n in ("Dependencies.csv", "_DEPENDENCIES.md"):
            if os.path.exists(f + "/" + n):
                inputs[f + "/" + n] = sha(f + "/" + n)
    rc_c, args_c, cur = run(current, os.path.join(REL, "Evidence"), PRIOR_CUR)
    rc_a, args_a, alls = run(["ALL"], os.path.join(REL, "Evidence", "ALL"), PRIOR_ALL)
    stable = all(sha(p) == h for p, h in inputs.items())
    tool = {"schema": "app-dep-closure-tool-run/v1", "analyzer": AN, "analyzer_sha256": sha(AN),
            "runs": [{"label": "CURRENT51", "argv": ["python3", AN] + args_c, "exit_code": rc_c, "run_status": cur["run_status"],
                      "subject_status": cur["subject_status"]},
                     {"label": "ALL", "argv": ["python3", AN] + args_a, "exit_code": rc_a, "run_status": alls["run_status"],
                      "subject_status": alls["subject_status"]}],
            "prior_summaries": {"CURRENT51": [PRIOR_CUR, sha(PRIOR_CUR)], "ALL": [PRIOR_ALL, sha(PRIOR_ALL)]},
            "accepted_dag": "none (_DAG/_LATEST.md absent)", "input_hashes_stable": stable,
            "accepted_input_basis": [{"path": p, "sha256": h} for p, h in sorted(inputs.items())]}
    json.dump(tool, open(os.path.join(HERE, "Tool_Run.json"), "w"), indent=1)
    iso = [r["DeliverableID"] for r in csv.DictReader(open(os.path.join(REL, "Evidence", "isolated.csv")))]
    iss = []
    for u in iso:
        iss.append(["WARNING", "isolated_units", u, "", "", f"{REL}/Evidence/isolated.csv", "Topology signal only; no missing target row. Review with the unit owner."])
    for u, (cls, why) in EXEMPT.items():
        iss.append(["INFO", "exemption", u, "", "", f"{REL}/Evidence/ALL/coverage.csv", f"Declared exemption {cls}: {why}."])
    with open(os.path.join(HERE, "Dependency_Closure_IssueLog.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["ID", "Severity", "Check", "FromDeliverableID", "TargetDeliverableID", "DependencyID", "Evidence", "FixSuggestion"])
        for i, x in enumerate(iss, 1):
            w.writerow([f"DCL-{i:03d}"] + x[:2] + [x[2], x[3], x[4], x[5], x[6]])
    comp_c = cur.get("comparison", {}).get("deltas", {})
    comp_a = alls.get("comparison", {}).get("deltas", {})
    summary = {"CURRENT51": {k: cur.get(k) for k in ("run_status", "subject_status", "graph_nodes", "graph_edges", "scc_count", "orphan_count",
                                                        "outside_scope_count", "isolated_count", "bidirectional_pair_count", "hub_count",
                                                        "schema_invalid", "implements_node_missing", "checks")},
               "ALL": {k: alls.get(k) for k in ("run_status", "subject_status", "graph_nodes", "graph_edges", "scc_count", "orphan_count",
                                                 "isolated_count", "schema_invalid", "implements_node_missing", "checks")},
               "deltas_vs_prior": {"CURRENT51_vs_1923": comp_c, "ALL_vs_1923": comp_a}, "isolated_current": iso}
    json.dump(summary, open(os.path.join(HERE, "closure_run_summary.json"), "w"), indent=1)
    print(json.dumps(summary, indent=1)[:2500])
    subprocess.run([sys.executable, "-B", os.path.join(REL, "edge_delta.py"), "63e5de1f2f19c3a1dab073babbadfbfcc6199e70", "edge_delta.csv"], check=True)


if __name__ == "__main__":
    main()
