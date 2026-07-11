# DEL-02-05 concordance notes — R2 Wave-1

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; source state `frontend/` @ `fac46e33f` (byte-identical to `4c8ed8907`/`61d70bdb0`; GATE-TRANSCRIPT W1). Read-only discovery.

## Census

- Total claim rows: 21 (+ header).
- By ClaimType: REQUIREMENT 10 (R01–R10), EXCLUSION 5, ACCEPTANCE 1, IMPLEMENTED_UNMAPPED 1, REGISTER_DEFECT 3, REMAINING_WORK 1.
- By Disposition: ALIGNED 16, STALE_SPECIFICATION 1, IMPLEMENTED_UNDOCUMENTED 1, REMAINING_STATE_MISMATCH 3.
- AssessmentEvidence tokens: STILL CURRENT 10, OVERTAKEN 4 (R10, ACC-001, REGISTER-1, REGISTER-2), NOT APPLICABLE 7.
- SelectableUnderCurrentLoop = YES on REMAINING-1 only (UNGATED, IN_PROGRESS, standing-loop selectable).

## R1 index gap recorded (dispatch-noted caveat)

`R1_INVENTORY/REQUIREMENT_INDEX.csv` lists ZERO requirement IDs for DEL-02-05 (regex parser did not capture the `DEL-02-05-Rnn` form). The 10 requirement claims were re-derived directly from `Specification.md` Requirements table (lines 27–38). The Specification requirement IDs (R01–R10) are stable and map 1:1 to the INSP-03 Requirements Conformance Matrix, so MR-9 old-REQ remapping is not needed (no post-assessment spec rewrite of IDs). REMAINING_INVENTORY (1 item), ASSESSMENT_INDEX, DECISION_INDEX, IMPLEMENTATION_SURFACES, VERIFICATION_INDEX rows for DEL-02-05 were consulted and are consistent with the derived set.

## Method notes / MR application

- MR-4: Datasheet Attributes/Conditions restatements folded into their covering REQ rows (key status values -> R02; precedence -> R03; storage location/mechanism -> R01; retry -> R06; redaction -> R09; turn:error/process:exit events -> R07). The only datasheet-distinct condition emitted as ACCEPTANCE is the PRD source-integrity/hash-warning condition (ACC-001).
- MR-3/MR-10: behavioral ALIGNED rows cite `GATE-TRANSCRIPT(W1@fac46e33f)` plus named test files with line anchors. Doc/scope rows (EXC-*) use scope-review prose per the R0 exemplar; ACC-001 and REGISTER-1 use `SNAPSHOT+LIVE-REVERIFY(_REFERENCES.md REF-006)`; REGISTER-2/R10 use `DOC-BASIS(Evidence_ORN-08)`.
- API-key-handling caveat honored: no key values or SHAs-of-keys copied; masking/storage cited by file/line only. (The SHA in ACC-001 is the docs/PRD.md document hash, not key material.)
- Scope split: this deliverable is a UI/IPC feedback slice. The provider wrapper (anthropic-agent-sdk-manager.ts, DEL-04-05), the redaction helper implementation (run-logger.ts), the runtime event emitters (turn-engine.ts, PKG-03), and network allowlist enforcement are out of scope (EXC-002/003/004). R03/R07/R09 therefore bind only the in-scope UI consumption/status surfaces; the cross-layer implementation is cited as context and its own tests are attributed to the owning layer.

## Register-defect summary (MR-5)

- REGISTER-1 (HIGH): `_DEPENDENCIES.md` line 49 SOURCE_WARNING still asserts REF-006 hash mismatch; `_REFERENCES.md` line 12 shows REF-006 MATCH at fac46e33f (D-APP-38/D-APP-35). Metadata lag -> REMAINING_STATE_MISMATCH.
- REGISTER-2 (LOW, self-flagged): `Dependencies.csv` DEP-02-05-005 marks the typed error-taxonomy target UNKNOWN/TBD; ORN-08 (2026-07-10) + R10 resolve it to `@chirality/harness-contract`. ORN-08 explicitly declines to mutate the register absent a ruling, so the lag persists by design — hence LOW confidence and a HumanDecision reference rather than a clean repair.
- REGISTER-3 (LOW): SOW-023 traceability delta — Datasheet line 47 cites SOW-023 for retry state, but no SOW-023 anchor row exists and `_CONTEXT.md` lists only SOW-013/SOW-019; self-documented by `_DEPENDENCIES.md` line 50 TRACEABILITY_DELTA.
- Non-register hygiene (not a REGISTER row): api-key-storage.ts line 2 and api-key-store.ts line 2 header comments mislabel the surface `DEL-02-06` (INSP-03 Gap, Low); folded into R01 RemainingWork rather than a ledger row since it is a code comment, not a register file.

## Least-confident rows (mandatory self-flagging — recheck these plus all non-ALIGNED rows)

1. **DEL-02-05-R03 (ALIGNED, MEDIUM).** Alternative reading that would flip it: **PARTIALLY_IMPLEMENTED**. The requirement literally says "the UI must reflect API key precedence: UI first, ANTHROPIC second, CHIRALITY third." The in-scope UI status layer (api-key-ipc.ts) collapses both env vars into a single `env` source and only orders `ui > env > none`; the ANTHROPIC-before-CHIRALITY tie-break is realized and tested exclusively in the out-of-scope provider layer (anthropic-agent-sdk-manager.ts). If the verifier reads R03 as demanding the three-tier ordering be observable in the UI slice itself, this is PARTIALLY_IMPLEMENTED. I kept ALIGNED because INSP-03 rated it PASS on the combined UI+runtime evidence and the deliverable is scoped as a feedback surface.

2. **DEL-02-05-EXC-005 (ALIGNED, MEDIUM).** Alternative reading: **STALE_SPECIFICATION** (as with DEL-02-01 EXC-004). A `Dependencies.csv` with 6 rows exists, yet the Specification lists "Dependency extraction and Dependencies.csv creation" as out of scope. I read the exclusion as scoping the four-document TASK (a separate ruled 2026-05-20 extract run produced the register, and Procedure line 13's "no accepted dependency edges" is true on the extracted-vs-human-accepted distinction). Unlike DEL-02-01, this kit does not flatly assert "Dependencies.csv not produced," so I did not treat it as flatly-false kit text under MR-8. If the verifier weights the surface contradiction over the TASK-scoping reading, this flips to STALE_SPECIFICATION.

3. **REGISTER-2 (REMAINING_STATE_MISMATCH, LOW).** Alternative reading: **ACCEPTED_DIVERGENCE / no defect**. Because ORN-08 deliberately left `Dependencies.csv` unmutated ("does not mutate or satisfy Dependencies.csv") and no ruling directs an update, the UNKNOWN/TBD target could be read as a disclosed, intentionally-open state rather than a lagging defect. I emitted it as a metadata-lag REGISTER_DEFECT because the evidence to resolve the target now exists; the resolution is gated on a dependency-mapping decision (flagged in HumanDecisionNeeded), not a free repair.

4. **DEL-02-05-R10 (ALIGNED, HIGH — flagged because AssessmentEvidence is OVERTAKEN).** The INSP-03 PARTIAL was an issuance-gate/architecture-review concern, not a current-behavior gap. ORN-08 resolves ownership to the canonical harness-contract seam and error-display.ts imports it. Alternative reading: if a verifier treats the unresolved cross-package *governance* question as a live scope defect (not lifecycle), it could read PARTIALLY_IMPLEMENTED; I judged current behavior fully conformant (type consumed, taxonomy not redefined).

## HumanDecisionNeeded pointers (non-ledger)

- EXC-002 references Guidance CT002 (SOW-019 scope split across DEL-02-05/DEL-04-05/DEL-09-06), "Human ruling: TBD"; live split matches the proposed authority.
- REGISTER-2 references the open taxonomy dependency-mapping decision (whether DEP-02-05-005 should be refreshed to the harness-contract owner).
- UNMAPPED-1 routes a scope-adoption question for the remove/reveal management controls (plan boundary 1: no automatic adoption).

No AUTHORITY_CONFLICT, no DEFERRED_AGENT_WORKFLOW, no UNKNOWN dispositions in this wave. No cross-project (F-APP-3) surfaces were read.
