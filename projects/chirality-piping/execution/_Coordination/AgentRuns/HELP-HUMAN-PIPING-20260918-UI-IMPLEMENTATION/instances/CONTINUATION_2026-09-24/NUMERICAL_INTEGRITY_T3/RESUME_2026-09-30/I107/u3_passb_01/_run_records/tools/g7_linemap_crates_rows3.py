"""[I107 U3 copy of round 2's g7_linemap_crates_rows.py: a deleted file maps nothing (no crash), and each key in a
changed hunk is reported as "deleted" (its lines removed with nothing in their place) or "replaced".]
[I107 PR-N copy of SQ's g7_linemap_crates.py. One change: a short key (`lib.rs:N`) that is ambiguous because
several changed files share its basename resolves to the one candidate on which the basis's own TEXT run has a row at
line N (env LINEMAP_ROWS: SQ's G5 point text_budget, keyed at 57c92a7b33); with no row in any candidate (a citation),
to the one candidate with at least N lines. The candidates are every chain-crate file of that basename at OLD, changed or
not; a key resolved to an unchanged file is left as written. Anything else stays ambiguous and unmapped. Each resolution
is reported.]
[I104 SQ copy: CHANGED restricted to crate_dirs.txt; otherwise I65's tool unchanged]
I65 U4 G7: carry the TEXT chain's line-keyed rules from the G6 text basis (1e323058f3) to the
integrated tree (stdlib only; Git reads only, GIT_OPTIONAL_LOCKS=0).

Every production file whose text changed between OLD and NEW is listed (CHANGED; the run fails if
`git diff --name-only` names another non-test .rs file under core/). For each, `git diff -U0`
gives the hunks; an unchanged OLD line maps to its NEW line by the cumulative offset. A key whose
line lies inside a changed hunk is NOT mapped: it is reported, and the script exits non-zero, so
no rule is silently re-pointed. A `file:line:fn` key must still define `fn` at the new line; a
`file:line` site key must carry the same text at the new line. Keys in descriptive fields (why,
evidence, about, reason) are citations and are left as written.
Usage: python3 g7_linemap.py <repo root> <OLD> <NEW> <out dir> <rules json> [<rules json> ...]
"""
import json, os, re, subprocess, sys
repo, old, new, outdir = sys.argv[1:5]
srcs = sys.argv[5:]
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def git(*a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env, check=True).stdout
changed_all = [f[len(P):] for f in git("diff", "--name-only", old, new, "--", P + "core").split("\n") if f.endswith(".rs")]
CHANGED = [f for f in changed_all if "/tests/" not in f and not f.endswith("_tests.rs")]
# I104 SQ: only the TEXT chain's crates (crate_dirs.txt, env LINEMAP_CRATES) are scanned by the chain, so only
# their files are mapped; other crates' same-basename files (core/rules/*/src/lib.rs, SI1b/SI1c) would make
# the short `lib.rs:N` keys ambiguous. A rule key can only name a chain crate's file.
_CR = open(os.environ["LINEMAP_CRATES"]).read().split()
CHANGED = [f for f in CHANGED if any(f.startswith(c + "/") for c in _CR)]
maps, oldtext, newtext = {}, {}, {}
for f in CHANGED:
    hunks = []
    for line in git("diff", "-U0", old, new, "--", P + f).split("\n"):
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            hunks.append((int(m.group(1)), int(m.group(2) or 1), int(m.group(3)), int(m.group(4) or 1)))
    maps[f] = hunks
    try:
        oldtext[f] = git("show", f"{old}:{P}{f}").split("\n")
    except subprocess.CalledProcessError:
        oldtext[f] = []                                     # a file new since OLD: no OLD key can name it
    try:
        newtext[f] = git("show", f"{new}:{P}{f}").split("\n")
    except subprocess.CalledProcessError:
        newtext[f] = []                                     # I107 U3: a file deleted since OLD: no key maps into it
def remap(f, ln):
    off = 0
    for o, oc, n, nc in maps[f]:
        start = o if oc > 0 else o + 1
        if oc > 0 and o <= ln < o + oc:
            return None
        if ln >= start:
            off += nc - oc
    return ln + off
BASES = sorted({os.path.basename(f) for f in CHANGED})
KEY = re.compile(r"((?:W/)|(?:core/[a-z_/]+/src/)|(?:[a-z_]+/src/))?((?:[a-z_]+/)*(?:" + "|".join(re.escape(b) for b in BASES) + r")):(\d+)(?::([A-Za-z_0-9]+))?")
TOKS = ("format!", "write!", "writeln!", "diag(", ".to_string", ".clone", ".into", "String::from", ".to_owned", "Diagnostic", ".push_str", ".join", ".replace", "ok_or", "map_err", ".collect")
report, unmapped, resolved = [], [], []
import gzip
_rows = json.load(gzip.open(os.environ["LINEMAP_ROWS"]) if os.environ["LINEMAP_ROWS"].endswith(".gz") else open(os.environ["LINEMAP_ROWS"]))["rows"]
ROWS = {(r["file"].split("projects/chirality-piping/")[-1], r["line"]) for r in _rows}
ALL_OLD = [f[len(P):] for c in _CR for f in git("ls-tree", "-r", "--name-only", old, "--", P + c).split("\n") if f.endswith(".rs")]
_len = {}
def old_len(f):
    if f not in _len: _len[f] = len(git("show", f"{old}:{P}{f}").split("\n"))
    return _len[f]
def candidates(prefix, rel, W):
    if prefix == "W/":
        full = W + "/" + rel
        return [full[len("core/"):] if False else full] if full in maps or ("core/" + full) in maps else []
    if prefix and prefix.startswith("core/"):
        f = (prefix + rel)
        return [f] if f in maps else []
    tail = (prefix or "") + rel
    return [f for f in CHANGED if f.endswith("/" + tail) or f == tail]
def fix(s, W, ctx):
    def sub(m):
        whole, prefix, rel, ln, name = m.group(0), m.group(1), m.group(2), int(m.group(3)), m.group(4)
        c = candidates(prefix, rel, W)
        if prefix == "W/":
            c = [x for x in [W + "/" + rel] if x in maps]
        hits = []
        for f in c:
            ol = oldtext[f][ln - 1] if ln <= len(oldtext[f]) else ""
            if name:
                if re.search(r"\bfn\s+" + re.escape(name) + r"\b", ol):
                    hits.append(f)
            else:
                hits.append(f)
        if not hits:
            return whole                                   # names an unchanged file (another crate's same basename)
        if len(hits) > 1:
            # every chain-crate file with this basename at OLD, changed or not, is a candidate for a short key
            same = [f for f in ALL_OLD if f.endswith("/" + rel) or f == rel]
            byrow = [f for f in same if (f, ln) in ROWS]
            bylen = [f for f in same if ln <= old_len(f)]
            pick, how = (byrow, "the one file with a TEXT row there at the basis") if byrow else (bylen, "the one file with that line")
            if len(pick) != 1:
                unmapped.append([ctx, whole, "ambiguous: " + ", ".join(hits)]); return whole
            if pick[0] not in hits:
                resolved.append([ctx, whole, pick[0], how + " (unchanged: left as written)"]); return whole
            resolved.append([ctx, whole, pick[0], how])
            hits = pick
        f = hits[0]
        nl = remap(f, ln)
        if nl is None:
            # I107 U3: say whether the line was removed with nothing in its place (a deletion) or replaced
            h = next(((o, oc, n, nc) for o, oc, n, nc in maps[f] if oc > 0 and o <= ln < o + oc), None)
            kind = "deleted" if (not newtext[f] or (h and h[3] == 0)) else "replaced"
            unmapped.append([ctx, whole, f"line {ln} of {f} lies in a changed hunk", kind]); return whole
        nline = newtext[f][nl - 1]
        if name and not re.search(r"\bfn\s+" + re.escape(name) + r"\b", nline):
            unmapped.append([ctx, whole, f"new line {nl} does not define fn {name}"]); return whole
        if not name and oldtext[f][ln - 1].strip() != nline.strip():
            unmapped.append([ctx, whole, f"new line {nl} differs"]); return whole
        out = whole.replace(f":{ln}", f":{nl}", 1)
        if out != whole:
            report.append([ctx, whole, out])
        return out
    return KEY.sub(sub, s)
DESCR = {"why", "evidence", "about", "reason", "note", "source"}
def walk(v, W, ctx, descr=False):
    if isinstance(v, str):
        return v if descr else fix(v, W, ctx)
    if isinstance(v, list):
        return [walk(x, W, ctx) for x in v]
    if isinstance(v, dict):
        return {fix(k, W, ctx + "/key"): walk(x, W, ctx + "/" + k[:40], k in DESCR) for k, x in v.items()}
    return v
os.makedirs(outdir, exist_ok=True)
for src in srcs:
    if src.endswith(".py"):
        # a script's hard-coded fn keys (sens.py's TB_FN_ZERO / branch keys): only its key lines
        lines = open(src).read().split("\n")
        lines = [fix(l, "", os.path.basename(src)) if re.match(r'\s*(ZW|ENVZERO)\s*=|.*TB_FN_ZERO"\]\s*=\s*"', l) else l for l in lines]
        open(os.path.join(outdir, os.path.basename(src)), "w").write("\n".join(lines))
        continue
    data = json.load(open(src))
    W = data.get("W", "") if isinstance(data, dict) else ""
    out = walk(data, W, os.path.basename(src))
    json.dump(out, open(os.path.join(outdir, os.path.basename(src)), "w"), indent=1)
summary = {"old": old, "new": new, "changed_production_rs": CHANGED, "hunks": {f: len(h) for f, h in maps.items()},
           "remapped": len(report), "unmapped": unmapped, "resolved_ambiguous": resolved}
json.dump({"summary": summary, "remapped": report}, open(os.path.join(outdir, "g7_linemap.out.json"), "w"), indent=1)
print(json.dumps(summary, indent=1))
sys.exit(1 if unmapped else 0)
