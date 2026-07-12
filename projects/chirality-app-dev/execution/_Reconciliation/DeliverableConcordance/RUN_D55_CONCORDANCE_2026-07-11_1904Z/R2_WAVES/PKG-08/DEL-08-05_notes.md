# DEL-08-05 concordance notes (R2 Wave-3, RUN_D55_CONCORDANCE_2026-07-11_1904Z)

Deliverable: DEL-08-05 Subagent Child Run Records and Artifacts (PKG-08, DATA_MODEL_CHANGE).
Source state: `frontend/` at `fac46e33f` (byte-identical through HEAD `74150b3a8` per the W3
source-state binding); behavioral verification cites `GATE-TRANSCRIPT(W1@fac46e33f)`
(typecheck exit 0; Vitest 667 passed/4 skipped).

## Census

Rows total: 17 (18 lines incl. 19-column header).

By ClaimType: REQUIREMENT 12; EXCLUSION 2; IMPLEMENTED_UNMAPPED 1; REMAINING_WORK 1; REGISTER_DEFECT 1.

By Disposition: ALIGNED 14; STALE_SPECIFICATION 1; IMPLEMENTED_UNDOCUMENTED 1; REMAINING_STATE_MISMATCH 1.

All 12 requirements have live implementation on the DEL-08-05 harness surfaces and INSP-03 PASS
that remains STILL CURRENT. The single spec-drift row (REQ-001) is a documentation defect in the
Datasheet/Guidance, not a requirement failure.

## PKG-08 frozen-process caution applied

No row required a `DEFERRED_AGENT_WORKFLOW` disposition. DEL-08-05 is the product-runtime DATA_MODEL
slice (event/record/artifact shapes) of PKG-08, not an agent-instruction/matrix/persona surface. The
adjacent DEL-08-04 governance bridge and any agent-definition files were read only as frozen context;
none is judged or repaired here. The `AGENT_SUBAGENT_PREREQUISITE_POSTURE` constant
(agent-runtime-contract.ts lines 19-25) asserts executable delegation stays blocked/contract-only;
that execution-posture question is DEL-08-04 governance territory and was not converted into a
DEL-08-05 claim.

## Least-confident rows (self-flagged; each carries the alternative reading that would flip it)

- **REQ-001 (STALE_SPECIFICATION, MEDIUM).** Called stale because the Datasheet Construction
  "Target ChildRunRecord Fields" table (lines 49-60) lists a non-existent `completedAt` field and
  omits the governed-required `mode`/`capabilityPolicy`/`governance`/`contractVersion`, and the
  Guidance example (lines 43-58) uses `persona`/`sdkAgentId`/`model`/`startedAt`/`completedAt` absent
  from the implemented type. ALTERNATIVE READING: mark ALIGNED — the operative *requirement*
  (Specification REQ-001) and Procedure Verification already match the implementation exactly, so the
  Datasheet/Guidance are merely secondary/illustrative restatements and the drift is a doc-repair
  residual rather than the row's defect. I chose STALE_SPECIFICATION because a declared-state document
  (Datasheet) flatly asserts a now-false field shape (MR-8 tie-break: flat now-false assertion ->
  STALE_SPECIFICATION, repair-shaped).

- **REQ-006 (ALIGNED, MEDIUM).** "unique event IDs" is proven only as per-message id derivation +
  append-order preservation; no test asserts dedup ENFORCEMENT. ALTERNATIVE READING: PARTIALLY_
  IMPLEMENTED if "unique event IDs" is read as requiring an enforced uniqueness guarantee. I kept
  ALIGNED because the SPEC 9.2 wording is satisfied by unique-per-message id generation and the
  requirement does not demand a dedup gate; recorded the un-asserted gap in RemainingWork.

- **REQ-011 / EXC-002 (ALIGNED, MEDIUM).** Negative/absence claims ("does not reactivate retired
  scope"). Verified by scope-boundary review of the DEL-08-05 surfaces (RUN-INSPECTION@fac46e33f) plus
  grep for pipeline-record/dep-graph/deliverable-lock/staleness symbols — none present. ALTERNATIVE
  READING: UNKNOWN if a reviewer wants a whole-tree negative rather than a surface-scoped one. I bound
  the claim to the named DEL-08-05 surfaces (its data-model scope), which is where the requirement
  applies.

- **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** The hardcoded child-output byte limits
  (16 KiB inline / 512 KiB artifact, tool-result-artifacts.ts lines 38-39). ALTERNATIVE READING:
  fold into REQ-007 as a bare implementation detail (no separate row) since REQ-007's storage behavior
  is already mapped. I raised it because the *threshold values* determine truncation/data-loss
  behavior, are unmapped to any requirement, and the W2 PKG-05 wave explicitly flagged this surface
  (DEL-05-05 UNMAPPED-1) as likely DEL-08-05 — see cross-wave note below.

- **REGISTER-1 (REMAINING_STATE_MISMATCH, MEDIUM).** DEP-08-05-006 metadata lag. ALTERNATIVE READING:
  not a defect — TBD is the conservative extraction posture and re-scoring DOCUMENT-prerequisite
  satisfaction is a DepClosure/R1 duty, not a per-deliverable register defect. I flagged it because
  the row's own Notes/EvidenceQuote assert the prerequisite is satisfied (ADQ-12 proof, LastSeen
  2026-06-21) while the Status column still reads TBD — an internal self-contradiction, which is the
  narrowest MR-5 trigger.

## Cross-wave verification of the W2 context handle

The dispatch handed me a W2 observation: child-output artifact storage with hardcoded limits
(PKG-05 DEL-05-05 UNMAPPED-1) as a likely DEL-08-05 surface. Verified independently:
`persistChildOutputArtifact` (tool-result-artifacts.ts lines 141-236) uses the hardcoded
`CHILD_OUTPUT_INLINE_BYTE_LIMIT`/`CHILD_OUTPUT_ARTIFACT_BYTE_LIMIT` constants — this is genuinely on
DEL-08-05's surface (REQ-007/008). It is distinct from `persistToolResultArtifact` (same file, lines
58-139), which uses `descriptor.resultBudget` (the DEL-05-05 tool-descriptor budget). So the child
path is DEL-08-05's own and the *thresholds* are unmapped -> recorded as UNMAPPED-1; the storage
*behavior* itself is mapped to REQ-007.

## Register-defect summary

- One REGISTER_DEFECT emitted: REGISTER-1 (DEP-08-05-006 SatisfactionStatus/ProposedMaturity = TBD
  contradicting its own satisfaction Notes; internal inconsistency / metadata lag).
- NOT emitted, by rule: `_DEPENDENCIES.md` "Declared Upstream: TBD" and "Declared Downstream: TBD"
  (lines 14-18). Per the W3 rule and docs/SPEC.md §5.2, Declared Upstream/Downstream are human-owned
  declaration sections (TBD by design), distinct from the agent-owned Extracted register; a bare
  Declared-TBD is not a register defect. Observation only.
- Broader pattern (noted, not separately flagged): DEP-08-05-005/007/008/009 are also DOCUMENT
  prerequisites/constraints whose target docs exist and are MATCH-verified, yet carry
  SatisfactionStatus=TBD. Unlike DEP-006 their Notes do not assert satisfaction, so they are
  defensible conservative-extraction states rather than self-contradictions. Class-level
  harmonization is an R3/DepClosure item.
- Dependencies.csv vs _DEPENDENCIES.md are internally consistent (10 ACTIVE rows; SATISFIED 4 / TBD 6
  matches both files). Schema validation PASS is corroborated by the D53A DepClosure coverage row
  `DEL-08-05,Y,10,Y,Y`.

## Other observations (informational; out of write scope to repair here)

- **Stale plans/ artifact:** `plans/artifacts/runtime_capability_matrix.md` row 18 (DEL-08-05) reads
  "PARTIAL - createAdapterObservedChildRunRecord exists and is contract-tested, but the factory has no
  adapter caller yet." That is OVERTAKEN at fac46e33f: `sdk-message-mapper.ts`
  `createChildRunRecordForTaskMessage` (lines 206-241) now calls `createAdapterObservedChildRunRecord`
  and wires it into the SDK task lifecycle (tested at sdk-message-mapper.test.ts lines 806-880). This
  strengthens REQ-004/005 ALIGNED. `plans/**` is historical context per AUTHORITY_MAP and is not a
  deliverable document, so no REGISTER_DEFECT and no repair row; recorded for R3 visibility.
- **INSP-03 ID format (MR-9):** the assessment uses `REQ-08-05-00n`; the current Specification uses
  `DEL-08-05-REQ-00n`. The spec was not rewritten after INSP-03 in a way that breaks mapping (same
  requirement content, 1:1 by number), so AssessmentEvidence maps `REQ-08-05-00n` -> the current
  DEL-08-05-REQ-00n row directly. No "no direct conclusion" cases arose.
- **Datasheet event-category under-listing:** Datasheet "Relevant event categories" (line 28) lists
  only `subagent.started`/`subagent.completed` while the implementation and REQ-004 carry all four
  (`started`/`progress`/`completed`/`failed`). Minor; folded into the REQ-004 RemainingWork note, not
  a separate defect (the label says "Relevant", not "all").

## Method deviations / blockers

None. Wrote exactly the two authorized artifacts
(`R2_WAVES/PKG-08/DEL-08-05_claims.csv`, this notes file). No tests executed; no dependencies
installed; no deliverable documents or `_STATUS.md` edited. Verification bound to `fac46e33f` via
`GATE-TRANSCRIPT(W1@fac46e33f)` per MR-3. No AUTHORITY_CONFLICT encountered; no cross-project
execution tree read (F-APP-3 respected).
