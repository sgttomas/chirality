# DEL-10-01 concordance notes (R2 Wave-6)

Deliverable: DEL-10-01 DomainEngineProfile Contract Draft (PKG-10).
Source state: frontend/ at `fac46e33f`, byte-identical through HEAD `1976b379d`
(re-verified this run: `git diff fac46e33f HEAD -- projects/chirality-app-dev/frontend`
empty). Kit/register/docs surfaces read at HEAD `1976b379d`. No test suite executed;
behavioral bindings cite GATE-TRANSCRIPT(W1@fac46e33f).

## Census

Total rows: 25 (11 REQUIREMENT, 4 EXCLUSION, 4 ACCEPTANCE, 2 IMPLEMENTED_UNMAPPED,
3 REMAINING_WORK, 1 REGISTER_DEFECT).

Disposition counts:
- ALIGNED 17 (REQ-001, REQ-003..REQ-011, EXC-001..EXC-004, REMAINING-1..3)
- STALE_SPECIFICATION 4 (REQ-002, ACC-001, ACC-003, ACC-004)
- STALE_ASSESSMENT 1 (ACC-002)
- IMPLEMENTED_UNDOCUMENTED 2 (UNMAPPED-1, UNMAPPED-2)
- REMAINING_STATE_MISMATCH 1 (REGISTER-1)

AssessmentEvidence tokens: STILL CURRENT 4, OVERTAKEN 8, NOT APPLICABLE 13.
SelectableUnderCurrentLoop: YES only on REMAINING-3 (the concordance bootstrap itself).

MR-9 applies to this deliverable: the Specification was rewritten to the canonical
REF-008 vocabulary by the D-APP-45 canon-conformance tranche (ruled 2026-07-02) AFTER
INSP-03 (2026-06-21 @0aea715f5). Old-REQnnn mappings are stated per row; old REQ005
(deterministic validation), REQ010 (descriptor shape), and REQ011 (manifestRules) have
no direct current-claim counterpart ("no direct conclusion").

R1 REQUIREMENT_INDEX parser gap: does NOT apply here — the index carries all 11
DEL-10-01 REQ IDs; the claim set was still re-derived from Specification.md directly
and matches (11 REQ rows).

## Least-confident rows (mandatory self-flagging)

1. **REQ-002 (STALE_SPECIFICATION, MEDIUM).** Alternative reading that would flip it
   to ALIGNED: "not current implementation" can be read as "no domain-engine
   integration / live-binding claim", which the ruled tool surface itself affirms
   (registry and proposal-tool result semantics disclaim live binding and verdicts;
   D-APP-51/52 wording). Under that reading the kit statement remains true and only
   the corpus lag (SPEC §18 / TYPES §11 forward note) needs a packet. I coded
   STALE_SPECIFICATION because the kit words are class-specific ("source types, MCP
   tools") and those exact classes are now ruled-live — the W5-settled rule that a
   ruling permitting the adjacent surface does not accept the kit-text divergence.
2. **EXC-001 (ALIGNED, MEDIUM).** Alternative reading: the exclusion restates the
   product-level non-implementation claim, in which case it should be
   STALE_SPECIFICATION like ACC-001 rather than a deliverable-scope claim. I read
   "Out of scope [of this deliverable]" as scoping the deliverable's own work, which
   remains true; the product-level wording defect is carried at REQ-002/ACC-001 so
   the defect is not lost either way.
3. **ACC-002 (STALE_ASSESSMENT, MEDIUM).** Alternative reading: the row's kit claim
   (sequencing condition) is simply ALIGNED and the INSP-03 staleness belongs only in
   AssessmentEvidence columns across rows, leaving no STALE_ASSESSMENT disposition for
   this deliverable. I coded STALE_ASSESSMENT here because the assessment's Gap 1
   (doc-only acceptance basis unresolved) is the acceptance-basis counterpart of this
   condition, live surfaces agree with reality (D-APP-37 ruled the basis; D-APP-53
   closed the register; REF hashes MATCH), the file carries no superseding note
   (W3-settled test), and MR-1 wants the overtaken-conclusion defect coded where it is
   operative.
4. **ACC-003 (STALE_SPECIFICATION, MEDIUM).** Alternative reading: Datasheet line 29
   states a rule ("TBD **until** governed amendment"), and governed amendments did the
   supplying, so there is no divergence — ALIGNED with a note. I coded stale because
   Guidance line 73 makes a flat current-state assertion ("the ADOPTED profile's own
   hook fields still read TBD") that is false against the cited profile's live bytes
   (open_pipe_stress.yaml lines 83/90/117 carry concrete schema refs).
5. **UNMAPPED-2 (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** Alternative reading: the
   registry belongs to DEL-10-04's subject (profile validation/fixture posture) and a
   sibling W6 row may claim it, which would make this a cross-deliverable handle
   rather than an unmapped surface. Decomposition v3.2 assigns no code surface to any
   PKG-10 deliverable (all doc drafts), so I kept the row; R3 should dedupe against
   sibling PKG-10 claims.

## Register-defect summary

- REGISTER-1: `_REFERENCES.md` REF-007/REF-008 use machine-absolute paths
  (`/Users/ryan/ai-env/projects/chirality/agents/...`) — known run-wide class; joins
  that R5 tranche. All eight reference hashes were recomputed this run and MATCH
  (including REF-006 docs/PRD.md — the INSP-03 HASH_MISMATCH caveat is obsolete).
- Not coded as defects: `_DEPENDENCIES.md` Declared Upstream/Downstream "TBD — no
  accepted dependency edges have been extracted yet" (human-owned declaration
  sections, TBD by design per docs/SPEC.md §5.2; the sentence is also defensible —
  zero EXECUTION edges exist and the 3 ANCHOR rows are not deliverable-to-deliverable
  edges). Dependencies.csv (3 rows, SATISFIED per D-APP-53) and the `_DEPENDENCIES.md`
  lifecycle summary are internally consistent and agree with the live tree
  (decomposition anchors re-verified at §7 line 270, §8 line 371, §5 lines 224-225,
  §9 lines 448-449).

## F-APP-3 notes

No other project's execution tree was read. Cross-project facts used:
- The stage gate on REMAINING-2 (piping DEC-064 / TP-RUNNER-014) was judged
  unsatisfied from this project's own pinned surface (tool-descriptor.ts lines
  711-738 gateReason at fac46e33f), not from any piping surface — no UNKNOWN cell
  was needed.
- ACC-003 takes the existence of the piping-published schema refs from the shared
  root-level profile `_DomainEngines/profiles/open_pipe_stress.yaml` (a surface this
  kit's Guidance explicitly cites); the schema files themselves were NOT opened in
  the piping tree. Row text records this.
No UNKNOWN cells were written.

## Method deviations

None. One convention note: doc-only verification bases cite RUN-INSPECTION@1976b379d
(HEAD, where kit/docs/registers live) while frontend-source inspection cites
RUN-INSPECTION@fac46e33f (the reviewed frontend state, byte-identical through HEAD) —
same convention as the W4/W5 waves.
