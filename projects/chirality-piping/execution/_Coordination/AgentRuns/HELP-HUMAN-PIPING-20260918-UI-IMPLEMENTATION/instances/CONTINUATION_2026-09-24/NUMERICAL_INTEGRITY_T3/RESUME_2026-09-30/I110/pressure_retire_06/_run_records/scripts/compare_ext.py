#!/usr/bin/env python3
"""I110 round 6: byte comparison against B under ROOT's extended check (r6 harness rows).
Each output of each row is classed against B's raw SHA:
  equal     - the same bytes;
  declared  - differs only in declared strings (norm == B);
  receipt   - differs only in declared strings and the source-block receipt's two digests, recomputed by
              the product's rule from the normalized content (norm_receipt == B; ROOT's extended check);
  document  - a runner export document: differs only in declared strings, the embedded receipt digests and
              the document's own two source bindings (source checksum, derivative hash), each recomputed by
              the product's rule (doc_ext.norm_document == B; beyond ROOT's two digests, reported separately);
  other     - anything else.
Usage: compare_ext.py <B.jsonl> <C.jsonl> [out.json]"""
import json, sys, collections
def load(p): return {(r['label'], r['mode']): r for r in map(json.loads, open(p))}
b, c = load(sys.argv[1]), load(sys.argv[2])
def outputs(r):
    return {'ordinary': r['ordinary'].get('sha') or r['ordinary'].get('error'),
            'mechanics': r['runner'].get('mechanics'), 'document': r['runner'].get('document'),
            'unavailability': json.dumps(r['runner'].get('unavailability'), sort_keys=True),
            'runner_error': r['runner'].get('error'),
            'retained': r['retained'].get('sha') or r['retained'].get('error'), 'retained_kind': r['retained'].get('kind')}
order = ['equal', 'declared', 'receipt', 'document', 'other']
rows = collections.Counter(); outs = collections.Counter(); detail = []; rule_fail = []
for k in sorted(set(b) | set(c)):
    rb, rc = b.get(k), c.get(k)
    if rb is None or rc is None:
        rows[('missing', 'other')] += 1; detail.append({'row': k, 'missing': True}); continue
    ob, oc = outputs(rb), outputs(rc)
    worst = 'equal'
    for name in ob:
        if ob[name] == oc[name]: cls = 'equal'
        else:
            t = rc.get('texts', {}).get(name, {})
            de = rc.get('texts', {}).get('doc_ext', {})
            if t.get('norm') == ob[name]: cls = 'declared'
            elif t.get('norm_receipt') == ob[name] and t.get('rule_holds'): cls = 'receipt'
            elif name == 'document' and de.get('norm_document') == ob[name] and de.get('rules_hold'): cls = 'document'
            else: cls = 'other'
            if t.get('rule_holds') is False and name != 'document': rule_fail.append((k, name))
            detail.append({'set': rb['set'], 'label': k[0], 'mode': k[1], 'output': name, 'class': cls})
        outs[(rb['set'], name, cls)] += 1
        if order.index(cls) > order.index(worst): worst = cls
    rows[(rb['set'], worst)] += 1
summary = {'rows_by_set_and_worst_class': {f'{s}/{w}': n for (s, w), n in sorted(rows.items())},
           'outputs_by_set_name_class': {f'{s}/{n}/{w}': v for (s, n, w), v in sorted(outs.items()) if w != 'equal'},
           'receipt_rule_failures_on_candidate_outputs': rule_fail, 'not_equal_outputs': detail}
print(json.dumps(summary['rows_by_set_and_worst_class']))
print(json.dumps(summary['outputs_by_set_name_class']))
print('other:', [d for d in detail if d.get('class') == 'other' or d.get('missing')][:10])
if len(sys.argv) > 3: json.dump(summary, open(sys.argv[3], 'w'), indent=1)
