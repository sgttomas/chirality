#!/usr/bin/env python3
"""Dry-run validation of the SCA-APP-011 group-2 postimage (read-only).

Run from the repository root. It builds the postimage of every edited file in
a temporary copy of the affected deliverable folders and documents, with
{APPLICATION_DATE} filled by a placeholder date. Then it checks:

  1. markdown table rows touched by an edit keep their pipe count;
  2. every edited ScopeOfWork.md still validates under
     tools/scope_of_work/validate_scope_of_work.py;
  3. no edit leaves the retired route or form paths in a sentence that does not
     also carry an SCA-APP-011 marker (on the edited lines only).

It writes Evidence/Group2/POSTIMAGE_VALIDATION.md and never modifies the tree.
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT = os.path.join(HERE, "POSTIMAGE_VALIDATION.md")
PLACEHOLDER = "2099-01-01"


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, f"{name}.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    edits = load("amendment_edits").EDITS
    builder = load("build_amendment_preview")
    results, errors = builder.plan(edits, PLACEHOLDER)
    lines = ["# SCA-APP-011 group-2 postimage validation\n\n",
             f"Dry run with `{{APPLICATION_DATE}}` = `{PLACEHOLDER}` (placeholder). Nothing in the tree is modified.\n\n"]
    failures = list(errors)

    # 1. table pipe counts on touched lines
    table_checks = 0
    for path, r in results.items():
        for e, _ in r["edits"]:
            old_lines, new_lines = e["old"].split("\n"), e["new"].replace("{APPLICATION_DATE}", PLACEHOLDER).split("\n")
            old_rows = [ln for ln in old_lines if ln.lstrip("> ").startswith("|")]
            new_rows = [ln for ln in new_lines if ln.lstrip("> ").startswith("|")]
            if old_rows and new_rows:
                ref = old_rows[0].count("|") - old_rows[0].count("\\|")
                for ln in new_rows:
                    table_checks += 1
                    if ln.count("|") - ln.count("\\|") != ref:
                        failures.append(f"{e['id']} {path}: table row pipe count {ln.count('|')} != {ref}")
    lines.append(f"1. Table rows checked on edited passages: {table_checks}; pipe-count mismatches: "
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
                failures.append(f"SOW validator {os.path.basename(src_dir)}: pre {pre.returncode}, post {post.returncode}: {post.stdout[-400:]}{post.stderr[-400:]}")
    lines.append("2. `validate_scope_of_work.py` on each edited Scope of Work (exit code before → after):\n\n")
    lines.append("| Deliverable folder | Before | After |\n|---|---|---|\n")
    for name, a, b in sow_results:
        lines.append(f"| `{name}` | {a} | {b} |\n")
    lines.append("\n")

    # 3. retired paths on edited lines carry an SCA-APP-011 marker
    retired = re.compile(r"/api/working-root/deliverable/(status|dependencies)|/api/harness/scaffold|"
                         r"pipeline-surface|workbench-surface|lifecycle-gate-fields|deliverable-api\.ts|"
                         r"scaffoldHarnessExecutionRoot|api/working-root/deliverable-contracts\.test\.ts")
    unmarked = []
    for path, r in results.items():
        for e, _ in r["edits"]:
            for para in re.split(r"\n\s*\n", e["new"]):
                if retired.search(para) and "SCA-APP-011" not in para:
                    unmarked.append(f"{e['id']}: {para[:120]!r}")
    lines.append(f"3. Edited paragraphs naming a retired route, form, client module or route test without an "
                 f"SCA-APP-011 marker: {len(unmarked)}.\n")
    for u in unmarked:
        lines.append(f"   - {u}\n")
    failures += [f"unmarked retired reference {u}" for u in unmarked]

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
