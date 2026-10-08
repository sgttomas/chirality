"""I105: re-derive each mutant's verdict from its filtered log with the corrected test-name pattern
(a `should_panic` test prints "name - should panic ... FAILED", which the first pattern missed).
Usage: rederive.py <results.json> <log dir> <out results.json>; prints every changed verdict."""
import json, pathlib, re, sys
rows = json.loads(pathlib.Path(sys.argv[1]).read_text())
for r in rows:
    log = (pathlib.Path(sys.argv[2]) / f"{r['id']}.log").read_text()
    failed = sorted(set(re.findall(r'^test (.+?) \.\.\. FAILED', log, re.M)))
    passed = len(re.findall(r'^test .+? \.\.\. ok', log, re.M))
    compiled = 'error[E' not in log and 'could not compile' not in log
    verdict = 'compile' if not compiled else ('killed' if failed else ('survived' if passed else 'no-tests'))
    if verdict != r['verdict'] or failed != r['failed']:
        print(f"{r['id']}: {r['verdict']} -> {verdict} {failed}")
    r.update(verdict=verdict, failed=failed, passed=passed)
pathlib.Path(sys.argv[3]).write_text(json.dumps(rows, indent=1))
