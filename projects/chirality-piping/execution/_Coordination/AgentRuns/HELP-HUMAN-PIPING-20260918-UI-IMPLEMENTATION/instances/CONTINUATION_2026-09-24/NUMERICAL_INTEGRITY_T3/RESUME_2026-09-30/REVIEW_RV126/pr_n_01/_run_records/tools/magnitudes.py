"""RV126: check that published support magnitudes equal RN(sqrt(Fx^2+Fy^2+Fz^2)) of their own
published components (rows `<prefix>:force_magnitude` / `<prefix>:moment_magnitude` against
`<prefix>:Fx|Fy|Fz` / `<prefix>:Mx|My|Mz`), using check.py's exact oracle A.

Usage: magnitudes.py FILE [JSON-pointer-ish selectors are not needed: every list of result rows
       with `id`, `kind` and `value` anywhere in the document is scanned]
"""
import json
import math
import struct
import sys

import check


def bits(x):
    return struct.unpack('<Q', struct.pack('<d', x))[0]


def fb(b):
    return struct.unpack('<d', struct.pack('<Q', b))[0]


def rows_lists(node, path='$'):
    if isinstance(node, list):
        if node and all(isinstance(x, dict) and 'id' in x and 'kind' in x and 'value' in x for x in node):
            yield path, node
        for i, x in enumerate(node):
            yield from rows_lists(x, f'{path}[{i}]')
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from rows_lists(v, f'{path}.{k}')


def main():
    total = bad = 0
    for path in sys.argv[1:]:
        doc = json.load(open(path))
        for where, rows in rows_lists(doc):
            by_id = {r['id']: r for r in rows}
            for r in rows:
                if r['kind'] not in ('support_reaction_force_magnitude_v2', 'support_reaction_moment_magnitude_v2'):
                    continue
                prefix, comp = r['id'].rsplit(':', 1)
                names = ['Fx', 'Fy', 'Fz'] if comp == 'force_magnitude' else ['Mx', 'My', 'Mz']
                parts = [by_id.get(f'{prefix}:{n}') for n in names]
                if any(p is None for p in parts):
                    print('MISSING-COMPONENTS', path, where, r['id'])
                    continue
                v = [p['value'] for p in parts]
                _, want = check.oracle_a([bits(x) for x in v])
                total += 1
                chain = math.hypot(math.hypot(v[0], v[1]), v[2])
                if bits(r['value']) != want:
                    bad += 1
                    print('NOT-RN3', path, where, r['id'], repr(r['value']), 'RN3', repr(fb(want)), 'libm-chain-here', repr(chain))
                elif bits(chain) != want:
                    print('rn3-differs-from-this-libm-chain', path, where, r['id'], repr(r['value']), 'chain', repr(chain))
    print({'magnitudes_checked': total, 'not_RN3': bad})


if __name__ == '__main__':
    main()
