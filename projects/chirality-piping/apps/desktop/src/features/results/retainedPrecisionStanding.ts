/** U6d: TypeScript standing and carriers for the F2a preview successor
 * `openpipestress.result_semantics/0.3.0/preview-physics-retained-1`.
 *
 * Peer of Rust `semantic_contract.rs` (U6a) and Python `compatibility.py`
 * (U6b). The statement itself is checked only by the accepted reader
 * (`retainedPrecision.ts`, read-only here). This module adds:
 *
 * - a private registration: only a completed reader validation, run with the
 *   captured native invocation, is recorded against these exact source bytes
 *   (T1's `loadReferenceSourceEvidence` pattern). A copy, a header, a hash or a
 *   saved record never registers, and any later byte change voids it;
 * - synchronous standing from that registration only (D2 4.9.4; plan 3).
 *   `numerical_quality` never contributes. While the reader's eligibility is
 *   held (until U7) the result is never better than `needs_recompute`;
 * - validated row classes for binding refusals and the per-case summary
 *   (D2 4.9.9). An unregistered or refused statement has no validated class.
 *
 * Nothing here claims the sharper stop-rule bound or truth enclosure by the
 * extrema intervals (RV86 limits); the only bound named is the receipt's
 * published absolute bound b of an `absolute_verified` row.
 */
import { validateRetainedPrecision, type AccuracyClass, type RetainedPrecisionError, type RetainedPrecisionValidation, type RowClassification } from "./retainedPrecision";
import { ordinaryCaseEligible } from "./numericalResultQuality";
import { checkedJsonText } from "../../services/hashService";
import type { MechanicsResult, PreviewModel } from "../../types";

/** No completed reader validation is registered for these exact bytes. */
export const RETAINED_PRECISION_VALIDATION_REQUIRED = "RETAINED_PRECISION_VALIDATION_REQUIRED";
/** The registered validation does not make the successor numerically eligible. */
export const RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE = "RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE";

export type RetainedStandingToken = "numerically_eligible" | "needs_recompute" | "unsupported";
export type RetainedClassificationSummary = {
  case_id: unknown;
  relative_verified: number;
  absolute_verified: number;
  interval_bindable: number;
  not_covered: number;
  input_derived: number;
  non_quantity: number;
  withheld: number;
};
type Json = any; // eslint-disable-line @typescript-eslint/no-explicit-any
type Fingerprint = { text: string; negativeZeros: string };
type Outcome = { validation: RetainedPrecisionValidation; error: null } | { validation: null; error: string };
type Registration = { source: Fingerprint; invocation: unknown; outcome: Outcome };
const registrations = new WeakMap<object, Registration>();

function negativeZeroPaths(value: unknown): string {
  const paths: string[] = [];
  const visit = (item: unknown, path: string) => {
    if (Object.is(item, -0)) paths.push(path);
    else if (item && typeof item === "object") for (const [key, child] of Object.entries(item)) visit(child, `${path}/${key.replaceAll("~", "~0").replaceAll("/", "~1")}`);
  };
  visit(value, "");
  return JSON.stringify(paths);
}
function fingerprint(value: unknown): Fingerprint | null {
  try { return { text: checkedJsonText(value), negativeZeros: negativeZeroPaths(value) }; } catch { return null; }
}
/** Key-order-insensitive JSON equality (serde_json `Value` equality, where an
 * absent member reads as null). */
function sameJson(a: unknown, b: unknown): boolean {
  const order = (v: unknown): unknown => Array.isArray(v) ? v.map(order)
    : v && typeof v === "object" ? Object.fromEntries(Object.keys(v).sort().map(k => [k, order((v as Record<string, unknown>)[k])])) : v;
  return JSON.stringify(order(a ?? null)) === JSON.stringify(order(b ?? null));
}
function receiptCases(source: MechanicsResult): Json[] {
  const cases = (source as Json)?.retained_precision?.body?.cases;
  return Array.isArray(cases) ? cases : [];
}

/** Registration after actual direct IPC or a completed known job only
 * (`previewService.validateCapturedSource`). Runs the accepted reader with the
 * captured invocation and records its outcome, validation or first code,
 * against the exact bytes it validated. A refusal is rethrown after it is
 * recorded, so the caller does not register the native invocation. */
export async function registerRetainedPrecision(source: MechanicsResult, invocation: unknown): Promise<RetainedPrecisionValidation> {
  // Captured before the reader's first await, as the reader snapshots its inputs.
  // Bytes outside the checked JSON profile never register (the reader refuses them).
  const sourcePrint = fingerprint(source), captured = structuredClone(invocation);
  const record = (outcome: Outcome) => { if (sourcePrint) registrations.set(source, { source: sourcePrint, invocation: captured, outcome }); };
  try {
    const validation = await validateRetainedPrecision(source, invocation);
    record({ validation, error: null });
    return validation;
  } catch (error) {
    // The reader throws only RetainedPrecisionError, whose message is its code.
    record({ validation: null, error: (error as RetainedPrecisionError).message });
    throw error;
  }
}
/** The registration of these exact bytes, or null (absent, or bytes changed). */
function registered(source: MechanicsResult | null | undefined): Registration | null {
  const registration = registrations.get(source as object);
  if (!registration) return null;
  const current = fingerprint(source);
  return current && current.text === registration.source.text && current.negativeZeros === registration.source.negativeZeros ? registration : null;
}
/** The registered validation outcome for these exact bytes: a validation, the
 * reader's first code, or null when nothing is registered. Query only. */
export function retainedPrecisionRegistration(source: MechanicsResult | null | undefined): Readonly<Outcome> | null {
  return registered(source)?.outcome ?? null;
}

/** Every case is `selected`, or `not_required` and ordinarily eligible by the
 * base rules, by its receipt index (D2 4.9.4; I66 F-7). Mirrors Rust
 * `not_required_cases_ordinarily_eligible`, including the requirement that every
 * result and diagnostic id is a unique non-empty string. */
function notRequiredCasesOrdinarilyEligible(source: MechanicsResult, cases: Json[]): boolean {
  const quality: Json[] = Array.isArray(source.numerical_quality?.cases) ? source.numerical_quality!.cases : [];
  const ids = new Set<string>();
  for (const items of [source.results, source.diagnostics]) {
    for (const item of Array.isArray(items) ? items : []) {
      const id = (item as Json)?.id;
      if (typeof id !== "string" || !id || ids.has(id)) return false;
      ids.add(id);
    }
  }
  return cases.every((c, index) => {
    if (c?.status === "selected") return true;
    if (c?.status !== "not_required") return false;
    const q = quality[index];
    return !!q && sameJson(q.basis_ref, c.basis_ref) && ordinaryCaseEligible(q, ids);
  });
}
/** D2 4.9.4 over an accepted-reader validation (Rust `retained_standing_from`).
 * `numerically_eligible` needs all of: an invocation-bound validation whose
 * eligibility is set; requested refs equal to the receipt's case order;
 * `MECHANICS_SOLVED`; and every case `selected` or an ordinarily eligible
 * `not_required` case. `numerical_quality` never contributes for a selected case. */
export function retainedStandingFrom(validation: Pick<RetainedPrecisionValidation, "invocation_bound" | "numerical_eligible">, source: MechanicsResult, requested: readonly unknown[]): "numerically_eligible" | "needs_recompute" {
  const cases = receiptCases(source);
  if (!validation.invocation_bound || !validation.numerical_eligible
    || cases.length !== requested.length || cases.some((c, index) => !sameJson(c?.basis_ref, requested[index]))
    || source.status?.mechanics !== "MECHANICS_SOLVED"
    || !notRequiredCasesOrdinarilyEligible(source, cases)) return "needs_recompute";
  return "numerically_eligible";
}
function requestedRefs(model: Pick<PreviewModel, "load_cases"> | null | undefined): Json[] {
  return (model?.load_cases ?? []).map(c => ({ ref_type: "load_case", ref_id: c.id }));
}
/** Synchronous successor standing (plan 3, rule 1-3):
 * - nothing registered for these bytes: `needs_recompute`, VALIDATION_REQUIRED;
 * - the registered reader refused: `unsupported`, with the reader's first code;
 * - otherwise D2 4.9.4 with the model's requested load cases; not eligible gives
 *   `needs_recompute`, NOT_NUMERICALLY_ELIGIBLE. */
export function retainedPrecisionStanding(source: MechanicsResult, model?: Pick<PreviewModel, "load_cases"> | null): { standing: RetainedStandingToken; eligible: boolean; findings: string[] } {
  const registration = registered(source);
  if (!registration) return { standing: "needs_recompute", eligible: false, findings: [RETAINED_PRECISION_VALIDATION_REQUIRED] };
  if (registration.outcome.error !== null) return { standing: "unsupported", eligible: false, findings: [registration.outcome.error] };
  if (retainedStandingFrom(registration.outcome.validation, source, requestedRefs(model)) === "numerically_eligible") return { standing: "numerically_eligible", eligible: true, findings: [] };
  return { standing: "needs_recompute", eligible: false, findings: [RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE] };
}
/** The registered invocation, for the rule-check backend's existing
 * `sourceBlockInvocation` argument; null unless the standing is eligible. */
export function retainedPrecisionInvocation(source: MechanicsResult, model: PreviewModel): unknown {
  if (!retainedPrecisionStanding(source, model).eligible) return null;
  return structuredClone(registered(source)!.invocation);
}
/** Validated G5c classes by result id from the registration; null when nothing
 * valid is registered (no validated class exists for any row). */
export function retainedRowClasses(source: MechanicsResult | null | undefined): ReadonlyMap<string, RowClassification> | null {
  const validation = registered(source)?.outcome.validation;
  return validation ? new Map(validation.classifications.map(row => [row.result_id, row])) : null;
}
const CLASS_INDEX: Record<AccuracyClass, number> = { relative_verified: 0, absolute_verified: 1, not_covered: 2, input_derived: 3, non_quantity: 4 };
/** D2 4.9.9 per-case counts over a validated statement (Rust
 * `classification_summary_from`). `withheld` counts the quantity rows that
 * cannot bind under the standing for `requested`: every quantity row unless the
 * standing is `numerically_eligible`; otherwise the absolute and not-covered
 * rows, since S-I has not landed (`interval_bindable` is 0). */
export function classificationSummaryFrom(validation: RetainedPrecisionValidation, source: MechanicsResult, requested: readonly unknown[]): RetainedClassificationSummary[] {
  const current = retainedStandingFrom(validation, source, requested) === "numerically_eligible";
  return receiptCases(source).map(c => {
    const id = c?.basis_ref?.ref_id;
    const n = [0, 0, 0, 0, 0];
    for (const row of validation.classifications) if (sameJson(row.basis_ref?.ref_id, id)) n[CLASS_INDEX[row.class]] += 1;
    const withheld = current ? n[1] + n[2] : n[0] + n[1] + n[2] + n[3];
    return { case_id: id, relative_verified: n[0], absolute_verified: n[1], interval_bindable: 0, not_covered: n[2], input_derived: n[3], non_quantity: n[4], withheld };
  });
}
/** The per-case summary over the registered validation; empty when nothing
 * valid is registered for these bytes. */
export function classificationSummary(source: MechanicsResult | null | undefined, model?: Pick<PreviewModel, "load_cases"> | null): RetainedClassificationSummary[] {
  const validation = registered(source)?.outcome.validation;
  return validation ? classificationSummaryFrom(validation, source!, requestedRefs(model)) : [];
}
/** Results-panel standing text from the registered receipt only, never from the
 * ordinary `numerical_quality` (D2 4.9.2). Text only; it changes no standing. */
export function retainedPrecisionStandingText(source: MechanicsResult): string {
  const outcome = retainedPrecisionRegistration(source);
  const cases = receiptCases(source);
  const selected = cases.filter(c => c?.status === "selected").length;
  const receipt = !outcome ? "not validated for these exact bytes in this session (saved, reference or copied data never register); needs recompute"
    : outcome.error !== null ? `refused by the retained-precision reader (${outcome.error}); unsupported, historical values only`
    : `validated by the retained-precision reader ${outcome.validation.invocation_bound ? "against the actual invocation" : "without an invocation"} for these exact bytes`;
  return `Retained precision: receipt ${receipt}. Selected cases: ${selected} of ${cases.length}. Current use is checked separately against the actual invocation and the requested cases. Numerical checks do not establish engineering correctness.`;
}
