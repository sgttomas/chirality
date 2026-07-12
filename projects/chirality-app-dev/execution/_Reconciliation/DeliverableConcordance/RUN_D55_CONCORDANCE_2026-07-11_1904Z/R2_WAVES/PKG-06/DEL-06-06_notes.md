# DEL-06-06 Hook Lifecycle and Compaction Mirror — R2 concordance notes

Run: RUN_D55_CONCORDANCE_2026-07-11_1904Z. Source state: frontend/ at fac46e33f
(byte-identical through HEAD 1625b396a). Read-only discovery.

## Census

Total rows: 22 (initially 23; REGISTER-1 withdrawn after fan-in verification —
see Fan-in reconciliation below).

By ClaimType:
- REQUIREMENT: 15 (REQ-001..015)
- EXCLUSION: 5 (EXC-001..005)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-1)
- REGISTER_DEFECT: 0
- REMAINING_WORK: 1 (REMAINING-1)

By Disposition:
- ALIGNED: 19
- STALE_SPECIFICATION: 2 (REQ-014, REQ-015)
- IMPLEMENTED_UNDOCUMENTED: 1 (UNMAPPED-1)

## Fan-in reconciliation (verifier verdicts, independently re-verified, accepted)

1. **REGISTER-1 withdrawn (REFUTED verdict accepted).** The original row read
   the `_DEPENDENCIES.md` Declared Upstream/Downstream "TBD - no accepted
   dependency edges have been extracted yet" prose as contradicting the 8-row
   Extracted Dependency Register. Re-verified against docs/SPEC.md §5.2 (lines
   ~288-297): `_DEPENDENCIES.md` is defined as a hybrid container whose
   human-owned Declared Upstream/Downstream sections are separate from the
   agent/tool-owned Extracted Dependency Register — a TBD human declaration
   coexisting with extracted rows is the designed state, and Datasheet.md line
   44 accurately describes the Declared sections. Row dropped; not contested.
   The coordinator notes this row-class recurs across PKG-03/04/05 wave outputs
   and goes to R3 harmonization regardless.
2. **REQ-005 factual correction applied.** The HarnessToolPermission union has
   SIX members — read|workspace-write|network|shell|subagent|danger
   (tool-descriptor.ts lines 28-35), not five as originally recorded.
   Re-verified directly against the source. Verdict unchanged (still no
   'domain' family).
3. **UNMAPPED-1 evidence corrected (row strengthened).** The original cell
   claimed indirect test coverage of the hook_progress mapping branch;
   re-verified grep of frontend/src/__tests__ at fac46e33f finds ZERO
   references to hook.progress or hook_progress — the branch is entirely
   untested. Cell corrected; disposition (IMPLEMENTED_UNDOCUMENTED) unchanged
   and now better supported.

## R1 parser-gap note

R1 REQUIREMENT_INDEX reports 15 regex-scanned IDs for DEL-06-06; the real claim
set was re-derived from Specification.md. All 15 REQ IDs (REQ-001..015) are
present and reconciled, plus 5 Out-of-scope EXCLUSION claims, 1 unmapped
category, and the single seeded REMAINING item. No parser zero-scan gap
applied here.

## Cross-cutting finding: implementation landed, four-doc kit not refreshed

DEL-06-06's implementation is fully present and behavior-verified, but the
four-document kit was authored in an anticipatory "path: TBD" style and never
updated post-implementation. All requirement obligations are satisfied at the
source state (19 ALIGNED requirement/exclusion rows); the staleness is confined
to (a) the HASH_MISMATCH warning wording (REQ-014) and (b) the blanket TBD
path placeholders in Specification Documentation/Datasheet Construction/
Procedure Records (REQ-015). Both are captured as STALE_SPECIFICATION repair
rows. The INSP-03 assessment (2026-06-21, SHA 09c840be) is actually *ahead* of
the kit — it enumerated the concrete paths and already recorded REF-006 MATCH —
so every REQ row carries `AssessmentEvidence = STILL CURRENT`, not
STALE_ASSESSMENT.

## Assessment path drift (noted, not defect-raised)

INSP-03 cited `frontend/src/lib/harness/event-schema.ts` (REQ-002/012) which has
since moved to `frontend/packages/harness-contract/src/event-schema.ts` under
the D-APP-48 harness-contract package pin; the emitted Chirality-owned type
names and HarnessEvent shape are unchanged. INSP-03 also attributed
`turn.interrupted` to sdk-message-mapper lines 800-835 (REQ-010) whereas the
interruption events are actually emitted by the SDK managers
(anthropic/claude-agent-sdk-manager.ts). Conclusions hold; only the anchors
drifted. These are recorded inline in the affected rows rather than as separate
STALE_VERIFICATION rows because the verification substance still binds.

## Cross-package boundary handling (per dispatch)

DEL-04-03's ledger owns the compaction / mirror-error EVENT MAPPING inside
sdk-message-mapper.ts. REQ-007/008 (context.compacted) and REQ-010 (terminal
outcome) therefore cite that shared surface as implementation evidence but flag
DEL-04-03 (compaction mapping) and DEL-03-04 (durable terminal ownership)
co-ownership in-cell, so the same lines are not claimed as DEL-06-06-exclusive.
DEL-06-06's own mapper surface is chirality-hooks.ts (governed-tool hook
callbacks) plus the adapter hook_* lifecycle branches of sdk-message-mapper.ts.

## Register-defect summary

No register defects stand after fan-in. The initially raised REGISTER-1
(Declared-vs-Extracted prose tension in `_DEPENDENCIES.md`) was refuted against
docs/SPEC.md §5.2 and withdrawn (see Fan-in reconciliation). `Dependencies.csv`
is internally consistent with the Extracted Dependency Register; DEP-06-06-008
SATISFIED agrees across both files, and the four still-PENDING execution edges
(DEL-05-02/06-04/03-04/09-02) are defensibly deferred to their owning
deliverables per the INSP-03 Dependency Closure Note, so no defect was raised
for the PENDING states.

`_REFERENCES.md` is internally consistent (all seven refs MATCH); the stale
HASH_MISMATCH text lives in the kit prose (REQ-014), not in the reference
register, so it is a STALE_SPECIFICATION requirement row rather than a
REGISTER_DEFECT.

## Least-confident rows (self-flagged for fan-in recheck)

1. **REQ-005 (ALIGNED, MEDIUM)** — Fail-closed is proven for write/shell/subagent
   (tested), but the requirement's literal "domain" family has no distinct
   `HarnessToolPermission` (enum is read|workspace-write|network|shell|subagent|danger,
   tool-descriptor.ts lines 28-35) and no named test asserts a domain
   fail-closed path. Alternative reading that would flip it:
   **PARTIALLY_IMPLEMENTED** if "domain" is intended as a first-class governed
   family requiring its own descriptor/fail-closed path rather than being
   subsumed under subagent/workspace-write routing of domain-engine tools.

2. **REQ-015 (STALE_SPECIFICATION, MEDIUM)** — Rated stale because concrete
   evidence paths now exist and the assessment identified them, so the kit's
   blanket TBD placeholders no longer describe reality. Alternative reading:
   **ALIGNED** if the requirement is read purely as a closure-review *obligation*
   ("evidence MUST identify paths ... unassigned remain TBD") that is discharged
   the moment the assessment supplies the paths, leaving the kit placeholders as
   a pure documentation-repair note rather than a spec-staleness disposition.

3. **UNMAPPED-1 hook.progress (IMPLEMENTED_UNDOCUMENTED, MEDIUM)** — hook.progress
   is registered (event-schema.ts line 26) and emitted (sdk-message-mapper.ts
   986-1001) but named by no requirement and covered by ZERO tests (verified
   grep of frontend/src/__tests__). Alternative reading: fold under REQ-004
   ("hook.started and hook.completed ... where hook execution evidence is
   available") as an incidental additional lifecycle category, not a separate
   unmapped surface — in which case it would collapse into the REQ-004 row rather
   than stand alone. Kept separate because REQ-004 enumerates a closed category
   list that omits it.

4. **REQ-010 (ALIGNED, MEDIUM)** — terminal-outcome events are split across
   sdk-message-mapper (completed/failed) and the SDK managers (interrupted);
   durable terminal ownership is DEL-03-04. Alternative reading: this is more
   properly a DEL-03-04/DEL-04-03 claim and DEL-06-06's REQ-010 is only the
   *finalization-to-terminal linkage*, which could be recorded as
   ACCEPTED_DIVERGENCE-style shared ownership rather than a standalone ALIGNED
   here. Rated ALIGNED because D-APP-43 explicitly accepts adapter result mapping
   as the Stop/finalization closure surface for this slice.

## Method deviations

None. Header copied verbatim from the R0 exemplar (19 columns). MR-1 tokens
present exactly once per row; MR-2 (Selectable=YES only on REMAINING-1); MR-3
behavioral rows cite GATE-TRANSCRIPT(W1@fac46e33f) plus named test files/lines;
MR-5 no register-defect rows stand after fan-in; MR-7 governance-vs-context
tagging applied to D-APP-43/40/38/48; MR-8 tie-break applied (flatly-false
HASH_MISMATCH wording -> STALE_SPECIFICATION); MR-10 vocabulary used for
doc-only rows.
