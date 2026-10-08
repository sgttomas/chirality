"""ROOT: compare two run_suites_nff.sh outputs test by test. Key = manifest log, test binary (hash stripped), test name."""
import json, os, re, sys
def load(d):
    out = {}
    for f in sorted(os.listdir(d)):
        if not f.endswith('.log'): continue
        binname = '?'
        for line in open(os.path.join(d, f), errors='replace'):
            m = re.match(r'\s*Running (?:unittests )?(\S+) \((?:.*/)?([^/)]+?)(?:-[0-9a-f]{16})?\)', line)
            if m: binname = m.group(2); continue
            m = re.match(r'\s*Doc-tests (\S+)', line)
            if m: binname = 'doc:' + m.group(1); continue
            m = re.match(r'test (.+?) \.\.\. (ok|FAILED|ignored)', line)
            if m:
                k = (f, binname, m.group(1))
                out[k] = m.group(2)
    return out
a, b = load(sys.argv[1]), load(sys.argv[2])
added = sorted(k for k in b if k not in a); removed = sorted(k for k in a if k not in b)
changed = [(k, a[k], b[k]) for k in sorted(a) if k in b and a[k] != b[k]]
def tally(o):
    t = {}
    for v in o.values(): t[v] = t.get(v, 0) + 1
    return t
print('base', tally(a), 'cand', tally(b)); print('added', len(added), 'removed', len(removed), 'changed', len(changed))
from collections import Counter
print('added by log/bin', Counter((k[0], k[1]) for k in added).most_common())
for k in removed[:40]: print('REMOVED', k)
for c in changed: print('CHANGED', c)
json.dump({'added': added, 'removed': removed, 'changed': changed}, open(sys.argv[3], 'w'), indent=1)
