# DEL-07-02 concordance notes (R2 Wave-3, PKG-07)

Source state: `frontend/` at `fac46e33f` (byte-identical through HEAD `74150b3a8`).
Deliverable: Execution Root Scaffolding from Decomposition (BACKEND_FEATURE_SLICE).
Primary surface: `frontend/src/lib/harness/scaffold.ts` (+ `src/app/api/harness/scaffold/route.ts`).

## Census

Total rows: 21.

By ClaimType: REQUIREMENT 13, EXCLUSION 4, ACCEPTANCE 1, IMPLEMENTED_UNMAPPED 1,
REMAINING_WORK 1, REGISTER_DEFECT 1.

By Disposition: ALIGNED 16, PARTIALLY_IMPLEMENTED 3, STALE_SPECIFICATION 1,
REMAINING_STATE_MISMATCH 1.

(Fan-in correction, W3: UNMAPPED-1 was initially filed IMPLEMENTED_UNDOCUMENTED
with a NEW-PACKET flag; the fan-in verifier refuted it against decomposition
v3.2 line 330, which assigns "status read, dependency read, scope scan, and
scaffold preview/dry-run" to sibling DEL-06-03 (SOW-048/SOW-050) — an accepted
mapping under the binding W3 rule. Independently re-verified against the
decomposition text. The row now carries Disposition ALIGNED with the DEL-06-03
cross-deliverable handle named in ImplementationEvidence/NormativeSource, and
HumanDecisionNeeded reverts to NO. ClaimType stays IMPLEMENTED_UNMAPPED as the
run-local record of how the claim was generated: live behavior on this
deliverable's surface with no DEL-07-02 kit mapping.)

Requirement coverage: R1 REQUIREMENT_INDEX.csv lists all 13 IDs (REQ-001..013);
the parser gap noted in the brief did NOT apply here — all 13 were re-derived
from Specification.md and matched. No requirement dropped.

## Key finding — INSP-03 overtaken by ADQ-06 (same day)

INSP-03 (2026-06-21, SHA `210b5b7427`) rated REQ-004 FAIL, REQ-005 FAIL, and
REQ-010 PARTIAL against gap G1 (scaffold did not seed the minimum PREPARATION
metadata baseline). ADQ-06 (Evidence_ADQ-06_Scaffold_Baseline_Seeding.md, plus
the "ADQ-06 Superseding Note" at the top of the assessment itself) implemented
G1. Live `scaffold.ts` now seeds all five metadata files (lines 905-919), writes
a canonical `OPEN` `_STATUS.md` (buildStatusTemplate line 590), and blocks
PREPARATION readiness on missing metadata (validatePreparationCompatibility
lines 771-773). Tests confirm (harness-scaffold.test.ts 115-127, 197-227,
254-284). These three rows are therefore ALIGNED with AssessmentEvidence
OVERTAKEN. `ADQ` items are queue/evidence records, not decision-register
rulings, so `LatestDecision` = NONE_FOUND for them (consistent with the empty
PKG-07 DECISION_INDEX).

Residual doc-quality note (not a separate claim): the assessment's Requirements
Conformance Matrix rows for REQ-004/005 (FAIL) and REQ-010 (PARTIAL) were never
edited to agree with the ADQ-06 superseding note above them; captured as an R5
doc-annotation residual in those rows' RemainingWork.

## Register cross-reference

- Dependencies.csv: 7 ACTIVE rows (DEP-07-02-001..007); internally consistent
  with `_DEPENDENCIES.md` (ACTIVE 7; ANCHOR 3 / EXECUTION 4; RequiredMaturity
  SEMANTIC_READY 4 / TBD 3). No count/lifecycle lag.
- One register defect (REGISTER-1): DEP-07-02-007 Notes/EvidenceQuote and
  `_DEPENDENCIES.md` Run Notes line 44 still assert REF-006 (docs/PRD.md) is a
  HASH_MISMATCH warning, but live `_REFERENCES.md` REF-006 shows MATCH and the
  recomputed `docs/PRD.md` hash at fac46e33f equals the recorded value
  (`ac35fba40...c30bfd`). Metadata lag → REMAINING_STATE_MISMATCH.
- The same REF-006 stale warning is carried in the four-doc kit
  (Datasheet/Specification/Guidance/Procedure); captured as the ACCEPTANCE row
  ACC-001 (STALE_SPECIFICATION), mirroring the DEL-02-01 R0 ACC-001 pattern.
  ACC-001 and REGISTER-1 are distinct surfaces (kit acceptance declaration vs
  dependency register lag), not double-counting.
- Declared Upstream / Declared Downstream in `_DEPENDENCIES.md` are both bare
  "TBD". Per the W3 rule (docs/SPEC.md §5.2: human-owned declaration sections,
  TBD by design) these are NOT register defects and no REGISTER row was emitted
  for them.

## Decision search

No D-APP ruling governs any DEL-07-02 requirement (DECISION_INDEX.csv has zero
PKG-07 rows). Incidental corpus mentions: D-APP-08 (distinguishes non-executable
scaffolding conceptually), D-APP-13 (`mcp__chirality__scaffold_exec` naming),
D-APP-29 (CoordinationMode/scaffold-seed design) — cited only as `(context)` on
REQ-006 where marginally relevant. D-APP-35/D-APP-38 govern the REF-006 hash
reconciliation (ACC-001, REGISTER-1).

## "No test exists" assertions — searched, not assumed

- REQ-011: grep of scaffold.ts at fac46e33f finds NO working-root-containment or
  instruction-root check (only `requireAbsolutePath`, lines 214-225). The
  containment helper `assertLexicallyWithinProjectRoot` exists only on the READ
  path (read-tools.ts 414-431), not on scaffold writes. VERIFICATION_INDEX lists
  only harness-scaffold.test.ts and scaffold-route.test.ts for this deliverable;
  neither asserts a scaffold write is rejected outside the working root or
  blocked from the instruction root. Absence verified, not assumed.
- REQ-012 / REQ-013: no missing-value-preserved-as-TBD fixture and no
  unsupported-but-partial table-shape fixture exist in harness-scaffold.test.ts;
  the only negative fixture (lines 229-252) is a whole-document rejection.

## Least-confident rows (mandatory self-flag, with the flip reading)

- **REQ-004, REQ-005** (ALIGNED / OVERTAKEN): flip to **STALE_ASSESSMENT** if
  the verifier holds that the assessment's uncorrected FAIL matrix rows still
  "present the stale conclusion as current truth" (MR-1) despite the in-file
  ADQ-06 superseding note. I judged the same-file superseding annotation retracts
  them, so live concordance is ALIGNED and the matrix lag is only an R5
  annotation residual — but this is the closest call in the packet.
- **REQ-011** (PARTIALLY_IMPLEMENTED): flip to **ALIGNED** if one accepts that
  decomposition SOW-027 assigns working-root containment / instruction-root
  protection to sibling DEL-07-01 (DEP-07-02-005), so the scaffold slice's only
  obligation is the absolute-path check it does perform. I kept
  PARTIALLY_IMPLEMENTED because the Specification text puts the MUST on "runtime
  tools involved in scaffolding" and Procedure step 2 directs the scaffold itself
  to reject out-of-root writes, which it does not.
- **REQ-012** (PARTIALLY_IMPLEMENTED): flip to **ALIGNED** if the ResponsibleParty
  TBD default plus fail-fast rejection of unparseable input are read as fully
  satisfying "preserved as TBD or reported diagnostics." I kept it partial on the
  verification gap and because most decomposition fields are dropped, not TBD'd.
- **UNMAPPED-1** — originally self-flagged here as IMPLEMENTED_UNDOCUMENTED with
  exactly this flip reading (sibling ownership of the preview surface). The
  fan-in verifier confirmed the flip: decomposition v3.2 line 330 assigns
  scaffold preview/dry-run to DEL-06-03, an accepted mapping. Row corrected to
  ALIGNED with the DEL-06-03 cross-deliverable handle; no longer low-confidence.

## Method deviations / blockers

None. Write scope respected (only these two files). No tests executed; behavioral
evidence bound to GATE-TRANSCRIPT(W1@fac46e33f) plus named test files/line
anchors. REF-006 reconciliation independently re-verified by live `shasum -a 256`
of `docs/PRD.md` at fac46e33f.
