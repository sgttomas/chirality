#!/usr/bin/env python3
"""I112 (PR-N gates): byte-exact difference accounting between a base and a candidate output, and the norm check.

Applies the brief's acceptance rule to one pair of outputs:
  * the two texts are lexed into JSON lexemes (whitespace runs, punctuation, strings, numbers, literals); every lexeme must be
    identical except value lexemes (so keys, punctuation, whitespace and structure are byte-identical);
  * each differing value lexeme is mapped to its leaf path (document order), and must be either
      - the `value` of a result row whose kind is a published magnitude (displacement_magnitude,
        support_reaction_force_magnitude_v2, support_reaction_moment_magnitude_v2), differing by at most one ulp; or
      - a hash string (64 lowercase hex) under a key naming a hash; such a difference is returned for the caller to verify
        (the caller recomputes it over the moved bytes);
  * for each moved magnitude, the candidate's value must equal the correctly rounded Euclidean norm of the same output's own
    components, computed exactly: the components are binary64 values, so their squares sum exactly as a Fraction, and the
    correctly rounded square root is found by comparing the square of each rounding-interval endpoint with that sum
    (Fractions only; ties to even).
Components: support force -> the same support action's Fx, Fy, Fz rows; support moment -> Mx, My, Mz; displacement
magnitude -> the same id's ux, uy, uz rows. Where the row lists source_result_refs, the components must be among them.
Anything else is OTHER (a stop under the brief).
"""
import json
import math
import re
import struct
from fractions import Fraction as Fr

MAG_KINDS = {
    'support_reaction_force_magnitude_v2': ('force_magnitude', ('Fx', 'Fy', 'Fz')),
    'support_reaction_moment_magnitude_v2': ('moment_magnitude', ('Mx', 'My', 'Mz')),
    'displacement_magnitude': (None, ('ux', 'uy', 'uz')),
}
NUM_RE = re.compile(r'-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?')
HEX64 = re.compile(r'^"[0-9a-f]{64}"$')


def lex(text):
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c in ' \t\r\n':
            j = i
            while j < n and text[j] in ' \t\r\n':
                j += 1
            out.append(('w', text[i:j]))
            i = j
        elif c in '{}[]:,':
            out.append(('p', c))
            i += 1
        elif c == '"':
            j = i + 1
            while text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            out.append(('s', text[i:j + 1]))
            i = j + 1
        elif c == '-' or c.isdigit():
            m = NUM_RE.match(text, i)
            out.append(('n', m.group(0)))
            i = m.end()
        else:
            for lit in ('true', 'false', 'null'):
                if text.startswith(lit, i):
                    out.append(('l', lit))
                    i += len(lit)
                    break
            else:
                raise ValueError('unlexable at %d' % i)
    # mark keys: a string whose next non-whitespace lexeme is ':'
    marked = []
    for k, (t, v) in enumerate(out):
        if t == 's':
            j = k + 1
            while j < len(out) and out[j][0] == 'w':
                j += 1
            if j < len(out) and out[j] == ('p', ':'):
                t = 'k'
        marked.append((t, v))
    return marked


class Num:
    __slots__ = ('text',)

    def __init__(self, text):
        self.text = text


def parse(text):
    return json.loads(text, object_pairs_hook=lambda pairs: ('obj', pairs), parse_float=Num, parse_int=Num)


def leaves(node, path=()):
    if isinstance(node, tuple) and len(node) == 2 and node[0] == 'obj':
        for k, v in node[1]:
            yield from leaves(v, path + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from leaves(v, path + (i,))
    else:
        yield path, node


def to_plain(node):
    if isinstance(node, tuple) and len(node) == 2 and node[0] == 'obj':
        return {k: to_plain(v) for k, v in node[1]}
    if isinstance(node, list):
        return [to_plain(v) for v in node]
    if isinstance(node, Num):
        return float(node.text) if any(ch in node.text for ch in '.eE') else int(node.text)
    return node


def ulps(a, b):
    def key(x):
        i = struct.unpack('<q', struct.pack('<d', x))[0]
        return i if i >= 0 else -(i & 0x7FFFFFFFFFFFFFFF)
    return abs(key(a) - key(b))


def cr_sqrt(s):
    """The binary64 nearest to sqrt(s) for an exact non-negative Fraction s (ties to even), by exact comparison.
    The start point is an integer square root of s scaled by 4^k (at least 120 bits), so every range (subnormal to huge)
    starts within an ulp; the loop then moves to the binary64 whose rounding interval contains sqrt(s), by comparing the
    squares of the interval endpoints with s exactly."""
    if s == 0:
        return 0.0
    p, q = s.numerator, s.denominator
    k = max(0, (240 - (p.bit_length() - q.bit_length())) // 2 + 1)
    r = float(Fr(math.isqrt((p << (2 * k)) // q), 1 << k))
    for _ in range(8):
        up, dn = math.nextafter(r, math.inf), math.nextafter(r, 0.0)
        hi = (Fr(r) + Fr(up)) / 2
        lo = (Fr(r) + Fr(dn)) / 2 if r > 0 else Fr(0)
        if s > hi * hi:
            r = up
            continue
        if s < lo * lo:
            r = dn
            continue
        if s == hi * hi or s == lo * lo:  # exact midpoint: ties to even
            other = up if s == hi * hi else dn
            mant = lambda x: struct.unpack('<q', struct.pack('<d', x))[0] & 1
            return r if mant(r) == 0 else other
        return r
    raise RuntimeError('cr_sqrt did not converge')


def cr_norm(values):
    return cr_sqrt(sum(Fr(v) * Fr(v) for v in values))


_BY_ID = {}


def norm_check(doc_plain, row_index):
    """Exact norm check of results[row_index] in the given document."""
    rows = doc_plain['results']
    row = rows[row_index]
    suffix, comps = MAG_KINDS[row['kind']]
    rid = row['id']
    if suffix is not None:
        assert rid.endswith(':' + suffix), rid
        stem = rid[:-(len(suffix) + 1)]
    else:
        stem = rid
    by_id = _BY_ID.get(id(rows))
    if by_id is None or by_id[0] is not rows:
        by_id = (rows, {r['id']: r for r in rows})
        _BY_ID.clear()
        _BY_ID[id(rows)] = by_id
    by_id = by_id[1]
    want = [stem + ':' + c for c in comps]
    missing = [w for w in want if w not in by_id]
    if missing:
        return dict(ok=False, why='components missing: %s' % missing)
    srr = row.get('source_result_refs')
    if srr is not None and not set(want) <= set(srr):
        return dict(ok=False, why='components not among source_result_refs')
    comp_rows = [by_id[w] for w in want]
    units = {r['unit'] for r in comp_rows}
    if units != {row['unit']}:
        return dict(ok=False, why='unit mismatch %s vs %s' % (units, row['unit']))
    if any(r.get('entity_ref') != row.get('entity_ref') or r.get('basis_ref') != row.get('basis_ref') for r in comp_rows):
        return dict(ok=False, why='entity/basis mismatch')
    vals = [float(r['value']) for r in comp_rows]
    cr = cr_norm(vals)
    return dict(ok=(cr == float(row['value'])), components={w.rsplit(':', 1)[1]: v for w, v in zip(want, vals)},
                cr_norm=repr(cr), cand=repr(float(row['value'])))


def compare(base_text, cand_text):
    """Returns (verdict, items). verdict: 'identical', 'norm_only' (every difference a <=1-ulp magnitude move whose candidate
    value is the correctly rounded norm, plus hash strings listed for the caller), or 'OTHER'."""
    if base_text == cand_text:
        return 'identical', []
    try:
        lb, lc = lex(base_text), lex(cand_text)
        pb, pc = parse(base_text), parse(cand_text)
    except Exception as e:  # not JSON on either side
        return 'OTHER', [dict(why='not comparable as JSON: %s' % e)]
    if len(lb) != len(lc):
        return 'OTHER', [dict(why='lexeme count differs %d vs %d' % (len(lb), len(lc)))]
    vb = [x for x in lb if x[0] in ('s', 'n', 'l')]
    lv_b, lv_c = list(leaves(pb)), list(leaves(pc))
    assert len(vb) == len(lv_b), ('leaf/lexeme alignment', len(vb), len(lv_b))
    vi, items, other = 0, [], []
    cand_plain = None
    for (tb, xb), (tc, xc) in zip(lb, lc):
        is_value = tb in ('s', 'n', 'l')
        if (tb, xb) != (tc, xc):
            if not is_value or tb != tc:
                other.append(dict(why='non-value lexeme differs', base=xb[:200], cand=xc[:200]))
            else:
                path_b, path_c = lv_b[vi][0], lv_c[vi][0]
                if path_b != path_c:
                    other.append(dict(why='path differs', base=str(path_b), cand=str(path_c)))
                elif tb == 'n':
                    if cand_plain is None:
                        cand_plain = to_plain(pc)
                        base_plain = to_plain(pb)
                    p = path_b
                    if len(p) == 3 and p[0] == 'results' and p[2] == 'value' and cand_plain['results'][p[1]]['kind'] in MAG_KINDS:
                        row = cand_plain['results'][p[1]]
                        u = ulps(float(xb), float(xc))
                        nc = norm_check(cand_plain, p[1])
                        nb = norm_check(base_plain, p[1])
                        item = dict(path='/results/%d/value' % p[1], id=row['id'], kind=row['kind'], unit=row['unit'],
                                    base=xb, cand=xc, ulps=u, norm_ok=nc['ok'], base_is_cr=nb.get('ok'),
                                    components=nc.get('components'), cr_norm=nc.get('cr_norm'), why=nc.get('why'))
                        items.append(item)
                        if u > 1 or not nc['ok']:
                            other.append(dict(item, why='magnitude fails the rule: %s' % (item.get('why') or ('%d ulp' % u if u > 1 else 'candidate is not the correctly rounded norm'))))
                    else:
                        other.append(dict(why='non-magnitude number differs', path='/'.join(map(str, p)), base=xb, cand=xc))
                elif tb == 's' and HEX64.match(xb) and HEX64.match(xc) and re.search(r'sha256|hash|digest', str(path_b[-1])):
                    items.append(dict(path='/'.join(map(str, path_b)), hash_field=True, base=xb.strip('"'), cand=xc.strip('"')))
                else:
                    other.append(dict(why='value differs', path='/'.join(map(str, path_b)), base=xb[:200], cand=xc[:200]))
        if is_value:
            vi += 1
    if other:
        return 'OTHER', items + [dict(OTHER=True, **o) for o in other]
    return 'norm_only', items


if __name__ == '__main__':
    import sys
    v, items = compare(open(sys.argv[1]).read(), open(sys.argv[2]).read())
    print(v)
    for it in items:
        print(json.dumps(it, ensure_ascii=False))
