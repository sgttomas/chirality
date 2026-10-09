"""I107 SB round 3 (U3): two comparisons with SQ's recorded runs, with U3's differences attributed.
  controls_u3 <controls json> <SQ controls json>
      SQ's 12 controls on G5's point: each control's name, outcome, completeness and finding (file and expression, line
      numbers dropped) equal SQ's, and its TAV's offset from the unmodified control (c0) equals SQ's offset. The common
      shift (c0's TAV, SQ's -> this run's) is U3's TAV change, read with the TEXT gate. Exit 0 if all hold, else 6.
  noncand_u3 <nomult out> <SQ nomult out> <run rows> <SQ rows> <linemap prune json>
      QUAL §11's non-candidate sweep: the rows equal SQ's (site line and fn line dropped, multiplicity kept) except SQ's
      rows at a site the line map pruned as deleted (its line removed with nothing in its place); no row is new; the
      RV87 comparison equals SQ's apart from those rows (absent from the run, their multiplicity changes gone with them).
      Exit 0 if all hold (the removed rows are listed), else 6.
  forms_u3 <I65's forms gate json>
      The committed GENERATED PROFILE block against its regeneration from this run's profile tree (I65's forms gate, 6
      when they differ): every differing line is a `const NAME: u64 = V;` whose committed value is >= the regenerated one,
      so the committed block over-prices this code by the listed amounts. Exit 0 if so, else 6."""
import collections, gzip, json, os, re, sys
cmd, args = sys.argv[1], sys.argv[2:]
def load(p):
    if not os.path.exists(p) and os.path.exists(p + ".gz"): return json.loads(gzip.open(p + ".gz").read())
    return json.load(open(p))
def done(code, **kw):
    print(json.dumps({"check": cmd, "code": code, **kw})); sys.exit(code)
nl = lambda s: re.sub(r":\d+", "", s)
if cmd == "controls_u3":
    a, b = load(args[0]), load(args[1])
    c0a, c0b = a[0]["TAV"], b[0]["TAV"]
    rows, bad = [], []
    for x, y in zip(a, b):
        same = (x["control"], x["pass"], x["complete"], nl(json.dumps(x["findings"]))) == (y["control"], y["pass"], y["complete"], nl(json.dumps(y["findings"])))
        off = (x["TAV"] - c0a, y["TAV"] - c0b)
        rows.append([x["control"], x["pass"], x["complete"], off[0], off[1], same])
        if not same or off[0] != off[1] or not x["pass"]: bad.append(x["control"])
    if len(a) != len(b): bad.append("count")
    done(6 if bad else 0, controls=[len(a), len(b)], tav_c0=[c0b, c0a], common_shift=c0a - c0b, rows=rows, differ=bad)
if cmd == "noncand_u3":
    na, nb, ra, rb = load(args[0]), load(args[1]), load(args[2]), load(args[3])
    pr = load(args[4]); pruned = {k.split("core/")[-1] for k in pr.get("keys", [])}
    k = lambda r: (r["site"].rsplit(":", 1)[0].split("core/")[-1], (r["fn"] or "").rsplit(":", 1)[-1], str(r["kind_or_spec"]), str(r["class"]),
                   " ".join(r["expr"].split()), str(r["mult"]))
    site = lambda r: r["site"].split("core/")[-1]
    removed = [r for r in rb if site(r) in pruned]
    A = collections.Counter(map(k, ra)); B = collections.Counter(map(k, [r for r in rb if site(r) not in pruned]))
    extra_run, missing = list((A - B).elements()), list((B - A).elements())
    issues = []
    if extra_run: issues.append({"rows_new_or_changed_in_run": extra_run[:6]})
    if missing: issues.append({"sq_rows_missing_not_removed": missing[:6]})
    ka = lambda r: (r["site"].rsplit(":", 1)[0].split("core/")[-1], (r["fn"] or "").rsplit(":", 1)[-1], str(r["kind_or_spec"]), str(r["class"]), " ".join(r["expr"].split()))
    if sorted(map(ka, na["new_noncandidates"])) != sorted(map(ka, nb["new_noncandidates"])): issues.append({"differs": "new_noncandidates"})
    absent_extra = [r for r in na["rv87_rows_absent_now"] if ka(r) not in set(map(ka, nb["rv87_rows_absent_now"]))]
    rem_keys = collections.Counter(ka(r)[1:] for r in removed)   # fn, kind, class, expr (sites differ between RV87's and SQ's lines)
    if sorted(collections.Counter(ka(r)[1:] for r in absent_extra).items()) != sorted(rem_keys.items()):
        issues.append({"rv87_absent_beyond_removed": [ka(r) for r in absent_extra]})
    mc = collections.Counter(na["multiplicity_changes"]); exp = collections.Counter(nb["multiplicity_changes"])
    for r in absent_extra:
        sqr = next((x for x in removed if ka(x)[1:] == ka(r)[1:]), None)
        if sqr: exp[f"{r['mult']}->{sqr['mult']}"] -= 1
    exp = +exp
    if mc != exp: issues.append({"multiplicity_changes_beyond_removed": [dict(mc - exp), dict(exp - mc)]})
    if na["run_rows"] != nb["run_rows"] - len(removed) or na["matched"] != nb["matched"] - len(absent_extra): issues.append({"counts": [na["run_rows"], nb["run_rows"], na["matched"], nb["matched"]]})
    done(6 if issues else 0, issues=issues, run_rows=[nb["run_rows"], na["run_rows"]], matched=[nb["matched"], na["matched"]],
         removed_with_their_lines=[{"site": r["site"], "expr": r["expr"], "class": r["class"], "mult": r["mult"], "fn": r["fn"]} for r in removed],
         rv87_absent_added=[{"site": r["site"], "mult": r["mult"]} for r in absent_extra])
if cmd == "forms_u3":
    g = load(args[0]); diff = g.get("diff", [])
    C = re.compile(r"^([-+])\s*pub\(crate\) const (\w+): u64 = (\d+); //(.*)$")
    old, new, other = {}, {}, []
    for l in diff:
        if l.startswith("@@"): continue
        m = C.match(l)
        if m: (old if m.group(1) == "-" else new)[m.group(2)] = (int(m.group(3)), m.group(4).strip())
        else: other.append(l)
    rows = [[k, old[k][1], old[k][0], new.get(k, (None,))[0], old[k][0] - new[k][0] if k in new else None] for k in sorted(old)]
    bad = other + [r[0] for r in rows if r[3] is None or r[3] > r[2]] + [k for k in new if k not in old]
    done(0 if g.get("code") in (0, 6) and not bad else 6, forms_gate=g.get("code"), constants=rows, committed_minus_regenerated_total=sum(r[4] or 0 for r in rows),
         not_conservative=bad[:6])
done(2, error="unknown command")
