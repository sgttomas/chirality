#!/usr/bin/env python3
"""Dry-run validation of the SCA-APP-012 group-2 postimage (read-only).

Run from the repository root. It builds the postimage of every edited file in
memory (and, for Scopes of Work, in a temporary copy of the deliverable folder)
with {APPLICATION_DATE} filled by a placeholder date. Then it checks:

  1. every edit's `old` passage occurs exactly once, in sequence (builder plan);
     markdown table rows touched by an edit keep their pipe count;
  2. every edited ScopeOfWork.md still validates under
     tools/scope_of_work/validate_scope_of_work.py (exit code before and after);
  3. every edited paragraph that names a retired item carries an SCA-APP-012
     marker;
  4. every retired item is named, with an SCA-APP-012 marker in the same
     paragraph, somewhere in the postimage, and the retired routes are gone
     from the PRD §9.2 and SPEC §17.2 tables;
  5. every register row has at least one edit or is listed as carried;
  6. across every deliverable ScopeOfWork.md and _CONTEXT.md under
     PKG-*/1_Working and the decomposition, PRD, SPEC, PLAN, DIRECTIVE and
     TYPES (postimage where edited, current bytes otherwise), no line names a
     retired item or keeps the loop-first UI or a later App-side scaffold entry
     as a current obligation, unless the line carries an SCA-APP-012 marker,
     it lies inside an SCA-APP-012 controlling section, or it is one of the
     historical passages listed in HISTORICAL with its reason. Units are table
     rows and list items with their wrapped continuation lines, or whole prose
     paragraphs. The same sweep over the current bytes is reported for scale.

It writes Evidence/Group2/POSTIMAGE_VALIDATION.md and never modifies the tree.
"""
from __future__ import annotations

import csv
import glob
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.dirname(os.path.dirname(HERE))
REPORT = os.path.join(HERE, "POSTIMAGE_VALIDATION.md")
PLACEHOLDER = "2099-01-01"
MARK = "SCA-APP-012"
CONTROLLING = "## SCA-APP-012 Current Contract (Controlling)"
APP = "projects/chirality-app-dev"

# Names of retired items (routes, modules, symbols, requirement) as they appear in text.
RETIRED = re.compile(
    r"/api/working-root/scope\b|/api/working-root/workflow(?![-\w])|DeliverablesProvider|deliverables-provider|"
    r"agent-matrix-(?:cells|launch)|components/portal/agent-matrix|agent-matrix\.tsx|"
    r"(?<![\w-])loop-shell\.tsx|portal-loop-shell|loop-tertiary-shell|sidebar-right-loop-layout|tertiary-sidebar-tabs|"
    r"legacyHref|\?legacy=1|workflows-view|workflow-detail|woven-workflows|ProjectScaffoldPort|DEL-02-03-REQ-009")
# Wording that keeps the loop-first UI, or a later App-side scaffold entry, as a current obligation.
OBLIGATION = re.compile(
    r"loop-first (?:UI|implementation|compatibility|shell|launch|route-state)|live loop-first|active loop-first|"
    r"existing loop-first|loop-first and matrix UI|(?:existing|old|current) UI remain|"
    r"App-side (?:scaffold )?entry|later governed write/path-hook surface|"
    r"routeable deliverable rows|operator routing|route (?:targets|consumers)|dispatch preselection")

# Every retired item must be named with an SCA-APP-012 marker in the same paragraph somewhere in the postimage.
ITEMS = {
    "loop-shell.tsx": r"(?<![\w-])loop-shell\.tsx",
    "portal-loop-shell.tsx": r"portal-loop-shell\.tsx",
    "loop-tertiary-shell.tsx": r"loop-tertiary-shell\.tsx",
    "sidebar-right-loop-layout.tsx": r"sidebar-right-loop-layout\.tsx",
    "tertiary-sidebar-tabs.tsx": r"tertiary-sidebar-tabs\.tsx",
    "role-directory panel agent-matrix.tsx": r"components/portal/agent-matrix\.tsx",
    "legacy prop": r"`legacy` prop",
    "?legacy=1 link (legacyHref)": r"`legacyHref`",
    "agent-matrix-cells.ts": r"agent-matrix-cells\.ts",
    "agent-matrix-launch.ts": r"agent-matrix-launch\.ts",
    "DeliverablesProvider": r"DeliverablesProvider",
    "/api/working-root/scope": r"/api/working-root/scope",
    "workflows-view.tsx": r"workflows-view\.tsx",
    "workflow-detail.tsx": r"workflow-detail\.tsx",
    "/api/working-root/workflow": r"/api/working-root/workflow(?![-\w])",
    "DEL-02-03-REQ-009": r"DEL-02-03-REQ-009",
    "loop-first UI (decision record)": r"loop-first (?:compatibility )?UI",
    "no App-side scaffold entry": r"[Nn]o App-side scaffold entry",
    "ProjectScaffoldPort retired": r"ProjectScaffoldPort",
}

# Historical passages that name a retired item or loop-first wording and stay unchanged, with the reason.
HISTORICAL = [
    (f"{APP}/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/"
     "DEL-07-02_Execution_Root_Scaffolding_from_Decomposition/ScopeOfWork.md",
     "- **APP-R058:** The scaffold must compose on the current ProjectScaffoldPort/501",
     "Closed Task Management record APP-R058 (closed by SCA-APP-011); history, unchanged (Impact Assessment §9)"),
    (f"{APP}/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md",
     "- SCA-APP-004 selects Woven Dialogue with a Work/Agents Coordination Panel",
     "SCA-APP-004 §13 note kept as history; the new SCA-APP-012 §13 note (E23) says it ends that compatibility period"),
    (f"{APP}/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/"
     "DEL-02-02_Workbench_and_Pipeline_Selection_UX/ScopeOfWork.md",
     "tertiary forms in the loop-first shell",
     "DEL-02-02 CLM-003 Workbench and Pipeline content, retired as history by its SCA-APP-011 controlling section"),
]


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, f"{name}.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def paragraphs(text: str):
    return re.split(r"\n\s*\n", text)


ITEM_START = re.compile(r"^(?:> ?)*(?:\||[-*] |\d+\. |#)")


def units(text: str):
    """Yield (first line number, text) units: a table row or list item with its wrapped
    continuation lines, or a whole prose paragraph (hard-wrapped prose is one unit)."""
    out, cur, start = [], [], 0
    for n, ln in enumerate(text.split("\n"), 1):
        if not ln.strip():
            if cur:
                out.append((start, "\n".join(cur)))
            cur = []
            continue
        continuation = ln.startswith((" ", "\t")) and not ITEM_START.match(ln.lstrip())
        if cur and (continuation or not ITEM_START.match(ln) and not ITEM_START.match(cur[0])):
            cur.append(ln)
            continue
        if cur:
            out.append((start, "\n".join(cur)))
        cur, start = [ln], n
    if cur:
        out.append((start, "\n".join(cur)))
    return out


def controlling_blocks(text: str):
    """The body of every SCA-APP-012 controlling section (heading to the next level-2 heading)."""
    blocks, pos = [], text.find(CONTROLLING)
    while pos != -1:
        end = text.find("\n## ", pos + len(CONTROLLING))
        blocks.append(text[pos:end if end != -1 else len(text)])
        pos = text.find(CONTROLLING, pos + 1)
    return blocks


def main() -> int:
    edits_mod = load("amendment_edits")
    edits, carried = edits_mod.EDITS, edits_mod.CARRIED_BY
    builder = load("build_amendment_preview")
    results, errors = builder.plan(edits, PLACEHOLDER)
    lines = ["# SCA-APP-012 group-2 postimage validation\n\n",
             f"Dry run with `{{APPLICATION_DATE}}` = `{PLACEHOLDER}` (placeholder). Nothing in the tree is modified.\n\n"]
    failures = list(errors)
    lines.append(f"1. Edits applied in sequence: {sum(len(r['edits']) for r in results.values())} in "
                 f"{len(results)} files; `old` passages not found exactly once: {len(errors)}.\n")

    table_checks = 0
    for path, r in results.items():
        for e, _ in r["edits"]:
            old_rows = [ln for ln in e["old"].split("\n") if ln.lstrip("> ").startswith("|")]
            new_rows = [ln for ln in e["new"].replace("{APPLICATION_DATE}", PLACEHOLDER).split("\n")
                        if ln.lstrip("> ").startswith("|")]
            if old_rows and new_rows:
                ref = old_rows[0].count("|") - old_rows[0].count("\\|")
                for ln in new_rows:
                    table_checks += 1
                    if ln.count("|") - ln.count("\\|") != ref:
                        failures.append(f"{e['id']} {path}: table row pipe count {ln.count('|')} != {ref}")
    lines.append(f"   Table rows checked on edited passages: {table_checks}; pipe-count mismatches: "
                 f"{sum('pipe count' in f for f in failures)}.\n")

    # 2. SOW validator on postimages
    sow_results = []
    with tempfile.TemporaryDirectory() as tmp:
        for path, r in results.items():
            if not path.endswith("ScopeOfWork.md"):
                continue
            src_dir = os.path.dirname(path)
            dst_dir = os.path.join(tmp, os.path.basename(src_dir))
            shutil.copytree(src_dir, dst_dir)
            with open(os.path.join(dst_dir, "ScopeOfWork.md"), "w", encoding="utf-8") as fh:
                fh.write(r["post"])
            pre = subprocess.run([sys.executable, "tools/scope_of_work/validate_scope_of_work.py", src_dir],
                                 capture_output=True, text=True)
            post = subprocess.run([sys.executable, "tools/scope_of_work/validate_scope_of_work.py", dst_dir],
                                  capture_output=True, text=True)
            sow_results.append((os.path.basename(src_dir), pre.returncode, post.returncode))
            if post.returncode != pre.returncode or post.returncode != 0:
                failures.append(f"SOW validator {os.path.basename(src_dir)}: pre {pre.returncode}, post "
                                f"{post.returncode}: {post.stdout[-400:]}{post.stderr[-400:]}")
    lines.append("2. `validate_scope_of_work.py` on each edited Scope of Work (exit code before → after):\n\n")
    lines.append("| Deliverable folder | Before | After |\n|---|---|---|\n")
    for name, a, b in sow_results:
        lines.append(f"| `{name}` | {a} | {b} |\n")
    lines.append("\n")

    # 3. edited paragraphs naming a retired item carry the marker
    unmarked = []
    for path, r in results.items():
        for e, _ in r["edits"]:
            if CONTROLLING in e["new"]:
                continue  # the whole inserted section is the SCA-APP-012 statement
            for _, para in units(e["new"]):
                if (RETIRED.search(para) or OBLIGATION.search(para)) and MARK not in para:
                    unmarked.append(f"{e['id']}: {para[:140]!r}")
    lines.append(f"3. Edited paragraphs naming a retired item or loop-first obligation without an SCA-APP-012 "
                 f"marker: {len(unmarked)}.\n")
    for u in unmarked:
        lines.append(f"   - {u}\n")
    failures += [f"unmarked retired reference {u}" for u in unmarked]

    # 4. every retired item is marked somewhere; retired routes gone from the API tables
    post_paras = [p for r in results.values() for _, p in units(r["post"]) if MARK in p]
    post_paras += [b for r in results.values() for b in controlling_blocks(r["post"])]
    missing = [name for name, rx in ITEMS.items() if not any(re.search(rx, p) for p in post_paras)]
    table_left = []
    for path, heading in ((f"{APP}/docs/PRD.md", "### 9.2 Workspace APIs"), (f"{APP}/docs/SPEC.md", "### 17.2 Workspace APIs")):
        post = results[path]["post"]
        sec = post[post.find(heading):]
        sec = sec[:sec.find("\n### ", 4)]
        if re.search(r"^\| `/api/working-root/(scope|workflow)`", sec, re.M):
            table_left.append(path)
    lines.append(f"4. Retired items named with an SCA-APP-012 marker: {len(ITEMS) - len(missing)}/{len(ITEMS)}"
                 f"{' (missing: ' + ', '.join(missing) + ')' if missing else ''}; retired routes left in the PRD §9.2 "
                 f"or SPEC §17.2 table: {len(table_left)}.\n")
    failures += [f"retired item not marked: {m}" for m in missing] + [f"retired route left in table: {t}" for t in table_left]

    # 5. register rows carried
    with open(os.path.join(SNAP, "Amendment_Actions.csv"), encoding="utf-8", newline="") as fh:
        seqs = [int(r["ActionSeq"]) for r in csv.DictReader(fh)]
    edited = {e["seq"] for e in edits}
    orphan = [s for s in seqs if s not in edited and s not in carried]
    unknown = sorted(edited - set(seqs))
    lines.append(f"5. Register rows: {len(seqs)}; rows with their own edits: {len(edited & set(seqs))}; rows "
                 f"carried by other rows' edits: {sorted(set(carried) & set(seqs))}; rows with neither: {orphan}; "
                 f"edits naming an unknown row: {unknown}.\n")
    failures += [f"register row {s} has no edit" for s in orphan] + [f"edit names unknown row {s}" for s in unknown]

    # 6. sweep
    pattern = f"{APP}/execution/PKG-*/1_Working/DEL-*/"
    targets = sorted(glob.glob(pattern + "ScopeOfWork.md") + glob.glob(pattern + "_CONTEXT.md"))
    targets += [f"{APP}/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"]
    targets += [f"{APP}/docs/{n}.md" for n in ("PRD", "SPEC", "PLAN", "DIRECTIVE", "TYPES")]
    uncovered, by_section, historical_hits = [], [], []
    preimage_hits = 0
    for path in targets:
        before = open(path, encoding="utf-8").read()
        preimage_hits += sum(1 for _, u in units(before)
                             if (RETIRED.search(u) or OBLIGATION.search(u)) and MARK not in u
                             and not any(h[0] == path and h[1] in u for h in HISTORICAL))
        text = results[path]["post"] if path in results else open(path, encoding="utf-8").read()
        has_section = CONTROLLING in text
        inside = "\n".join(controlling_blocks(text))
        for n, ln in units(text):
            if not (RETIRED.search(ln) or OBLIGATION.search(ln)) or MARK in ln or ln in inside:
                continue
            hist = next((h for h in HISTORICAL if h[0] == path and h[1] in ln), None)
            if hist:
                historical_hits.append(f"`{os.path.basename(os.path.dirname(path)) or path}` L{n}: {hist[2]}")
            elif has_section:
                by_section.append(f"{path}:{n}: {ln.strip()[:140]}")
            else:
                uncovered.append(f"{path}:{n}: {ln.strip()[:160]}")
    lines.append(f"6. Files swept: {len(targets)} (every deliverable `ScopeOfWork.md` and `_CONTEXT.md`, the "
                 f"decomposition, PRD, SPEC, PLAN, DIRECTIVE and TYPES). Lines naming a retired item or keeping a "
                 f"retired obligation without an SCA-APP-012 marker: {len(uncovered)} uncovered; "
                 f"{len(by_section)} in files whose SCA-APP-012 controlling section governs them; "
                 f"{len(historical_hits)} listed historical passages. The same sweep over the current bytes "
                 f"(before the amendment) finds {preimage_hits} such units, which the edits address.\n")
    for u in uncovered:
        lines.append(f"   - UNCOVERED {u}\n")
    if by_section:
        lines.append("\n   Governed by the file's SCA-APP-012 controlling section (dated history below it):\n\n")
        for u in by_section:
            lines.append(f"   - {u}\n")
    if historical_hits:
        lines.append("\n   Historical passages, unchanged:\n\n")
        for u in historical_hits:
            lines.append(f"   - {u}\n")
    failures += [f"uncovered retired obligation {u}" for u in uncovered]

    lines.append(f"\nResult: {'PASS' if not failures else 'FAIL'}\n")
    for f in failures:
        lines.append(f"- {f}\n")
    open(REPORT, "w", encoding="utf-8").write("".join(lines))
    print("PASS" if not failures else "FAIL", REPORT)
    for f in failures:
        print(" ", f)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
