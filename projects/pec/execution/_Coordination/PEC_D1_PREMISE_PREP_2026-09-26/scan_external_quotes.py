#!/usr/bin/env python3
"""Consequence scan for the D1 premise amendment (provisional D-PEC-105):
which quotations of a target's accepted preimage, held in OTHER files under
projects/pec, stop being verbatim once the candidates land, and which files
anchor a target's preimage SHA-256. Heuristic and informational; it writes
nothing and gates nothing.

For each target in <prep>/targets.json the preimage is <tree>/<target path>
(the pre-act export) and the postimage is <prep>/candidates/<target path>.
Every other text file under <tree>/projects/pec is scanned, except the targets
themselves, the preparation folder and any act run root (--exclude prefixes;
when --prep lies inside --tree it is excluded too). In each file:
  - quoted spans: a double-quoted or backticked span of >= --min (20) characters
    on one line, and each blockquote line (columns 0-3 '>') of >= --min
    characters after the marker is stripped;
  - a span (whitespace collapsed; blockquote markers stripped on both sides)
    that occurs in a target's preimage is classified STALE when it does not
    occur in that target's candidate and KEPT when it does;
  - ANCHOR: a line naming a target's preimage SHA-256 (full, or a 12-hex
    prefix) is listed with whether the full hash or only a prefix appears.
Files under a --history prefix (default projects/pec/execution/_Evaluation/Reviews/)
are reported with the HISTORY- prefix (HISTORY-STALE, HISTORY-KEPT,
HISTORY-ANCHOR): they are snapshots, listed separately.

Output: one line per finding `<CLASS> <KEY> <file>:<line> <span or hash form>`,
STALE and ANCHOR first, then a final SUMMARY line with counts.

Usage: scan_external_quotes.py --tree <pre-act export root> --prep <prep dir>
          [--exclude PREFIX ...] [--history PREFIX ...] [--min N] [--no-kept]
Exit 0 when the scan completes. Read-only; stdlib only.
"""
import argparse, hashlib, json, re, sys
from pathlib import Path

DEFAULT_EXCLUDE = ["projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/",
                   "projects/pec/execution/_Coordination/D1_PREMISE_AMEND_"]
DEFAULT_HISTORY = ["projects/pec/execution/_Evaluation/Reviews/"]
ap = argparse.ArgumentParser()
ap.add_argument("--tree", required=True); ap.add_argument("--prep", required=True)
ap.add_argument("--exclude", nargs="*", default=None, help="path prefixes to skip (replaces the defaults)")
ap.add_argument("--history", nargs="*", default=None, help="path prefixes reported as HISTORY (replaces the default)")
ap.add_argument("--min", type=int, default=20)
ap.add_argument("--no-kept", action="store_true", help="count KEPT spans but do not list them")
a = ap.parse_args()
tree, prep = Path(a.tree).resolve(), Path(a.prep).resolve()
excl = list(DEFAULT_EXCLUDE if a.exclude is None else a.exclude)
hist = list(DEFAULT_HISTORY if a.history is None else a.history)
try:
    excl.append(prep.relative_to(tree).as_posix().rstrip("/") + "/")
except ValueError:
    pass
targets = json.loads((prep / "targets.json").read_text(encoding="utf-8"))["targets"]

def norm(s):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    return re.sub(r"\s+", " ", s).strip()

T = []
for t in targets:
    pb = (tree / t["path"]).read_bytes()
    cp = prep / "candidates" / t["path"]
    if not cp.is_file():
        print(f"WARN {t['key']} candidate missing; every span found for it counts as STALE")
    T.append({"key": t["key"], "path": t["path"], "pre": norm(pb.decode("utf-8")),
              "post": norm(cp.read_text(encoding="utf-8")) if cp.is_file() else "",
              "sha": hashlib.sha256(pb).hexdigest()})
tpaths = {t["path"] for t in T}

QRE = re.compile(r'"([^"\n]{%d,})"|`([^`\n]{%d,})`' % (a.min, a.min))
BQ = re.compile(r"^ {0,3}>")
rows = {"STALE": [], "KEPT": [], "ANCHOR": []}
counts = {}
nfiles = 0
for f in sorted((tree / "projects/pec").rglob("*")):
    if not f.is_file() or f.is_symlink():
        continue
    rel = f.relative_to(tree).as_posix()
    if rel in tpaths or any(rel.startswith(x) for x in excl) or "/.git/" in rel or "__pycache__" in rel:
        continue
    try:
        text = f.read_bytes().decode("utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    nfiles += 1
    pre_h = "HISTORY-" if any(rel.startswith(x) for x in hist) else ""
    for ln, line in enumerate(text.splitlines(), 1):
        for t in T:
            if t["sha"][:12] in line:
                form = "full" if t["sha"] in line else "prefix-12"
                rows["ANCHOR"].append(f"{pre_h}ANCHOR {t['key']} {rel}:{ln} {form} {t['sha'][:12]}")
        spans = [m.group(1) or m.group(2) for m in QRE.finditer(line)]
        if BQ.match(line):
            spans.append(line)
        seen = set()
        for sp in spans:
            n = norm(sp)
            if len(n) < a.min or n in seen:
                continue
            seen.add(n)
            for t in T:
                if n in t["pre"]:
                    cls = "KEPT" if n in t["post"] else "STALE"
                    rows[cls].append(f"{pre_h}{cls} {t['key']} {rel}:{ln} {n[:160]!r}")
for cls in ("STALE", "ANCHOR", "KEPT"):
    for r in rows[cls]:
        tag = r.split(" ", 1)[0]
        counts[tag] = counts.get(tag, 0) + 1
        if cls == "KEPT" and a.no_kept:
            continue
        print(r)
order = ["STALE", "ANCHOR", "KEPT", "HISTORY-STALE", "HISTORY-ANCHOR", "HISTORY-KEPT"]
print("SUMMARY files_scanned=%d " % nfiles + " ".join(f"{k.lower()}={counts.get(k, 0)}" for k in order))
