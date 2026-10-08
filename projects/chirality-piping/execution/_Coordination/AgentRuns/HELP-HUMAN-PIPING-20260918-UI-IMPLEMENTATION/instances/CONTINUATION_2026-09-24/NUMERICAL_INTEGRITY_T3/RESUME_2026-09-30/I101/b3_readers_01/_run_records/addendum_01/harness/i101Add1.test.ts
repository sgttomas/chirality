/** I101 scratch harness (never committed): the TS reader's three readings of I100's addendum-01 shapes.
 * ADD1_INPUTS names I100's input lines ({name, base, source, invocation}); ADD1_OUT receives one line per shape. */
import { expect, it } from 'vitest';
import { readFileSync, writeFileSync } from 'node:fs';
import { validateRetainedPrecision, validateRetainedPrecisionTransport, RetainedPrecisionError } from './retainedPrecision';
const reading = async (run: () => Promise<any>) => { try { const r = await run(); return { ok: { eligible: r.numerical_eligible } }; } catch (e) { expect(e).toBeInstanceOf(RetainedPrecisionError); return { gate: (e as any).gate, code: (e as any).code }; } };
it('I101: addendum-01 readings', async () => {
  const rows = readFileSync(process.env.ADD1_INPUTS!, 'utf8').split('\n').filter(l => l.trim()).map(l => JSON.parse(l));
  const out: string[] = [];
  for (const d of rows) {
    out.push(JSON.stringify({ name: d.name, base: d.base, bound: await reading(() => validateRetainedPrecision(structuredClone(d.source), structuredClone(d.invocation))),
      unbound: await reading(() => validateRetainedPrecision(structuredClone(d.source))), transport: await reading(() => validateRetainedPrecisionTransport(structuredClone(d.source))) }));
  }
  writeFileSync(process.env.ADD1_OUT!, out.join('\n') + '\n');
  expect(rows.length).toBe(52);
}, 120_000);
