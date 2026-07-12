# DEL-06-03 concordance notes — Initial Chirality MCP Read Tools (PKG-06, W2)

Source state: `fac46e33f` (frontend byte-identical to `4c8ed8907`/`61d70bdb0`;
GATE-TRANSCRIPT(W1@fac46e33f): typecheck exit 0, Vitest 667 passed/4 skipped).

## Census

Total rows: 23.

By ClaimType: REQUIREMENT=15, EXCLUSION=5, ACCEPTANCE=1, REMAINING_WORK=1,
REGISTER_DEFECT=1.

By Disposition: ALIGNED=20, ACCEPTED_DIVERGENCE=1 (EXC-005),
STALE_SPECIFICATION=1 (ACC-001), REMAINING_STATE_MISMATCH=1 (REGISTER-1).

SelectableUnderCurrentLoop=YES on REMAINING-1 only (UNGATED, this run); all
other rows NO per MR-2.

## R1 index gap (recorded per dispatch)

REQUIREMENT_INDEX.csv carries only a single generic `DEL-06-03,REQ-06` row —
the known regex-parser gap. IMPLEMENTATION_SURFACES.csv and VERIFICATION_INDEX.csv
have zero DEL-06-03 rows. The real 15-requirement set (REQ-06-03-001..015) plus
5 exclusions and 1 datasheet-distinct acceptance condition were re-derived from
`Specification.md` lines 23-74 and `Datasheet.md`. Assessment and remaining
indices resolved correctly (ASSESSMENT_INDEX row present; REMAINING_INVENTORY
row 34 = the concordance bootstrap, UNGATED).

## Structural finding: descriptor surface relocated under D-APP-48

The INSP-03 assessment (2026-06-21, SHA `09c840be2`) cited
`frontend/src/lib/harness/tool-descriptor.ts` and `.../mcp/tool-names.ts`. Both
files no longer exist at `src/lib/harness/`; their content was extracted verbatim
into the SHA-pinned `@chirality/harness-contract` package
(`frontend/packages/harness-contract/src/tool-descriptor.ts`,
`.../src/mcp/tool-names.ts`) per the D-APP-48 intra-repo pull ruling. The four
read tools and their behavior are unchanged, so all 15 REQ conclusions remain
substantively PASS (AssessmentEvidence token STILL CURRENT). Every REQ row's
ImplementationEvidence was re-anchored to the current package/file line ranges;
the assessment's own path anchors are now dead links (evidence-pointer staleness,
not a conclusion reversal — see least-confident item 3).

## MR-4 handling

Datasheet Conditions/Attributes were folded into the covering REQ rows
(permission mode -> REQ-009, deny/allowedTools -> REQ-008, status/dep truth ->
REQ-011/012, scaffold posture -> REQ-003, MCP namespace -> REQ-001). Only the
source-state hash-warning condition (Datasheet line 41) is datasheet-distinct
and became ACC-001.

## Co-location captured under exclusions (no IMPLEMENTED_UNMAPPED emitted)

The mutating tools (`status_transition`, `deps_write`) and the D-APP-50/51/52
domain read tools now live in the same `read-tools.ts` / harness-contract
descriptor surface that DEL-06-03 introduces. Because they are mapped elsewhere
by ruling (adjacent write/lifecycle deliverables; PKG-10 F3 lane and the pec
bridge lane), they are NOT truly unmapped — they are captured as honored/diverged
exclusions (EXC-001 write tools = ALIGNED via permission-class + mode gating;
EXC-005 domain tools = ACCEPTED_DIVERGENCE under D-APP-50/51/52) rather than as
IMPLEMENTED_UNMAPPED rows, to avoid double-counting behavior that has an owner.
Flagged for R3 surface-ownership synthesis.

## Register-defect summary (REGISTER-1)

`_DEPENDENCIES.md` Lifecycle Summary declares SATISFIED=4 / TBD=5 and lists
`DEP-06-03-005` among Open dependency closure items, but the live
`Dependencies.csv` shows `DEP-06-03-005` = SATISFIED (LastSeen 2026-06-21), i.e.
SATISFIED=5 / TBD=4. The same `_DEPENDENCIES.md` file's ADQ-11 reconciliation
note (lines 20-25, 36) already states 005 is SATISFIED, so the summary table and
open-items list simply lag the ADQ-11/D-APP-43 flip. Disposition
REMAINING_STATE_MISMATCH; repair is an R5 register-metadata edit. No other
internal inconsistency found in Dependencies.csv (9 rows, parent-anchor PASS),
`_DEPENDENCIES.md` (row count 9 agrees), or `_REFERENCES.md` (all 7 refs MATCH;
REF-006 PRD hash live-reverified = ExpectedSHA256).

## Least-confident rows (self-flagged for fan-in recheck; plus all non-ALIGNED rows)

1. **REQ-06-03-005 (deterministic construction), ALIGNED / MEDIUM.** Alternative
   reading that would flip it: REQ-005 demands determinism across the full
   session/persona/mode/option/SDK-version/MCP-server/permission tuple, and the
   Specification (line 59) proposes snapshot/table-driven proof. Current evidence
   is type constraints + registry-parity + alias tests, not a single full-tuple
   ordering snapshot. A reviewer holding the spec to a literal full-tuple snapshot
   could downgrade to PARTIALLY_IMPLEMENTED.
2. **EXC-06-03-005 (domain-engine ops), ACCEPTED_DIVERGENCE / MEDIUM.**
   Alternative reading: if the co-located domain read tools are judged to breach
   DEL-06-03's line-21 "domain-engine operations" exclusion rather than being
   cleanly owned by D-APP-50/51/52, the row flips to STALE_SPECIFICATION (the
   exclusion wording is now false for the read surface) or IMPLEMENTED_UNDOCUMENTED.
   I read D-APP-51 (which explicitly edited `read-tools.ts`) plus D-APP-50/52 as
   ruled, bounded co-location owned outside DEL-06-03 -> ACCEPTED_DIVERGENCE.
3. **AssessmentEvidence token on the 15 REQ rows (STILL CURRENT vs OVERTAKEN).**
   Representative row: REQ-06-03-001. The assessment's PASS conclusions still hold
   behaviorally, but its file/line evidence anchors are dead after the D-APP-48
   relocation. I treated conclusion-currency (STILL CURRENT) as distinct from
   pointer-staleness. Alternative reading: if a reviewer treats relocated evidence
   pointers as "overtaken," the token flips to OVERTAKEN across all 15 REQ rows and
   a STALE_VERIFICATION angle on the assessment's anchors could be argued (no live
   disposition change — the requirements still pass at fac46e33f).
4. **ACC-06-03-001 as an ACCEPTANCE row.** Alternative reading: the PRD hash
   warning could be folded into a REF/REQ row or omitted since REQ rows cite
   corroborating non-PRD sources. I kept it as the one datasheet-distinct
   acceptance condition (mirrors the R0 DEL-02-01 ACC-001 pattern) and marked it
   STALE_SPECIFICATION because the kit still asserts the now-false HASH_MISMATCH.

## Method deviations

None. 19-column §6 header verbatim from the R0 exemplar; MR-1..MR-11 applied;
MR-10 vocabulary used for doc/scope rows; no tests executed; read-only discovery.
