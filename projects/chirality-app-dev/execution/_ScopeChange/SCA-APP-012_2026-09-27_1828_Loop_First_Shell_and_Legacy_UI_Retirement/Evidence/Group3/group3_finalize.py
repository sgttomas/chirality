#!/usr/bin/env python3
"""SCA-APP-012 group-3 finalize path: apply the acceptance-conditional edits exactly.

Run from the repository root, after checkpoint group 3 is accepted and its
decision folder is committed:

    group3_finalize.py --date YYYY-MM-DD --owner-act TEXT --utc STAMP
                       [--root DIR] [--dry-run]

    group3_finalize.py --render     write Evidence/Group3/STATUS_RECORDS_POSTIMAGE.md
    group3_finalize.py --check      that file equals the rendering; templates well formed

The finalize mode refuses (exit 3) unless all of these hold in ROOT:
  - --date is YYYY-MM-DD and
    `_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_{date}/DECISION.md`
    exists, its first line starts `# SCA-APP-012 checkpoint group 3 — accepted`,
    and it contains the line `> {owner act}` verbatim;
  - `_ScopeChange/SCA-APP-012_GROUP-2_AUTHORIZED.md` exists;
  - --utc is a `YYYYMMDDTHHMMSSZ` stamp (the `_PostAcceptanceValidation/`
    record's suffix).
It refuses (exit 1) unless every before-state holds:
  - the 12 edited files have their recorded group-2 candidate hashes
    (`Evidence/Group2/PREIMAGE_POSTIMAGE.csv`), so E26 is not yet applied;
  - `_LATEST.md` has SHA-256 LATEST_BEFORE (it names SCA-APP-011);
  - `Brief.md` line 3 starts with BRIEF_BEFORE_PREFIX;
  - `Decision_Log.md` has exactly one line starting with G3_BEFORE_PREFIX;
  - `Handoff_State.md` starts with HANDOFF_BEFORE_HEADING.
Then it writes, and nothing else:
  1. E26 into the decomposition ({APPLICATION_DATE} = --date), through the
     group-2 edit data (`build_amendment_preview.apply_edits`);
  2. `_LATEST.md` = `Evidence/Group3/LATEST_POSTIMAGE.md` with {APPLICATION_DATE};
  3. `Brief.md` line 3 = BRIEF_AFTER, `Decision_Log.md` G3 line = G3_AFTER;
  4. `Handoff_State.md` = `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md` with
     {APPLICATION_DATE}, {OWNER_ACT_VERBATIM} and {UTC}.
It prints every written file's SHA-256; --dry-run prints them and writes
nothing. A rerun is refused because the before-states no longer hold.

This tool makes no git call, so no git environment can open its gate; the
gate is the committed group-3 decision folder and the group-2 pointer in ROOT.
It does not write the decision folder, the `_PostAcceptanceValidation/` record
or any code, and it does not merge.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.dirname(os.path.dirname(HERE))
G2 = os.path.join(SNAP, "Evidence", "Group2")
SC = "projects/chirality-app-dev/execution/_ScopeChange"
SNAP_REL = f"{SC}/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement"
POINTER2 = f"{SC}/SCA-APP-012_GROUP-2_AUTHORIZED.md"
LATEST = f"{SC}/_LATEST.md"
BRIEF = f"{SNAP_REL}/Brief.md"
DLOG = f"{SNAP_REL}/Decision_Log.md"
HANDOFF = f"{SNAP_REL}/Handoff_State.md"
LATEST_TEMPLATE = os.path.join(HERE, "LATEST_POSTIMAGE.md")
HANDOFF_TEMPLATE = os.path.join(HERE, "HANDOFF_STATE_POSTIMAGE.md")
STATUS_DOC = os.path.join(HERE, "STATUS_RECORDS_POSTIMAGE.md")
LATEST_BEFORE = "904c1bd6fc30b4293b7da78aa52268142c08d69bfe71b3ea8812c56762185637"
HEADING = "# SCA-APP-012 checkpoint group 3 — accepted"
HANDOFF_BEFORE_HEADING = "# SCA-APP-012 — Handoff State (group-3 CANDIDATE)\n"
BRIEF_BEFORE_PREFIX = "**Status:** `CHECKPOINT_GROUP_2_ACCEPTED` — "
G3_BEFORE_PREFIX = "| G3 | — | Checkpoint group 3 | "
GROUP1 = ('"Accept SCA-APP-012 group 1: R-b, W-b, P-keep (keeping the two pages, as recommended), defaults."; '
          '`../checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`')
GROUP2 = '"Accept SCA-APP-012 group 2: T-a, Q-a."; `../checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`'
BRIEF_AFTER = (
    "**Status:** `CHECKPOINT_GROUP_3_ACCEPTED` — the owner accepted checkpoint group 1 on 2026-09-27 (" + GROUP1
    + "), checkpoint group 2 on 2026-09-27 (" + GROUP2 + ") and checkpoint group 3 on {APPLICATION_DATE} "
    "(\"{OWNER_ACT_VERBATIM}\"; `../checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/`). Revision 4 of "
    "this brief is bound at SHA-256 `3924974af3cd4ffe81169b6f8654657e9e880181d8a217747158255ad8c56d49` (the bytes "
    "before this status line changed). This folder is the active snapshot named by `_LATEST.md`.")
G3_AFTER = (
    "| G3-ACCEPT | {APPLICATION_DATE} | Checkpoint group 3 | \"{OWNER_ACT_VERBATIM}\" | Audited poststate accepted "
    "with the code candidate (Q-a); E26, `_LATEST.md` and these records applied by `Evidence/Group3/group3_finalize.py` "
    "as listed in `Evidence/Group3/ACCEPTANCE_CONDITIONAL_EDITS.csv` | "
    "`checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/` |")


def sha_text(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def load(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read(root: str, rel: str) -> str | None:
    p = os.path.join(root, rel)
    return open(p, encoding="utf-8").read() if os.path.isfile(p) else None


def fill(text: str, date: str, act: str = "", utc: str = "") -> str:
    return text.replace("{APPLICATION_DATE}", date).replace("{OWNER_ACT_VERBATIM}", act).replace("{UTC}", utc)


def render_status_doc() -> str:
    return (
        "# SCA-APP-012 — Post-acceptance status records (exact post-images)\n\n"
        "These are acceptance-conditional items 4 and 5 in `ACCEPTANCE_CONDITIONAL_EDITS.csv`. None of these edits "
        "is applied before group-3 acceptance. `Evidence/Group3/group3_finalize.py` applies them, together with E26 "
        "and `_LATEST.md`, and this file is rendered from its constants (`--render`; `--check` confirms it).\n\n"
        "**Slot rule.** Three slots are filled, and nothing else changes.\n"
        "- `{APPLICATION_DATE}` is the date of the group-3 decision folder "
        "`checkpoint_snapshots/SCA-APP-012_GROUP-3_{APPLICATION_DATE}/`.\n"
        "- `{OWNER_ACT_VERBATIM}` is the owner's words exactly as quoted (after `> `) in that folder's "
        "`DECISION.md`. Any `\"` inside them is kept.\n"
        "- `{UTC}` (Handoff_State.md only) is the suffix of `_PostAcceptanceValidation/SCA-APP-012_{UTC}/`.\n\n"
        "These post-images fit a plain acceptance of this package. If the owner amends or returns group 3, they do "
        "not apply, and the records return to the owner's act.\n\n"
        "## 1. `Brief.md`, line 3 (status line)\n\n"
        f"Before: the line starting with `{BRIEF_BEFORE_PREFIX.strip()}` (the group-2 status line; its wording after "
        "that prefix may be updated while the candidate is integrated).\n\n"
        "After (exact line):\n\n```text\n" + BRIEF_AFTER + "\n```\n\n"
        "## 2. `Decision_Log.md`, the G3 row\n\n"
        f"Before: the one line starting with `{G3_BEFORE_PREFIX.strip()}`.\n\n"
        "After (exact line):\n\n```text\n" + G3_AFTER + "\n```\n\n"
        "## 3. `Handoff_State.md`\n\n"
        f"Before: a file whose first line is `{HANDOFF_BEFORE_HEADING.strip()}`.\n\n"
        "After: the whole file replaced by `Evidence/Group3/HANDOFF_STATE_POSTIMAGE.md` with the three slots "
        "filled.\n")


def plan(root: str, date: str, act: str, utc: str, errors: list) -> dict:
    b = load("build_amendment_preview", os.path.join(G2, "build_amendment_preview.py"))
    edits = load("amendment_edits", os.path.join(G2, "amendment_edits.py")).EDITS
    rows = list(csv.DictReader(open(os.path.join(G2, "PREIMAGE_POSTIMAGE.csv"), newline="", encoding="utf-8")))
    out: dict = {}
    for r in rows:
        cur = read(root, r["File"])
        if cur is None or sha_text(cur) != r["CandidateSHA256"]:
            errors.append(f"not the reviewed candidate (or E26 already applied): {r['File']}")
    cond = [e for e in edits if e.get("conditional")]
    for f in sorted({e["file"] for e in cond}):
        cur = read(root, f) or ""
        text, _ = b.apply_edits(cur, [e for e in cond if e["file"] == f], date, errors, f)
        out[f] = text
    latest = read(root, LATEST)
    if latest is None or sha_text(latest) != LATEST_BEFORE:
        errors.append(f"{LATEST} is not the SCA-APP-011 pointer {LATEST_BEFORE[:12]}…")
    out[LATEST] = fill(open(LATEST_TEMPLATE, encoding="utf-8").read(), date)
    brief = read(root, BRIEF) or ""
    lines = brief.split("\n")
    if len(lines) < 3 or not lines[2].startswith(BRIEF_BEFORE_PREFIX):
        errors.append(f"{BRIEF} line 3 is not the group-2 status line")
    else:
        lines[2] = fill(BRIEF_AFTER, date, act)
        out[BRIEF] = "\n".join(lines)
    dlog = read(root, DLOG) or ""
    dl = dlog.split("\n")
    hits = [i for i, ln in enumerate(dl) if ln.startswith(G3_BEFORE_PREFIX)]
    if len(hits) != 1:
        errors.append(f"{DLOG}: {len(hits)} G3 rows awaiting the owner (expected 1)")
    else:
        dl[hits[0]] = fill(G3_AFTER, date, act)
        out[DLOG] = "\n".join(dl)
    hand = read(root, HANDOFF) or ""
    if not hand.startswith(HANDOFF_BEFORE_HEADING):
        errors.append(f"{HANDOFF} is not the group-3 candidate handoff")
    out[HANDOFF] = fill(open(HANDOFF_TEMPLATE, encoding="utf-8").read(), date, act, utc)
    left = [p for p, t in out.items() if re.search(r"\{(APPLICATION_DATE|OWNER_ACT_VERBATIM|UTC)\}", t)]
    errors += [f"unfilled slot in {p}" for p in left]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--render", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--owner-act")
    ap.add_argument("--utc")
    ap.add_argument("--root", default=".")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.render:
        open(STATUS_DOC, "w", encoding="utf-8").write(render_status_doc())
        print(os.path.relpath(STATUS_DOC))
        return 0
    if args.check:
        bad = []
        if not os.path.isfile(STATUS_DOC) or open(STATUS_DOC, encoding="utf-8").read() != render_status_doc():
            bad.append("STATUS_RECORDS_POSTIMAGE.md differs from the rendering of group3_finalize.py")
        for p in (LATEST_TEMPLATE, HANDOFF_TEMPLATE):
            if "{APPLICATION_DATE}" not in open(p, encoding="utf-8").read():
                bad.append(f"{os.path.basename(p)} carries no {{APPLICATION_DATE}} slot")
        for b in bad:
            print(b)
        print("check:", "FAIL" if bad else "OK")
        return 1 if bad else 0

    root = args.root
    if not (args.date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date)):
        print("refused: --date YYYY-MM-DD is required", file=sys.stderr)
        return 3
    if not (args.utc and re.fullmatch(r"\d{8}T\d{6}Z", args.utc)):
        print("refused: --utc YYYYMMDDTHHMMSSZ is required", file=sys.stderr)
        return 3
    act = args.owner_act or ""
    dec = f"{SC}/checkpoint_snapshots/SCA-APP-012_GROUP-3_{args.date}/DECISION.md"
    text = read(root, dec)
    first = next((ln.strip() for ln in (text or "").split("\n") if ln.strip()), "")
    if text is None or not (first == HEADING or re.match(re.escape(HEADING) + r"[ .,;…]", first)):
        print(f"refused: no accepted group-3 DECISION.md at {dec}", file=sys.stderr)
        return 3
    if not act or f"> {act}" not in text.split("\n"):
        print("refused: --owner-act must equal a `> ` quoted line of that DECISION.md, verbatim", file=sys.stderr)
        return 3
    if not os.path.isfile(os.path.join(root, POINTER2)):
        print(f"refused: {POINTER2} is absent", file=sys.stderr)
        return 3
    errors: list = []
    out = plan(root, args.date, act, args.utc, errors)
    if errors:
        print("refused:\n  " + "\n  ".join(errors), file=sys.stderr)
        return 1
    for p, t in out.items():
        print(("would write" if args.dry_run else "wrote"), p, sha_text(t))
        if not args.dry_run:
            with open(os.path.join(root, p), "w", encoding="utf-8") as fh:
                fh.write(t)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
