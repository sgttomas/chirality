// RV125 (RV-X of PR-B1; disposable archive copy only, never committed): the TS reader on the
// successors and invocations RV125's Rust harness wrote (W-C2 and W-C2 permuted c, a, b; both modes),
// bound, unbound and transport. Writes one JSON line per check to RV125_TS_OUT.
import { describe, expect, it } from 'vitest';
import { readFileSync, appendFileSync } from 'node:fs';
import { validateRetainedPrecision, validateRetainedPrecisionTransport } from './retainedPrecision';

const prefix = process.env.RV125_OUT as string;
const out = process.env.RV125_TS_OUT as string;
const show = async (p: Promise<unknown>) => {
  try { const r = await p as Record<string, unknown>; return { ok: true, bound: r.invocation_bound, eligible: r.numerical_eligible, standing: r.standing, classes: (r.classifications as unknown[]).length }; }
  catch (e) { const x = e as { gate?: string; code?: string; message?: string }; return { ok: false, gate: x.gate, code: x.code, message: x.message }; }
};
describe('RV125 TS reader on B1 multi-case successors', () => {
  for (const label of ['w_c2', 'w_c2_cab']) for (const mode of ['sparse_interactive', 'dense_scrutiny']) {
    it(`${label} ${mode}`, async () => {
      const source = JSON.parse(readFileSync(`${prefix}.${label}_${mode}.source.json`, 'utf8'));
      const invocation = JSON.parse(readFileSync(`${prefix}.${label}_${mode}.invocation.json`, 'utf8'));
      const row = { label, mode, ts_bound: await show(validateRetainedPrecision(source, invocation)),
        ts_unbound: await show(validateRetainedPrecision(source)), ts_transport: await show(validateRetainedPrecisionTransport(source)) };
      appendFileSync(out, JSON.stringify(row) + '\n');
      expect(row.ts_bound.ok).toBe(true);
    });
  }
});
