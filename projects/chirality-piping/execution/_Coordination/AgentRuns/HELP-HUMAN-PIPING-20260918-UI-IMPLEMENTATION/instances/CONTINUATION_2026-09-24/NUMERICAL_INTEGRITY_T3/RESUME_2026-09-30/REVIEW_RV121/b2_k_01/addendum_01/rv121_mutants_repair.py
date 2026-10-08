"""RV121's own mutants on lane K's code. Each mutant is one exact text replacement in a scratch copy of FK
(the replaced text must occur exactly once), FK's lib tests run with the B2-K/B3-K filters, and the failing
tests are recorded. The copy is restored from head's bytes after every mutant."""
import json, os, re, shutil, subprocess, sys, time
S = 'WT/scratch/rv121_rvk'
SRC = S + '/head/projects/chirality-piping/core/solver/frame_kernel'
DST = S + '/mut/frame_kernel'
R = 'src/structural/retained/'
FC = R + 'product_certificate/final_case.rs'; SR = R + 'product_certificate/source_residual.rs'
PC = R + 'product_certificate.rs'; AD = R + 'adaptive.rs'; OR = R + 'origins.rs'; CB = R + 'combine.rs'
FILTERS = ['b2k_', 'b3k_', 'source_residual_combination_and_missing_uniqueness_are_explicit_refusals']
import sys as _sys
TREE = _sys.argv[1]          # 'rep1' (repair head) or 'head' (ef51a2d295)
SRC = S + '/' + TREE + '/projects/chirality-piping/core/solver/frame_kernel'
DST = S + '/mut_' + TREE + '/frame_kernel'
FILTERS = ['b2k_', 'b3k_', 'source_residual_combination_and_missing_uniqueness_are_explicit_refusals']
M = [
 ('p2m29', FC, 'let up=upper>0 || (upper==0 && odd);', 'let up=upper>0;', "I102's p2m29: upper tie clause dropped (RK-1)"),
 ('m36', FC, 'let combination=!self.data.owner.prep.factors.is_empty();', 'let combination=true;', '(ii) for case owners too (RK-2)'),
 ('m18', FC, '!(combination && j % 21 == 20)', '!(j % 21 == 20)', 'slot 20 exempt for case owners too (RK-3)'),
 ('rk4', FC, '                        nr.class == adaptive::RowClass::InputDerived,\n                    )',
  '                        nr.class == adaptive::RowClass::InputDerived\n                            || (!owner.prep.factors.is_empty() && matches!(id, QuantityId::DisplacementMagnitude(_))),\n                    )',
  'availability: a combination magnitude row gated as InputDerived (RK-4)'),
]
def restore():
    if os.path.exists(DST): shutil.rmtree(DST)
    shutil.copytree(SRC, DST)
def run(tag):
    env = dict(os.environ, TMPDIR=S + '/tmp', CARGO_TARGET_DIR='WT/targets/rv121-fk-mut-' + TREE)
    log = f'{S}/mut_{TREE}/logs/{tag}.log'
    t = time.time()
    with open(log, 'w') as f:
        rc = subprocess.call(['WT/tools/t3_cargo.sh', 'test', '--locked', '--offline', '--lib', '--'] + FILTERS,
                             cwd=DST, stdout=f, stderr=subprocess.STDOUT, env=env)
    text = open(log, errors='replace').read()
    failed = sorted(set(re.findall(r'^test (\S+) \.\.\. FAILED', text, re.M)))
    passed = len(re.findall(r'^test \S+ \.\.\. ok', text, re.M))
    built = 'error[E' not in text and 'could not compile' not in text
    return {'rc': rc, 'built': built, 'failed': [f.split('::')[-1] for f in failed], 'passed': passed, 'seconds': round(time.time() - t)}
os.makedirs(S + '/mut_' + TREE + '/logs', exist_ok=True)
only = sys.argv[2:]
results = {}
restore()
results['baseline'] = run('baseline')
for mid, path, old, new, what in M:
    if only and mid not in only: continue
    restore()
    p = os.path.join(DST, path); text = open(p).read()
    n = text.count(old)
    if n != 1:
        results[mid] = {'what': what, 'error': f'pattern occurs {n} times'}; continue
    open(p, 'w').write(text.replace(old, new))
    r = run(mid); r['what'] = what; r['file'] = path
    r['verdict'] = 'NOT BUILT' if not r['built'] else ('KILLED' if r['failed'] else 'SURVIVED')
    results[mid] = r
    print(mid, r['verdict'], r['failed'][:4], flush=True)
restore()
json.dump(results, open(S + '/mut_' + TREE + '/rv121_mutants_repair.json', 'w'), indent=1)
print(json.dumps({k: (v.get('verdict') or v.get('error') or v.get('rc')) for k, v in results.items()}, indent=1))
