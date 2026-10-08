"""I101: re-read the TS mutant logs with vitest's colour codes stripped (the first TS run's parser missed coloured failure
lines), keeping each row's id, file and rc. Usage: mutants_reparse.py <in.jsonl> <out.jsonl>"""
import json, re, sys, pathlib
S = pathlib.Path("WT/scratch/i101_b3r")
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
with open(sys.argv[2], "w") as f:
    for d in rows:
        log = re.sub(r"\x1b\[[0-9;]*m", "", (S / "logs" / f"ts_mut_{d['id']}.log").read_text(errors="replace"))
        d["failed"] = sorted(set(re.findall(r"^\s+[×✗] (.+?)(?: \d+ms)?$", log, re.M)))
        d["build_error"] = ("Transform failed" in log or "SyntaxError" in log) and not d["failed"]
        if d["id"] != "control":
            d["killed"] = d.get("rc", 0) != 0 and bool(d["failed"])
        d["reparsed"] = True
        f.write(json.dumps(d) + "\n")
