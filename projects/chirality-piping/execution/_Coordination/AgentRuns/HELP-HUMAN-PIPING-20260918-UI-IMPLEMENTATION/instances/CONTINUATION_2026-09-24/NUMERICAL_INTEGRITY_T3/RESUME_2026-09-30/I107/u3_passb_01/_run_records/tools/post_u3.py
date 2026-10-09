"""I107 SB round 3 (U3): readings of item 5's outputs after the pass (the pass's own gates compare with main or SQ for
equality; these attribute each difference). Each prints one JSON line; exit 0 if every difference is attributed, else 6.
  outcomes_u3 <main outcomes> <candidate outcomes> <repo> <old rev> <new rev> <crate dir under P>
      PP's or the runner's outcomes (I65's extraction) on main's tree and the candidate's: every line only on main is a
      test whose #[test] fn the commit removed from the crate, every line only on the candidate one it added (by source
      scan of the crate's .rs files at both revisions, the fn name compared with the test path's last segment), and no
      test present on both sides changes outcome.
  law_u3 <candidate law log> <SQ's registered law log>
      The I65_G5_* lines: every PHASE and PROFILE line equals SQ's with requested, max_without_R and E_mov_plus_R exactly
      800 lower (moving unchanged; fraction_of_M allowed to move in its last digit); the ATOM lines (keyed by kind and
      atom; tab-separated `I65_G5_ATOM <kind> <atom> <bytes> <second column>`) differ only for
      s((&str,StressRecoveryResult)) (bytes 32 lower) and s((String,DerivedSection)) (8 lower), the second column equal;
      every other line equal.
  challenge_u3 <chal dir> <SQ dev_table.json>
      Each entry passed; its outcome, rows and bound name equal SQ's; bound_bytes exactly 800 lower; peak_bytes not above
      SQ's (a lower peak is listed); the ratio is peak/bound to 6 places. process_floor: live_bytes - len(argv[0]) equals
      SQ's 4162 - len(SQ's argv[0])... SQ's argv[0] is not recorded, so the floor is checked as 4060 + len(argv[0]) with
      argv[0] this run's challenge binary path (round 1's environmental floor).
  witnesses_u3 <wit dir> <SQ table_dev.json>
      Each of SQ's 40 entry points passed with no panic, and printed SQ's witness lines (timing lines excluded); a
      differing line is listed with SQ's."""
import collections, json, os, re, subprocess, sys
cmd, args = sys.argv[1], sys.argv[2:]
def done(code, **kw):
    print(json.dumps({"check": cmd, "code": code, **kw})); sys.exit(code)
NOTIME = lambda ls: [l for l in ls if "_TIME " not in l]
if cmd == "outcomes_u3":
    ma, ca, repo, old, new, crate = args
    A, B = set(open(ma).read().split("\n")) - {""}, set(open(ca).read().split("\n")) - {""}
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    def tests(rev):
        files = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", rev, f"projects/chirality-piping/{crate}"], capture_output=True, text=True, env=env).stdout.split()
        out = collections.Counter()
        for f in files:
            if not f.endswith(".rs"): continue
            t = subprocess.run(["git", "-C", repo, "show", f"{rev}:{f}"], capture_output=True, text=True, env=env).stdout
            for m in re.finditer(r"#\[test\](?:\s*#\[[^\]]*\])*\s*(?:pub\s+)?(?:async\s+)?fn\s+(\w+)", t): out[m.group(1)] += 1
        return out
    to, tn = tests(old), tests(new)
    removed, added = set(to - tn), set(tn - to)
    name = lambda l: re.sub(r" \.\.\. .*$", "", l.split(" :: test ", 1)[-1]).split("::")[-1]
    state = lambda l: l.rsplit(" ... ", 1)[-1]
    key = lambda l: re.sub(r" \.\.\. .*$", "", l)
    ka, kb = {key(l): l for l in A}, {key(l): l for l in B}
    only_main = sorted(k for k in ka if k not in kb); only_cand = sorted(k for k in kb if k not in ka)
    flips = sorted([k, state(ka[k]), state(kb[k])] for k in ka if k in kb and state(ka[k]) != state(kb[k]))
    bad = [k for k in only_main if name(k) not in removed] + [k for k in only_cand if name(k) not in added] + [f[0] for f in flips]
    done(6 if bad else 0, lines=[len(A), len(B)], removed_tests_listed=len(only_main), added_tests_listed=len(only_cand),
         only_main=only_main, only_candidate=only_cand, flips=flips, unattributed=bad,
         source_scan={"removed": sorted(removed), "added": sorted(added)},
         failed_both=sorted(k for k in ka if k in kb and state(ka[k]) == "FAILED"))
if cmd == "law_u3":
    pick = lambda p: [l.split("... ", 1)[-1].strip() for l in open(p, errors="replace").read().splitlines()
                      if re.search(r"I65_G5_(ATOM|BUDGET|ESTIMATE_WEIGHT|IDENTITY|PHASE|PROFILE|READER_LAYOUT|REVIEWED_INPUTS)\b", l)]
    a, b = pick(args[0]), pick(args[1])
    kv = lambda l: dict(re.findall(r"(\w+)=([^ ]+)", l))
    def ident(l):
        t = l.split()[0]; d = kv(l)
        if t == "I65_G5_PHASE": return (t, d.get("mode"), d.get("phase"))
        if t == "I65_G5_PROFILE": return (t, d.get("mode"))
        if t == "I65_G5_ATOM": return tuple(l.split()[:3])   # I65_G5_ATOM <kind> <atom> <bytes> <second column>
        return (t, l)
    A = {ident(l): l for l in a}; B = {ident(l): l for l in b}
    rows, bad = [], []
    ATOMS = {"s((&str,StressRecoveryResult))": 32, "s((String,DerivedSection))": 8}
    for k in sorted(set(A) | set(B), key=str):
        x, y = A.get(k), B.get(k)
        if x == y: continue
        if x is None or y is None: bad.append({"only_" + ("sq" if x is None else "mine"): x or y}); continue
        dx, dy = kv(x), kv(y)
        if k[0] in ("I65_G5_PHASE", "I65_G5_PROFILE"):
            moved = {f: int(dy[f]) - int(dx[f]) for f in dx if f in dy and re.fullmatch(r"\d+", dx[f]) and dx[f] != dy[f]}
            fr = (dx.get("fraction_of_M"), dy.get("fraction_of_M"))
            ok = all(f in ("requested", "max_without_R", "E_mov_plus_R") and v == 800 for f, v in moved.items()) and \
                 all(dx[f] == dy[f] for f in dx if f not in moved and f != "fraction_of_M") and \
                 (fr[0] == fr[1] or (fr[0] and fr[1] and abs(float(fr[0]) - float(fr[1])) <= 0.0001))
            rows.append({"line": " ".join(map(str, k)), "sq_minus_mine": moved, "fraction_of_M": fr}); (None if ok else bad.append(rows[-1]))
        elif k[0] == "I65_G5_ATOM":
            nx, ny = x.split()[3:], y.split()[3:]
            atom = k[2]
            # the first column is the in-build size; the second (unchanged here) is checked equal
            ok = (atom in ATOMS and len(nx) == len(ny) >= 1 and int(ny[0]) - int(nx[0]) == ATOMS[atom] and nx[1:] == ny[1:])
            rows.append({"atom": atom, "kind": k[1], "mine": nx, "sq": ny}); (None if ok else bad.append(rows[-1]))
        else:
            bad.append({"differs": [x, y]})
    done(6 if bad or not a else 0, lines=[len(a), len(b)], changed=rows, unattributed=bad)
if cmd == "challenge_u3":
    D, sq = args[0], json.load(open(args[1])); rows, bad = [], []
    alen = int(open(os.path.join(D, "argv0_len.txt")).read().strip()) if os.path.exists(os.path.join(D, "argv0_len.txt")) else None
    for f in sorted(os.listdir(D)):
        if not f.endswith(".log"): continue
        t = open(os.path.join(D, f)).read(); name = f[:-4]
        ok = re.search(r"test result: ok\. 1 passed; 0 failed", t) is not None
        lines = NOTIME([l.split("... ", 1)[-1].strip() for l in t.splitlines() if "I104_SQ_CHALLENGE" in l])
        if name == "default":
            rows.append({"entry": name, "ok": ok}); (None if ok else bad.append(name)); continue
        key = "floor" if name == "process_floor" else "dev." + name.replace("__", ".")
        if key not in sq: bad.append({"absent_in_sq": name}); continue
        ref = NOTIME(sq[key]["1"]["lines"])
        if name == "process_floor":
            lb = int(re.search(r"live_bytes=(\d+)", lines[0]).group(1)) if lines else None
            exp = 4060 + alen if alen is not None else None
            rows.append({"entry": name, "ok": ok, "live_bytes": lb, "sq": ref, "argv0_len": alen, "4060+len(argv0)": exp})
            if not ok or lb is None or (exp is not None and lb != exp): bad.append(name)
            continue
        if len(lines) != 1 or len(ref) != 1: bad.append({"entry": name, "lines": lines, "sq": ref}); continue
        x, y = dict(re.findall(r"(\w+)=([^ ]+)", lines[0])), dict(re.findall(r"(\w+)=([^ ]+)", ref[0]))
        same = all(x.get(k) == y.get(k) for k in ("outcome", "rows", "bound"))
        db = int(y["bound_bytes"]) - int(x["bound_bytes"]); dp = int(y["peak_bytes"]) - int(x["peak_bytes"])
        ratio_ok = abs(float(x["ratio"]) - int(x["peak_bytes"]) / int(x["bound_bytes"])) < 5e-7
        r = {"entry": name, "ok": ok, "outcome": x.get("outcome"), "rows": x.get("rows"), "bound": x.get("bound"), "bound_bytes_sq_minus_mine": db,
             "peak_bytes_sq_minus_mine": dp, "ratio": [y.get("ratio"), x.get("ratio")]}
        rows.append(r)
        if not (ok and same and db == 800 and dp >= 0 and ratio_ok): bad.append(r)
    keys = {("process_floor" if k == "floor" else k[4:].replace(".", "__")) for k in sq}
    missing = sorted(keys - {f[:-4] for f in os.listdir(D) if f.endswith(".log")})
    if missing: bad.append({"missing": missing})
    done(6 if bad else 0, entries=len(rows), sq_entries=len(sq), rows=rows, unattributed=bad,
         peaks_lower=[r["entry"] for r in rows if r.get("peak_bytes_sq_minus_mine", 0) > 0])
if cmd == "witnesses_u3":
    D, sq = args[0], json.load(open(args[1])); bad, diffs = [], []
    for name, ref in sorted(sq.items()):
        p = os.path.join(D, name + ".out")
        if not os.path.exists(p): bad.append({"missing": name}); continue
        t = open(p).read(); res = re.search(r"test result: (\w+)\. (\d+) passed; (\d+) failed", t)
        lines = NOTIME([l.split("... ", 1)[-1] for l in t.splitlines() if "I65_G5_WITNESS" in l or "I104_SQ_" in l])
        panics = [l for l in t.splitlines() if "panicked" in l or "overflow" in l.lower() or "SIGABRT" in l]
        result = f"{res.group(1)} {res.group(2)}/{res.group(3)}" if res else "NO RESULT (abort?)"
        if lines != NOTIME(ref["lines"]): diffs.append({"entry": name, "mine": [l for l in lines if l not in ref["lines"]][:4], "sq": [l for l in NOTIME(ref["lines"]) if l not in lines][:4]})
        if result != "ok 1/0" or panics or result != ref["result"]: bad.append({"entry": name, "result": result, "panics": panics[:2]})
    done(6 if bad or diffs else 0, entries=len(sq), failed=bad, differing_lines=diffs)
done(2, error="unknown command")
