---
reviewer: A
lens: vertical-authority-trace
review_freeze_commit: da31c19b5656dd74615e308c4215688971d33dc9
manifest_sha256: 8ac8abb86f064a2a1ef5c51c4eacbbf7b90497d78d1f7a92b55406a44a27096c
charter_sha256: 1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f
date: 2026-07-26
finding_count: 26
---

# Section 1 — Independent orientation account

This account was formed from governed records only, before the charter was opened.
Basis verification: worktree HEAD equals the freeze commit
`da31c19b5656dd74615e308c4215688971d33dc9`; tracked tree clean (only the review
workspace untracked); `REVIEW_MANIFEST.json` and the charter file hash-verified
against the frontmatter values. All six primary accepted documents were
hash-verified: `docs/PRD_ROOT.md` `82f7ea2944e7…`, Root decomposition
`14067a7d97c9…`, App PRD `ef638f43ccae…`, App decomposition `952d3cbf81b0…`,
PEC PRD `de0a969cad15…`, PEC decomposition `3e5be4e453ed…`.

## Chirality Root

**Identity.** The repository-root product. Ruled genus (RD-1, two-level
formulation) carried in the adopted PRD and propagated to DIRECTIVE §1 and four
document self-descriptions through D-GOV-23/24.

**Accepted basis.** PRD Revision 5 adopted by D-GOV-22 (2026-07-25) against
candidate SHA `90fae458b…`; adopted bytes preserved at
`execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md`, with
`docs/PRD_ROOT.md` being a pointer block plus those exact bytes. The pointer
block carries the D-GOV-27 amendment-of-record superseding §5.2 O-1's
six-member instruction-surface enumeration by instrument (authoritative
enumeration: `docs/SPEC.md` §0.2.1, eight members). First root decomposition
v1.0 (6 packages / 45 deliverables / 103 scope items / 7 objectives) accepted
by D-GOV-25 against AcceptedCandidateSHA `ec62af070…`; all seven gates ruled
together by merge-and-proceed direction, verbatim ruling in the decision
record. I parsed all five companion registers programmatically: ledger 103
rows (94 IN / 9 OUT / 0 TBD), 45 deliverable rows, 7 objectives, forward
register 84 rows (83 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL — the ruled
OBJ-2 situated-working-root deferral, §12.1/OI-013), reverse register 51/51
TRACED. Every IN item maps to at least one deliverable; every item carries
exactly one PackageID; no dangling deliverable references.

**Acceptance provenance.** Exceptionally strong and explicit at the record
level: exact-candidate-SHA rulings, verbatim owner fences, distinct SHA roles
(AcceptedCandidateSHA / PublicationSHA / EffectiveSHA per E-3), and a
navigational register (`docs/governance_harness/_DECISIONS/_REGISTER.md`,
D-GOV-01..27) that defers to per-decision records. Two provenance defects
exist: D-GOV-27's EffectiveSHA is an unbound placeholder, and the
decomposition working surface's header assigns the "EffectiveSHA" label to a
different commit than the accepting instrument does (findings A-F-001,
A-F-002).

**Current state.** 45 ScopeOfWork.md contracts at INITIALIZED, all pinning
decomposition basis `653fabc9b…` (verified 45/45 by grep); ResponsibleParty
"Ryan Tufts" across the deliverable register and 45 `_CONTEXT.md` (verified);
guards G1–G4 registered/passing in `execution/_harness/root_guards.yaml`; all
six work-graph nodes `pending`. Navigation: `LOOP_INIT.md` →
`CURRENT_WORKPLAN.md` → `WORKPLAN_2026-07-25_root_initialization.md` (still
marked ACTIVE though its goal completed at PR #354/PR-2 merge) →
`LOOP_RECEIPTS.md` Receipt 52, which functions as the de-facto initialization
handoff; `HANDOFF_STATE.md` still carries the superseded Stage-2 PKG-00
consolidation arc.

## Chirality App

**Identity.** `projects/chirality-app-dev/`, a registered project loop
(`chirality.project.json`), not a domain engine. Product: the Chirality
desktop harness (Woven Dialogue IA per D-APP-74/SCA-APP-004).

**Accepted basis.** `docs/PRD.md` (no internal version; header date
2026-05-20; identity of record = its exact pin in AUTHORITY_CORPUS.json v17,
`ef638f43ccae…` — verified CLEAN against the live file, as were all six
project-doc pins and the two root `agents/` pins `ad849d9a…` and
`bb2df7178d…`). The PRD reflects accumulated D-APP rulings (through D-APP-74)
rather than a single adoption act, and carries two sections numbered "17".
Decomposition `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`: 78 scope items /
10 packages / 51 deliverables / 10 objectives; Gate Posture line: "Gates 1-7
accepted by implicit human approval per user instruction" (DEC-002); amended
in place by SCA-APP-001..004 (D-APP-72/73/74) topology-preserving. Its
required-or-deferred companion `contract_invariant_coverage_register.csv`
does not exist (the `_Decomposition/` directory holds only the working
surface) and I found no deferral ruling.

**Acceptance provenance.** Weakest of the three products at the decomposition
layer: no ruling record, no SHA-bound acceptance act, no gate-by-gate owner
text (contrast D-GOV-25 and D-PEC-60). The decision register (74 rows, all
RULED through D-APP-74; self-described "non-governing tracking surface")
provides dense per-tranche provenance for later changes, including verbatim
rulings and canonical ruling-text SHA-256 values from ~D-APP-57 onward.

**Current state.** 53 deliverables (51 decomposition + 2 PKG-00 control
deliverables), all `IN_PROGRESS` (verified census 53/53), none ISSUED
(F-APP-4 fences CHECKING→ISSUED). One orphan directory
`PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/`
containing only `Evidence/` sits outside the decomposition and duplicates the
PKG-03 number. Loop navigation: committed-HEAD workplan selection (D-APP-64)
→ `WORKPLAN_2026-07-18b_app_dev_loop.md` → Receipt 91 (daemon-as-service
tranche EXECUTED; "owner merge of the pull request is terminal" with no merge
SHA); the associated run handoff still reads
`APPDEV_DAEMON_SERVICE_IMPLEMENTATION_COMPLETE_PENDING_PR_AND_OWNER_MERGE`,
while git shows PR #333 merged at `612c35226`. SCA-APP-004 `_LATEST.md`:
`GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING`. The D-APP-48 pull contract's
12 pinned files are 12/12 DRIFT (verified by hash: all now deprecation shims
re-exporting `@chirality/runtime-contracts`). The project AGENTS.md overlay
carries frontmatter `status: draft`.

## PEC

**Identity.** `projects/pec/` — the optional coordination plane: a
deterministic, rebuildable projection of governed file truth plus ephemeral
presence; no governed act may require it (PEC-K-01).

**Accepted basis.** PRD v2.1 (`de0a969cad15…`): v2.0 adopted by D-PEC-58
(owner verbatim in §17 and the packet), directed-bootstrap clarification to
v2.1 by D-PEC-61. Invariants PEC-K-01..11; PRD expressly states nothing in it
is an implementation mandate. Decomposition `SOFTWARE_DECOMP.md` revision 1.2
(`status: current_basis`): rev 1.0 accepted at Gate 7 by verbatim owner
ruling ("I rule that this decomposition is now the accepted basis for
downstream work.", D-PEC-60); SCA-001/D-PEC-61 (FULL_GRAPH directed
bootstrap, +C16), SCA-002/D-PEC-64 (objective-mapping completion). Registers
parsed programmatically: ScopeLedger 94 rows (71 IN / 14 OUT / 9 TBD),
Deliverables.csv 64 rows across PKG-00..PKG-10, per-package counts matching
the working surface.

**Acceptance provenance.** Strong: per-gate verbatim owner confirmations in
the Gate Log; scope changes run through recorded SCA sessions with immutable
evidence under `execution/_ScopeChange/`; every implementation tranche fenced
behind its own D-PEC packet (F-PEC-1..4 per D-T0-15 in force).

**Current state.** 32 of 64 deliverables INITIALIZED with validated SOWs (all
32 SOWs pin `SOFTWARE_DECOMP.md@3623b958b`, i.e. rev 1.2 — verified); the
other 32 P2–P4 deliverables OPEN without SOWs by deliberate sequencing
(D-PEC-63 wave scope). Dependency state verified by parsing all 64 local
`Dependencies.csv`: 254 rows = 135 ANCHOR + 119 EXECUTION, zero waiver
sidecars, census 32/32 — exactly matching `_COORDINATION.md` item 9 (which
correctly supersedes item 8's pre-D-PEC-66 numbers). Latest receipt: 112.
Next owner gates: P1 build-slice packets, then WORKING_ITEMS ownership.

## Cross-product control surfaces

Tier-0 register `_DomainEngines/_DECISIONS/_REGISTER.md` read in full: 23
D-T0 rows, including D-T0-15 (F-PEC fences), D-T0-19 (bridge lane and
cross-loop D-APP minting grant), D-T0-23 (shared-runtime convergence). Root
AGENTS.md (runtime doctrine + agent index) and both project overlays read in
full. `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` read in full. Domain
source manifests recomputed by hash: `domains/chirality` 126 CLEAN / 93 DRIFT
/ 6 MISSING (the six missing are ACTIVE-pinned retired agent contracts:
AGENT_CONTEXT_TRANSPOSE, AGENT_DECOMP_BASE, AGENT_ORCHESTRATOR,
AGENT_SCHEDULING, AGENT_SKILLMAKER, AGENT_TOOLMAKER);
`domains/chirality-app-dev` 119 CLEAN / 129 DRIFT / 219 MISSING. Notice
routing surveyed: `domains/chirality/_Coordination/` holds D-GOV-21/23/24
notices but no D-GOV-26 notice; App `_Coordination/` holds D-GOV-21/23/24/26
notices; Piping holds no D-GOV doctrine notices (only a HELPS_HUMANS notice);
PEC holds none.

# Section 2 — Findings

### A-F-001 — D-GOV-27 EffectiveSHA remains an unbound placeholder

```yaml finding
FindingID: A-F-001
Product: ROOT
Surface: docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md
Assertion: The EffectiveSHA field of D-GOV-27 is a prose placeholder ("merge of the closing-tranche PR into `main`; backfilled by a later tranche per precedent") and no later tranche has backfilled it, so the record's own K-AUTH-2 vehicle ("approval binds at the merge SHA of the human-gated PR carrying it") currently binds to no identified commit.
EvidenceRefs:
  - docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md#line-6 (EffectiveSHA placeholder) and #line-44..47 (vehicle statement)
  - execution/_Coordination/LOOP_RECEIPTS.md#Receipt-52 ("D-GOV-27 EffectiveSHA backfill owed to the next tranche")
Class: trace_gap
Severity: REVIEW
DisclosedCondition: basis-wide condition 1
Consequence: The acceptance chain for the entire initialization phase (45 lifecycle flips, ResponsibleParty assignment, DEC-021 register propagation, the O-1 supersession note) terminates in a record whose applied-state identity is unresolved. Any consumer wanting to machine-verify "what commit carries the state D-GOV-27 approved" must reconstruct it from git (PR-2 merge) rather than from the record. Because D-GOV-26's identical debt was discharged by D-GOV-27 itself, the precedent works, but the chain is presently open at its newest link, and no successor workplan exists to carry the backfill obligation (see A-F-006).
SmallestAction: One owner-gated micro-tranche backfilling the EffectiveSHA field with the PR-2 merge commit, per the recorded precedent.
Owner: Root governance loop (CHANGE-published backfill per the D-GOV precedent)
Confidence: HIGH
```

### A-F-002 — Decomposition SHA-role label conflicts with the accepting instrument

```yaml finding
FindingID: A-F-002
Product: ROOT
Surface: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md (header)
Assertion: The accepted decomposition's header states "EffectiveSHA: ea0ad7a566… (merge of PR #347)" while the accepting instrument D-GOV-25 assigns that same commit the role "CandidateMergeSHA" and assigns "EffectiveSHA" to 653fabc9b3e8… (merge of PR #348); the two accepted surfaces therefore assign the same E-3 SHA-role vocabulary to different commits.
EvidenceRefs:
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#header-line-9 [14067a7d97c9]
  - docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md#lines-5..8 (AcceptedCandidateSHA / CandidateMergeSHA / EffectiveSHA role assignment)
  - execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md frontmatter (45/45 pin decomposition_basis @653fabc9b…, consistent with D-GOV-25, not with the header)
Class: semantic_conflict
Severity: REVIEW
DisclosedCondition: basis-wide condition 2
Consequence: PRD E-3 makes the three SHA roles a TRANSCRIBED product commitment ("recorded distinctly"). A reader resolving "the applied state of the accepted decomposition" from the working surface alone gets PR #347's merge; every downstream SOW and D-GOV-27 use 653fabc9b…. The decision record governs on disagreement (D-1), so the correct resolution is discoverable — but only by a reader who knows to distrust the header of the accepted working surface, which is precisely the failure mode E-3 exists to prevent. Left standing, the conflict will propagate into any tooling that parses the header.
SmallestAction: A recorded amendment to the working-surface header relabeling ea0ad7a56… as CandidateMergeSHA (companion-register/working-surface amendment citing D-GOV-25; no scope change).
Owner: Root decomposition amendment surface (per §14 On-amendment rule), owner-gated
Confidence: HIGH
```

### A-F-003 — Accepted post-candidate amendments lack one supplied verifying diff

```yaml finding
FindingID: A-F-003
Product: ROOT
Surface: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md §13 (DEC-014..DEC-021)
Assertion: The live decomposition is the accepted candidate (ec62af070…) plus two waves of applied dispositions (D-GOV-25 publication tranche; D-GOV-27/DEC-021 additive propagation), each asserting "no scope item, package, deliverable, objective, or identifier changed," but no supplied diff artifact verifies that claim; verification requires independent git archaeology across ec62af070… → 653fabc9b… → 31b8dc94a….
EvidenceRefs:
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#DEC-020 (byte-equivalence-in-substance claim), #DEC-021, #Change-Log
Class: trace_gap
Severity: WARN
DisclosedCondition: basis-wide condition 3
Consequence: The claim is plausible and the counts I recomputed from the live registers (103/45/7; 84 forward; 51 reverse) match the accepted headline counts, which is meaningful but partial corroboration — count-stability does not prove content-stability of statements or mappings. The burden of proving the amendments stayed within their ruled dispositions currently falls on every future reader instead of being discharged once. This weakens the otherwise strong Root acceptance chain at exactly the surface downstream work pins.
SmallestAction: Publish one diff summary (candidate SHA → current) as decomposition evidence, cited from the change log; no content change.
Owner: Root decomposition amendment surface / CHANGE
Confidence: HIGH
```

### A-F-004 — OI-011 remains OPEN after its resolution condition was met

```yaml finding
FindingID: A-F-004
Product: ROOT
Surface: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md §12 (OI-011)
Assertion: OI-011 ("ResponsibleParty is TBD throughout; a later planning act assigns responsibility") remains status OPEN in the accepted decomposition even though D-GOV-27 performed exactly the assignment it awaited ("Ryan Tufts" on the deliverable register and all 45 _CONTEXT.md, verified 45/45), and the same tranche that applied DEC-021 to the registers did not close the issue.
EvidenceRefs:
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#OI-011
  - docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md#effect-2
  - execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv (ResponsibleParty = "Ryan Tufts", 45/45, parsed)
Class: trace_gap
Severity: WARN
DisclosedCondition: Root condition 4 (OI-011 stale)
Consequence: The decomposition's own open-issue discipline (per-issue closure against its own stated condition, DEC-019) is violated by omission: a reader trusting §12 concludes responsibility is unassigned, contradicting the register that the same document declares authoritative. Low practical risk (the register wins by the document's own companion rule), but it is a live counterexample to OBJ-1's discoverability condition inside the accepted basis itself.
SmallestAction: Close OI-011 as CLOSED_BY_RULING citing D-GOV-27, in the next recorded amendment touching the working surface.
Owner: Root decomposition amendment surface
Confidence: HIGH
```

### A-F-005 — Stale "ResponsibleParty remains TBD" prose across the initialized SOW corpus

```yaml finding
FindingID: A-F-005
Product: ROOT
Surface: 21 of 45 ScopeOfWork.md contracts; all 45 _CONTEXT.md Source Authority boilerplate
Assertion: 21 SOW contracts contain axiology prose of the form "`ResponsibleParty` remains `TBD` until a human assigns ownership" and all 45 _CONTEXT.md files instruct "Downstream work must preserve `ResponsibleParty: TBD` until a human assigns ownership," while the same _CONTEXT.md files carry "**Responsible:** Ryan Tufts" — the assignment has occurred, so the "remains TBD" assertion is factually stale even though the conditional ("until a human assigns") self-resolves.
EvidenceRefs:
  - execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/1_Working/DEL-01-01_Genus_Concordance_Closure_and_Standing_Map/ScopeOfWork.md#AX-005
  - execution/PKG-01_.../DEL-01-01_.../_CONTEXT.md#lines-7,49-51 (Responsible: Ryan Tufts + preserve-TBD boilerplate)
  - grep count: 21/45 SOWs match "ResponsibleParty. remains .TBD"
Class: observation
Severity: INFO
DisclosedCondition: extends Root condition 4
Consequence: Consequence is cosmetic-but-corpus-wide: the D-GOV-27 contract-refresh ruling amended only the four objective-divergence contracts, leaving the other 41 with pre-assignment prose. Any future bulk validation or concordance pass over Root SOWs will re-discover this 21+45-surface delta; recording it now converts a future rediscovery into a known, dispositioned condition.
SmallestAction: Note the condition in the next Root concordance/enrichment phase plan; amend prose opportunistically at the next per-contract touch (no dedicated tranche warranted).
Owner: Next owner-gated Root SOW phase (semantic enrichment or production dispatch)
Confidence: HIGH
```

### A-F-006 — Initialization closure is navigationally unclosed: ACTIVE completed workplan, receipt-as-handoff, stale HANDOFF_STATE

```yaml finding
FindingID: A-F-006
Product: ROOT
Surface: execution/_Coordination/CURRENT_WORKPLAN.md; WORKPLAN_2026-07-25_root_initialization.md; HANDOFF_STATE.md; LOOP_RECEIPTS.md Receipt 52
Assertion: The deterministic standing-plan pointer targets a workplan still marked "ACTIVE — ROOT DELIVERABLE INITIALIZATION" whose own stop-state ("After PR 2 merges this workplan is complete") has been reached; the only initialization handoff is Receipt 52; and the file named HANDOFF_STATE.md still carries the superseded Stage-2 PKG-00-consolidation arc — so the loop's three navigation surfaces disagree about where the loop stands.
EvidenceRefs:
  - execution/_Coordination/CURRENT_WORKPLAN.md#Status
  - execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md#Status,#Stop-state
  - execution/_Coordination/HANDOFF_STATE.md#Status ("STAGE2_CLOSED — PKG-00 CONSOLIDATED…")
  - execution/_Coordination/LOOP_RECEIPTS.md#Receipt-52
Class: trace_gap
Severity: WARN
DisclosedCondition: basis-wide conditions 4 and 5
Consequence: LOOP_INIT.md's session-init contract sends a resuming operator to the pointer, the workplan, and the newest receipt. The pointer resolves to a completed plan whose ACTIVE banner asserts otherwise; the AGENTS.md handoff-state rule ("any workflow that stops with work intended for a later phase must emit an explicit handoff state") is satisfied only if a receipt is accepted as that handoff, while a file literally named HANDOFF_STATE.md carries a different, older arc. A fresh session recovers correctly only by privileging the receipt over both the banner and the named handoff file — recoverable, but the loop's own E-2/E-7 discipline is not exhibited by its most current phase boundary. This also leaves the A-F-001 backfill debt without a carrying surface.
SmallestAction: Open the next workplan (or mark the current one COMPLETE with a pointer note) and either supersede or re-point HANDOFF_STATE.md; both are coordination-surface edits requiring no ruling.
Owner: Root governance loop (HELP_HUMAN posture), next session
Confidence: HIGH
```

### A-F-007 — Candidate AC/VER status is machine-opaque across the 45 Root contracts

```yaml finding
FindingID: A-F-007
Product: ROOT
Surface: all 45 execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md
Assertion: The candidate (not-yet-accepted) status of every AC-*/VER-* definition is expressed through per-contract prose that varies across the corpus (sampled 12/45: at least six distinct formulations, e.g. "candidate content for owner review", "*candidate* authored under MODE=INIT", "candidates for owner disposition, not accepted criteria", "candidate criteria authored under this initialization run"), with no frontmatter field, marker, or register recording acceptance state deterministically.
EvidenceRefs:
  - DEL-01-01/ScopeOfWork.md#line-39; DEL-02-01#line-25,121; DEL-04-03#line-27,98; DEL-05-03#line-27; DEL-06-07#line-36; DEL-03-05#line-112 (sampled formulations)
  - docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md#§3-§4 (frontmatter schema has no acceptance-state field; checklist tool emits AC text, not acceptance state)
Class: omission
Severity: WARN
DisclosedCondition: basis-wide condition 6
Consequence: The deterministic checklist tool (D-GOV-15/16 machinery) compiles AC-* in source order with exact text; nothing in that artifact or the frontmatter distinguishes candidate from accepted criteria. When a later phase accepts some criteria, the only way to flip status will be prose edits in 45 differently-worded places — the drift pattern the PRD's own registry discipline (§5, anti-rot) warns against. The condition is disclosed; the consequence beyond disclosure is that acceptance, when it comes, has no landing surface, so the machine-opacity compounds at exactly the moment it matters.
SmallestAction: Owner-decision request: define one deterministic representation for AC/VER acceptance state (frontmatter field or per-deliverable register column) before the first acceptance act, via the SOW standard's own amendment path (D-GOV family).
Owner: HELPS_HUMANS proposal → D-GOV ruling (SOW standard amendment)
Confidence: HIGH
```

### A-F-008 — PRD O-1 supersession is carried only by the pointer block

```yaml finding
FindingID: A-F-008
Product: ROOT
Surface: docs/PRD_ROOT.md (pointer block vs adopted bytes)
Assertion: PRD §5.2 O-1's six-member instruction-surface enumeration is superseded solely through the pointer-block amendment-of-record above the horizontal rule; every byte below the rule still carries the stale enumeration, and any consumer that reads, copies, or exports the adopted bytes without the pointer block reads superseded doctrine with no in-band signal.
EvidenceRefs:
  - docs/PRD_ROOT.md#lines-15-24 (amendment of record), #§5.2-O-1 (stale enumeration in adopted bytes)
  - docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md#effect-5 (D-13 mechanics)
Class: observation
Severity: INFO
DisclosedCondition: Root condition 10
Consequence: This is D-13/D-16 working as designed (adopted bytes never overwritten at their path), and the D-14 source-currency check is the designed detector for exactly this class — but D-14's capability is unbuilt (OI-005). Until DEL-04-09 exists, the O-1 supersession is the first live instance of a superseded-in-place adopted byte with no executable currency check over it; the exposure grows with each further supersession-by-instrument.
SmallestAction: None now; prioritize DEL-04-09 (the D-14 capability) in the next phase selection, and ensure the export profile carries the pointer block with the adopted bytes.
Owner: Root loop phase selection (owner-gated)
Confidence: HIGH
```

### A-F-009 — The live agent index does not identify the root product's own accepted work structure

```yaml finding
FindingID: A-F-009
Product: ROOT
Surface: AGENTS.md (root)
Assertion: Root AGENTS.md — the canonical runtime doctrine and live index that every session loads — predates the root decomposition and contains no reference to the accepted 6-package/45-deliverable root work structure, the root guards G0–G4, or the D-GOV-21 root working-root exception, while it does describe project-level machinery in detail.
EvidenceRefs:
  - AGENTS.md (full read; no occurrence of PKG-01..PKG-06 root packages, execution/_harness, or D-GOV-21/25/27)
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#§8-§9 (the accepted structure)
Class: omission
Severity: WARN
DisclosedCondition: Root condition 7
Consequence: OBJ-1 commits the product to "a reader can determine what governs, from the repository alone." A session orienting from AGENTS.md (the declared entry surface, imported by CLAUDE.md) learns the delegation doctrine but not that the repository root is itself a governed working root with materialized packages, guards, and a fenced execution tree — knowledge that lives only in LOOP_INIT/D-GOV records. An agent entering outside the root loop protocol could plausibly treat root execution/ as ordinary space. The agent-index change-notice rule also means any future AGENTS.md amendment to fix this must ship routed notices — cheap now, more entangled later.
SmallestAction: Owner-gated M2 tranche adding a short "Root product structure" section (or pointer) to AGENTS.md citing D-GOV-21/25 and execution/_harness; routed notices per the change-notice rule.
Owner: HELPS_HUMANS proposal → M2 instruction-surface tranche
Confidence: HIGH
```

### A-F-010 — Root-doctrine notice coverage is uneven and nowhere dispositioned

```yaml finding
FindingID: A-F-010
Product: CROSS_PRODUCT
Surface: routed-notice surfaces of the four downstream loops
Assertion: Routed D-GOV doctrine notices exist for App (D-GOV-21/23/24/26) and domains/chirality (D-GOV-21/23/24 but not D-GOV-26), while Piping and PEC received no D-GOV doctrine notices at all; and none of the delivered notices has a recorded adoption/amend/decline disposition in the receiving loop's register or receipts.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-{21,23,24,26}*.md (present; no disposition rows in the D-APP register)
  - domains/chirality/_Coordination/ (NOTICE_D-GOV-26 absent; 21/23/24 present)
  - projects/chirality-piping/execution/_Coordination/ (only NOTICE_2026-07-25_helps_humans_p1_p7_applied.md)
  - projects/pec/execution/_Coordination/ and _DomainEngines/pec/ (no NOTICE_D-GOV files)
  - docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md register row ("Routed notice to projects/chirality-app-dev" only)
Class: ownership_gap
Severity: REVIEW
DisclosedCondition: basis-wide condition 13
Consequence: The AGENTS.md change-notice rule is scoped to tranches touching agents/ (and pin/mirror surfaces), so per-tranche routing decisions were mostly lawful — D-GOV-27's none-required survey is explicit and evidence-based. But the aggregate effect is that notice coverage tracks which pins a tranche-time survey found, not which loops rely on the doctrine: PEC's PRD and fences cite D-GOV-20/D-GOV-01 yet PEC has never received a doctrine notice; Piping's detection depends entirely on its own drift checks. Meanwhile the notices that were delivered sit undispositioned, so "notice → adopt/amend/decline under own instruments" — the rule's second half — has never been exercised end-to-end. The architecture's downstream-detection fallback (manifest drift status) is demonstrably alive (A-F-012) but heavily backlogged, which is exactly the state where notice routing is supposed to carry the load.
SmallestAction: Owner-decision request: (a) direct each receiving loop to record a disposition for held notices at its next session; (b) clarify (doctrine or ruling) whether doctrine-consuming loops without pins (PEC, Piping) are in-scope recipients for D-GOV doctrine notices.
Owner: Agent 0 / per-loop managers; doctrine clarification via HELPS_HUMANS → owner
Confidence: HIGH
```

### A-F-011 — The D-GOV-24 notice to App misidentifies its stale target

```yaml finding
FindingID: A-F-011
Product: APP
Surface: projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-24_OPERATING_SYSTEM_PROSE_PROPAGATION.md
Assertion: The notice states "Any local mirror, snapshot, or sha256 pin of these four files is now stale … (the App Dev AUTHORITY_CORPUS.json pins all four)", but AUTHORITY_CORPUS.json v17 pins the project-local copies (projects/chirality-app-dev/docs/DIRECTIVE.md etc.), which D-GOV-24 did not touch; the v17 pins verify CLEAN at the freeze, so the notice's staleness claim about the corpus is false.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-24_OPERATING_SYSTEM_PROSE_PROPAGATION.md#lines-33-35
  - projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json#v17 (hashes verified CLEAN against project-local docs)
  - docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md#Downstream-coordination (the later, correct pin survey: corpus resolves to project-local copies)
Class: semantic_conflict
Severity: WARN
DisclosedCondition: App condition 10 (the misidentifying notice)
Consequence: A notice is coordination, not authority — but its factual claims are what the receiving loop acts on. Acting on this one would trigger a needless corpus version bump; D-GOV-27's later survey silently corrects the error in a different loop's records, where the App loop has no reason to look. Small in itself, it is direct evidence that tranche-time pin surveys can be wrong in the routed artifact while right in the decision record, strengthening the case for receiving-loop dispositions (A-F-010).
SmallestAction: App loop records a decline/correction disposition for this notice citing the v17 pin verification; no corpus change.
Owner: App loop (next session, coordination surface)
Confidence: HIGH
```

### A-F-012 — domains/chirality source manifest carries 93 DRIFT and six missing ACTIVE-pinned retired agents

```yaml finding
FindingID: A-F-012
Product: ROOT
Surface: domains/chirality/_Sources/Source_Manifest.csv
Assertion: Recomputing all 225 manifest rows by SHA-256 at the freeze yields 126 CLEAN / 93 DRIFT / 6 MISSING; the six missing rows are AGENT_CONTRACT pins for agent files retired from agents/ (AGENT_CONTEXT_TRANSPOSE, AGENT_DECOMP_BASE, AGENT_ORCHESTRATOR, AGENT_SCHEDULING, AGENT_SKILLMAKER, AGENT_TOOLMAKER) whose retirements were ruled in D-GOV-11/13/18-era decisions, with no manifest update or routed notice reflected in the domain pack.
EvidenceRefs:
  - domains/chirality/_Sources/Source_Manifest.csv (recomputed; missing rows SRC-AGENTS-AGENT-{CONTEXT-TRANSPOSE,DECOMP-BASE,ORCHESTRATOR,SCHEDULING,SKILLMAKER,TOOLMAKER})
  - docs/governance_harness/_DECISIONS/_REGISTER.md#D-GOV-18 (ORCHESTRATOR rename), #D-GOV-14 (SCHEDULING retirement)
Class: trace_gap
Severity: WARN
DisclosedCondition: basis-wide condition 12
Consequence: The domain pack is consulted-only context, so no product correctness depends on it — but it is the designated exemplar of the change-notice architecture's detection half. 93 drifted + 6 dangling pins that have accumulated across multiple ruled agent-index changes show detection works (the drift is computable) while remediation has no owner or cadence: the AGENTS.md change-notice rule obligates the changing tranche to notify, and the receiving loop to act, yet neither has produced a manifest refresh over roughly six weeks of index changes. This is the concrete cost that A-F-010's routing-and-disposition gap accrues.
SmallestAction: A domains/chirality loop session re-pins or retires the six missing rows and refreshes drifted pins on its own cadence (the notices' own stated remedy).
Owner: domains/chirality loop
Confidence: HIGH
```

### A-F-013 — App decomposition acceptance rests on "implicit human approval" with no ruling record

```yaml finding
FindingID: A-F-013
Product: APP
Surface: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md (Gate Posture; DEC-002)
Assertion: The App decomposition's Gate Log records all seven gates PASSED with acceptance stated as "Gates 1-7 accepted by implicit human approval per user instruction" (DEC-002, 2026-05-20); no separate gate-acceptance ruling file, verbatim owner text, or SHA-bound acceptance act exists for the base decomposition, in contrast to Root (D-GOV-25) and PEC (D-PEC-60 with per-gate verbatim confirmations).
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#header-Gate-Posture, #Gate-Log, #DEC-002
  - projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md#Gate-Log (contrast: verbatim per-gate rulings)
Class: authority_conflict
Severity: REVIEW
DisclosedCondition: basis-wide condition 8
Consequence: 53 live SOW contracts, four SCA amendments, the D-APP-55/56 concordance run, and PRD §16 all build on this decomposition as accepted basis. The subsequent record is strong — SCA-APP-002/003/004 each carry explicit owner rulings, and D-APP-35/38 re-pinned REF-006 — so the practical acceptance is heavily corroborated by later owner acts that treat it as accepted. But the founding acceptance itself is attested only by the artifact it accepts, predates the K-AUTH-2-style vehicle discipline the program later adopted, and cannot be independently verified from any instrument. If any future dispute about v3.2's base content arises (e.g., against the missing invariant register, A-F-014), there is no ruling text to resolve it against.
SmallestAction: Owner-decision request: a single retrospective confirmation ruling (one D-APP row) binding the current v3.2 bytes at a SHA as the accepted decomposition basis — an attestation of existing fact, not a new acceptance.
Owner: App loop owner gate (D-APP register)
Confidence: HIGH
```

### A-F-014 — The required-or-deferred contract invariant coverage register is neither present nor deferred

```yaml finding
FindingID: A-F-014
Product: APP
Surface: projects/chirality-app-dev/execution/_Decomposition/ (absent contract_invariant_coverage_register.csv)
Assertion: v3.2 §2.2 declares contract_invariant_coverage_register.csv a "Planned authoritative companion register" that "must be created or explicitly deferred before REVIEW closure," and §10B repeats the created-synchronized-or-explicitly-deferred check; the file does not exist (the _Decomposition directory contains only the working surface), no deferral ruling appears in the 74-row D-APP register, and REVIEW-shaped closure acts have since occurred (D-APP-55/56 concordance run CLOSED with R6 backcheck; SCA-APP-004 Gate-5 closure validation).
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#§2.2,#§10B,#DEC-015
  - projects/chirality-app-dev/execution/_Decomposition/ (directory listing: single file)
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md (no deferral row; D-APP-55 cell records RUN CLOSED)
Class: omission
Severity: REVIEW
DisclosedCondition: basis-wide condition 9
Consequence: §10A.1's compact invariant-family table exists as prose, but the decomposition's own acceptance checklist makes machine-truth invariant coverage a REVIEW-closure precondition. The precondition has now been passed through at least twice (concordance run closure; SCA-APP-004 closure) without either the artifact or the deferral. This converts a self-imposed conformance check into dead text — the specific failure mode the program's closure rule (E-7 analog) exists to prevent — and leaves K-* invariant coverage reviewable only through 1,115 concordance claim rows rather than the designed register.
SmallestAction: Owner-decision request with two lawful outcomes: create the register (bounded documentary tranche) or rule an explicit deferral naming the concordance corpus as the interim coverage surface.
Owner: App loop owner gate (D-APP register)
Confidence: HIGH
```

### A-F-015 — App PRD identity depends wholly on the external corpus pin; internal identity is defective

```yaml finding
FindingID: A-F-015
Product: APP
Surface: projects/chirality-app-dev/docs/PRD.md
Assertion: The PRD carries no version number, a header date (2026-05-20) more than two months older than its newest content (the §17 Shared Runtime amendment reflecting D-GOV-20/D-APP-73/SCA-APP-003, and Woven Dialogue content from D-APP-74), and two sections both numbered "17" ("Approval and Change Control" at line 1676 and "Shared Runtime and Local-Agent Pilot Amendment" at line 1692); its identity of record is only the AUTHORITY_CORPUS.json v17 hash pin.
EvidenceRefs:
  - projects/chirality-app-dev/docs/PRD.md#header (Status/Date), #line-1676, #line-1692 [ef638f43ccae]
  - projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json#v17 (binding_commit 1cfd3e29…, verified CLEAN)
Class: omission
Severity: WARN
DisclosedCondition: basis-wide condition 7; App condition 2
Consequence: The D-APP-38 corpus model deliberately makes the pin the identity, and the pin verifies — so identity is sound for anyone using the governed mechanism. The residual defects are citation integrity: "PRD §17" is ambiguous between change-control rules and the shared-runtime amendment (both are load-bearing), and the header misdates the document's content, which invites exactly the stale-fact reliance the corpus model was built to prevent in consumers who read the file directly (including packaged builds and the public repository). A duplicate section number in the top authority document is also the kind of defect the loop's own concordance machinery repeatedly flags in deliverable kits.
SmallestAction: A documentary tranche renumbering the second §17 to §18, adding a corpus-version line to the header (identity remains the pin), and bumping the corpus per D-APP-38.
Owner: App loop (D-APP-38 reconciliation path)
Confidence: HIGH
```

### A-F-016 — The D-APP-48 SHA-pinned pull contract is 12/12 stale against deprecation shims

```yaml finding
FindingID: A-F-016
Product: APP
Surface: projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json
Assertion: All 12 files pinned by the D-APP-48 pull contract now hash-mismatch their recorded sha256 values (verified 12/12 DRIFT); the current file contents are deprecation shims re-exporting @chirality/runtime-contracts ("This package remains only as a source-compatible facade for one migration cycle"), and no repin, supersession, or retirement of the pull contract is recorded, while Piping's D-30 consumption record still points at it.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json#exports (12 sha256 pins; all recomputed DRIFT)
  - projects/chirality-app-dev/frontend/packages/harness-contract/src/index.ts (deprecation shim text)
  - projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json#pullContractPath
Class: trace_gap
Severity: REVIEW
DisclosedCondition: basis-wide condition 10
Consequence: The pull contract is the recorded mechanism satisfying DEC-041's no-manual-toil automation condition and the basis of Piping's ruled consumption path. As it stands, a consumer executing the contract verbatim would fail hash verification on every file; a consumer skipping verification would consume shims whose real contract now lives in root runtime/ under different ownership (D-APP-73). Neither D-APP-73's ruling row nor SCA-APP-003 records a decision terminating, repinning, or rehoming the pull mechanism, so the accepted record still asserts a consumable pinned surface that no longer exists as pinned. This is the sharpest concrete instance of the migration-arrangement-becoming-stale pattern, and it also puts D-APP-49's "field-for-field SHA-pinned mirrors … in @chirality/harness-contract" obligation in doubt (not independently verified; see Section 7).
SmallestAction: Owner-decision request in the App loop: repin the contract against runtime-contracts, or formally retire/supersede D-APP-48's mechanism with a pointer to the shared-runtime successor, with a routed notice to Piping (D-30).
Owner: App loop owner gate; notice to Piping loop
Confidence: HIGH
```

### A-F-017 — Orphan PKG-03_Harness_Runtime_Core tree duplicates a package number outside the decomposition

```yaml finding
FindingID: A-F-017
Product: APP
Surface: projects/chirality-app-dev/execution/PKG-03_Harness_Runtime_Core/
Assertion: The execution tree contains two PKG-03 directories — the registered PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle and an orphan PKG-03_Harness_Runtime_Core containing only 1_Working/DEL-03-06_Outbound_Network_Guardrails/Evidence/ (no _STATUS.md, no ScopeOfWork.md); neither the package label nor DEL-03-06 exists in the accepted v3.2 decomposition (PKG-03 has four deliverables, DEL-03-01..04).
EvidenceRefs:
  - projects/chirality-app-dev/execution/ (directory listing: both PKG-03_* entries)
  - projects/chirality-app-dev/execution/PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/ (contents: Evidence/ only)
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#§8-PKG-03
Class: ownership_gap
Severity: WARN
DisclosedCondition: App condition 7
Consequence: Stable-ID discipline makes PKG-03/DEL-03-06 collide at the identifier level: any tooling that scans execution/ by prefix (deliverable scans, census tools, PEC's future lifecycle parser) will either double-count PKG-03 or mis-attribute the orphan. Because the orphan has no _STATUS.md it is invisible to the status census (verified: census counts 53), which means it survives precisely because nothing owns it. Historical evidence should live in a dispositioned location (archive or a registered evidence surface), not in an ID-bearing execution path.
SmallestAction: A recorded relocation of the evidence tree to an archive/evidence surface (or a register note declaring the path historical), via the loop's ordinary coordination cadence — no ruling needed unless content is deleted.
Owner: App loop coordination
Confidence: HIGH
```

### A-F-018 — Receipt 91 and its run handoff disagree with git about the terminal merge

```yaml finding
FindingID: A-F-018
Product: APP
Surface: projects/chirality-app-dev/loop/LOOP_RECEIPTS.md Receipt 91; execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/HANDOFF_STATE.md
Assertion: Receipt 91 names "owner merge of the pull request" as the terminal act without recording the merge SHA, and the run's HANDOFF_STATE.md still reads APPDEV_DAEMON_SERVICE_IMPLEMENTATION_COMPLETE_PENDING_PR_AND_OWNER_MERGE, while git history shows PR #333 merged at 612c35226 (with a follow-up commit 01ff160bc recording the PR number in the receipt pointer).
EvidenceRefs:
  - projects/chirality-app-dev/loop/LOOP_RECEIPTS.md#Receipt-91 (Gate-Outcome; Pointers cite "PR #333" without merge SHA)
  - projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/HANDOFF_STATE.md#line-3
  - git log: 612c35226 "Merge pull request #333"
Class: trace_gap
Severity: WARN
DisclosedCondition: App conditions 9 and 12
Consequence: The loop's own D-APP-57 receipt contract exists to make the ledger an exact cursor; here the newest receipt's terminal fact must be recovered from git rather than the ledger, and the durable handoff asserts a pending state that is false at the freeze. Any orientation consumer (including PEC's intended receipt parser, whose per-loop grammar is calibrated on this ledger) would report the daemon-service tranche as awaiting merge. Self-healing on the next receipt, but at the freeze the coordination surface misstates the loop's terminal state.
SmallestAction: Next receipt (or a receipt-contract-conformant addendum) records the 612c35226 merge; the run HANDOFF_STATE gains a terminal line.
Owner: App loop, next session
Confidence: HIGH
```

### A-F-019 — The App AGENTS.md overlay operates while marked draft

```yaml finding
FindingID: A-F-019
Product: APP
Surface: projects/chirality-app-dev/AGENTS.md
Assertion: The project agent-index overlay carries frontmatter "status: draft" (created 2026-06-15) while functioning as the live overlay that binds path anchors, agent posture, attribution rules (D-GOV-17 M1-D), and delegation structure for all App work.
EvidenceRefs:
  - projects/chirality-app-dev/AGENTS.md#frontmatter
Class: observation
Severity: INFO
DisclosedCondition: App condition 11
Consequence: Content-wise the overlay is current (it carries the post-D-GOV-17 attribution rules and D-APP-61 outcomes), so the "draft" label is a status-metadata defect rather than a doctrine defect. Its cost is epistemic: the program elsewhere treats status fields as load-bearing (D-GOV-06's whole cleanup arc), so a surface that is de-facto operative while self-labelled draft is a small standing contradiction of the discoverability objective, and a trap for any tooling that filters by status.
SmallestAction: Flip frontmatter to live/active in an ordinary documentary commit at next touch.
Owner: App loop
Confidence: HIGH
```

### A-F-020 — Materialized package folder label diverges from the amended package name

```yaml finding
FindingID: A-F-020
Product: APP
Surface: projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/
Assertion: The accepted v3.2 decomposition (as amended by SCA-APP-004) names PKG-02 "Woven Dialogue Shell, Navigation, and Operator State", while the materialized folder label remains PKG-02_Desktop_Shell_Navigation_and_Operator_State; the number is stable but the label halves of the surface identity disagree.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#§7-PKG-02
  - projects/chirality-app-dev/execution/ (directory listing)
Class: observation
Severity: INFO
DisclosedCondition: none
Consequence: SCA-APP-004 preserved IDs and lifecycle deliberately, and folder renames would churn dozens of recorded paths, so the divergence is a defensible cost of the amendment discipline — but it is nowhere recorded as a known label divergence, so a reader matching decomposition names to folders finds an unexplained mismatch on the product's most active package. One sentence in the SCA snapshot or the decomposition's §7 would close it.
SmallestAction: Record the label-divergence note in the decomposition or SCA-APP-004 snapshot at next amendment; do not rename folders.
Owner: App decomposition amendment surface
Confidence: HIGH
```

### A-F-021 — docs/MANIFEST.json remains an unmarked stale identity surface

```yaml finding
FindingID: A-F-021
Product: APP
Surface: projects/chirality-app-dev/docs/MANIFEST.json
Assertion: The docs manifest (created 2026-06-13, status "governance_index") lists the six governance documents with roles but no hashes or version linkage, has not tracked the corpus-versioning model that superseded it (D-APP-38 / AUTHORITY_CORPUS.json v17), and carries no marker telling a reader that the corpus pin, not this manifest, is the identity of record.
EvidenceRefs:
  - projects/chirality-app-dev/docs/MANIFEST.json (created/status fields; no hashes)
  - projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json#model
Class: observation
Severity: INFO
DisclosedCondition: App identity condition (brief §4.2: manifest stale, use v17 pin)
Consequence: Harmless while readers know the corpus model; misleading to any consumer (or packaged build) that discovers docs/ through its own manifest. Same remediation class as A-F-019.
SmallestAction: Add a superseded-for-identity pointer line to the manifest, or retire it, at next docs touch.
Owner: App loop
Confidence: HIGH
```

### A-F-022 — Root and PEC SOW validation identities straddle a method change

```yaml finding
FindingID: A-F-022
Product: CROSS_PRODUCT
Surface: skills/scope-of-work + tools/scope_of_work (shared method layer) vs Root 45 SOWs / PEC 32 SOWs
Assertion: The shared SOW method changed through amendments v1–v6.1 (QA-item-20 harmonization); PEC's 32 contracts were repaired and re-validated under the current method (D-PEC-66: 21 flagged matrix rows dispositioned, validator "PASS ×10", --strict clean), while Root's 45 contracts hold PASS results produced before the v6/v6.1 change and have not been re-run; the two products' identical-looking "validated SOW_V1" states therefore certify different method eras.
EvidenceRefs:
  - projects/pec/execution/_Coordination/_COORDINATION.md#item-9 (post-QA-20 clean state)
  - execution/_Coordination/LOOP_RECEIPTS.md#Receipt-52 ("45× validator PASS" — pre-v6 era per the shared-method history)
  - projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md#D-PEC-66 (QA-item-20 dispositions)
Class: observation
Severity: WARN
DisclosedCondition: basis-wide condition 15
Consequence: Tool-basis discipline (Common-Brief §5.5 analog, and the program's own D-GOV-02 era-binding) is currently carried by nothing machine-readable: no Root surface records which validator version produced its PASS. A future current-tool rerun over Root would likely emit QA-20-style findings that are tool-drift artifacts, not falsifications of the accepted validation — and without a recorded tool basis, distinguishing the two will require archaeology. Conversely, genuine QA-20-class defects in Root contracts (over-linked matrix rows) are presently invisible.
SmallestAction: Record the validation-era (tool version/commit) for the Root 45 in the next phase plan, and schedule a current-tool advisory rerun whose findings are triaged as drift-vs-defect rather than pass/fail.
Owner: Root loop next phase; shared method layer (HELPS_HUMANS) for era-stamping validator output
Confidence: HIGH
```

### A-F-023 — Semantic ownership of the rehomed runtime is divided between Root doctrine and App decomposition

```yaml finding
FindingID: A-F-023
Product: CROSS_PRODUCT
Surface: runtime/ (Root) vs App decomposition PKG-03/04 and SCA-APP-003 impact map
Assertion: D-GOV-20 and D-T0-23 make root runtime/ a Root-owned product subsystem with App and PEC as distinct clients, while the App decomposition's Downstream Execution Notes state "Root runtime/ ownership is an implementation-location change; app-dev deliverables retain semantic ownership and acceptance evidence through the SCA-APP-003 impact map" — leaving the runtime's semantic ownership split between a Root doctrine claim and a standing App claim, with no accepted instrument that transfers, terminates, or time-bounds the App-side ownership, and with the App-side contract mirrors already stale (A-F-016).
EvidenceRefs:
  - AGENTS.md#Shared-Runtime-Doctrine; docs/PRD_ROOT.md#O-2 (runtime substrate as Root operative layer)
  - _DomainEngines/_DECISIONS/_REGISTER.md#D-T0-23
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#§13-Downstream-Execution-Notes, #OI-007, #DEC-019
Class: ownership_gap
Severity: REVIEW
DisclosedCondition: partially assesses conditions 10 and 19-adjacent doctrine (shared runtime)
Consequence: Today the split is coherent as a migration posture: Root owns the generic runtime going forward; App retains ownership of its historical deliverable evidence and its client integration. But the App deliverables that "retain semantic ownership" (PKG-03 engine contract, PKG-04 adapter) describe surfaces whose authoritative implementation now lives in Root runtime/, and Root's accepted decomposition — PRD-only by design — covers the runtime solely as conformance slices (DEL-02-02 three-layer boundary; no scope item enumerates protocol/daemon/sessions/credentials work). Neither product's accepted basis currently owns forward evolution of the runtime contract as work: Root has no runtime deliverable beyond boundary conformance, and App's runtime deliverables are doctrinally demoted to client scope. A change to the runtime contract tomorrow has no unambiguous accepted landing surface. This is the divided-ownership pattern the Tier-0 register was built to prevent, one migration late.
SmallestAction: Owner-decision request: record (one instrument, likely a D-GOV or D-T0 row) which surface owns forward runtime-contract change — e.g., Root loop work derived from PRD O-2 with App/PEC as noticed consumers — and direct the App loop to reclassify its retained runtime deliverables as client/evidence scope at its next amendment.
Owner: Owner via Tier-0/Root governance; App loop follow-on
Confidence: MEDIUM
```

### A-F-024 — Root runtime coverage is a single conformance slice against a multi-surface substrate

```yaml finding
FindingID: A-F-024
Product: ROOT
Surface: execution/_Decomposition (DEL-02-02; scope items derived from PRD O-2)
Assertion: The Root decomposition's coverage of the runtime substrate consists of conformance-style deliverables derived from PRD O-2's three-layer commitment (principally DEL-02-02, ContextEnvelope M), and no scope item or deliverable enumerates the runtime's concrete owned functions (protocol, daemon, clients, sessions, delegation, credentials, residency, conformance evidence) as distinct work — a faithful consequence of the PRD-as-sole-scope-source rule, since the PRD carries the runtime by reference.
EvidenceRefs:
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#§9-PKG-02 (DEL-02-02), #§2.1 (REF-001 sole source)
  - docs/PRD_ROOT.md#O-2 (runtime layer incorporated by reference)
Class: observation
Severity: INFO
DisclosedCondition: none
Consequence: Not a conformance defect: the accepted basis is internally consistent, and F4 closes. The observation is that the PRD's registry-discipline style (incorporate by reference, don't enumerate) means the decomposition inherits reference-level granularity for the runtime; whether that granularity suffices becomes testable only when runtime work is actually dispatched. If the owner resolves A-F-023 toward Root ownership of runtime evolution, this granularity question becomes live and may warrant a PRD amendment or a scope change rather than silent expansion of DEL-02-02.
SmallestAction: None now; couple to the A-F-023 owner decision.
Owner: Root loop (contingent)
Confidence: MEDIUM
```

### A-F-025 — The PEC domain-engine profile remains ADOPTED for a retired product pending v2 supersession

```yaml finding
FindingID: A-F-025
Product: PEC
Surface: _DomainEngines/profiles/pec.yaml
Assertion: The pec profile remains status ADOPTED (Gate 2, 2026-07-05) and binds the frozen v0.4 prototype instance; it was amended (0.1→0.2, D-PEC-59) with pivot notes and archive paths, and both it and the PEC surfaces state that full supersession awaits the v2 implementation shape — so the tier-0 profile surface currently describes, accurately but confusingly, an adopted profile of a product that no longer exists as a live application.
EvidenceRefs:
  - _DomainEngines/profiles/pec.yaml#header (ADOPTED; frozen-corpus provenance)
  - projects/pec/docs/STATUS.md#Governance ("full supersession remains pending v2 implementation shape")
  - projects/pec/AGENTS.md#Governance-Pointers ("binds the frozen engine instance only")
Class: observation
Severity: INFO
DisclosedCondition: PEC condition 1
Consequence: The interim state is explicitly recorded in three places, which is the disclosure discipline working. Residual risk is confined to tier-0-side readers who encounter the ADOPTED profile without the PEC-side pointers; the profile's own pivot notes mitigate this. The condition self-resolves at the first v2 implementation packet; no earlier act is warranted.
SmallestAction: None until v2 has shape; the supersession is already a named D-PEC-58/59 follow-on.
Owner: PEC loop (future packet)
Confidence: HIGH
```

### A-F-026 — Recorded PEC REVIEW residuals are tracked and low-consequence

```yaml finding
FindingID: A-F-026
Product: PEC
Surface: DEL-08-01, DEL-08-02, DEL-00-03 ScopeOfWork.md
Assertion: The three recorded REVIEW residuals stand as described and are bounded: DEL-08-01's AC-005 second clause is exercised only through the OUT-001 matrix row that pairs CLM-002/CLM-005 with AC-007's HUMAN_REVIEW method (verified in the matrix); DEL-00-03's CLM-001 is a transcription-shaped claim not referenced from its matrix; DEL-08-02's CLM-002/AX-006 provenance text stands as recorded — none of the three misstates scope, invents commitments, or breaks frontmatter traceability (all three contracts pin rev 1.2 @3623b958b and non-empty scope/objective refs).
EvidenceRefs:
  - projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md#AC-005,#AC-007,#matrix-rows-164,169
  - projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/ScopeOfWork.md#CLM-001
Class: observation
Severity: INFO
DisclosedCondition: PEC conditions 3 and 4
Consequence: Assessed in context per the brief's instruction: these are contract-craft imperfections inside candidate (unaccepted) AC/VER content, already dispositioned by D-PEC-66's QA pass or recorded as residuals. They matter only at the future acceptance act, where the owner will rule on candidate criteria anyway. No pre-acceptance action improves the record.
SmallestAction: None; carry to the acceptance-time review of candidate criteria.
Owner: PEC loop (acceptance phase)
Confidence: HIGH
```

# Section 3 — Coverage matrix

Products ROOT / APP / PEC × seven layers. "FULL" = document(s) read in full;
"SAMPLE n/of" = sampled with the count shown. Register CSVs were parsed
programmatically wherever counting mattered.

| Layer | Examined | Depth verdict | Breadth verdict | FindingRefs | Residual unknowns |
|---|---|---|---|---|---|
| ROOT · PRD | FULL (docs/PRD_ROOT.md 1056 lines; pointer block + adopted bytes; hash verified) | Sound: adoption chain D-GOV-21→22→23→24 verified in register; provenance-label discipline internally consistent | Sound: registry-discipline style pushes enumeration outward; see A-F-024 | A-F-008, A-F-024 | Concordance annex not read (derivative, never adopted) |
| ROOT · AuthorityChain/Corpus | FULL register (D-GOV-01..27); D-GOV-25/27 records FULL; DIRECTIVE/CONTRACT/SPEC/TYPES consulted via PRD transcriptions and targeted greps, not full reads | Acceptance chains verified through per-decision records; two defects at the newest links | Chain architecture (register navigational, records govern) working as designed | A-F-001, A-F-002 | C-2 (invariant-index arithmetic) and C-4 (export description) not independently re-verified; CONTRACT/SPEC bodies not fully read |
| ROOT · Decomposition+Registers | FULL working surface; all 5 companion CSVs parsed (103/45/7/84/51 verified) | F4 closes both directions; counts verified; amendment provenance weak on diffs | Partition rationale (6 work domains vs 4 categories) coherent; D-15 demonstrated | A-F-002, A-F-003, A-F-004 | Content-stability of amendments not diff-verified (A-F-003) |
| ROOT · ScopesOfWork | SAMPLE 12/45 (2+ per package: DEL-01-01 FULL, DEL-01-04, DEL-02-01, DEL-02-04, DEL-03-05, DEL-03-06, DEL-04-03, DEL-04-09, DEL-05-03, DEL-05-08, DEL-06-07, DEL-06-08); 45/45 frontmatter basis-pin grep-verified | Frontmatter uniform and correctly pinned; candidate-status prose varies (A-F-007) | Contracts stay within accepted register scope in sample; write-locus boundary language uniform | A-F-005, A-F-007 | 33 SOW bodies unread; semantic quality beyond sample UNKNOWN |
| ROOT · Decisions | FULL register + D-GOV-25/27 records | Verbatim rulings, SHA vehicles present except A-F-001 | Register/record division of authority clean | A-F-001 | Individual records D-GOV-01..24 not all opened (register summaries relied on for pre-July decisions) |
| ROOT · Coordination/CurrentState | FULL: LOOP_INIT, CURRENT_WORKPLAN, initialization workplan, Receipt 52, HANDOFF_STATE head; guard state + work graph verified | Receipt-52-as-handoff verified; navigation defects found | Loop protocol itself (LOOP_INIT) is sound; state surfaces lag | A-F-006 | Receipts 1–51 unread except via register cross-references |
| ROOT · Integration/Drift | domains/chirality manifest recomputed 225/225; notice surfaces enumerated across all four loops; root AGENTS.md FULL | Drift counts independently reproduced (126/93/6) | Notice-routing architecture assessed end-to-end | A-F-009, A-F-010, A-F-012 | The 93 DRIFT rows not individually triaged (age/cause unknown per row) |
| APP · PRD | FULL (1720 lines, three passes) | Amendment layering visible in-file; identity defects found | Non-goals and boundary discipline extensive and consistent with decomposition | A-F-015 | Whether every D-APP ruling with PRD effect is reflected in the bytes: UNKNOWN (no per-ruling PRD concordance register) |
| APP · AuthorityChain/Corpus | AUTHORITY_CORPUS.json parsed; all 8 v17 pins hash-verified CLEAN; MANIFEST.json inspected | Corpus model (D-APP-38) verified working at the freeze | Pins cover six docs + two root agent files; nothing pins root docs (by design) | A-F-021 | Corpus versions v1–v16 not examined |
| APP · Decomposition+Registers | FULL working surface (614 lines; SSOW+ledger inline); no companion CSVs exist | Acceptance provenance weakest of three products; invariant register absent | 10A invariant-family prose coverage exists; ledger coverage checked by inspection (spot, not parsed — tables inline) | A-F-013, A-F-014 | Full 78-row ledger cross-check not machine-parsed (inline markdown), scope-item↔deliverable closure taken from §10 telemetry plus spot checks |
| APP · ScopesOfWork | SAMPLE 0 full reads; existence/census verified 53/53 (all IN_PROGRESS); orphan tree examined | Lifecycle census verified; contract content not sampled this pass | 53 = 51 + 2 PKG-00 control deliverables confirmed on filesystem | A-F-017 | App SOW content quality: UNKNOWN this pass (D-APP-55/56 concordance run provides extensive recent coverage; I did not re-derive it) |
| APP · Decisions | FULL register (74 rows, both pages) | Ruling records rich; canonical ruling-text SHAs from D-APP-57 on | Cross-loop authoring grant (D-T0-19) mechanics understood | A-F-013 (contrast), A-F-016 | Individual packet/ruling files opened only for D-APP-48-adjacent surfaces |
| APP · Coordination/CurrentState | LOOP_INIT read (40 lines + loader rules); Receipts 90–91 FULL; SCA _LATEST FULL; workplan headers | Receipt/handoff/git divergence verified against git | Committed-HEAD plan loader (D-APP-64) is a strong navigation design | A-F-018 | Receipts 1–89 unread; WORKPLAN_2026-07-18b body skimmed only |
| APP · Integration/Drift | D-APP-48 contract 12/12 hash-recomputed; domain manifest recomputed 467/467; notices read; coverage package verdicts checked | Stale-mirror and notice-misidentification independently verified | Runtime-seam files listed, not read (frontend/src/lib/runtime-client/*) | A-F-011, A-F-016, A-F-023 | D-APP-49 mirror obligations vs rehomed architecture: UNKNOWN (not verified; Section 7) |
| PEC · PRD | FULL (490 lines; hash verified) | Adoption chain D-PEC-57→58→61 verified in register and packet pointers | Non-goals (§4.2) and optionality posture exceptionally explicit | — | v1.0/v0.4 archived texts not read (out of accepted basis) |
| PEC · AuthorityChain/Corpus | PRD + AGENTS.md overlay FULL; Tier-0 register FULL; fences F-PEC-1..4 traced to D-T0-15 | Instrument lineage coherent incl. partial supersession of D-PEC-56 | Tier-0/local register division clean (pointer rows used correctly) | A-F-025 | D-PEC packets 01–56 mostly unopened (register cells relied on) |
| PEC · Decomposition+Registers | FULL working surface (662 lines); ScopeLedger + Deliverables CSVs parsed (94/64 verified); dependency registers parsed 64/64 (254 = 135+119; 0 waivers) | Gate-by-gate verbatim acceptance; SCA-001/002 lineage clean; live counts match coordination item 9 exactly | 11-package partition with declared forced-boundary log (DL-11) is the strongest decomposition craft in the corpus | — | ContextBudgetQA.csv and Companion_Inventory.csv not parsed (low stakes) |
| PEC · ScopesOfWork | SAMPLE 6/32 (DEL-00-03, DEL-02-03, DEL-08-01, DEL-08-02 headers+targets; DEL-10-10 header+§1 FULL-ish; DEL-01-01 via decomposition); 32/32 basis-pin implied by D-PEC-63 wave records and spot-verified on all 6 | Rev-1.2 pinning correct in sample incl. the recorded superseded-provenance note handling | Deferred-32 posture verified against census (32 OPEN / 32 INITIALIZED) | A-F-026 | 26 SOW bodies unread; the DEL-04-05/DEL-08-03 seam-gap SCA candidate not assessed |
| PEC · Decisions | FULL register (D-PEC-01..66) | Verbatim rulings pervasive; residual-row convention consistently applied | Indefinite-postponement rows honestly carried | — | Pre-pivot rows (01–56) assessed only for lineage, not content |
| PEC · Coordination/CurrentState | FULL: STATUS.md, _COORDINATION.md; Receipt 112 via register/coordination cross-refs | Item-9-supersedes-item-8 layering verified against parsed registers | Blocker state correctly framed as advisory | — | LOOP_RECEIPTS.md body not read directly (register cells + coordination summaries relied on) |
| PEC · Integration/Drift | pec.yaml header read; shared-runtime boundary sections FULL in AGENTS.md/PRD | Client-not-authority posture consistent across all surfaces | PKG-07/08 seams identified; SOW-074/083 fencing of runtime/ writes verified | A-F-025 | None material |

# Section 4 — Boundary matrix

| Function | Semantic owner per accepted basis | Producers | Consumers | Fallback/degraded | Routed change path | Verdict | FindingRefs |
|---|---|---|---|---|---|---|---|
| Shared runtime (protocol, daemon, sessions, engines, credentials) | Root (D-GOV-20; D-T0-23; PRD O-2; AGENTS.md Shared Runtime Doctrine) — but App decomposition retains a standing "semantic ownership" claim over rehomed surfaces | Root runtime/ implementation (extracted per D-APP-73/SCA-APP-003) | App (Desktop/CLI client), PEC (client, D-PEC-56 as partially superseded), project loops | Checkout-contained project truth survives daemon loss (D-GOV-20 §operational-only); App had pre-daemon in-process path as migration posture | D-GOV/D-T0 rulings for doctrine; SCA-APP-003 for App-side effects; no instrument for forward contract evolution | DIVIDED — ownership of forward change unassigned; mirrors stale | A-F-016, A-F-023, A-F-024 |
| Work-surface / human-agent mediation | App (PRD goals 4, 23–25; PKG-02/PKG-08; D-APP-74 Woven Dialogue) | App frontend + instruction-root personas | Human operator; agents via personas; future embedded/companion reuse is charter framing only | Legacy loop-first UI retained through compatibility period (accepted PRD constraint) | D-APP rulings + SCA amendments (SCA-APP-004 exemplar) | CLEAR — single owner, disciplined amendment trail | A-F-015 (identity), A-F-020 |
| Coordination projection (PEC) | PEC (PRD v2.1; PEC-K-01..11) | PEC v2 (unbuilt); file truth remains producer of record | Harnesses on behalf of agents; owner dashboards | Total: file-native fallback is the invariant (kill test PEC-K-01); deleting PEC blocks nothing | D-PEC packets per tranche; §16 open decisions reserved to owner | CLEAR — best-specified optionality contract in the corpus | A-F-026 |
| Resource governance (candidate) | None — candidate architecture only; no accepted instrument exists in the repository | — | — | N/A (nothing exists to degrade) | Would require its own service/authority/data/degraded-mode contract before product scope (charter's own statement) | CORRECTLY ABSENT — no accepted surface claims it; absence is not a gap | — |
| SOW method layer | Root shared method (docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md, D-GOV-16; skills/scope-of-work; tools/scope_of_work) | HELPS_HUMANS-maintained skill/tool amendments (v1–v6.1) | Root (45), PEC (32), App (53 via earlier conversion), Piping | Legacy four-doc readers retained until owner-gated retirement (standard §7) | D-GOV rulings for the standard; skill/tool amendments for method | CLEAR owner; ERA-SKEWED consumers | A-F-007, A-F-022 |
| Decision/register mechanism | Per-loop: records govern, registers navigate (Root D-GOV; App D-APP self-described non-governing; PEC D-PEC; Tier-0 D-T0) | Each loop's human gate; cross-loop D-APP minting grant to PEC loop (D-T0-19 O-1A, serialized) | All loops; PEC v2 plans to parse registers (row identity only) | Registers are derivative; loss recoverable from records + git | Supersede-never-edit conventions; residual-row conventions (owner-ruled per loop) | CLEAR — consistent architecture; App's founding decomposition acceptance is the one weak instrument | A-F-001, A-F-013 |
| Notice routing | Changing tranche must ship (AGENTS.md change-notice rule; D-GOV-21 M6); receiving loop dispositions under own instruments | Root tranches (D-GOV-21/23/24/26 notices shipped) | App, domains/chirality (received); PEC, Piping (never received a D-GOV notice) | Downstream deterministic detection (manifest drift status) — alive but backlogged | AGENTS.md amendment for the rule itself | UNEVEN — delivery partial, disposition never exercised, one notice factually wrong | A-F-010, A-F-011, A-F-012 |
| Domain truth | Domain engines own authoritative domain truth (K-DOMAIN-1; PRD N-1 exception; App PKG-10 future boundary; PEC content-minimal) | Engines (frozen pec v0.4 instance; future OpenPipeStress fixture) | Chirality governs work around engines; App staged read/propose tools (D-APP-49..52) fenced | Engine loss is out of Chirality's correctness scope by construction | Tier-0 D-T0 rows per engine; per-op risk grading (D-T0-03) | CLEAR — boundary consistently restated at every layer examined | A-F-025 |
| Evidence-and-acceptance flow | Human owner (K-AUTH-1/2); evidence surfaces per loop (AgentRuns, receipts, snapshots) | All loops' runs and tranches | Owner judgment; reviewers; future PEC projection | Git is the event store; chat-only facts are transcribed into packets/receipts (observed practice) | Supersession instruments; SHA-bound rulings | STRONG with two open links at the newest Root records and terminal-state lags in App | A-F-001, A-F-003, A-F-006, A-F-018 |

# Section 5 — Charter challenge outcomes

Order per REVIEW_MANIFEST.json review_question_set. The charter was read only
after Sections 1–4's underlying examination was complete.

1. **Shared runtime ownership (ROOT).** Partially. Doctrine ownership is
   unambiguous (D-GOV-20, D-T0-23, PRD O-2, AGENTS.md). But no single Root
   package owns runtime "protocol, daemon, clients, sessions, tools,
   delegation, credentials, adapters, compatibility, security, migration, and
   release evidence" as *work*: Root's accepted decomposition covers the
   runtime as conformance slices (DEL-02-02 and related PKG-02/PKG-03 items),
   a faithful consequence of PRD-only scope sourcing. The charter's
   accepted-basis claim "runtime ownership must land at Root" is satisfied at
   doctrine level and untested at deliverable level. Divergence from the
   charter: I find the residual risk lives in the *App-side retained
   ownership* claim (A-F-023), which the charter's framing of Root-side
   coverage alone would miss. Findings: A-F-023, A-F-024.
2. **Producer, consumer, and fallback (CROSS_PRODUCT).** Mostly yes — see
   Section 4. Owners, consumers, and fallbacks are explicit for runtime
   (doctrine), work surface, PEC, SOW method, decisions, and domain truth.
   Two functions fail the "routed-change obligations explicit" clause: notice
   routing (obligations explicit, execution uneven and never dispositioned —
   A-F-010) and the runtime's forward-change path (unassigned — A-F-023).
3. **Four-category coverage without folder mimicry (ROOT).** Yes,
   demonstrably. The decomposition's §11.2 shows all four §4.1 categories
   covered by a many-to-many mapping over six work-domain packages, with no
   package coextensive with a category (DEC-003 records the deliberate
   refusal of category-mimicry; D-15 satisfied with zero deferrals). My
   register parsing corroborates the mapping columns exist and are populated.
   No divergence from the charter.
4. **Application composition boundary (CROSS_PRODUCT).** The corpus provides
   no accepted home for reusable work-surface/application-integration
   contracts, and — decisively — no accepted PRD commits to one. App PRD
   goals 21–22 and PKG-10 provide the *domain-profile* future boundary; the
   charter's richer "application environment profile" is expressly candidate
   architecture. Per the assertion-status discipline this is a genuine
   possible-PRD-gap to route to the owner, not a conformance finding; I
   record it in Section 7 rather than as a finding. The charter's own framing
   ("do not invent it through decomposition") matches the record's current
   posture.
5. **Standalone product and reusable work surface (APP).** The App PRD
   supports the standalone identity comprehensively. The reusable/embedded
   work-surface identity is present only as fragments (compatibility
   surfaces, provider-neutral contracts, packaging posture); nothing in the
   accepted basis governs embedding/companion/sidecar reuse, and the
   semantic-parity work that would begin it is not an instrument (condition
   18). Charter's "two identities" framing is clarified framing; the accepted
   basis currently warrants one identity plus reusable *contracts*, not a
   reusable *surface*. No conformance finding is available or warranted.
6. **Faithful human/agent mediation (APP).** The accepted basis is unusually
   strong here: PRD principles 26–30, FR-001..013, FR-041..044, journeys 7.2,
   and the D-APP-74 amendment all bind presentation to admitted sources,
   forbid prose-to-plan conversion, keep replay observational, and forbid
   panel-authored authority. The R5 managed-delegation surface (FR-060,
   7.11) binds the agent path to the same governance. I found no accepted
   surface permitting either path to bypass governance. Residual: parity
   between UI and direct-agent paths is owner-directed future work, not yet
   an instrument (condition 18) — consistent with the charter.
7. **Runtime client, not runtime authority (APP-ROOT).** Directionally yes at
   doctrine level; materially incomplete at the record level: the App
   decomposition's retained-semantic-ownership note, the stale D-APP-48
   mirrors, and the unverified D-APP-49 mirror obligations mean the App-side
   record still asserts more-than-client ownership of runtime surfaces.
   Findings A-F-016, A-F-023. Divergence: the charter frames this as an
   App-deliverable-scoping question; the record shows it is equally a
   missing-instrument question on the Root/Tier-0 side.
8. **Coordination without authority (PEC).** Yes, with the strongest
   invariant discipline in the corpus: PEC-K-01..11, §4.2 permanent
   non-goals, SOW-065..073 OUT rows with IN/OUT verification twinning
   (DL-8: SOW-025 tests the no-ruling-write boundary), and DEL-10-02/10-03
   as standing release-gating tests. The advisory blocker state is correctly
   labelled visibility-not-authority in every surface I checked. No
   divergence.
9. **Complexity-dependent availability (PEC).** Yes as designed: the §5 modes
   ladder is carried into constraints (C15) and scope (SOW-008), and
   graceful absence is release-gated (kill test). Unbuilt, so "available
   where concurrency warrants" is untested by construction. One doctrine
   dependency is honestly flagged but unresolved: lawfulness of concurrent
   Agent 0 operation absent a common parent is an open AGENTS.md question
   the PRD deliberately does not settle (SOW-086 deferred). Section 7 item.
10. **Optional planning and resource service (resource governance).** Nothing
    in the accepted basis establishes, requires, or depends on resource
    governance; no surface I examined treats it as scope, authority, or
    system of record. Its absence is correct per the assertion-status rules.
    The charter's description (consumes accepted system information; provides
    estimates/sequencing/locks/budgets/usage/cost/forecast; optional,
    replaceable, no authority) has no counterpart instrument to test against
    — outcome: correctly absent; any entry requires its own contract first.
11. **Human judgment remains the hinge (ALL).** Confirmed across all three
    products at every layer examined: Root's three-judgments model (PRD §4.2,
    §8.3) with K-GATE-1/D-GOV-02 keeping machine gates non-judgmental; App's
    NFR-023, approval-SHA gates, and F-APP-4; PEC's PEC-GAT-004/SOW-025 and
    human-only-act survivals from D-PEC-56. I looked specifically for silent
    acquisition of decision force by validators or conventions: the closest
    approaches are the App's founding "implicit approval" (A-F-013 — a
    provenance defect, not a machine usurpation) and era-skewed validator
    PASS claims (A-F-022). No machine gate has acquired human force.
12. **Domain truth remains situated (ALL).** Confirmed: K-DOMAIN-1 and the
    N-1 exception at Root; App PKG-10's future-boundary discipline with the
    D-APP-49..52 staging fenced and per-op risk-graded; PEC's content-minimal
    rule excluding domain content entirely. The pec.yaml interim state
    (A-F-025) is a labelling lag, not an absorption.
13. **Executable and warranted scope (SOW).** Sampled verdict (12 Root + 6
    PEC contracts): every sampled SOW traces to accepted register rows via
    non-empty frontmatter refs, has one owner deliverable, names outputs and
    evidence expectations per the matrix contract, and fits its envelope;
    write-locus boundary language uniformly denies self-authorization. No
    sampled SOW introduces a new product commitment through prose; the
    nearest misses are candidate AC/VER opacity (A-F-007) and PEC's recorded
    residuals (A-F-026). App SOW content was not re-sampled this pass (the
    recent D-APP-55/56 concordance corpus covers it far more densely than a
    review sample could; its closure evidence is an accepted-loop record).

# Section 6 — Disclosed-conditions assessment

For each of the twenty §4.5 basis-wide conditions: consequence assessment
beyond the disclosure, cross-referenced. None is presented as newly
discovered.

1. **D-GOV-27 EffectiveSHA unbound.** Escalated with consequence analysis:
   the debt has no carrying surface because no successor workplan is open —
   the two conditions compound. → A-F-001, A-F-006.
2. **SHA-role language conflicts.** Escalated: the conflict is between the
   accepted working surface and its accepting instrument, on a TRANSCRIBED
   product commitment (E-3), and will propagate into header-parsing tooling.
   → A-F-002.
3. **Amendments without verifying diff.** Partially mitigated by my
   independent count-reproduction (all headline counts match); content-level
   verification remains undischarged. → A-F-003.
4. **Receipt 52 as handoff.** Validated as recoverable but non-conformant to
   the loop's own handoff-state rule, aggravated by the stale
   HANDOFF_STATE.md file. → A-F-006.
5. **Completed workplan still ACTIVE.** Same navigation cluster; the
   deterministic pointer discipline (LOOP_INIT's anti-mtime rule) prevents
   mis-selection but not mis-orientation. → A-F-006.
6. **AC/VER candidate status machine-opaque.** Escalated: the opacity has no
   landing surface for the future acceptance act; six distinct prose
   formulations verified in a 12-contract sample. → A-F-007.
7. **App PRD identity via corpus v17.** Validated: all v17 pins reproduce
   CLEAN. Residual internal-identity defects (no version, stale date,
   duplicate §17) assessed as citation-integrity risk. → A-F-015.
8. **App decomposition acceptance provenance.** Escalated to REVIEW: the
   founding acceptance is attested only by the accepted artifact itself;
   later owner acts corroborate but cannot substitute for an instrument.
   → A-F-013.
9. **Invariant-coverage register absent.** Escalated: the
   required-or-deferred precondition has now been passed through at least two
   REVIEW-shaped closures without either branch being taken. → A-F-014.
10. **D-APP-48 mirror 12/12 stale.** Independently reproduced by hash;
    escalated because the stale pins are load-bearing for DEC-041 and
    Piping's D-30. → A-F-016; feeds A-F-023.
11. **App domain source manifest heavily drifted.** Reproduced exactly
    (119/129/219). Consequence folded into the notice/detection assessment:
    detection alive, remediation ownerless. → context for A-F-010.
12. **Chirality domain manifest drift + six missing ACTIVE pins.** Reproduced
    exactly (126/93/6); the six missing pins identified as retired agent
    contracts, tying the drift to specific ruled index changes. → A-F-012.
13. **Notice routing uneven/undispositioned.** Escalated: the disposition
    half of the rule has never been exercised; one delivered notice is
    factually wrong about its target. → A-F-010, A-F-011.
14. **PEC's 32 absent SOWs deliberate.** Validated: census 32/32 reproduced;
    wave scope (3 pre-P1 + 29 P1) matches D-PEC-63's ruled scope; not a
    coverage gap. No finding.
15. **Root/PEC SOW validation-era skew.** Escalated: no machine-readable
    tool-basis exists on the Root side, so future rerun findings cannot be
    classified without archaeology. → A-F-022.
16. **Domain packs consulted-only but evidentiary.** Used exactly so: both
    manifests recomputed as drift evidence, not treated as reviewed products.
    → A-F-010, A-F-012.
17. **Piping as notice-coverage exemplar.** Confirmed: Piping's coordination
    surface holds no D-GOV doctrine notice; its detection burden is wholly
    local. → A-F-010.
18. **App semantic-parity work not an instrument.** Confirmed by absence:
    SCA _LATEST ends at SCA-APP-004; no D-APP row establishes parity work.
    Treated throughout as not-basis; no absence-as-gap finding made.
19. **Resource governance optional candidate.** Confirmed by absence across
    every examined surface; assessed at Section 5 Q10 and boundary matrix.
    No finding (correctly absent).
20. **Charter is challenge material, not evidence.** Complied with: charter
    opened only after Sections 1–4 examination; every charter proposition
    tested against records; divergences recorded in Section 5 (notably Q1
    and Q7, where my account locates the risk differently than the charter's
    framing).

Product-specific condition lists were likewise assessed: Root conditions 1–10
map to A-F-001..A-F-009 and Section 7 (condition 9: instrument conflicts —
not independently examined, see below); App conditions 1–12 map to
A-F-011..A-F-021 and conditions 18/8 above; PEC conditions 1–5 map to
A-F-025, A-F-026, and validations recorded in Sections 3 and 5 (condition 5:
the frozen DAG exhibit's superseded 120-edge figures are correctly superseded
by the live 254-row/119-edge state, which I reproduced by parsing all 64
registers; D-PEC-66 records the mirrors as annotated).

# Section 7 — Standing questions and UNKNOWNs

Stated as owner-decision or information requests; none is a new requirement.

1. **Runtime forward-change ownership (owner decision).** Which accepted
   surface owns evolution of the shared runtime contract — a Root instrument
   derived from PRD O-2, or a continued App-side arrangement? The frozen
   basis holds both a Root doctrine claim and a standing App
   retained-ownership note, with no instrument deciding between them
   (A-F-023). Any resolution should also disposition the D-APP-48 pull
   mechanism (A-F-016).
2. **D-APP-49 mirror obligations (information request).** Whether the
   "field-for-field SHA-pinned mirrors of agents/AGENT_DOMAIN_ENGINE.md
   @77a327727" required by D-APP-49 still describe the rehomed
   runtime-contracts architecture is UNKNOWN at this pass: I verified the
   harness-contract package is now shims but did not trace where the type
   modules landed or whether their pins survive. An App-loop verification
   (not a review act) can settle this.
3. **Root initialization instrument conflicts (information request).** The
   disclosed unresolved conflicts involving AGENT_TASK absolute-path fields,
   validate_id_format.sh, the SOW validator's prefix set, and
   tools/REGISTRY.md (Root condition 9) were not independently examined this
   pass; their current state is UNKNOWN here. The owning record (Receipt
   51/D-GOV-27 fan-in evidence) should be the resolution surface.
4. **AC/VER acceptance-state representation (owner decision).** Before any
   acceptance act over Root's candidate criteria: one deterministic
   representation for acceptance state (A-F-007). The frozen basis cannot
   decide the mechanism; the SOW standard's amendment path can.
5. **Doctrine-notice recipient scope (owner decision).** Are
   doctrine-consuming loops without pins (PEC, Piping) intended recipients
   of D-GOV doctrine notices? The change-notice rule as written keys on
   pins/mirrors; the observed outcome (A-F-010) suggests the rule
   under-covers reliance-without-pins. Clarification is a doctrine act only
   the owner can direct.
6. **Concurrent Agent 0 lawfulness (owner decision, already flagged by the
   basis).** PEC's PRD §5 doctrine note and SOW-086 defer the root AGENTS.md
   amendment for concurrent Agent 0 operation without a common parent. PEC's
   P3+ value proposition presumes a resolution; the frozen basis leaves it
   correctly open. Recorded here so the dependency is visible at P1 packet
   time, not discovered at P3.
7. **Application-integration home (owner decision, charter-derived).** If
   reusable work-surface/embedding contracts are wanted, the frozen basis
   has no PRD warrant in any product; the lawful entry is a PRD amendment
   (Root or App) — never decomposition or SOW prose. This restates the
   charter's own constraint as an owner-decision request, consistent with
   condition 18.
8. **Retrospective App decomposition attestation (owner decision).** Whether
   to bind the current v3.2 bytes by a one-row SHA-bound confirmation
   (A-F-013). The frozen basis cannot repair founding provenance
   retroactively; only an owner act can convert corroboration into an
   instrument.
