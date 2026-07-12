# DEL-10-05 concordance notes — R2 Wave 6 (PKG-10)

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: frontend/ at
`fac46e33f` (byte-identical through HEAD `1976b379d` = main per the W6
dispatch); documents and registers read at `1976b379d`. Method: pinned plan
§§6–7 @ 551f84ef6 + R2_METHOD_ADDENDUM MR-1..MR-11. Discovery only; nothing
outside the two wave artifacts touched. F-APP-3 heightened fence observed: no
other project's execution tree was read; every cross-engine fact cites this
project's own surfaces (frontend source, decision register, this
deliverable's registers) — the `_DomainEngines/profiles/*.yaml` files were
not opened; the registry facts cited come from
`frontend/src/lib/harness/mcp/domain-profile-registry.ts` itself.

## Census

**15 rows total.**

By ClaimType:

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 8 |
| ACCEPTANCE | 4 |
| EXCLUSION | 1 |
| REMAINING_WORK | 1 |
| REGISTER_DEFECT | 1 |

By Disposition:

| Disposition | Rows |
|---|---:|
| ALIGNED | 11 |
| STALE_SPECIFICATION | 2 (REQ-007, ACC-001) |
| STALE_ASSESSMENT | 1 (REQ-004) |
| REMAINING_STATE_MISMATCH | 1 (REGISTER-1) |

HumanDecisionNeeded: NEW-PACKET on REQ-007 only (governed authority-doc
amendment to transcribe the D-APP-49..52 ruled staged-live posture into
`docs/SPEC.md` §18 / PRD KG-016 — same corpus-lag class the R0 exemplar
routed to NEW-PACKET; no register row exists for that amendment yet).

Requirement re-derivation: `REQUIREMENT_INDEX.csv` lines 610–617 carries
REQ-001..REQ-008 for DEL-10-05 (no parser gap); the re-derived set from
`Specification.md` lines 18–25 matches it exactly. MR-4 fold: Datasheet
Attributes rows (lines 22–29) restate the REQ set and were folded into REQ
rows; the four ACCEPTANCE rows carry only datasheet/kit-distinct conditions
(PRD hash warning, adoption gate, OperationProposal schema-citation
condition, DomainEngineProfile schema TBD). INSP-03 REQ001..REQ008 map 1:1 to
current REQ-001..008 (spec not rewritten since the assessment); MR-9
satisfied by stating the 1:1 mapping on each row.

## Enforcement-truth checks performed (PKG-10 / dispatch duty)

Boundary-notice and separation claims were checked on the live frontend, not
just the kit:

- **Solver-truth / no-verdict copy is live and test-pinned:**
  `domain-proposal-tools.ts` lines 101–102 (`PEC_PROPOSAL_RESULT_SEMANTICS`);
  `domain-profile-registry.ts` lines 45–46 (`NO_VERDICT_RESULT_SEMANTICS`);
  asserted by `domain-proposal-tools.test.ts` line 376 ("a green dry-run is
  NOT acceptance") and line 575 ("no domain verdict").
- **Human-gate separation is enforced, not just worded:** no
  accept/apply/force tool is registered (`tool-catalog.ts` lines 130–131;
  grep clean); `domain_proposal_validate` reaches no POST-capable method
  (test lines 541–580, packet rider 7); `domain_propose_operation` is
  permission-graded workspace-write with a K-DOMAIN-3 humanGate reason
  (`tool-descriptor.ts` lines 762–767; tests lines 250–318).
- **Contract-level notice fields exist:** `operation-proposal.ts` lines
  76–77 (`boundary_notice`, `required_human_gate` required fields) and lines
  20–23 (accepted/applied require a human approval record);
  `domain-profile.ts` lines 100–102/117–126 (professional_boundary block;
  protected vs agent-writable path fields distinct).
- **Prohibited-claim scan of live copy:** descriptors, catalog text, and
  envelope semantics strings grepped for approval / validation / compliance /
  certification / solver-truth claims — none present as Chirality claims.
- **No `/api/domain/*` endpoint exists** (SPEC §18 candidate families remain
  unimplemented); the only descriptor-only domain tool is
  `domain_headless_preview_run` (`tool-descriptor.ts` lines 737–738).

## Zero IMPLEMENTED_UNMAPPED rows — justification

The live boundary/solver-truth copy on the ruled tool surfaces is already
mapped: its content is governed by this deliverable's REQ-001..004 content
rules (and cited as evidence there), and ownership of the tool surface itself
is carried by sibling DEL-10-03's W6 row set (its UNMAPPED-1 covers the
proposal-tool surface ownership question). Per the W6 rule that a behavior
mapped to a sibling deliverable counts as an accepted mapping, no
IMPLEMENTED_UNMAPPED row is warranted here; cross-deliverable handle:
DEL-10-03 (proposal-tool surface), DEL-10-02 (protected-path policy),
DEL-10-04 (fixture/validation posture).

## Least-confident rows (mandatory self-flagging)

- **DEL-10-05-REQ-007 (STALE_SPECIFICATION, MEDIUM).** Coded stale because
  the kit (Spec line 24; Datasheet line 35) and its corpus sources flatly
  assert domain tools "must not be implemented as current-release scope" /
  "must not imply implementation is active," while D-APP-49..52 ruled a
  staged tool surface live (MR-11: rulings stand over untranscribed corpus
  wording; MR-8 first branch). Alternative reading that would flip it: read
  REQ-007 narrowly as a copy rule about *mentions* — every kit mention is
  indeed marked future/provisional, so the copy rule is satisfied and only
  the corpus/datasheet premise lags → ALIGNED with the lag carried on a
  NEW-PACKET RemainingWork. I kept STALE_SPECIFICATION because obeying the
  requirement's letter ("MUST NOT imply implementation is active") would now
  produce false copy for the ruled staged subset, which makes the
  requirement wording itself the defect.
- **DEL-10-05-REQ-004 (STALE_ASSESSMENT, MEDIUM).** INSP-03's PARTIAL premise
  "Operation surfaces and evidence format are future/TBD" is half-false
  (D-APP-52 landed live operation-proposal tools carrying the human-gate
  copy) and carries no superseding note. Alternative reading: the
  acceptance-*evidence format* half of the premise is still genuinely TBD
  (acceptance lives in pec, storage location unselected), so the row could be
  ALIGNED with AssessmentEvidence OVERTAKEN and only an annotation
  RemainingWork. I kept STALE_ASSESSMENT because the surface-existence half
  is the operative sentence a reader would take as current truth.
- **DEL-10-05-REQ-003 (ALIGNED, MEDIUM).** Kept ALIGNED with assessment
  STILL CURRENT: the "no accepted surface inventory" gap INSP-03 named
  persists, but the spec's own Verification row 7 TBD carve makes it a
  compliant open item, and the prohibition itself holds on every live ruled
  surface (checked). Flip reading: treat the kit's "selected surfaces are
  TBD until a future amendment" as overtaken by the ruled-live tool/event
  surfaces → STALE_SPECIFICATION (the DEL-10-03 EXC-002 pattern). I did not,
  because no ruling accepted those surfaces as *boundary-notice locations*
  for this deliverable's program — the TBD statement remains true in its own
  terms.
- **DEL-10-05-ACC-002 (ALIGNED, MEDIUM).** The adoption-gate condition
  ("future domain-engine work requires governed amendment") was exercised,
  not violated: each landed tranche has its own owner-ruled packet. Flip
  reading: "governed amendment" ≠ decision-register ruling, so the staged
  tranches happened outside the stated vehicle → STALE_SPECIFICATION on the
  gate wording. This is the same owner question DEL-10-03's REMAINING-1
  NEW-PACKET already carries (whether D-APP-50/51/52 constitute the accepted
  amendment); I did not duplicate the packet here.
- **DEL-10-05-ACC-004 (ALIGNED, MEDIUM).** Kit TBD is faithful to its cited
  source (PRD KG-017, still present at corpus v6). Flip reading: TYPES §11.1
  (RATIFIED) plus the D-APP-49 typed mirrors already constitute an accepted
  generic profile schema, making both KG-017 and the kit row stale. I kept
  ALIGNED because a ratified *vocabulary* section and inert source types are
  not the accepted generic profile *specification* KG-017 contemplates, and
  the corpus itself still carries KG-017.
- **DEL-10-05-EXC-001 (ALIGNED, MEDIUM).** The exclusion's plain subject
  (this deliverable implements nothing; operation execution/apply excluded)
  holds live. Flip reading: the trailing "PKG-10 remains future-boundary/
  gated scope" clause is a now-partially-false state assertion →
  STALE_SPECIFICATION (DEL-10-03 EXC-002 pattern). I kept ALIGNED and routed
  that clause's repair onto the REQ-007 row to avoid double-counting one
  wording defect across two rows.

## Register-defect summary

- **REGISTER-1 (REMAINING_STATE_MISMATCH, HIGH):** `_REFERENCES.md` REF-007
  uses the machine-absolute path
  `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md`
  (known run-wide class; same defect as sibling DEL-10-02/10-03 REGISTER-1
  rows). Content integrity holds — the repo-relative copy's SHA256
  reproduces both recorded hashes.
- **Considered and NOT coded (dated-note discipline, consistent with
  DEL-10-02):** (a) `_DEPENDENCIES.md` line 32 ends "`_STATUS.md` stays
  CHECKING (F-APP-4)" — true when the dated 2026-07-10 D-APP-53 note was
  written, overtaken next day by D-APP-54 (live state IN_PROGRESS); treated
  as historical evidence inside an explicitly dated annotation. (b)
  `Dependencies.csv` DEP-10-05-007/-008 Notes cite `docs/SPEC.md` SHA
  `2a63277a...` and `docs/TYPES.md` SHA `aed33a0f...` from the D-APP-53-era
  corpus; the live v6 `_REFERENCES.md` records (and I recomputed) `cbca612e...`
  and `bb4af418...`. The satisfaction basis (document present, Status MATCH)
  still holds at v6, and the SHAs sit inside dated reconciliation notes, so
  no defect row; flagged for the fan-in verifier in case the dated-note
  reading is judged too charitable.
- Register otherwise healthy: `_DEPENDENCIES.md` tables in sync with the CSV
  post-D53A (ACTIVE 10 / RETIRED 0; SATISFIED 10); all seven `_REFERENCES.md`
  hash pairs reproduce by direct recomputation at `1976b379d` (including the
  D-APP-53-repaired REF-006 PRD MATCH); Declared Upstream/Downstream TBD
  sections are by-design (docs/SPEC.md §5.2), not defects. One wording
  oddity noted, not coded: the Declared sections say "no accepted dependency
  edges have been *extracted* yet" while the same file's register lists 10
  extracted rows — read as "no *accepted* edges," which is true (all
  human-acceptance/maturity values remain TBD).

## F-APP-3 UNKNOWN cells

None written. No cell required another engine's or project's status beyond
what this project's own surfaces state; pec and open_pipe_stress facts cite
this repo's frontend source (registry/tool modules), the D-APP-49..52
register rows, and this deliverable's own registers. No fence reads occurred
(`projects/chirality-piping/execution/**` and `projects/pec/execution/**`
untouched; `_DomainEngines/**` not opened).

## Method deviations

None. MR-1: exactly one token per AssessmentEvidence cell (OVERTAKEN 5,
STILL CURRENT 7, NOT APPLICABLE 3). MR-2: Selectable derived only on REMAINING-1
(YES — ungated, this run is its execution); all other rows NO. MR-3/MR-10:
behavioral evidence binds to GATE-TRANSCRIPT(W1@fac46e33f) plus named test
files with line anchors; doc-only rows carry `documentary claim` plus exact
sections and RUN-INSPECTION / SNAPSHOT+LIVE-REVERIFY bases verbatim; no tests
executed, no dependencies installed. MR-5: bare `REGISTER-1` ClaimID. MR-6:
the sole Remaining item is UNGATED (verbatim; no suffix present). MR-7:
governs vs (context) distinguished on every LatestDecision. MR-11 applied on
REQ-007 (rulings stand over untranscribed corpus wording).
