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

import { validateRetainedPrecision, validateRetainedPrecisionTransport, RetainedPrecisionError } from './retainedPrecision';
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
    const base = corpus.cases.find((c: any) => c.id === m.base), source = structuredClone(base.source), invocation = structuredClone(base.invocation);
    for (const edit of m.edits) {
      let value = source; for (const key of edit.path.slice(0, -1)) value = value[key];
      const key = edit.path.at(-1); if (edit.op === 'remove') delete value[key]; else value[key] = structuredClone(edit.value);
    }
    if (m.rehash) await rehash(source);
    let error: unknown; try { await validateRetainedPrecision(source, invocation); } catch (e) { error = e; }
    expect(error).toBeInstanceOf(RetainedPrecisionError);
    expect({ gate: (error as RetainedPrecisionError).gate, code: (error as RetainedPrecisionError).code }).toEqual(m.expected);
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
