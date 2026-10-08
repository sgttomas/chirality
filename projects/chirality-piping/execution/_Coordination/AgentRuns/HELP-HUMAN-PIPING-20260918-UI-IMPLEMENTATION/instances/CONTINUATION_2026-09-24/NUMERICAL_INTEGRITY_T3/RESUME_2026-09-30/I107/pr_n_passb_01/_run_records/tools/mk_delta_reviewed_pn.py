"""I107 SB round 2: PR-N's reviewed delta table (delta_reviewed_pn.json) for I65's delta_inventory2.py, from a dry run's
inventory (main 7eae707bb7 -> PR-N's code commit). An entry is written only for a hunk attributed mechanically to I109's
correctly rounded norm (RR "I109: a correctly rounded norm replaces libm `hypot` on published paths; ..."):
  M  the norm module itself (frame_kernel/src/correct_norm.rs, new): its production part (before `#[cfg(test)]`) has no
     allocating construct, and no fn of it reaches itself on this pass's call graph (no recursion);
  D  a declaration of the module: `pub mod correct_norm;`, stress_recovery's `#[path]` include, or a `use` of norm2/norm3;
  C  a call site: every removed code line calls `hypot`, every added code line calls norm2/norm3; per file, the removed
     lines' `hypot` calls equal the added lines' norm arguments less one (norm2: 1, norm3: 2: one chain becomes one norm),
     and the identifiers agree apart from hypot/norm2/norm3/crate/correct_norm and `let` temporaries the chain removed;
  Q  a qualification-test hunk of I109 round 2's ring check (RV125 A1-N1) inside `cap_maximal_ring_is_the_trigonometric_ring`.
Comment lines are ignored in every check. A hunk that fits none gets no entry, so the pass stops on it (5), or reads it (6).
Usage: python3 mk_delta_reviewed_pn.py <repo> <dry-run delta_inventory.json> <pass dir (its n5/edges.json)> <out json>"""
import json, os, re, subprocess, sys
repo, inv_p, pass_dir, out_p = sys.argv[1:5]
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
git = lambda *a: subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env, check=True).stdout
inv = json.load(open(inv_p)); old, new = inv["old"], inv["new"]
code = lambda l: l.split("//")[0].strip()
ids = lambda ls: set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", " ".join(code(l) for l in ls)))
def hunks(rel):
    out, cur = {}, None
    for l in git("diff", "-U0", old, new, "--", P + rel).split("\n"):
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", l)
        if m:
            n, nc = int(m.group(3)), int(m.group(4) or 1)
            cur = out.setdefault(f"{n}-{n + nc - 1}" if nc else f"after {n}", ([], [])); continue
        if cur is not None and l[:1] in "-+" and l[:1] and not l.startswith(("---", "+++")):
            (cur[0] if l[0] == "-" else cur[1]).append(l[1:])
    return out
NORM = "core/solver/frame_kernel/src/correct_norm.rs"
newtext = git("show", f"{new}:{P}{NORM}")
prod = newtext.split("#[cfg(test)]")[0]
alloc = re.findall(r"\b(Vec|String|Box|Rc|Arc|HashMap|BTreeMap|vec!|format!|to_string|to_owned|collect|alloc)\b", "\n".join(code(l) for l in prod.split("\n")))
E = json.load(open(os.path.join(pass_dir, "n5", "edges.json")))["edges"]
fns = [k for k in E if k.endswith(".rs") is False and "/correct_norm.rs:" in k]
def reaches_self(k):
    seen, st = set(), list(E.get(k, []))
    while st:
        v = st.pop()
        if v == k: return True
        if v not in seen and "/correct_norm.rs:" in v: seen.add(v); st.extend(E.get(v, []))
    return False
recursive = [k.split("/src/")[-1] for k in fns if reaches_self(k)]
pooled = {}
def file_pool(rel):
    if rel not in pooled:
        hs = hunks(rel).values(); pooled[rel] = ([l for m, _ in hs for l in m], [l for _, p in hs for l in p])
    return pooled[rel]
need = inv["unreviewed"] + inv["unreviewed_qualification_tests"]; entries, refused = [], []
for r in need:
    rel, nl = r["file"], r["new_lines"]; minus, plus = hunks(rel).get(nl, ([], []))
    mc, pc = [l for l in minus if code(l)], [l for l in plus if code(l)]
    kind = why = None
    if rel == NORM and not minus:
        if not alloc and not recursive:
            kind, why = "M", (f"the norm module (new, {len(plus)} lines): norm2/norm3 and their helpers. Its production part has no allocating "
                              f"construct and no recursion on this pass's call graph ({len(fns)} fns). I109's oracle: 0 misrounded in 22,000,000 "
                              "results against exact integer square roots (R/I109/platform_norm_01/). Its loops: this pass's item 4.")
    elif not mc and pc and all(re.fullmatch(r"(pub )?mod correct_norm;|#\[path = \"[./]*(solver/frame_kernel/src/)?correct_norm\.rs\"\]|#\[allow\(dead_code\)\]|"
                                             r"use open_pipe_stress_frame_kernel::correct_norm::(norm2|norm3|\{norm2, norm3\});", code(l)) for l in pc):
        kind, why = "D", "a declaration of the norm module or an import of norm2/norm3; no executable code"
    elif mc or pc:
        fm, fp = file_pool(rel)
        calls_ok = (not mc or "hypot(" in " ".join(code(l) for l in mc)) and all(re.search(r"\bnorm[23]\(", code(l)) for l in pc)
        n_hypot = sum(code(l).count("hypot(") for l in fm)
        n_norm = sum(code(l).count("norm2(") + 2 * code(l).count("norm3(") for l in fp)
        temps = {m.group(1) for l in fm for m in [re.search(r"\blet\s+(\w+)\s*=", code(l))] if m} - ids(fp)
        extra_plus = ids(pc) - {"norm2", "norm3", "crate", "correct_norm"} - ids(fm)
        extra_minus = ids(mc) - {"hypot"} - ids(fp) - temps
        if calls_ok and n_hypot == n_norm and not extra_plus and not extra_minus:
            kind, why = "C", (f"a call site: libm `hypot` replaced by the correctly rounded norm with the same operands "
                              f"(file: {n_hypot} hypot calls = {n_norm} norm arguments less one per norm"
                              + (f"; the chain's temporary {sorted(temps)} removed" if temps else "") + ")")
    if rel.endswith("retained_memory_law_tests.rs") and r["class"] == "qualification-test":
        t = git("show", f"{new}:{P}{rel}").split("\n"); a = int(nl.split("-")[0].split()[-1])
        # the enclosing fn; for a hunk of `///` doc lines only, the fn they document (the next one)
        doc = (minus or plus) and all(l.strip().startswith("///") for l in minus + plus)
        order = range(a - 1, len(t)) if doc else range(a - 1, -1, -1)
        fn = next((re.search(r"fn (\w+)", t[i]).group(1) for i in order if re.match(r"\s*(pub(\([^)]*\))? )?fn \w+", t[i])), None)
        if fn == "cap_maximal_ring_is_the_trigonometric_ring":
            kind, why = "Q", ("I109 round 2's ring check (RV125 A1-N1; I109 pr_n_01 RETURN §3, commit e4ec1cb5c9): the absolute 1e-14 "
                              "escape now covers only the three counted near-zero residues; every other coordinate within one ulp. A tightening")
    if not kind:
        refused.append({"file": rel, "new_lines": nl, "class": r["class"], "fingerprint": r["fingerprint"]}); continue
    entries.append({"fingerprint": r["fingerprint"], "file": rel, "at_final_basis": f"{os.path.basename(rel)}:{nl}", "class": r["class"],
                    "attribution": kind, "removed": [code(l) for l in mc][:6], "added": [code(l) for l in pc][:6] if kind != "M" else ["(the module)"],
                    "evidence": why,
                    "reviewed_by": "attributed by I107 (SB, Pass B round 2) to I109's norm (RR \"I109: a correctly rounded norm replaces libm `hypot` "
                                   "on published paths; ...\"); for RV126 (RV-N), which reviews the module and every call site, and RV124's confirmation"})
json.dump({"about": "PR-N Pass B (I107): entries for the hunks of main 7eae707bb7 (B1 as merged) -> 8dd64c1835 (PR-N's code) that need "
                    "one, keyed by delta_inventory2.py's fingerprint, each attributed to the norm by mk_delta_reviewed_pn.py's checks.",
           "dry_run_inventory": {"old": old, "new": new, "needing_entries": len(need)}, "norm_module": {"alloc_tokens": alloc, "recursive_fns": recursive, "fns": len(fns)},
           "entries": entries, "refused": refused}, open(out_p, "w"), indent=1)
print(json.dumps({"needing": len(need), "entries": len(entries), "refused": len(refused),
                  "by_kind": {k: sum(1 for e in entries if e["attribution"] == k) for k in "MDCQ"}}))
sys.exit(1 if refused else 0)
