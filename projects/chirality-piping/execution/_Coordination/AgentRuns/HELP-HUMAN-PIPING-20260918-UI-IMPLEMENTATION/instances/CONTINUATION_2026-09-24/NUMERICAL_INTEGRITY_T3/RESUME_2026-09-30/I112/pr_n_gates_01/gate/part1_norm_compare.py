#!/usr/bin/env python3
"""I112 PR-N both-entry gate part 1: run-by-run comparison of base B and candidate C under the brief's acceptance rule (new;
it complements KF2's compare_gate_kf2.py, which requires identity and so reports every norm move as a difference).

For every run key (case, mode, entry):
  runs.jsonl  streamed as bytes; each record line is compared with wall_seconds, peak_rss_kib, memorystatus_level_end and
              probe.run.solve_seconds replaced by a fixed token and probe.run.envelope_sha256 removed (each must occur the
              expected number of times). Where the lines still differ, both records are parsed and the differing fields listed;
              the only accepted residue is probe.run.envelope equal to that side's envelopes/<key>.json (the summary envelope,
              judged below);
  full/       normdiff2.compare: identical, norm_only (every difference a <= 1-ulp published magnitude whose candidate value is
              the exactly computed correctly rounded norm of the same envelope's own components), DIAG (diagnostic text numbers
              besides) or OTHER;
  envelopes/  (the summary span) the same;
  stdout/     byte-identical once the candidate's run.solve_seconds and run.envelope_sha256 value texts and its summary span are
              replaced by the base's (each occurring once); each envelope_sha256 must be the sha256 of that side's full envelope;
  stderr/     identical.
The brief's rule passes a run only when everything is identical or norm_only. DIAG items and magnitude moves of more than one
ulp are listed with their checks and counted as outside the rule (stops). Writes <out.json> and prints a summary.
Usage: python3 -B part1_norm_compare.py <base-dir> <cand-dir> <normdiff-dir> <out.json>
"""
import collections
import hashlib
import json
import os
import re
import sys

base_dir, cand_dir, nd_dir, out_path = sys.argv[1:5]
sys.path.insert(0, nd_dir)
import normdiff2 as N2  # noqa: E402

NORM_FIELDS = [(re.compile(rb'"wall_seconds": [-0-9.eE+]+'), b'"wall_seconds": X', 1, 1),
               (re.compile(rb'"peak_rss_kib": [-0-9]+'), b'"peak_rss_kib": X', 1, 1),
               (re.compile(rb'"memorystatus_level_end": [-0-9]+'), b'"memorystatus_level_end": X', 1, 1),
               (re.compile(rb'"solve_seconds": [-0-9.eE+]+'), b'"solve_seconds": X', 0, 1)]
ENV_SHA = re.compile(rb'"envelope_sha256": "([0-9a-f]{64})"')
KEY = re.compile(rb'"case": ("(?:[^"\\]|\\.)*"), "mode": ("[^"]*"), "entry": ("[^"]*")')
SOLVE = re.compile(rb'"solve_seconds":(-?[0-9][0-9.eE+-]*)')
ESHA = re.compile(rb'"envelope_sha256":"([0-9a-f]{64})"')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_runs(d):
    out = {}
    with open(os.path.join(d, 'runs.jsonl'), 'rb') as fh:
        for line in fh:
            m = KEY.search(line, max(0, len(line) - 4096))
            k = tuple(json.loads(x) for x in m.groups())
            assert k not in out, k
            norm = line
            for rx, rep, lo, hi in NORM_FIELDS:
                norm, n = rx.subn(rep, norm)
                assert lo <= n <= hi, (k, rep, n)
            es = ENV_SHA.findall(norm)
            assert len(es) <= 1, k
            norm = ENV_SHA.sub(b'"envelope_sha256": X', norm)
            out[k] = (sha(norm), es[0].decode() if es else None)
    return out


def record_residue(k, key):
    """Parses both records of key k and returns the differing fields beyond the masked ones, with probe.run.envelope accepted
    when each side equals its own envelopes/<key>.json."""
    recs = []
    for d in (base_dir, cand_dir):
        with open(os.path.join(d, 'runs.jsonl'), 'rb') as fh:
            for line in fh:
                m = KEY.search(line, max(0, len(line) - 4096))
                if tuple(json.loads(x) for x in m.groups()) == k:
                    recs.append(json.loads(line))
                    break
    a, b = recs
    for r in (a, b):
        for f in ('wall_seconds', 'peak_rss_kib', 'memorystatus_level_end'):
            r.pop(f, None)
        run = r.get('probe', {}).get('run', {})
        run.pop('solve_seconds', None)
        run.pop('envelope_sha256', None)
    residue = []
    for f in sorted(set(a) | set(b)):
        if a.get(f) == b.get(f):
            continue
        if f != 'probe':
            residue.append(f)
            continue
        pa, pb = a['probe'], b['probe']
        for g in sorted(set(pa) | set(pb)):
            if pa.get(g) == pb.get(g):
                continue
            if g != 'run':
                residue.append('probe.' + g)
                continue
            ra, rb_ = pa['run'], pb['run']
            for h in sorted(set(ra) | set(rb_)):
                if ra.get(h) == rb_.get(h):
                    continue
                if h == 'envelope':
                    eb = json.load(open(os.path.join(base_dir, 'envelopes', key + '.json')))
                    ec = json.load(open(os.path.join(cand_dir, 'envelopes', key + '.json')))
                    if ra[h] == eb and rb_[h] == ec:
                        continue
                residue.append('probe.run.' + h)
    return residue


def read(d, sub, name):
    p = os.path.join(d, sub, name)
    return open(p, 'rb').read() if os.path.exists(p) else None


def stdout_check(ob, oc, full_sha_b, full_sha_c, env_b, env_c):
    issues = []
    for side, o in (('base', ob), ('cand', oc)):
        if len(SOLVE.findall(o)) != 1 or len(ESHA.findall(o)) > 1:
            issues.append('stdout %s: unexpected solve_seconds/envelope_sha256 count' % side)
    if issues:
        return issues
    sb = SOLVE.search(ob).group(1)
    eb, ec = ESHA.search(ob), ESHA.search(oc)
    patched = SOLVE.sub(lambda m: b'"solve_seconds":' + sb, oc, count=1)
    if eb and ec:
        patched = ESHA.sub(lambda m: b'"envelope_sha256":"' + eb.group(1) + b'"', patched, count=1)
        if eb.group(1).decode() != full_sha_b or ec.group(1).decode() != full_sha_c:
            issues.append('stdout envelope_sha256 is not the full envelope sha256')
    elif bool(eb) != bool(ec):
        issues.append('stdout envelope_sha256 on one side only')
    if patched != ob and env_b is not None and env_c is not None and env_b != env_c:
        if patched.count(env_c) == 1 and ob.count(env_b) == 1:
            patched = patched.replace(env_c, env_b, 1)
    if patched != ob:
        issues.append('stdout differs beyond run.solve_seconds, run.envelope_sha256 and the summary span')
    return issues


rb, rc = load_runs(base_dir), load_runs(cand_dir)
report = dict(runs_base=len(rb), runs_cand=len(rc), missing=sorted(map(list, set(rb) ^ set(rc))), differing_runs=[])
counts = collections.Counter()
for k in sorted(set(rb) & set(rc)):
    key = '%s__%s__%s' % k
    (db, shb), (dc, shc) = rb[k], rc[k]
    fb, fc = read(base_dir, 'full', key + '.json'), read(cand_dir, 'full', key + '.json')
    eb, ec = read(base_dir, 'envelopes', key + '.json'), read(cand_dir, 'envelopes', key + '.json')
    issues = []
    if (fb is None) != (fc is None) or (eb is None) != (ec is None):
        issues.append('full or summary envelope present on one side only')
    fsb = sha(fb) if fb is not None else None
    fsc = sha(fc) if fc is not None else None
    if (shb, shc) != (fsb, fsc):
        issues.append('run.envelope_sha256 is not the full envelope sha256')
    if db != dc:
        res = record_residue(k, key)
        if res:
            issues.append('runs.jsonl fields differ: %s' % res)
    full_v, full_items = N2.compare(fb, fc) if fb is not None else ('none', [])
    sum_v, sum_items = N2.compare(eb, ec) if eb is not None else ('none', [])
    ob, oc = read(base_dir, 'stdout', key + '.out'), read(cand_dir, 'stdout', key + '.out')
    if ob != oc:
        issues += stdout_check(ob, oc, fsb, fsc, eb, ec) if (ob and oc) else ['stdout empty on one side']
    if read(base_dir, 'stderr', key + '.err') != read(cand_dir, 'stderr', key + '.err'):
        issues.append('stderr differs')
    counts['full_' + full_v] += 1
    counts['summary_' + sum_v] += 1
    within = not issues and full_v in ('identical', 'norm_only', 'none') and sum_v in ('identical', 'none')
    if not (full_v in ('identical', 'none') and sum_v in ('identical', 'none') and not issues):
        report['differing_runs'].append(dict(run=key, within_rule=within, full_verdict=full_v, summary_verdict=sum_v,
                                             issues=issues, full_items=full_items, summary_items=sum_items,
                                             full_sha256_base=fsb, full_sha256_cand=fsc))
    counts['runs_within_rule' if within else 'runs_outside_rule'] += 1
    del fb, fc
mags = [it for d in report['differing_runs'] for it in d['full_items'] if 'kind' in it]
diags = [(d['run'], src, it) for d in report['differing_runs'] for src in ('full', 'summary') for it in d[src + '_items'] if it.get('DIAG')]
other = [(d['run'], it) for d in report['differing_runs'] for it in d['full_items'] + d['summary_items']
         if it.get('OTHER') and not it.get('DIAG') and 'kind' not in it]
report['counts'] = dict(counts)
report['magnitudes'] = dict(moved=len(mags), by_kind=dict(collections.Counter(it['kind'] for it in mags)),
                            by_ulps=dict(collections.Counter(it['ulps'] for it in mags)),
                            candidate_is_cr=sum(1 for it in mags if it.get('norm_ok')),
                            base_is_cr=sum(1 for it in mags if it.get('base_is_cr')),
                            base_is_libm_chain=sum(1 for it in mags if it.get('base_is_libm_chain')),
                            base_components_equal=sum(1 for it in mags if it.get('base_components_equal')))
report['diagnostic_items'] = len(diags)
report['other_items'] = len(other)
report['runs_with_issues'] = [d['run'] for d in report['differing_runs'] if d['issues']]
report['RESULT'] = 'PASS' if counts['runs_outside_rule'] == 0 and not report['missing'] else 'STOP'
json.dump(report, open(out_path, 'w'), indent=1, ensure_ascii=False, default=str)

print('runs: base %d cand %d missing either side %d' % (len(rb), len(rc), len(report['missing'])))
print('full envelopes:', {k[5:]: v for k, v in sorted(counts.items()) if k.startswith('full_')})
print('summary envelopes:', {k[8:]: v for k, v in sorted(counts.items()) if k.startswith('summary_')})
print('runs within the rule (identical or norm-only): %d; outside: %d' % (counts['runs_within_rule'], counts['runs_outside_rule']))
m = report['magnitudes']
print('moved magnitudes: %d; by kind %s; by ulps %s' % (m['moved'], m['by_kind'], m['by_ulps']))
print('  candidate equals the exact correctly rounded norm: %d of %d; base is CR: %d; base equals this host\'s libm hypot chain: %d; '
      'base components equal: %d' % (m['candidate_is_cr'], m['moved'], m['base_is_cr'], m['base_is_libm_chain'], m['base_components_equal']))
print('magnitude moves of more than one ulp:')
for d in report['differing_runs']:
    for it in d['full_items']:
        if 'kind' in it and it['ulps'] > 1:
            print('  %s %s: %s -> %s, %d ulp; CR %s (cand %s); base libm chain %s' % (d['run'], it['id'], it['base'], it['cand'],
                  it['ulps'], it['cr_norm'], 'equals' if it['norm_ok'] else 'DIFFERS', it['base_is_libm_chain']))
print('diagnostic-text items: %d' % len(diags))
for run, src, it in diags:
    print('  %s [%s] %s %s %s: %s' % (run, src, it['path'], it['code'], it['severity'],
          '; '.join('%s -> %s (%d ulp) at "%s"' % (n['base'], n['cand'], n['ulps'], n['context'][-40:]) for n in it['numbers'])))
print('other items: %d' % len(other))
for run, it in other:
    print('  %s %s' % (run, json.dumps(it)[:300]))
print('runs with issues: %d' % len(report['runs_with_issues']))
for d in report['differing_runs']:
    if d['issues']:
        print('  %s: %s' % (d['run'], d['issues']))
print('RESULT', report['RESULT'])
