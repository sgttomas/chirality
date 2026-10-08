"""RV123 round 2: independent checks of every dumped B2-P witness successor (outside PP): SCHEMA,
the hashes (receipt, publication, sources, CombinationSource operand identities, preparation and
operand-preparation bindings), the orders B2-C §2.7 fixes, diagnostics, R-COMB-1's producer side,
headlines, the combination magnitudes, and the linear consistency of selected combinations."""
import json, hashlib, sys, struct, math, glob
from fractions import Fraction as F
from jsonschema import Draft202012Validator
P, D = sys.argv[1], sys.argv[2]
def canonical(v): return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
def ecma(x):
    if x == 0: return "0"
    if x < 0: return "-" + ecma(-x)
    r = repr(x); m, _, e = r.partition("e"); e = int(e) if e else 0
    ip, _, fp = m.partition("."); fp = fp.rstrip("0") if fp != "0" else ""
    digits = (ip + fp).lstrip("0"); lead = len(ip.lstrip("0")) if ip.lstrip("0") else -(len(fp) - len(fp.lstrip("0")))
    n = e + lead; digits = digits.rstrip("0"); k = len(digits)
    if k <= n <= 21: return digits + "0" * (n - k)
    if 0 < n <= 21: return digits[:n] + "." + digits[n:]
    if -6 < n <= 0: return "0." + "0" * (-n) + digits
    ex = n - 1; sign = "+" if ex >= 0 else "-"
    return (digits[0] + ("." + digits[1:] if k > 1 else "")) + "e" + sign + str(abs(ex))
def jcs(v):
    if isinstance(v, bool) or v is None: return json.dumps(v)
    if isinstance(v, int): return str(v)
    if isinstance(v, float): return ecma(v)
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list): return "[" + ",".join(jcs(x) for x in v) + "]"
    keys = sorted(v, key=lambda k: k.encode("utf-16-be"))
    return "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + jcs(v[k]) for k in keys) + "}"
def hj(domain, payload): return hashlib.sha256(jcs({"domain": domain, "payload": payload}).encode()).hexdigest()
for t, want in [(1.0,"1"),(0.5,"0.5"),(1e-7,"1e-7"),(1.5e21,"1.5e+21"),(123456789012345680000.0,"123456789012345680000"),(0.000001,"0.000001"),(2.5e-6,"0.0000025"),(1e21,"1e+21"),(-0.0,"0"),(3.14e-300,"3.14e-300")]:
    assert ecma(t) == want, (t, ecma(t), want)
def h(domain, payload): return hashlib.sha256(canonical({"domain": domain, "payload": payload})).hexdigest()
schema = json.load(open(f'{P}/schemas/retained_precision_mp_v2.schema.json')); V = Draft202012Validator(schema)
rr = dict(schema['$defs']['RawRow']); rr['$defs'] = schema['$defs']; VR = Draft202012Validator(rr)
DEFO = h('retained_precision_formation_v1', json.load(open(f'{P}/fixtures/results/retained_precision_prepared_ordinary_v1.json')))
DEFC = h('retained_precision_formation_v1', json.load(open(f'{P}/fixtures/results/retained_precision_prepared_combination_v1.json')))
def bits(x): return struct.pack('>d', x).hex()
def rn_sqrt(S):
    if S == 0: return 0.0
    y = math.sqrt(float(S))
    for c in sorted({math.nextafter(math.nextafter(y, 0), 0), math.nextafter(y, 0), y, math.nextafter(y, math.inf), math.nextafter(math.nextafter(y, math.inf), math.inf)}):
        if c <= 0: continue
        lo = (F(c) + F(math.nextafter(c, 0))) / 2; hi = (F(c) + F(math.nextafter(c, math.inf))) / 2
        if lo * lo < S < hi * hi or ((lo * lo == S or hi * hi == S) and struct.unpack('>Q', struct.pack('>d', c))[0] % 2 == 0): return c
    raise AssertionError
def prep_payload(a, H, purpose=None):
    members = [{"member": m["member"], "old_source": m["old_source"], "old_facts": m["old_facts"], "section": m["result"]["section"]} for m in a['preparation']['members']]
    p = {"definition_id": a["definition_id"], "definition_sha256": H, "owner_ref": a["owner_ref"], "ordinary_attempt_ref": a["ordinary_attempt_ref"], "material_basis_ref": a["material_basis_ref"], "members": members}
    if purpose: p["purpose"] = purpose
    return p
def ident(s):
    x = dict(s); x.pop('index'); return h('retained_precision_source_mp_v2', x)
fails = []
def check(ok, what):
    if not ok: fails.append(what)
for path in sorted(glob.glob(f'{D}/*.successor.json')):
    doc = json.load(open(path)); name = path.rsplit('/', 1)[-1].replace('.successor.json', '')
    s = doc['source']; r = s['retained_precision']; b = r['body']; model = doc['invocation']['request']['model']
    plain = json.load(open(path.replace('.successor.json', '.plain.json')))
    L = lambda w: f'{name}: {w}'
    check(not list(V.iter_errors(r)), L('SCHEMA receipt')); check(all(not list(VR.iter_errors(x)) for x in s['results']), L('SCHEMA rows'))
    check(h('retained_precision_receipt_mp_v2', b) == r['receipt_sha256'], L('receipt hash'))
    pub = dict(s); pub.pop('retained_precision'); check(hj('retained_precision_publication_mp_v2', pub) == b['publication_sha256'], L('publication hash'))
    srcs = b['sources']; check([x['index'] for x in srcs] == list(range(len(srcs))), L('sources index = position'))
    kinds = [x['owner']['kind'] for x in srcs]
    check(kinds == sorted(kinds, key=lambda k: 0 if k == 'case' else 1), L('case sources before combination sources'))
    # case sources: batch ones (preparation.attempt_ref) before operand-prepared ones (operand_preparation_ref)
    case_srcs = [x for x in srcs if x['owner']['kind'] == 'case']
    tags = ['a' if 'attempt_ref' in (x.get('preparation') or {}) else 'o' for x in case_srcs]
    check(tags == sorted(tags), L('batch case sources before operand-prepared ones'))
    for x in srcs:
        p = x.get('preparation')
        if p and 'attempt_ref' in p:
            a = b['product_attempts'][p['attempt_ref']]
            if all(m['result']['kind'] == 'prepared' for m in a['preparation']['members']):
                check(h('retained_precision_preparation_v1', prep_payload(a, DEFO)) == p['sha256'], L('case preparation hash (DEF-O)'))
        if p and 'operand_preparation_ref' in p:
            rec = b['operand_preparations'][p['operand_preparation_ref']]
            check(rec['source_ref'] == x['index'] and rec['owner_ref']['index'] == x['owner']['case_index'], L('operand preparation <-> source'))
            check(h('retained_precision_operand_preparation_v1', prep_payload(rec, DEFO, 'combination_operand')) == p['sha256'], L('operand preparation hash'))
    for i, rec in enumerate(b.get('operand_preparations', [])):
        check(rec['id'] == i and rec['definition_id'] == 'RP-PREPARED-ORDINARY-DUAL-v1', L('operand preparation id/definition'))
        check(rec['requested_by'] == sorted(set(rec['requested_by'])), L('requested_by ascending unique'))
    check('operand_preparations' not in b or len(b['operand_preparations']) > 0, L('C-6 absent when empty'))
    # calls: consecutive ids, meter chain, charged
    calls = b['calls']; check([c['id'] for c in calls] == list(range(len(calls))), L('call ids'))
    check(calls[0]['kind'] == 'case_batch' and all(c['kind'] == 'mechanics_combination' for c in calls[1:]), L('call kinds'))
    check(all(calls[i]['invocation_before'] == calls[i - 1]['invocation_after'] for i in range(1, len(calls))), L('meter chain'))
    check(b['work']['charged'] == calls[-1]['invocation_after'], L('charged = last call after'))
    # combinations: one per model combination, authored order
    combos = b['combinations']; mc = model.get('combinations', [])
    check([c['basis_ref']['ref_id'] for c in combos] == [m['id'] for m in mc], L('combinations order'))
    attempts = b['product_attempts']
    ncase_attempts = sum(1 for a in attempts if a['owner_ref']['kind'] == 'case')
    check(all(a['owner_ref']['kind'] == 'case' for a in attempts[:ncase_attempts]), L('case attempts first'))
    check([a['id'] for a in attempts] == list(range(len(attempts))), L('attempt ids'))
    called = [k for k, c in enumerate(combos) if c.get('call_ref') is not None]
    for c in combos:
        cid = c['basis_ref']['ref_id']; rows_c = [x for x in s['results'] if x['basis_ref']['ref_type'] == 'combination' and x['basis_ref']['ref_id'] == cid]
        check(c['result_ids'] == [x['id'] for x in rows_c], L(f'{cid} result_ids'))
        plain_rows = {x['id']: x for x in plain['results']}
        if c['disposition'] == 'retained_selected':
            check(all(x.get('recovery_method') == 'contribution_preserving_multiprecision_v1' for x in rows_c), L(f'{cid} method on selected rows'))
            src = srcs[c['source_ref']]
            check(src['owner'] == {"kind": "combination", "combination_index": combos.index(c), "combination_id": cid}, L(f'{cid} CombinationSource owner'))
            check(src['representative_source_ref'] == src['operands'][0]['source_ref'], L(f'{cid} representative'))
            for op in src['operands']:
                check(op['source_identity_sha256'] == ident(srcs[op['source_ref']]), L(f'{cid} operand identity'))
            check(c['source_identity_sha256'] == ident(src), L(f'{cid} source identity'))
            check(src['ledger_sha256'] == c['selection']['ledger_sha256'], L(f'{cid} ledger = selection ledger'))
            st = srcs[src['operands'][0]['source_ref']]['stiffness_sha256']
            check(src['stiffness_sha256'] == st and all(srcs[o['source_ref']]['stiffness_sha256'] == st for o in src['operands']), L(f'{cid} stiffness equal'))
            run = c['run']; check(run['origin']['owner_ref'] == {"kind": "combination", "index": combos.index(c)}, L(f'{cid} run owner'))
            att = attempts[c['product_attempt_ref']]; check(att['definition_id'] == 'RP-PREPARED-COMBINATION-DUAL-v1' and att['owner_ref'] == {"kind": "combination", "index": combos.index(c)}, L(f'{cid} attempt'))
            # option (ii): displacement magnitude = RN64 of the exact 3-norm of the published translations
            byn = {}
            for x in rows_c: byn.setdefault(x['entity_ref'], {})[x['kind']] = x['value']
            for n, k in byn.items():
                if 'displacement_magnitude' in k:
                    e = rn_sqrt(sum(F(k[t]) ** 2 for t in ['global_nodal_displacement_x', 'global_nodal_displacement_y', 'global_nodal_displacement_z']))
                    check(bits(e) == bits(k['displacement_magnitude']), L(f'{cid} {n} exact-norm magnitude'))
        else:
            check(all('recovery_method' not in x for x in rows_c), L(f'{cid} no method on non-selected rows'))
            check(all(x['value'] == plain_rows[x['id']]['value'] for x in rows_c), L(f'{cid} R-COMB-1: ordinary values'))
    # execution_order: case Runs then combination Runs, combination by authored index
    eo = b['work']['execution_order']
    check(eo == sorted(eo, key=lambda o: 0 if o['kind'] == 'case' else 1), L('execution order'))
    check([o['index'] for o in eo if o['kind'] == 'combination'] == [k for k, c in enumerate(combos) if c.get('run')], L('combination runs by authored index'))
    # diagnostics: combination diagnostics after the case diagnostics, only for retained ones
    rp_diags = [d for d in s['diagnostics'] if d['code'].startswith('RETAINED_PRECISION_')]
    case_ids = [c['id'] for c in model['load_cases']]
    order = ['case' if d['affected_refs'][0] in case_ids else 'combination' for d in rp_diags]
    check(order == sorted(order), L('case diagnostics before combination diagnostics'))
    check(sorted(d['affected_refs'][0] for d in rp_diags if d['affected_refs'][0] not in case_ids) == sorted(c['basis_ref']['ref_id'] for c in combos if c['disposition'].startswith('retained')), L('combination diagnostics = retained'))
    # headlines over load-case rows
    for key in ['max_displacement', 'max_open_formula_stress']:
        hl = s['summary'].get(key)
        if hl: check(next(x for x in s['results'] if x['id'] == hl['result_ref'])['basis_ref']['ref_type'] == 'load_case', L(f'{key} is a load-case row'))
    # linear consistency of a selected combination of selected cases: comb ~ sum f_i * case_i, row by row
    for k, c in enumerate(combos):
        if c['disposition'] != 'retained_selected': continue
        terms = mc[k]['terms']; st = {x['basis_ref']['ref_id']: x['status'] for x in b['cases']}
        if not all(st[t['load_case']] == 'selected' for t in terms): continue
        def base_id(rid, case): return rid
        rows_by = {(x['basis_ref']['ref_id'], x['entity_ref'], x['kind'], (x.get('metadata') or {}).get('component'), (x.get('metadata') or {}).get('location')): x['value'] for x in s['results']}
        worst = 0.0; scale = {}
        for (ref, ent, kind, comp, loc), v in rows_by.items():
            if ref != c['basis_ref']['ref_id'] or 'magnitude' in kind: continue
            parts = [rows_by.get((t['load_case'], ent, kind, comp, loc)) for t in terms]
            if any(p is None for p in parts): continue
            lin = sum(t['factor'] * p for t, p in zip(terms, parts))
            scale[kind] = max(scale.get(kind, 0.0), abs(v), *(abs(p) for p in parts))
            worst = max(worst, abs(v - lin) / max(scale[kind], 1e-300))
        print(f'{name}: {c["basis_ref"]["ref_id"]} linear consistency worst |comb - sum f*case| / kind scale = {worst:.3e}')
    zero = [x['value'] for x in s['results'] if x['basis_ref']['ref_type'] == 'combination' and x.get('recovery_method')]
    if name.startswith('w_cb1z'):
        print(f'{name}: selected combination rows: {len(zero)}, nonzero {sum(1 for v in zero if v != 0)}, max |v| {max(map(abs, zero)) if zero else 0}; plain nonzero {sum(1 for x in plain["results"] if x["basis_ref"]["ref_type"] == "combination" and x["value"] != 0)}')
    print(f'{name}: dispositions {[c["disposition"] for c in combos]} cases {[c["status"] for c in b["cases"]]} calls {len(calls)} sources {len(srcs)} oppreps {len(b.get("operand_preparations", []))} precommit_today {doc.get("precommit_today")}')
print('FAILS', len(fails)); [print(' ', f) for f in fails[:40]]
