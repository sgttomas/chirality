# DEL-06-02 R2 concordance notes

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A whole corpus).
Source state: `frontend/` at `fac46e33f` (byte-identical through HEAD `1625b396a`).
Method: pinned plan §§6-7 @ `551f84ef6` + R2_METHOD_ADDENDUM MR-1..MR-11.

## Census (post fan-in rework, 2026-07-11)

Total claim rows: 22 (excludes header).

By ClaimType:
- REQUIREMENT: 13 (REQ-001..013, re-derived from Specification.md; matches the 13 canonical IDs in R1 REQUIREMENT_INDEX — the 8 bare `REQ-00n` entries there are regex-parser duplicates of the same rows, not distinct claims)
- EXCLUSION: 5 (EXC-001..004; EXC-005 reworked from former UNMAPPED-2 at fan-in)
- ACCEPTANCE: 1 (ACC-001, PRD hash-mismatch condition)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-1 domain MCP roster)
- REMAINING_WORK: 1 (REMAINING-1 concordance bootstrap)
- REGISTER_DEFECT: 1 (REGISTER-2; REGISTER-1 withdrawn at fan-in — the ID gap is intentional, no renumbering)

By Disposition:
- ALIGNED: 19
- STALE_SPECIFICATION: 1 (ACC-001)
- ACCEPTED_DIVERGENCE: 1 (UNMAPPED-1)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-2, contested)

## Fan-in rework record (W2 verifier feedback; cited sources independently re-verified)

Verifier verdicts on 6 rechecked rows: 3 CONFIRMED (ACC-001, UNMAPPED-1 incl its
ACCEPTED_DIVERGENCE basis, REQ-005 — all unchanged), 2 REFUTED, 1 CONTESTED. I re-read every
cited source before editing.

1. **UNMAPPED-2 → DEL-06-02-EXC-005 (REFUTED verdict ACCEPTED).** Re-verified: DEL-06-04
   Specification.md REQ-010 (line 40) explicitly names `mcp__chirality__status_transition`
   and `mcp__chirality__deps_write` as DEL-06-04's owned write/gated MCP surface with
   SDK-parity gating, and DEL-06-04 Datasheet.md Conditions 'Current MCP write surface'
   (line 41) matches. An accepted intra-package mapping exists, so IMPLEMENTED_UNDOCUMENTED
   was wrong (this matched my own self-flagged alternative reading #2). Reworked as
   exclusion-style row DEL-06-02-EXC-005 (ALIGNED, HIGH), mirroring DEL-06-03's sibling
   treatment; the former NEW-PACKET ownership question is removed as answered intra-package.
2. **REGISTER-1 (REFUTED verdict ACCEPTED — row dropped).** Re-verified: app-dev docs/SPEC.md
   §5.2 (lines 289-297) defines `_DEPENDENCIES.md` as a hybrid container in which Declared
   Upstream/Downstream are human-owned declaration sections distinct from the agent-owned
   Extracted Dependency Register, and the root docs/SPEC.md template (lines 346, 349) confirms
   the human-owned placeholder convention. An empty/TBD Declared section beside 11 extracted
   rows is the designed state, not metadata lag; the defect row is withdrawn. Residual
   non-defect observation preserved for the R3 class-level harmonization: the boilerplate
   phrase "no accepted dependency edges have been extracted yet" is literally false in its
   "extracted" clause (11 edges were extracted) — a scaffold-template phrasing infelicity,
   not a register defect under SPEC §5.2. R3 context: PKG-03/04/05 verifiers CONFIRMED
   structurally identical rows in five sibling ledgers without consulting SPEC §5.2, so the
   defect class is contested between verifiers and goes to R3 for harmonization either way.
3. **REGISTER-2 (CONTESTED — KEPT with contest note; discovery agent's call per coordinator).**
   Confidence lowered MEDIUM→LOW; HumanDecisionNeeded set to NEW-PACKET; both readings now in
   the row. Reading A (mine): the single-row advance is internally inconsistent — only
   DEP-06-02-011 went SATISFIED while equally-MATCH REF-002/003/004/005 rows stayed TBD,
   regardless of whether TBD is a legitimate open state. Reading B (verifier alternative, per
   DEL-06-05 sibling treatment): TBD satisfaction is legitimate open acceptance state for
   IN_PROGRESS. The deciding fact — whether ADQ-11/D-APP-43's reconciliation scope obligated
   sibling-row review — is unresolved; keeping the row rather than silently resolving follows
   plan boundary 4. If R3/R4 rules Reading B, the row drops with no repair implied.

## Parser-gap / source-state notes

- R1 REQUIREMENT_INDEX for DEL-06-02 is NOT a zero-ID parser gap; it captured all 13
  canonical `DEL-06-02-REQ-0nn` IDs plus 8 bare `REQ-nnn` duplicates. I re-derived the
  claim set from Specification.md regardless (13 REQ rows).
- Material implementation relocation since INSP-03 (2026-06-21, SHA 09c840be2): the
  Assessment cites `frontend/src/lib/harness/tool-descriptor.ts` and
  `frontend/src/lib/harness/mcp/tool-names.ts`, which no longer exist at `fac46e33f`.
  The tool registry now lives in the D-APP-48-pinned package at
  `frontend/packages/harness-contract/src/tool-descriptor.ts` (+ `.../src/mcp/tool-names.ts`),
  and resolver logic split into `frontend/src/lib/harness/tool-pool.ts`. All 13 INSP-03
  PASS conclusions remain substantively true against the relocated surfaces (behavior
  verified via the still-present test files), so per MR-1 the REQ rows are ALIGNED with an
  AssessmentEvidence `STILL CURRENT` token that also records the pointer drift. This
  path drift is the single most systematic staleness in the kit; it is an evidence-pointer
  refresh (R5 doc repair), not a disposition flip.
- Reference integrity re-verified live this run by `shasum -a 256`: docs/PRD.md,
  CONTRACT.md, SPEC.md, TYPES.md all MATCH `_REFERENCES.md` recorded ActualSHA256. REF-006
  (PRD) is MATCH, confirming ACC-001's STALE_SPECIFICATION finding (the kit's pervasive
  HASH_MISMATCH warning tags are overtaken by D-APP-38 v6 / ADQ-11).

## Cross-package ownership check (brief dispatch item)

W2's DEL-04-02 ledger flagged the domain tool ROSTER as "DEL-06-02 / PKG-10 descriptor
deliverables and rulings D-APP-50/52." Checked my side: the domain MCP descriptors
(`domain_completeness_check`, `domain_rule_check_run`, `domain_headless_preview_run`
[descriptor-only park], `domain_propose_operation`, `domain_proposal_validate`) are physically
in the DEL-06-02-consumed registry (`harness-contract/src/tool-descriptor.ts` lines 661-877).
They are captured as UNMAPPED-1 with ACCEPTED_DIVERGENCE (MR-8: rulings D-APP-50/D-APP-52
acknowledge the bounded difference and keep unsound transport descriptor-only; not a
repair-shaped STALE row). Per F-APP-3 / MR-6 I read only this project's own pinned surfaces
(the descriptor `runtime.exposedToModel` flags and the D-APP-50/52 rulings, all app-dev) and
did not read chirality-piping's execution tree to judge pec transport soundness. No
cross-project gate suffix appears in DEL-06-02's `## Remaining`, so no RemainingGate UNKNOWN
was needed.

## Least-confident rows (as self-flagged at initial submission; fan-in outcomes annotated)

1. **UNMAPPED-1 (ACCEPTED_DIVERGENCE)** — Alternative reading: STALE_SPECIFICATION. The
   DEL-06-02 kit (Guidance.md line 83) still says treat `mcp__chirality__domain_*` as
   unsupported/TBD "unless accepted source updates authorize future domain tools." One could
   argue D-APP-50/52 are exactly those accepted updates and the kit wording is now flatly
   false (→ STALE_SPECIFICATION, repair-shaped). I chose ACCEPTED_DIVERGENCE because the
   rulings frame the exposure as a bounded, staged tranche (descriptor-only park for unsound
   transport) rather than a blanket adoption into DEL-06-02 scope, and the ownership question
   (DEL-06-02 vs a PKG-10 descriptor deliverable) is unresolved — a NEW-PACKET item for R3/R4,
   not a mechanical kit-text repair. If the fan-in verifier judges the Guidance wording
   "flatly false now," flip to STALE_SPECIFICATION. [Fan-in outcome: CONFIRMED as filed.]

2. **UNMAPPED-2 (IMPLEMENTED_UNDOCUMENTED)** — Alternative reading: exclusion-style/ALIGNED
   treatment (as DEL-06-03 did). [Fan-in outcome: REFUTED on this alternative's side —
   reworked as DEL-06-02-EXC-005; see Fan-in rework record item 1.]

3. **REGISTER-2 (REMAINING_STATE_MISMATCH)** — Alternative reading: not a defect; TBD
   satisfaction may be a deliberate FULL_GRAPH convention (closure not run at project level;
   `_DEPENDENCIES.md` line 85). The inconsistency I flag is narrower: only DEP-06-02-011
   (REF-006) was advanced to SATISFIED by ADQ-11 while its four sibling MATCH
   doc-prerequisite rows stayed TBD. [Fan-in outcome: CONTESTED — kept at LOW confidence with
   contest note; see Fan-in rework record item 3.]

4. **DEL-06-02-REQ-005 (ALIGNED, MEDIUM)** — Determinism across SDK-version and MCP-server-set
   variation (named in the requirement) is asserted only indirectly: fixtures vary tool input
   order while holding version/policy constant. Behavior is correct for what is tested; the
   requirement wording is broader than the fixtures. Not a disposition flip (implementation is
   deterministic by construction), but flagged as the weakest behavioral-evidence match.

## Register-defect summary (post fan-in)

- REGISTER-1: WITHDRAWN at fan-in. The "Declared Upstream/Downstream: TBD" narrative is a
  human-owned declaration section by design (app-dev docs/SPEC.md §5.2, lines 289-297;
  root SPEC template lines 346/349) — not metadata lag. Residual "extracted"-wording
  phrasing concern recorded in the Fan-in rework record for the R3 class-level harmonization.
- REGISTER-2: KEPT, CONTESTED (LOW confidence, NEW-PACKET). `Dependencies.csv` per-row
  SatisfactionStatus: only the REF-006 row was reconciled to SATISFIED (ADQ-11) while sibling
  MATCH doc prerequisites and implemented adjacent-deliverable edges stayed TBD. Competing
  reading (legitimate open acceptance state for IN_PROGRESS, per DEL-06-05 sibling treatment)
  recorded in the row; deciding fact is an R3/R4 question.

## Method deviations

None. 19-column header copied from the R0 exemplar; MR-1 (single AssessmentEvidence token),
MR-2 (Selectable only on REMAINING-1), MR-5 (bare `REGISTER-n` ClaimIDs), MR-7 (governs vs
context vs NONE_FOUND), MR-8 (STALE_SPECIFICATION vs ACCEPTED_DIVERGENCE tie-break), and MR-10
(verification-basis vocabulary) applied as written. No lifecycle transition, no deliverable-doc
edit, no test execution (GATE-TRANSCRIPT(W1@fac46e33f) is the behavioral binding).
