"""I103 lane A: one mutant per new admission check, each run against the law tests that should kill it.
Usage: mutants.py <mutation tree root (archive of the candidate)> <out dir> [mutant ids...]
Each mutant edits PP's retained_memory.rs in the tree (one exact replacement), runs
`cargo test --lib` through WT/tools/t3_cargo.sh with a test filter, records the result,
and restores the file. A mutant is killed when the run fails with a named test failure."""
import json, os, pathlib, re, subprocess, sys

WT = pathlib.Path('WT')
ROOT = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
PP = ROOT / 'projects/chirality-piping/core/product_physics'
SRC = PP / 'src/retained_memory.rs'

# (id, check, old, new, test filter)
MUTANTS = [
    ('B2A-01', 'combination ids disjoint (C-9)',
     'if m.combinations.iter().any(|combination| m.load_cases.iter().any(|case| case.id == combination.id)) {',
     'if false && m.combinations.iter().any(|combination| m.load_cases.iter().any(|case| case.id == combination.id)) {',
     'b2_a_combination_ids'),
    ('B2A-02', 'z <= 2: the cap',
     'row(K::Combinations, t.combinations.length, COMBINATIONS),',
     'row(K::Combinations, t.combinations.length, COMBINATIONS + 1),', 'b2_a_d1_admits'),
    ('B2A-03', 'z <= 2: combination counting',
     'row(K::Combinations, t.combinations.length, COMBINATIONS),',
     'row(K::Combinations, t.combinations.length.min(COMBINATIONS), COMBINATIONS),', 'b2_a_d1_admits'),
    ('B2A-04', 'C_eq = c + z: combination counting (z dropped)',
     'row(K::CaseEquivalents, t.load_cases.length.saturating_add(t.combinations.length), CASE_EQUIVALENTS),',
     'row(K::CaseEquivalents, t.load_cases.length, CASE_EQUIVALENTS),', 'b2_a_'),
    ('B2A-05', 'C_eq <= 3: the bound',
     'row(K::CaseEquivalents, t.load_cases.length.saturating_add(t.combinations.length), CASE_EQUIVALENTS),',
     'row(K::CaseEquivalents, t.load_cases.length.saturating_add(t.combinations.length), CASE_EQUIVALENTS + 1),', 'b2_a_'),
    ('B2A-06', 'h <= 3: the term bound',
     'row(K::CombinationTerms, z.terms.length, COMBINATION_TERMS),',
     'row(K::CombinationTerms, z.terms.length, COMBINATION_TERMS + 1),', 'b2_a_terms'),
    ('B2A-07', 'h: term counting over every combination',
     'for combination in &request.model.combinations {\n        widest(',
     'for combination in request.model.combinations.iter().take(1) {\n        widest(', 'b2_a_terms'),
    ('B2A-08', 'h: the typed terms capacity',
     'row(K::CombinationTermsCapacity, z.terms.capacity, COMBINATION_TERMS),',
     'row(K::CombinationTermsCapacity, z.terms.length, COMBINATION_TERMS),', 'b2_a_terms'),
    ('B2A-09', 'range operands <= 3: the bound',
     'row(K::RangeOperands, z.range_operands.length, RANGE_OPERANDS),',
     'row(K::RangeOperands, z.range_operands.length, RANGE_OPERANDS + 1),', 'b2_a_terms'),
    ('B2A-10', 'range operands: the typed capacity',
     'row(K::RangeOperandsCapacity, z.range_operands.capacity, RANGE_OPERANDS),',
     'row(K::RangeOperandsCapacity, z.range_operands.length, RANGE_OPERANDS),', 'b2_a_terms'),
    ('B2A-11', 'combinations typed capacity <= 2',
     'row(K::CombinationsCapacity, t.combinations.capacity, COMBINATIONS),',
     'row(K::CombinationsCapacity, t.combinations.capacity, COMBINATIONS + 1),', 'typed_capacity_and_units_rows'),
    ('B2A-12', 'the typed census reads combination strings',
     '        for combination in &m.combinations {\n            self.string(&combination.id)?;',
     '        for combination in m.combinations.iter().take(0) {\n            self.string(&combination.id)?;', 'b2_a_typed_census'),
    ('B2A-13', 'G-C: EnvelopeResults <= C_eq * P_final (vs c * P_final; equivalent while C_eq\'s cap = C\'s)',
     '            ceq * P_FINAL,\n', '            c * P_FINAL,\n', 'b2_a_g_c|b1_sa_'),
    ('B3A-01', 'L3: the contract version',
     '("0.3.0", Some(c)) if contract_is(c, "1.0.0", "legacy_pressure_v1")',
     '("0.3.0", Some(c)) if c.mode.as_deref() == Some("legacy_pressure_v1")', 'b3a_'),
    ('B3A-02', 'L3: the contract mode',
     '("0.3.0", Some(c)) if contract_is(c, "1.0.0", "legacy_pressure_v1")',
     '("0.3.0", Some(c)) if c.version.as_deref() == Some("1.0.0")', 'b3a_'),
    ('B3A-03', 'L3: the schema 0.3.0',
     '("0.3.0", Some(c)) if contract_is(c, "1.0.0", "legacy_pressure_v1")',
     '(_, Some(c)) if contract_is(c, "1.0.0", "legacy_pressure_v1")', 'b3a_'),
    ('B3A-04', 'D1.3 refusal map: a contract outside its branch is PressureContract',
     '("0.1.0" | "0.2.0" | "0.3.0", _) => Err(FamilyFact::PressureContract),',
     '("0.1.0" | "0.2.0" | "0.3.0", _) => Err(FamilyFact::SchemaVersion),', 'b3a_|every_family_clause'),
    ('B3A-05', 'the typed census reads the contract strings',
     '        if let Some(contract) = &m.pressure_contract {\n            self.optional(&contract.version)?;',
     '        if let Some(contract) = m.pressure_contract.as_ref().filter(|_| false) {\n            self.optional(&contract.version)?;', 'b3a_'),
    ('B3B-01', 'exact D1.4: no combination (ruling 4)',
     'if exact && !m.combinations.is_empty() {', 'if false && exact && !m.combinations.is_empty() {', 'b3b_'),
    ('B3B-02', 'exact D1.5: regions absent refuse',
     '            None => !exact,', '            None => true,', 'b3b_'),
    ('B3B-03', 'exact D1.5: non-empty regions refuse',
     '            Some(regions) => exact && regions.is_empty(),', '            Some(_) => exact,', 'b3b_'),
    ('B3B-04', 'D1.5 on L and L3: Some([]) refuses',
     '            Some(regions) => exact && regions.is_empty(),', '            Some(regions) => regions.is_empty(),', 'b3a_|every_family_clause'),
    ('B3B-05', 'E: the contract version',
     '("0.3.0", Some(c)) if contract_is(c, "2.0.0", "exact_straight_pressure_v2")',
     '("0.3.0", Some(c)) if c.mode.as_deref() == Some("exact_straight_pressure_v2")', 'b3b_'),
    ('B3B-06', 'E: 0.4.0 stays out',
     '("0.3.0", Some(c)) if contract_is(c, "2.0.0", "exact_straight_pressure_v2")',
     '("0.3.0" | "0.4.0", Some(c)) if contract_is(c, "2.0.0", "exact_straight_pressure_v2")', 'b3b_'),
]

def run(mid, filt):
    env = dict(os.environ)
    env.update({'RUSTUP_TOOLCHAIN': '1.97.1', 'RUSTUP_AUTO_INSTALL': '0', 'CARGO_INCREMENTAL': '0', 'CARGO_BUILD_JOBS': '8',
                'RUST_TEST_THREADS': '4', 'CARGO_TARGET_DIR': str(WT / 'targets/i103-b2-a-mut'), 'TMPDIR': str(WT / 'scratch/i103_b2_a/tmp')})
    env.pop('RUSTFLAGS', None); env.pop('CARGO_ENCODED_RUSTFLAGS', None)
    args = [str(WT / 'tools/t3_cargo.sh'), 'test', '--locked', '--offline', '--manifest-path', str(PP / 'Cargo.toml'), '--lib', '--']
    args += filt.split('|')
    with open(OUT / f'{mid}.log', 'w') as log:
        rc = subprocess.run(args, cwd=PP, env=env, stdout=log, stderr=subprocess.STDOUT).returncode
    text = (OUT / f'{mid}.log').read_text()
    failed = re.findall(r'^test (\S+) \.\.\. FAILED$', text, re.M)
    passed = len(re.findall(r'^test \S+ \.\.\. ok$', text, re.M))
    return rc, failed, passed, 'error[E' in text

wanted = sys.argv[3:]
original = SRC.read_text()
results = []
for mid, check, old, new, filt in MUTANTS:
    if wanted and mid not in wanted:
        continue
    assert original.count(old) == 1, (mid, original.count(old))
    SRC.write_text(original.replace(old, new))
    try:
        rc, failed, passed, compile_error = run(mid, filt)
    finally:
        SRC.write_text(original)
    killed = rc != 0 and bool(failed) and not compile_error
    results.append({'id': mid, 'check': check, 'filter': filt, 'rc': rc, 'killed': killed, 'compile_error': compile_error,
                    'passed': passed, 'killed_by': failed})
    print(json.dumps(results[-1]), flush=True)
(OUT / 'mutants.json').write_text(json.dumps(results, indent=1) + '\n')
