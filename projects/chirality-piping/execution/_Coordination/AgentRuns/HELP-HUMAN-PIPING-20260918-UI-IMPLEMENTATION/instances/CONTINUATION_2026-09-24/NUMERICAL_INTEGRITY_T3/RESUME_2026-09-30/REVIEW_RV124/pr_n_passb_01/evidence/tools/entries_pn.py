"""RV124: a mechanical check of I107's 25 PR-N entries (delta_reviewed_pn.json).
For each entry: (1) a hunk of `git diff -U0 7eae707bb7 8dd64c1835` (as delta_inventory2.py forms them) has the stored
fingerprint (I65's fp()), and the entry's removed/added lines are that hunk's lines with comment-only and blank lines
dropped (the entries store the code view; M's entry stores a one-line summary, and its hunk is checked in (3));
(2) a row of the reproduced inventory (delta_inventory2.py, main 7eae707bb7 -> 8dd64c1835) carries that fingerprint,
file and class; (3) by attribution:
  C  the removed lines call `hypot`, the added lines call norm2/norm3; #hypot = sum(arity - 1) over the norms; the
     identifier/literal/operator token multisets are equal with hypot/norm2/norm3/crate/correct_norm dropped
     (final_case.rs's two entries are checked as one, since the temporary `xy` is dropped);
  D  removed nothing; every added code line is a declaration of the norm module or an import of norm2/norm3;
  M  the new module: no allocating token in its production part (lines before #[cfg(test)]);
  Q  the qualification test: printed for reading.
Usage: entries_pn.py <reviewed json> <reproduced inventory json> <module text at 8dd64c1835> <repo>"""
import collections, hashlib, json, re, sys
import os, subprocess
rev, inv, mod, repo = sys.argv[1:5]
P = "projects/chirality-piping/"
git = lambda *a: subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"), check=True).stdout
def hunks_of(f):
    out, cur = [], None
    for line in git("diff", "-U0", "7eae707bb7", "8dd64c1835", "--", P + f).split("\n"):
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m: cur = {"minus": [], "plus": []}; out.append(cur); continue
        if cur is not None and line.startswith("-") and not line.startswith("---"): cur["minus"].append(line[1:])
        elif cur is not None and line.startswith("+") and not line.startswith("+++"): cur["plus"].append(line[1:])
    return out
D = json.load(open(rev)); rows = json.load(open(inv))["rows"]
byfp = {r["fingerprint"]: r for r in rows if r.get("fingerprint")}
def fp(rel, minus, plus):
    return hashlib.sha256((rel + "\n" + "\n".join("-" + x.strip() for x in minus) + "\n" + "\n".join("+" + x.strip() for x in plus)).encode()).hexdigest()
def code(l): return re.sub(r'"(\\.|[^"\\])*"', '""', l).split("//")[0]
DROP = {"hypot", "norm2", "norm3", "crate", "correct_norm"}
def toks(lines):
    s = " ".join(code(x) for x in lines)
    return collections.Counter(t for t in re.findall(r"[A-Za-z_][A-Za-z_0-9]*|\d+\.\d+|\d+|[-+*/<>=!]+", s) if t not in DROP)
def arity(lines):
    s = " ".join(code(x) for x in lines); out = []
    for m in re.finditer(r"norm([23])\(", s): out.append(int(m.group(1)))
    return out
DECL = re.compile(r'^(pub mod correct_norm;|mod correct_norm;|#\[path = "\.\./\.\./\.\./solver/frame_kernel/src/correct_norm\.rs"\]|#\[allow\(dead_code\)\]|use open_pipe_stress_frame_kernel::correct_norm::(norm3|norm2|\{norm2, norm3\});)$')
ok_all = True; pair = []
for e in D["entries"]:
    f = e["fingerprint"]; r = byfp.get(f)
    hs = [h for h in hunks_of(e["file"]) if fp(e["file"], h["minus"], h["plus"]) == f]
    cv = lambda L: [x.strip() for x in L if code(x).strip()]
    c1 = len(hs) == 1 and cv(hs[0]["minus"]) == cv(e["removed"]) and (cv(hs[0]["plus"]) == cv(e["added"]) or e["attribution"] == "M")
    c2 = bool(r) and r["file"] == e["file"] and r["class"] == e["class"]
    a = e["attribution"]; c3 = None; note = ""
    if a == "C":
        if e["file"].endswith("final_case.rs"):
            pair.append(e); c3 = True; note = "checked with its pair below"
        else:
            h = sum(code(x).count("hypot(") for x in e["removed"]); ar = arity(e["added"])
            c3 = h > 0 and h == sum(k - 1 for k in ar) and toks(e["removed"]) == toks(e["added"])
            note = f"hypot {h}, norms {ar}"
    elif a == "D":
        added = [x.strip() for x in e["added"] if code(x).strip()]
        c3 = not [x for x in e["removed"] if code(x).strip()] and all(DECL.match(x) for x in added); note = f"{len(added)} declaration line(s)"
    elif a == "M":
        L = open(mod, encoding="utf-8").read().split("\n"); cut = L.index("#[cfg(test)]")
        bad = [i + 1 for i, l in enumerate(L[:cut]) if re.search(r"\b(Vec|String|Box|Rc|Arc|HashMap|BTreeMap)\b|format!|vec!|\.collect\(|\.to_vec\(|\.to_string\(", code(l))]
        c3 = not bad and len(hs) == 1 and hs[0]["plus"] == L[:len(L) - (L[-1] == "")] and not hs[0]["minus"]; note = f"production lines 1-{cut}, allocating tokens {bad}, hunk = whole file {c1 and c3}"
    elif a == "Q":
        c3 = True; note = "read: " + " / ".join(x.strip() for x in e["added"] if x.strip())[:160]
    ok = c1 and c2 and c3; ok_all &= ok
    print(f"{'OK ' if ok else 'BAD'} {a} {e['class']:<18} {e['file'].split('/src/')[-1]}:{e['at_final_basis'].split(':')[-1]}  hunk={c1} row={c2} check={c3}  {note}")
rm = [x for e in pair for x in e["removed"]]; ad = [x for e in pair for x in e["added"]]
h = sum(code(x).count("hypot(") for x in rm); ar = arity(ad)
tr, ta = toks(rm), toks(ad)
extra = tr - ta; missing = ta - tr
ok = h == sum(k - 1 for k in ar) and extra == collections.Counter({"let": 1, "xy": 2, "=": 1}) and not missing
ok_all &= ok
print(f"{'OK ' if ok else 'BAD'} final_case.rs pair: hypot {h}, norms {ar}; tokens only in removed {dict(extra)}, only in added {dict(missing)} (the temporary xy)")
print("entries", len(D["entries"]), "refused", D["refused"], "ALL OK" if ok_all else "NOT ALL OK")
sys.exit(0 if ok_all else 1)
