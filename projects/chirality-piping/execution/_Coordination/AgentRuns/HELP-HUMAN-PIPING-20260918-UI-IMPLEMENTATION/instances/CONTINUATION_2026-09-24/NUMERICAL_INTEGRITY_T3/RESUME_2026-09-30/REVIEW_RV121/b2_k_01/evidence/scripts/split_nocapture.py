"""Split a --nocapture --test-threads=1 libtest log into {test: [printed lines]} and compare two logs."""
import sys, re, json
def split(path):
    out = {}; cur = None
    for line in open(path, errors='replace'):
        line = line.rstrip('\n')
        m = re.match(r'^test (\S+) \.\.\. (.*)$', line)
        if m:
            cur = m.group(1); out[cur] = []
            rest = m.group(2)
            if rest not in ('ok', 'FAILED', 'ignored'):
                if rest.endswith(' ok'): rest = rest[:-3]
                out[cur].append(rest)
            continue
        if cur is None: continue
        if line in ('ok', 'FAILED', 'ignored') or line.startswith('test result:') or line == '':
            if line.startswith('test result:'): cur = None
            continue
        out[cur].append(line)
    return out
a, b = split(sys.argv[1]), split(sys.argv[2])
common = sorted(set(a) & set(b))
diff = [t for t in common if a[t] != b[t]]
print(json.dumps({'a_tests': len(a), 'b_tests': len(b), 'common': len(common),
    'common_with_output': sum(1 for t in common if a[t]), 'printed_lines_common': sum(len(a[t]) for t in common),
    'differ': diff, 'only_a': sorted(set(a) - set(b)), 'only_b_count': len(set(b) - set(a))}, indent=1))
for t in diff[:5]:
    import difflib
    print('\n'.join(list(difflib.unified_diff(a[t], b[t], lineterm=''))[:20]))
