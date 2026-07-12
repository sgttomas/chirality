# DEL-09-02 concordance notes (R2 Wave-4, PKG-09)

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: frontend/ at fac46e33f,
byte-identical through HEAD 6f7c06814 (per W4 dispatch). Read-only discovery.

## Census

- Total claim rows: 22
- By ClaimType: REQUIREMENT 16 (RQ-001..RQ-016), ACCEPTANCE 1, EXCLUSION 3,
  REGISTER_DEFECT 1, REMAINING_WORK 1.
- By Disposition: ALIGNED 16, PARTIALLY_IMPLEMENTED 2 (RQ-010, RQ-014),
  STALE_SPECIFICATION 3 (ACC-001 PRD-hash, EXC-001 domain-profile gating,
  RQ-015 landed-manifest wording), REMAINING_STATE_MISMATCH 1 (REGISTER-1).
- Fan-in resolution: RQ-015 was CONTESTED by the PKG-09 verifier; this agent
  re-weighed both readings and changed the row from PARTIALLY_IMPLEMENTED to
  STALE_SPECIFICATION (rationale in the RQ-015 entry below). Counts above
  reflect the final state.
- REGISTER defect count: 1.

## Requirement re-derivation (R1 parser gap applies)

REQUIREMENT_INDEX.csv scanned ZERO IDs for DEL-09-02 (the known regex parser gap).
The 16 requirement rows were re-derived directly from Specification.md
Requirements table (RQ-001..RQ-016, lines 17-32). REMAINING_INVENTORY.csv row 52
(the concordance bootstrap) and the absence of any DECISION_INDEX rows for
DEL-09-02 were confirmed against the live indices.

## Key state changes since INSP-03 (reviewed d0766e0f2, 2026-06-21)

The Section 9 validation surface materially evolved past the assessed and
kit-documented state; the live surfaces AGREE, so the changes are recorded in
`AssessmentEvidence` (OVERTAKEN) rather than as staleness defects except where a
kit surface still presents a now-false state as current:

1. **13 IDs -> 16 governed IDs.** A dedicated governed manifest
   `frontend/scripts/harness-section9-manifest.json` (schemaVersion 1) now
   enumerates 16 checks and is enforced by both `validate-harness-section9.mjs`
   (lines 92-98) and the release-quality wrapper `validate-release-quality-evidence.mjs`
   (REQUIRED_SECTION9_IDS lines 53-69, validateSection9Summary 209-265). The 16
   IDs are byte-equal to ratified PRD 12.4 (lines 1182-1197) and SPEC 19.3
   (lines 934-949). This overtakes INSP-03 RQ001/013/015 (RQ-001, RQ-013, RQ-015).
2. **Naming drift, kit-only.** Datasheet.md line 26 "Section 9 validation ID
   source list" still names `section9.sdk_turn_engine_event_log` and
   `section9.sdk_message_mapper` (old `sdk_` prefix). Ratified PRD/SPEC and live
   code use the `adapter_` prefix (SCA-APP-001 provider-adapter-general rename).
   Folded into RQ-001 RemainingWork rather than a separate row (MR-4).
3. **PRD hash now MATCH.** `_REFERENCES.md` REF-006 records docs/PRD.md MATCH
   (Expected=Actual=`ac35fba4...`); live `shasum -a 256 docs/PRD.md` reproduces
   `ac35fba4...`. The kit's HASH_MISMATCH warning (expected `86cb6fb9...`,
   observed `fb1c73f7...`) is stale under D-APP-38 -> ACC-001 (STALE_SPECIFICATION)
   plus REGISTER-1 for the `_DEPENDENCIES.md` Run-Notes metadata lag.
4. **Domain-profile amendment landed.** `section9.domain_profile_validation` is no
   longer gated/pending: `src/lib/harness/mcp/domain-profile-registry.ts` is the
   D-APP-50/D-APP-51 closed registry (two ruled profileIds, registration-is-the-gate,
   in-process-read-evidence transport only) and is validated live by
   `domain-profile-registry.test.ts`. Kit "gated/pending" framing is stale -> EXC-001.

## Least-confident rows (self-flagged; the alternative reading that would flip)

- **EXC-001 (domain-profile gating, STALE_SPECIFICATION, MEDIUM).** I read the
  landed D-APP-50/D-APP-51 registry + its passing test as satisfying "a governed
  domain-profile amendment enters scope," so the kit's gated/pending framing is
  stale. FLIP: if PRD's "domain-profile runtime validation" means full
  engine-execution validation (beyond closed-registry closure and read-evidence
  transport), the ID would still be partially pending and the row would become
  PARTIALLY_IMPLEMENTED with the gating framing partly current. Fenced to
  in-process read-evidence per F-APP-3 (this run reads, does not judge, domain
  engine integration level).
- **RQ-015 (governed manifest, STALE_SPECIFICATION, HIGH — re-dispositioned at
  fan-in).** Initially recorded PARTIALLY_IMPLEMENTED (warnings/blockers arrays
  present but content-empty read as an unsupported bounded portion). The PKG-09
  verifier contested with the reading that the SHOULD is satisfied — the
  manifest verifiably carries id/sourceReferences/testFiles/evidenceFiles/
  warnings/blockers per check, and the "warning/blocker notes ... when
  available" clause is satisfied vacuously since no warnings exist to record —
  and that the operative defect is the requirement's own now-false second
  sentence ("Current registry path is validate-harness-section9.mjs; richer
  warning/blocker metadata remains a future enhancement"), which under the MR-8
  tie-break (kit text flatly asserting a now-false state) is
  STALE_SPECIFICATION. On independent re-weighing this agent ADOPTED that
  reading: the deciding facts are (a) the original row's own RemainingWork
  contained only doc repair and no evidence-based implementation residual,
  which contradicts PARTIALLY_IMPLEMENTED's "only a bounded portion is
  supported"; (b) empty warning/blocker arrays are the honest correct content
  when nothing is pending — all 16 IDs bind to landed, passing surfaces — so
  no implementation gap exists to support; and (c) the changed row now applies
  the tie-break uniformly with ACC-001/EXC-001 (now-false kit sentence ->
  STALE_SPECIFICATION) and with RQ-001 (true requirement sentence, drift only
  in secondary kit text -> ALIGNED + doc-repair RemainingWork). Residual FLIP
  back to PARTIALLY_IMPLEMENTED only if "richer warning/blocker metadata"
  is read as a normative content obligation independent of the "when
  available" qualifier; this agent judges that reading weaker because the
  sentence presents itself as a current-state description, not a requirement
  clause. Judgment is this agent's own, not a ruling.
- **RQ-013 (summary schema, ALIGNED, MEDIUM).** Marked ALIGNED because the spec's
  own current-state wording (status/testCount/results + wrapper consistency) is
  exactly implemented and INSP-03's "underdeveloped enum" is partly overtaken by
  the governed statusVocabulary. FLIP to PARTIALLY_IMPLEMENTED only if
  warning/blocker CONTENT population is read as a normative obligation of
  RQ-013 — a reading this ledger rejected at fan-in for RQ-015 (the "when
  available" clause is satisfied vacuously; see the RQ-015 entry).
- **EXC-003 (dependency-register exclusion, ALIGNED, MEDIUM).** The exclusion
  ("no Dependencies.csv creation") reads as absolute, yet an extracted
  Dependencies.csv (25 rows) exists. I reconciled it as separate extract tooling
  per `_DEPENDENCIES.md` run history, so no repair. FLIP to STALE_SPECIFICATION
  if the exclusion is read literally as violated (parallels DEL-02-01-EXC-004,
  which the R0 exemplar dispositioned STALE_SPECIFICATION).
- **REGISTER-1 (`_DEPENDENCIES.md` PRD-hash metadata lag, REMAINING_STATE_MISMATCH,
  MEDIUM).** Emitted as a register defect. FLIP to no-defect if the line is read
  as immutable dated run-history provenance (it sits under "Run Notes" logging the
  2026-05-20 extraction) rather than a live current-state claim.
- **RQ-014 (status honesty / report-only, PARTIALLY_IMPLEMENTED, NEW-PACKET).**
  Two residuals bundled: the pass/fail-only enum (currently moot - all 16 IDs have
  landed phases) and the unruled report-only-vs-gate policy decision (INSP-03 G6
  gap + forward rec 1). FLIP to ALIGNED if the enum gap is judged immaterial while
  no ID is pending and the report-only policy is treated as already-documented
  current state rather than an open decision.

## Register-defect summary

- **REGISTER-1** (`_DEPENDENCIES.md` line 29): stale PRD_HASH_MISMATCH warning
  carrying superseded hashes; reconciled to MATCH by D-APP-38 / live tree.
  Disposition REMAINING_STATE_MISMATCH.
- No defect emitted for the Declared Upstream/Downstream "TBD" sections in
  `_DEPENDENCIES.md`: per the brief and docs/SPEC.md §5.2 these are human-owned
  declaration sections (TBD by design), distinct from the agent-owned Extracted
  register (25 rows, internally consistent, targets resolve to live sibling
  deliverables). Guidance CONFLICT-003 restates this by-design tension and remains
  an open human-ruling item (not a defect).
- `_REFERENCES.md` is internally consistent: all 7 refs recompute to MATCH against
  the live tree at 6f7c06814 (PRD verified directly).

## Cross-deliverable handles (no unmapped behavior on this surface)

DEL-09-02 owns validation glue only (section9 script/manifest, premerge wrapper,
release-quality wrapper). The runtime evidenceFiles each ID validates
(`src/lib/harness/**`) are owned by sibling deliverables per Dependencies.csv
DEP-09-02-014..025 (DEL-09-01 Section 8; DEL-03-01 engine; DEL-04-02/03 settings/
mapper; DEL-05-02/05 events/artifacts; DEL-06-01/03/04/06 permission/MCP/hooks;
DEL-08-04/05 subagent governance + child records). RQ-011's child-run-record/
artifact residual is owned by DEL-08-05, not here. No IMPLEMENTED_UNMAPPED rows
were warranted: all 16 live manifest IDs map under RQ-001 (inventory) plus their
specific RQ rows.

The DEL-09-04 packaged-SDK cross-handle noted in the brief does not touch
DEL-09-02: ADQ-14 (this deliverable's release-quality wrapper) explicitly scopes
out "packaged SDK subprocess proof refresh, which remains ADQ-15 scope"
(Evidence_ADQ-14 line 19), and DMG/packaging/signing to ADQ-15/ADQ-16.

## Method notes / deviations

- MR-3: behavioral ALIGNED rows cite GATE-TRANSCRIPT(W1@fac46e33f) (typecheck
  exit 0; Vitest 667 passed/4 skipped) plus named manifest testFiles; all 16
  manifest testFiles and 13 evidenceFiles were verified readable at 6f7c06814. No
  test suites were executed.
- MR-10: doc/manifest-structural rows (RQ-001, RQ-012..016, EXC-002/003, ACC-001,
  REGISTER-1) use RUN-INSPECTION@6f7c06814 and/or DOC-BASIS(D-APP-38) /
  Evidence_ADQ-14, not invented code tests.
- ADQ-14 evidence itself reports "13 Section 9 IDs" (line 51), predating the growth
  to 16; treated as a dated evidence record, not current truth (plan §1).
- No secrets or key values were copied into any cell (PKG-09 discipline).
