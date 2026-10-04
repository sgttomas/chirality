#!/usr/bin/env python3
"""U9 citation check: every record citation the PR adds to maintained source resolves through the index.

Read-only, standard library only. The Git reads are `diff`, `cat-file` and `rev-parse`, run with
GIT_OPTIONAL_LOCKS=0. The script writes only --out.

Usage:
  python3 check_citations.py --repo <checkout> --base <main SHA> --head <PR head> \
      [--index citations.json] [--package <local package dir>] [--out resolved.md] [--list]

The source set S is `git diff --name-only <base> <head>`, minus execution paths. The script scans
every added line of S's diff for these citation classes:
  record_path      R/I<n>[/...]                        e.g. R/I65/u4_g6_01/QUALIFICATION.md
  review_path      REVIEW_RV<n>[/...]                  e.g. REVIEW_RV77/coverage_producer_01/tests/rv77_pp.rs
  run              RV<n> <run>_<nn> | I<n> <run>_<nn>  e.g. RV92 u6f_01
  generator        <...>/_run_records/<file>           e.g. part2/_run_records/g5_profile.py
  generator_input  profile_tree.json
  rr_line          RR:<line>[–<line>]                  ROOT_RULINGS_V1.md line numbers
  rr_title         RR "<title>" | ROOT_RULINGS_V1 "<title>" (also JSON-escaped)

Each occurrence must match one index entry, by class and token. Each entry used is then verified
at the index's pinned NUM commit:
  - num_paths exist (relative to the index's records_root);
  - copies exist in --package with the recorded sha256;
  - an rr_line lies in the recorded section, whose heading text matches;
  - an rr_title starts the recorded heading.

Exit 1 on any unresolved occurrence or failed verification; exit 0 otherwise. Citations of named
design documents without a path (C1:160, D1 §4.4, BUILD.md §2.1, API.md, STACK_PLAN, ROUTING:98,
COMP:66) are counted and reported, but not resolved by this index: they are report-only.
"""
import argparse, hashlib, json, os, re, subprocess, sys

P = "projects/chirality-piping/"
ap = argparse.ArgumentParser()
ap.add_argument("--repo", required=True); ap.add_argument("--base", required=True); ap.add_argument("--head", required=True)
here = os.path.dirname(os.path.abspath(__file__))
ap.add_argument("--index", default=os.path.join(here, "citations.json"))
ap.add_argument("--package", default=here)
ap.add_argument("--out"); ap.add_argument("--list", action="store_true")
ap.add_argument("--suggest", help="write index entries for unresolved tokens to this JSON file (auto-resolved where unambiguous, else TODO)")
a = ap.parse_args()
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def git(*args, ok=(0,)):
    r = subprocess.run(["git", "-C", a.repo, *args], capture_output=True, env=env)
    if r.returncode not in ok: sys.exit(f"git {' '.join(args)}: {r.stderr.decode(errors='replace')}")
    return r
idx = json.load(open(a.index, encoding="utf-8"))
NUM, R, RR = idx["num_commit"], idx["records_root"], idx["rr_path"]

CLASSES = [
    ("record_path", re.compile(r"(?<![\w/])R/I\d+(?:/[\w.\-]+)*")),
    ("review_path", re.compile(r"(?<![\w/])REVIEW_RV\d+(?:/[\w.\-]+)*")),
    ("run", re.compile(r"\b(?:RV|I)\d{2,3} [a-z][a-z0-9_]*_\d{2}[a-z]?\b")),
    ("generator", re.compile(r"(?:[\w.\-]+/)*_run_records/[\w.\-/]+")),
    ("generator_input", re.compile(r"(?<![\w/.])profile_tree\.json")),
    ("rr_line", re.compile(r"\bRR:\d+(?:[–-]\d+)?")),
    ("rr_title", re.compile(r'\bRR "([^"]+)"|ROOT_RULINGS_V1 \\"(.+?)\\"|ROOT_RULINGS_V1 "([^"\\]+)"')),
]
REPORT_ONLY = re.compile(r"\b(?:C[123]:\d+|C[123] §|D[12] §|D[12]:\d+|BUILD\.md|API\.md|STACK_PLAN|ROUTING:\d+|COMP:\d+)")
def norm_title(t): return t.rstrip("…").rstrip(".").strip()

def tokens(line):
    for cls, rx in CLASSES:
        for m in rx.finditer(line):
            if cls == "rr_title":
                yield cls, norm_title(next(g for g in m.groups() if g))
            else:
                yield cls, m.group(0).rstrip(".")

S = [n for n in git("diff", "--name-only", a.base, a.head, "--", ".", ":!" + P + "execution", ":!execution").stdout.decode().split("\n") if n]
diff = git("diff", "-U0", a.base, a.head, "--", *S).stdout.decode("utf-8", errors="replace") if S else ""
occ, report_only, f, ln = [], 0, None, 0
for line in diff.split("\n"):
    if line.startswith("+++ "): f = line[6:] if line.startswith("+++ b/") else None; continue
    m = re.match(r"@@ -\S+ \+(\d+)(?:,\d+)? @@", line)
    if m: ln = int(m.group(1)); continue
    if line.startswith("+") and f:
        for cls, tok in tokens(line[1:]): occ.append((f, ln, cls, tok))
        report_only += len(REPORT_ONLY.findall(line)); ln += 1

entries = {(e["class"], e["token"]): e for e in idx["citations"]}
unresolved = [o for o in occ if (o[2], o[3]) not in entries]
used = {(o[2], o[3]) for o in occ} & set(entries)
rr_lines = None
def rr_text():
    global rr_lines
    if rr_lines is None: rr_lines = git("cat-file", "blob", f"{NUM}:{RR}").stdout.decode("utf-8").split("\n")
    return rr_lines
def heading_for(n):
    hs = [(i + 1, l[3:]) for i, l in enumerate(rr_text()[:n]) if l.startswith("## ")]
    return hs[-1] if hs else (None, None)
def url(path):
    t = git("cat-file", "-t", f"{NUM}:{path}", ok=(0, 128)).stdout.decode().strip()
    return (f"{idx['github']}/{'tree' if t == 'tree' else 'blob'}/{NUM}/{path}", t)
failed, rows = [], []
for key in sorted(used):
    e = entries[key]; out = []
    for p in e.get("num_paths", []):
        u, t = url(f"{R}/{p}")
        if t not in ("blob", "tree"): failed.append((key, f"missing at NUM: {p}"))
        out.append(u)
    if e.get("copy"):
        fp = os.path.join(a.package, e["copy"])
        if not os.path.isfile(fp) or hashlib.sha256(open(fp, "rb").read()).hexdigest() != e["sha256"]:
            failed.append((key, f"copy missing or sha256 mismatch: {e['copy']}"))
        out.append(f"package: {e['copy']}")
    if key[0] in ("rr_line", "rr_title"):
        hl = e["heading_line"]; text = rr_text()
        if not text[hl - 1].startswith("## ") or text[hl - 1][3:] != e["heading"]:
            failed.append((key, f"heading at RR:{hl} differs"))
        if key[0] == "rr_line":
            lo = int(re.findall(r"\d+", key[1])[0])
            if heading_for(lo)[0] != hl: failed.append((key, f"RR line {lo} is not in section {hl}"))
        elif not e["heading"].startswith(key[1]):
            failed.append((key, "title is not the heading's prefix"))
        out.append(f"{idx['github']}/blob/{NUM}/{RR}#L{hl} — \"{e['heading']}\"")
    rows.append((key, out))
for o in unresolved: print(f"UNRESOLVED {o[0]}:{o[1]} [{o[2]}] {o[3]}")
if a.suggest:
    sug, seen = [], set()
    heads = [(i + 1, l[3:]) for i, l in enumerate(rr_text()) if l.startswith("## ")]
    def exists(p): return git("cat-file", "-t", f"{NUM}:{R}/{p}", ok=(0, 128)).stdout.decode().strip() in ("blob", "tree")
    for f_, l_, c, t in unresolved:
        if (c, t) in seen: continue
        seen.add((c, t)); e = {"class": c, "token": t, "first_seen": f"{f_}:{l_}"}
        cand = None
        if c == "record_path": cand = [t[2:]]
        elif c == "review_path": cand = [t]
        elif c == "run":
            who, run = t.split(); cand = [("REVIEW_" + who if who.startswith("RV") else who) + "/" + run]
        if cand and all(exists(p) for p in cand): e["num_paths"] = cand
        elif c == "rr_line":
            hl, h = heading_for(int(re.findall(r"\d+", t)[0])); e.update(heading_line=hl, heading=h)
        elif c == "rr_title" and len([h for h in heads if h[1].startswith(t)]) == 1:
            hl, h = next(h for h in heads if h[1].startswith(t)); e.update(heading_line=hl, heading=h)
        else: e["TODO"] = "resolve by hand"
        sug.append(e)
    json.dump(sug, open(a.suggest, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"suggested {len(sug)} entries, {sum('TODO' in e for e in sug)} TODO -> {a.suggest}")
for k, why in failed: print(f"FAILED {k[0]} {k[1]!r}: {why}")
unused = sorted(set(entries) - used)
print(f"occurrences {len(occ)}; distinct {len({(o[2], o[3]) for o in occ})}; unresolved {len(unresolved)}; "
      f"verification failures {len(failed)}; unused index entries {len(unused)}; report-only design-doc citations {report_only}")
for k in unused: print(f"  unused: {k[0]} {k[1]!r}")
if a.list:
    for o in occ: print(f"  {o[0]}:{o[1]}\t{o[2]}\t{o[3]}")
if a.out:
    with open(a.out, "w", encoding="utf-8") as w:
        w.write(f"# Resolved citations (NUM {NUM})\n\n| Class | Token | Resolves to |\n|---|---|---|\n")
        for (c, t), out in rows: w.write(f"| {c} | `{t}` | {'<br>'.join(out)} |\n")
print("RESULT", "PASS" if not unresolved and not failed else "FAIL")
sys.exit(0 if not unresolved and not failed else 1)
