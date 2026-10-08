#!/usr/bin/env python3
"""I112 (PR-N gates): normdiff for large envelopes (the gate's full envelopes reach 400 MB). Same acceptance rule as
normdiff.py, with a structure walk that keeps memory small:

* the top-level object of each side is walked key by key with json.JSONDecoder.raw_decode; every array value is walked element
  by element; the bytes between values (keys, separators, brackets) are compared exactly, so the two documents are accounted for
  byte for byte;
* identical elements are skipped by comparing their exact byte spans; each differing element is parsed alone and compared
  leaf by leaf with normdiff's lexeme accounting (normdiff.lex / normdiff.leaves);
* a differing element of `results` must differ only in its `value`, the row must be a published magnitude kind, the move at most
  one ulp, and the candidate's value the correctly rounded Euclidean norm of the same envelope's own component rows (found by id,
  each id occurring exactly once), checked exactly with normdiff.cr_norm (Fractions);
* a differing element of `diagnostics` is reported as DIAG with every differing number token of its text fields (base, cand, ulps)
  and must otherwise be identical; DIAG is outside the brief's rule (a stop) and is returned for separate analysis;
* anything else is OTHER.
"""
import ctypes
import ctypes.util
import json
import re

import normdiff as N

# this host's libm hypot (what Rust's f64::hypot calls on macOS), to show that each base value is the libm chain
_LIBM = ctypes.CDLL(ctypes.util.find_library('m'))
_LIBM.hypot.restype = ctypes.c_double
_LIBM.hypot.argtypes = [ctypes.c_double, ctypes.c_double]


def libm_chain(vals):
    r = _LIBM.hypot(vals[0], vals[1])
    for v in vals[2:]:
        r = _LIBM.hypot(r, v)
    return r

DEC = json.JSONDecoder()
WS = re.compile(r'[ \t\r\n]*')
NUMTOK = re.compile(r'-?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?')


def _ws(t, i):
    return WS.match(t, i).end()


def _expect(t, i, ch):
    i = _ws(t, i)
    if t[i] != ch:
        raise ValueError('expected %r at %d, got %r' % (ch, i, t[i:i + 20]))
    return i + 1


def top_spans(t):
    """The top-level object as an exact partition of the text: ('#gap', text) for everything between values (braces, keys,
    colons, commas, whitespace), ('#value', key, start, end) for a non-array value, ('#elem', key, index, start, end) for each
    element of an array value. The partition is checked to cover the text exactly."""
    out = []
    i = _ws(t, 0)
    if t[i] != '{':
        raise ValueError('not an object')
    pos, i, first = 0, i + 1, True
    while True:
        j = _ws(t, i)
        if t[j] == '}':
            out.append(('#gap', t[pos:j + 1]))
            if t[j + 1:].strip():
                raise ValueError('trailing data')
            out.append(('#gap', t[j + 1:]))
            break
        if not first:
            if t[j] != ',':
                raise ValueError('expected , at %d' % j)
            j = _ws(t, j + 1)
        key, k_end = DEC.raw_decode(t, j)
        c = _ws(t, k_end)
        if t[c] != ':':
            raise ValueError('expected : at %d' % c)
        v = _ws(t, c + 1)
        if t[v] == '[':
            out.append(('#gap', t[pos:v + 1]))
            e, n = v + 1, 0
            while True:
                e2 = _ws(t, e)
                if t[e2] == ']':
                    out.append(('#gap', t[e:e2 + 1]))
                    i = pos = e2 + 1
                    break
                if n:
                    if t[e2] != ',':
                        raise ValueError('expected , in array at %d' % e2)
                    e2 = _ws(t, e2 + 1)
                out.append(('#gap', t[e:e2]))
                _, end = DEC.raw_decode(t, e2)
                out.append(('#elem', key, n, e2, end))
                e, n = end, n + 1
        else:
            out.append(('#gap', t[pos:v]))
            _, end = DEC.raw_decode(t, v)
            out.append(('#value', key, v, end))
            i = pos = end
        first = False
    covered = sum(len(x[1]) if x[0] == '#gap' else x[-1] - x[-2] for x in out)
    if covered != len(t):
        raise ValueError('partition covers %d of %d characters' % (covered, len(t)))
    return out


def _diff_text(tb, tc):
    """Leaf-level differences of two small JSON texts: [(path, base_lexeme, cand_lexeme)] or raises on structure differences."""
    lb, lc = N.lex(tb), N.lex(tc)
    if len(lb) != len(lc):
        return None
    lv = list(N.leaves(N.parse(tb)))
    lv2 = list(N.leaves(N.parse(tc)))
    out, vi = [], 0
    for xb, xc in zip(lb, lc):
        isv = xb[0] in ('s', 'n', 'l')
        if xb != xc:
            if not isv or xb[0] != xc[0] or lv[vi][0] != lv2[vi][0]:
                return None
            out.append((lv[vi][0], xb, xc))
        if isv:
            vi += 1
    return out


ID_AT = re.compile(r'\{\s*"id"\s*:\s*("(?:[^"\\\\]|\\\\.)*")')


def _component_ids(row):
    suffix, comps = N.MAG_KINDS[row['kind']]
    rid = row['id']
    if suffix is not None:
        if not rid.endswith(':' + suffix):
            return None
        rid = rid[:-(len(suffix) + 1)]
    return [rid + ':' + c for c in comps]


def _index_rows(t, spans, wanted):
    """id -> [row, count] for the wanted ids among the `results` elements (one regex match per element)."""
    found = {}
    for x in spans:
        if x[0] == '#elem' and x[1] == 'results':
            m = ID_AT.match(t, x[3])
            if m is None:
                continue
            rid = json.loads(m.group(1))
            if rid in wanted:
                if rid in found:
                    found[rid][1] += 1
                else:
                    found[rid] = [json.loads(t[x[3]:x[4]]), 1]
    return found


def _norm_check(found, row):
    want = _component_ids(row)
    if want is None:
        return dict(ok=False, why='id suffix')
    rows = []
    for w in want:
        if w not in found:
            return dict(ok=False, why='component row %s not found' % w)
        if found[w][1] != 1:
            return dict(ok=False, why='component row %s not unique' % w)
        rows.append(found[w][0])
    srr = row.get('source_result_refs')
    if srr is not None and not set(want) <= set(srr):
        return dict(ok=False, why='components not among source_result_refs')
    if {r['unit'] for r in rows} != {row['unit']}:
        return dict(ok=False, why='unit mismatch')
    if any(r.get('entity_ref') != row.get('entity_ref') or r.get('basis_ref') != row.get('basis_ref') for r in rows):
        return dict(ok=False, why='entity/basis mismatch')
    vals = [float(r['value']) for r in rows]
    cr = N.cr_norm(vals)
    return dict(ok=(cr == float(row['value'])), components={w.rsplit(':', 1)[1]: v for w, v in zip(want, vals)},
                cr_norm=repr(cr), libm_chain=repr(libm_chain(vals)), is_libm_chain=(libm_chain(vals) == float(row['value'])))


def _num_tokens_diff(sb, sc):
    """Differing number tokens of two strings whose non-number text is identical; None if the text differs otherwise."""
    pb, pc = NUMTOK.split(sb), NUMTOK.split(sc)
    nb, nc = NUMTOK.findall(sb), NUMTOK.findall(sc)
    if pb != pc or len(nb) != len(nc):
        return None
    out = []
    for i, (x, y) in enumerate(zip(nb, nc)):
        if x != y:
            fx, fy = float(x), float(y)
            out.append(dict(index=i, base=x, cand=y, ulps=N.ulps(fx, fy),
                            context=(pb[i][-80:] + '|' + pb[i + 1][:40])))
    return out


def compare(bb, bc):
    """bb, bc: bytes. Returns (verdict, items) with verdict 'identical', 'norm_only', 'DIAG' (diagnostic-text numbers only,
    besides norm_only moves) or 'OTHER'."""
    if bb == bc:
        return 'identical', []
    tb, tc = bb.decode('utf-8'), bc.decode('utf-8')
    try:
        sb, sc = top_spans(tb), top_spans(tc)
    except Exception as e:
        return 'OTHER', [dict(OTHER=True, why='structure walk failed: %s' % e)]
    if len(sb) != len(sc):
        return 'OTHER', [dict(OTHER=True, why='structure differs (%d vs %d spans)' % (len(sb), len(sc)))]
    items, verdict = [], 'norm_only'
    for xb, xc in zip(sb, sc):
        if xb[0] != xc[0]:
            return 'OTHER', items + [dict(OTHER=True, why='span kinds differ')]
        if xb[0] == '#gap':
            if xb[1] != xc[1]:
                return 'OTHER', items + [dict(OTHER=True, why='bytes between values differ: %r vs %r' % (xb[1][:80], xc[1][:80]))]
            continue
        if xb[0] == '#value':
            vb, vc = tb[xb[2]:xb[3]], tc[xc[2]:xc[3]]
            if xb[1] != xc[1]:
                return 'OTHER', items + [dict(OTHER=True, why='keys differ')]
            if vb != vc:
                d = _diff_text(vb, vc)
                items.append(dict(OTHER=True, why='top-level value %s differs' % xb[1],
                                  leaves=[('/'.join(map(str, p)), b[1][:120], c[1][:120]) for p, b, c in (d or [])][:20]))
                verdict = 'OTHER'
            continue
        # array element
        key = xb[1]
        eb, ec = tb[xb[3]:xb[4]], tc[xc[3]:xc[4]]
        if key != xc[1] or xb[2] != xc[2]:
            return 'OTHER', items + [dict(OTHER=True, why='element alignment')]
        if eb == ec:
            continue
        d = _diff_text(eb, ec)
        if d is None:
            items.append(dict(OTHER=True, why='element %s[%d] differs structurally' % (key, xb[2])))
            verdict = 'OTHER'
            continue
        if key == 'results' and all(p == ('value',) and b[0] == 'n' for p, b, c in d):
            row_c = json.loads(ec)
            row_b = json.loads(eb)
            if row_c['kind'] not in N.MAG_KINDS:
                items.append(dict(OTHER=True, why='non-magnitude result value differs', id=row_c['id'], kind=row_c['kind'],
                                  base=d[0][1][1], cand=d[0][2][1]))
                verdict = 'OTHER'
                continue
            u = N.ulps(float(d[0][1][1]), float(d[0][2][1]))
            it = dict(path='/results/%d/value' % xb[2], id=row_c['id'], kind=row_c['kind'], unit=row_c['unit'],
                      base=d[0][1][1], cand=d[0][2][1], ulps=u, _rows=(row_b, row_c))
            items.append(it)
            continue
        if key == 'diagnostics':
            db, dc = json.loads(eb), json.loads(ec)
            fields = sorted(f for f in set(db) | set(dc) if db.get(f) != dc.get(f))
            nums, ok = [], True
            for f in fields:
                if not (isinstance(db.get(f), str) and isinstance(dc.get(f), str)):
                    ok = False
                    break
                t = _num_tokens_diff(db[f], dc[f])
                if t is None:
                    ok = False
                    break
                nums += [dict(field=f, **x) for x in t]
            it = dict(DIAG=True, path='/diagnostics/%d' % xb[2], code=dc.get('code'), severity=dc.get('severity'),
                      id=dc.get('id'), fields=fields, numbers=nums)
            if not ok:
                it['OTHER'] = True
                it['why'] = 'diagnostic differs beyond number tokens'
                verdict = 'OTHER'
            elif verdict == 'norm_only':
                verdict = 'DIAG'
            items.append(it)
            continue
        items.append(dict(OTHER=True, why='element %s[%d] differs' % (key, xb[2]),
                          leaves=[('/'.join(map(str, p)), b[1][:120], c[1][:120]) for p, b, c in d][:20]))
        verdict = 'OTHER'
    # the norm checks: one indexing pass per side over the results elements, for the component ids needed
    mags = [it for it in items if '_rows' in it]
    if mags:
        wanted = set()
        for it in mags:
            wanted |= set(_component_ids(it['_rows'][1]) or [])
        fb, fc = _index_rows(tb, sb, wanted), _index_rows(tc, sc, wanted)
        for it in mags:
            row_b, row_c = it.pop('_rows')
            nc, nb = _norm_check(fc, row_c), _norm_check(fb, row_b)
            it.update(norm_ok=nc['ok'], base_is_cr=nb.get('ok'), components=nc.get('components'), cr_norm=nc.get('cr_norm'),
                      base_is_libm_chain=nb.get('is_libm_chain'), base_components_equal=(nb.get('components') == nc.get('components')),
                      why=nc.get('why'))
            if it['ulps'] > 1 or not nc['ok'] or not it['base_components_equal']:
                it['OTHER'] = True
                it['rule_failure'] = ('%d ulp' % it['ulps']) if nc['ok'] and it['base_components_equal'] else 'norm check'
                verdict = 'OTHER'
    return verdict, items
