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
M = [
 ('m01', PC, 'directed::round_toward(&mut ctx, &mut sum, toward)?',
  'directed::round_toward(&mut ctx, &mut sum, match toward { Toward::Up => Toward::Down, Toward::Down => Toward::Up })?',
  'net enclosure: directions swapped'),
 ('m02', PC, 'let lo = self.net_toward(ledger, dof, Toward::Down)?;', 'let lo = self.net_toward(ledger, dof, Toward::Up)?;',
  'net enclosure: lo rounded up (one-sided)'),
 ('m03', SR, 'out[a] = w.add(out[a], net)?;', 'let _ = w.add(out[a], net)?;', 'free rows: combined net dropped'),
 ('m04', SR, 'reaction[ci] = w.sub(reaction[ci], net)?;', 'reaction[ci] = w.add(reaction[ci], net)?;', 'reaction offset: sign flipped'),
 ('m05', SR, '    if view.owner().prep.factors.is_empty() {\n        // Actual individual terms', '    if true {\n        // Actual individual terms',
  'free rows: representative loads for a combination'),
 ('m06', SR, '    if view.owner().prep.factors.is_empty() {\n        for load in source.loads() {', '    if true {\n        for load in source.loads() {',
  'reaction offsets: representative loads for a combination'),
 ('m07', SR, '    for (a, &g) in view.group().ordering.free.iter().enumerate() {\n        w.visit()?;\n        if ledger.net(g).is_some_and(|net| !net.is_zero()) {',
  '    for (a, &g) in view.group().ordering.free.iter().enumerate() {\n        w.visit()?;\n        if ledger.net(g).is_some() {',
  'free rows: zero nets enclosed too (work only)'),
 ('m08', AD, 'if term.1.to_bits() != 0f64.to_bits() {', 'if false {', 'view: P2 value check dropped'),
 ('m09', AD, 'if term.1.to_bits() != 0f64.to_bits() {', 'if term.1 != 0.0 {', 'view: P2 by value (admits -0.0)'),
 ('m10', AD, 'if term.0.to_bits() != factor.to_bits() {', 'if false {', 'view: factor bits unchecked'),
 ('m11', AD, 'if *g != c.dof.global() || terms.len() != self.prep.factors.len() {', 'if *g != c.dof.global() {', 'view: term count unchecked'),
 ('m12', AD, 'if *g != c.dof.global() || terms.len() != self.prep.factors.len() {',
  'prescribed[*g] = true; if *g != c.dof.global() || terms.len() != self.prep.factors.len() {', 'view: combination prescribed flags set'),
 ('m13', OR, 'let kind=match owner {NativeOwner::Case(_)=>solve.prep.factors.is_empty(),',
  'let kind=true||match owner {NativeOwner::Case(_)=>solve.prep.factors.is_empty(),', 'product_owner: kind check dropped'),
 ('m14', FC, 'if invocation.product_owner(run, owner).is_none() {', 'if false {', 'run_case: recorded owner unchecked'),
 ('m15', FC, 'if combination && matches!(r.recipe, ProductRecipe::NonQuantity', 'if false && matches!(r.recipe, ProductRecipe::NonQuantity',
  'row_scales: combination row families admitted'),
 ('m16', FC, '|| !(nonquantity || combination)', '|| !nonquantity', 'row_scales: mode record required of a combination'),
 ('m17', FC, '!(combination && j % 21 == 20)', '!(combination && j % 21 == 19)', 'row_scales: wrong exempt slot'),
 ('m18', FC, '!(combination && j % 21 == 20)', '!(j % 21 == 20)', 'row_scales: slot 20 exempt for cases too'),
 ('m19', FC, 'let combination=!self.data.owner.prep.factors.is_empty();', 'let combination=false;', 'project: no (ii), hull projection'),
 ('m20', FC, 'let odd=y&1==1;', 'let odd=y&1==0;', 'norm: ties to odd'),
 ('m21', FC, 'else {lift(f64::from_bits(bits)).map_err(|_|H::Invariant)}',
  'else if bits==0x000f_ffff_ffff_ffff {shift(&lift(f64::from_bits(0x001f_ffff_ffff_ffff)).map_err(|_|H::Invariant)?,-1).map_err(|_|H::Invariant)}\n        else {lift(f64::from_bits(bits)).map_err(|_|H::Invariant)}',
  'norm: binade-rule lower midpoint at 2^-1022 (SA4-1 (a))'),
 ('m22', FC, 'if up && y==MAX_BITS {return Err(H::Binary64Range);}', 'if up && y==MAX_BITS {return Ok(f64::MAX);}', 'norm: beyond MAX published as MAX (SA4-1 (b))'),
 ('m23', FC, 'B::Overflow{negative:false}=>MAX_BITS,', 'B::Overflow{negative:false}=>return Err(H::Binary64Range),', 'norm: overflowing estimate refused outright (SA4-1 (c))'),
 ('m24', FC, 'if step==1 || (up && down) {return Err(H::Invariant);}', 'if up && down {return Err(H::Invariant);}', 'norm: a second step allowed (SA4-1 (d))'),
 ('m25', FC, "        let upper=side(y+1)?;\n        let lower=side(y-1)?;", "        let upper=if step==9 {side(y+1)?} else {-1};\n        let lower=if step==9 {side(y-1)?} else {1};",
  'norm: exact side test skipped (estimate published)'),
 ('m26', FC, 'if found || spec.unit!=ProductUnit::Millimetre || !values[i].is_finite(){return Err(bad("displacement norm identity/unit"));}',
  'if found || !values[i].is_finite(){return Err(bad("displacement norm identity/unit"));}', 'norm: component unit unchecked'),
 ('m27', OR, '            || !self.runs_fit(sources.len())\n', '', 'SF-1: Run-capacity check dropped'),
 ('m28', OR, 'remaining\n            .and_then(|r| self.store.runs.len().checked_add(n)?.checked_add(r))',
  'remaining\n            .and_then(|_r| self.store.runs.len().checked_add(n))', 'SF-1: remaining combinations not reserved'),
 ('m29', OR, '        if next > self.capacity.cases {\n            return Err(OriginError::Capacity);\n        }\n        let id = self.store.sources.len();',
  '        let id = self.store.sources.len();', 'registration: capacity unchecked'),
 ('m30', OR, '                            && origin.identity[..] == *prepared.identity()\n', '\n', 'I7: identity unchecked'),
 ('m31', OR, '                        matches!(origin.owner, NativeOwner::Case(_))\n                            && origin.combination_ledger.is_none()',
  '                        origin.combination_ledger.is_none()', 'I7: owner kind unchecked'),
 ('m32', OR, '                            && origin.combination_ledger.is_none()\n', '\n', 'I7: combination ledger unchecked'),
 ('m33', OR, '        let runs = cases\n            .checked_add(combinations)', '        let runs = cases.saturating_add(prepared_sources)\n            .checked_add(combinations)',
  'for_invocation: prepared sources reserve Runs'),
 ('m34', CB, '        o.source.stiffness_encoding() != identity\n', '        false\n', 'OperandsDiffer: K4STF unchecked'),
 ('m35', OR, '            for slot in OriginSlot::ALL {\n                let i = slot.index();\n                if slots[i].is_none() {',
  '            for slot in OriginSlot::ALL.into_iter().rev() {\n                let i = slot.index();\n                if slots[i].is_none() || operand_index > 0 {',
  'imports: last selected operand wins (authored order lost)'),
 ('p1a', PC, 'let represented_z = if hooks::material_gated(&input.material) {',
  'let represented_z = if hooks::material_gated(&input.material) || matches!(input.material, MaterialOperands::ExactENu { .. }) {',
  'K3-2 reverted in production code'),
 ('p1b', R + 'product_certificate/final_case.rs', 'Self::BaseENu { e, nu } => MaterialOperands::ExactENu { e, nu },',
  'Self::BaseENu { e, nu } => MaterialOperands::Ordinary { e, g: e / (2.0 * (1.0 + nu)) },', 'K3-1 mapped to the ordinary route'),
]
def restore():
    if os.path.exists(DST): shutil.rmtree(DST)
    shutil.copytree(SRC, DST)
def run(tag):
    env = dict(os.environ, TMPDIR=S + '/tmp', CARGO_TARGET_DIR='WT/targets/rv121-fk-mut')
    log = f'{S}/mut/logs/{tag}.log'
    t = time.time()
    with open(log, 'w') as f:
        rc = subprocess.call(['WT/tools/t3_cargo.sh', 'test', '--locked', '--offline', '--lib', '--'] + FILTERS,
                             cwd=DST, stdout=f, stderr=subprocess.STDOUT, env=env)
    text = open(log, errors='replace').read()
    failed = sorted(set(re.findall(r'^test (\S+) \.\.\. FAILED', text, re.M)))
    passed = len(re.findall(r'^test \S+ \.\.\. ok', text, re.M))
    built = 'error[E' not in text and 'could not compile' not in text
    return {'rc': rc, 'built': built, 'failed': [f.split('::')[-1] for f in failed], 'passed': passed, 'seconds': round(time.time() - t)}
os.makedirs(S + '/mut/logs', exist_ok=True)
only = sys.argv[1:]
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
json.dump(results, open(S + '/mut/rv121_mutants.json', 'w'), indent=1)
print(json.dumps({k: (v.get('verdict') or v.get('error') or v.get('rc')) for k, v in results.items()}, indent=1))
