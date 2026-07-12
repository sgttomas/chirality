# DEL-08-03 concordance notes (R2 Wave-3, RUN_D55_CONCORDANCE_2026-07-11_1904Z)

Deliverable: DEL-08-03 Pipeline Category and Task Scope Dispatch (PKG-08, UX_UI_SLICE).
Source state: frontend/ at fac46e33f, byte-identical through HEAD 74150b3a8 (git diff empty
for pipeline-surface.tsx, task-scope.ts, filesystem.ts, options.ts, and the cited test files).

## Census

Total rows: 19.

By ClaimType: REQUIREMENT 12, ACCEPTANCE 1, EXCLUSION 4, IMPLEMENTED_UNMAPPED 1,
REMAINING_WORK 1. (REGISTER_DEFECT 0.)

By Disposition: ALIGNED 16, IMPLEMENTED_DIFFERENTLY 1 (REQ-010), STALE_SPECIFICATION 1
(EXC-003), IMPLEMENTED_UNDOCUMENTED 1 (UNMAPPED-1).

All 12 requirements were re-derived from the current Specification.md (REQ-001..012); the
R1 REQUIREMENT_INDEX.csv listed all 12, so no parser-gap re-derivation was needed. INSP-03
(2026-06-21, SHA d92ef1253) rated all twelve PASS under REQ-08-03-nnn naming; those IDs map
1:1 to DEL-08-03-REQ-nnn (no post-INSP-03 spec rewrite, so MR-9 old-REQ mapping is not
triggered).

## Least-confident rows (self-flagged; alternative reading that would flip them)

- **DEL-08-03-REQ-010 -> IMPLEMENTED_DIFFERENTLY (MEDIUM).** Flip reading: **ALIGNED.** The
  requirement's evidence clause names `/api/working-root/scope`, but the pipeline surface's
  dynamic scope scan actually consumes the sibling `/api/project/deliverables` route
  (deliverables-provider.tsx lines 116-119 -> scanProjectDeliverables). Both are docs/SPEC.md
  Section 17.2 active-root scan surfaces (lines 867 and 868), so the substantive
  anti-hard-coding intent (FR-013) is satisfied; only the specifically-named endpoint differs.
  Marked IMPLEMENTED_DIFFERENTLY because the requirement text and the Datasheet/INSP-03
  evidence pointer both name `/api/working-root/scope`, which is not the endpoint the pipeline
  consumes. It would flip to ALIGNED if the run treats "active working-root scope surface" as
  satisfied by any Section 17.2 active-root route regardless of the named example.

- **DEL-08-03-UNMAPPED-1 -> IMPLEMENTED_UNDOCUMENTED (MEDIUM).** Flip readings: (a) fold into a
  sibling as ALIGNED once DEL-07-02 (scaffold) / DEL-07-04 (status-transition) are read to own
  the UI layer — but DEL-02-02's wave note recorded that DEL-07-02's Specification excludes "UI
  presentation beyond the scaffold API result surface," so the pipeline scaffold/transition UI
  is currently unowned; (b) treat it as out-of-scope noise not worth an UNMAPPED row on
  DEL-08-03 because the same behavior is already captured under DEL-02-02 UNMAPPED-1/2 on the
  shared pipeline-surface.tsx. Recorded here (with an explicit DEL-02-02 cross-handle) because
  the panels are material live behavior physically resident in a file DEL-08-03's Datasheet
  names as its construction surface, and plan §6 asks each deliverable to list unmapped surface
  behavior. R3 should de-duplicate the shared-surface claim rather than count it twice.

- **DEL-08-03-EXC-003 -> STALE_SPECIFICATION (HIGH, lower-priority self-flag).** Flip reading:
  leave as an accepted exclusion. Marked STALE_SPECIFICATION because Specification.md line 20
  still says "Dependencies.csv remains deferred" while the live register holds 10 ACTIVE rows
  (mirrors the R0 exemplar's DEL-02-01-EXC-004 handling). Confidence is high that the wording is
  stale; the only judgment is disposition label vs. a REGISTER_DEFECT (see below).

## Cross-deliverable / shared-surface observations (for R3)

- **Shared pipeline-surface.tsx ownership.** Decomposition v3.2 maps SOW-007 "Pipeline
  selectors" primarily to PKG-08/DEL-08-03 (line 389, "Primary package is agent dispatch"),
  while DEL-02-02 "Workbench and Pipeline Selection UX" also covers "category controls,
  task-scope selectors, and disabled coming-soon variants" (line 290) and DEL-07-03 owns the
  document-kit/metadata scanners for SOW-026. So pipeline-surface.tsx (selectors) and
  filesystem.ts (knowledge-type discovery) carry accepted dual mappings. This wave maps
  DEL-08-03's requirements to those surfaces and flags the DEL-02-02 co-claim; R3 should confirm
  the intended split (DEL-08-03 = dispatch semantics; DEL-02-02 = shell/navigation presentation).

## Register-defect summary (0 defects)

`Dependencies.csv` (v3.1, 10 rows: 5 ANCHOR DEP-001..005 + 5 EXECUTION DEP-006..010), the
`_DEPENDENCIES.md` Extracted Dependency Register (Total 10 / ACTIVE 10 / ANCHOR 5 / EXECUTION 5),
and the Datasheet Dependency Edge Snapshot agree on the row set. All seven `_REFERENCES.md`
SHA-256 hashes still MATCH the live docs at HEAD (DIRECTIVE/CONTRACT/SPEC/TYPES/PLAN/PRD
re-verified; REF-007 `AGENT_SOFTWARE_DECOMP.md` is a FROZEN_PROCESS_INPUT surface, hash
unchanged). No `Dependencies.csv` / `_DEPENDENCIES.md` / `_REFERENCES.md` internal inconsistency
or metadata lag was found -> no REGISTER_DEFECT rows.

Noted (not a defect, per the Wave-3 rule): `_DEPENDENCIES.md` "Declared Upstream" and "Declared
Downstream" both read "TBD - no accepted dependency edges have been extracted yet" (lines 14, 18)
even though the Extracted register just below lists 10 rows. Per the W3 brief (docs/SPEC.md §5.2:
Declared sections are human-owned, TBD by design, distinct from the agent-owned Extracted
register), a Declared-TBD is not a register defect; the stale explanatory clause is a class-level
harmonization item for R3, consistent with how DEL-08-01/02 handled the same pattern. The stale
"Dependencies.csv remains deferred" claim in Specification.md line 20 is a kit-document (not a
register-internal) inconsistency and is carried as EXC-003 STALE_SPECIFICATION, not a
REGISTER_DEFECT.

## "No test exists" checks performed

- REQ-010: grep confirmed `/api/working-root/scope` is fetched only by workbench-surface.tsx
  (line 211), and the pipeline surface's scan path is `/api/project/deliverables`; no test binds
  the pipeline scan to `/api/working-root/scope`. This is a real absence, not an assumed one.
- REQ-011 governance-negative: the property IS tested (routes.test.ts lines 703-763 assert
  pipelineIntent is dropped as an unknown opts field; lines 646-701 assert subagentGovernance
  cannot bypass the runtime environment gate), so REQ-011 is a behavioral ALIGNED with both
  implementation (options.ts warnOnUnknownOpts) and verification evidence.

## Method deviations / blockers

None. Read-only discipline held (only the two wave-output files written). No mutating git/test
execution. PKG-08 FROZEN_PROCESS_INPUT caution applied: no agent-instruction/matrix/persona
surface was judged; UNMAPPED-1's scaffold/transition panels are product-runtime UI (ownership
question), not an agent-workflow contract, so they take an IMPLEMENTED_UNDOCUMENTED product
disposition rather than DEFERRED_AGENT_WORKFLOW. No DEFERRED_AGENT_WORKFLOW rows were required
for this deliverable.
