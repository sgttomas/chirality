// RV120 (B3 review) raw runner for the TypeScript reader. Not part of any candidate; copied into the reviewer's probe copy only.
// RV120_IN: JSON lines {name, source, invocation}; RV120_OUT: JSON lines {name, bound, unbound, transport}.
import { it } from 'vitest';
import { readFileSync, writeFileSync } from 'node:fs';
import { RetainedPrecisionError, validateRetainedPrecision, validateRetainedPrecisionTransport } from './retainedPrecision';
type J = any;
async function one(run: () => Promise<J>): Promise<J> {
  try { const v = await run(); return { ok: { eligible: v.numerical_eligible, bound: v.invocation_bound } }; }
  catch (e) { if (e instanceof RetainedPrecisionError) return { gate: e.gate, code: e.code, detail: e.detail ?? null }; return { throw: String(e) }; }
}
it('rv120 b3 raw', async () => {
  const input = process.env.RV120_IN, out = process.env.RV120_OUT; if (!input || !out) return;
  const lines: string[] = [];
  for (const text of readFileSync(input, 'utf8').split('\n')) {
    if (!text.trim()) continue;
    const d = JSON.parse(text);
    lines.push(JSON.stringify({ name: d.name,
      bound: await one(() => validateRetainedPrecision(structuredClone(d.source), structuredClone(d.invocation))),
      unbound: await one(() => validateRetainedPrecision(structuredClone(d.source))),
      transport: await one(() => validateRetainedPrecisionTransport(structuredClone(d.source))) }));
  }
  writeFileSync(out, lines.join('\n') + '\n');
}, 3_600_000);
