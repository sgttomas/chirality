"""I101: suite comparisons, test by test.

re <i4 cargo log> <head cargo log> <out.json>
    cargo test output: per binary ("Running <path>" lines; the hash suffix dropped) and test name, its outcome.
vitest <i4 json> <head json> <out.json>
    vitest JSON reports: per file (relative to apps/desktop) and full test name (duplicates numbered in report order).
junit <base junit xml> <head junit xml> <out.json>
    pytest junit reports: per classname and test name; passed, failed, error or skipped.
"""
import json
import re
import sys


def cargo_outcomes(path):
    out, binary = {}, None
    for line in open(path, errors="replace"):
        m = re.match(r"\s+Running (?:unittests )?(\S+)", line)
        if m:
            binary = re.sub(r"-[0-9a-f]{16}\)?$", "", m.group(1).split("/")[-1].rstrip(")"))
            binary = re.sub(r"-[0-9a-f]{16}$", "", binary)
            continue
        m = re.match(r"\s*Doc-tests (\S+)", line)
        if m:
            binary = "doc:" + m.group(1)
            continue
        m = re.match(r"test (.+?) \.\.\. (ok|FAILED|ignored)", line)
        if m and binary:
            out[f"{binary} :: {m.group(1)}"] = m.group(2)
    return out


def vitest_outcomes(path):
    d, out = json.load(open(path)), {}
    for f in d["testResults"]:
        name = re.sub(r"^.*/apps/desktop/", "", f["name"])
        for a in f["assertionResults"]:
            key, n = f"{name} :: {a['fullName']}", 1
            while f"{key} #{n}" in out:
                n += 1
            out[f"{key} #{n}"] = a["status"]
    return out


def junit_outcomes(path):
    import xml.etree.ElementTree as ET
    out = {}
    for tc in ET.parse(path).iter("testcase"):
        tags = {c.tag for c in tc}
        status = "failed" if "failure" in tags else "error" if "error" in tags else "skipped" if "skipped" in tags else "passed"
        out[f"{tc.get('classname')} :: {tc.get('name')}"] = status
    return out


def compare(a, b, out_path, label):
    tally = lambda r: {s: sum(1 for v in r.values() if v == s) for s in sorted(set(r.values()))}
    diff = [{"test": k, "base": a.get(k), "head": b.get(k)} for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]
    res = {"suite": label, "base": tally(a), "head": tally(b), "differences": diff}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps({"suite": label, "base": tally(a), "head": tally(b), "differences": len(diff)}))
    for x in diff:
        print("  ", json.dumps(x)[:260])


if __name__ == "__main__":
    kind, a, b, out = sys.argv[1:5]
    f = {"re": cargo_outcomes, "vitest": vitest_outcomes, "junit": junit_outcomes}[kind]
    compare(f(a), f(b), out, kind)
