import { describe, expect, it } from 'vitest';
import corpusText from '../../../../../fixtures/results/retained_precision_cases.json?raw';
import { absoluteBound, upwardProduct, upwardSmallSum, binary64Bits, decodeBinary64 } from './retainedPrecision';
const corpus = JSON.parse(corpusText);
type Rational = readonly [bigint, bigint];
// Independent test oracle: exact fractions plus a binary search over ordered
// positive binary64 words. It shares neither the reader's quantum rounding nor
// its significand extraction/rounding implementation.
const MAX_FINITE = 0x7fefffffffffffffn;
function fraction(word: bigint): Rational {
  const exponent = Number((word >> 52n) & 2047n), tail = word & 0xfffffffffffffn;
  const significand = exponent === 0 ? tail : 0x10000000000000n + tail;
  const power = exponent === 0 ? -1074 : exponent - 1075;
  return power < 0 ? [significand, 1n << BigInt(-power)] : [significand << BigInt(power), 1n];
}
function compare(a: Rational, b: Rational): number {
  const delta = a[0] * b[1] - b[0] * a[1]; return delta < 0n ? -1 : delta > 0n ? 1 : 0;
}
const add = (a: Rational, b: Rational): Rational => [a[0] * b[1] + b[0] * a[1], a[1] * b[1]];
const multiply = (a: Rational, b: Rational): Rational => [a[0] * b[0], a[1] * b[1]];
function upperWord(value: Rational): bigint {
  if (compare(value, fraction(MAX_FINITE)) > 0) throw new Error('finite upper does not exist');
  let lo = 0n, hi = MAX_FINITE;
  while (lo < hi) { const mid = (lo + hi) / 2n; if (compare(fraction(mid), value) < 0) lo = mid + 1n; else hi = mid; }
  return lo;
}
function nearestWord(value: Rational): bigint {
  const high = upperWord(value);
  if (high === 0n || compare(fraction(high), value) === 0) return high;
  const low = high - 1n, midpoint = multiply(add(fraction(low), fraction(high)), [1n, 2n]);
  const direction = compare(value, midpoint);
  return direction < 0 || (direction === 0 && low % 2n === 0n) ? low : high;
}
function scaledOracle(word: bigint, power: number): bigint {
  const input = fraction(word), factor: Rational = [1n << BigInt(power), 1n];
  const nearest = nearestWord(multiply(input, [1n, factor[0]]));
  const back = nearestWord(multiply(fraction(nearest), factor));
  return compare(fraction(back), input) < 0 ? nearest + 1n : nearest;
}
function expectLeastUpper(actual: number, exact: Rational): void {
  const word = BigInt('0x' + binary64Bits(actual));
  expect(compare(fraction(word), exact)).toBeGreaterThanOrEqual(0);
  if (word !== 0n) expect(compare(fraction(word - 1n), exact)).toBeLessThan(0);
}
describe('synthetic prepared receipt arithmetic controls, not execution evidence', () => {
  it('preserves the independently derived small-bound bits', () => {
    for (const row of corpus.arithmetic.small_bounds) {
      expect(binary64Bits(absoluteBound(decodeBinary64(row.value), decodeBinary64(row.scale))), row.id).toBe(row.expected);
    }
  });
  it('preserves finite exact-product controls and overflow refusal', () => {
    for (const row of corpus.arithmetic.products) {
      const run = () => upwardProduct(decodeBinary64(row.a), decodeBinary64(row.b));
      if (row.expected === null) expect(run).toThrow(); else expect(binary64Bits(run())).toBe(row.expected);
    }
  });
  it('retains the distant low tail and canonicalizes bound zero', () => {
    expect(binary64Bits(upwardSmallSum(1, Number.MIN_VALUE))).toBe('3ff0000000000001');
    expect(binary64Bits(upwardProduct(-0, 1))).toBe('0000000000000000');
    for (const value of [NaN, Infinity, -Infinity, -1]) expect(() => upwardProduct(value, 1)).toThrow();
  });
  it('independently brackets every protected small-bound result with exact fractions', () => {
    for (const row of corpus.arithmetic.small_bounds) {
      const value = BigInt('0x' + row.value) & 0x7fffffffffffffffn, scale = BigInt('0x' + row.scale);
      const base = scaledOracle(scale, 64), rounding = scaledOracle(value, 53);
      expect(base.toString(16).padStart(16, '0')).toBe(row.b0);
      expect(rounding.toString(16).padStart(16, '0')).toBe(row.rounding);
      const exact = add(add(fraction(base), fraction(rounding)), fraction(1n));
      const actual = absoluteBound(decodeBinary64(row.value), decodeBinary64(row.scale));
      expectLeastUpper(actual, exact);
      expect(BigInt('0x' + binary64Bits(actual))).toBe(upperWord(exact));
    }
  });
  it('independently brackets products, the normal boundary and distant-tail sums', () => {
    for (const row of corpus.arithmetic.products) {
      const exact = multiply(fraction(BigInt('0x' + row.a)), fraction(BigInt('0x' + row.b)));
      if (row.expected === null) { expect(() => upperWord(exact)).toThrow(); continue; }
      expectLeastUpper(upwardProduct(decodeBinary64(row.a), decodeBinary64(row.b)), exact);
    }
    for (const [a, b] of [[1, Number.MIN_VALUE], [2 ** -1022, Number.MIN_VALUE], [0, -0]]) {
      const exact = add(add(fraction(BigInt('0x' + binary64Bits(a))), fraction(BigInt('0x' + binary64Bits(b)))), fraction(1n));
      expectLeastUpper(upwardSmallSum(a, b), exact);
    }
    expect(() => upwardSmallSum(Number.MAX_VALUE, 0)).toThrow();
    expect(() => upwardSmallSum(Number.MAX_VALUE, Number.MAX_VALUE)).toThrow();
  });
  it('keeps zero/sign behavior explicit at every finite helper entrypoint', () => {
    for (const zero of [0, -0]) {
      for (const value of [0, -0, 1, -1, Number.MAX_VALUE, -Number.MAX_VALUE]) expect(binary64Bits(absoluteBound(value, zero))).toBe('0000000000000000');
      expect(binary64Bits(upwardProduct(zero, Number.MAX_VALUE))).toBe('0000000000000000');
      expect(binary64Bits(upwardProduct(Number.MAX_VALUE, zero))).toBe('0000000000000000');
      expect(binary64Bits(upwardSmallSum(zero, zero))).toBe('0000000000000001');
    }
    for (const invalid of [-1, NaN, Infinity, -Infinity]) {
      expect(() => absoluteBound(0, invalid)).toThrow();
      expect(() => upwardSmallSum(invalid, 0)).toThrow(); expect(() => upwardSmallSum(0, invalid)).toThrow();
    }
    for (const invalid of [NaN, Infinity, -Infinity]) expect(() => absoluteBound(invalid, 0)).toThrow();
    expect(binary64Bits(absoluteBound(-16, Number.MIN_VALUE))).toBe(binary64Bits(absoluteBound(16, Number.MIN_VALUE)));
  });
});

import { validateRetainedPrecision, validateRetainedPrecisionTransport, RetainedPrecisionError, phi512, eHat, stopFeasible, nativeSchedule, ordinaryAttempts, accountingRules, nativeRuns } from './retainedPrecision';
import { canonicalSha256HexCheckedV1 } from '../../services/hashService';
async function rehash(source: any) {
  const body = source.retained_precision.body;
  for (const s of body.sources) if (s.preparation) {
    const a = body.product_attempts[s.preparation.attempt_ref];
    s.preparation.sha256 = await canonicalSha256HexCheckedV1({ domain: 'retained_precision_preparation_v1', payload: {
      definition_id: a.definition_id, definition_sha256: 'a7ed7ca0bf0bba6e8b821ca4befa00a0fa9541a83694be8b28ac63e39b1d0349', owner_ref: a.owner_ref, ordinary_attempt_ref: a.ordinary_attempt_ref, material_basis_ref: a.material_basis_ref,
      members: a.preparation.members.map((m: any) => ({ member: m.member, old_source: m.old_source, old_facts: m.old_facts, section: m.result.section })) } });
  }
  for (const c of body.cases) if (c.status === 'selected') { const { index: _, ...s } = body.sources[c.source_ref]; c.source_identity_sha256 = await canonicalSha256HexCheckedV1({ domain: 'retained_precision_source_mp_v2', payload: s }); }
  const { retained_precision: _, ...publication } = source;
  body.publication_sha256 = await canonicalSha256HexCheckedV1({ domain: 'retained_precision_publication_mp_v2', payload: publication });
  source.retained_precision.receipt_sha256 = await canonicalSha256HexCheckedV1({ domain: 'retained_precision_receipt_mp_v2', payload: body });
}
function applyEdits(root: any, edits: any[] | undefined): void {
  for (const edit of edits ?? []) {
    let value = root; for (const key of edit.path.slice(0, -1)) value = value[key];
    const key = edit.path.at(-1);
    // RV78-N5: an array removal splices (no hole); unknown operations are refused.
    if (edit.op === 'remove') { if (Array.isArray(value)) value.splice(key, 1); else delete value[key]; }
    else if (edit.op === 'set') value[key] = structuredClone(edit.value);
    else throw new Error('unsupported edit op ' + edit.op);
  }
}
/** SHARED_SNAPSHOT_06C format_change: source edits; invocation edits on a copy of the base
 * invocation; a non-empty invocation edit list rebinds the receipt's invocation digest; then rehash. */
async function applyEntry(m: any): Promise<{ base: any; source: any; invocation: any }> {
  const base = corpus.cases.find((c: any) => c.id === m.base), source = structuredClone(base.source), invocation = structuredClone(base.invocation);
  applyEdits(source, m.edits);
  applyEdits(invocation, m.invocation_edits);
  if (m.invocation_edits?.length) source.retained_precision.body.invocation.value = await canonicalSha256HexCheckedV1({ domain: 'source_blocks_invocation_v1', payload: invocation });
  // D11/RV78-N5: the shared format admits only rehash "all"; any other value is refused.
  if (m.rehash !== 'all') throw new Error('unsupported rehash ' + m.rehash);
  await rehash(source);
  return { base, source, invocation };
}
describe('shared synthetic prepared receipt controls, never solver execution evidence', () => {
  for (const c of corpus.cases) {
    it(c.id, async () => {
      const source = structuredClone(c.source), invocation = structuredClone(c.invocation);
      const before = structuredClone({ source, invocation });
      const result = await validateRetainedPrecision(source, invocation);
      expect({ invocation_bound: result.invocation_bound, numerical_eligible: result.numerical_eligible, standing: result.standing }).toEqual(c.expected);
      expect(result.classifications).toEqual(c.expected_classifications);
      expect({ source, invocation }).toEqual(before);
      expect(Object.isFrozen(result)).toBe(true);
    });
    it(c.id + ' missing invocation and metadata transport remain needs-recompute', async () => {
      const unbound = await validateRetainedPrecision(c.source);
      expect(unbound.invocation_bound).toBe(false); expect(unbound.numerical_eligible).toBe(false);
      const transport = structuredClone(c.source); delete transport.results;
      const result = await validateRetainedPrecisionTransport(transport);
      expect(result.numerical_eligible).toBe(false); expect(result.classifications).toEqual([]);
    });
    it(c.id + ' snapshots all inputs before awaiting', async () => {
      const s = structuredClone(c.source), invocation = structuredClone(c.invocation);
      const pending = validateRetainedPrecision(s, invocation);
      s.results.length = 0; invocation.request.model.nodes.length = 0;
      expect((await pending).classifications).toEqual(c.expected_classifications);
    });
  }
  for (const m of corpus.mutations ?? []) it(m.id, async () => {
    const { source, invocation } = await applyEntry(m);
    let error: unknown; try { await validateRetainedPrecision(source, invocation); } catch (e) { error = e; }
    expect(error).toBeInstanceOf(RetainedPrecisionError);
    // Per-reader expectations (06b G7 settlement) override the shared expectation for TypeScript.
    expect({ gate: (error as RetainedPrecisionError).gate, code: (error as RetainedPrecisionError).code }).toEqual(m.expected_by_reader?.typescript ?? m.expected);
  });
  // Snapshot 05a: publicly consistent or permitted failure-path rewrites the reader must accept.
  for (const m of corpus.must_pass ?? []) it('must pass: ' + m.id, async () => {
    expect(m.expected).toBe('pass');
    const { base, source, invocation } = await applyEntry(m);
    const result = await validateRetainedPrecision(source, invocation);
    expect(result.numerical_eligible).toBe(false);
    expect(result.classifications).toEqual(base.expected_classifications);
  });
});

// Reader-logic controls mirroring Python's for checklist branches without a native-faithful
// shared base yet (N5 verification-pass terminal, N8 Ceiling, N10 idle entry, O5 source_decline).
describe('reader-logic checklist controls, not corpus or producer evidence', () => {
  const caseOf = (id: string) => structuredClone(corpus.cases.find((c: any) => c.id === id));
  const rejects = (run: () => void) => { let error: unknown; try { run(); } catch (e) { error = e; } expect(error).toBeInstanceOf(RetainedPrecisionError); expect({ gate: (error as any).gate, code: (error as any).code }).toEqual({ gate: 'G5', code: 'RETAINED_PRECISION_ATTEMPT_MISMATCH' }); };
  const stopReason = { space: 'attempt', tag: 'stop_rule', quantity: { tag: 'displacement', dof: { node: 1, component: 'UX' } }, body: 0, kind: 'translation' };
  it('N10/N1: an idle invocation-entry run has no records or charge and never selects', () => {
    const base = caseOf('ordinary_prepared_synthetic').source.retained_precision.body, source = base.sources[0];
    const idle = { ...base.cases[0].run, records: [], attempts: [], case_charge: 0, invocation_increment: 0, kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'budget', scope: 'invocation' } } };
    nativeSchedule(idle, source);
    rejects(() => nativeSchedule({ ...idle, kernel_terminal: { kind: 'selected', reason: null } }, source));
    rejects(() => nativeSchedule({ ...idle, case_charge: 1 }, source));
    // A meter fault at invocation entry is never emitted (C1:66-68): an idle WorkAccounting run is refused.
    rejects(() => nativeSchedule({ ...idle, kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'work_accounting', fault: 'overflow' } } }, source));
  });
  it('N6: a rejected p128 candidate must hand its verification on, so a Ceiling there is refused', () => {
    const base = caseOf('ordinary_prepared_synthetic').source.retained_precision.body, run = base.cases[0].run;
    run.attempts[0].outcome = run.records[0].outcome = { kind: 'rejected', reason: stopReason };
    run.records[1].outcome = { kind: 'solved' };
    run.kernel_terminal = { kind: 'unresolved', reason: { space: 'unresolved', tag: 'ceiling' } };
    rejects(() => nativeSchedule(run, base.sources[0]));
  });
  it('N5: a non-escalating verification-pass failure is terminal and never selects', () => {
    const base = caseOf('ordinary_prepared_synthetic').source.retained_precision.body, run = base.cases[0].run;
    const stop = { space: 'attempt', tag: 'stop', stop: { space: 'stop', tag: 'structure' } };
    run.attempts[0].outcome = run.records[0].outcome = { kind: 'rejected', reason: { space: 'attempt', tag: 'verification_failed' } };
    run.attempts[0].verification = { record: 1, precision: 256, phase: 'failed', reason: stop };
    run.records[1].outcome = { kind: 'failed', reason: stop };
    run.kernel_terminal = { kind: 'refused', reason: { space: 'refusal', tag: 'structure' } };
    nativeSchedule(run, base.sources[0]);
    rejects(() => nativeSchedule({ ...run, kernel_terminal: { kind: 'selected', reason: null } }, base.sources[0]));
    // terminal(stop) is exact: an Unresolved terminal for a Structure refusal is not native.
    rejects(() => nativeSchedule({ ...run, kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'ceiling' } } }, base.sources[0]));
    // An escalating verification-pass stop has no terminal() translation, and the work-fault
    // WorkAccounting alternative is never emitted (C1:66-68), so neither terminal is admitted.
    const pivot = { space: 'attempt', tag: 'stop', stop: { space: 'stop', tag: 'pivot', global_dof: 0 } };
    const escalating = structuredClone(run); escalating.attempts[0].verification.reason = pivot; escalating.records[1].outcome = { kind: 'failed', reason: pivot };
    escalating.kernel_terminal = { kind: 'unresolved', reason: { space: 'unresolved', tag: 'pivot', global_dof: 0 } };
    rejects(() => nativeSchedule(escalating, base.sources[0]));
    rejects(() => nativeSchedule({ ...escalating, kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'work_accounting', fault: 'inconsistent' } } }, base.sources[0]));
    rejects(() => nativeSchedule({ ...run, kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'work_accounting', fault: 'overflow' } } }, base.sources[0]));
  });
  it('N8: a rejected p512 candidate with a solved p1024 verification is the Ceiling', () => {
    const base = caseOf('p512_ladder_synthetic').source.retained_precision.body, run = base.cases[0].run, source = base.sources[base.cases[0].source_ref];
    run.attempts[2].outcome = run.records[2].outcome = { kind: 'rejected', reason: stopReason };
    run.records[3].outcome = { kind: 'solved' };
    run.kernel_terminal = { kind: 'unresolved', reason: { space: 'unresolved', tag: 'ceiling' } };
    nativeSchedule(run, source);
    rejects(() => nativeSchedule({ ...run, kernel_terminal: { kind: 'refused', reason: { space: 'refusal', tag: 'structure' } } }, source));
    // Leaving the ladder is never a work-accounting point, so no WorkAccounting terminal there.
    rejects(() => nativeSchedule({ ...run, kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'work_accounting', fault: 'overflow' } } }, source));
  });
  it('R1-R3: each 06d accounting mutation falsifies exactly its own rule on one attempt', async () => {
    const intended: Record<string, boolean[]> = { adapter_fault_present: [false, true, true], accounting_cause_without_fault: [false, true, true], scalar_trace_lost_unavailable: [true, false, true], work_accounting_cause_exact_status: [true, true, false] };
    for (const c of corpus.cases) for (const a of c.source.retained_precision.body.product_attempts) expect(accountingRules(a), c.id).toEqual([true, true, true]);
    for (const [id, rules] of Object.entries(intended)) {
      const m = corpus.mutations.find((x: any) => x.id === id), { source } = await applyEntry(m);
      const failing = source.retained_precision.body.product_attempts.map((a: any) => accountingRules(a)).filter((r: boolean[]) => r.includes(false));
      expect(failing, id).toEqual([rules]);
    }
  });
  it('O5: a source decline names its own unavailable case and material basis', () => {
    const fixture = caseOf('two_case_preparation_failure_synthetic'), body = fixture.source.retained_precision.body;
    const decline = { input_owner: { case_index: 1, case_id: body.cases[1].basis_ref.ref_id, material_basis_ref: body.ordinary_attempts[1].material_basis_ref },
      constructor_counts: { nodes: 2, members: 1, springs: 0, constraints: 6, nodal_terms: 6, stations: 3, supports: 1, id_utf8_bytes: 0, directional_springs: 0 }, error: { tag: 'no_nodes' } };
    body.cases[1].source_decline = decline;
    ordinaryAttempts(body, fixture.source);
    body.cases[1].source_decline = { ...decline, input_owner: { ...decline.input_owner, case_index: 0 } };
    rejects(() => ordinaryAttempts(body, fixture.source));
    body.cases[1].source_decline = decline; body.cases[0].source_decline = { ...decline, input_owner: { ...decline.input_owner, case_index: 0, case_id: body.cases[0].basis_ref.ref_id } };
    rejects(() => ordinaryAttempts(body, fixture.source));
  });
});

// Review repair 07 (ruling D1-D7, D13, D14): reader-local relations, not shared corpus entries.
// RV78 probe entries (PROBES.json, review evidence; same grammar as the corpus plus post_rehash_edits).
const RV78_PROBES: any[] = [{"id":"R1a_execution_order_swapped","base":"two_case_synthetic","edits":[{"path":["retained_precision","body","work","execution_order"],"op":"set","value":[{"kind":"case","index":1},{"kind":"case","index":0}]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R1b_run_id_not_position","base":"two_case_synthetic","edits":[{"path":["retained_precision","body","cases",1,"run","id"],"op":"set","value":5},{"path":["retained_precision","body","calls",0,"run_refs"],"op":"set","value":[0,5]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R2_old_members_reordered","base":"two_body_synthetic","edits":[{"path":["retained_precision","body","product_attempts",0,"operational","old"],"op":"set","value":[{"member":1,"inputs":["0000000000000000","4014000000000000","0000000000000000","3ff0000000000000","4014000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}},{"member":0,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R3_complete_old_short_of_source","base":"two_body_synthetic","edits":[{"path":["retained_precision","body","product_attempts",0,"operational","old"],"op":"set","value":[{"member":0,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R4_unavailable_source_backref_foreign","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","sources",1,"preparation","attempt_ref"],"op":"set","value":0}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}},{"id":"R5_attempt_and_source_basis_not_ordinary","base":"two_case_two_groups_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"material_basis_ref"],"op":"set","value":0},{"path":["retained_precision","body","sources",1,"material_basis_ref"],"op":"set","value":0}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}},{"id":"R6a_native_error_with_selected_run","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"result","error"],"op":"set","value":{"kind":"native","run_ref":1}}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH"}},{"id":"R8_group_call_out_of_range","base":"two_case_synthetic","edits":[{"path":["retained_precision","body","groups",0,"call"],"op":"set","value":3}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T1_escalating_failed_verification_pass_entered","base":"verification_failure_skip_synthetic","edits":[{"path":["retained_precision","body","cases",0,"run","records",1],"op":"set","value":{"index":1,"precision":256,"role":"verification","outcome":{"kind":"failed","reason":{"space":"attempt","tag":"stop","stop":{"space":"stop","tag":"condition"}}},"residual_basis":320,"corrections":0,"pivot_margin_min":null,"rcond":null,"residual_worst":null,"gate":null,"work":{"wide_lme":1,"exact_sum_lme":0,"own_lme":1,"shared_lme":4,"stop_rule_lme":0,"verification_lme":1,"verification_shared_lme":0,"own_stages":{"formation":0,"assembly":0,"residual_formation":0,"factor":0,"condition":0,"rhs":0,"solve":0,"refinement":0,"recovery":0,"stop_rule":0,"bounded_gate":0,"scale":0,"estimate":0,"charge":0,"bound":1,"shift":0,"bounded_formation":0,"wide_formation":0,"uc":0},"shared_stages":{"formation":4,"assembly":0,"residual_formation":0,"factor":0,"condition":0,"rhs":0,"solve":0,"refinement":0,"recovery":0,"stop_rule":0,"bounded_gate":0,"scale":0,"estimate":0,"charge":0,"bound":0,"shift":0,"bounded_formation":0,"wide_formation":0,"uc":0},"shared_built_here":true,"verification_shared_built_here":false},"storage":{"pattern_entries":144,"profile_entries":21,"limbs_per_entry":4},"verification":null,"bound_refusals":[],"shared_build_ref":1,"verification_shared_build_ref":null}},{"path":["retained_precision","body","cases",0,"run","attempts",0],"op":"set","value":{"precision":128,"candidate_record":0,"origin":{"kind":"fresh"},"verification":{"record":1,"precision":256,"phase":"failed","reason":{"space":"attempt","tag":"stop","stop":{"space":"stop","tag":"condition"}}},"outcome":{"kind":"rejected","reason":{"space":"attempt","tag":"verification_failed"}},"charges":[{"record":0,"part":"solve_and_verification"},{"record":0,"part":"candidate_stop"},{"record":1,"part":"solve_and_verification"}],"case_charge":9,"invocation_increment":9}},{"path":["retained_precision","body","cases",0,"run","case_charge"],"op":"set","value":37},{"path":["retained_precision","body","cases",0,"run","invocation_increment"],"op":"set","value":37},{"path":["retained_precision","body","cases",0,"run","invocation_after"],"op":"set","value":37},{"path":["retained_precision","body","calls",0,"invocation_after"],"op":"set","value":37},{"path":["retained_precision","body","work","charged"],"op":"set","value":37}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T2_stop_rule_quantity_other_body","base":"p512_ladder_synthetic","edits":[{"path":["retained_precision","body","cases",0,"run","records",0,"outcome","reason","quantity"],"op":"set","value":{"tag":"displacement","dof":{"node":3,"component":"UX"}}},{"path":["retained_precision","body","cases",0,"run","attempts",0,"outcome","reason","quantity"],"op":"set","value":{"tag":"displacement","dof":{"node":3,"component":"UX"}}}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T3_candidate_record_with_verification","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","cases",0,"run","records",0,"verification"],"op":"set","value":{"resolution":[{"body":0,"force":"426d1a94a2000000","moment":"426d1a94a2000000"}],"theta":[{"body":0,"value":"0000000000000000"}],"bound":[{"body":0,"value":"3ff0000000000000"}],"data_blocks":1,"shift_factorizations":0,"g_max":0,"uc_missing":null,"g_violation":null}}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T4a_ordinary_diagnostic_ref_duplicate","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","ordinary_attempts",0,"diagnostic_refs"],"op":"set","value":["diagnostic:numerical-integrity:case:six-component-load","diagnostic:numerical-integrity:case:six-component-load"]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T4b_ordinary_diagnostic_ref_dangling","base":"ordinary_prepared_synthetic","edits":[{"path":["retained_precision","body","ordinary_attempts",0,"diagnostic_refs"],"op":"set","value":["diagnostic:numerical-integrity:case:six-component-load","diagnostic:rv78:absent"]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"T4c_source_identity_stale_receipt_rehashed","base":"ordinary_prepared_synthetic","edits":[],"invocation_edits":[],"post_rehash_edits":[{"path":["retained_precision","body","cases",0,"source_identity_sha256"],"op":"set","value":"0000000000000000000000000000000000000000000000000000000000000000"}],"rehash":"all","expected":{"gate":"G1","code":"RETAINED_PRECISION_RECEIPT_MISMATCH"}},{"id":"T4d_ordinary_dangling_plus_adapter_fault","base":"two_case_facade_after_certificate_synthetic","edits":[{"path":["retained_precision","body","ordinary_attempts",1,"diagnostic_refs"],"op":"set","value":["diagnostic:numerical-integrity:case:unavailable-row","diagnostic:rv78:absent"]},{"path":["retained_precision","body","product_attempts",1,"adapter","fault"],"op":"set","value":{"kind":"overflow","event":"map_write"}}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}},{"id":"R2b_unsourced_old_member_noncontiguous","base":"two_case_preparation_failure_synthetic","edits":[{"path":["retained_precision","body","product_attempts",1,"operational","old",0],"op":"set","value":{"member":1,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"R3b_complete_old_longer_than_source","base":"two_body_synthetic","edits":[{"path":["retained_precision","body","product_attempts",0,"operational","old"],"op":"set","value":[{"member":0,"inputs":["0000000000000000","0000000000000000","0000000000000000","3ff0000000000000","0000000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}},{"member":1,"inputs":["0000000000000000","4014000000000000","0000000000000000","3ff0000000000000","4014000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}},{"member":2,"inputs":["0000000000000000","4014000000000000","0000000000000000","3ff0000000000000","4014000000000000","0000000000000000","42474876e8000000","4231ed8ec2000000","3f6c4f3caf32fd23","3ee61aa4872838c0"],"result":{"kind":"ready","length":"3ff0000000000000","axial_stiffness":"41c4990f17e516ad","torsional_stiffness":"4128c47ead23fa80","normalization":["3ff0000000000000","0000000000000000","0000000000000000"]},"work":{"entered":0,"checks":0,"lost":false}}]}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G3","code":"RETAINED_PRECISION_COVERAGE_MISMATCH"}},{"id":"B_interpolation_target_at_lower_point_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4072c00000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4072c00000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":300,"unit":"K"}}],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_interpolation_target_below_range_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4072b00000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4072b00000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":299,"unit":"K"}}],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_interpolation_target_at_upper_point_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4073600000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4073600000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":310,"unit":"K"}}],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_interpolation_target_above_range_equal_point_E","base":"ordinary_prepared_interpolated_material_synthetic","edits":[{"path":["retained_precision","body","material_bases",0,"selector","kelvin"],"op":"set","value":"4073700000000000"},{"path":["retained_precision","body","material_bases",0,"materials",0,"selection","target_kelvin"],"op":"set","value":"4073700000000000"}],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","load_cases",0,"modulus_basis_temperature"],"op":"set","value":{"value":311,"unit":"K"}}],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G8","code":"RETAINED_PRECISION_PREPARATION_MISMATCH"}},{"id":"B_control_equal_point_E_bracketed","base":"ordinary_prepared_interpolated_material_synthetic","edits":[],"invocation_edits":[{"path":["request","model","materials",0,"temperature_points",0,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}},{"path":["request","model","materials",0,"temperature_points",1,"elastic_modulus"],"op":"set","value":{"value":200000000000.0,"unit":"Pa"}}],"post_rehash_edits":[],"rehash":"all","expected":"pass"},{"id":"T4e_selected_case_ordinary_checks_passed","base":"ordinary_prepared_synthetic","edits":[{"path":["numerical_quality","cases",0,"solve_quality"],"op":"set","value":"checks_passed"},{"path":["retained_precision","body","ordinary_attempts",0,"initial","outcome"],"op":"set","value":"checks_passed"}],"invocation_edits":[],"post_rehash_edits":[],"rehash":"all","expected":{"gate":"G5","code":"RETAINED_PRECISION_ATTEMPT_MISMATCH"}}];
async function rehashOuter(source: any) {
  const { retained_precision: _, ...publication } = source, body = source.retained_precision.body;
  body.publication_sha256 = await canonicalSha256HexCheckedV1({ domain: 'retained_precision_publication_mp_v2', payload: publication });
  source.retained_precision.receipt_sha256 = await canonicalSha256HexCheckedV1({ domain: 'retained_precision_receipt_mp_v2', payload: body });
}
async function firstFailure(source: any, invocation?: any): Promise<{ gate: string; code: string } | 'pass'> {
  try { const r = await validateRetainedPrecision(source, invocation); expect(r.numerical_eligible).toBe(false); return 'pass'; }
  catch (e) { expect(e).toBeInstanceOf(RetainedPrecisionError); return { gate: (e as any).gate, code: (e as any).code }; }
}
async function edited(baseId: string, edit: (source: any, invocation: any) => void, rehashAll = true) {
  const base = structuredClone(corpus.cases.find((c: any) => c.id === baseId)); edit(base.source, base.invocation);
  if (rehashAll) await rehash(base.source);
  return base;
}
const G = (gate: string, suffix: string) => ({ gate, code: gate === 'G0' ? suffix : 'RETAINED_PRECISION_' + suffix });
describe('review repair 07: RV78 probe relations (reader-local)', () => {
  for (const p of RV78_PROBES) it(p.id, async () => {
    const { source, invocation } = await applyEntry(p);
    if (p.post_rehash_edits.length) { applyEdits(source, p.post_rehash_edits); await rehashOuter(source); }
    expect(await firstFailure(source, invocation)).toEqual(p.expected);
  });
});
describe('review repair 07: decisions without a probe (reader-local)', () => {
  it('D1/RV81-B1: unsourced old ids must be 0..len-1 at G3, with or without the invocation', async () => {
    const p = RV78_PROBES.find(x => x.id === 'R2b_unsourced_old_member_noncontiguous'), { source } = await applyEntry(p);
    expect(await firstFailure(source)).toEqual(G('G3', 'COVERAGE_MISMATCH'));
  });
  it('D1: unsourced complete old coverage is non-empty and matches the CaseSource member count', async () => {
    const empty = await edited('two_case_preparation_failure_synthetic', s => { s.retained_precision.body.product_attempts[1].operational.old = []; });
    expect(await firstFailure(empty.source, empty.invocation)).toEqual(G('G3', 'COVERAGE_MISMATCH'));
    const longer = await edited('two_case_preparation_failure_synthetic', s => { const old = s.retained_precision.body.product_attempts[1].operational.old; old.push({ ...structuredClone(old[0]), member: old.length }); });
    expect(await firstFailure(longer.source, longer.invocation)).toEqual(G('G3', 'COVERAGE_MISMATCH'));
  });
  it('D1/RV81-S1: a captured prefix with a Run is a G5 association defect, not G3', async () => {
    const m = structuredClone(corpus.must_pass.find((x: any) => x.id === 'prefix_captured'));
    m.edits.push({ path: ['retained_precision', 'body', 'product_attempts', 1, 'run_ref'], op: 'set', value: 0 });
    const { source, invocation } = await applyEntry(m);
    expect(await firstFailure(source, invocation)).toEqual(G('G5', 'PRODUCT_ATTEMPT_MISMATCH'));
  });
  it('D2: G0 owns the producer component/schema versions, receipt constants and thresholds; body shape waits for G1', async () => {
    const at0 = async (edit: (s: any) => void) => { const c = structuredClone(corpus.cases[0]); edit(c.source); return firstFailure(c.source, c.invocation); };
    expect(await at0(s => { s.producer.component_version = '0.1.0'; })).toEqual(G('G0', 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED'));
    expect(await at0(s => { s.producer.component_name = 'other'; })).toEqual(G('G0', 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED'));
    expect(await at0(s => { s.schema_version = '0.3.0'; })).toEqual(G('G0', 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED'));
    expect(await at0(s => { s.retained_precision.body.canonicalization = 'other'; })).toEqual(G('G0', 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED'));
    expect(await at0(s => { delete s.retained_precision.body.work; })).toEqual(G('G0', 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED'));
    expect(await at0(s => { s.retained_precision.body.product_attempts = {}; })).toEqual(G('G1', 'RECEIPT_MISMATCH'));
    expect(await at0(s => { s.retained_precision.body.product_attempts[0] = 7; })).toEqual(G('G1', 'RECEIPT_MISMATCH'));
  });
  it('D3: a native class with an ATTEMPT defect reports ATTEMPT even when an earlier-coded WORK defect exists', async () => {
    const p = structuredClone(RV78_PROBES.find(x => x.id === 'R8_group_call_out_of_range'));
    p.edits.push({ path: ['retained_precision', 'body', 'calls', 0, 'invocation_before'], op: 'set', value: 1 });
    const { source, invocation } = await applyEntry(p);
    expect(await firstFailure(source, invocation)).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
    const workOnly = await edited('two_case_synthetic', s => { s.retained_precision.body.calls[0].invocation_before = 1; });
    expect(await firstFailure(workOnly.source, workOnly.invocation)).toEqual(G('G5', 'WORK_MISMATCH'));
  });
  it('D4c/RV81-B2: a prepared_product_failure cause must name the case\'s own attempt', async () => {
    for (const cause of [1, 0]) {
      const c = await edited('two_case_preparation_failure_synthetic', s => {
        const b = s.retained_precision.body; b.product_attempts = [b.product_attempts[0]]; b.cases[1].product_attempt_ref = null; b.cases[1].reason.cause.product_attempt_ref = cause;
      });
      expect(await firstFailure(c.source, c.invocation), String(cause)).toEqual(G('G5', 'PRODUCT_ATTEMPT_MISMATCH'));
    }
  });
  it('D4e: run_ref is null exactly when no native call happened', async () => {
    const c = await edited('ordinary_prepared_synthetic', s => { s.retained_precision.body.product_attempts[0].run_ref = null; });
    expect(await firstFailure(c.source, c.invocation)).toEqual(G('G5', 'PRODUCT_ATTEMPT_MISMATCH'));
    const p = await edited('two_case_preparation_failure_synthetic', s => { s.retained_precision.body.product_attempts[1].run_ref = 0; });
    expect(await firstFailure(p.source, p.invocation)).toEqual(G('G5', 'PRODUCT_ATTEMPT_MISMATCH'));
  });
  it('D5c: rejected(verification_failed) requires a failed verification phase', () => {
    const base = structuredClone(corpus.cases.find((c: any) => c.id === 'p512_ladder_synthetic')).source.retained_precision.body, run = base.cases[0].run;
    run.attempts[2].outcome = run.records[2].outcome = { kind: 'rejected', reason: { space: 'attempt', tag: 'verification_failed' } };
    run.records[3].outcome = { kind: 'solved' }; run.kernel_terminal = { kind: 'unresolved', reason: { space: 'unresolved', tag: 'ceiling' } };
    let error: any; try { nativeSchedule(run, base.sources[base.cases[0].source_ref]); } catch (e) { error = e; }
    expect({ gate: error?.gate, code: error?.code }).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
  });
  it('D5a/RV81-M04: a candidate record carrying verification work alone is an ATTEMPT defect', async () => {
    const c = await edited('ordinary_prepared_synthetic', s => { const r = s.retained_precision.body.cases[0].run.records[0]; r.work.verification_lme = 1; });
    expect(await firstFailure(c.source, c.invocation)).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
  });
  it('D6c: a published W2 needs a nonzero exponent and the initial failure\'s trigger', () => {
    const fixture = structuredClone(corpus.cases[0]), body = fixture.source.retained_precision.body, o = body.ordinary_attempts[0];
    const error = { tag: 'synthetic_formation_error' }, ref = o.initial.report_diagnostic_ref;
    o.initial = { kind: 'formation_failure', error };
    o.w2 = { kind: 'published', trigger: { tag: 'formation', error }, force_scale_exponent: 1, report_diagnostic_ref: ref };
    ordinaryAttempts(body, fixture.source);
    const rejects = (edit: (w: any) => void) => { const b = structuredClone(body); edit(b.ordinary_attempts[0].w2); let e: any; try { ordinaryAttempts(b, fixture.source); } catch (x) { e = x; } expect({ gate: e?.gate, code: e?.code }).toEqual(G('G5', 'ATTEMPT_MISMATCH')); };
    rejects(w => { w.force_scale_exponent = 0; });
    rejects(w => { w.trigger.tag = 'evaluation'; });
    rejects(w => { w.trigger.error = { tag: 'other' }; });
  });
  it('D6d/RV81-N2: legacy_source.work_ref is a reference check reported as ATTEMPT', () => {
    const fixture = structuredClone(corpus.cases[0]), body = fixture.source.retained_precision.body;
    const run = (work: any[], ref: number) => { const b = structuredClone(body); b.legacy_source_work = work; b.ordinary_attempts[0].legacy_source.work_ref = ref; let e: any; try { ordinaryAttempts(b, fixture.source); } catch (x) { e = x; } return e ? { gate: e.gate, code: e.code } : 'pass'; };
    expect(run([], 0)).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
    expect(run([{ case_index: 1 }], 0)).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
    expect(run([{ case_index: 0 }], 0)).toBe('pass');
  });
  it('D7: a RETAINED_PRECISION_UNAVAILABLE diagnostic naming no requested case fails G4', async () => {
    const c = await edited('ordinary_prepared_synthetic', s => {
      const d = structuredClone(s.diagnostics.find((x: any) => x.code === 'RETAINED_PRECISION_SELECTED'));
      s.diagnostics.push({ ...d, id: 'diagnostic:i64:foreign-case', code: 'RETAINED_PRECISION_UNAVAILABLE', affected_refs: ['case:not-requested'] });
    });
    expect(await firstFailure(c.source, c.invocation)).toEqual(G('G4', 'DIAGNOSTIC_MISMATCH'));
  });
  it('D13/RV81-M13: a no-data body needs theta = +0 in its verification record', async () => {
    const c = await edited('ordinary_prepared_no_data_synthetic', s => { const b = s.retained_precision.body; b.cases[0].selection.theta[0].value = '3fd0000000000000'; b.cases[0].run.records[1].verification.theta[0].value = '3fd0000000000000'; });
    expect(await firstFailure(c.source, c.invocation)).toEqual(G('G5a', 'SCALE_MISMATCH'));
  });
  it('D13/RV81-M16: a p128 verification-solve failure continues at p512, so it never ends in the Ceiling', () => {
    const base = structuredClone(corpus.cases.find((c: any) => c.id === 'verification_failure_skip_synthetic')).source.retained_precision.body, run = base.cases[0].run;
    const truncated = { ...run, attempts: [run.attempts[0]], records: run.records.slice(0, 2), kernel_terminal: { kind: 'unresolved', reason: { space: 'unresolved', tag: 'ceiling' } } };
    let error: any; try { nativeSchedule(truncated, base.sources[base.cases[0].source_ref]); } catch (e) { error = e; }
    expect({ gate: error?.gate, code: error?.code }).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
  });
  it('D13/RV81-M08: R3 needs every fault of every work_accounting cause, including both', () => {
    const attempt = (causes: any[], statuses: string[]) => ({ adapter: { fault: null }, causes, work: statuses.map(s => ({ sticky_status: s })) });
    expect(accountingRules(attempt([{ kind: 'work_accounting', fault: 'both' }], ['overflow']))[2]).toBe(false);
    expect(accountingRules(attempt([{ kind: 'work_accounting', fault: 'both' }], ['overflow', 'inconsistent']))[2]).toBe(true);
    expect(accountingRules(attempt([{ kind: 'work_accounting', fault: 'both' }], ['both']))[2]).toBe(true);
    expect(accountingRules(attempt([{ kind: 'work_accounting', fault: 'overflow' }, { kind: 'work_accounting', fault: 'inconsistent' }], ['overflow']))[2]).toBe(false);
  });
  it('D13: the absolute bound switches at S = 2^-988 on both sides', () => {
    const value = 3, valueWord = BigInt('0x' + binary64Bits(value));
    const at = 2 ** -988, below = decodeBinary64((BigInt('0x' + binary64Bits(at)) - 1n).toString(16).padStart(16, '0'));
    expect(BigInt('0x' + binary64Bits(absoluteBound(value, at)))).toBe(scaledOracle(BigInt('0x' + binary64Bits(at)), 64));
    const exact = add(add(fraction(scaledOracle(BigInt('0x' + binary64Bits(below)), 64)), fraction(scaledOracle(valueWord, 53))), fraction(1n));
    expect(BigInt('0x' + binary64Bits(absoluteBound(value, below)))).toBe(upperWord(exact));
  });
  it('RV81-M07 (N17): the case scope wins when both budget limits are exceeded', () => {
    const body = structuredClone(corpus.cases[0]).source.retained_precision.body, run = body.cases[0].run;
    body.cases[0].status = 'unavailable'; body.work.case_limit = 10; body.work.invocation_limit = 10;
    const withScope = (scope: string) => { const b = structuredClone(body), r = b.cases[0].run; const stop = { space: 'attempt', tag: 'stop', stop: { space: 'stop', tag: 'budget', scope } };
      r.attempts[0].outcome = r.records[0].outcome = { kind: 'failed', reason: stop }; r.records[1].outcome = { kind: 'solved' };
      r.kernel_terminal = { kind: 'unresolved', reason: { space: 'unresolved', tag: 'budget', scope } }; let e: any; try { nativeRuns(b); } catch (x) { e = x; } return e ? { gate: e.gate, code: e.code } : 'pass'; };
    expect(run.case_charge).toBeGreaterThan(10);
    expect(withScope('case')).toBe('pass');
    expect(withScope('invocation')).toEqual(G('G5', 'WORK_MISMATCH'));
  });
  it('D12/N11: a refused group preparation gives a Run with its group index, no attempts and the refusal', () => {
    const body = structuredClone(corpus.cases[0]).source.retained_precision.body, run = body.cases[0].run, refusal = { space: 'refusal', tag: 'structure' };
    body.cases[0].status = 'unavailable'; body.groups[0].preparation = { kind: 'refused', reason: refusal }; body.builds = [];
    Object.assign(run, { records: [], attempts: [], case_charge: 0, invocation_increment: 0, invocation_after: 0, cache_after: [], kernel_terminal: { kind: 'refused', reason: refusal } });
    body.calls[0].invocation_after = 0; body.work.charged = 0;
    const result = (edit: (b: any) => void) => { const b = structuredClone(body); edit(b); let e: any; try { nativeRuns(b); } catch (x) { e = x; } return e ? { gate: e.gate, code: e.code } : 'pass'; };
    expect(run.origin.group).toBe(0);
    expect(result(() => undefined)).toBe('pass');
    expect(result(b => { b.cases[0].run.kernel_terminal = { kind: 'refused', reason: { space: 'refusal', tag: 'negative_energy', i: 0, j: 1 } }; })).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
    expect(result(b => { b.cases[0].run.origin.group = null; })).toEqual(G('G5', 'ATTEMPT_MISMATCH'));
  });
  it('RV81-M12: a non-null empty roster fails G3 even against an empty body inventory', async () => {
    const c = await edited('ordinary_prepared_no_data_synthetic', s => { const b = s.retained_precision.body; b.sources[0].body_membership = []; b.product_attempts[0].proof.summary_coverage = []; });
    expect(await firstFailure(c.source, c.invocation)).toEqual(G('G3', 'COVERAGE_MISMATCH'));
  });
  it('D11/RV78-N5: the harness admits only rehash "all" and splices array removals', async () => {
    expect([...corpus.mutations, ...corpus.must_pass].every((m: any) => m.rehash === 'all')).toBe(true);
    await expect(applyEntry({ ...corpus.mutations[0], rehash: 'receipt' })).rejects.toThrow('unsupported rehash');
    const list = [1, 2, 3]; applyEdits({ list }, [{ path: ['list', 1], op: 'remove' }]); expect(list).toEqual([1, 3]);
  });
  it('D14: no non-test module imports the @internal reader exports', async () => {
    const fs = await import('node:fs'), path = await import('node:path');
    const root = path.resolve(__dirname, '../..'), internal = ['nativeSchedule', 'nativeRuns', 'ordinaryAttempts', 'accountingRules', 'stopFeasible', 'phi512', 'eHat'];
    const offenders: string[] = [];
    for (const rel of fs.readdirSync(root, { recursive: true }) as string[]) {
      if (!/\.(ts|tsx)$/.test(rel) || /\.test\.(ts|tsx)$/.test(rel) || rel.endsWith(path.join('results', 'retainedPrecision.ts'))) continue;
      const text = fs.readFileSync(path.join(root, rel), 'utf8');
      for (const m of text.matchAll(/import\s*\{([^}]*)\}\s*from\s*['"][^'"]*retainedPrecision['"]/g)) if (internal.some(name => new RegExp('\\b' + name + '\\b').test(m[1]))) offenders.push(rel);
    }
    expect(offenders).toEqual([]);
  });
});

describe('native p512 floor rounding, independent of any corpus case', () => {
  // Literal transcription of verify.rs phi_512 and adaptive.rs next_up, for comparison only.
  const fromWord = (word: bigint) => { const v = new DataView(new ArrayBuffer(8)); v.setBigUint64(0, word); return v.getFloat64(0); };
  function nativePhi(hat: number): number {
    const nearest = hat * fromWord(0x2490000000000000n);
    if (!(nearest * fromWord(0x5b50000000000000n) < hat)) return nearest;
    return nearest === 0 ? fromWord(1n) : fromWord(BigInt('0x' + binary64Bits(nearest)) + 1n);
  }
  const words = [0n, 1n, 3n, 0x000fffffffffffffn, 0x0010000000000000n, 0x1b6fffffffffffffn, 0x1b70000000000001n, 0x1b80000000000003n, 0x2000000000000001n,
    0x249fffffffffffffn, 0x3ff0000000000000n, 0x3ff0000000000001n, 0x426d1a94a2000000n, 0x7fefffffffffffffn];
  let seed = 0x9e3779b97f4a7c15n;
  for (let i = 0; i < 200; i++) { seed = (seed * 6364136223846793005n + 1442695040888963407n) & ((1n << 64n) - 1n); words.push(seed % 0x7ff0000000000000n); }
  it('phi512 is the least binary64 at or above 2^-438 * e_hat and equals the native transcription', () => {
    for (const word of words) {
      const hat = fromWord(word), phi = phi512(hat);
      expect(binary64Bits(phi), word.toString(16)).toBe(binary64Bits(nativePhi(hat)));
      const exact = multiply(fraction(word), [1n, 1n << 438n]);
      expect(BigInt('0x' + binary64Bits(phi)), word.toString(16)).toBe(upperWord(exact));
      expect(phi > 0).toBe(hat > 0);
    }
  });
  // Row-level transcription of final_case.rs summary_coverage_data (D = false in C3): every
  // kind is absent, input-only, non-input zero or non-input nonzero; L = 0 or not; floor none or
  // any sign pair. The feasible stop set must equal the natively generated set exactly.
  it('stopFeasible admits exactly the natively generated stop vectors, including L = 0', () => {
    const bits = (n: number) => [0, 1, 2, 3].map(k => ((n >> k) & 1) === 1);
    let groups = 0;
    for (let state = 0; state < 256; state++) {
      const kinds = [0, 1, 2, 3].map(k => (state >> (2 * k)) & 3); // 0 absent, 1 input-only, 2 non-input zero, 3 non-input nonzero
      const present = kinds.map(s => s > 0), nonInput = kinds.map(s => s >= 2);
      for (const extentNonzero of [false, true]) for (const floor of [null, [false, false], [false, true], [true, false], [true, true]] as (boolean[] | null)[]) {
        const native = (nonzero: boolean[]) => {
          let positive = [0, 1, 2, 3].map(k => nonInput[k] && nonzero[k]);
          if (extentNonzero) positive = [positive[0] || positive[1], positive[0] || positive[1], positive[2] || positive[3], positive[2] || positive[3]];
          if (floor) { positive[2] ||= floor[0]; positive[3] ||= floor[1]; }
          return [0, 1, 2, 3].map(k => present[k] && (positive[k] || (nonInput[k] && nonzero[k])));
        };
        const generated = new Set<string>();
        for (let a = 0; a < 16; a++) generated.add(JSON.stringify(native(bits(a))));
        const floors = [floor ?? [false, false]];
        for (let s = 0; s < 16; s++) {
          const stop = bits(s);
          expect(stopFeasible(stop, present, nonInput, extentNonzero, floors), JSON.stringify({ kinds, extentNonzero, floor, stop })).toBe(generated.has(JSON.stringify(stop)));
        }
        groups++;
      }
    }
    expect(groups).toBe(2560);
    // L = 0 keeps translation/rotation independent; L != 0 couples them.
    expect(stopFeasible([true, false, false, false], [true, true, true, true], [true, true, true, true], false, [[false, false]])).toBe(true);
    expect(stopFeasible([true, false, false, false], [true, true, true, true], [true, true, true, true], true, [[false, false]])).toBe(false);
  });
  it('e_hat couples force and moment only for a nonzero extent', () => {
    expect(eHat(2, 3, 0)).toEqual([2, 3]);
    expect(eHat(2, 3, 4)).toEqual([2, 8]);
    expect(eHat(1, 0, 1)).toEqual([1, 1]);
    expect(eHat(0, 0, 5)).toEqual([0, 0]);
  });
});

describe('source-bound recovery controls', () => {
  const base = () => structuredClone(corpus.cases[0]);
  async function rejectedAfterRehash(edit: (source: any) => void, gate: string, code: string) {
    const c = base(); edit(c.source); await rehash(c.source);
    await expect(validateRetainedPrecision(c.source, c.invocation)).rejects.toMatchObject({ gate, code });
  }
  it('rederives K4SRC independently of repaired semantic receipt hashes', async () => {
    await rejectedAfterRehash(source => {
      source.retained_precision.body.sources[0].kernel_source_sha256 = '1'.repeat(64);
    }, 'G8', 'RETAINED_PRECISION_PREPARATION_MISMATCH');
  });
  it('rederives K4STF even when source and group repeat the same forged digest', async () => {
    await rejectedAfterRehash(source => {
      const b = source.retained_precision.body;
      b.sources[0].stiffness_sha256 = '2'.repeat(64); b.groups[0].stiffness_sha256 = '2'.repeat(64);
    }, 'G8', 'RETAINED_PRECISION_PREPARATION_MISMATCH');
  });
  it('keeps signed bound zero invalid at G2 despite a later row-method defect', async () => {
    await rejectedAfterRehash(source => {
      source.retained_precision.body.cases[0].selection.floor_ratio = '8000000000000000';
      source.results[0].recovery_method = '';
    }, 'G2', 'RETAINED_PRECISION_ENCODING_MISMATCH');
  });
  it('binds residual precision to the actual native solve width', async () => {
    await rejectedAfterRehash(source => {
      source.retained_precision.body.cases[0].run.records[0].residual_basis = 1024;
    }, 'G5', 'RETAINED_PRECISION_ATTEMPT_MISMATCH');
  });
  it('reconciles stop-rule stages independently of the total own work', async () => {
    await rejectedAfterRehash(source => {
      const stages = source.retained_precision.body.cases[0].run.records[0].work.own_stages;
      stages.formation += stages.stop_rule; stages.stop_rule = 0;
    }, 'G5', 'RETAINED_PRECISION_WORK_MISMATCH');
  });
  it('reconciles every shared stage with both contributing build records', async () => {
    await rejectedAfterRehash(source => {
      const stages = source.retained_precision.body.builds[0].stages;
      stages.assembly += stages.formation; stages.formation = 0;
    }, 'G5', 'RETAINED_PRECISION_WORK_MISMATCH');
  });
  it('requires the first actual candidate to start at128', async () => {
    await rejectedAfterRehash(source => {
      const b = source.retained_precision.body, run = b.cases[0].run;
      run.records[0].precision = 256; run.records[0].residual_basis = 320;
      run.records[1].precision = 512; run.records[1].residual_basis = 576; run.records[1].storage.limbs_per_entry = 8;
      run.attempts[0].precision = 256; run.attempts[0].verification.precision = 512;
      b.cases[0].selection.precision = 256; b.cases[0].selection.verification_precision = 512;
    }, 'G5', 'RETAINED_PRECISION_ATTEMPT_MISMATCH');
  });
  // I57 §2/§4: G5a rederives the canonical layout and +0 prescription relation from
  // the bound source maps before compact-flag feasibility; G8 binds them later.
  it('rejects a purported input-derived force row at G5a before invocation binding', async () => {
    await rejectedAfterRehash(source => {
      const row = source.retained_precision.body.sources[0].layout.find((r: any) => r.kind === 'force');
      row.input_derived = true;
    }, 'G5a', 'RETAINED_PRECISION_SCALE_MISMATCH');
  });
  it('rejects a constrained displacement row not marked input-derived at G5a', async () => {
    await rejectedAfterRehash(source => {
      const row = source.retained_precision.body.sources[0].layout.find((r: any) => r.input_derived);
      row.input_derived = false;
    }, 'G5a', 'RETAINED_PRECISION_SCALE_MISMATCH');
  });
  it('rejects a nonzero prescription at G5a because D is false only for exact +0', async () => {
    await rejectedAfterRehash(source => {
      source.retained_precision.body.sources[0].constraints[0].value = '3ff0000000000000';
    }, 'G5a', 'RETAINED_PRECISION_SCALE_MISMATCH');
  });
  // I57 §5 trust boundary: publicly consistent attestation rewrites must not be
  // over-rejected; only producer custody/replay can catch them.
  for (const [name, index, edit] of [
    ['stop [T,T,F,F] with its exact stop roster', 0, (b: any) => { b.product_attempts[0].proof.summary_coverage[0].stop = [true, true, false, false]; b.cases[0].selection.stop_rule = b.cases[0].selection.stop_rule.slice(0, 2); }],
    ['all-false stop with an empty stop roster', 0, (b: any) => { b.product_attempts[0].proof.summary_coverage[0].stop = [false, false, false, false]; b.cases[0].selection.stop_rule = []; }],
    ['no-data all-true stop with four zero stop entries', 2, (b: any) => { b.product_attempts[0].proof.summary_coverage[0].stop = [true, true, true, true]; b.cases[0].selection.stop_rule = ['translation', 'rotation', 'force', 'moment'].map(kind => ({ body: 0, kind, value: '0000000000000000' })); }],
    ['no-data body attesting one data block with its bound', 2, (b: any) => {
      const bound = [{ body: 0, value: '3ff0000000000000' }], record = b.cases[0].run.records[1].verification;
      b.product_attempts[0].proof.summary_coverage[0].has_data = true; b.cases[0].selection.certified_bound = bound; record.bound = structuredClone(bound); record.data_blocks = 1;
    }],
  ] as const) it('admits the publicly consistent rewrite: ' + name, async () => {
    const c = structuredClone(corpus.cases[index]); edit(c.source.retained_precision.body); await rehash(c.source);
    expect((await validateRetainedPrecision(c.source, c.invocation)).classifications).toEqual(c.expected_classifications);
  });
  it('requires actual entered proof state and checks it before product work', async () => {
    await rejectedAfterRehash(source => {
      const a = source.retained_precision.body.product_attempts[0];
      a.stages.proof_start = 'not_entered';
      a.preparation.members[0].work.conversions.value = 0;
    }, 'G5', 'RETAINED_PRECISION_PRODUCT_ATTEMPT_MISMATCH');
  });
});
