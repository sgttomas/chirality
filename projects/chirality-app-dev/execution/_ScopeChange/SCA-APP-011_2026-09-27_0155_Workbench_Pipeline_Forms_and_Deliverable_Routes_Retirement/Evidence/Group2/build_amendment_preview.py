#!/usr/bin/env python3
"""SCA-APP-011 exact amendment: render, check, write the group-3 candidate, finalize.

Run from the repository root. The edit data is `amendment_edits.py`. Each edit
replaces one exact substring that must occur exactly once in the file, as it
stands after the earlier edits to that file. Edits marked `conditional` are the
acceptance-conditional edits; there is one, E47, with the slot
`{APPLICATION_DATE}`.

Three states per file are recorded in `PREIMAGE_POSTIMAGE.csv`:

  Preimage   the current tree (group-2 basis);
  Candidate  every edit except the acceptance-conditional ones (group-3 candidate
             poststate, written before group-3 acceptance per method.md);
  Final      the candidate plus the acceptance-conditional edits. Its hash is
             recorded where it does not depend on the acceptance date.

Modes:

  build_amendment_preview.py
      Check every edit against the current tree and write Amendment_Preview.md
      and PREIMAGE_POSTIMAGE.csv.

  build_amendment_preview.py --check
      Write nothing. Fail on any of: a preimage hash differs from the CSV; the
      CSV rows (files, edit ids, candidate and final hashes) differ from what the
      edit data produces; Amendment_Preview.md differs from the rendering of the
      edit data.

  build_amendment_preview.py --candidate [--root DIR]
      Group-3 preparation, after group-2 acceptance (method.md, checkpoint group
      3 preparation, steps 1-2). Recheck every preimage hash against the CSV,
      write the candidate poststate (no acceptance-conditional edit is applied),
      and verify every written file against the CSV candidate hash. Without
      --root it writes the repository tree and requires the group-2 authority
      pointer `_ScopeChange/SCA-APP-011_GROUP-2_AUTHORIZED.md`; with --root it
      writes a scratch copy rooted at DIR and needs no pointer.

  build_amendment_preview.py --finalize --date YYYY-MM-DD --group3-decision PATH [--root DIR]
      After group-3 acceptance only. PATH must be
      `projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_{date}/DECISION.md`
      with the same date as --date, and its first line must be the heading
      `# SCA-APP-011 checkpoint group 3 — accepted …`. Recheck that every file
      still has its CSV candidate hash, apply only the acceptance-conditional
      edits with {APPLICATION_DATE} = --date, and verify each file against its
      CSV final hash where one is recorded. Pointer moves (`_LATEST.md`) are
      listed in Propagation_Plan.md §6 and are not written by this script.
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
SLOT = "{APPLICATION_DATE}"
CSV_PATH = os.path.join(HERE, "PREIMAGE_POSTIMAGE.csv")
PREVIEW = os.path.join(SNAP, "Amendment_Preview.md")
SCOPE_CHANGE = "projects/chirality-app-dev/execution/_ScopeChange"
GROUP2_POINTER = f"{SCOPE_CHANGE}/SCA-APP-011_GROUP-2_AUTHORIZED.md"
GROUP3_DECISION = re.compile(
    re.escape(SCOPE_CHANGE) + r"/checkpoint_snapshots/SCA-APP-011_GROUP-3_(\d{4}-\d{2}-\d{2})/DECISION\.md")
GROUP3_HEADING = re.compile(r"^# SCA-APP-011 checkpoint group 3 — accepted[ .,;…]")
FIELDS = ["File", "Edits", "ConditionalEdits", "PreimageSHA256", "CandidateSHA256", "FinalSHA256", "FinalRule"]


def load_edits():
    spec = importlib.util.spec_from_file_location("amendment_edits", os.path.join(HERE, "amendment_edits.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.EDITS, mod.CARRIED_BY


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read(root: str, path: str) -> str | None:
    full = os.path.join(root, path)
    return open(full, encoding="utf-8").read() if os.path.isfile(full) else None


def apply_edits(text: str, items, date: str | None, errors: list, path: str, original: str | None = None):
    rendered = []
    for e in items:
        count = text.count(e["old"])
        if count != 1:
            errors.append(f"{e['id']} {path}: old text occurs {count} times (expected 1)")
            continue
        base = original if original is not None else text
        line = base.count("\n", 0, base.find(e["old"])) + 1 if e["old"] in base else None
        new = e["new"].replace(SLOT, date) if date else e["new"]
        text = text.replace(e["old"], new, 1)
        rendered.append((e, line))
    return text, rendered


def plan(edits, date: str | None, root: str = "."):
    """Return per-file original, candidate and final texts.

    `final` fills {APPLICATION_DATE} with `date`; with no date it keeps the slot.
    `post` is kept as an alias of `final` for validate_postimage.py.
    """
    by_file: "OrderedDict[str, list]" = OrderedDict()
    for e in edits:
        by_file.setdefault(e["file"], []).append(e)
    results = OrderedDict()
    errors: list = []
    for path, items in by_file.items():
        original = read(root, path)
        if original is None:
            errors.append(f"{path}: missing")
            continue
        fixed = [e for e in items if not e.get("conditional")]
        cond = [e for e in items if e.get("conditional")]
        candidate, r1 = apply_edits(original, fixed, None, errors, path, original)
        final, r2 = apply_edits(candidate, cond, date, errors, path, original)
        order = {e["id"]: i for i, e in enumerate(items)}
        rendered = sorted(r1 + r2, key=lambda x: order[x[0]["id"]])
        results[path] = dict(original=original, candidate=candidate, final=final, post=final,
                             edits=rendered, conditional=bool(cond), cond_edits=cond)
    return results, errors


def csv_rows(results):
    rows = []
    for path, r in results.items():
        rows.append(dict(
            File=path,
            Edits=";".join(e["id"] for e, _ in r["edits"]),
            ConditionalEdits=";".join(e["id"] for e in r["cond_edits"]),
            PreimageSHA256=sha(r["original"]),
            CandidateSHA256=sha(r["candidate"]),
            FinalSHA256="" if r["conditional"] else sha(r["final"]),
            FinalRule=("candidate plus " + ";".join(e["id"] for e in r["cond_edits"])
                       + " with {APPLICATION_DATE} = date of SCA-APP-011_GROUP-3_{date}")
            if r["conditional"] else "same as candidate",
        ))
    return rows


def fence(text: str) -> str:
    body = text.rstrip("\n")
    return "```text\n" + (body if body else "(nothing: the text is removed)") + "\n```\n"


def render(results, carried) -> str:
    total = sum(len(r["edits"]) for r in results.values())
    cond_ids = [e["id"] for r in results.values() for e in r["cond_edits"]]
    out = [
        "# SCA-APP-011 — Amendment Preview (checkpoint group 2)\n\n",
        "Generated by `Evidence/Group2/build_amendment_preview.py` from `Evidence/Group2/amendment_edits.py` "
        "against the tree at the time of generation. Each edit replaces one exact passage (before → after). "
        f"{total} edits in {len(results)} files. Line numbers are the edit's first line in the current file. "
        "`--check` confirms that this file, the edit data and `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` agree.\n\n",
        "## When the edits are written\n\n",
        "- Group-3 candidate (after group-2 acceptance, before group-3 acceptance): "
        "`build_amendment_preview.py --candidate` rechecks every preimage hash, writes every edit except the "
        f"acceptance-conditional ones ({', '.join(cond_ids)}), and verifies each written file against its "
        "recorded candidate hash. This is the poststate the independent audit and the owner review at group 3.\n",
        "- After group-3 acceptance only: `build_amendment_preview.py --finalize --date YYYY-MM-DD "
        "--group3-decision PATH` rechecks the candidate hashes and applies only the acceptance-conditional edits.\n\n",
        "## Acceptance-conditional edits\n\n",
        "Only one edit depends on the acceptance act: E47 (decomposition Coverage and Telemetry `Revision` and "
        "`Date`), with the slot `{APPLICATION_DATE}`. It is filled with the date of the group-3 decision folder "
        "`_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_{YYYY-MM-DD}/`, whose `DECISION.md` first line "
        "is `# SCA-APP-011 checkpoint group 3 — accepted …`. The finalize step refuses a date that differs from "
        "that folder's date. All other bytes are fixed and their hashes are recorded. The pointer move "
        "(`_LATEST.md` to the accepted SCA-APP-011 snapshot) and the group-3 decision snapshot are listed in "
        "`Propagation_Plan.md` §6.\n\n",
    ]
    if carried:
        out.append("## Rows carried by another row's edit\n\n")
        for seq, ids in carried.items():
            out.append(f"- Register row {seq}: carried by {', '.join(ids)}.\n")
        out.append("\n")
    for path, r in results.items():
        out.append(f"## `{path}`\n\n")
        for e, line in r["edits"]:
            cond = " — acceptance-conditional" if e.get("conditional") else ""
            where = f"L{line}" if line else "after an earlier edit"
            out.append(f"### {e['id']} — register row {e['seq']} — {where}{cond}\n\n")
            out.append("Before:\n\n" + fence(e["old"]) + "\nAfter:\n\n" + fence(e["new"]) + "\n")
    return "".join(out).rstrip("\n") + "\n"


def recorded_rows():
    return {r["File"]: r for r in csv.DictReader(open(CSV_PATH, newline="", encoding="utf-8"))}


def write_files(root: str, texts: dict):
    for path, text in texts.items():
        with open(os.path.join(root, path), "w", encoding="utf-8") as fh:
            fh.write(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--candidate", action="store_true")
    mode.add_argument("--finalize", action="store_true")
    ap.add_argument("--root", default=".")
    ap.add_argument("--date")
    ap.add_argument("--group3-decision")
    args = ap.parse_args()
    edits, carried = load_edits()
    ids = [e["id"] for e in edits]
    if len(ids) != len(set(ids)):
        print("duplicate edit ids", file=sys.stderr)
        return 2
    root = args.root

    if args.check:
        rec = recorded_rows()
        results, errors = plan(edits, None, root)
        bad = list(errors)
        for path, r in rec.items():
            cur = read(root, path)
            if cur is None or sha(cur) != r["PreimageSHA256"]:
                bad.append(f"DRIFT preimage {path}")
        want = {r["File"]: r for r in csv_rows(results)}
        if set(want) != set(rec):
            bad.append(f"CSV files differ from edit data: {sorted(set(want) ^ set(rec))}")
        for path in set(want) & set(rec):
            for field in FIELDS:
                if want[path][field] != rec[path][field]:
                    bad.append(f"CSV {field} differs for {path}")
        current = open(PREVIEW, encoding="utf-8").read() if os.path.isfile(PREVIEW) else ""
        if current != render(results, carried):
            bad.append("Amendment_Preview.md differs from the rendering of amendment_edits.py")
        for b in bad:
            print(b)
        print("check:", "FAIL" if bad else f"OK ({len(rec)} files, {len(ids)} edits)")
        return 1 if bad else 0

    if args.candidate:
        if root == "." and not os.path.isfile(GROUP2_POINTER):
            print(f"refused: {GROUP2_POINTER} is absent (group 2 not accepted)", file=sys.stderr)
            return 3
        rec = recorded_rows()
        results, errors = plan(edits, None, root)
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        if set(results) != set(rec):
            print("refused: CSV files differ from edit data", file=sys.stderr)
            return 1
        drift = [p for p, r in results.items() if sha(r["original"]) != rec[p]["PreimageSHA256"]]
        if drift:
            print("refused: preimage drift:\n  " + "\n  ".join(drift), file=sys.stderr)
            return 1
        write_files(root, {p: r["candidate"] for p, r in results.items()})
        bad = []
        for p in results:
            got = sha(read(root, p))
            ok = got == rec[p]["CandidateSHA256"]
            bad += [] if ok else [p]
            print("candidate", "OK   " if ok else "MISMATCH", p)
        return 1 if bad else 0

    if args.finalize:
        if not (args.date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date)):
            print("--finalize needs --date YYYY-MM-DD", file=sys.stderr)
            return 2
        dec = (args.group3_decision or "").replace(os.sep, "/")
        m = GROUP3_DECISION.fullmatch(dec)
        if not m or m.group(1) != args.date:
            print("refused: --group3-decision must be the SCA-APP-011_GROUP-3_{date}/DECISION.md "
                  "for the same date as --date", file=sys.stderr)
            return 3
        full = os.path.join(root, dec)
        first = ""
        if os.path.isfile(full):
            first = next((ln.strip() for ln in open(full, encoding="utf-8") if ln.strip()), "")
        if not GROUP3_HEADING.match(first + " "):
            print("refused: no accepted SCA-APP-011 group-3 DECISION.md at that path", file=sys.stderr)
            return 3
        rec = recorded_rows()
        drift = []
        for p, r in rec.items():
            cur = read(root, p)
            if cur is None or sha(cur) != r["CandidateSHA256"]:
                drift.append(p)
        if drift:
            print("refused: file differs from the reviewed candidate:\n  " + "\n  ".join(drift), file=sys.stderr)
            return 1
        by_file: "OrderedDict[str, list]" = OrderedDict()
        for e in edits:
            if e.get("conditional"):
                by_file.setdefault(e["file"], []).append(e)
        errors: list = []
        out = {}
        for p, items in by_file.items():
            out[p], _ = apply_edits(read(root, p), items, args.date, errors, p)
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        write_files(root, out)
        for p, text in out.items():
            want = rec[p]["FinalSHA256"]
            print("finalized", p, sha(text), "(no fixed final hash: date slot)" if not want else
                  ("OK" if sha(text) == want else "MISMATCH"))
        return 0

    results, errors = plan(edits, None, root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    with open(PREVIEW, "w", encoding="utf-8") as fh:
        fh.write(render(results, carried))
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(csv_rows(results))
    print(f"{sum(len(r['edits']) for r in results.values())} edits, {len(results)} files: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
