"""RV123: recompute the exact successors' receipt, preparation (route H) and source-identity hashes,
and DEF-E's H, with a JCS canonicalizer for float-free JSON (B3-D's `canonical`)."""
import json, hashlib, sys
root = sys.argv[1]
def canonical(v): return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
def h(domain, payload): return hashlib.sha256(canonical({"domain": domain, "payload": payload})).hexdigest()
def floats(v):
    if isinstance(v, float): return 1
    if isinstance(v, dict): return sum(floats(x) for x in v.values())
    if isinstance(v, list): return sum(floats(x) for x in v)
    return 0
he = h('retained_precision_formation_v1', json.load(open(f'{root}/fixtures/results/retained_precision_prepared_exact_v1.json')))
ho = h('retained_precision_formation_v1', json.load(open(f'{root}/fixtures/results/retained_precision_prepared_ordinary_v1.json')))
print('H(DEF-E)', he); print('H(DEF-O)', ho)
for mode in ['sparse_interactive', 'dense_scrutiny']:
    d = json.load(open(f'{root}/fixtures/results/retained_precision_exact_successor_{mode}.json'))['source']
    r = d['retained_precision']; b = r['body']
    assert floats(b) == 0
    print(mode, 'receipt', h('retained_precision_receipt_mp_v2', b) == r['receipt_sha256'])
    for s in b['sources']:
        a = b['product_attempts'][s['preparation']['attempt_ref']]
        members = [{"member": m["member"], "old_source": m["old_source"], "old_facts": m["old_facts"], "section": m["result"]["section"]} for m in a['preparation']['members']]
        pay = lambda H: {"definition_id": a["definition_id"], "definition_sha256": H, "owner_ref": a["owner_ref"], "ordinary_attempt_ref": a["ordinary_attempt_ref"], "material_basis_ref": a["material_basis_ref"], "members": members}
        print(mode, 'preparation DEF-E', h('retained_precision_preparation_v1', pay(he)) == s['preparation']['sha256'], 'DEF-O', h('retained_precision_preparation_v1', pay(ho)) == s['preparation']['sha256'])
    for c in b['cases']:
        if 'source_identity_sha256' in c:
            x = dict(b['sources'][c['source_ref']]); x.pop('index')
            print(mode, 'source identity', h('retained_precision_source_mp_v2', x) == c['source_identity_sha256'])
