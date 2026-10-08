"""I107 SB round 2 (PR-N): round 1's post_run_b1.py retargeted (scratch WT/scratch/i107_pn/; no RV124 comparison).
Round 1: gather B1's Pass B run into the records (stdlib only; read-only for every input). The WT root is
written as `WT`; a remaining absolute machine path stops the gathering. Test-printed timing lines (`*_TIME`)
are left out: this pass measures nothing.
Usage: I107_WT=<WT> python3 post_run_b1.py <tag> <records out dir>"""
import gzip, hashlib, json, os, re, shutil, sys
T = os.environ["I107_WT"].rstrip("/"); TAG, OUT = sys.argv[1:3]
O = f"{T}/scratch/i107_pn/pass_{TAG}"; L = f"{O}/logs"
BAD = re.compile("|".join(["/" + "Users/", "/" + "private/", "~" + "/", "/" + "home/"]))   # machine path forms, spelt in pieces
def clean(s):
    s = s.replace(T, "WT")
    m = BAD.search(s)
    if m: raise SystemExit(f"machine path left after cleaning: {s[max(0, m.start() - 60):m.end() + 60]!r}")
    return s
def put(name, text, gz=False):
    p = os.path.join(OUT, name); os.makedirs(os.path.dirname(p), exist_ok=True); text = clean(text)
    if gz:
        with open(p + ".gz", "wb") as fh: fh.write(gzip.compress(text.encode(), mtime=0))
    else:
        open(p, "w").write(text)
def copy(src, name=None, gz=False):
    put(name or os.path.basename(src), open(src, encoding="utf-8", errors="replace").read(), gz)
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
os.makedirs(OUT, exist_ok=True)
for f in ["VERDICT.txt", "verdict.tsv", "D.txt", "delta.out.txt", "statics.json", "statics_vs_u4_passA.info.json", "linemap.out.json",
          "linemap_premise57.json", "linemap_sq_edges_looplog.out.json", "noncand_compare_nomult.out.json", "controls.out.txt", "cargo_summary.txt",
          "sq_pp.outcomes", "item10_error_owners.json"] + sorted(x for x in os.listdir(O) if x.startswith("gate_")):
    if os.path.exists(f"{O}/{f}"): copy(f"{O}/{f}")
copy(f"{O}/delta_inventory.json", gz=True); copy(f"{O}/noncand_compare.info.json", gz=True)
copy(f"{O}/ctl/audit_controls_g7.out.json")
for p in ("g5", "n5"):
    copy(f"{O}/{p}/summary.json", f"text_{p}_summary.json"); copy(f"{L}/point_{p}.txt", f"text_{p}_point.txt")
for f in os.listdir(L):
    if f.endswith(".outcomes") or f in ("witness_entries.txt", "challenge_entries.txt", "sq_n5_chain.log"): copy(f"{L}/{f}")
if os.path.exists(f"{L}/cargo.out"): copy(f"{L}/cargo.out", "run_cargo_b1.out.txt")
for f in os.listdir(L):
    if f.endswith(".log") and f != "law.log" and ("_pp" in f or "runner" in f):
        copy(f"{L}/{f}", f"suites/{f}", gz=True)
law = open(f"{L}/law.log").read() if os.path.exists(f"{L}/law.log") else ""
put("law_record.txt", "\n".join(m.group(0) for m in (re.search(r"I65_G5_\w.*", l) for l in law.split("\n")) if m) + "\n"
    + "\n".join(l for l in law.split("\n") if l.startswith("test result")) + "\n")
wit = {}
for f in sorted(os.listdir(f"{O}/wit")) if os.path.isdir(f"{O}/wit") else []:
    t = open(f"{O}/wit/{f}").read(); res = re.search(r"test result: (\w+)\. (\d+) passed; (\d+) failed", t)
    wit[f[:-4]] = {"result": f"{res.group(1)} {res.group(2)}/{res.group(3)}" if res else "NO RESULT (abort?)",
                   "lines": [l.split("... ", 1)[-1] for l in t.splitlines() if ("I65_G5_WITNESS" in l or "I104_SQ_" in l) and "_TIME " not in l],
                   "panics": [l for l in t.splitlines() if "panicked" in l or "overflow" in l.lower() or "SIGABRT" in l]}
put("witnesses_table.json", json.dumps(wit, indent=1) + "\n")
chal = {}
for f in sorted(os.listdir(f"{O}/chal")) if os.path.isdir(f"{O}/chal") else []:
    t = open(f"{O}/chal/{f}").read()
    chal[f[:-4]] = {"result": (re.search(r"test result: .*?;.*?;", t) or [""])[0],
                    "lines": [l.split("... ", 1)[-1].strip() for l in t.splitlines() if "I104_SQ_CHALLENGE" in l and "_TIME " not in l]}
put("challenge_table.json", json.dumps(chal, indent=1) + "\n")
put("hashes_not_copied.txt", "".join(f"{sha(p)}  {clean(p)}\n" for p in [f"{O}/noncand.json", f"{O}/n5/work/profile_tree.json", f"{O}/g5/work/profile_tree.json",
                                                                         f"{O}/retained_memory.regen.rs", f"{O}/g5/edges.json"] if os.path.exists(p)))
print(json.dumps({"out": clean(OUT), "files": sum(len(fs) for _, _, fs in os.walk(OUT))}))
