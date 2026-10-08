#!/usr/bin/env python3
"""K-13: compare the printed output of every test present in both captures
(single-threaded, --nocapture). Prints a JSON summary; exit 1 on a difference
in a test common to both builds, other than the declared K-11 re-pin."""
import json, re, sys

DECLARED = {'structural::retained::adaptive::source_residual_tests::'
            'source_residual_combination_and_missing_uniqueness_are_explicit_refusals'}
HEAD = re.compile(r'^test (\S+) \.\.\. ?(.*)$')


def blocks(path):
    out, name, buf = {}, None, []
    for line in open(path, errors='replace'):
        line = line.rstrip('\n')
        m = HEAD.match(line)
        if m:
            if name:
                out[name] = buf
            name, buf = m.group(1), [m.group(2)]
        elif name:
            if line.startswith('test result:') or line.startswith('RUN label='):
                out[name] = buf
                name, buf = None, []
            else:
                buf.append(line)
    if name:
        out[name] = buf
    return out


a, b = blocks(sys.argv[1]), blocks(sys.argv[2])
common = sorted(set(a) & set(b))
differ = [t for t in common if a[t] != b[t] and t not in DECLARED]
lines = sum(len(a[t]) for t in common)
summary = {
    'common_tests': len(common), 'common_output_lines': lines,
    'only_in_first': sorted(set(a) - set(b)), 'only_in_second': sorted(set(b) - set(a)),
    'declared_repin_differs': [t for t in common if t in DECLARED and a[t] != b[t]],
    'differ': differ,
}
print(json.dumps(summary, indent=1))
sys.exit(1 if differ or summary['only_in_first'] else 0)
