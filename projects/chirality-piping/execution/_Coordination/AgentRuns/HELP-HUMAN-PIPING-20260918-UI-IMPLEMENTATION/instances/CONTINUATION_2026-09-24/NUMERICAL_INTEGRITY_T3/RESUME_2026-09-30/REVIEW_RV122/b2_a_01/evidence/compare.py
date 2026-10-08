# RV122: test-by-test comparison of two suite runs (cargo, pytest -v, vitest verbose).
import json, re, sys, pathlib
def cargo(text):
    out, binary = {}, "?"
    for line in text.splitlines():
        m = re.match(r"\s+Running (\S+)", line)
        if m: binary = m.group(1); continue
        m = re.match(r"test (\S+) \.\.\. (ok|FAILED|ignored)", line)
        if m: out[f"{binary}::{m.group(1)}"] = m.group(2)
    return out
def pytest(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"(tests/\S+::\S+) (PASSED|FAILED|SKIPPED|ERROR|XFAIL|XPASS)", line)
        if m: out[m.group(1)] = m.group(2)
    return out
def vitest(text):
    out = {}
    for line in text.splitlines():
        line = re.sub(r"\x1b\[[0-9;]*m", "", line)
        m = re.match(r"\s*([✓×↓]|✗)\s+(\S+\.test\.tsx?)\s+>\s+(.*?)(?:\s+\d+ms)?$", line)
        if m: out[f"{m.group(2)} > {m.group(3)}"] = {"✓": "ok", "×": "FAILED", "✗": "FAILED", "↓": "skipped"}[m.group(1)]
    return out
PARSE = {"pp": cargo, "re": cargo, "runner": cargo, "py": pytest, "ts": vitest}
a, b = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
res = {}
for part, f in PARSE.items():
    pa, pb = a / f"{part}.log", b / f"{part}.log"
    if not (pa.exists() and pb.exists()): continue
    x, y = f(pa.read_text(errors="replace")), f(pb.read_text(errors="replace"))
    tally = lambda d: {s: sum(1 for v in d.values() if v == s) for s in sorted(set(d.values()))}
    res[part] = {"base": tally(x), "candidate": tally(y),
        "changed": {k: [x[k], y[k]] for k in x if k in y and x[k] != y[k]},
        "only_base": {k: x[k] for k in x if k not in y}, "only_candidate": {k: y[k] for k in y if k not in x},
        "failed_both": sorted(k for k in x if x[k] == "FAILED" and y.get(k) == "FAILED")}
print(json.dumps(res, indent=1, ensure_ascii=False))
