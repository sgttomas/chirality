# DEL-06-04 concordance notes — Write/Edit Surface and Path Hooks (PKG-06, W2)

Source state: `fac46e33f` (frontend byte-identical through HEAD `1625b396a` and to
`4c8ed8907`; GATE-TRANSCRIPT(W1@fac46e33f): typecheck exit 0, Vitest 667 passed/4 skipped).
No tests executed; read-only discovery.

## Census

Total rows: 22.

By ClaimType: REQUIREMENT=16, EXCLUSION=5, REMAINING_WORK=1.

By Disposition: ALIGNED=21, STALE_SPECIFICATION=1 (REQ-016).

SelectableUnderCurrentLoop=YES on REMAINING-1 only (UNGATED, this run); all other
rows NO per MR-2.

## R1 index note

REQUIREMENT_INDEX.csv carried all 16 real IDs (DEL-06-04-REQ-001..016) plus four
stray bare `REQ-00x` rows — no parser gap for this deliverable (unlike sibling
DEL-06-03). IMPLEMENTATION_SURFACES.csv, VERIFICATION_INDEX.csv, and DECISION_INDEX.csv
have zero DEL-06-04 rows; the surfaces/tests were re-derived from Specification.md
lines 31-46, the Verification/Documentation tables, and the INSP-03 assessment,
then re-anchored to current line ranges. ASSESSMENT_INDEX row present (2026-06-21,
SHA 09c840be2). REMAINING_INVENTORY row = the concordance bootstrap, UNGATED.

## MR-4 handling (Datasheet folded into REQ rows)

Datasheet Attributes/Conditions were folded: PreToolUse gate -> REQ-001; path
containment -> REQ-002; instruction-root -> REQ-003; symlink -> REQ-004; exact edit
precondition -> REQ-005; hook-failure fail-closed -> REQ-006; deny precedence ->
REQ-007; mode dependency -> REQ-009; MCP parity / current MCP write surface ->
REQ-010; provenance obligation -> REQ-011/013. The only datasheet-distinct
condition — the PRD REF-006 HASH_MISMATCH source-state warning (Datasheet line 37) —
is already the subject of a first-class requirement (REQ-016), so NO separate
ACCEPTANCE row was emitted (avoids double-counting; differs from DEL-06-03, whose
hash warning had no covering REQ and so became ACC-001).

## Structural finding: descriptor surface relocated under D-APP-48

The INSP-03 assessment cited `frontend/src/lib/harness/tool-descriptor.ts` (REQ-009,
lines 987-1062). That file no longer exists at `src/lib/harness/`; its content was
pulled verbatim into the SHA-pinned `@chirality/harness-contract` package
(`frontend/packages/harness-contract/src/tool-descriptor.ts`) per the D-APP-48
intra-repo ruling — the same relocation DEL-06-03's ledger documented. Behavior is
unchanged, so REQ-009 stays ALIGNED with AssessmentEvidence token STILL CURRENT;
the dead path is flagged for an R5 evidence-pointer refresh (not a conclusion
reversal). chirality-hooks.ts also grew (subagent/shell branches added) so most
assessment line anchors shifted; every REQ row re-anchored to current lines.

## Cross-reference: mutating MCP tool ownership resolved (dispatch item)

DEL-06-03's ledger flagged `mcp__chirality__status_transition` and
`mcp__chirality__deps_write` as co-located on the read-tools surface but owned
"elsewhere by ruling." This spec DOES own them: Specification.md REQ-010 and
Datasheet.md lines 40-41 name both as the current MCP write/gated surface and
require SDK-parity gating. Live code confirms ownership here —
`runMutatingMcpToolWithEvidence` / `assertMutatingMcpPermission`
(read-tools.ts lines 263-411) run path policy + permission decision + evidence
before every status/dependency mutation (chirality-mutating-mcp.test.ts lines
120-309). So the boundary is clean: DEL-06-03 owns the read surface they sit on,
DEL-06-04 owns their write/parity governance. Flagged for R3 surface-ownership
synthesis only as confirmation, not conflict.

## Cross-package boundary: path guards (DEL-05-01 / DEL-07-01)

Dispatch asked whether my path-hook scope covers the DEL-05-01 session-manager
`assertSafeSessionId` / `assertProjectRootAccessible` guards. It does not: those are
session-id/project-root-access guards on a different surface (session management,
PKG-03/PKG-05). DEL-06-04's path hooks are write-path containment
(`tool-path-policy.ts`) plus the instruction-root check, and the instruction-root
resolver itself is the DEL-07-01-owned surface consumed via `./instruction-root`
(DEP-06-04-008, INTERFACE, PENDING — legitimately open until DEL-07-01 closes it).
No claim overlap; no AUTHORITY_CONFLICT. Recorded in REQ-002/REQ-003 evidence.

## No IMPLEMENTED_UNMAPPED, no REGISTER_DEFECT

- IMPLEMENTED_UNMAPPED: none. The write hook module (chirality-hooks.ts) also routes
  shell and subagent descriptors, but those are honored exclusions (EXC-003 Bash ->
  DEL-06-05; subagent bridge -> DEL-06-01/executable-bridge) captured as exclusion
  rows rather than unmapped behavior, mirroring DEL-06-03's co-location discipline.
  All write/edit-specific behavior maps to REQ-001..016.
- REGISTER_DEFECT: none. Dependencies.csv (10 rows) and _DEPENDENCIES.md agree
  internally (ACTIVE=9, RETIRED=1, DEP-010 SATISFIED, DEP-007/008 PENDING,
  DEP-009 RETIRED); the DepClosure snapshot coverage row
  `DEL-06-04,Y,10,Y,Y` matches the live register; all 7 _REFERENCES.md refs MATCH
  with REF-006 (docs/PRD.md) hash live-reverified this run (recomputed sha256 ==
  ExpectedSHA256 ac35fba4...c30bfd). The DEP-06-04-010 row's Statement/EvidenceQuote
  retain the original HASH_MISMATCH extraction wording while Satisfaction=SATISFIED /
  Notes=MATCH — this is the normal claim-vs-current-status register pattern, not an
  internal inconsistency, so no MR-5 row.

## The one non-ALIGNED row (REQ-016, STALE_SPECIFICATION)

REQ-016 requires PRD-derived controlled-write behavior to stay warning-qualified
"until REF-006 source state is reconciled." REF-006 IS now reconciled (MATCH under
D-APP-38 corpus v6; hash live-reverified). The INSP-03 assessment already records
this (REQ016 PASS + Source-State Caveat), but the kit documents still flatly assert
HASH_MISMATCH: Datasheet.md line 37 and References line 66, Guidance.md "PRD Hash
Warning" (line 38), and the Specification.md REQ-016/standards wording. Per MR-8
(kit text asserting a now-false state -> STALE_SPECIFICATION). Repair is a
deliverable-local R5 doc edit (HumanDecisionNeeded=NO; D-APP-38 already ruled the
reconciliation — no new packet). AssessmentEvidence token STILL CURRENT because the
assessment's conclusion is correct; the staleness is in the four-doc kit.

## Least-confident rows (self-flagged for fan-in recheck; plus the non-ALIGNED REQ-016)

1. **REQ-010 (MCP parity), ALIGNED / MEDIUM.** Alternative reading that would flip
   it: the spec/guidance still frame `mcp__chirality__scaffold` as "gated, must be
   classified before mutation," implying an open write-classification. The live
   surface exposes only read-only `scaffold_preview` (permissions ['read'] in the
   descriptor; "without writing files"), so I read the classification as SETTLED to
   preview-only and REQ-010's parity requirement as met by status_transition/deps_write.
   A reviewer treating the unresolved kit wording as an implementation gap could
   downgrade to PARTIALLY_IMPLEMENTED or call the scaffold wording IMPLEMENTED_DIFFERENTLY.
   I left it ALIGNED with an R5 doc-refresh note.
2. **REQ-009 (mode mapping), ALIGNED / MEDIUM.** Alternative reading: the assessment's
   sole descriptor evidence pointer (src/lib/harness/tool-descriptor.ts 987-1062) is a
   dead link after D-APP-48. I treated conclusion-currency (STILL CURRENT, behavior
   verified via permission-overlay + sdk-options-builder + relocated descriptor) as
   distinct from pointer staleness. A reviewer treating the relocated pointer as
   "overtaken" would flip the AssessmentEvidence token to OVERTAKEN (no live
   disposition change — readOnly-deny/workspaceWrite-after-gates still holds at fac46e33f).
3. **REQ-016 (STALE_SPECIFICATION), HIGH.** Alternative reading: because REQ-016 is a
   conditional ("keep warning UNTIL reconciled") and the warning WAS kept until
   reconciliation, one could call the requirement itself ALIGNED and treat the residual
   HASH_MISMATCH text as merely a pending doc-refresh residual (RemainingWork on an
   ALIGNED row). I chose STALE_SPECIFICATION because multiple kit surfaces now assert a
   now-false source state as current truth (MR-8 repair-shaped), matching the R0
   DEL-02-01 ACC-001 and sibling DEL-06-03 ACC-001 precedent.
4. **EXC-005 (domain-engine protected-path), ALIGNED / MEDIUM.** Alternative reading:
   if the co-located D-APP-52 pec proposal tools were judged to import protected-path
   operation semantics onto this deliverable's surface, the exclusion wording would be
   partly false (STALE_SPECIFICATION) or the behavior IMPLEMENTED_UNMAPPED. I read the
   pec tools as read-only/loopback evidence owned in the PKG-10/pec lane (per D-APP-52
   and the DEL-06-03 ledger), with no protected-path operation logic in tool-path-policy.ts
   -> exclusion honored, ALIGNED.

## Method deviations

None. 19-column §6 header verbatim from the R0 exemplar; MR-1..MR-11 applied; MR-10
vocabulary (DOC-BASIS, GATE-TRANSCRIPT) used for the doc-basis rows (REQ-015/016);
behavioral ALIGNED rows carry both implementation (file+line) and fac46e33f-bound
verification evidence; no tests executed; read-only discovery.
