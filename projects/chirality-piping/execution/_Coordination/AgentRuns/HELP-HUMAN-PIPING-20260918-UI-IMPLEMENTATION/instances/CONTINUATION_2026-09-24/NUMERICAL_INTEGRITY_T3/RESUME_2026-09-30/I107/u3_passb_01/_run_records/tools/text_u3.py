"""I107 SB round 3 (U3): the TEXT gate against SQ's recorded point (B1's Pass A), every difference attributed.
SQ's point is B1's tree. The candidate is main (B1 + PR-N) + U3, so a difference is PR-N's norm (round 2's text_pn
allowances, kept) or U3's: a removal (the legacy pressure path) or added code (refusals, text corrections).
Checks, per output SQ recorded:
  - text_budget (4 variants): complete, nothing unclassified or unmapped; rows grouped by (file, kind, fn name) and
    aligned in line order (a monotone matching that prefers dominated pairs). A row is
      kept        matched with mult, bytes and req all <= SQ's (a removal can only shrink it);
      gone        SQ's row unmatched: its fn is deleted (no `fn name` left in the candidate's file) or encloses a delta
                  row of this pass that removed code;
      grown/new   matched but larger, or unmatched in the candidate: its fn encloses a delta row of this pass that ADDED
                  code (a refusal or a text correction). Listed as increases to read.
    D equal; TAV and every scalar total <= SQ's; function_multiplicity <= SQ's by (file, fn name), or attributed as above.
  - edges.json (SQ's, carried 57c92a7b33 -> the candidate by the line map): a node SQ had and the candidate lacks is a
    deleted fn, or one whose every SQ caller is itself lost or encloses a delta row (it fell off the graph), or re-keyed
    (same file and name, header edited: the new key encloses a delta row); a lost edge leaves a lost node or a delta fn;
    an added node is the norm's (correct_norm.rs) or re-keyed; an added edge touches the norm or leaves a delta fn that
    added code; site_loops likewise (headers compared hypot/norm-free); spans move only in changed files and resize only
    for fns enclosing a delta row (this pass, PR-N's or round 1's reviewed rows).
  - looplog.json: a multiset with line numbers and hypot/norm spellings dropped; a lost entry belongs to a lost node or a
    delta fn, an added one to the norm or a delta fn that added code.
  - cg.out.json: nodes and edges equal SQ's plus the norm's and re-keyed, less the lost; root depths equal (as values);
    cyclic components equal as sets.
  - every other JSON output: numbers <= SQ's; a symbolic form (`c*atom + ... + k`) termwise <= SQ's with no new atom;
    any other value equal.
Prints one JSON line. Exit 0: every difference attributed and nothing grew. 6: anything unattributed (issues) or any
attributed increase (increases_to_read): I65's "delta to read".
A fn "encloses a delta row" when it encloses a removed line at the delta's base or an added line at the candidate
(fn spans by brace matching, as I65's delta tool finds them; its own rows give fns only for added lines). A node SQ had is
"deleted" when its fn name is gone from the candidate's file, or the line map tagged its header line `deleted` (it lay
in a hunk with nothing in its place). A grown row with mult 0 on both sides requests nothing; it is listed, not read.
Usage: python3 text_u3.py <run dir> <SQ point dir> <text_row_diff.py|-> <mapped SQ dir|-> <delta_inventory.json>
       <rules linemap out json> <round 1's delta_inventory.json(.gz)> <round 2's delta_inventory.json(.gz)> <candidate tree>
       <repo>
(<candidate tree> holds projects/chirality-piping; the text_row_diff.py argument only says whether rows are compared.)"""
import collections, gzip, json, os, re, subprocess, sys
run, ref, rowdiff, mapped, inv_p, lm_p, r1_p, r2_p, tree, repo = sys.argv[1:11]
P = os.path.join(tree, "projects/chirality-piping")
raw = lambda p: gzip.open(p + ".gz").read() if not os.path.exists(p) and os.path.exists(p + ".gz") else open(p, "rb").read()
jl = lambda p: json.load(gzip.open(p) if p.endswith(".gz") else open(p))
CN = "/correct_norm.rs:"
nh = lambda s: re.sub(r"[^A-Za-z0-9_\[\]]", "", s.replace("hypot", "").replace("norm3", "").replace("norm2", ""))
nl = lambda s: re.sub(r":\d+", "", s)
inv, r1, r2 = jl(inv_p), jl(r1_p), jl(r2_p)
lm = json.load(open(lm_p)); lm = lm.get("summary", lm)
name = lambda k: (k or "").rsplit(":", 1)[-1]
full = lambda k: k if k.startswith("core/") or k.startswith("validation/") else None
# fns enclosing a delta row of this pass, by (file, fn line at the candidate, name) and by (file, name)
def dfns(rows, need=None):
    out = set()
    for r in rows:
        if need and not need(r): continue
        for i in r.get("fns", []):
            out.add((r["file"], name(i["fn"])))
    return out
D_ANY = dfns(inv["rows"]); D_ADD = dfns(inv["rows"], lambda r: r.get("added", 0) > 0); D_REM = set()
# every delta row's enclosing fns on both sides, by I65's span rule (removed lines at the base, added lines at the candidate)
FN = re.compile(r"^\s*(pub(\([^)]*\))?\s+)?(const\s+)?(async\s+)?(unsafe\s+)?(extern\s+\"[^\"]*\"\s+)?fn\s+(\w+)")
def code_of(l):
    l = re.sub(r'"(\\.|[^"\\])*"', '""', l); l = re.sub(r"'(\\.|[^'\\])'", "''", l); return l.split("//")[0]
def fn_spans(L):
    out = []
    for i, l in enumerate(L):
        m = FN.match(l)
        if not m: continue
        depth, started, j = 0, False, i
        while j < len(L):
            cl = code_of(L[j]); depth += cl.count("{") - cl.count("}")
            if "{" in cl: started = True
            if started and depth <= 0: break
            if not started and cl.rstrip().endswith(";"): break
            j += 1
        out.append((i + 1, j + 1, m.group(7)))
    return out
genv = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
gshow = lambda rev, f: subprocess.run(["git", "-C", repo, "show", f"{rev}:projects/chirality-piping/{f}"], capture_output=True, text=True, env=genv)
for f in sorted({r["file"] for r in inv["rows"] if r["file"].endswith(".rs") and r["class"] not in ("not-d1",)}):
    o = gshow(inv["old"], f); n = gshow(inv["new"], f)
    OS = fn_spans(o.stdout.split("\n")) if o.returncode == 0 else []; NS = fn_spans(n.stdout.split("\n")) if n.returncode == 0 else []
    d = subprocess.run(["git", "-C", repo, "diff", "-U0", inv["old"], inv["new"], "--", "projects/chirality-piping/" + f], capture_output=True, text=True, env=genv).stdout
    for m in re.finditer(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", d):
        oa, oc, na, nc = int(m.group(1)), int(m.group(2) or 1), int(m.group(3)), int(m.group(4) or 1)
        for x in range(oa, oa + oc) if oc else ():
            for a, b, nm in OS:
                if a <= x <= b: D_REM.add((f, nm))
        for x in range(na, na + nc) if nc else ():
            for a, b, nm in NS:
                if a <= x <= b: D_ADD.add((f, nm))
D_ANY |= D_REM | D_ADD
D_PRIOR = dfns(r2["rows"]) | dfns([r for r in r1["rows"] if r.get("reviewed")])
changed = (set(lm["changed_production_rs"]) | {r["file"] for r in inv["rows"]} | {r["file"] for r in r2["rows"]}
           | {r["file"] for r in r1["rows"] if r.get("reviewed")})
_src = {}
def src(f):
    if f not in _src:
        p = os.path.join(P, f); _src[f] = open(p).read() if os.path.exists(p) else None
    return _src[f]
def deleted_fn(f, n):
    t = src(f)
    return t is None or not re.search(r"\bfn\s+" + re.escape(n) + r"\b", t)
LM_DELETED = set()
if mapped != "-" and os.path.exists(os.path.join(mapped, "g7_linemap.out.json")):
    _m = json.load(open(os.path.join(mapped, "g7_linemap.out.json"))); _m = _m.get("summary", _m)
    LM_DELETED = {u[1] for u in _m.get("unmapped", []) if len(u) > 3 and u[3] == "deleted"}
def kf(k):  # a graph key "core/.../x.rs:LINE:name" -> (file, name)
    parts = k.rsplit(":", 2); return (parts[0], parts[-1]) if len(parts) == 3 else (k, "")
issues, increases, attributed, compared = [], [], {}, []
where = lambda f: next((p for p in (os.path.join(run, "work", f), os.path.join(run, f)) if os.path.exists(p)), None)

# ---------- generic dominance for the remaining outputs
TERM = re.compile(r"^\s*(?:(\d+)\*)?(.+?)\s*$")
def symbolic(s):
    if not isinstance(s, str) or "+" not in s and not re.fullmatch(r"\d+", s.strip()): return None
    out = collections.Counter()
    for t in s.split(" + "):
        t = t.strip()
        if re.fullmatch(r"\d+", t): out["1"] += int(t); continue
        m = re.fullmatch(r"(\d+)\*(.+)", t)
        if not m: return None
        out[m.group(2)] += int(m.group(1))
    return out
def dominated(a, b, path, bad, grew):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in b:
            if k not in a: bad.append(f"{path}/{k}: new key")
            else: dominated(a[k], b[k], f"{path}/{k}", bad, grew)
        return
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): bad.append(f"{path}: list length {len(a)} -> {len(b)}"); return
        for i, (x, y) in enumerate(zip(a, b)): dominated(x, y, f"{path}[{i}]", bad, grew)
        return
    if isinstance(a, bool) or isinstance(b, bool):
        if a != b: bad.append(f"{path}: {a} -> {b}")
        return
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b > a: grew.append(f"{path}: {a} -> {b}")
        return
    if a == b: return
    sa, sb = symbolic(a), symbolic(b)
    if sa is not None and sb is not None:
        new_atoms = [x for x in sb if x not in sa]; up = [x for x in sb if x in sa and sb[x] > sa[x]]
        if new_atoms: bad.append(f"{path}: new atoms {new_atoms[:4]}")
        if up: grew.append(f"{path}: coefficients up {up[:4]}")
        return
    bad.append(f"{path}: {str(a)[:80]} -> {str(b)[:80]}")

# ---------- text_budget rows
def align(old, new):
    """Monotone matching of two line-ordered row lists; a dominated pair scores 3, another pair 1."""
    n, m = len(old), len(new)
    dom = lambda x, y: y["mult"] <= x["mult"] and y["bytes"] <= x["bytes"] and y["req"] <= x["req"]
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            S[i][j] = max(S[i + 1][j], S[i][j + 1], S[i + 1][j + 1] + (3 if dom(old[i], new[j]) else 1))
    i = j = 0; pairs = []
    while i < n and j < m:
        w = 3 if dom(old[i], new[j]) else 1
        if S[i][j] == S[i + 1][j + 1] + w: pairs.append((i, j)); i += 1; j += 1
        elif S[i][j] == S[i + 1][j]: i += 1
        else: j += 1
    return pairs
def rows_check(f, a, b):
    grp = lambda t: collections.defaultdict(list)
    A, B = collections.defaultdict(list), collections.defaultdict(list)
    for r in a["rows"]: A[(r["file"], r["kind"], name(r["fn"]))].append(r)
    for r in b["rows"]: B[(r["file"], r["kind"], name(r["fn"]))].append(r)
    out = {"kept_equal": 0, "kept_smaller": 0, "gone": [], "gone_zero": 0, "grown": [], "new": []}
    smaller_bytes, smaller_mult = collections.Counter(), collections.Counter()
    bad, inc = [], []
    for g in sorted(set(A) | set(B)):
        old = sorted(A.get(g, []), key=lambda r: r["line"]); new = sorted(B.get(g, []), key=lambda r: r["line"])
        pairs = align(old, new); mo = {i for i, _ in pairs}; mn = {j for _, j in pairs}
        fkey = (g[0], g[2])
        for i, j in pairs:
            x, y = old[i], new[j]
            if (x["mult"], x["bytes"], x["req"]) == (y["mult"], y["bytes"], y["req"]): out["kept_equal"] += 1
            elif y["mult"] <= x["mult"] and y["bytes"] <= x["bytes"] and y["req"] <= x["req"]:
                out["kept_smaller"] += 1
                if y["bytes"] < x["bytes"]: smaller_bytes[f"{x['bytes']}->{y['bytes']}"] += 1
                if y["mult"] < x["mult"]: smaller_mult[g[0].split("core/")[-1] + ":" + g[2] + (" (encloses a delta row)" if fkey in D_ANY else "")] += 1
            else:
                e = [g[0].split("core/")[-1], g[1], g[2], (x["line"], x["mult"], x["bytes"], x["req"]), (y["line"], y["mult"], y["bytes"], y["req"])]
                out["grown"].append(e)
                if fkey not in D_ADD: bad.append(["grown"] + e)
                elif x["mult"] or y["mult"] or x["req"] or y["req"]: inc.append(["grown"] + e)
        for i, x in enumerate(old):
            if i in mo: continue
            if not x["mult"]: out["gone_zero"] += 1
            why = "deleted fn" if deleted_fn(g[0], g[2]) else ("fn encloses a removal" if fkey in D_REM else None)
            e = [g[0].split("core/")[-1], g[1], g[2], x["line"], x["mult"], x["req"], why]
            if x["mult"]: out["gone"].append(e)
            if not why: bad.append(["gone"] + e)
        for j, y in enumerate(new):
            if j in mn: continue
            e = [g[0].split("core/")[-1], g[1], g[2], y["line"], y["mult"], y["req"]]
            out["new"].append(e)
            if fkey not in D_ADD: bad.append(["new"] + e)
            elif y["mult"] or y["req"]: inc.append(["new"] + e)
    # scalars and per-fn multiplicity
    sc_bad, sc_grew = [], []
    for k in ("sites", "sites_reached", "sites_with_positive_multiplicity", "total_text_requested_bytes", "largest_single_site_bytes",
              "total_text_moving_bytes", "retained_diagnostic_bytes", "reachable_fns"):
        if k in a and b.get(k, 0) > a[k]: sc_grew.append(f"{k}: {a[k]} -> {b.get(k)}")
    if b["D_diagnostics"] != a["D_diagnostics"]: sc_bad.append(f"D {a['D_diagnostics']} -> {b['D_diagnostics']}")
    for k in ("complete", "unmapped_loop_headers", "unclassified_args", "self_recursive_ancestors"):
        if k in a and json.dumps(b.get(k)) != json.dumps(a[k]) and k != "self_recursive_ancestors": sc_bad.append(f"{k} differs")
    fm = lambda t: {(kf(k)[0], kf(k)[1]): v for k, v in t.get("function_multiplicity", {}).items()}
    fa, fb = fm(a), fm(b); fm_up = []
    for k, v in fb.items():
        if k not in fa:
            if k not in D_ADD and not (CN in k[0] + ":"): fm_up.append(["new fn", k, v])
        elif v > fa[k] and k not in D_ADD: fm_up.append(["up", k, fa[k], v])
    fm_lost = [k for k in fa if k not in fb and not deleted_fn(*k) and k not in D_REM and k not in D_ANY]
    out["function_multiplicity"] = {"fns": [len(fa), len(fb)], "lost_deleted": sum(1 for k in fa if k not in fb and deleted_fn(*k)),
                                    "lost_other": len([k for k in fa if k not in fb and not deleted_fn(*k)]), "unattributed": fm_up[:6] + fm_lost[:6]}
    bad += [["scalar", s] for s in sc_bad] + [["function_multiplicity", str(x)] for x in fm_up + fm_lost]
    out["scalars_grew"] = sc_grew; bad += [["scalar grew", s] for s in sc_grew]
    out["kept_smaller_bytes"] = dict(smaller_bytes.most_common()); out["kept_smaller_mult_by_fn"] = dict(sorted(smaller_mult.items()))
    out["tav"] = [a["total_text_requested_bytes"], b["total_text_requested_bytes"]]; out["D"] = [a["D_diagnostics"], b["D_diagnostics"]]
    out["rows"] = [len(a["rows"]), len(b["rows"])]
    return out, bad, inc

names = sorted({f[:-3] if f.endswith(".gz") else f for f in os.listdir(ref)} - {"run_point.log", "audit_controls.out.json", "audit_controls.out.txt"})
mine_edges = json.load(open(os.path.join(run, "edges.json")))
lost_nodes = set()
if mapped != "-":
    ea, eb = json.load(open(os.path.join(mapped, "edges.json")))["edges"], mine_edges["edges"]
    # re-keyed: SQ's key unmapped (header in an edited hunk) and the candidate has the same (file, name) under a new key
    sq_by = collections.defaultdict(set); my_by = collections.defaultdict(set)
    for k in ea: sq_by[kf(k)].add(k)
    for k in eb: my_by[kf(k)].add(k)
    gone_keys = set(ea) - set(eb); new_keys = set(eb) - set(ea)
    rekey = {}
    for k in sorted(gone_keys):
        if k in LM_DELETED: continue   # its header line was deleted: not a re-key
        fk = kf(k); cand = sorted(x for x in my_by.get(fk, ()) if x in new_keys and x not in rekey.values())
        if cand and fk in D_ANY: rekey[k] = cand[0]
    callers = collections.defaultdict(set)
    for k, ws in ea.items():
        for w in ws: callers[w].add(k)
    lost = {k for k in gone_keys if k not in rekey}
    # a lost node: deleted fn; or every SQ caller lost (fixpoint) or a delta fn
    why = {}
    for k in lost:
        if deleted_fn(*kf(k)): why[k] = "deleted fn"
        elif k in LM_DELETED: why[k] = "deleted fn (its header line deleted, per the line map)"
    changed_flag = True
    while changed_flag:
        changed_flag = False
        for k in lost - set(why):
            cs = callers.get(k, set())
            if cs and all((c in lost and c in why) or kf(c) in D_ANY for c in cs): why[k] = "fell off the graph (its callers removed or edited)"; changed_flag = True
    lost_nodes = set(why)
GONE_FN = {kf(k) for k in lost_nodes}
def comments_only_in(k):
    """the fn's span resized though no delta row encloses it: every hunk of the line map's diff (SQ's TEXT basis -> the
    candidate) that overlaps the fn at the candidate changes only comments and blank lines (e.g. PR-N's head, RV124 C-N1)"""
    f, n = kf(k)
    t = src(f)
    if t is None or not lm.get("old"): return False
    spans_ = [(a, b) for a, b, nm in fn_spans(t.split("\n")) if nm == n]
    d = subprocess.run(["git", "-C", repo, "diff", "-U0", lm["old"], inv["new"], "--", "projects/chirality-piping/" + f], capture_output=True, text=True, env=genv).stdout
    hs, cur = [], None
    for line in d.split("\n"):
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", line)
        if m: cur = [int(m.group(3)), int(m.group(4) or 1), []]; hs.append(cur); continue
        if cur is not None and line[:1] in "+-" and not line.startswith(("+++", "---")): cur[2].append(line[1:])
    touching = [h for h in hs for a, b in spans_ if h[0] <= b and h[0] + max(h[1], 1) - 1 >= a]
    return bool(touching) and all(not code_of(l).strip() for h in touching for l in h[2])
for f in names:
    mine = where(f)
    if mine is None: issues.append({"missing_in_run": f}); continue
    if f.startswith("text_budget") and rowdiff != "-":
        b = json.load(open(mine)); a = json.loads(raw(os.path.join(ref, f)))
        if not b["complete"] or b["unclassified_args"] or b["unmapped_loop_headers"]:
            issues.append({"file": f, "incomplete": b["unclassified_args"][:10], "unmapped": b["unmapped_loop_headers"][:5]})
        o, bad, inc = rows_check(f, a, b)
        attributed[f] = {k: (v if not isinstance(v, list) or len(v) <= 16 else v[:16] + [f"... {len(v)} in all"]) for k, v in o.items()}
        issues += [{"file": f, "row": x} for x in bad]; increases += [{"file": f, "row": x} for x in inc]
        compared.append([f, "rows aligned; kept rows dominated; gone in removed code; grown/new in added code", not bad, o["tav"], o["D"]]); continue
    if f == "edges.json" and mapped != "-":
        x, y = json.load(open(os.path.join(mapped, f))), mine_edges
        ea, eb = x["edges"], y["edges"]
        unexplained_lost = sorted(gone_keys - set(rekey) - lost_nodes)
        new_nodes = sorted(new_keys - set(rekey.values()))
        bad = [("lost node", k) for k in unexplained_lost] + [("new node", n) for n in new_nodes if CN not in n]
        okfn = lambda k: k in lost_nodes or kf(k) in D_ANY or kf(k) in D_PRIOR
        lost_e = [(k, w) for k in ea for w in ea[k] if w not in eb.get(rekey.get(k, k), []) and rekey.get(w) not in eb.get(rekey.get(k, k), [])]
        bad += [("lost edge", e) for e in lost_e if not (okfn(e[0]) or e[1] in lost_nodes)]
        inv_rekey = {v: k for k, v in rekey.items()}
        added_e = [(k, w) for k in eb for w in eb[k] if w not in ea.get(inv_rekey.get(k, k), []) and inv_rekey.get(w, w) not in ea.get(inv_rekey.get(k, k), [])]
        bad += [("added edge", e) for e in added_e if not (CN in e[0] or CN in e[1] or kf(e[0]) in D_ADD or kf(e[0]) in D_PRIOR)]
        sl = lambda L, rk: collections.Counter(json.dumps([rk.get(e[0], e[0]), rk.get(e[1], e[1]), [[nh(h) for h in p] for p in e[2]]]) for e in L)
        sa, sb = sl(x["site_loops"], rekey), sl(y["site_loops"], {})
        sl_lost = list((sa - sb).elements()); sl_added = list((sb - sa).elements())
        bad += [("lost site loop", e[:160]) for e in sl_lost if not (okfn(json.loads(e)[0]) or json.loads(e)[1] in lost_nodes)]
        # an added entry for an edge whose caller is a delta fn and that lost an entry: fewer call sites, or a loop header's
        # recorded text window shifted by the edit; allowed when its per-site loop counts are a sub-multiset of the lost entry's
        lost_by = collections.defaultdict(list)
        for e in sl_lost: lost_by[tuple(json.loads(e)[:2])].append(json.loads(e)[2])
        def narrowed(e):
            c, w, sites = json.loads(e)
            if not (kf(c) in D_ANY or kf(c) in D_PRIOR): return False
            cnt = collections.Counter(len(p) for p in sites)
            return any(not (cnt - collections.Counter(len(p) for p in old)) for old in lost_by.get((c, w), []))
        sl_narrowed = [e for e in sl_added if narrowed(e)]
        bad += [("added site loop", e[:160]) for e in sl_added if e not in sl_narrowed
                and not (CN in json.loads(e)[0] or CN in json.loads(e)[1] or kf(json.loads(e)[0]) in D_ADD or kf(json.loads(e)[0]) in D_PRIOR)]
        px, py = x["spans"], y["spans"]
        moved = [k for k in px if k in py and px[k] != py[k]]
        bad += [("span moved outside a changed file", k) for k in moved if px[k][0] != py[k][0] or not any(px[k][0].endswith(c) for c in changed)]
        resized = sorted({k for k in moved if px[k][2] - px[k][1] != py[k][2] - py[k][1]})
        comment_only = [k for k in resized if kf(k) not in D_ANY and kf(k) not in D_PRIOR and comments_only_in(k)]
        bad += [("span resized", k) for k in resized if kf(k) not in D_ANY and kf(k) not in D_PRIOR and k not in comment_only]
        bad += [("span lost", k) for k in set(px) - set(py) if k not in lost_nodes and k not in rekey]
        bad += [("span new", k) for k in set(py) - set(px) if CN not in k and k not in rekey.values()]
        attributed["edges"] = {"lost_nodes": sorted(k.split("/src/")[-1] + " (" + why[k] + ")" for k in lost_nodes),
                               "rekeyed": {k.split("/src/")[-1]: v.split("/src/")[-1] for k, v in rekey.items()},
                               "new_nodes": [n.split("/src/")[-1] for n in new_nodes], "lost_edges": len(lost_e), "added_edges": len(added_e),
                               "added_edges_not_norm": [[a.split("/src/")[-1], b.split("/src/")[-1]] for a, b in added_e if CN not in a and CN not in b][:20],
                               "lost_site_loops": len(sl_lost), "added_site_loops": len(sl_added), "spans_moved": len(moved),
                               "resized": [k.split("/src/")[-1] for k in resized],
                               "resized_by_comment_edits_only": [k.split("/src/")[-1] for k in comment_only],
                               "added_site_loops_narrowed": len(sl_narrowed), "bad": [str(b)[:220] for b in bad[:12]]}
        compared.append([f, "SQ's graph less removed code, plus the norm and code U3 added", not bad]); issues += [{"edges": str(b)[:220]} for b in bad[:12]]
        continue
    if f == "looplog.json" and mapped != "-":
        def fnof(e):  # 'call A -> B' or a fn key: the caller's (file basename, name)
            s = e[0].split(" -> ")[0].replace("call ", "")
            parts = s.rsplit(":", 2); return (parts[0], parts[-1]) if len(parts) == 3 else (s, "")
        base_gone = {(os.path.basename(k[0]), k[1]) for k in GONE_FN}
        base = lambda s: {(os.path.basename(k[0]), k[1]) for k in s}
        DA, DD = base(D_ANY | D_PRIOR), base(D_ADD | D_PRIOR)
        c = lambda L: collections.Counter(json.dumps([nl(e[0]), nh(e[1])] + e[2:]) for e in L)
        A_, B_ = json.load(open(os.path.join(mapped, f))), json.load(open(mine))
        a, b = c(A_), c(B_)
        lostl = list((a - b).elements()); addl = list((b - a).elements())
        def keyof(s):
            e = json.loads(s)[0]
            e = re.sub(r"^(call|site) ", "", e).split(" -> ")[0]; return e.split(" @")[0]
        def fn_base(s):
            t = keyof(s); parts = t.split(":"); return (parts[0], parts[-1]) if len(parts) >= 2 else (t, "")
        def callee_gone(s):
            e = json.loads(s)[0]
            if " -> " not in e: return False
            t = e.split(" -> ")[1]; parts = t.split(":"); return (parts[0], parts[-1]) in base_gone
        bad = [e for e in lostl if not (fn_base(e) in base_gone or fn_base(e) in DA or callee_gone(e))]
        bad += [e for e in addl if "correct_norm.rs" not in e and fn_base(e) not in DD]
        attributed["looplog"] = {"entries": [sum(a.values()), sum(b.values())], "lost": len(lostl), "added": len(addl),
                                 "added_entries": [e[:160] for e in addl][:10]}
        compared.append([f, "multiset, lines and hypot/norm spellings dropped; lost in removed code, added in the norm or added code", not bad])
        issues += [{"looplog": e[:200]} for e in bad[:8]]; continue
    if f == "cg.out.json":
        x, y = json.loads(raw(os.path.join(ref, f))), json.load(open(mine))
        eb = mine_edges["edges"]
        n_cn = sum(1 for k in eb if CN in k)
        if mapped != "-":
            ea = json.load(open(os.path.join(mapped, "edges.json")))["edges"]
            exp_nodes = x["nodes"] + len(set(eb) - set(ea)) - len(set(ea) - set(eb))
            exp_edges = x["edges"] + sum(len(v) for v in eb.values()) - sum(len(v) for v in ea.values())
        else:  # N-5's point: SQ's N-5 edges are not recorded; compare against this run's G5 graph identity
            exp_nodes, exp_edges = y["nodes"], y["edges"]
        same_set = lambda k: sorted(json.dumps(v, sort_keys=True) for v in x.get(k, [])) == sorted(json.dumps(v, sort_keys=True) for v in y.get(k, []))
        ok = (y["nodes"] == exp_nodes and y["edges"] == exp_edges and sorted(y["root_depths"].values()) == sorted(x["root_depths"].values())
              and same_set("cyclic_components") and same_set("cyclic_component_edges")
              and all(x[k] == y[k] for k in x if k not in ("files", "nodes", "edges", "root_depths", "cyclic_components", "cyclic_component_edges")))
        attributed["cg.out"] = {"files": [x.get("files"), y.get("files")], "nodes": [x["nodes"], y["nodes"]], "edges": [x["edges"], y["edges"]],
                                "norm_nodes": n_cn, "root_depths": [sorted(x["root_depths"].values()), sorted(y["root_depths"].values())],
                                "cyclic_components_equal_as_sets": same_set("cyclic_components") and same_set("cyclic_component_edges")}
        compared.append([f, "nodes/edges = SQ's less lost plus new (counted from the graphs); depths and cycles equal", ok])
        if not ok: issues.append({"differs": f, "detail": attributed["cg.out"]})
        continue
    a, b = json.loads(raw(os.path.join(ref, f))), json.load(open(mine))
    if a == b: compared.append([f, "equal", True]); continue
    bad, grew = [], []
    dominated(a, b, f, bad, grew)
    compared.append([f, "numbers <= SQ's, symbolic forms termwise <=, other values equal", not bad and not grew])
    issues += [{"file": f, "not_dominated": s} for s in bad[:8] + grew[:8]]
    attributed.setdefault("dominated", []).append(f)
s = json.load(open(os.path.join(run, "summary.json")))
code = 6 if issues or increases else 0
print(json.dumps({"check": "text_u3", "code": code, "issues": issues, "increases_to_read": increases, "attributed": attributed,
                  "compared": compared, "D": s.get("D"), "D_env": s.get("D_env"), "TAV": s.get("TAV"), "complete": s.get("text_complete"),
                  "E_mov_plus_R_chain": [s["sparse"]["E_mov_plus_R"], s["dense"]["E_mov_plus_R"]]}))
sys.exit(code)
