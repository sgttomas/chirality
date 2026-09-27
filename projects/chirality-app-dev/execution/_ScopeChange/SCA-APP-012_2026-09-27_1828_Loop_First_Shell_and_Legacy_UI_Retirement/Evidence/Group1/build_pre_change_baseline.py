#!/usr/bin/env python3
"""SCA-APP-012 checkpoint-group-1 pre-change baseline (read-only).

Synthesizes the pre-change baseline for SCA-APP-012 (retire the remaining
loop-first UI; settle the DEL-02-03 REQ-009 residual). It reads the App
decomposition, the deliverable records, the App governance documents and the
frontend source, runs the registered deterministic tools report-only, and
writes only `Pre_Change_Coverage.json` in this snapshot folder.

Run from the repository root:

    python3 projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Evidence/Group1/build_pre_change_baseline.py

The output carries no timestamp or absolute path. For an unchanged tree it is
byte-identical on every run. `governed_inputs_identical_to_basis` records
whether the App inputs still equal the basis commit (this snapshot folder
excluded).

The scaffold-entry scan (added at the coordinator's request of 2026-09-27)
records every App scope text that names `ProjectScaffoldPort` or a future App
scaffold entry, and every App or Runtime source that names the Runtime
scaffold port or its types. The Runtime retirement of that API is a separate,
pending change; the scan reports the basis only.

Revision 2 (same basis) also reports the flat-file workflow view and its read
route (choice W) and the layout metadata string among the code references,
and lists the workflow view among the in-scope modules without a product
importer.

Inputs (read-only):
  - projects/chirality-app-dev/execution/_Decomposition/*.md, *.csv
  - projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md
  - projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/{_STATUS.md,ScopeOfWork.md,_CONTEXT.md,Dependencies.csv}
  - projects/chirality-app-dev/docs/{PRD,SPEC,PLAN,TYPES,DIRECTIVE,CONTRACT}.md
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-74*, D-APP-108*
  - projects/chirality-app-dev/frontend/{src,electron,scripts}
  - projects/chirality-runtime/packages (reference scan only)
  - the reused full audit COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500
Registered tools invoked (report-only, into a temporary directory):
  - tools/evaluation/audit_structure.py --variant SOFTWARE
  - tools/coordination/analyze_dep_closure.py
  - tools/validation/validate_decomposition_registers.py
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter

SNAP_REL = (
    "projects/chirality-app-dev/execution/_ScopeChange/"
    "SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement"
)
BASIS_COMMIT = "0adfbc7476df33521883ce1573781237cd24d384"
APP = "projects/chirality-app-dev"
EXEC = f"{APP}/execution"
DOCS = f"{APP}/docs"
DECOMP = f"{EXEC}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
REGISTER = f"{EXEC}/_Decomposition/contract_invariant_coverage_register.csv"
POINTER = f"{EXEC}/_ScopeChange/_LATEST.md"
REUSED_AUDIT = f"{EXEC}/_Evaluation/DecompCoverage/COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500"
FRONTEND = f"{APP}/frontend"
SRC = f"{FRONTEND}/src"
RUNTIME_PACKAGES = "projects/chirality-runtime/packages"
DECISIONS = [
    f"{EXEC}/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md",
    f"{EXEC}/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md",
]
AFFECTED = ["DEL-02-01", "DEL-02-03", "DEL-06-03", "DEL-06-04", "DEL-07-02", "DEL-07-03", "DEL-08-02", "DEL-08-03",
            "DEL-09-06"]
SCOPE_ITEMS = ["SOW-001", "SOW-003", "SOW-005", "SOW-007", "SOW-024", "SOW-025"]
OBJECTIVES = ["OBJ-001", "OBJ-006", "OBJ-007"]
DEP_IDS = ["DEP-02-03-009", "DEP-02-03-004", "DEP-08-02-013", "DEP-08-03-007", "DEP-02-01-006", "DEP-02-01-008"]

# The three loop-first shells passed as the discarded `legacy` element.
LEGACY_SHELLS = [f"{SRC}/components/shell/{n}" for n in
                 ("loop-shell.tsx", "portal-loop-shell.tsx", "loop-tertiary-shell.tsx")]
DELIVERABLES_PROVIDER = f"{SRC}/components/workspace/deliverables-provider.tsx"
# Modules already without a product importer at the basis that this amendment addresses
# (the portal helpers, and the flat-file workflow view of choice W).
IN_SCOPE_UNREACHED = ("src/lib/portal/", "src/components/woven-dialogue/workflows-view.tsx",
                      "src/components/woven-dialogue/workflow-detail.tsx")
PAGE_DIRS = [f"{SRC}/app/workbench/", f"{SRC}/app/pipeline/"]

TEXT_PATTERNS = {
    "loop_first": r"loop-first|Loop-first",
    "legacy_shell_module": r"loop-shell|LoopShell|PortalLoopShell|LoopTertiaryShell|SidebarRightLoopLayout|sidebar-right-loop|tertiary-sidebar",
    "agent_matrix_ui": r"agent-matrix|AgentMatrix|matrix UI|matrix behavio|3x4",
    "legacy_prop_or_link": r"legacy prop|data-legacy|legacy=1|legacyHref|[Oo]ld[- ]UI|existing UI|current UI|legacy UI",
    "deliverables_provider": r"DeliverablesProvider|deliverables-provider",
    "scope_route": r"/api/working-root/scope",
    "page_routes": r"(?<![A-Za-z])/workbench\b|(?<![A-Za-z])/pipeline\b|PORTAL/WORKBENCH/PIPELINE",
    "req_009": r"DEL-02-03-REQ-009|DEL-02-03 REQ-009|DEP-02-03-009",
    "route_query_compat": r"DEP-08-02-013|route/query",
    "workflow_read_route": r"/api/working-root/workflow(?![-\w])|workflows-view|WorkflowsView|workflow-detail",
    "scaffold_entry": r"ProjectScaffoldPort|scaffold entry|write-capable scaffold|mcp__chirality__scaffold|"
                      r"/v1/projects/\{id\}/scaffold|RuntimeService\.scaffold",
}
CODE_PATTERNS = [
    "/api/working-root/scope", "scanProjectScopes", "useDeliverables", "DeliverablesProvider", "legacy={",
    "legacyHref", "'/workbench'", "'/pipeline'", "mergeMatrixTargetIntoCurrentUrl", "DIRECT_ENTRY_ROLE_IDS",
    "isRoleSelectionBlocked", "buildPortalPersonaHref", "buildDirectChatHref", "RoleDirectoryPanel", "AgentMatrix",
    "createTertiarySidebarTabs", "SidebarRightLoopLayout", "LoopTertiaryShell", "PortalLoopShell", "LoopShell",
    "pipelineTab", "workbenchTab", "portalTab", "RENDERER_SECURITY_PROBE_ROUTES", "PACKAGED_RENDERER_ROUTES",
    "ProjectScaffoldPort", "ScaffoldExecutionRootRequest", "ScaffoldExecutionRootResponse",
    "/api/working-root/workflow?", "WorkflowsView", "WorkflowDetail", "workflow-read-contract", "workflow-store",
    "PORTAL, PIPELINE, and WORKBENCH",
]
EXTS = (".ts", ".tsx", ".js", ".mjs")
IMPORT_RX = re.compile(
    r"""(?:import|export)\s[^'";]*?from\s+['"]([^'"]+)['"]|import\s*\(\s*['"]([^'"]+)['"]\s*\)|import\s+['"]([^'"]+)['"]""",
    re.S,
)


def sha256(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def section(lines: list[str], heading: str) -> list[str]:
    out: list[str] = []
    inside = False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip().startswith(heading)
            continue
        if inside:
            out.append(line)
    if not out:
        raise SystemExit(f"unresolved section binding: {heading}")
    return out


def table_rows(lines: list[str], id_pattern: str) -> list[list[str]]:
    rx = re.compile(r"^\|\s*(" + id_pattern + r")\s*\|")
    return [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines if rx.match(line)]


def ids(cell: str, prefix: str) -> list[str]:
    if prefix in ("PKG", "DEL"):
        return re.findall(prefix + r"-\d\d(?:-\d\d)?", cell)
    return re.findall(prefix + r"-\d{3}", cell)


def run_tool(cmd: list[str]) -> int:
    return subprocess.run(cmd, capture_output=True, text=True).returncode


def code_files() -> list[str]:
    out = []
    for base in (SRC, f"{FRONTEND}/electron", f"{FRONTEND}/scripts"):
        for dp, dn, fn in os.walk(base):
            dn[:] = sorted(d for d in dn if d != "node_modules")
            for f in sorted(fn):
                if f.endswith(EXTS):
                    out.append(os.path.join(dp, f))
    return sorted(out)


def resolve(frm: str, spec: str) -> str | None:
    if not spec.startswith("."):
        return None
    base = os.path.normpath(os.path.join(os.path.dirname(frm), spec))
    for cand in [base] + [base + e for e in EXTS] + [os.path.join(base, "index" + e) for e in EXTS]:
        if os.path.isfile(cand):
            return cand
    return None


def is_test(path: str) -> bool:
    return "/__tests__/" in path


def reachability(files: list[str]) -> dict:
    graph = {}
    for f in files:
        deps = set()
        for m in IMPORT_RX.finditer(read(f)):
            r = resolve(f, m.group(1) or m.group(2) or m.group(3))
            if r:
                deps.add(r)
        graph[f] = deps
    product = [f for f in files if not is_test(f) and f.startswith(SRC + "/") or f.startswith(f"{FRONTEND}/electron/")]
    product = sorted(set(f for f in product if not is_test(f)))

    def roots(drop_pages: bool) -> list[str]:
        out = []
        for f in product:
            if f.startswith(f"{SRC}/app/") and os.path.basename(f) in ("page.tsx", "layout.tsx", "not-found.tsx", "route.ts"):
                if drop_pages and any(f.startswith(d) for d in PAGE_DIRS):
                    continue
                out.append(f)
            elif f.startswith(f"{FRONTEND}/electron/"):
                out.append(f)
        return out

    def reach(dropped_edges: set[str], drop_pages: bool) -> set[str]:
        seen: set[str] = set()
        stack = list(roots(drop_pages))
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            for d in graph.get(n, ()):
                if d not in dropped_edges:
                    stack.append(d)
        return seen

    rel = lambda p: os.path.relpath(p, FRONTEND)
    s0 = reach(set(), False)
    s1 = reach(set(LEGACY_SHELLS), False)
    s2 = reach(set(LEGACY_SHELLS) | {DELIVERABLES_PROVIDER}, False)
    s3 = reach(set(LEGACY_SHELLS) | {DELIVERABLES_PROVIDER}, True)

    def importers(mod: str) -> dict:
        tests = sorted(rel(f) for f in files if is_test(f) and mod in graph[f])
        prod = sorted(rel(f) for f in product if mod in graph[f])
        return {"product_importers": prod, "test_importers": tests}

    def delta(a: set[str], b: set[str]) -> list[dict]:
        return [{"module": rel(m), **importers(m)} for m in sorted(a - b)]

    unreached = sorted(set(product) - s0)
    return {
        "method": "Static relative-import graph over frontend/src (tests excluded) and frontend/electron. Roots: every "
                  "app page.tsx, layout.tsx, not-found.tsx and route.ts, and every electron module. A JSX element passed "
                  "as `legacy` counts as an import edge although WovenDialogueRoute never renders it; the scenarios "
                  "remove those edges to show what is reachable only through them.",
        "product_modules": len(product),
        "reachable_S0_actual": len(s0),
        "S1_only_via_discarded_legacy_element": delta(s0, s1),
        "S2_additionally_only_via_DeliverablesProvider": delta(s1, s2),
        "S3_additionally_only_via_workbench_pipeline_pages": delta(s2, s3),
        "unreachable_at_basis_in_scope": [
            {"module": rel(m), **importers(m)} for m in unreached
            if rel(m).startswith(IN_SCOPE_UNREACHED)
        ],
        "unreachable_at_basis_other_count": len([m for m in unreached if not rel(m).startswith(IN_SCOPE_UNREACHED)]),
        "unreachable_at_basis_other": [rel(m) for m in unreached if not rel(m).startswith(IN_SCOPE_UNREACHED)],
    }


def code_references(files: list[str]) -> dict:
    out = {}
    runtime_files = []
    if os.path.isdir(RUNTIME_PACKAGES):
        for dp, dn, fn in os.walk(RUNTIME_PACKAGES):
            dn[:] = sorted(d for d in dn if d not in ("node_modules", "dist"))
            runtime_files += [os.path.join(dp, f) for f in sorted(fn) if f.endswith(EXTS)]
    texts = {f: read(f) for f in files}
    rtexts = {f: read(f) for f in sorted(runtime_files)}
    for pat in CODE_PATTERNS:
        hit = {"product": [], "tests": [], "electron_scripts": [], "runtime": []}
        for f, t in texts.items():
            if pat in t:
                r = os.path.relpath(f, FRONTEND)
                key = "tests" if is_test(f) else ("product" if r.startswith("src/") else "electron_scripts")
                hit[key].append(r)
        hit["runtime"] = [os.path.relpath(f, "projects/chirality-runtime") for f, t in rtexts.items() if pat in t]
        out[pat] = hit
    return out


def legacy_css(files: list[str]) -> dict:
    """Class tokens used by the legacy-only components, and whether any other product module uses them."""
    legacy = [f"{SRC}/components/shell/{n}" for n in
              ("loop-shell.tsx", "portal-loop-shell.tsx", "loop-tertiary-shell.tsx", "sidebar-right-loop-layout.tsx")]
    legacy.append(f"{SRC}/components/portal/agent-matrix.tsx")
    tokens = set()
    for f in legacy:
        for m in re.finditer(r"className=(?:\{[^}]*\}|\"[^\"]*\"|'[^']*')", read(f)):
            for lit in re.findall(r"['\"`]([^'\"`]+)['\"`]", m.group(0)):
                tokens.update(t for t in lit.split() if re.fullmatch(r"[a-z][a-z0-9_-]+", t))
    others = [f for f in files if not is_test(f) and f.startswith(SRC + "/") and f not in legacy]
    other_text = {f: read(f) for f in others}
    css = read(f"{SRC}/app/globals.css")
    out = {}
    for tok in sorted(tokens):
        rx = re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(tok) + r"(?![A-Za-z0-9_-])")
        users = sorted(os.path.relpath(f, FRONTEND) for f, t in other_text.items() if rx.search(t))
        out[tok] = {"other_product_users": users,
                    "globals_css_selector_hits": len(re.findall(r"\." + re.escape(tok) + r"(?![A-Za-z0-9_-])", css))}
    return out


def text_scan(paths: list[str]) -> dict:
    out = {}
    compiled = {k: re.compile(v) for k, v in TEXT_PATTERNS.items()}
    for p in paths:
        hits = []
        for n, line in enumerate(read(p).splitlines(), 1):
            tags = sorted(k for k, rx in compiled.items() if rx.search(line))
            if tags:
                hits.append({"line": n, "tags": tags, "text": line.strip()[:220]})
        if hits:
            out[p] = hits
    return out


def main() -> int:
    if not os.path.isfile(DECOMP):
        print("run from the repository root", file=sys.stderr)
        return 2
    lines = read(DECOMP).splitlines()
    ssow = table_rows(section(lines, "5. SSOW"), r"SOW-\d{3}")
    objectives = table_rows(section(lines, "6. Objectives"), r"OBJ-\d{3}")
    packages = table_rows(section(lines, "7. Packages"), r"PKG-\d\d")
    deliverables = table_rows(section(lines, "8. Deliverables"), r"DEL-\d\d-\d\d")
    ledger = table_rows(section(lines, "9. Scope Ledger"), r"SOW-\d{3}")
    decisions = table_rows(section(lines, "12. Decision Log"), r"DEC-\d{3}")

    del_by_id = {r[0]: r for r in deliverables}
    retired = sorted(d for d, r in del_by_id.items() if "[RETIRED" in r[1] or "[RETIRED" in r[4])
    ledger_map = {r[0]: {"status": r[1], "package": r[4], "deliverables": ids(r[5], "DEL"),
                         "objectives": ids(r[6], "OBJ")} for r in ledger}
    del_scope = {d: ids(r[6], "SOW") for d, r in del_by_id.items()}
    del_obj = {d: ids(r[7], "OBJ") for d, r in del_by_id.items()}

    folders = {}
    for path in sorted(glob.glob(f"{EXEC}/PKG-*/1_Working/DEL-*")):
        m = re.search(r"(DEL-\d\d-\d\d)", os.path.basename(path))
        if m:
            folders[m.group(1)] = path
    declared, found = set(del_by_id), set(folders)

    def state(d: str) -> str:
        m = re.search(r"\*\*Current State:\*\*\s*(\S+)", read(os.path.join(folders[d], "_STATUS.md")))
        return m.group(1) if m else "UNKNOWN"

    all_states = Counter(state(d) for d in folders)

    scope_items = {}
    for s in SCOPE_ITEMS:
        row = ledger_map[s]
        scope_items[s] = {**row, "active_carriers": [d for d in row["deliverables"] if d not in retired]}
    objective_support = {o: sorted(d for d, objs in del_obj.items() if o in objs and d not in retired) for o in OBJECTIVES}
    affected = {d: {"name": del_by_id[d][1], "type": del_by_id[d][3], "envelope": del_by_id[d][8],
                    "covers_scope_items": del_scope[d], "supports_objectives": del_obj[d],
                    "lifecycle": state(d)} for d in AFFECTED}

    # DEL-02-03 REQ-009 and its dependency row.
    sow_0203 = os.path.join(folders["DEL-02-03"], "ScopeOfWork.md")
    req009 = [{"line": n, "text": line.strip()[:260]} for n, line in enumerate(read(sow_0203).splitlines(), 1)
              if "REQ-009" in line]

    dep_rows = []
    rx_dep = re.compile("|".join(TEXT_PATTERNS.values()))
    for reg in sorted(glob.glob(f"{EXEC}/PKG-*/1_Working/DEL-*/Dependencies.csv")):
        with open(reg, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                blob = " ".join(r.get(k) or "" for k in ("TargetName", "TargetLocation", "Statement", "EvidenceQuote", "SourceRef"))
                if r["DependencyID"] in DEP_IDS or rx_dep.search(blob):
                    dep_rows.append({"DependencyID": r["DependencyID"], "From": r["FromDeliverableID"],
                                     "Direction": r["Direction"], "Type": r["DependencyType"],
                                     "Target": r["TargetDeliverableID"] or r["TargetRefID"],
                                     "TargetName": r["TargetName"][:120], "Status": r.get("Status", ""),
                                     "SatisfactionStatus": r.get("SatisfactionStatus", ""),
                                     "Statement": r["Statement"][:220]})

    # Governance and scope texts.
    scope_texts = [DECOMP] + [f"{DOCS}/{n}.md" for n in ("PRD", "SPEC", "PLAN", "TYPES", "DIRECTIVE", "CONTRACT")]
    scope_texts += DECISIONS + [POINTER]
    scope_texts += sorted(glob.glob(f"{EXEC}/PKG-*/1_Working/DEL-*/ScopeOfWork.md"))
    scope_texts += sorted(glob.glob(f"{EXEC}/PKG-*/1_Working/DEL-*/_CONTEXT.md"))

    files = code_files()

    # Registered tools, into a temporary directory; summaries are path-sanitized.
    root = os.getcwd()
    tool = {}
    with tempfile.TemporaryDirectory() as tmp:
        rc = run_tool([sys.executable, "tools/evaluation/audit_structure.py", "--root", EXEC,
                       "--output", f"{tmp}/structure.json", "--variant", "SOFTWARE"])
        with open(f"{tmp}/structure.json", encoding="utf-8") as fh:
            s = json.load(fh)
        tool["audit_structure"] = {"exit": rc, "run_status": s["run_status"], "subject_status": s["subject_status"],
                                   "summary": s["summary"], "issues": s["issues"]}
        rc = run_tool([sys.executable, "tools/coordination/analyze_dep_closure.py", EXEC, "--output-dir", f"{tmp}/closure"])
        with open(f"{tmp}/closure/closure_summary.json", encoding="utf-8") as fh:
            c = json.load(fh)
        tool["analyze_dep_closure"] = {"exit": rc, **{k: v for k, v in c.items()
                                                      if not isinstance(v, (list, dict)) and "time" not in k.lower()
                                                      and "generated" not in k.lower()}}
        rc = run_tool([sys.executable, "tools/validation/validate_decomposition_registers.py", EXEC,
                       "--json", f"{tmp}/registers.json", "--evidence-root", "."])
        with open(f"{tmp}/registers.json", encoding="utf-8") as fh:
            v = json.load(fh)
        tool["validate_decomposition_registers"] = {
            "exit": rc, "skipped": v.get("skipped"), "registers_scanned": v.get("registers_scanned"),
            "dependency_rows": v.get("dependency_rows"), "findings_by_code": v.get("findings_by_code"),
            "error_count": v.get("error_count"), "warning_count": v.get("warning_count"),
            "note": "XRG is skipped because the App carries no Deliverables.csv/ScopeLedger.csv; EVQ-006 reflects "
                    "deliverable-relative EvidenceFile paths (carried convention)."}
    tool = json.loads(json.dumps(tool, sort_keys=True).replace(root + "/", "").replace(root, "."))

    # Reused full audit: its recorded inputs must be byte-identical to the current tree.
    reused_inputs = []
    with open(os.path.join(REUSED_AUDIT, "INPUT_MANIFEST.sha256"), encoding="utf-8") as fh:
        for line in fh:
            h, rest = line.split(None, 1)
            p = rest.split("  #")[0].strip()
            cur = sha256(p) if os.path.isfile(p) else "MISSING"
            reused_inputs.append(cur == h)
    with open(os.path.join(REUSED_AUDIT, "coverage_summary.json"), encoding="utf-8") as fh:
        cov = json.load(fh)

    diff = subprocess.run(["git", "diff", "--quiet", BASIS_COMMIT, "--", APP, f":(exclude){SNAP_REL}"])

    baseline = {
        "run_label": "SCA_APP_012_GROUP1_PRECHANGE",
        "decomp_variant": "SOFTWARE",
        "method": "Pre-change baseline under scope-change method step 5. The latest full audit-decomp run is reused "
                  "because every one of its recorded inputs is byte-identical to this basis; it is complemented by "
                  "the registered structure, dependency-closure and register tools, a static import-reachability "
                  "analysis of the frontend, and a line-level scan of the scope and governance texts.",
        "basis_commit": BASIS_COMMIT,
        "governed_inputs_identical_to_basis": diff.returncode == 0,
        "decomposition_path": DECOMP,
        "decomposition_sha256": sha256(DECOMP),
        "companion_register_path": REGISTER,
        "companion_register_sha256": sha256(REGISTER),
        "scope_change_pointer_sha256": sha256(POINTER),
        "active_snapshot": "execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/",
        "accepted_project_dag": None,
        "reused_full_audit": {
            "path": REUSED_AUDIT,
            "inputs_recorded": len(reused_inputs),
            "inputs_identical": sum(reused_inputs),
            "run_status": cov.get("run_status"),
            "closure_readiness": cov.get("closure_readiness"),
            "repository_topology": cov.get("repository_topology"),
            "ledger_distribution": cov.get("ledger_distribution"),
            "physical_inventory": cov.get("physical_inventory"),
            "lifecycle_distribution": cov.get("lifecycle_distribution"),
            "issue_counts": cov.get("issue_counts"),
            "checks": cov.get("checks"),
        },
        "repository_topology": {"packages": len(packages), "deliverables": len(deliverables),
                                "retired_deliverables": retired, "objectives": len(objectives),
                                "scope_items": len(ssow), "ledger_rows": len(ledger),
                                "highest_decision_log_id": max(r[0] for r in decisions)},
        "ledger_distribution": dict(sorted(Counter(r[1] for r in ledger).items())),
        "forward_coverage": {"declared": len(declared), "found": len(declared & found),
                             "missing_folders": sorted(declared - found)},
        "reverse_coverage": {"folders": len(found), "undeclared_folders": sorted(found - declared)},
        "scope_items_without_deliverable": sorted(s for s, r in ledger_map.items()
                                                  if r["status"] == "IN" and not [d for d in r["deliverables"] if d not in retired]),
        "objectives_without_deliverable": sorted(o[0] for o in objectives
                                                 if not any(o[0] in v for d, v in del_obj.items() if d not in retired)),
        "lifecycle_distribution": dict(sorted(all_states.items())),
        "issued_deliverables": sorted(d for d in folders if state(d) == "ISSUED"),
        "checking_deliverables": sorted(d for d in folders if state(d) == "CHECKING"),
        "affected_deliverables": affected,
        "affected_scope_items": scope_items,
        "objective_active_supporters": objective_support,
        "del_02_03_req_009": {"scope_of_work": sow_0203, "lines": req009},
        "dependency_rows": dep_rows,
        "frontend_reachability": reachability(files),
        "frontend_references": code_references(files),
        "legacy_css_tokens": legacy_css(files),
        "scope_text_hits": text_scan(scope_texts),
        "tools": tool,
    }
    out = os.path.join(SNAP_REL, "Pre_Change_Coverage.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(baseline, fh, indent=2, sort_keys=False, ensure_ascii=False)
        fh.write("\n")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
