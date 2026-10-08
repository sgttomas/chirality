"""RV120: two `cargo test` logs, test by test (keyed by the test binary's name and the test's name).
Usage: python3 compare_cargo_suite.py <i4.log> <head.log> <out.json>"""
import json
import re
import sys


def tests(path):
    out, binary = {}, "?"
    for line in open(path, errors="replace"):
        m = re.match(r"\s*Running (?:unittests )?(\S+) \(.*/deps/([A-Za-z0-9_]+)-[0-9a-f]+\)", line)
        if m:
            binary = m.group(2)
            continue
        m = re.match(r"\s*Doc-tests (\S+)", line)
        if m:
            binary = "doc:" + m.group(1)
            continue
        m = re.match(r"test (.+?) \.\.\. (ok|FAILED|ignored)\s*$", line)
        if m:
            out[f"{binary} :: {m.group(1)}"] = m.group(2)
    return out


a, b = tests(sys.argv[1]), tests(sys.argv[2])
tally = lambda r: {s: sum(1 for v in r.values() if v == s) for s in sorted(set(r.values()))}
diff = [{"test": k, "i4": a.get(k), "head": b.get(k)} for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]
res = {"i4": tally(a), "head": tally(b), "differences": diff}
json.dump(res, open(sys.argv[3], "w"), indent=1)
print(json.dumps({"i4": tally(a), "head": tally(b), "differences": len(diff)}))
for x in diff:
    print("  ", json.dumps(x))
