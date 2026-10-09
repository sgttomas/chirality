#!/usr/bin/env python3
"""I112 round 2, U3 both-entry gate part 1: run-by-run comparison of base B and candidate C under the U3 brief's acceptance rule
(derived from round 1's part1_norm_compare.py; the envelope classifier is u3diff.classify instead of normdiff2.compare).

For every run key (case, mode, entry):
  runs.jsonl  streamed as bytes; each record line is compared with wall_seconds, peak_rss_kib, memorystatus_level_end and
              probe.run.solve_seconds replaced by a fixed token and probe.run.envelope_sha256 removed (each must occur the
              expected number of times). Where the lines still differ, both records are parsed and the differing fields listed;
              the only accepted residue is probe.run.envelope equal to that side's envelopes/<key>.json (the summary envelope,
              judged below);
  full/       u3diff.classify with the run's request model (gen_out): identical, declared, declared_t2, refusal or OTHER;
  envelopes/  (the summary span) the same;
  stdout/     byte-identical once the candidate's run.solve_seconds and run.envelope_sha256 value texts and its summary span are
              replaced by the base's (each occurring once); each envelope_sha256 must be the sha256 of that side's full envelope;
  stderr/     identical.
The brief's rule passes a run when every output is identical, declared, declared_t2 or a designed refusal; OTHER is a stop.
Writes <out.json> and prints a summary.
Usage: python3 -B part1_u3_compare.py <base-dir> <cand-dir> <u3diff-dir> <gen_out> <out.json>
"""
import collections
import hashlib
import json
import os
import re
import sys

base_dir, cand_dir, nd_dir, gen, out_path = sys.argv[1:6]
sys.path.insert(0, nd_dir)
import u3diff as U  # noqa: E402
CASES = {c['id']: c for c in json.load(open(os.path.join(gen, 'cases.json')))}
WORK = os.path.join(os.path.dirname(os.path.abspath(out_path)), 'tmp')
os.makedirs(WORK, exist_ok=True)


def model_for(case):
    c = CASES[case]
    return json.load(open(os.path.join(gen, c['request_file'])))['model'] if 'request_file' in c else None

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
    model = model_for(k[0])
    if fb is None or fc is None:
        full_v, full_info = ('none', {}) if fb is None and fc is None else ('OTHER', {'why': 'full envelope on one side only'})
    else:
        full_v, full_info = ('identical', {}) if fb == fc else U.classify(fb.decode('utf-8'), fc.decode('utf-8'), model, WORK)
    if eb is None or ec is None:
        sum_v, sum_info = ('none', {}) if eb is None and ec is None else ('OTHER', {'why': 'summary envelope on one side only'})
    else:
        sum_v, sum_info = ('identical', {}) if eb == ec else U.classify(eb.decode('utf-8'), ec.decode('utf-8'), model, WORK)
    ob, oc = read(base_dir, 'stdout', key + '.out'), read(cand_dir, 'stdout', key + '.out')
    if ob != oc:
        issues += stdout_check(ob, oc, fsb, fsc, eb, ec) if (ob and oc) else ['stdout empty on one side']
    if read(base_dir, 'stderr', key + '.err') != read(cand_dir, 'stderr', key + '.err'):
        issues.append('stderr differs')
    counts['full_' + full_v] += 1
    counts['summary_' + sum_v] += 1
    accepted = ('identical', 'none', 'declared', 'declared_t2', 'refusal')
    within = not issues and full_v in accepted and sum_v in accepted
    if not (full_v in ('identical', 'none') and sum_v in ('identical', 'none') and not issues):
        report['differing_runs'].append(dict(run=key, within_rule=within, full_class=full_v, summary_class=sum_v, issues=issues,
                                             full_info=full_info, summary_info=sum_info, full_sha256_base=fsb, full_sha256_cand=fsc))
    counts['runs_within_rule' if within else 'runs_outside_rule'] += 1
    del fb, fc
report['counts'] = dict(counts)
report['RESULT'] = 'PASS' if counts['runs_outside_rule'] == 0 and not report['missing'] else 'STOP'
json.dump(report, open(out_path, 'w'), indent=1, ensure_ascii=False, default=str)

print('runs: base %d cand %d missing either side %d' % (len(rb), len(rc), len(report['missing'])))
print('full envelopes:', {k[5:]: v for k, v in sorted(counts.items()) if k.startswith('full_')})
print('summary envelopes:', {k[8:]: v for k, v in sorted(counts.items()) if k.startswith('summary_')})
print('runs within the rule: %d; outside: %d' % (counts['runs_within_rule'], counts['runs_outside_rule']))
for d in report['differing_runs']:
    fi = d['full_info']
    desc = d['full_class']
    if d['full_class'] == 'refusal':
        desc += ' %s (base %s %s)' % (sorted({c for c, _, _ in fi['refusal']}), fi.get('base_status'), fi.get('base_blocking_codes'))
    elif fi.get('declared'):
        desc += ' %s' % fi['declared']
    print('  %s: full %s; summary %s %s%s' % (d['run'], desc, d['summary_class'], d['summary_info'].get('declared', ''),
          ('; ISSUES ' + '; '.join(d['issues'])) if d['issues'] else ''))
    for side in ('full', 'summary'):
        if d[side + '_class'] == 'OTHER':
            print('      %s OTHER: %s' % (side, json.dumps(d[side + '_info'])[:400]))
print('RESULT', report['RESULT'])
