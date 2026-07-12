# DEL-10-03 concordance notes — R2 Wave 6 (PKG-10)

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: frontend/ at
`fac46e33f` (byte-identical through HEAD `1976b379d` = main); doc/register
inspection at `1976b379d`. Method: pinned plan §§6–7 @ 551f84ef6 +
R2_METHOD_ADDENDUM MR-1..MR-11.

## Census

21 rows.

By ClaimType:
- REQUIREMENT: 10 (REQ-10-03-001..010)
- EXCLUSION: 3
- ACCEPTANCE: 2
- IMPLEMENTED_UNMAPPED: 1
- REMAINING_WORK: 4
- REGISTER_DEFECT: 1

By Disposition:
- ALIGNED: 12
- STALE_SPECIFICATION: 4 (REQ-10-03-007, REQ-10-03-010, DEL-10-03-EXC-002, DEL-10-03-ACC-002)
- STALE_ASSESSMENT: 3 (REQ-10-03-003, REQ-10-03-004, REQ-10-03-005)
- IMPLEMENTED_UNDOCUMENTED: 1 (UNMAPPED-1)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

HumanDecisionNeeded: NEW-PACKET on UNMAPPED-1 (tool-surface ownership/mapping)
and REMAINING-1 (the already-recorded owner call on whether D-APP-50/51/52
constitute the accepted amendment — no register row exists for that decision
itself).

## R1 parser gap (recorded per brief)

`REQUIREMENT_INDEX.csv` line 597 carries a single mangled row `DEL-10-03,REQ-10`
for this deliverable. The live Specification.md defines ten requirements
REQ-10-03-001..010 (lines 15–24); the claim set above was re-derived from the
Specification directly. Known parser gap, not absence of requirements.

## Least-confident rows (self-flagged, with the reading that would flip them)

1. **DEL-10-03-EXC-002 (STALE_SPECIFICATION, MEDIUM).** Alternative reading:
   the Scope exclusion describes only what this deliverable's four-document
   kit contains (record shape + workflow contract), and the D-APP-49/50/52
   tranches executed outside the kit under their own rulings — under that
   reading the exclusion is still literally true of the kit and the row is
   ALIGNED (or at most a wording nit). I coded STALE_SPECIFICATION because the
   exclusion's clause "remain future amendment or sibling-deliverable scope"
   is a state assertion now false (the tools are ruled-live, and this
   deliverable's own register rows DEP-10-03-007/-008 and Remaining item 2
   claim that surface as DEL-10-03 evidence/work), and no ruling accepts the
   kit-wording divergence itself (W5 DEL-01-04 ACC-002 pattern).
2. **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** Alternative reading:
   D-APP-50/52 rulings plus _STATUS.md Remaining item 2 already constitute an
   accepted mapping of the proposal-tool surface to DEL-10-03, making the row
   a transcription lag (the EXC-002 staleness) rather than an unmapped
   implementation — in which case UNMAPPED-1 collapses into EXC-002 and the
   NEW-PACKET is unnecessary. I kept the row because decomposition v3.2
   assigns the surface to no deliverable and no kit requirement states it
   (plan §7: live behavior without an accepted mapping); checked sibling
   assignments (DEL-10-01/02/04/05 rows, decomposition lines 367–375) before
   asserting no accepted mapping.
3. **REQ-10-03-004 (STALE_ASSESSMENT, MEDIUM).** Alternative reading: the
   INSP-03 "acceptance evidence format is TBD" conclusion is still partially
   current because the concrete acceptance-record artifact schema remains TBD
   (Procedure.md line 82) — that reading yields ALIGNED with AssessmentEvidence
   STILL CURRENT. I coded OVERTAKEN/STALE_ASSESSMENT on the D-APP-53
   DEP-10-03-008 closure basis (gate format defined: K-AUTH-2 SHA-bound human
   approval record), which distinguishes format (defined) from artifact schema
   (TBD by design under REQ-10-03-010).
4. **REQ-10-03-003 (STALE_ASSESSMENT, MEDIUM).** Alternative reading: "no
   actual proposal record store or workflow exists" is still true app-dev-side
   (no store; pec workflow is engine-side over the loopback transport), which
   would make the assessment STILL CURRENT and the row ALIGNED. I coded
   OVERTAKEN because a live, ruled proposal workflow (propose/refresh/validate)
   now exists and the PARTIAL is readable as current truth without any
   superseding note (W3 superseding-note test).
5. **REQ-10-03-010 (STALE_SPECIFICATION, MEDIUM).** Alternative reading:
   "concrete `DomainEngineProfile` instance for the target engine: TBD" can be
   read generically (any future proposal's target engine supplies its own
   profile), in which case the TBD is still valid design language and the row
   is ALIGNED. I coded stale because the tier-0 target-engine instance is
   ADOPTED and registered, and the Datasheet's own Conditions row (line 44)
   already records that resolution — the Specification's Documentation ledger
   lags its own Datasheet.
6. **REMAINING-2 SelectableUnderCurrentLoop = UNKNOWN.** F-APP-3 cell: the
   stage gate is piping-side transport soundness; no pinned app-dev surface
   states its current status and the piping execution tree is fenced. If an
   own-project surface I missed states soundness, the cell becomes YES/NO
   accordingly.

## Register-defect summary

- REGISTER-1: `_REFERENCES.md` REF-007/REF-008 Path cells are machine-absolute
  (`/Users/ryan/ai-env/projects/chirality/agents/...`). Hashes verified MATCH
  by live recomputation of all eight rows this run. Joins the run-wide
  machine-absolute-REF-path R5 tranche class.
- Considered and NOT coded: the `_DEPENDENCIES.md` 2026-05-20
  `HASH_MISMATCH_SOURCE` run note (line 28) — unlike the PKG-09 cases, this
  register carries a dated 2026-07-10 correction in the same file (Run Notes
  D-APP-53 entry and Run History row "REF-006 now MATCH"), so the historical
  warning does not read as current truth. The Declared Upstream/Downstream
  "TBD" sections are human-owned TBD by design (docs/SPEC.md §5.2) and were
  not coded; the false extraction-era mirror wording in Datasheet/Procedure is
  coded at DEL-10-03-ACC-002 instead.
- Dependencies.csv (8 rows) re-verified against the live tree: anchors live at
  decomposition lines 270/227/451/373; -005 ADOPTED profile + registry
  confirmed; -006 sibling DEL-10-02 kit present; -007 validator + proposal
  tools + published schemas confirmed (schema files existence-checked only);
  -008 operation-proposal.ts gate field/doc lines confirmed (field at line 77,
  gate doc at lines 19-24). No internal CSV/`_DEPENDENCIES.md` inconsistency
  found beyond REGISTER-1.

## Method notes / deviations

- F-APP-3: no other project's execution tree was read. The two
  `projects/chirality-piping/schemas/*.json` refs cited by this kit were
  verified by file-existence check only (no content read). Root-level
  `_DomainEngines/profiles/open_pipe_stress.yaml` (explicitly cited by the
  kit) was read as a shared contract surface, including its git history to
  date the hook-binding tier-0 CHANGE (`d70d8df92`, 2026-07-02) — that commit
  is a root-governance act cited as context, not an app-dev register decision.
- MR-9 old-ID mapping: INSP-03 used REQ001..REQ011; mappings stated per row
  (REQ001→001, REQ002→002, REQ003→003, REQ004+REQ009→004, REQ005→006,
  REQ006→008, REQ007→009, REQ008→005, REQ010→007, REQ011→010). INSP-03's Gap
  Inventory items are all overtaken (status-history repaired under D-APP-37;
  REF-006 MATCH under D-APP-35/38; dependency closure executed under
  D-APP-53); the assessment carries no superseding note, so the R5
  supersede/annotate tranche prescribed on the STALE_ASSESSMENT rows should
  cover the Gap Inventory and Source-State Caveat as well.
- No secrets or key values copied into any cell; credential-handling evidence
  cited by test line ranges only.
