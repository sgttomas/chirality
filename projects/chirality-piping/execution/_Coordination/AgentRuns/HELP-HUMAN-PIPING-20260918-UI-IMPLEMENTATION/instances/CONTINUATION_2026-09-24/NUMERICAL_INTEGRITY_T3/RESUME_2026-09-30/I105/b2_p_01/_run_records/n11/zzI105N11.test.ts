// I105 (B3b-P, N-11): physics-1's TS base readers on each exact fallback envelope (scratch only).
import { describe, expect, it } from 'vitest';
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { sourceContract, numericalResultStanding } from './numericalResultQuality';
import { validatePhysicsEvidence } from './physicsResultEvidence';

const dir = join(__dirname, '__i105_n11__');
const tags = readdirSync(dir).filter(f => f.endsWith('_base.json')).map(f => f.slice(0, -'_base.json'.length)).sort();
const read = (name: string) => JSON.parse(readFileSync(join(dir, name), 'utf8'));

describe('I105 N-11: physics-1 base readers accept the noticed exact fallback', () => {
  it('has the written envelopes', () => { expect(tags.length).toBe(8); });
  for (const tag of tags) {
    it(tag, () => {
      const base = read(`${tag}_base.json`), noticed = read(`${tag}_noticed.json`), invocation = read(`${tag}_invocation.json`);
      const model = invocation.request.model;
      expect(sourceContract(base)).toBe('physics');
      expect(sourceContract(noticed)).toBe('physics');
      expect(() => validatePhysicsEvidence(base, model)).not.toThrow();
      expect(() => validatePhysicsEvidence(noticed, model)).not.toThrow();
      const standing = numericalResultStanding(noticed, model);
      expect(standing).toEqual(numericalResultStanding(base, model));
      expect(noticed.diagnostics.filter((d: { code: string }) => d.code === 'RETAINED_PRECISION_UNAVAILABLE').length).toBe(1);
      console.log(`N11_TS ${tag} contract=${sourceContract(noticed)} status=${standing.status} findings=${standing.findings.join('|')}`);
      // Negative control: the same reader refuses a non-empty connector.
      const bad = JSON.parse(JSON.stringify(noticed));
      bad.contract_evidence.connector = [{}];
      expect(() => validatePhysicsEvidence(bad, model)).toThrow();
    });
  }
});
