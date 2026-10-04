/** U6d: TypeScript carriers and standing for the F2a preview successor
 * (plan 1d and 3; D2 4.7, 4.9.4 and 4.9.9).
 *
 * Inputs are PP's pinned milestone successor bytes (D-U6-5; checked by sha256)
 * with their invocation, delivered through mocked direct and job IPC. This is a
 * unit transport replay, NOT a native witness: Tauri never delivers a successor
 * in the milestone domain (plan F-1; D-U6-3 qualification limit).
 *
 * The reader's eligibility stays held until U7, so every real standing here is
 * at best `needs_recompute`. The post-U7 rules are exercised two ways without
 * touching the flag: the pure seams (`retainedStandingFrom`,
 * `classificationSummaryFrom`) and a test-only wrapper of the accepted reader
 * (`u7.simulate`) that sets `numerical_eligible` on an invocation-bound
 * validation, and optionally marks one row `not_covered` (no available
 * statement has one; U6a F3) or reclassifies the absolute rows, to reach the
 * summary branches. With `u7.simulate` false the wrapper returns the reader's own
 * frozen result unchanged.
 */
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { cleanup, render, screen } from "@testing-library/react";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
const invokeMock = vi.hoisted(() => vi.fn());
vi.mock("@tauri-apps/api/core", () => ({ invoke: invokeMock }));
const u7 = vi.hoisted(() => ({ simulate: false, notCovered: null as string | null, noAbsolute: false }));
vi.mock("./retainedPrecision", async (importOriginal) => {
  const actual = await importOriginal<typeof import("./retainedPrecision")>();
  return {
    ...actual,
    validateRetainedPrecision: async (source: unknown, invocation?: unknown) => {
      const validation = await actual.validateRetainedPrecision(source, invocation);
      if (!u7.simulate || !validation.invocation_bound) return validation;
      return Object.freeze({
        ...validation, numerical_eligible: true, standing: "eligible" as const,
        classifications: validation.classifications.map(row => row.result_id === u7.notCovered ? { ...row, class: "not_covered" as const, scale_bits: null, bound_bits: null }
          : u7.noAbsolute && row.class === "absolute_verified" ? { ...row, class: "relative_verified" as const, bound_bits: null } : row),
      });
    },
  };
});
import type { LocalProjectEnvelope, MechanicsResult, PreviewModel } from "../../types";
// Import order matters for the wrapper above: the carriers load first, so their
// import of the reader resolves to the wrapped module, not through the cycle.
import {
  PREVIEW_PHYSICS_CONTRACT_ID, PREVIEW_PHYSICS_RETAINED_CONTRACT_ID, PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256, PREVIEW_PHYSICS_RETAINED_PROFILE,
  RETAINED_PRECISION_DOWNGRADE_FORBIDDEN, currentSemanticContract, hasCurrentSourceContract, numericalResultStanding,
  ordinaryCaseEligible, retainedPrecisionDowngrade, sourceContract, sourceSemanticBinding,
} from "./numericalResultQuality";
import {
  RETAINED_METHOD, RETAINED_PRECISION_ID, RETAINED_PRECISION_PROFILE, decodeBinary64, validateRetainedPrecision,
  type RetainedPrecisionValidation,
} from "./retainedPrecision";
import {
  RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE, RETAINED_PRECISION_VALIDATION_REQUIRED, classificationSummary, classificationSummaryFrom,
  registerRetainedPrecision, retainedPrecisionInvocation, retainedPrecisionRegistration, retainedPrecisionStanding, retainedPrecisionStandingText, retainedRowClasses, retainedStandingFrom,
} from "./retainedPrecisionStanding";
import {
  FRESH_SEMANTIC_CONTRACT_IDS, N_HEADLINE, N_RP_ABSOLUTE, N_RP_NOT_COVERED, N_RP_UNVALIDATED, N_SB, RULE_QUANTITY_BELOW_VERIFIED_FLOOR, RULE_QUANTITY_NOT_COVERED,
  classBindingRefusal, isFreshSemanticResult, knownSemanticNotices, resultRowLabel, retainedAbsoluteNotice, ruleBindingRefusal, standingReason, upwardBoundText,
} from "./knownSemanticLimitations";
import { semanticContractForSource, previewPhysicsSemanticContract } from "./resultSemantics";
import { ResultsPanel } from "./ResultsPanel";
import { buildHistoricalRunContext } from "./HistoricalRunContext";
import { hasNativeMechanicsInvocation, pollPreviewMechanicsJob, runPreviewMechanics, startPreviewMechanicsJob, type PreviewSolverMode } from "../../services/previewService";
import { ruleBindingPrecheck, runRuleChecks, type RuleCheckBindingPlan } from "../../services/ruleCheckService";
import { ANALYSIS_RETAINED_PRECISION_RECEIPT_MISMATCH, buildAnalysisRunV03, modelLoadBasisRefs } from "../../services/analysisRunCompatibility";
import { computeModelHash, computeProjectEnvelopeHash } from "../../services/hashService";
import type { RulePackDocument } from "../../services/rulePackService";

type Json = any; // eslint-disable-line @typescript-eslint/no-explicit-any
const root = resolve(__dirname, "../../../../../");
const caseFile = JSON.parse(readFileSync(resolve(root, "fixtures/results/retained_precision_carrier_cases.json"), "utf8"));
const MODES = ["sparse_interactive", "dense_scrutiny"] as const;
const sha256 = (bytes: Buffer | string) => createHash("sha256").update(bytes).digest("hex");
/** The pinned successor and its invocation, checked by sha256 (D-U6-5). */
function milestone(mode: PreviewSolverMode) {
  const entry = caseFile.fixtures[`milestone_${mode}`];
  const bytes = readFileSync(resolve(root, entry.path));
  expect(sha256(bytes)).toBe(entry.sha256);
  const doc = JSON.parse(bytes.toString("utf8"));
  return { source: doc.source as MechanicsResult, invocation: doc.invocation as Json, model: doc.invocation.request.model as PreviewModel };
}
const OTHER: Record<PreviewSolverMode, PreviewSolverMode> = { sparse_interactive: "dense_scrutiny", dense_scrutiny: "sparse_interactive" };
let jobSequence = 0;
/** Mocked direct IPC: the native command returns these bytes for this mode. */
async function deliverDirect(source: MechanicsResult, model: PreviewModel | null, mode: PreviewSolverMode): Promise<MechanicsResult> {
  (window as Json).__TAURI_INTERNALS__ = {};
  invokeMock.mockImplementation(async (command: string, args: Json) => {
    expect(command).toBe("run_preview_mechanics_with_solver_mode");
    expect(args.solverMode).toBe(mode);
    return structuredClone(source);
  });
  return runPreviewMechanics(model, mode);
}
/** Mocked job IPC: start, then one completed poll delivering these bytes. */
async function deliverJob(source: MechanicsResult, model: PreviewModel, mode: PreviewSolverMode): Promise<MechanicsResult> {
  (window as Json).__TAURI_INTERNALS__ = {};
  const jobId = `unit-transport-replay:retained:${++jobSequence}`;
  invokeMock.mockImplementation(async (command: string, args: Json) => {
    if (command === "start_preview_mechanics_job_with_solver_mode") {
      expect(args.solverMode).toBe(mode);
      return { job_id: jobId, backend_cancellation_token: `${jobId}:token`, state: "queued", cancellation_scope: "unit_transport_replay_not_native_ui_qualification" };
    }
    expect(command).toBe("poll_preview_mechanics_job");
    expect(args.jobId).toBe(jobId);
    return { job_id: jobId, state: "completed", cancellation_requested: false, cancellation_status: "not_requested", cancellation_scope: "unit_transport_replay_not_native_ui_qualification", result: structuredClone(source), error_message: null };
  });
  await startPreviewMechanicsJob(model, mode);
  return (await pollPreviewMechanicsJob(jobId)).result!;
}
function setPath(target: Json, path: (string | number)[], value: unknown) {
  let at = target;
  for (const key of path.slice(0, -1)) at = at[key];
  at[path[path.length - 1]] = value;
}
const caseIds = (model: PreviewModel) => model.load_cases.map(c => c.id);
const withLoadCases = (model: PreviewModel, ids: string[]) => ({ ...model, load_cases: ids.map(id => ({ ...model.load_cases[0], id })) }) as PreviewModel;

beforeEach(() => { u7.simulate = false; u7.notCovered = null; u7.noAbsolute = false; });
afterEach(() => {
  cleanup();
  invokeMock.mockReset();
  delete (window as Json).__TAURI_INTERNALS__;
  u7.simulate = false; u7.notCovered = null; u7.noAbsolute = false;
});

describe("the inputs and the pinned identity", () => {
  it("uses PP's byte-identical successors and the shared 14-case file", () => {
    expect(caseFile.format).toBe("I66-U6-CARRIER-CASES-v1");
    expect(caseFile.cases).toHaveLength(14);
    for (const mode of MODES) expect(milestone(mode).source.producer!.semantic_contract_id).toBe(RETAINED_PRECISION_ID);
  });
  it("dispatch constants equal the accepted reader's and the pinned table, whose rows are preview-physics-1's", () => {
    expect(PREVIEW_PHYSICS_RETAINED_CONTRACT_ID).toBe(RETAINED_PRECISION_ID);
    expect(PREVIEW_PHYSICS_RETAINED_PROFILE).toBe(RETAINED_PRECISION_PROFILE);
    const bytes = readFileSync(resolve(root, "fixtures/results/semantic_contract_v0_3_preview_physics_retained_1.json"));
    expect(sha256(bytes)).toBe(PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256);
    const { source } = milestone("sparse_interactive");
    const table = semanticContractForSource(source) as Json;
    expect(table.semantic_contract_id).toBe(RETAINED_PRECISION_ID);
    expect(table.rows).toStrictEqual(previewPhysicsSemanticContract.rows);
    expect(sourceSemanticBinding(source)).toStrictEqual({ id: RETAINED_PRECISION_ID, sha256: PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256 });
    expect(FRESH_SEMANTIC_CONTRACT_IDS).toContain(RETAINED_PRECISION_ID);
  });
});

describe.each(MODES)("%s: registration through mocked IPC", (mode) => {
  it.each([["direct", deliverDirect], ["job", deliverJob]] as const)("%s IPC registers only after the accepted reader passes with the captured invocation", async (_route, deliver) => {
    const { source, invocation, model } = milestone(mode);
    const received = await deliver(source, model, mode);
    expect(received).toStrictEqual(source);
    expect(sourceContract(received)).toBe("retained_preview_physics");
    expect(hasNativeMechanicsInvocation(received, model, mode)).toBe(true);
    const outcome = retainedPrecisionRegistration(received)!;
    expect(outcome.error).toBeNull();
    expect(outcome.validation!.invocation_bound).toBe(true);
    expect(outcome.validation!.numerical_eligible).toBe(false);
    expect(outcome.validation!.classifications).toHaveLength(source.results.length);
    // Synchronous standing reads only the registration: held eligibility gives needs_recompute.
    expect(numericalResultStanding(received, model)).toStrictEqual({ contract: "retained_preview_physics", status: "needs_recompute", eligible: false, findings: [RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE] });
    expect(retainedPrecisionStanding(received, model).standing).toBe("needs_recompute");
    expect(retainedPrecisionInvocation(received, model)).toBeNull();
    // Fresh by membership (D-U6-6), never by standing.
    expect(isFreshSemanticResult(received)).toBe(true);
    expect(currentSemanticContract(received)).toStrictEqual({ id: RETAINED_PRECISION_ID, sha256: PREVIEW_PHYSICS_RETAINED_CONTRACT_SHA256 });
    expect(standingReason(received)).toBeNull();
    // The registration binds the actual invocation, which the reader's G8 checked.
    expect((await validateRetainedPrecision(received, invocation)).invocation_bound).toBe(true);
  });

  it("copies, saved bytes, headers and a model-less solve never register", async () => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    for (const copy of [structuredClone(received), JSON.parse(JSON.stringify(received)) as MechanicsResult, source]) {
      expect(retainedPrecisionRegistration(copy)).toBeNull();
      expect(numericalResultStanding(copy, model)).toStrictEqual({ contract: "retained_preview_physics", status: "needs_recompute", eligible: false, findings: [RETAINED_PRECISION_VALIDATION_REQUIRED] });
      expect(hasNativeMechanicsInvocation(copy, model, mode)).toBe(false);
    }
    // No model, no captured invocation: delivered bytes are kept but nothing registers.
    const uncaptured = await deliverDirect(source, null, mode);
    expect(retainedPrecisionRegistration(uncaptured)).toBeNull();
    expect(numericalResultStanding(uncaptured, model).findings).toStrictEqual([RETAINED_PRECISION_VALIDATION_REQUIRED]);
    // Browser preview (no Tauri runtime) refuses before any delivery.
    delete (window as Json).__TAURI_INTERNALS__;
    await expect(runPreviewMechanics(model, mode)).rejects.toThrow();
  });

  it("a later edit of the received bytes voids the registration, including a sign of zero", async () => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    const original = received.results[3].value;
    received.results[3].value = original + 1;
    expect(retainedPrecisionRegistration(received)).toBeNull();
    expect(numericalResultStanding(received, model).findings).toStrictEqual([RETAINED_PRECISION_VALIDATION_REQUIRED]);
    expect(hasNativeMechanicsInvocation(received, model, mode)).toBe(false);
    expect(ruleBindingRefusal(received, received.results[3])).toBe(RULE_QUANTITY_NOT_COVERED);
    received.results[3].value = original;
    expect(retainedPrecisionRegistration(received)!.error).toBeNull();
    const zero = received.results.findIndex(row => Object.is(row.value, 0));
    expect(zero).toBeGreaterThanOrEqual(0);
    received.results[zero].value = -0;
    expect(retainedPrecisionRegistration(received)).toBeNull();
    // Bytes outside the checked profile void it, and so does a receipt edit.
    received.results[zero].value = NaN;
    expect(retainedPrecisionRegistration(received)).toBeNull();
    received.results[zero].value = 0;
    (received.retained_precision as Json).receipt_sha256 = "0".repeat(64);
    expect(retainedPrecisionRegistration(received)).toBeNull();
  });

  it("bytes outside the checked profile never register, even when registration is called directly", async () => {
    const { source, invocation } = milestone(mode);
    const unchecked = structuredClone(source); unchecked.results[3].value = NaN;
    await expect(registerRetainedPrecision(unchecked, invocation)).rejects.toThrow("RETAINED_PRECISION_RECEIPT_MISMATCH");
    expect(retainedPrecisionRegistration(unchecked)).toBeNull();
    unchecked.results[3].value = source.results[3].value;
    expect(retainedPrecisionRegistration(unchecked)).toBeNull();
  });

  it("bytes outside the checked profile never register, even after a later repair", async () => {
    const { source, model } = milestone(mode);
    const unchecked = structuredClone(source); unchecked.results[3].value = NaN;
    const received = await deliverDirect(unchecked, model, mode);
    expect(retainedPrecisionRegistration(received)).toBeNull();
    received.results[3].value = source.results[3].value;
    expect(retainedPrecisionRegistration(received)).toBeNull();
    expect(numericalResultStanding(received, model).findings).toStrictEqual([RETAINED_PRECISION_VALIDATION_REQUIRED]);
    expect(hasNativeMechanicsInvocation(received, model, mode)).toBe(false);
  });

  it.each([
    ["an edited covered row", (s: Json) => { s.results[0].value = 12345; }, "RETAINED_PRECISION_RECEIPT_MISMATCH"],
    ["a hash-consistent-looking quality claim of checks_passed", (s: Json) => { s.numerical_quality.status = "checks_passed"; s.numerical_quality.cases[0].solve_quality = "checks_passed"; }, "RETAINED_PRECISION_RECEIPT_MISMATCH"],
    ["an altered receipt", (s: Json) => { s.retained_precision.body.receipt_version = 1; s.retained_precision.receipt_sha256 = "f".repeat(64); }, "RETAINED_PRECISION_RECEIPT_MISMATCH"],
  ] as const)("a delivery with %s records the reader's first code: unsupported, never registered natively", async (_label, edit, code) => {
    const { source, model } = milestone(mode);
    const edited = structuredClone(source); edit(edited);
    const received = await deliverDirect(edited, model, mode);
    expect(retainedPrecisionRegistration(received)).toStrictEqual({ validation: null, error: code });
    expect(retainedPrecisionStanding(received, model)).toStrictEqual({ standing: "unsupported", eligible: false, findings: [code] });
    expect(numericalResultStanding(received, model)).toStrictEqual({ contract: "retained_preview_physics", status: "needs_recompute", eligible: false, findings: [code] });
    expect(hasNativeMechanicsInvocation(received, model, mode)).toBe(false);
    expect(retainedRowClasses(received)).toBeNull();
  });

  it("numerical_quality never contributes, even with the post-U7 reader and a fully passing ordinary claim", async () => {
    u7.simulate = true;
    const { source, model } = milestone(mode);
    const claimed = structuredClone(source) as Json;
    claimed.numerical_quality.status = "checks_passed";
    claimed.numerical_quality.cases[0].solve_quality = "checks_passed";
    // The generic branch would accept this ordinary claim; the successor branch refuses it at G1.
    expect(claimed.numerical_quality.cases.every((c: Json) => ordinaryCaseEligible(c, new Set([...claimed.results, ...claimed.diagnostics].map((x: Json) => x.id))))).toBe(true);
    const received = await deliverDirect(claimed, model, mode);
    expect(numericalResultStanding(received, model)).toStrictEqual({ contract: "retained_preview_physics", status: "needs_recompute", eligible: false, findings: ["RETAINED_PRECISION_RECEIPT_MISMATCH"] });
  });

  it("a registration without an invocation is never eligible, even with the post-U7 reader, and says so", async () => {
    u7.simulate = true;
    const { source, model } = milestone(mode);
    const own = structuredClone(source);
    const validation = await registerRetainedPrecision(own, undefined);
    expect(validation.invocation_bound).toBe(false);
    expect(retainedPrecisionStanding(own, model)).toStrictEqual({ standing: "needs_recompute", eligible: false, findings: [RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE] });
    expect(retainedPrecisionStandingText(own)).toContain("validated by the retained-precision reader without an invocation");
    expect(retainedPrecisionInvocation(own, model)).toBeNull();
  });

  it("a foreign solver mode is refused at the reader's invocation binding", async () => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, OTHER[mode]);
    expect(retainedPrecisionRegistration(received)).toStrictEqual({ validation: null, error: "RETAINED_PRECISION_INVOCATION_MISMATCH" });
    expect(retainedPrecisionStanding(received, model).standing).toBe("unsupported");
    expect(hasNativeMechanicsInvocation(received, model)).toBe(false);
  });
});

describe("the post-U7 standing rules (seams; the reader's flag is untouched)", () => {
  const { source } = milestone("sparse_interactive");
  const requested = [{ ref_type: "load_case", ref_id: "case" }];
  const bound = { invocation_bound: true, numerical_eligible: true };
  /** A two-case statement: the milestone's selected case plus a not_required one. */
  function twoCase(edit?: (s: Json) => void): MechanicsResult {
    const s = structuredClone(source) as Json;
    s.retained_precision.body.cases.push({ basis_ref: { ref_type: "load_case", ref_id: "second" }, status: "not_required" });
    s.numerical_quality.cases.push({ basis_ref: { ref_type: "load_case", ref_id: "second" }, structural_status: "passive_model_basis", solve_quality: "checks_passed", model_matrix_fidelity: "represented_equations_retained", accuracy_evidence: "not_claimed", evidence_refs: [s.diagnostics[0].id] });
    edit?.(s);
    return s;
  }
  const two = [...requested, { ref_type: "load_case", ref_id: "second" }];
  it("is numerically_eligible only with every conjunct", () => {
    expect(retainedStandingFrom(bound, source, requested)).toBe("numerically_eligible");
    expect(retainedStandingFrom({ ...bound, invocation_bound: false }, source, requested)).toBe("needs_recompute");
    expect(retainedStandingFrom({ ...bound, numerical_eligible: false }, source, requested)).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, source, [])).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, source, [{ ref_type: "load_case", ref_id: "other" }])).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, source, [...requested, ...requested])).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, { ...source, status: { ...source.status, mechanics: "MODEL_INCOMPLETE" } }, requested)).toBe("needs_recompute");
    // Key order is not significant (serde_json Value equality).
    expect(retainedStandingFrom(bound, source, [{ ref_id: "case", ref_type: "load_case" }])).toBe("numerically_eligible");
  });
  it("applies the base ordinary-eligibility predicate to not_required cases (F-7) and refuses other statuses", () => {
    expect(retainedStandingFrom(bound, twoCase(), two)).toBe("numerically_eligible");
    expect(retainedStandingFrom(bound, twoCase(), [two[1], two[0]])).toBe("needs_recompute");
    for (const [field, value] of [["solve_quality", "sensitive"], ["structural_status", "numerically_unresolved"], ["model_matrix_fidelity", "assembly_uncertainty"], ["accuracy_evidence", "unresolved"], ["evidence_refs", []], ["evidence_refs", ["missing"]], ["evidence_refs", [source.diagnostics[0].id!, "missing"]], ["basis_ref", { ref_type: "load_case", ref_id: "elsewhere" }]] as const) {
      expect(retainedStandingFrom(bound, twoCase(s => { s.numerical_quality.cases[1][field] = value; }), two), field).toBe("needs_recompute");
    }
    expect(retainedStandingFrom(bound, twoCase(s => { s.numerical_quality.cases.pop(); }), two)).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, twoCase(s => { s.retained_precision.body.cases[1].status = "unavailable"; }), two)).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, twoCase(s => { s.diagnostics.push(structuredClone(s.diagnostics[0])); }), two)).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, twoCase(s => { delete s.diagnostics[1].id; }), two)).toBe("needs_recompute");
    expect(retainedStandingFrom(bound, twoCase(s => { s.results[1].id = ""; }), two)).toBe("needs_recompute");
  });
  it("counts withheld rows by standing (Rust classification_summary_from)", async () => {
    const validation = await validateRetainedPrecision(source);
    const notCurrent = classificationSummaryFrom(validation, source, requested);
    expect(notCurrent).toStrictEqual([{ case_id: "case", relative_verified: 25, absolute_verified: 69, interval_bindable: 0, not_covered: 0, input_derived: 3, non_quantity: 1, withheld: 97 }]);
    const current = classificationSummaryFrom({ ...validation, invocation_bound: true, numerical_eligible: true }, source, requested);
    expect(current[0].withheld).toBe(69);
    const uncovered: RetainedPrecisionValidation = { ...validation, invocation_bound: true, numerical_eligible: true, classifications: validation.classifications.map((row, i) => i === 1 ? { ...row, class: "not_covered" } : row) };
    expect(classificationSummaryFrom(uncovered, source, requested)[0]).toMatchObject({ not_covered: 1, withheld: 69 + 1 - (validation.classifications[1].class === "absolute_verified" ? 1 : 0) });
    // Rows count only toward their own case.
    const split: RetainedPrecisionValidation = { ...validation, classifications: validation.classifications.map((row, i) => i < 10 ? { ...row, basis_ref: { ref_type: "load_case", ref_id: "second" } } : row) };
    const counts = classificationSummaryFrom(split, twoCase(), two).map(c => [c.case_id, c.relative_verified + c.absolute_verified + c.not_covered + c.input_derived + c.non_quantity]);
    expect(counts).toStrictEqual([["case", validation.classifications.length - 10], ["second", 10]]);
  });
});

describe.each(MODES)("%s: the simulated post-U7 path through the real carriers", (mode) => {
  it("standing becomes eligible only for the requested cases, and the rule-check gate passes the registered invocation", async () => {
    u7.simulate = true;
    const { source, invocation, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    expect(numericalResultStanding(received, model)).toStrictEqual({ contract: "retained_preview_physics", status: "integrity_checked", eligible: true, findings: [] });
    expect(numericalResultStanding(received, withLoadCases(model, ["other"])).findings).toStrictEqual([RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE]);
    expect(numericalResultStanding(received, null).eligible).toBe(false);
    expect(retainedPrecisionInvocation(received, model)).toStrictEqual(invocation);
    expect(classificationSummary(received, model)[0].withheld).toBe(69);
    expect(classificationSummary(received, null)[0].withheld).toBe(97);
    invokeMock.mockReset();
    invokeMock.mockImplementation(async (command: string, args: Json) => {
      expect(command).toBe("run_rule_checks");
      expect(args.sourceBlockInvocation).toStrictEqual(invocation);
      expect(args.solvedEnvelope).toBe(received);
      return { document_kind: "rule_check_run", rule_pack_id: "invented", grammar_version: "1.0.0", aggregate_status: "RULE_INPUTS_INCOMPLETE", checks: [], professional_boundary_notice: "unit simulation" };
    });
    const route = await runRuleChecks({ rulePackDocument: {} as RulePackDocument, model, solvedEnvelope: received });
    expect(route.route).toBe("tauri_backend");
    expect(invokeMock).toHaveBeenCalledTimes(1);
    // Saved or copied bytes still never register, even with the post-U7 reader.
    expect(numericalResultStanding(structuredClone(received), model).findings).toStrictEqual([RETAINED_PRECISION_VALIDATION_REQUIRED]);
  });
  it("a not_covered row is labelled, refused and counted (fabricated class; no statement has one)", async () => {
    u7.simulate = true;
    const { source, model } = milestone(mode);
    const target = source.results.find(row => row.kind === "global_nodal_rotation_x")!;
    u7.notCovered = target.id;
    const received = await deliverDirect(source, model, mode);
    expect(ruleBindingRefusal(received, target)).toBe(RULE_QUANTITY_NOT_COVERED);
    expect(resultRowLabel(target, received)).toBe(N_RP_NOT_COVERED);
    expect(knownSemanticNotices(received).map(n => n.id)).toContain("retained-precision-not-covered:case");
    expect(ruleBindingPrecheck(received, { solverInputs: [{ input_id: "x", name: "x", dimension: "angle", unit_ref: "rad", solver_result_ref: { result_id: target.id } }], valueInputs: [], valueSlots: [], libraryInputs: [] })).toStrictEqual([{ input_id: "x", result_id: target.id, reason: RULE_QUANTITY_NOT_COVERED, notice: N_RP_NOT_COVERED }]);
    expect(classificationSummary(received, model)[0].not_covered).toBe(1);
  });
  it("without absolute rows there is no absolute summary notice", async () => {
    u7.simulate = true; u7.noAbsolute = true;
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    expect(classificationSummary(received, model)[0]).toMatchObject({ absolute_verified: 0, not_covered: 0 });
    expect(knownSemanticNotices(received).map(n => n.id)).toStrictEqual(["headline-label"]);
    expect(ruleBindingRefusal(received, received.results[3])).toBeNull();
  });
});

describe.each(MODES)("%s: the rule-check gate and binding refusals (eligibility held)", (mode) => {
  const pack = {} as RulePackDocument;
  it("refuses a registered successor before any rule backend call, and unregistered bytes as not native", async () => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    invokeMock.mockReset();
    await expect(runRuleChecks({ rulePackDocument: pack, model, solvedEnvelope: received })).rejects.toThrow(`${RETAINED_PRECISION_NOT_NUMERICALLY_ELIGIBLE}: the retained-precision result is not numerically eligible for rule checks.`);
    await expect(runRuleChecks({ rulePackDocument: pack, model, solvedEnvelope: structuredClone(received) })).rejects.toThrow("RULE_NATIVE_INVOCATION_REQUIRED");
    const edited = structuredClone(source); edited.results[0].value = 12345;
    const refused = await deliverDirect(edited, model, mode);
    invokeMock.mockReset();
    await expect(runRuleChecks({ rulePackDocument: pack, model, solvedEnvelope: refused })).rejects.toThrow("RULE_NATIVE_INVOCATION_REQUIRED");
    expect(invokeMock).not.toHaveBeenCalled();
  });
  it("binds rows by validated class; a headline is refused as the row it names; unregistered rows are all refused", async () => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    const classes = retainedRowClasses(received)!;
    const byClass = (cls: string) => received.results.filter(row => classes.get(row.id)!.class === cls);
    expect(byClass("absolute_verified")).toHaveLength(69);
    for (const row of byClass("absolute_verified")) expect(ruleBindingRefusal(received, row)).toBe(RULE_QUANTITY_BELOW_VERIFIED_FLOOR);
    for (const cls of ["relative_verified", "input_derived", "non_quantity"]) {
      expect(byClass(cls).length).toBeGreaterThan(0);
      for (const row of byClass(cls)) expect(ruleBindingRefusal(received, row), cls).toBeNull();
    }
    expect(ruleBindingRefusal(received, { id: "result:absent", kind: "x" })).toBeNull();
    const headline = received.summary.max_open_formula_stress!.result_ref;
    expect(classes.get(headline)!.class).toBe("absolute_verified");
    const plan: RuleCheckBindingPlan = { solverInputs: [{ input_id: "headline", name: "h", dimension: "stress", unit_ref: "Pa", solver_result_ref: { result_id: headline } }, { input_id: "relative", name: "r", dimension: "force", unit_ref: "N" }], valueInputs: [], valueSlots: [], libraryInputs: [] };
    const relative = byClass("relative_verified")[0];
    const findings = ruleBindingPrecheck(received, plan, [{ input_id: "relative", result_id: relative.id }]);
    const label = retainedAbsoluteNotice(classes.get(headline)!.bound_bits!, "Pa");
    expect(findings).toStrictEqual([{ input_id: "headline", result_id: headline, reason: RULE_QUANTITY_BELOW_VERIFIED_FLOOR, notice: label }]);
    expect(label).not.toBe(N_SB);
    const copy = structuredClone(received);
    expect(ruleBindingRefusal(copy, relative)).toBe(RULE_QUANTITY_NOT_COVERED);
    expect(ruleBindingPrecheck(copy, plan, [{ input_id: "relative", result_id: relative.id }]).map(f => [f.reason, f.notice])).toStrictEqual([[RULE_QUANTITY_NOT_COVERED, N_RP_UNVALIDATED], [RULE_QUANTITY_NOT_COVERED, N_RP_UNVALIDATED]]);
    expect(classBindingRefusal("not_covered")).toBe(RULE_QUANTITY_NOT_COVERED);
    expect(classBindingRefusal("absolute_verified")).toBe(RULE_QUANTITY_BELOW_VERIFIED_FLOOR);
    expect(classBindingRefusal(undefined)).toBeNull();
  });
  it("summarizes classes per case over the registration only", async () => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    expect(classificationSummary(received, model)).toStrictEqual([{ case_id: "case", relative_verified: 25, absolute_verified: 69, interval_bindable: 0, not_covered: 0, input_derived: 3, non_quantity: mode === "sparse_interactive" ? 1 : 2, withheld: 97 }]);
    expect(classificationSummary(structuredClone(received), model)).toStrictEqual([]);
    expect(classificationSummary(null)).toStrictEqual([]);
  });
});

describe("the downgrade guard (F-5)", () => {
  const { source } = milestone("sparse_interactive");
  const relabel = (s: Json) => { s.producer.semantic_contract_id = PREVIEW_PHYSICS_CONTRACT_ID; s.formulation_basis.profile_id = "product_preview_mechanics_v1"; return s; };
  it.each([
    ["the receipt and the token rows", (s: Json) => relabel(s)],
    ["the token rows only", (s: Json) => { delete relabel(s).retained_precision; }],
    ["a null receipt member only", (s: Json) => { relabel(s).retained_precision = null; for (const row of s.results) delete row.recovery_method; }],
    ["one token row only", (s: Json) => { delete relabel(s).retained_precision; for (const row of s.results.slice(1)) delete row.recovery_method; }],
  ] as const)("a successor relabelled as preview-physics-1 keeping %s is unsupported", (_label, edit) => {
    const s = structuredClone(source) as Json; edit(s);
    expect(retainedPrecisionDowngrade(s)).toBe(true);
    expect(sourceContract(s)).toBe("unsupported");
    expect(numericalResultStanding(s, null)).toStrictEqual({ contract: "unsupported", status: "needs_recompute", eligible: false, findings: [RETAINED_PRECISION_DOWNGRADE_FORBIDDEN] });
    expect(hasCurrentSourceContract(s)).toBe(false);
    expect(isFreshSemanticResult(s)).toBe(false);
    expect(ruleBindingRefusal(s, s.results[0])).toBeNull();
  });
  it("with neither the receipt nor a token row it is the base identity again, and the guard ignores other method strings", () => {
    const s = relabel(structuredClone(source));
    delete s.retained_precision;
    for (const row of s.results) delete row.recovery_method;
    expect(retainedPrecisionDowngrade(s)).toBe(false);
    expect(sourceContract(s)).toBe("preview_physics");
    s.results[0].recovery_method = "some_other_method";
    expect(retainedPrecisionDowngrade(s)).toBe(false);
  });
  it("applies to every other identity, including legacy 0.1.0 and an unparseable header", () => {
    const legacy = JSON.parse(readFileSync(resolve(root, "fixtures/product_preview/invented_mechanics_result.json"), "utf8"));
    expect(sourceContract(legacy)).toBe("legacy");
    expect(sourceContract({ ...legacy, retained_precision: {} })).toBe("unsupported");
    expect(numericalResultStanding({ ...legacy, retained_precision: {} }, null).findings).toStrictEqual([RETAINED_PRECISION_DOWNGRADE_FORBIDDEN]);
    const preview = JSON.parse(readFileSync(resolve(root, "fixtures/results/preview_physics_connected_sparse.json"), "utf8"));
    expect(sourceContract(preview)).toBe("preview_physics");
    expect(sourceContract({ ...preview, retained_precision: structuredClone(source.retained_precision) })).toBe("unsupported");
    expect(sourceContract({ ...preview, results: preview.results.map((row: Json, i: number) => i ? row : { ...row, recovery_method: RETAINED_METHOD }) })).toBe("unsupported");
    expect(retainedPrecisionDowngrade({ ...legacy, results: [null, 3] })).toBe(false);
    expect(retainedPrecisionDowngrade({ ...legacy, results: "rows" })).toBe(false);
    expect(numericalResultStanding({ ...legacy, producer: { semantic_contract_id: "unknown" } } as MechanicsResult, null).findings).toStrictEqual(["SOURCE_NUMERICAL_CONTRACT_UNSUPPORTED"]);
  });
  it("the successor's own header requires its profile, its contract evidence and a receipt object, and no other receipt", () => {
    expect(sourceContract(source)).toBe("retained_preview_physics");
    for (const edit of [
      (s: Json) => { s.formulation_basis.profile_id = "product_preview_mechanics_v1"; },
      (s: Json) => { delete s.contract_evidence; },
      (s: Json) => { s.retained_precision = null; },
      (s: Json) => { s.retained_precision = [s.retained_precision]; },
      (s: Json) => { s.retained_precision = "receipt"; },
      (s: Json) => { delete s.retained_precision; },
      (s: Json) => { s.source_block_recovery = {}; },
      (s: Json) => { s.carrier_evidence = {}; },
      (s: Json) => { s.producer.component_version = "0.1.0"; },
    ]) {
      const s = structuredClone(source) as Json; edit(s);
      expect(sourceContract(s)).toBe("unsupported");
      expect(numericalResultStanding(s, null).findings).toStrictEqual(["SOURCE_NUMERICAL_CONTRACT_UNSUPPORTED"]);
    }
  });
});

describe("the 14 shared parity scenarios agree with Rust U6a", () => {
  it.each<[string, Json]>((caseFile.cases as Json[]).map(c => [c.id, c]))("%s", async (_id, c) => {
    const mode = c.fixture.replace(/^milestone_/, "") as PreviewSolverMode;
    const doc = milestone(mode);
    const source = structuredClone(doc.source) as Json, invocation = structuredClone(doc.invocation);
    for (const edit of c.edits) {
      expect(edit.op).toBe("set");
      setPath(edit.target === "source" ? source : invocation, edit.path, edit.value);
    }
    // TS has no synchronous reader: the invocation case is a capture of that
    // invocation through mocked IPC; no invocation is a delivery without a capture.
    const solveMode = invocation.solver_mode as PreviewSolverMode;
    const received = await deliverDirect(source, c.invocation === null ? null : invocation.request.model, solveMode);
    const requestedIds = c.requested === "invocation" ? caseIds(doc.model) : c.requested.map((r: Json) => r.ref_id);
    const model = withLoadCases(doc.model, requestedIds);
    const route = sourceContract(received);
    const standing = route === "unsupported" ? "unsupported" : route === "retained_preview_physics" ? retainedPrecisionStanding(received, model).standing : "unexpected";
    expect(standing).toBe(c.expected_standing);
    // Raw dispatch: the header route, then the accepted reader without an invocation.
    let dispatch: string;
    if (route === "unsupported") dispatch = numericalResultStanding(received, model).findings[0];
    else dispatch = await validateRetainedPrecision(received).then(() => "ok", (error: Json) => error.code);
    expect(dispatch).toBe(c.expected_dispatch);
    expect(numericalResultStanding(received, model).eligible).toBe(false);
  });
});

describe("notices, labels and the results-panel standing text", () => {
  it("the bound is printed upward with three significant digits", () => {
    expect(upwardBoundText(0)).toBe("0");
    // A printed value equal to b as a binary64 is stepped up too: never below b.
    expect(upwardBoundText(1.25)).toBe("1.26e+0");
    expect(upwardBoundText(1.2344e-20)).toBe("1.24e-20");
    expect(upwardBoundText(9.9951e-5)).toBe("1.00e-4");
    expect(upwardBoundText(9.996e3)).toBe("1.00e+4");
    // A step up from 9.99 carries into the exponent.
    expect(upwardBoundText(9.994e-5)).toBe("1.00e-4");
    expect(upwardBoundText(9.993e3)).toBe("1.00e+4");
    expect(upwardBoundText(1.2345e7)).toBe("1.24e+7");
    expect(upwardBoundText(1.23e-20)).toBe("1.24e-20");
    expect(N_RP_ABSOLUTE).toContain("±{b} {unit}");
    // b is in the SI unit the reader classified the quantity in.
    const one = "3ff0000000000000";
    for (const [unit, si] of [["mm", "m"], ["kN", "N"], ["kN*m", "N*m"], ["MPa", "Pa"], ["N", "N"], ["rad", "rad"]]) expect(retainedAbsoluteNotice(one, unit)).toBe(N_RP_ABSOLUTE.replace("{b}", "1.01e+0").replace("{unit}", si));
  });
  it.each(MODES)("%s: registered rows carry their class label with an upward b in SI units; notices summarize per case", async (mode) => {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    const classes = retainedRowClasses(received)!;
    let checked = 0;
    for (const row of received.results) {
      const c = classes.get(row.id)!, label = resultRowLabel(row, received);
      if (c.class !== "absolute_verified") { expect(label === null || !label.includes("Uncovered quantity"), row.id).toBe(true); continue; }
      const match = /±(\S+) (\S+), below/.exec(label!)!;
      expect(Number(match[1])).toBeGreaterThanOrEqual(decodeBinary64(c.bound_bits!));
      expect(match[2]).toBe({ mm: "m", MPa: "Pa", kN: "N" }[row.unit] ?? row.unit);
      checked += 1;
    }
    expect(checked).toBe(69);
    const mm = received.results.find(row => row.unit === "mm" && classes.get(row.id)!.class === "absolute_verified");
    if (mm) expect(resultRowLabel(mm, received)).toContain(" m, below");
    const headline = received.results.find(row => row.id === received.summary.max_open_formula_stress!.result_ref)!;
    expect(resultRowLabel(headline, received)).toBe(`${retainedAbsoluteNotice(classes.get(headline.id)!.bound_bits!, headline.unit)} ${N_HEADLINE}`);
    const notices = knownSemanticNotices(received);
    expect(notices.map(n => n.id)).toStrictEqual(["headline-label", "retained-precision-absolute:case"]);
    expect(notices[1].text).toContain("69 quantities verified only to an absolute bound");
    // Unregistered: no class is known, so no row is presented as verified.
    const copy = structuredClone(received);
    expect(knownSemanticNotices(copy).map(n => n.id)).toStrictEqual(["headline-label", "retained-precision-unvalidated"]);
    expect(resultRowLabel(headline, copy)).toBe(N_HEADLINE);
  });
  it("the standing text comes from the registered receipt, never from numerical_quality", async () => {
    const { source, model } = milestone("sparse_interactive");
    const received = await deliverDirect(source, model, "sparse_interactive");
    expect(source.numerical_quality!.status).toBe("sensitive");
    render(<ResultsPanel result={received} knowledge={null} analysisRun={null} selectedResultId={null} onSelectResult={() => {}} />);
    const text = screen.getByTestId("numerical-result-standing").textContent!;
    expect(text).toBe(retainedPrecisionStandingText(received));
    expect(text).toContain("receipt validated by the retained-precision reader against the actual invocation");
    expect(text).not.toMatch(/sensitive|Numerical integrity:/);
    const absolute = received.results.find(row => retainedRowClasses(received)!.get(row.id)!.class === "absolute_verified" && row.unit === "N")!;
    expect(screen.getByTestId(`result-row-label-${absolute.id}`).textContent).toContain("Uncovered quantity: verified only to an absolute bound");
    expect(screen.getByTestId("results-notice-retained-precision-absolute:case")).toBeTruthy();
    cleanup();
    render(<ResultsPanel result={structuredClone(received)} knowledge={null} analysisRun={null} selectedResultId={null} onSelectResult={() => {}} />);
    expect(screen.getByTestId("numerical-result-standing").textContent).toContain("receipt not validated for these exact bytes");
    cleanup();
    const edited = structuredClone(source); edited.results[0].value = 12345;
    const refused = await deliverDirect(edited, model, "sparse_interactive");
    expect(retainedPrecisionStandingText(refused)).toContain("refused by the retained-precision reader (RETAINED_PRECISION_RECEIPT_MISMATCH); unsupported");
    expect(retainedPrecisionStandingText(received)).toContain("Selected cases: 1 of 1.");
    const twoCases = structuredClone(source) as Json;
    twoCases.retained_precision.body.cases.push({ basis_ref: { ref_type: "load_case", ref_id: "second" }, status: "not_required" });
    expect(retainedPrecisionStandingText(twoCases)).toContain("Selected cases: 1 of 2.");
  });
});

describe.each(MODES)("%s: reopen revalidates the saved statement and never mints standing", (mode) => {
  async function saved(edit?: (envelope: Json) => void): Promise<LocalProjectEnvelope> {
    const { source, model } = milestone(mode);
    const received = await deliverDirect(source, model, mode);
    const manifest = { manifest_ref: { object_type: "InputManifest", ref: "manifest:invented-retained-reopen" }, manifest_sha256: "1".repeat(64), manifest: { model_basis: { model_ref: received.model_ref }, solver_basis: { solver_name: received.producer!.component_name, solver_version: received.producer!.component_version, solver_build_ref: "unit-transport-replay-not-native-witness" } } };
    const analysis_run = await buildAnalysisRunV03(received, manifest, undefined, modelLoadBasisRefs(model));
    // Persistence keeps JSON text (src-tauri mechanics_result_json, analysis_run_json).
    const envelope: Json = JSON.parse(JSON.stringify({ model, mechanics_result: received, analysis_run, model_hash: await computeModelHash(model), editor_intents: [], proposal: null, selected_review_target: null }));
    edit?.(envelope);
    envelope.project_envelope_hash = await computeProjectEnvelopeHash(envelope);
    return envelope as LocalProjectEnvelope;
  }
  it("a saved successor reads needs_recompute; its receipt revalidates and its AnalysisRun copy matches", async () => {
    u7.simulate = true; // even the post-U7 reader cannot mint standing from saved bytes
    const opened = await saved();
    const context = (await buildHistoricalRunContext(opened))!;
    expect(context.mechanicsResult).not.toBeNull();
    expect(context.findings).toStrictEqual(["HISTORICAL_INPUT_MANIFEST_MISSING", RETAINED_PRECISION_VALIDATION_REQUIRED]);
    expect(numericalResultStanding(context.mechanicsResult!, opened.model).eligible).toBe(false);
    expect(hasNativeMechanicsInvocation(context.mechanicsResult, opened.model, mode)).toBe(false);
    expect(retainedPrecisionRegistration(context.mechanicsResult)).toBeNull();
  });
  it("a saved successor without an AnalysisRun is revalidated and reports no copy mismatch", async () => {
    const opened = await saved(envelope => { envelope.analysis_run = null; });
    const findings = (await buildHistoricalRunContext(opened))!.findings;
    expect(findings).toContain(RETAINED_PRECISION_VALIDATION_REQUIRED);
    expect(findings).toContain("HISTORICAL_RUN_EVIDENCE_INCOMPLETE");
    expect(findings).not.toContain(ANALYSIS_RETAINED_PRECISION_RECEIPT_MISMATCH);
  });
  it("a mutated saved row reads unsupported: the reader's own code is a finding", async () => {
    const opened = await saved(envelope => { envelope.mechanics_result.results[0].value = 12345; });
    const findings = (await buildHistoricalRunContext(opened))!.findings;
    expect(findings).toEqual(expect.arrayContaining([RETAINED_PRECISION_VALIDATION_REQUIRED, "RETAINED_PRECISION_RECEIPT_MISMATCH", "HISTORICAL_RESULT_HASH_MISMATCH"]));
  });
  it.each([
    ["altered", (envelope: Json) => { envelope.analysis_run.analysis_run.retained_precision.body.receipt_version = 2; }],
    ["dropped", (envelope: Json) => { delete envelope.analysis_run.analysis_run.retained_precision; }],
  ] as const)("an %s AnalysisRun receipt copy is reported", async (_label, edit) => {
    const findings = (await buildHistoricalRunContext(await saved(edit)))!.findings;
    expect(findings).toContain(ANALYSIS_RETAINED_PRECISION_RECEIPT_MISMATCH);
    expect(findings).toContain("HISTORICAL_ANALYSIS_HASH_MISMATCH");
    expect(findings).not.toContain("RETAINED_PRECISION_RECEIPT_MISMATCH");
  });
});
