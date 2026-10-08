// I101 (B1 SC, item "PY and TS check SP's several-notice bytes", T-12): TS's check of I85's F/t12_bytes. Not part of any
// commit: copied into a scratch archive only. For each mode, the W-C2 ordinary envelope (base) and the same envelope with
// case-a's and case-c's RETAINED_PRECISION_UNAVAILABLE notices, plain and with the receipt detail on case-a's only: TS's
// base readers give the same raw and transport contract, the same evidence verdict and standing for the requested cases,
// the same binding refusals and classification summary, and an AnalysisRun record that validates against its envelope.
// The notices are counted. Environment: I101_T12_DIR (the t12_bytes folder), I101_T12_OUT (the JSON result).
import { it, expect } from 'vitest';
import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { sourceContract, sourceContractTransport, sourceSemanticBinding, numericalResultStanding } from './numericalResultQuality';
import { validatePreviewPhysicsEvidence } from './previewPhysicsEvidence';
import { ruleBindingRefusal } from './knownSemanticLimitations';
import { classificationSummary } from './retainedPrecisionStanding';
import { buildAnalysisRunV03, validateAnalysisRunV03, modelLoadBasisRefs } from '../../services/analysisRunCompatibility';

type J = any;
const message = (error: unknown) => (error instanceof Error ? error.message : String(error));

async function read(env: J, model: J, mode: string): Promise<J> {
  const o: J = {};
  o.raw = (() => { try { return [sourceContract(structuredClone(env)), sourceSemanticBinding(structuredClone(env))]; } catch (e) { return `refused: ${message(e)}`; } })();
  try { o.transport = await sourceContractTransport(structuredClone(env)); } catch (e) { o.transport = `refused: ${message(e)}`; }
  try { validatePreviewPhysicsEvidence(structuredClone(env)); o.evidence = 'ok'; } catch (e) { o.evidence = message(e); }
  const standing = numericalResultStanding(structuredClone(env), model);
  o.standing = { contract: standing.contract, status: standing.status, eligible: standing.eligible, findings: standing.findings };
  o.binding = env.results.map((row: J) => ruleBindingRefusal(env, row));
  o.summary = classificationSummary(structuredClone(env), model);
  const manifest = { manifest_ref: { object_type: 'InputManifest', ref: 'manifest:t12' }, manifest_sha256: '1'.repeat(64),
    manifest: { model_basis: { model_ref: env.model_ref, model_payload: model }, solver_basis: { solver_name: env.producer.component_name,
      solver_version: env.producer.component_version, solver_build_ref: 't12-check-not-native-witness', solver_mode: mode } } };
  try {
    const refs = modelLoadBasisRefs(model);
    const record = await buildAnalysisRunV03(structuredClone(env), manifest as J, undefined, refs);
    await validateAnalysisRunV03(record, structuredClone(env), refs);
    o.record = 'validates';
  } catch (e) { o.record = message(e); }
  return o;
}

it('T-12: TS base readers with several notices', async () => {
  const dir = process.env.I101_T12_DIR, out = process.env.I101_T12_OUT; if (!dir || !out) return;
  const bytes = (name: string) => readFileSync(join(dir, name));
  const sha = (b: Buffer) => createHash('sha256').update(b).digest('hex');
  const request = JSON.parse(bytes('w_c2_request.json').toString('utf8'));
  const res: J = { request_sha256: sha(bytes('w_c2_request.json')), modes: {} };
  let ok = true;
  for (const mode of ['sparse_interactive', 'dense_scrutiny']) {
    const names: Record<string, string> = { base: `w_c2_base_${mode}.json`, noticed_plain: `w_c2_noticed_plain_${mode}.json`, noticed_receipt: `w_c2_noticed_receipt_${mode}.json` };
    const docs: J = {}, reads: J = {}, m: J = { sha256: {} };
    for (const [k, name] of Object.entries(names)) { const b = bytes(name); m.sha256[k] = sha(b); docs[k] = JSON.parse(b.toString('utf8')); }
    for (const k of Object.keys(names)) reads[k] = await read(docs[k], request.model, mode);
    const baseIds = new Set(docs.base.diagnostics.map((d: J) => d.id));
    m.reads = Object.fromEntries(Object.entries(reads).map(([k, v]: [string, J]) => [k, { raw: v.raw, transport: v.transport, evidence: v.evidence, standing: v.standing, record: v.record,
      binding_refusals: v.binding.filter((x: unknown) => x !== null).length, summary_sha256: sha(Buffer.from(JSON.stringify(v.summary ?? null))) }]));
    m.notices = Object.fromEntries(Object.keys(names).map(k => [k, docs[k].diagnostics.filter((d: J) => !baseIds.has(d.id) && d.code === 'RETAINED_PRECISION_UNAVAILABLE').map((d: J) => d.id)]));
    const same = (a: J, b: J) => JSON.stringify(a) === JSON.stringify(b);
    m.same_as_base = Object.fromEntries(['noticed_plain', 'noticed_receipt'].map(k => [k, same(reads[k], reads.base)]));
    m.only_notices_added = Object.fromEntries(['noticed_plain', 'noticed_receipt'].map(k => {
      const strip = (d: J) => { const { diagnostics: _, ...rest } = d; return rest; };
      return [k, same(docs[k].diagnostics.filter((d: J) => baseIds.has(d.id)), docs.base.diagnostics) && same(strip(docs[k]), strip(docs.base))];
    }));
    ok = ok && Object.values(m.same_as_base).every(Boolean) && Object.values(m.only_notices_added).every(Boolean)
      && m.notices.noticed_plain.length === 2 && m.notices.noticed_receipt.length === 2 && reads.base.record === 'validates' && Array.isArray(reads.base.raw);
    res.modes[mode] = m;
  }
  res.ok = ok;
  writeFileSync(out, JSON.stringify(res, null, 1) + '\n');
  expect(ok).toBe(true);
}, 600_000);
