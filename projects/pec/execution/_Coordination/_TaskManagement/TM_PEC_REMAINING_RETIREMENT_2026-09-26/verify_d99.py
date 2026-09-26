#!/usr/bin/env python3
"""verify_d99.py — finite-account closure check for the D-PEC-99 (provisional) Remaining retirement.

Stdlib only. Two modes:

  account mode (before the act, on any checkout):
    python3 verify_d99.py --repo <REPO_ROOT> --account-only
  act mode (after the act; <PRE> is a fresh `git archive` export of the act's base commit):
    python3 verify_d99.py --repo <REPO_ROOT> --pre <PRE> [--decision D-PEC-NN] [--q1 s1|park|decline]
        [--allow-extra PATH ...]
  <PRE> is a `git archive` export of the commit immediately before the generator run. Run act mode
  right after the generator, before any other file is written; or name each later default-writable
  path (run root, FINAL_ROW_ACCOUNT.csv, graph, register, ruling, docs/STATUS.md, README.md) with
  --allow-extra. Only paths under projects/pec/execution/_Coordination/ and projects/pec/docs/STATUS.md
  and projects/pec/README.md may be allowed; protected paths can never be allowed.

Account mode checks the finite account: 92 keys equal to the census and unique; one disposition
per key in {c, d, e}; every (c) row cites evidence whose path exists with the cited hash prefix;
every (d) row names an exhibit destination class; every (e) row carries an owner question; each
live key's item block is present in its `_STATUS.md` with the census block hash; the 73 held
residuals are outside the census and still recorded in the concordance.
Act mode adds: no `^## Remaining` heading in any of the 66 deliverable `_STATUS.md`; each changed
`_STATUS.md` equals its preimage minus the Remaining section, with only `**Last Updated:**` changed
and one History line appended that names every key of the section; every moved key's text,
`Depends:` and gate appear in the exhibit; the frozen DEL-01-05 `_STATUS.md` and every protected
path are byte-identical; and the changed-path set under the checked roots equals the grant.
Exit 0 PASS, 1 FAIL. Prints one CHECK line per check.
"""
import argparse, csv, glob, hashlib, io, os, re, sys

TM = 'projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/'
CONC = ('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/'
        'R1_R4_2026-09-05/SYNTHESIS/APPLICATION_PREPARATION/FULL_01/CARRIER_DISPOSITIONS.csv')
ROOTS = ('projects/pec', 'docs', 'execution', 'projects/chirality-runtime/execution/_Coordination',
         'projects/chirality-app-dev/execution/_Coordination', 'projects/chirality-piping/execution/_Coordination')
CHECKING_OR_FROZEN = ('DEL-00-01', 'DEL-00-03', 'DEL-08-02', 'DEL-10-01', 'DEL-01-05')
fails = []


def check(name, ok, detail=''):
    print('CHECK %s %s%s' % (name, 'PASS' if ok else 'FAIL', (' ' + detail) if detail else ''))
    if not ok:
        fails.append(name)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rd(root, rel):
    p = os.path.join(root, rel)
    return open(p, 'rb').read() if os.path.isfile(p) else None


def csv_rows(b):
    return list(csv.DictReader(io.StringIO(b.decode('utf-8'), newline='')))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--pre')
    ap.add_argument('--account-only', action='store_true')
    ap.add_argument('--decision', default='D-PEC-99')
    ap.add_argument('--q1', choices=('s1', 'park', 'decline'), default='s1')
    ap.add_argument('--allow-extra', nargs='*', default=[])
    a = ap.parse_args()
    base = a.pre if a.pre else a.repo  # sources and the account are read from the preimage tree in act mode
    acc = csv_rows(rd(base, TM + 'SEMANTIC_DECISION_ACCOUNT.csv'))
    cen = csv_rows(rd(base, TM + 'REMAINING_CENSUS.csv'))
    keys = [r['Key'] for r in acc]
    check('keys_equal_census', keys == [r['Key'] for r in cen], '%d/%d' % (len(keys), len(cen)))
    check('keys_unique_92', len(set(keys)) == 92 == len(keys))
    check('one_disposition_each', all(r['Disposition'] in ('c', 'd', 'e') for r in acc))
    bad_c = []
    for r in acc:
        if r['Disposition'] != 'c':
            continue
        ok = False
        for item in r['Evidence'].split('; '):
            m = re.match(r'([^@]+)@([0-9a-f]{8,64})', item.strip())
            if m:
                b = rd(base, m.group(1)) or rd(base, 'projects/pec/' + m.group(1))
                if b is not None and sha(b).startswith(m.group(2)):
                    ok = True
                    break
        if not ok:
            bad_c.append(r['Key'])
    check('c_rows_cite_existing_evidence', not bad_c, ','.join(bad_c))
    check('d_rows_exhibit_class', all(r['DestinationClass'].startswith('EXHIBIT_') for r in acc if r['Disposition'] == 'd'))
    check('e_rows_have_question', all(r['OwnerQuestion'].strip() for r in acc if r['Disposition'] == 'e'))
    blk_bad = []
    for r in acc:
        if r['Population'] != 'LIVE_REMAINING':
            continue
        t = rd(base, r['SourcePath']).decode('utf-8')
        if sha(t.encode('utf-8')) != r['SourceSHA256']:
            blk_bad.append(r['Key'] + ':file')
            continue
        sec = t.split('\n## Remaining\n', 1)[1]
        blocks = re.split(r'\n(?=- \[.\] DEL-)', sec.strip('\n'))
        hit = [b for b in blocks if b.startswith('- [') and (' %s — ' % r['Key']) in b.split('\n', 1)[0]]
        if len(hit) != 1 or sha((hit[0].rstrip('\n') + '\n').encode('utf-8')) != r['ItemBlockSHA256']:
            blk_bad.append(r['Key'])
    check('item_blocks_match_census', not blk_bad, ','.join(blk_bad[:10]))
    held = 0
    for r in csv_rows(rd(base, CONC)):
        held += len([x for x in r['HeldOrConditionalResidualIDs'].split(';') if x])
    check('held_residuals_outside_census', held == 73 and not (set(keys) & {x for r in csv_rows(rd(base, CONC)) for x in r['HeldOrConditionalResidualIDs'].split(';') if x}), 'held=%d' % held)
    if a.account_only:
        print('RESULT', 'FAIL' if fails else 'PASS')
        sys.exit(1 if fails else 0)

    # act mode
    ex_rel = 'projects/pec/execution/_Coordination/_DECISIONS/%s_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md' % a.decision
    ex = (rd(a.repo, ex_rel) or b'').decode('utf-8')
    check('exhibit_present', bool(ex))
    missing = []
    for r in acc:
        moved = r['Disposition'] == 'd' or (r['Disposition'] == 'e' and a.q1 in ('s1', 'park'))
        in_a = r['DestinationClass'] == 'EXHIBIT_A_D83E' or (r['Disposition'] == 'e' and a.q1 == 'park')
        if moved and not all(x in ex for x in ('### ' + r['Key'] if in_a else '#### ' + r['Key'],
                                               r['ItemText'], 'Depends: ' + r['Depends'], 'Gate: ' + r['GateMarkers'])):
            missing.append(r['Key'])
        if (moved and r['DestinationClass'].startswith('EXHIBIT_B')) or (r['Disposition'] == 'e' and a.q1 in ('s1', 'park')):
            if r['DestinationExactText'].strip() not in ex:
                missing.append(r['Key'] + ':carry')
    check('moved_items_in_exhibit', not missing, ','.join(missing[:10]))
    declined = [r['Key'] for r in acc if r['Disposition'] == 'e' and a.q1 == 'decline']
    check('declined_items_absent_from_exhibit', not [k for k in declined if k in ex], ','.join(declined))
    all_status = sorted(glob.glob(os.path.join(a.repo, 'projects/pec/execution/PKG-*/1_Working/DEL-*/_STATUS.md')))
    surv = [p for p in all_status if re.search(r'^## Remaining', open(p, encoding='utf-8').read(), re.M)]
    present = all(os.path.isfile(os.path.join(a.repo, r['SourcePath'])) for r in acc if r['Population'] == 'LIVE_REMAINING')
    check('no_remaining_heading_all', len(all_status) >= 66 and present and not surv, '%d files; survivors %d' % (len(all_status), len(surv)))
    by_path = {}
    for r in acc:
        if r['Population'] == 'LIVE_REMAINING':
            by_path.setdefault(r['SourcePath'], []).append(r['Key'])
    shape_bad = []
    for rel, ks in by_path.items():
        pre = rd(a.pre, rel).decode('utf-8')
        post = rd(a.repo, rel).decode('utf-8')
        head = pre.split('\n\n## Remaining\n', 1)[0]
        pl, ql = head.split('\n'), post.rstrip('\n').split('\n')
        last = ql[-1]
        ok = len(ql) == len(pl) + 1 and all(
            x == y or (x.startswith('**Last Updated:** ') and y.startswith('**Last Updated:** ')) for x, y in zip(pl, ql[:-1]))
        ok = ok and last.startswith('- ') and a.decision in last and all(k in last for k in ks)
        if not ok:
            shape_bad.append(rel)
    check('status_edits_exact', not shape_bad, '%d files; bad %d' % (len(by_path), len(shape_bad)))
    # containment and protection
    changed, added, removed = set(), set(), set()
    for root in ROOTS:
        for side, other, sink in ((a.pre, a.repo, removed), (a.repo, a.pre, added)):
            for dp, dn, fn in os.walk(os.path.join(side, root)):
                if '/.git' in dp or '__pycache__' in dp:
                    continue
                for f in fn:
                    rel = os.path.relpath(os.path.join(dp, f), side)
                    ob = rd(other, rel)
                    if ob is None:
                        sink.add(rel)
                    elif side == a.repo and sha(ob) != sha(rd(side, rel)):
                        changed.add(rel)
    expect_changed = set(by_path) | {'projects/pec/AGENTS.md'}
    news = {x for x in added}
    exp_new_prefix = (ex_rel, 'docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-',
                      'execution/_Coordination/NOTICE_', 'projects/chirality-runtime/execution/_Coordination/NOTICE_')
    allowed_roots = ('projects/pec/execution/_Coordination/', 'projects/pec/docs/STATUS.md', 'projects/pec/README.md')
    bad_allow = [x for x in a.allow_extra if not x.startswith(allowed_roots)]
    check('allow_extra_default_writable_only', not bad_allow, ','.join(bad_allow))
    allow = lambda q: any(q == x or q.startswith(x.rstrip('/') + '/') for x in a.allow_extra if x not in bad_allow)
    changed = {q for q in changed if q in expect_changed or not allow(q)}
    added = {q for q in added if not allow(q)}
    news = set(added)
    check('changed_paths_equal_grant', changed == expect_changed, 'changed %d; unexpected %s' % (len(changed), sorted(changed - expect_changed)[:5]))
    check('new_paths_equal_grant', len(news) == 4 and all(any(n.startswith(p) for p in exp_new_prefix) for n in news) and not removed,
          'new %s; removed %d' % (sorted(news), len(removed)))
    prot = [p for p in changed if any('/%s_' % d in p for d in CHECKING_OR_FROZEN) or p.endswith('ScopeOfWork.md') or p.endswith('Dependencies.csv')]
    check('protected_paths_unchanged', not prot, ','.join(prot))
    print('RESULT', 'FAIL' if fails else 'PASS')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
