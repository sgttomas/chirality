"""I107 SB (B1 Pass B): the gates that compare this pass with SQ's Pass A records (R/I104/b1_sq_01).
I65's own gates (tree, entry, law, premise, forms, statics, controls, outcomes) run unchanged from
R/I65/u4_g7_06/_run_records/pass_checks.py; these add the B1 references. Each subcommand prints one JSON
line and exits 0 when the condition holds, else the stop code in brackets (I65's codes: 3 entry/law/M,
6 a delta to read). Stdlib only.
  m <rm.rs> <threshold>                         [3] the registered entry's threshold_bytes is not M
  entry_code <rm.rs> <applied registration rm.rs> [3] the entry's code lines differ from the applied registration's
  premise57 <linemap out json> <SQ linemap json> [4] I65's premise pins, carried to 57c92a7b33, differ from SQ's carry
  law_sq <law log> <SQ law log>                  [6] the in-build record (I65_G5_ lines) differs from SQ's registered record
  text_sq <run dir> <ref dir> <rowdiff|-> [<mapped ref dir> <delta inventory json>]
                                                 [6] a TEXT point is incomplete, or differs from SQ's recorded point:
                                                     text_budget rows (row-matched, line-agnostic), every other file SQ
                                                     recorded (byte-equal, or JSON-equal after the line map where named
                                                     in the mapped ref dir), and the summary
  noncand_sq <nomult out> <SQ nomult out> <run rows> <SQ rows>
                                                 [6] the multiplicity-free non-candidate comparison, or the rows
                                                     themselves (lines dropped), differ from SQ's swept set
  controls_sq <controls json> <SQ controls json> [6] a control's outcome, TAV or finding differs from SQ's
  witnesses_sq <wit dir> <SQ table_dev.json>     [6] an entry point SQ ran is missing, did not pass, panicked,
                                                     or printed different witness lines (timing lines excluded)
  challenge_sq <chal dir> <SQ dev_table.json>    [6] an entry did not pass, or its I104_SQ_CHALLENGE lines
                                                     (peaks, outcomes, bounds) differ from SQ's (timing lines excluded)
"""
import gzip, json, os, re, subprocess, sys
cmd, args = sys.argv[1], sys.argv[2:]
def done(code, **kw):
    print(json.dumps({"check": cmd, "code": code, **kw})); sys.exit(code)
def load(p):
    if not os.path.exists(p) and os.path.exists(p + ".gz"): p += ".gz"
    return gzip.open(p, "rb").read() if p.endswith(".gz") else open(p, "rb").read()
NOTIME = lambda ls: [l for l in ls if "_TIME " not in l]
if cmd == "m":
    t = open(args[0]).read(); i = t.index("static REGISTERED_PROFILES"); e = t[i:t.index("\n}];", i)]
    got = re.search(r"threshold_bytes: ([\d_]+)", e).group(1)
    done(0 if got == args[1] else 3, threshold=got, expected=args[1], registered_profiles=e.count("RegisteredProfile {"))
if cmd == "entry_code":
    # the entry against the applied registration (b1 ddc8eaaf54) with `//` comment lines set aside: ROOT's
    # citation correction (NUM 75cd6be76b) changed one comment in it; every code line must be equal
    blk = lambda p: (lambda t: t[t.index("static REGISTERED_PROFILES"):t.index("\n}];", t.index("static REGISTERED_PROFILES")) + 4])(open(p).read()).split("\n")
    a, b = blk(args[0]), blk(args[1]); code = lambda L: [l for l in L if not l.strip().startswith("//")]
    import difflib
    d = [l for l in difflib.unified_diff(b, a, lineterm="", n=0)][2:]
    done(0 if code(a) == code(b) else 3, code_equal=code(a) == code(b), comment_lines_differing=[l for l in d if not l.startswith("@@")])
if cmd == "premise57":
    mine = [r for r in json.load(open(args[0]))["remapped"] if r[0].startswith("premise_pins")]
    sq = [r for r in json.load(open(args[1]))["remapped"] if r[0].startswith("premise_pins")]
    done(0 if mine == sq and len(mine) == 3 else 4, mine=mine, sq=sq)
if cmd == "law_sq":
    pick = lambda p: [l.split("... ", 1)[-1].strip() for l in load(p).decode().splitlines() if re.search(r"I65_G5_(ATOM|BUDGET|ESTIMATE_WEIGHT|IDENTITY|PHASE|PROFILE|READER_LAYOUT|REVIEWED_INPUTS)\b", l)]
    a, b = pick(args[0]), pick(args[1])
    done(0 if sorted(a) == sorted(b) and a else 6, lines=[len(a), len(b)], in_order=a == b,
         only_mine=sorted(set(a) - set(b))[:10], only_sq=sorted(set(b) - set(a))[:10])
if cmd == "text_sq":
    run, ref, rowdiff = args[:3]; mapped = args[3] if len(args) > 3 else None; issues, compared = [], []
    where = lambda f: next((p for p in (os.path.join(run, "work", f), os.path.join(run, f)) if os.path.exists(p)), None)
    names = sorted({f[:-3] if f.endswith(".gz") else f for f in os.listdir(ref)} - {"run_point.log", "audit_controls.out.json", "audit_controls.out.txt"})
    for f in names:
        mine = where(f)
        if mine is None: issues.append({"missing_in_run": f}); continue
        if f.startswith("text_budget") and rowdiff != "-":
            t = json.load(open(mine))
            if not t["complete"] or t["unclassified_args"] or t["unmapped_loop_headers"]:
                issues.append({"file": f, "incomplete": t["unclassified_args"][:10], "unmapped": t["unmapped_loop_headers"][:5]})
            refp = os.path.join(run, "ref_" + f); open(refp, "wb").write(load(os.path.join(ref, f)))
            d = json.loads(subprocess.run([sys.executable, rowdiff, refp, mine], capture_output=True, text=True, check=True).stdout.split("\n")[0])
            os.remove(refp)
            if d["changed"] or d["unmatched_positive_in_first"] or d["only_in_second"] or d["tav"][0] != d["tav"][1] or d["D"][0] != d["D"][1]:
                issues.append({"file": f, "rows": d})
            compared.append([f, "rows", d["rows"], d["tav"][1], d["D"][1]]); continue
        if mapped and f == "edges.json" and os.path.exists(os.path.join(mapped, f)):
            # the call graph after the line map: edges and site loops equal; spans are (file, byte start, byte end), which
            # the line map does not carry, so a span may move only within a file the delta changed, and change its length
            # only for a fn that encloses a reviewed production hunk of the delta (delta_inventory.json's rows' fns)
            x, y = json.load(open(os.path.join(mapped, f))), json.load(open(mine))
            inv = json.load(open(args[4])); changed = {r["file"] for r in inv["rows"] if r["class"] not in ("not-d1",)}
            allowed = {i["fn"] for r in inv["rows"] if r.get("reviewed") for i in r.get("fns", [])}
            sx, sy = x["spans"], y["spans"]; moved = [k for k in sx if k in sy and sx[k] != sy[k]]
            bad = [k for k in moved if sx[k][0] != sy[k][0] or not any(sx[k][0].endswith(c) for c in changed)]
            resized = [k.split("/src/")[-1] for k in moved if sx[k][2] - sx[k][1] != sy[k][2] - sy[k][1]]
            eq = x["edges"] == y["edges"] and x["site_loops"] == y["site_loops"] and set(sx) == set(sy) and not bad and set(resized) <= allowed
            compared.append([f, "json-after-linemap (edges, site_loops; spans moved only in changed files, resized only for reviewed fns)", eq,
                             {"spans_moved": len(moved), "resized": resized, "bad": bad[:5]}])
        elif mapped and os.path.exists(os.path.join(mapped, f)):
            eq = json.load(open(os.path.join(mapped, f))) == json.loads(open(mine, "rb").read())
            compared.append([f, "json-after-linemap", eq])
        elif f == "summary.json":
            eq = json.loads(load(os.path.join(ref, f))) == json.loads(open(mine, "rb").read()); compared.append([f, "json", eq])
        else:
            eq = load(os.path.join(ref, f)) == open(mine, "rb").read(); compared.append([f, "bytes", eq])
        if not eq: issues.append({"differs": f})
    s = json.load(open(os.path.join(run, "summary.json")))
    done(6 if issues else 0, issues=issues, compared=compared, D=s.get("D"), D_env=s.get("D_env"), TAV=s.get("TAV"),
         complete=s.get("text_complete"), E_mov_plus_R=[s["sparse"]["E_mov_plus_R"], s["dense"]["E_mov_plus_R"]])
if cmd == "noncand_sq":
    a, b = json.load(open(args[0])), json.load(open(args[1]))
    k = lambda r: (r["site"].rsplit(":", 1)[0].split("core/")[-1], (r["fn"] or "").rsplit(":", 1)[-1], str(r["kind_or_spec"]), str(r["class"]), " ".join(r["expr"].split()), str(r["mult"]))
    issues = []
    for f in ("rv87_rows", "run_rows", "matched", "multiplicity_changes"):
        if a[f] != b[f]: issues.append({f: [a[f], b[f]]})
    for f in ("new_noncandidates", "rv87_rows_absent_now"):
        if sorted(map(k, a[f])) != sorted(map(k, b[f])): issues.append({"differs": f})
    ra, rb = json.load(open(args[2])), json.load(open(args[3]))
    rows_equal = sorted(map(k, ra)) == sorted(map(k, rb))
    if not rows_equal: issues.append({"differs": "rows (lines dropped)"})
    done(6 if issues else 0, issues=issues, run_rows=a["run_rows"], matched=a["matched"], new=len(a["new_noncandidates"]),
         gone=len(a["rv87_rows_absent_now"]), rows_equal_without_lines=rows_equal, rows_bytes_equal=open(args[2], "rb").read() == open(args[3], "rb").read())
if cmd == "controls_sq":
    a, b = json.load(open(args[0])), json.load(open(args[1]))
    norm = lambda d: [(r["control"], r["pass"], r["complete"], r["TAV"], json.dumps(r["findings"])) for r in d]
    done(0 if norm(a) == norm(b) else 6, controls=[len(a), len(b)], differ=[x for x, y in zip(norm(a), norm(b)) if x != y][:5])
if cmd == "witnesses_sq":
    D, sq = args[0], json.load(open(args[1])); issues = []
    for name, ref in sorted(sq.items()):
        p = os.path.join(D, name + ".out")
        if not os.path.exists(p): issues.append({"missing": name}); continue
        t = open(p).read(); res = re.search(r"test result: (\w+)\. (\d+) passed; (\d+) failed", t)
        lines = NOTIME([l.split("... ", 1)[-1] for l in t.splitlines() if "I65_G5_WITNESS" in l or "I104_SQ_" in l])
        panics = [l for l in t.splitlines() if "panicked" in l or "overflow" in l.lower() or "SIGABRT" in l]
        result = f"{res.group(1)} {res.group(2)}/{res.group(3)}" if res else "NO RESULT (abort?)"
        if result != "ok 1/0" or panics or lines != NOTIME(ref["lines"]) or result != ref["result"]:
            issues.append({"entry": name, "result": result, "sq": ref["result"], "lines_equal": lines == NOTIME(ref["lines"]), "panics": panics[:2]})
    done(6 if issues else 0, entries=len(sq), passed_and_equal=len(sq) - len(issues), issues=issues)
if cmd == "challenge_sq":
    D, sq = args[0], json.load(open(args[1])); issues = []; n = 0
    for f in sorted(os.listdir(D)):
        if not f.endswith(".log"): continue
        t = open(os.path.join(D, f)).read(); name = f[:-4]
        ok = re.search(r"test result: ok\. 1 passed; 0 failed", t) is not None
        lines = NOTIME([l.split("... ", 1)[-1].strip() for l in t.splitlines() if "I104_SQ_CHALLENGE" in l])
        if name == "default":
            ref = None
        else:
            key = "floor" if name == "process_floor" else "dev." + name.replace("__", ".")
            ref = NOTIME(sq[key]["1"]["lines"]) if key in sq else "absent"
        n += 1
        if not ok or (ref is not None and lines != ref):
            issues.append({"entry": name, "ok": ok, "lines": lines[:2], "sq": ref if ref is None or ref == "absent" else ref[:2]})
    keys = {("process_floor" if k == "floor" else k[4:].replace(".", "__")) for k in sq}
    missing = sorted(keys - {f[:-4] for f in os.listdir(D) if f.endswith(".log")})
    if missing: issues.append({"missing": missing})
    done(6 if issues else 0, entries=n, sq_entries=len(sq), issues=issues)
done(1, error="unknown check")
