"""RV124: the mutant table from logs/mut/*.log (test result, failing tests, build errors)."""
import glob, os, re, subprocess, json
S = "WT/scratch/rv124_rvq"
desc = {l.split("\t")[0]: (l.split("\t")[1], l.split("\t")[2]) for l in subprocess.run(
    ["WT/venv/bin/python", S + "/bin/mutants.py", "list"], capture_output=True, text=True).stdout.splitlines()}
rows = []
for m in sorted(desc):
    p = f"{S}/logs/mut/{m}.log"
    if not os.path.exists(p):
        continue
    t = open(p, errors="replace").read()
    res = re.findall(r"test result: (\w+)\. (\d+) passed; (\d+) failed", t)
    fails = sorted(set(re.findall(r"^test (\S+) \.\.\. FAILED", t, re.M)))
    err = "error[E" in t or "could not compile" in t
    killed = (bool(fails) or err) if m not in ("M00",) else None
    rows.append({"id": m, "selector": desc[m][0], "mutant": desc[m][1], "result": res, "failing": fails, "compile_error": err,
                 "verdict": "baseline" if m == "M00" else ("KILLED" if killed else "SURVIVED")})
json.dump(rows, open(S + "/ana/mutants.json", "w"), indent=1)
for r in rows:
    print(r["id"], r["verdict"], r["result"], "|", r["mutant"], "|", ", ".join(f.split("::")[-1] for f in r["failing"])[:200], "| compile_error" if r["compile_error"] else "")
