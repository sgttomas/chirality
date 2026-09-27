#!/usr/bin/env python3
"""SCA-APP-011 group-3 corrections to the accepted group-2 exact text, and the group-3 finalize path.

Run from the repository root. The group-2 bound evidence (amendment_edits.py,
PREIMAGE_POSTIMAGE.csv, build_amendment_preview.py, Propagation_Plan.md) is not
modified; this file records each disclosed group-3 correction as data and
carries the finalize path that accounts for it. It also records a basis
refresh: a file whose preimage moved on main after group 2 while every
accepted edit still applies unchanged.

  group3_corrections.py --apply [--root DIR]
      Write each correction into the candidate. Refuses unless the file has its
      group-2 candidate hash (PREIMAGE_POSTIMAGE.csv) before, and verifies the
      corrected hash after.

  group3_corrections.py --check [--root DIR]
      Write nothing. Every file in PREIMAGE_POSTIMAGE.csv must have its expected
      group-3 candidate hash: the group-2 candidate hash for unchanged files,
      the refreshed hash for a file whose basis moved (BASIS_REFRESH), and the
      corrected hash for a corrected file (CORRECTIONS).

  group3_corrections.py --finalize --date YYYY-MM-DD --group3-decision PATH [--root DIR]
      After group-3 acceptance only. The same decision gate as
      build_amendment_preview.py --finalize (the SCA-APP-011_GROUP-3_{date}
      folder, the same date, the "accepted" heading). Rechecks every file
      against its expected group-3 candidate hash, then applies only the
      acceptance-conditional edits (E47) from the accepted edit data.

Use this --finalize in place of build_amendment_preview.py --finalize, which
would refuse the corrected file.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.dirname(os.path.dirname(HERE))
G2 = os.path.join(SNAP, "Evidence", "Group2")
CSV_PATH = os.path.join(G2, "PREIMAGE_POSTIMAGE.csv")
DEL0704_SOW = ("projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/"
               "1_Working/DEL-07-04_Status_Transition_API_and_MCP_Tool/ScopeOfWork.md")

# Each correction replaces one exact substring, once, in the group-2 candidate text of one file.
CORRECTIONS = [
    dict(
        id="G3C-01",
        file=DEL0704_SOW,
        corrects_edit="E13",
        old="with each HTTP status expectation restated as the library's `WorkspaceValidationError` code and status.",
        new=("with each HTTP status expectation restated as the thrown workspace error's code and status "
             "(`WorkspaceOperationError` for most refusals, `WorkspaceValidationError` for path validation)."),
        group2_candidate_sha256="7300d7f8ec533cbd6facc7dd882c0c06ad822b689f2f926be749c258e547aec9",
        corrected_candidate_sha256="df03ef53fe679a7e4a4e49f0959c1f49cf8d620afe872da800de55b3385107ba",
        why=("frontend/src/lib/workspace/deliverable-contracts.ts throws WorkspaceOperationError for most refusals "
             "(gate, ruling, amendment and dependency-write refusals, including symlink writes) and "
             "WorkspaceValidationError only for path validation; frontend/src/__tests__/lib/deliverable-contracts.test.ts "
             "accepts either class and asserts code and status."),
    ),
]

# Files whose basis moved on main after group 2, where the accepted edits reapply unchanged.
# The candidate is the new basis plus exactly the accepted edits; only its hash changes.
BASIS_REFRESH = [
    dict(
        id="G3B-01",
        file="projects/chirality-app-dev/docs/SPEC.md",
        basis_commit="4087a4f8c500a84b85dc9e8652b632550ab21a5a",
        group2_preimage_sha256="4c8c9da13736943b8b525a212bac9a6279e58bc5f293d3266bd140b8aae108c2",
        basis_preimage_sha256="41ba57b0a8fa76a80add9f203f0be9289547fe122759412dbf8c8dcbd416da05",
        group2_candidate_sha256="af38a442dc486be6052dec7aa91f087efeea02223f03c6df0d1c3da32fdf94fd",
        group3_candidate_sha256="5a6fcf1577e4d481ad9d25845ac1a1194241cf5c4a696d7da18f8d05946e017f",
        why=("main commits 3d40c0836 and 387b43972 (2026-09-27) rewrote one SPEC paragraph on the recorded-register "
             "read (execution-root resolution), outside every SCA-APP-011 edit and naming no retired route or form; "
             "the accepted SPEC edits E68-E74, E110 and E111 each still occur exactly once and reapply unchanged."),
    ),
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read(root, path):
    full = os.path.join(root, path)
    return open(full, encoding="utf-8").read() if os.path.isfile(full) else None


def expected_hashes():
    rows = {r["File"]: r for r in csv.DictReader(open(CSV_PATH, newline="", encoding="utf-8"))}
    exp = {p: r["CandidateSHA256"] for p, r in rows.items()}
    for r in BASIS_REFRESH:
        exp[r["file"]] = r["group3_candidate_sha256"]
    for c in CORRECTIONS:
        exp[c["file"]] = c["corrected_candidate_sha256"]
    return rows, exp


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--finalize", action="store_true")
    ap.add_argument("--root", default=".")
    ap.add_argument("--date")
    ap.add_argument("--group3-decision")
    args = ap.parse_args()
    root = args.root
    rows, exp = expected_hashes()

    if args.apply:
        by_file: "OrderedDict[str, list]" = OrderedDict()
        for c in CORRECTIONS:
            by_file.setdefault(c["file"], []).append(c)
        for path, items in by_file.items():
            text = read(root, path)
            if text is None or sha(text) != rows[path]["CandidateSHA256"]:
                print(f"refused: {path} does not have its group-2 candidate hash", file=sys.stderr)
                return 1
            for c in items:
                if text.count(c["old"]) != 1:
                    print(f"refused: {c['id']} old text occurs {text.count(c['old'])} times", file=sys.stderr)
                    return 1
                text = text.replace(c["old"], c["new"], 1)
            if sha(text) != exp[path]:
                print(f"refused: {path} corrected hash {sha(text)} != recorded {exp[path]}", file=sys.stderr)
                return 1
            with open(os.path.join(root, path), "w", encoding="utf-8") as fh:
                fh.write(text)
            print("corrected", path, sha(text))
        return 0

    drift = []
    for path, want in exp.items():
        text = read(root, path)
        got = sha(text) if text is not None else "MISSING"
        if got != want:
            drift.append(path)
        if args.check:
            print("OK   " if got == want else "DRIFT", path)
    if args.check:
        print("check:", "FAIL" if drift else f"OK ({len(exp)} files, {len(CORRECTIONS)} correction(s))")
        return 1 if drift else 0

    # --finalize
    b = load("build_amendment_preview", os.path.join(G2, "build_amendment_preview.py"))
    if not (args.date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date)):
        print("--finalize needs --date YYYY-MM-DD", file=sys.stderr)
        return 2
    dec = (args.group3_decision or "").replace(os.sep, "/")
    m = b.GROUP3_DECISION.fullmatch(dec)
    if not m or m.group(1) != args.date:
        print("refused: --group3-decision must be the SCA-APP-011_GROUP-3_{date}/DECISION.md "
              "for the same date as --date", file=sys.stderr)
        return 3
    full = os.path.join(root, dec)
    first = ""
    if os.path.isfile(full):
        first = next((ln.strip() for ln in open(full, encoding="utf-8") if ln.strip()), "")
    if not b.GROUP3_HEADING.match(first + " "):
        print("refused: no accepted SCA-APP-011 group-3 DECISION.md at that path", file=sys.stderr)
        return 3
    if drift:
        print("refused: file differs from the reviewed group-3 candidate:\n  " + "\n  ".join(drift), file=sys.stderr)
        return 1
    edits, _ = b.load_edits()
    by_file = OrderedDict()
    for e in edits:
        if e.get("conditional"):
            by_file.setdefault(e["file"], []).append(e)
    errors: list = []
    out = {}
    for p, items in by_file.items():
        out[p], _ = b.apply_edits(read(root, p), items, args.date, errors, p)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    for p, text in out.items():
        with open(os.path.join(root, p), "w", encoding="utf-8") as fh:
            fh.write(text)
        print("finalized", p, sha(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
