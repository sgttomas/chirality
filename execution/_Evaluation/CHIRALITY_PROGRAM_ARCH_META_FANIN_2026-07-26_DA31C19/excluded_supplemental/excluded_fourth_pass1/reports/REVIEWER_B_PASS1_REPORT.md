---
reviewer: B
lens: horizontal-boundary-adversarial
review_freeze_commit: da31c19b5656dd74615e308c4215688971d33dc9
manifest_sha256: 8ac8abb86f064a2a1ef5c51c4eacbbf7b90497d78d1f7a92b55406a44a27096c
charter_sha256: 1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f
date: 2026-07-26
finding_count: 23
---

# Section 1 — Independent orientation account

Orientation was performed from governed records only, before the charter was
opened. HEAD of the review worktree verified equal to the freeze commit
`da31c19b5656dd74615e308c4215688971d33dc9`; tracked tree clean; manifest and
charter SHA-256 recomputed and matching. All hashes and counts below were
recomputed by me at the freeze unless marked otherwise.

## 1.1 Chirality Root

**Identity.** The root product of the repository root, defined by the adopted
PRD at `docs/PRD_ROOT.md` (recomputed sha256 `82f7ea2944e7…94b3`), which is a
pointer block plus the adopted Rev 5 candidate bytes, adopted by D-GOV-22
(exact-candidate-SHA ruling, 2026-07-25). A D-GOV-27 amendment-of-record note
supersedes §5.2 O-1's six-member instruction-surface enumeration by instrument
(authoritative enumeration `docs/SPEC.md` §0.2.1, eight members). Ruled genus
(RD-1): two-level formulation — canonical human-governed application
environment and generative operating form, containing a filesystem-native
agent operating system.

**Accepted basis and provenance.**
`execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` (recomputed
sha256 `14067a7d97c9…4cf7`), accepted by D-GOV-25 against
AcceptedCandidateSHA `ec62af070…`; the D-GOV-25 record assigns EffectiveSHA
`653fabc9b…` (PR #348) while the decomposition header itself says
"EffectiveSHA `ea0ad7a56…` (merge of PR #347)" — a live terminology conflict
(§2, B-F-007). Counts verified programmatically: scope ledger 103 rows (94
IN / 9 OUT / 0 TBD), deliverable register 45, objective register 7, forward
register 84, reverse register 51. 45 `ScopeOfWork.md` files exist, all
`INITIALIZED` (45/45 census recomputed), all pinning
`…SOFTWARE_DECOMP_v1_0.md@653fabc9b…` — a single uniform basis pin.
D-GOV register runs D-GOV-01..27; D-GOV-27 (initialization closing rulings)
carries an unbackfilled EffectiveSHA placeholder. Guard state
`execution/_harness/root_guards.yaml` records G1–G4 registered/passing.

**Current state.** `CURRENT_WORKPLAN.md` points at
`WORKPLAN_2026-07-25_root_initialization.md`, status
`ACTIVE — ROOT DELIVERABLE INITIALIZATION`, although that workplan's own stop
state says "After PR 2 merges this workplan is complete" and Receipt 52
records the closing tranche executed and merged. Receipt 52 is the de facto
initialization handoff; no dedicated current HANDOFF_STATE file exists. The
next phase (semantic enrichment or production dispatch) is owner-gated future
work.

**Integration and drift surfaces.** `domains/chirality/_Sources/Source_Manifest.csv`
recomputed at the freeze: 225 rows → 126 CLEAN / 93 DRIFT / 6 MISSING. Of the
six missing files, only **one** — `agents/AGENT_ORCHESTRATOR.md` — is pinned
`ACTIVE`; the other five are pinned `RETIRED` (this differs from the common
basis description; see §6, condition 12). Routed D-GOV notices: App loop
holds D-GOV-21/23/24/26; `domains/chirality/_Coordination/` holds
D-GOV-21/23/24 but not 26; the PEC and Piping loops hold no D-GOV doctrine
notices. Current-tool SOW validation rerun (read-only,
`tools/scope_of_work/validate_scope_of_work.py` at the freeze commit): Root
45/45 PASS.

## 1.2 Chirality App

**Identity.** Registered project loop at `projects/chirality-app-dev/`
(`chirality.project.json`). Accepted PRD `docs/PRD.md` (project-local),
recomputed sha256 `ef638f43ccae…4010`, exactly matching the
AUTHORITY_CORPUS.json v17 pin (binding commit `1cfd3e293…`). The PRD carries
no internal version number and contains two sections numbered §17
("Approval and Change Control" at line 1676 and "Shared Runtime and
Local-Agent Pilot Amendment" at line 1692). Identity of record is therefore
the corpus pin, as the register model (D-APP-38 Option D) intends.

**Accepted basis and provenance.**
`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
(recomputed sha256 `952d3cbf81b0…b08b`), gate posture "Gates 1-7 accepted by
implicit human approval per user instruction" (DEC-002), amended in place by
SCA-APP-001/-002/-003/-004 with topology preserved (78 scope items, 10
packages, 51 deliverables, 10 objectives — all verified by parsing the
document). The decomposition names one required companion register
(`contract_invariant_coverage_register.csv`, "created … or explicitly
deferred before REVIEW closure"); the `_Decomposition/` directory contains
only the main document — no companion register of any kind exists, and no
deferral ruling was found. 53 SOW + 53 `_STATUS.md` files (51 decomposition
deliverables + 2 PKG-00 control deliverables whose `decomposition_basis` is a
PKG-00 README); all 53 `IN_PROGRESS` (census recomputed). The 51
decomposition-based SOWs carry **five distinct** `decomposition_basis` commit
pins; four resolve to an identical pre-SCA-APP-002 blob
(`a907cda3…`, 2026-07-12/13), and one (`416b29033bba…`, pinned by six SOWs)
is not an object in the repository at all (`git cat-file -t` fails). Decision
register: 74 rows, all RULED, through D-APP-74. Current-tool SOW validation:
53/53 PASS.

**Current state.** Loop protocol LOOP_INIT → committed-HEAD workplan
selection (`WORKPLAN_2026-07-18b_app_dev_loop.md`) → receipts. Receipt 91
(daemon-as-service tranche) records checks passing and "owner merge of the
pull request is terminal", with no merge SHA; the run's HANDOFF_STATE still
reads `…PENDING_PR_AND_OWNER_MERGE`. SCA-APP-004 pointer:
`GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING`. Hard fences F-APP-1..5 in
force; F-APP-4 fences issuance. An orphan evidence tree
`execution/PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/`
sits beside the registered `PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle`.

**Integration and drift surfaces.** AUTHORITY_CORPUS.json v17: all eight pins
(six project docs + `agents/AGENT_SOFTWARE_DECOMP.md` `ad849d9a…` +
`agents/AGENT_DOMAIN_ENGINE.md` `bb2df717…`) recomputed **clean** at the
freeze. The D-APP-48 pull contract
(`_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`) pins 12 exports
at source commit `55a066fd…`; recomputed against the live tree: **12/12
mismatch** — yet the registered validator
`tools/coordination/validate_harness_contract_pull.py` exits "validation
passed" because it verifies pins only against the pinned commit's blobs.
`domains/chirality-app-dev/_Sources/Source_Manifest.csv` recomputed (paths
resolve project-root-relative, unlike the chirality domain manifest which is
repo-root-relative): 467 rows → 119 CLEAN / 129 DRIFT / 219 MISSING.
Runtime seams: root `runtime/README.md` declares the daemon "sole owner of
engines, credentials, sessions, delegation, turn locks, interruption, tools,
and local-model residency" with Desktop/CLI/projects as clients; the App
decomposition's Downstream Execution Notes state "app-dev deliverables retain
semantic ownership and acceptance evidence through the SCA-APP-003 impact
map" and OI-007 records the shared-runtime execution obligation.

## 1.3 PEC

**Identity.** `projects/pec/` — the optional coordination plane. PRD v2.1
(recomputed sha256 `de0a969cad15…4684`), v2.0 adopted by D-PEC-58, v2.1
clarification by D-PEC-61; invariants PEC-K-01..11; §4.2 permanent non-goals
(not a system of record, not a ruling surface, not an orchestrator, not a
lock manager, not a Git actor). Nothing in the PRD is an implementation
mandate; every build tranche needs its own owner-ruled packet (F-PEC-1
fences source work).

**Accepted basis and provenance.**
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.2 (recomputed sha256
`3e5be4e453ed…dd58`), status `current_basis`: rev 1.0 accepted at Gate 7
under D-PEC-60 (Gate Log verbatim rulings dated 2026-07-24), SCA-001/D-PEC-61
→ 1.1, SCA-002/D-PEC-64 → 1.2. Frontmatter's `accepted:` line dates the
"original Gate 7 owner ruling" 2026-07-25, conflicting with its own Gate Log
and the register (2026-07-24) — a date-level defect (B-F-012). Counts
verified: ScopeLedger 94 rows, Deliverables 64, ContextBudgetQA 64; 11
packages PKG-00..10. 32 SOWs exist (packages 00,01,02,03,04,08,10), all
pinned uniformly at `SOFTWARE_DECOMP.md@3623b958b`, whose blob I verified
byte-identical to the live rev-1.2 file. Census 32 INITIALIZED / 32 OPEN;
the 32 absent P2–P4 SOWs are deliberate sequencing (D-PEC-63 wave scope).
Current-tool SOW validation: 32/32 PASS.

**Current state.** `docs/STATUS.md` and `_COORDINATION.md` item 9 (which
explicitly supersedes item 8's numbers) give the calibrated dependency state:
64 registers / 254 rows = 135 ANCHOR + 119 EXECUTION / 62 nodes / 119 edges /
2 orphans / 0 SCCs / zero waivers / validator fully clean including
`--strict`; advisory blocker state 24 BLOCKED / 40 UNBLOCKED. Latest receipt:
112 (D-PEC-66 executed; the three Receipt-111 owner-routed items closed).
Next owner gates: P1 build-slice packets; WORKING_ITEMS activation. Recorded
REVIEW residuals (DEL-08-02 CLM-002/AX-006 provenance text; DEL-00-03
AC-005×VER-003 coverage gap) are carried in Receipt 112 — pre-disclosed, not
new. The domain-engine profile `_DomainEngines/profiles/pec.yaml` remains
ADOPTED at `integration_level: OPERATION_PROPOSAL` (L3) with
`profile_version: 0.2`; full supersession pending v2 implementation shape.

## 1.4 Cross-product surfaces established before charter reading

Tier-0 register (23 rows, D-T0-01..23) read in full: D-T0-19 (bridge lane +
cross-loop D-APP minting grant), D-T0-23 (shared-runtime convergence).
Shared SOW method layer read (`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`;
`tools/scope_of_work/`); root `AGENTS.md` (via project instructions) and both
project AGENTS overlays read in full; `runtime/README.md` read in full.
Resource governance: a repo-wide grep finds the term only in the charter —
no governed instrument mentions it. No repository instrument establishes the
proposed App semantic-parity work; the newest App SCA pointer is SCA-APP-004.

# Section 2 — Findings

### B-F-001 — Shared-runtime semantic ownership is divided between accepted records

```yaml finding
FindingID: B-F-001
Product: CROSS_PRODUCT
Surface: runtime/ ownership — AGENTS.md §Shared Runtime Doctrine; projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md §13 + OI-007; execution/_Decomposition/ (Root)
Assertion: Accepted doctrine (D-GOV-20, D-T0-23, AGENTS.md) makes root runtime/ Root-owned, but the accepted App decomposition states "app-dev deliverables retain semantic ownership and acceptance evidence" for the extracted runtime (Downstream Execution Notes; OI-007), while the accepted Root decomposition assigns runtime coverage only to DEL-02-02 Three-Layer Authority Boundary Conformance (SOW-027/SOW-035) and contains no deliverable owning runtime protocol, daemon, clients, adapters, conformance, migration, or release evidence.
EvidenceRefs:
  - AGENTS.md#Shared Runtime Doctrine
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#13 "Shared runtime promotion preserves this decomposition's existing package/deliverable topology… app-dev deliverables retain semantic ownership" [952d3cbf81b0]
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#11 OI-007
  - execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv#SOW-027,SOW-035 (both map only to DEL-02-02)
  - runtime/README.md#L7-11
  - docs/PRD_ROOT.md#§5.2 O-2 (runtime/ as operative layer (c)) [82f7ea2944e7]
Class: ownership_gap
Severity: REVIEW
DisclosedCondition: none (adjacent to §4.4 "test whether ownership and integration seams are sufficiently explicit")
Consequence: The program's most load-bearing shared component has no single accepted record answering "who owns a runtime contract change." A Root-side change today would have no Root deliverable to land conformance/acceptance evidence in; an App-side change is doctrinally a client acting on the owner's surface. Future domain applications registering as runtime clients cannot identify the compatibility counterparty.
SmallestAction: Owner decision naming the transitional arrangement explicitly — either a Root SCOPE_CHANGE adding runtime-substrate ownership deliverable(s), or a recorded ruling that App deliverables hold runtime semantic ownership for a bounded period with a stated end condition — routed through the D-GOV register and the SCA-APP-003 impact map.
Owner: Root governance (D-GOV register / Root SCOPE_CHANGE); App loop for the impact-map side
Confidence: HIGH
```

### B-F-002 — Six App SOWs pin an unresolvable decomposition_basis commit

```yaml finding
FindingID: B-F-002
Product: APP
Surface: ScopeOfWork.md of DEL-02-01, DEL-02-02, DEL-02-04, DEL-05-04, DEL-08-02, DEL-08-03
Assertion: Six App SOW contracts declare decomposition_basis "…Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@416b29033bbacb0bc3648d84033272b7ab4e6e11", and that commit is not an object in the repository at the freeze (git cat-file -t fails), so the declared accepted basis of these contracts cannot be resolved at all.
EvidenceRefs:
  - projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation/ScopeOfWork.md#frontmatter
  - git cat-file -t 416b29033bbacb0bc3648d84033272b7ab4e6e11 → "could not get object info" (at da31c19b5)
  - projects/chirality-app-dev/loop/LOOP_RECEIPTS.md#Receipt 90 Stale-Map-Delta (precedent of rewritten branch SHAs, e.g. 83a3a4733 → af52af478)
Class: trace_gap
Severity: REVIEW
DisclosedCondition: none
Consequence: The SOW schema's one provenance field is broken for six contracts — likely a rebased branch commit that never reached main. Any future CHECKING→ISSUED trace claim, checklist derivation record, or reviewer resolving decomposition_basis for these deliverables fails; the deterministic SOW validator does not resolve the commit, so this defect is invisible to the only automated check.
SmallestAction: Re-pin the six contracts' decomposition_basis to a commit reachable on main carrying the intended decomposition bytes (administrative repair, no content change), recorded in the loop receipt.
Owner: App loop (deliverable-local repair under its plan; no lifecycle effect)
Confidence: HIGH
```

### B-F-003 — App SOW basis pins are plural and uniformly pre-amendment stale

```yaml finding
FindingID: B-F-003
Product: APP
Surface: all 51 decomposition-based App ScopeOfWork.md files
Assertion: The 51 App SOWs carry five distinct decomposition_basis commit pins (15× b4d2c9ab2…, 14× ff59428ff…, 10× 0724f26f6…, 6× 416b29033… (unresolvable, B-F-002), 6× 2770fda4c…); every resolvable pin yields the identical 2026-07-12/13-era decomposition blob (sha256 prefix a907cda33835ebf0), which predates the in-place SCA-APP-002/-003/-004 amendments, so no App contract pins the live accepted decomposition bytes (952d3cbf81b0); no repin act exists. Root (45/45 @653fabc9b) and PEC (32/32 @3623b958b, blob verified identical to live rev 1.2) each maintain one uniform, live-matching pin.
EvidenceRefs:
  - programmatic census of decomposition_basis across projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md (53 files)
  - git show <pin>:…SOFTWARE_DECOMP_v3_2.md hashed at b4d2c9ab2/ff59428ff/0724f26f6/2770fda4c → a907cda33835ebf0… vs live 952d3cbf81b0…
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#Change Log (in-place amendments 2026-07-21..23)
Class: trace_gap
Severity: REVIEW
DisclosedCondition: partially assesses §4.5 condition 8 (weak App acceptance provenance) — the pin heterogeneity/staleness is additional to the disclosure
Consequence: "Accepted basis" for the App SOW corpus is plural and stale: the decomposition is amended in place under a stable filename while its consumers pin dead history, so which decomposition content a contract binds is answerable only by archaeology. Individual SOWs (e.g. DEL-02-01) have been content-updated for SCA-APP-004 while their pins were not, so the pin no longer even identifies the content era of its own contract.
SmallestAction: One administrative repin tranche moving all 51 contracts to the current accepted decomposition commit (or a ruled convention that App SOW pins are era markers, recorded in the SOW standard's project binding), receipt-recorded.
Owner: App loop; method question routes to HELPS_HUMANS / DELIVERABLE_SCOPE_OF_WORK_STANDARD.md
Confidence: HIGH
```

### B-F-004 — The D-APP-48 mirror is 12/12 stale and its validator is structurally unable to notice

```yaml finding
FindingID: B-F-004
Product: APP
Surface: execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json + tools/coordination/validate_harness_contract_pull.py
Assertion: All 12 export pins in the D-APP-48 pull contract mismatch the live files (recomputed sha256, 12/12 STALE — the shared-runtime tranche rewrote them to shims without repinning), yet the registered validator exits "harness contract pull validation passed" over this state, because it verifies each pin only against the blob at the contract's own pinned source commit (55a066fd…), never against the live tree.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json#exports (12 entries; source.commitSha 55a066fdff68…)
  - tools/coordination/validate_harness_contract_pull.py#L31-35, L93 (git_blob(commit,…) → sha256 compare)
  - recomputed live sha256 of all 12 sourcePaths at da31c19b5 → 0 OK / 12 STALE
  - projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md#Frontend contract surfaces (names this JSON as the pull-contract pin of record)
Class: observation
Severity: REVIEW
DisclosedCondition: §4.5 condition 10 (mirror entirely stale) — consequence analysis added: the divergence-detection architecture for this mirror is vacuous with respect to currency
Consequence: The mirror mechanism that the DEC-041 automation condition and the piping consumption lane rely on validates only its own frozen snapshot: it can never fail on live drift, so "validation passed" here is not evidence of a current mirror. Since the standing workplan names this JSON as the live pull-contract pin, a consumer following the plan gets a false-fresh signal. Which copy wins after divergence (live shims vs pinned exports) is undecided anywhere.
SmallestAction: Owner-routed disposition of the D-APP-48/D-APP-49 mirror obligations post-shared-runtime (repin, retire, or re-home to runtime/ contracts), plus a currency mode (or an explicit "snapshot-only, no currency claim" label) on the validator's output.
Owner: App loop decision register (D-APP row); coordinate with the runtime re-home under SCA-APP-003
Confidence: HIGH
```

### B-F-005 — The routed D-GOV-26 notice misidentifies its target corpus pins

```yaml finding
FindingID: B-F-005
Product: CROSS_PRODUCT
Surface: projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-26_SPEC_CONTRACT_AMENDMENTS.md
Assertion: The notice states that the App AUTHORITY_CORPUS.json "pins both docs/SPEC.md and docs/CONTRACT.md by sha256; both hashes change with this tranche" — but the corpus pins the App project's own docs/SPEC.md and docs/CONTRACT.md (verified clean against v17 at the freeze), not the root files D-GOV-26 amended; the root loop's own Receipt 52 M6 survey subsequently recorded "none-required — app-dev corpus pins resolve to project-local docs copies, verified by hash."
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-26_SPEC_CONTRACT_AMENDMENTS.md#Why this loop is notified
  - projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json#v17 (SPEC eee520f7…, CONTRACT 6d3a082c… — recomputed clean)
  - execution/_Coordination/LOOP_RECEIPTS.md#Receipt 52 ("M6 survey: none-required…")
Class: semantic_conflict
Severity: WARN
DisclosedCondition: assesses §4.2 App condition 10 (notice misidentifying its stale target) and §4.5 condition 13
Consequence: Notice routing keyed on bare relative paths collides across namespaces: "docs/SPEC.md" names different files at root scope and project scope. The shipped notice creates a false follow-on obligation ("re-pin the two files at the next corpus refresh") that the receiving loop should decline; undispositioned, it sits as standing misinformation on the coordination surface. The same collision class will recur for every project that mirrors root document names.
SmallestAction: Append a disposition note to the notice (declined-as-misdirected, citing Receipt 52's M6 survey); require routed notices to carry repo-root-anchored paths.
Owner: App loop (disposition); root loop M6 mechanism (path convention)
Confidence: HIGH
```

### B-F-006 — Notice routing and pin maintenance do not close the loop for agents/ changes

```yaml finding
FindingID: B-F-006
Product: CROSS_PRODUCT
Surface: AGENTS.md agent-index change-notice rule; domains/chirality/_Sources/Source_Manifest.csv; PEC and Piping coordination surfaces
Assertion: The agent-index change-notice rule requires routed notices to each loop pinning touched agents/ files, yet (a) domains/chirality still pins agents/AGENT_ORCHESTRATOR.md as ACTIVE although D-GOV-18's ruled rename (ORCHESTRATOR→PROJECT_SETUP) removed it — the only genuinely ACTIVE-and-missing pin among the six missing files (the other five are pinned RETIRED); (b) domains/chirality holds notices for D-GOV-21/23/24 but not D-GOV-26; (c) the PEC and Piping loops hold no D-GOV doctrine notices although PEC's accepted decomposition pins root AGENTS.md and docs/DECOMPOSITION_STANDARD.md as method basis (R2/R9); and (d) zero notice dispositions appear in any App loop receipt (0 references to NOTICE_D-GOV files in LOOP_RECEIPTS.md).
EvidenceRefs:
  - AGENTS.md#Governance Integration Rules (agent-index change-notice rule)
  - domains/chirality/_Sources/Source_Manifest.csv#SRC row agents/AGENT_ORCHESTRATOR.md ArchiveState=ACTIVE (recomputed MISSING); five sibling rows ArchiveState=RETIRED
  - domains/chirality/_Coordination/ (NOTICE_D-GOV-21/23/24 present, 26 absent)
  - find over projects/pec/execution/_Coordination and _DomainEngines/pec: no NOTICE_D-GOV_* file
  - grep -c "NOTICE_D-GOV" projects/chirality-app-dev/loop/LOOP_RECEIPTS.md → 0
Class: ownership_gap
Severity: REVIEW
DisclosedCondition: §4.5 conditions 12 and 13 — with the correction that only one of the six missing chirality-domain pins is ACTIVE
Consequence: The two-channel design (routed notice + downstream deterministic drift check) currently fails on both channels for some consumers: PEC/Piping received no notices, and the drift check on domains/chirality has been reporting the same 93-DRIFT/1-ACTIVE-MISSING state without a consuming disposition. Notices that do arrive accumulate undispositioned, so the routing rule produces write-only artifacts rather than closed loops. Downstream detection therefore does depend on exactly the thing the rule says it must not depend on alone.
SmallestAction: One notice-disposition sweep per receiving loop (adopt/amend/decline each held notice, receipt-recorded); repair or retire the AGENT_ORCHESTRATOR ACTIVE pin; extend M6 routing to loops whose accepted bases pin root doctrine (PEC at minimum).
Owner: each receiving loop for dispositions; root loop M6 mechanism for routing coverage; domain regeneration workflow for the manifest
Confidence: HIGH
```

### B-F-007 — "EffectiveSHA" is a conflicted role name across Root decomposition surfaces

```yaml finding
FindingID: B-F-007
Product: ROOT
Surface: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md header vs docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md
Assertion: The decomposition header states EffectiveSHA = ea0ad7a56… (merge of PR #347) while the accepting decision record states EffectiveSHA = 653fabc9b… (merge of PR #348); the 45 SOWs and the initialization workplan pin 653fabc9b…, and D-GOV-26's EffectiveSHA 31b8dc94a… is separately named the work-graph accepted basis — the same role word denotes three different commits depending on surface.
EvidenceRefs:
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#L9 [14067a7d97c9]
  - docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md#L8
  - execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md#Accepted upstream basis
  - execution/PKG-01_*/1_Working/DEL-01-01_*/ScopeOfWork.md#frontmatter (653fabc9b…)
Class: semantic_conflict
Severity: WARN
DisclosedCondition: §4.5 condition 2 — consequence analysis added
Consequence: Any tool or reader keying "EffectiveSHA" from the decomposition header binds PR #347's state, not the SOW basis; the role register that would fix this is itself a pending Root deliverable (DEL-05-03 SHA Role Register), so the conflict is presently curable only by reading the decision record. Cross-product reviewers replicating provenance will disagree depending on entry surface.
SmallestAction: One-line header correction (or role-splitting annotation "CandidateMergeSHA vs EffectiveSHA") in the decomposition working surface, executed as the amendment-surface act it is; longer-term, DEL-05-03 is the decomposed home.
Owner: Root loop (decomposition amendment surface; D-GOV-25/27 precedent for annotation-not-overwrite)
Confidence: HIGH
```

### B-F-008 — Root closure-state chain: complete workplan still ACTIVE, receipt standing in for a handoff file

```yaml finding
FindingID: B-F-008
Product: ROOT
Surface: execution/_Coordination/CURRENT_WORKPLAN.md; WORKPLAN_2026-07-25_root_initialization.md; LOOP_RECEIPTS.md Receipt 52
Assertion: The named current workplan's goal is complete (Receipt 52 records the closing PR-2 tranche executed; the workplan says "After PR 2 merges this workplan is complete") yet CURRENT_WORKPLAN.md still marks it ACTIVE with no successor, and the initialization handoff exists only as Receipt 52 rather than the explicit handoff state the Handoff-state rule (AGENTS.md Governance Integration Rules) requires a stopping workflow to emit.
EvidenceRefs:
  - execution/_Coordination/CURRENT_WORKPLAN.md#Status ACTIVE
  - execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md#Stop state
  - execution/_Coordination/LOOP_RECEIPTS.md#Receipt 52
  - AGENTS.md#Governance Integration Rules (Handoff-state rule)
Class: omission
Severity: WARN
DisclosedCondition: §4.5 conditions 4 and 5 — consequence analysis added
Consequence: The root loop's own doctrine distinguishes receipts (check outcomes, not governed truth) from handoff states (accepted upstream snapshot, closure verdict, rerun requirements); a fresh session following LOOP_INIT lands on an ACTIVE pointer for a finished phase and must reconstruct closure from a receipt the doctrine says is not that record. This is the exact stale-pointer failure mode the practitioner harness's GEN-7 checks exist to catch on other loops.
SmallestAction: Repoint or restate CURRENT_WORKPLAN (e.g. status COMPLETE—AWAITING_OWNER_PHASE_SELECTION) and emit a minimal initialization HANDOFF_STATE naming the accepted snapshot and open items already listed in Receipt 52.
Owner: Root loop coordination surface (agent-closeable; no owner ruling needed beyond direction)
Confidence: HIGH
```

### B-F-009 — D-GOV-27's EffectiveSHA remains unbound

```yaml finding
FindingID: B-F-009
Product: ROOT
Surface: docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md
Assertion: D-GOV-27's EffectiveSHA field still reads "(merge of the closing-tranche PR into main; backfilled by a later tranche per precedent)" — the ruling that flipped all 45 deliverables to INITIALIZED and assigned ResponsibleParty is not yet SHA-bound, and Receipt 52 records the debt without a due mechanism beyond "the next tranche".
EvidenceRefs:
  - docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md#L6
  - execution/_Coordination/LOOP_RECEIPTS.md#Receipt 52 ("D-GOV-27 EffectiveSHA backfill owed to the next tranche")
Class: trace_gap
Severity: WARN
DisclosedCondition: §4.5 condition 1 — consequence analysis added
Consequence: K-AUTH-2-style binding for the initialization phase's terminal ruling depends on a promised future act; until backfilled, the 45 INITIALIZED states and ResponsibleParty assignments trace to a record whose effective commit is unnamed, and the backfill precedent has no watchdog (no receipt/validator checks for outstanding placeholders).
SmallestAction: Backfill the merge SHA in the next tranche as promised; consider a self-check detector for unbound EffectiveSHA placeholders (the RULING_SHA_TBD detector precedent exists in the governance harness).
Owner: Root loop next tranche; governance harness for the detector
Confidence: HIGH
```

### B-F-010 — App invariant-coverage register neither present nor deferred; App decomposition has no companion registers at all

```yaml finding
FindingID: B-F-010
Product: APP
Surface: projects/chirality-app-dev/execution/_Decomposition/
Assertion: The accepted decomposition names contract_invariant_coverage_register.csv as a required companion that "must be created or explicitly deferred before REVIEW closure" (§2.2, DEC-015, 10B checklist); the _Decomposition directory contains only the main document — no companion register of any kind — and no deferral ruling exists in the 74-row register.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Decomposition/ (directory listing: 1 file)
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#2.2, #10B, DEC-015 [952d3cbf81b0]
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md (no deferral row)
Class: omission
Severity: REVIEW
DisclosedCondition: §4.5 condition 9 — consequence analysis added
Consequence: The decomposition's own acceptance checklist (10B) is unsatisfied on its own terms, and CONTRACT K-* invariant coverage is checkable only through the coarse §10A.1 family table. Because the App decomposition is a monolith (a structure PEC's DL-1 explicitly declined as "the app-dev monolith"), there is also no machine-truth surface for scope/deliverable data; every count check must parse prose tables. The condition has survived four in-place amendments without a deferral act.
SmallestAction: An explicit owner deferral row (smallest), or creation of the register as a bounded documentation tranche; no topology change involved.
Owner: App loop decision register (D-APP row)
Confidence: HIGH
```

### B-F-011 — Orphan PKG-03_Harness_Runtime_Core tree duplicates a package number outside the decomposition

```yaml finding
FindingID: B-F-011
Product: APP
Surface: projects/chirality-app-dev/execution/PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/
Assertion: An evidence tree claiming PKG-03/DEL-03-06 exists beside the registered PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle, although the accepted decomposition's PKG-03 contains only DEL-03-01..04 and no PKG-03_Harness_Runtime_Core package exists in any accepted topology.
EvidenceRefs:
  - projects/chirality-app-dev/execution/ (both PKG-03_* directories listed)
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#8 PKG-03 (DEL-03-01..04)
Class: overreach
Severity: WARN
DisclosedCondition: §4.2 App condition 7 — consequence analysis added
Consequence: The filesystem package namespace no longer bijects to the decomposition: PKG-03 and DEL-03-06 are ambiguous identifiers inside this project, and any glob-driven tool over execution/PKG-*/1_Working/DEL-*/ (the loop's own discovery idiom in the standing plan Step 0) can pick up an unregistered tree. It currently lacks _STATUS.md so lifecycle censuses are unaffected, but that is accident, not design.
SmallestAction: Owner-ruled disposition: archive/rename the orphan tree (e.g. under a non-PKG namespace) or register it through scope change; never both names on one number.
Owner: App loop decision register
Confidence: HIGH
```

### B-F-012 — PEC decomposition frontmatter misdates its own original acceptance

```yaml finding
FindingID: B-F-012
Product: PEC
Surface: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md frontmatter
Assertion: The frontmatter reads "accepted: 2026-07-25 (original Gate 7 owner ruling under D-PEC-60; …)", but the document's own Gate Log dates the Gate 7 ACCEPTED ruling 2026-07-24, and the D-PEC-60 register row records the ruling and Gates 1–7 confirmation on 2026-07-24.
EvidenceRefs:
  - projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md#frontmatter accepted: [3e5be4e453ed]
  - projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md#Gate Log (Gate 7, 2026-07-24)
  - projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md#D-PEC-60
Class: semantic_conflict
Severity: WARN
DisclosedCondition: none
Consequence: A date-level contradiction inside the identity block of an accepted basis document: a consumer citing "accepted 2026-07-25 under D-PEC-60" propagates a date the decision record refutes (2026-07-25 belongs to the rev-1.2/SCA-002 acceptance under D-PEC-64). Trivial to fix, corrosive if copied into derivative packages.
SmallestAction: One-line frontmatter correction through the decomposition's amendment surface, recorded in the next receipt.
Owner: PEC loop (working-surface amendment)
Confidence: HIGH
```

### B-F-013 — pec.yaml still asserts a live L3 lane that PEC's accepted records declare sunset

```yaml finding
FindingID: B-F-013
Product: CROSS_PRODUCT
Surface: _DomainEngines/profiles/pec.yaml vs projects/pec/docs/PRD.md §13 and projects/pec/AGENTS.md
Assertion: The ADOPTED machine-readable profile still declares integration_level "OPERATION_PROPOSAL" (L3) and authoritative_artifacts over the frozen v0.4 trees, while PEC's PRD v2 §13 records the L3 operation-proposal lane "sunset with the old product" and the PEC AGENTS overlay states the lane "is not an agent lane"; the pivot is carried only in profile comments, and the App-side multi-engine registry (D-APP-51/52) registered profileId "pec" against this profile.
EvidenceRefs:
  - _DomainEngines/profiles/pec.yaml#integration_level, #authoritative_artifacts, profile_version 0.2
  - projects/pec/docs/PRD.md#13 (profile superseded when v2 has shape; L3 lane sunset) [de0a969cad15]
  - projects/pec/AGENTS.md#Governance Pointers ("not an agent lane")
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md#D-APP-51, D-APP-52, D-APP-65 (piping/PKG-09 transport parked)
Class: semantic_conflict
Severity: REVIEW
DisclosedCondition: §4.3 PEC condition 1 (profile awaits full supersession) — consequence analysis added
Consequence: Two live surfaces answer "what may an agent do through the pec domain-engine lane" oppositely, and the machine-consumed one gives the permissive answer. The bridge-lane tools that read this profile were live-exposed under D-APP-51/52 before the pivot; nothing in the profile's machine fields tells such a consumer the lane is retired. The declared safeguard is comment prose, which registries do not parse.
SmallestAction: A minimal machine-field amendment (e.g. integration_level annotation or a lane_status field) under the existing D-PEC-59-style owner-directed follow-on, without attempting the full v2 supersession early; verify the App-side registry behavior against it.
Owner: Tier-0/D-T0 register (profile is a tier-0 surface) with PEC loop execution; App loop for the registry side
Confidence: MEDIUM (the live consumer's current behavior with the frozen instance was not executed in this review)
```

### B-F-014 — App AGENTS overlay operates as live authority while stamped draft

```yaml finding
FindingID: B-F-014
Product: APP
Surface: projects/chirality-app-dev/AGENTS.md frontmatter
Assertion: The project overlay carries status "draft" (created 2026-06-15, never amended to live) while functioning as the loop's active agent-posture, attribution-rule, and shared-runtime-boundary surface; the sibling PEC overlay is stamped "live" and version-annotated.
EvidenceRefs:
  - projects/chirality-app-dev/AGENTS.md#frontmatter status: draft
  - projects/pec/AGENTS.md#frontmatter status: live, amended 2026-07-25
Class: observation
Severity: WARN
DisclosedCondition: §4.2 App condition 11 — consequence analysis added
Consequence: Machine-readable status contradicts operational reality on the one file that defines the loop's delegation discipline; under the governance harness's own DRAFT_BASIS_AS_BINDING detector class this is exactly the pattern flagged elsewhere as drift.
SmallestAction: Flip the status field (with amended date) in an ordinary documentation tranche.
Owner: App loop
Confidence: HIGH
```

### B-F-015 — App terminal receipt and run handoff disagree; terminal merge SHA unrecorded

```yaml finding
FindingID: B-F-015
Product: APP
Surface: projects/chirality-app-dev/loop/LOOP_RECEIPTS.md Receipt 91; execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/HANDOFF_STATE.md
Assertion: Receipt 91 records the daemon-service tranche as EXECUTED with "owner merge of the pull request is terminal" but carries no merge SHA (Examined-Through is a pre-merge commit), while the run's HANDOFF_STATE still declares APPDEV_DAEMON_SERVICE_IMPLEMENTATION_COMPLETE_PENDING_PR_AND_OWNER_MERGE — the two coordination surfaces disagree about whether the terminal act happened.
EvidenceRefs:
  - projects/chirality-app-dev/loop/LOOP_RECEIPTS.md#Receipt 91 (Examined-Through e9068c87d…; PR #333)
  - projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/HANDOFF_STATE.md#Status
Class: trace_gap
Severity: WARN
DisclosedCondition: §4.2 App conditions 9 and 12 — consequence analysis added
Consequence: The D-APP-57 receipt contract's value is the exact cursor; here the ledger's newest cursor pre-dates the merge it declares terminal, and the handoff a successor session would read says the merge is still pending. State must be re-derived from Git (which the loop doctrine does prescribe), but both derivative surfaces are wrong in opposite directions.
SmallestAction: Append the merge SHA in the next receipt's stale-map delta and annotate the handoff status line closed (append-only), per the loop's own live-tree-wins rule.
Owner: App loop next iteration
Confidence: HIGH
```

### B-F-016 — App decomposition's REF-006 PRD pin is one corpus version stale

```yaml finding
FindingID: B-F-016
Product: APP
Surface: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md §2 References
Assertion: REF-006 pins docs/PRD.md at sha256 d9bcdcb701de… (the corpus v16 hash); the accepted PRD identity is the v17 pin ef638f43ccae… (changed 2026-07-24), so the accepted decomposition's source-reference table cites superseded PRD bytes; REF-001..005 match v17 because only the PRD changed at v17.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#REF-006 [952d3cbf81b0]
  - projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json#v16/v17 PRD hashes
  - recomputed live sha256 of projects/chirality-app-dev/docs/PRD.md = ef638f43ccae…
Class: trace_gap
Severity: WARN
DisclosedCondition: adjacent to §4.5 condition 7 (identity via corpus pin)
Consequence: The REF-006 lag class is the same one D-APP-35/D-APP-38 ruled on for deliverable _REFERENCES.md files, but the decomposition's own REF table sits outside the corpus-refresh mechanism, so it silently drifts one version behind every authority-doc edit. A reader verifying the decomposition against "its" PRD hash gets a mismatch against the live accepted PRD.
SmallestAction: Fold decomposition REF-table refresh into the D-APP-38 corpus-bump procedure, or annotate REF-006 as era-pinned.
Owner: App loop (D-APP-38 mechanism)
Confidence: HIGH
```

### B-F-017 — App decomposition's method reference is a foreign machine-absolute path

```yaml finding
FindingID: B-F-017
Product: APP
Surface: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md header
Assertion: The Method Reference is "/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md" — a machine-absolute path from a different checkout that does not resolve in this repository; REF-007 does pin the method file by sha256 (ad849d9a…, which matches live agents/AGENT_SOFTWARE_DECOMP.md), so identity is recoverable, but the named path is dead.
EvidenceRefs:
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#header Method Reference [952d3cbf81b0]
  - recomputed sha256 agents/AGENT_SOFTWARE_DECOMP.md = ad849d9a9274… (matches REF-007)
  - AGENTS overlays' Path Anchors sections (both projects mandate {REPO_ROOT} derivation, not machine-absolute paths)
Class: observation
Severity: WARN
DisclosedCondition: none
Consequence: The accepted basis document violates the path-anchor discipline both AGENTS overlays impose on briefs, and the root harness's GEN-8 machine-absolute-path lint class; harmless while humans read it, but it is the kind of pointer PEC-style parsers and future tooling will choke on, and it encodes a provenance to a checkout that no longer exists.
SmallestAction: Amend the header path to the repo-relative agents/AGENT_SOFTWARE_DECOMP.md in a documentation tranche (REF-007's hash already carries identity).
Owner: App loop
Confidence: HIGH
```

### B-F-018 — Candidate AC/VER status is prose-only across all three products' SOW corpora

```yaml finding
FindingID: B-F-018
Product: CROSS_PRODUCT
Surface: docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md; all 130 ScopeOfWork.md files
Assertion: The SOW schema (chirality-deliverable-sow/v1) has no deterministic field for the acceptance status of AC-*/VER-* content; "candidate until lifecycle acceptance" is expressed in free prose (present in 45/45 Root, 26/53 App, 29/32 PEC SOWs by case-insensitive grep), so no validator or checklist consumer can distinguish candidate from accepted criteria mechanically in any product.
EvidenceRefs:
  - docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md#3 (frontmatter schema — no status field), #4 (checklist tool contract)
  - programmatic grep census across the three SOW corpora
  - execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md#Authority basis item 3 ("they remain candidate until later lifecycle acceptance")
Class: omission
Severity: WARN
DisclosedCondition: §4.5 condition 6 — extended: the condition is method-layer-wide, not Root-specific
Consequence: The deterministic checklist deriver emits AC rows without acceptance status; any consumer (REVIEW, future issuance gates, PEC's planned register parsers) must infer status from varied prose or from lifecycle state alone. Because the method layer is shared, fixing it per-product would fork the schema.
SmallestAction: Owner-routed method amendment (HELPS_HUMANS) adding one optional deterministic status marker to the SOW schema/id-catalog, applied prospectively; no per-contract rewrite required.
Owner: HELPS_HUMANS / DELIVERABLE_SCOPE_OF_WORK_STANDARD.md governance (D-GOV-16 lineage)
Confidence: HIGH
```

### B-F-019 — Root working surface still declares ResponsibleParty TBD after D-GOV-27 assigned it

```yaml finding
FindingID: B-F-019
Product: ROOT
Surface: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md §9 and OI-011
Assertion: Section 9 states "ResponsibleParty is TBD for every deliverable … (OI-011)" and OI-011 remains OPEN, while the D-GOV-27 tranche assigned "Ryan Tufts" across the deliverable register and all 45 _CONTEXT.md files (recorded in the same document's Change Log and DEC-021 note, and verified in the register CSV) — OI-011's own resolution condition ("a later planning act assigns responsibility") has been met without the issue or §9 being updated.
EvidenceRefs:
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md#9 (first paragraph), #12 OI-011, #Change Log 2026-07-25 D-GOV-27 entry [14067a7d97c9]
  - execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv (ResponsibleParty "Ryan Tufts" rows)
Class: semantic_conflict
Severity: WARN
DisclosedCondition: §4.1 Root condition 4 (OI-011 stale) — consequence analysis added
Consequence: The accepted control surface contradicts its own authoritative companion register on an accountability fact; a reader of §9 alone concludes no one is responsible for anything. The register is declared the amendment surface, so the register wins — but the working surface was updated for DEC-021's objective changes in the same tranche and not for this one, showing the surface-sync step is best-effort.
SmallestAction: Close OI-011 with a dated disposition citing D-GOV-27 and correct the §9 sentence, via the amendment surface.
Owner: Root loop (decomposition amendment surface)
Confidence: HIGH
```

### B-F-020 — Domain source manifests are heavily stale and use divergent path conventions

```yaml finding
FindingID: B-F-020
Product: CROSS_PRODUCT
Surface: domains/chirality/_Sources/Source_Manifest.csv; domains/chirality-app-dev/_Sources/Source_Manifest.csv
Assertion: Recomputed at the freeze: domains/chirality 126 CLEAN / 93 DRIFT / 6 MISSING (of 225); domains/chirality-app-dev 119 CLEAN / 129 DRIFT / 219 MISSING (of 467) — and the two manifests resolve RepoRelPath against different bases (repo root vs project root), so no single deterministic checker can process both without per-domain knowledge.
EvidenceRefs:
  - programmatic recompute over both manifests (path base established empirically: app-dev rows resolve only with the projects/chirality-app-dev/ prefix)
  - domains/chirality-app-dev/_Sources/Source_Manifest.csv#header + first rows (project-relative execution/PKG-00_… paths)
Class: observation
Severity: WARN
DisclosedCondition: §4.5 conditions 11 and 12 — consequence analysis added
Consequence: Both derivative corpora are far from their sources (47% and 75% non-clean respectively), so retrieval or RESEARCH over these snapshots would serve stale text at scale; the inconsistent path convention means the "downstream deterministic detection" channel needs per-domain adapters, and a naive repo-root checker reports 461/467 missing for app-dev (as my first pass did), masking the real 129-row drift signal.
SmallestAction: Regenerate both snapshots under their owning domain workflows, and standardize (or field-declare) the path base in the manifest schema.
Owner: domain regeneration workflows (derivative packages; cite accepted upstream snapshots per the derivative-package rule)
Confidence: HIGH
```

### B-F-021 — PEC's planned parsers consume an App-loop-owned receipt contract with no routed change path

```yaml finding
FindingID: B-F-021
Product: CROSS_PRODUCT
Surface: projects/pec/docs/PRD.md PEC-RCN-002/§16.8; projects/pec/execution/_Decomposition SOW-013/DEL-02-03; D-APP-57
Assertion: The accepted PEC basis binds its receipts-ledger parser to "the D-APP-57 contract where a ledger has adopted it" — a contract created and amendable by the App loop's own register for its own ledger — and no App-side record carries any compatibility or notice obligation toward PEC as a consumer; whether other ledgers adopt the contract is PEC's open §16.8, but the change path for the contract itself is unowned from PEC's side.
EvidenceRefs:
  - projects/pec/docs/PRD.md#7.1 Receipt, #9.2 PEC-RCN-002, #16.8 [de0a969cad15]
  - projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-013, DEL-02-03 (L envelope, per-loop grammars)
  - projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md#D-APP-57 (contract scoped to the app-dev ledger)
Class: ownership_gap
Severity: WARN
DisclosedCondition: none
Consequence: Low today (PEC unimplemented; parser tolerances and PEC-ORI-006 honesty rules bound the failure to stated coverage limits), but at P1 the first cross-loop grammar change would break a consumer the producer does not know it has. This is the exact producer/consumer/compatibility pattern the program handles well elsewhere (corpus pins, M6 notices) and has not yet extended to loop-ledger grammars.
SmallestAction: When a P1 packet authors DEL-02-03, record the dependency in the App loop (one register row or notice acknowledging PEC as a D-APP-57 grammar consumer), or resolve §16.8 first.
Owner: PEC P1 packet + App loop register; §16.8 owner decision
Confidence: HIGH
```

### B-F-022 — Root AGENTS.md predates the Root decomposition it now sits above

```yaml finding
FindingID: B-F-022
Product: ROOT
Surface: AGENTS.md
Assertion: The runtime doctrine and agent index contain no reference to the accepted Root decomposition, its six packages, its 45 deliverables, or the initialization state — a reader of the doctrine alone cannot discover that the repository root is itself a materialized product under execution/PKG-*.
EvidenceRefs:
  - AGENTS.md (no occurrence of PKG-01..06 root packages or the decomposition path)
  - execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md (accepted 2026-07-25)
Class: observation
Severity: INFO
DisclosedCondition: §4.1 Root condition 7 — consequence analysis added
Consequence: Mild: LOOP_INIT §1 does route readers to the D-GOV-21 root-execution-root fact, so discovery works through the loop path; the doctrine file is simply one product-shape generation behind, which matters mainly for agents entering through AGENTS.md without the loop.
SmallestAction: One doctrine sentence (M2 tranche) noting root execution/ carries the accepted root decomposition — only when a routine doctrine amendment is next open; not worth its own tranche.
Owner: Root instruction surface (M2, owner-gated)
Confidence: HIGH
```

### B-F-023 — Identifier families are reused across products with only path context disambiguating

```yaml finding
FindingID: B-F-023
Product: CROSS_PRODUCT
Surface: program-wide ID grammar (PKG-XX, DEL-XX-YY, SOW-NNN, OBJ-NNN, OI-*, DEC-*)
Assertion: Root, App, and PEC each mint PKG/DEL/SOW/OBJ/OI/DEC identifiers from the same unprefixed grammar (e.g. "SOW-064" is a Root scope item about currency obligations, an App scope item about MCP catalogs, and PEC's directed-bootstrap item; "PKG-03" denotes three different packages), so cross-product records are unambiguous only while every citation carries a path or product qualifier; decision IDs (D-GOV/D-APP/D-PEC/D-T0) are the only product-qualified family.
EvidenceRefs:
  - execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv#SOW-064
  - projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#SOW-064
  - projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-064
  - projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md#9 Vocabulary (the one surface that explicitly disambiguates its package-token collisions)
Class: observation
Severity: INFO
DisclosedCondition: none
Consequence: Currently managed by discipline (PEC's vocabulary map is the model; the SOW external-reference grammar DEL-XX-YY-REQ-NNN qualifies within a product but not across products). Risk concentrates in cross-product surfaces — Tier-0 records, routed notices (see B-F-005's path-collision variant), and any future PEC record tier that models several loops' Package/Deliverable entities in one store.
SmallestAction: None now; when PEC P1 lands, require loop-qualified identity in its record-tier keys (its PRD §7.1 already implies this via Loop tenancy).
Owner: no action owner required; PEC P1 design inherits the constraint
Confidence: HIGH
```

# Section 3 — Coverage matrix

| Layer | Examined (FULL or SAMPLE) | Depth verdict | Breadth verdict | FindingRefs | Residual unknowns |
|---|---|---|---|---|---|
| ROOT / PRD | SAMPLE (pointer block, provenance key, §1 identity, §5.2 O-2/O-3, §8/§10.2 via grep; ~35% of 1055 lines) | Sound: adoption chain D-GOV-21→22→23/24 exact-SHA-bound; provenance-label discipline unusually strong | Runtime named as operative layer (c) but no engineering commitment beyond conformance | B-F-001 | Unread PRD middle sections could carry further runtime obligations (judged unlikely from the forward register's 84-item population) |
| ROOT / AuthorityChain-Corpus | SAMPLE (D-GOV register FULL; DIRECTIVE/CONTRACT/SPEC/TYPES via citations and amendment records only) | Ratification chain (D-GOV-09) and supersession mechanics coherent | Instruction-surface enumeration now 8-member via SPEC §0.2.1; pointer mechanism works but demands multi-hop reads | B-F-022 | Exact current text of DIRECTIVE/CONTRACT/SPEC/TYPES not independently read |
| ROOT / Decomposition+Registers | FULL (main doc; all 5 register CSVs parsed; counts verified 103/45/7/84/51) | Gate log, ruled dispositions, F4 both directions verified present; OI discipline exemplary | Six work-domain packages, no category mimicry (verified §11.2 spread) | B-F-007, B-F-019 | The one missing amendment-verifying diff (condition 3) not reconstructed |
| ROOT / ScopesOfWork | FULL structural (45/45 frontmatter, headings, pins) + content sample 12 (2 per package) + current-tool validation 45/45 PASS | Uniform basis pin 653fabc9b; heading/matrix conformance in all sampled | Conformance-slice framing (OI-004) consistent | B-F-018 | Semantic fitness of unsampled 33 contracts |
| ROOT / Decisions | FULL (register 201 lines; D-GOV-25/27 records sampled at cited lines) | Exact-candidate-SHA pattern consistent since D-GOV-21 | Cross-product effects (notices) recorded per decision | B-F-009 | Per-decision record bodies beyond D-GOV-25/27 headers |
| ROOT / Coordination-CurrentState | FULL (LOOP_INIT, CURRENT_WORKPLAN, initialization workplan, Receipt 52) | Receipt content complete and specific | Pointer/handoff hygiene lags the doctrine's own rules | B-F-008 | none |
| ROOT / Integration-Drift | FULL for the surfaces named in §4 (source manifest recomputed; guard state read; notice files enumerated) | Guard state G1–G4 registered/passing (state surface read, guards not re-executed) | Notice + pin channels leak (see findings) | B-F-005, B-F-006, B-F-020 | Guard validators not re-run |
| APP / PRD | SAMPLE (§16, both §17s, identity/hash verification, targeted greps; ~15% of 1720 lines) | Identity holds only through corpus v17 pin (verified clean); duplicate §17 confirmed | §16 correctly points to v3.2 topology | B-F-016 | PRD body requirements (KG/FR families) not read; parity of §16 counts vs decomposition verified only at headline level |
| APP / AuthorityChain-Corpus | FULL (AUTHORITY_CORPUS.json all 17 versions; all 8 v17 pins recomputed clean) | Corpus mechanism works and is currently clean | Ref names "AGENT_SOFTWARE_DECOMP.md" etc. are root-relative while doc refs are project-relative — same collision family as B-F-005 | B-F-005 (family), B-F-016 | none |
| APP / Decomposition+Registers | FULL (main doc read in full; counts parsed 78/10/51/10) | Gate provenance thin ("implicit human approval"); in-place amendment chain coherent | No companion registers at all; invariant register unmet | B-F-010, B-F-017 | none |
| APP / ScopesOfWork | FULL structural (53/53 frontmatter/pins) + content sample: DEL-02-01 (partial full-read) + 22 summarized (2 per package) + current-tool validation 53/53 PASS | Content current (SCA-APP-004-aware) but provenance pins broken/stale | PKG-00 control deliverables pin a README as basis — coherent once explained, undocumented in the SOW standard | B-F-002, B-F-003 | Semantic fitness of unsampled contracts; mediation-path depth (see Section 5 Q6) |
| APP / Decisions | FULL (register 100 lines, 74 rows) | Ruling records SHA-bound with occasional backfill; D-APP-72/73/74 rest on "owner explicitly instructed" without packets — weaker but recorded | Cross-loop minting grant (D-T0-19) explicitly governed | — | Individual packet bodies not read |
| APP / Coordination-CurrentState | FULL (LOOP_INIT, standing plan, Receipts 90–91, SCA _LATEST) | Receipt contract (D-APP-57) validated design; cursor gap found | Handoff/receipt disagreement | B-F-015 | Receipts 1–89 unexamined individually |
| APP / Integration-Drift | FULL for named surfaces (pull contract + validator executed read-only; domain manifest recomputed; runtime README; runtime-client seam paths confirmed existing) | Mirror stale; validator blind | Runtime ownership divided | B-F-001, B-F-004, B-F-011, B-F-014, B-F-020 | Behavior of frontend runtime-client code not executed |
| PEC / PRD | FULL (490/490 lines) | Invariant set and non-goals crisp; compliance posture section models the D-GOV-01 boundary explicitly | Optionality engineering (§5 modes ladder, kill test) is the program's best-articulated fallback contract | — | none |
| PEC / AuthorityChain-Corpus | FULL overlay (AGENTS.md); profile header + machine fields read | Overlay current (amended per D-PEC-64) | Profile lags accepted records | B-F-013 | Profile validator not re-run |
| PEC / Decomposition+Registers | FULL (main doc 662 lines; 3 register CSVs row-counted 94/64/64) | Gate log verbatim rulings; two adversarial-verification rounds recorded with defect counts | DL-8 twinning and DL-15 declared-duplication rules directly answer the duplicated-truth lens | B-F-012 | Register cell-level content beyond counts |
| PEC / ScopesOfWork | FULL structural (32/32, uniform pin verified byte-identical to live) + content sample DEL-10-10 (partial full-read) + 14 summarized + current-tool validation 32/32 PASS | Highest provenance care of the three corpora (self-discloses its own stale sibling pointer) | 32 absent SOWs deliberate (D-PEC-63 wave scope) | — | Unsampled contracts; the recorded REVIEW residuals accepted as disclosed |
| PEC / Decisions | FULL (register 84 lines, D-PEC-01..66) | Ruling verbatims carried; residual-row convention consistently applied | Pointer rows to tier-0 avoid duplicated authority — a model answer to my lens | — | Packet bodies not read |
| PEC / Coordination-CurrentState | FULL (STATUS.md, _COORDINATION.md, Receipts 110–112) | Supersession discipline explicit (item 9 supersedes item 8's numbers) | Calibrated invariants (254/119/0 SCC) internally consistent across all three surfaces | B-F-012 (date only) | none |
| PEC / Integration-Drift | FULL for named surfaces (profile, shared-runtime boundary, D-PEC-56 partial supersession chain) | D-PEC-56 supersession precisely scoped (behaviors 4/7 survive) | Receipt-grammar dependency on App loop unowned | B-F-013, B-F-021 | none |

# Section 4 — Boundary matrix

| Function | Semantic owner per accepted basis | Producers | Consumers | Fallback/degraded | Routed change path | Verdict | FindingRefs |
|---|---|---|---|---|---|---|---|
| Shared runtime (daemon, sessions, engines, delegation) | Root by doctrine (D-GOV-20, D-T0-23, AGENTS.md); **but** App decomposition retains "semantic ownership and acceptance evidence" of the extracted implementation | runtime/ workspace code (extracted by App loop tranches) | App Desktop/CLI, PEC (future v2 client seam DEL-07-05), future domain apps | Daemon-as-service self-healing (Receipt 91); no accepted degraded-mode contract for clients when daemon absent | Split: D-GOV for doctrine; D-APP/SCA-APP-003 for implementation — no single path | DIVIDED — the review's clearest ownership defect | B-F-001, B-F-004 |
| Work surface / human-agent mediation | App (PRD/decomposition PKG-02/03/06/08; K-AUTH human gates) | App frontend + harness | Human owner; agents via governed dispatch | Loop/file-native work continues without the App entirely (all governed acts are file acts) | D-APP register + SCA machinery | OWNED; reusable-surface identity remains clarified framing only, not accepted scope | — |
| Coordination projection (PEC) | PEC (PRD v2; PEC-K-01..11) | PEC reconciler over file truth (future) | Harnesses, human dashboards | Exemplary: graceful absence is a product invariant with a standing kill test; deletion degrades throughput never correctness | D-PEC register; §16 open decisions enumerated | OWNED and best-in-program for optionality | B-F-021 (one inbound grammar dependency unowned on the producer side) |
| Resource governance (candidate) | None — appears in no governed instrument (verified by repo-wide grep) | n/a | n/a | n/a (absence is the current state) | Would require its own PRD/decision instruments | CORRECTLY ABSENT; charter-only candidate; its lock/freeze semantics would touch the human-authority boundary and must not arrive via decomposition prose | — (Section 7 question) |
| SOW method layer | Root governance (D-GOV-15/16; docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md; tools/scope_of_work) | HELPS_HUMANS amendments (v1–v6.1) | Root, App, PEC SOW corpora + TASK skill + validators | Legacy four-doc readers retained until owner-ruled retirement (§7 of standard) | D-GOV register; PEC routes tool requests via REQUEST file to HELPS_HUMANS | OWNED; one schema gap (candidate status) and one consumer-era question resolved by my freeze-time rerun: 130/130 PASS under the current tool | B-F-018 |
| Decision/register mechanism | Per-product registers, all self-described non-governing pointers to human rulings; Tier-0 for cross-project | Each loop; PEC loop may author D-APP rows under the D-T0-19 O-1A grant (packet-only, serialized) | All loops; reviewers | Registers are navigation; per-decision records govern on disagreement | Owner rulings only; residual-work row convention shared across loops | OWNED; the cross-loop minting grant is explicitly bounded — a model of lawful shared-surface writing | — |
| Notice routing | Root M6 mechanism + AGENTS.md change-notice rule | Root loop (D-GOV tranches) | App, domains, PEC, Piping loops | Downstream deterministic drift checks are the declared backstop | Root tranche ships notices; receivers disposition under own instruments | LEAKY — coverage uneven, dispositions absent, one notice mistargeted, backstop checks unconsumed | B-F-005, B-F-006 |
| Domain truth | Domain engines / situated products (K-DOMAIN; App PKG-10 future boundary; F-APP-3) | Domain loops (piping; frozen pec v0.4 instance) | Root governance reads; App descriptor-only tools; agents via proposal lanes | Proposal-gated; apply-class acts human-only | Tier-0 register for profiles/lanes | OWNED with one stale machine surface | B-F-013 |
| Evidence-and-acceptance flow | Human owner (K-AUTH-1/2); evidence in checkout-contained records | All loops (receipts, AgentRuns, snapshots) | REVIEW/EVALUATION, future PEC record tier | Files+Git are the substrate; no service dependency | CHANGE for Git state; owner merges terminal | OWNED; weakest links are cursor/handoff hygiene at loop edges | B-F-008, B-F-009, B-F-015 |

# Section 5 — Charter challenge outcomes

Question set per REVIEW_MANIFEST.json (13 items). My independent account was
formed first; divergences from the charter's framing are stated per item.

1. **Shared runtime ownership (ROOT).** No — no single Root package owns
   runtime protocol/daemon/clients/sessions/tools/delegation/credentials/
   adapters/compatibility/security/migration/release evidence. Root coverage
   is DEL-02-02 boundary conformance only (SOW-027/035); the engineering
   surface's acceptance evidence sits in App deliverables by the App
   decomposition's own accepted words (B-F-001). The charter's premise that
   "the Root PRD already places runtime/ in the operative product" is
   confirmed (O-2, TRANSCRIBED); its expectation that the decomposition
   "must assign its contract and continuing conformance work" is half-met:
   conformance yes, contract ownership no. Divergence: the charter frames
   this as an assignment task; the basis shows it is an active conflict
   between two accepted records, which is stronger than the charter implies.

2. **Producer, consumer, and fallback (CROSS_PRODUCT).** Explicit for PEC
   (exemplary), for the authority corpus, and for the decision mechanism;
   implicit-to-broken for the runtime mirror (B-F-004), notice routing
   (B-F-005/006), loop-ledger grammar (B-F-021), and domain manifests
   (B-F-020). See Section 4. Divergence: none — the charter's question is
   well-posed; the basis answers it unevenly.

3. **Four-category coverage without folder mimicry (ROOT).** Yes. Six
   work-domain packages; §11.2 demonstrates every category spanning ≥4
   packages and no package coextensive with a category; D-15 satisfied with
   zero deferred categories; verified counts. No finding. Divergence: none.

4. **Application composition boundary (CROSS_PRODUCT).** The corpus provides
   no home for reusable work-surface or application-environment-profile
   contracts, and that absence is lawful: the profile is charter-declared
   candidate architecture, and no accepted PRD commits to it. Root PKG-06
   (variant service, promotion pathway) and App PKG-10 (domain future
   boundary) are the nearest lawful anchors. This is a genuine PRD-level
   question, not a decomposition gap — recorded in Section 7, not as a
   finding. Divergence: none; the charter itself forbids counting absence.

5. **Standalone product and reusable work surface (APP).** The accepted App
   basis governs one product; the reusable-surface identity appears nowhere
   as accepted scope. SCA-APP-004's compatibility-preservation discipline
   (routes, SSE names, state rollback) incidentally keeps the embedding
   option open, but nothing distinguishes "incidental presentation
   assumptions" from exportable contract. Concordance question for the
   owner; no conformance finding is lawful. Divergence: the charter's
   two-identity framing is coherent but has zero footprint in accepted
   records — reviewers should resist retrofitting it.

6. **Faithful human/agent mediation (APP).** Structural evidence supports
   it: SOW-054..058 (structured permission decisions, persisted before SDK
   return), DEL-06-01 overlay, hooks fail-closed for write/shell/domain/
   subagent, K-AUTH human-only professional acts, and the D-APP-55/56
   concordance run's 1,115-row claim census with zero AUTHORITY_CONFLICT.
   I did not execute or trace the runtime paths; depth here is register- and
   contract-level. Verdict: supported at the accepted-record level,
   UNKNOWN at the code-behavior level (out of my sampled depth; noted in
   the coverage matrix). Divergence: none.

7. **Runtime client, not runtime authority (APP↔ROOT).** Presently false in
   one direction: the App is doctrinally a client but its accepted
   decomposition retains semantic ownership of the runtime it extracted
   (B-F-001). The transitional arrangement may be intended — but no record
   names it transitional or gives an end condition. Divergence: the charter
   states the target ("App deliverables limited to client integration…");
   the basis documents the opposite as accepted text, which makes this the
   review's principal owner-decision request.

8. **Coordination without authority (PEC).** Yes, comprehensively: PEC-K-02/
   -06, permanent OUT rows SOW-065..073 with DL-8 verification twins
   (SOW-025 tests the no-ruling-write property), DEL-10-03, C-13, and the
   AGENTS overlay's binding restatement. No finding. Divergence: none — the
   basis is stronger than the charter's ask.

9. **Complexity-dependent availability (PEC).** Yes: the §5 modes ladder is
   accepted product text; PEC-K-11 makes mode-proportionality an invariant;
   zero-coordination modes are zero-contact; the kill test is a release
   gate. The concurrent-Agent-0 doctrine question is explicitly deferred
   (SOW-086, OUT/deferred) rather than silently assumed — the PRD flags that
   PEC's own lawfulness argument for concurrent Agent 0s awaits a root
   AGENTS.md amendment. Divergence: none; preserve SOW-086 as the open
   design question it is.

10. **Optional planning and resource service (resource governance).**
    Nothing to test: the term appears in no governed instrument (verified).
    The charter's own constraints (never system of record, never authority,
    locks/freezes attributable to accepted human/workflow authority) are the
    right entry conditions for any future instrument; its lock/freeze
    vocabulary would interact with the human-authority boundary (K-AUTH
    family) and with PEC's "no lock manager" non-goal — so a future service
    must be neither PEC nor confused with it. Recorded as Section 7
    questions. Divergence: none possible on this basis.

11. **Human judgment remains the hinge (ALL).** Supported everywhere I
    probed: every acceptance in all three products traces to a verbatim or
    transcribed owner act; fences (F-APP-4, F-PEC-1) hold issuance and
    source work behind human gates; the D-APP-64 latitude overlay carves out
    exactly the non-consequential space and keeps truthful attribution as
    the firm limit. The riskier patterns — App's "implicit human approval"
    gate posture, "conditional pre-ruling" language in D-APP-51/52, PEC's
    batch-halt clearing mid-wave — are all still recorded owner acts, though
    with thinner provenance than the exact-candidate-SHA pattern. My
    validator finding (B-F-004) shows a machine check that under-detects
    rather than one that usurps judgment. Divergence: none.

12. **Domain truth remains situated (ALL).** Supported: K-DOMAIN, App
    PKG-10's future-boundary posture (descriptor-only tools, apply excluded
    outright per D-APP-50), F-APP-3, PEC content-minimality, and Root
    DEL-06-05 Domain Engine Truth Boundary. The one seam: pec.yaml's
    machine fields still advertise a live L3 lane over the frozen instance
    (B-F-013). Piping (consulted-only) received no D-GOV doctrine notices —
    an inheritance-coverage observation folded into B-F-006. Divergence:
    none.

13. **Executable and warranted scope (SOW).** Root and PEC: yes — single
    live-resolvable basis pins, uniform schema conformance, current-tool
    validation 45/45 and 32/32 PASS at the freeze, context envelopes
    respected (no XL anywhere; every L carries notes). App: contracts are
    schema-valid (53/53 PASS) and content-current, but warrant is impaired:
    six contracts pin an unresolvable basis commit, the rest pin uniformly
    stale bytes, and the invariant-coverage companion is missing
    (B-F-002/003/010). No SOW examined introduces a new product commitment
    through prose; the PEC DEL-10-10 sample is a model of refusing exactly
    that (it routes its own gating-authority question to the owner via
    CON-001). Divergence: none.

# Section 6 — Disclosed-conditions assessment

Format: condition → assessment (validation vs escalation), finding
cross-reference. Rediscovery is avoided: where I only confirmed a
disclosure, I say so and add consequence.

1. **D-GOV-27 EffectiveSHA unbound.** Confirmed at the record. Escalated one
   step: no watchdog exists for placeholder debt. → B-F-009.
2. **Root SHA-role language conflicts.** Confirmed; three-way (header vs
   D-GOV-25 vs D-GOV-26 roles). Consequence: surface-dependent provenance;
   decomposed cure exists (DEL-05-03). → B-F-007.
3. **Accepted amendments without one verifying diff.** Not independently
   reconstructed. Partial mitigation verified: all headline counts
   (103/45/7/84/51) recomputed stable, and DEC-014..021 enumerate the edits.
   Residual risk confined to prose dispositions. No finding; validation
   with residual UNKNOWN.
4. **Receipt 52 as handoff.** Confirmed; conflicts with the Handoff-state
   rule the root doctrine itself imposes. → B-F-008.
5. **Completed-but-ACTIVE workplan.** Confirmed. → B-F-008.
6. **AC/VER candidate status machine-opaque.** Confirmed and extended: the
   gap is method-layer-wide (all three products), so a per-product fix would
   fork the schema. → B-F-018.
7. **App PRD identity via corpus v17.** Validated: the v17 pin matches the
   live file exactly; the mechanism works. Consequence noted: identity is a
   single JSON file with no internal-version cross-check; the stale
   docs/MANIFEST.json remains a decoy surface. No new finding.
8. **App decomposition acceptance provenance weaker.** Confirmed ("implicit
   human approval per user instruction", DEC-002). Consequence: combined
   with in-place amendment and plural SOW pins (B-F-003) the App basis has
   the weakest identity chain of the three products; assessed under
   B-F-003's context rather than as its own finding.
9. **Invariant-coverage register absent, not deferred.** Confirmed; extended
   with the observation that no companion register of any kind exists.
   → B-F-010.
10. **D-APP-48 mirror 12/12 stale.** Confirmed by recompute; escalated: the
    registered validator passes over the stale state by design. → B-F-004.
11. **App domain source manifest heavily drifted.** Confirmed by recompute
    (119/129/219) with the path-base caveat. → B-F-020.
12. **Chirality domain manifest drift + six missing ACTIVE pins.**
    Partially confirmed, **partially corrected**: drift matches
    (126/93/6), but only one of the six missing files
    (agents/AGENT_ORCHESTRATOR.md) is pinned ACTIVE; the other five are
    pinned RETIRED, for which absence may be expected. The basis
    description overstates the defect; the real defect is one ACTIVE pin
    orphaned by the D-GOV-18 rename. → B-F-006, B-F-020.
13. **Uneven notice routing/disposition.** Confirmed and quantified (App 4
    notices, zero dispositions; chirality domain 3 of 4; PEC and Piping
    zero). Escalated: both channels (notice and drift-check consumption)
    are currently open loops. → B-F-005, B-F-006.
14. **PEC's 32 absent SOWs deliberate.** Validated: wave scope and census
    match D-PEC-63 exactly (32 INITIALIZED / 32 OPEN recomputed). No
    finding.
15. **Root/PEC SOW validation-era identities differ.** Resolved at the
    pass/fail level by direct test: I reran the current validator
    (tools/scope_of_work/validate_scope_of_work.py at freeze commit
    da31c19b5) read-only over all three corpora — Root 45/45, App 53/53,
    PEC 32/32 PASS. The QA-item-20 harmonization therefore did not
    invalidate Root's or App's accepted validations at the exit-code level;
    residual skew, if any, lives in warning-class/QA-item judgments, which
    PEC alone has had dispositioned (D-PEC-66). Validation with a stated
    tool basis.
16. **Domain packs consulted-only but evidentiary.** Used exactly so: the
    two manifests supplied the drift/notice evidence. → B-F-006, B-F-020.
17. **Piping consulted-only exemplar.** Checked only for notice coverage
    (none present); folded into B-F-006. Not treated as a reviewed product.
18. **App semantic-parity work not established.** Validated: newest SCA is
    SCA-APP-004; no parity instrument exists. Correctly absent; no finding.
19. **Resource governance optional candidate.** Validated: zero governed
    mentions. Correctly absent; Section 7 carries the entry conditions.
20. **Charter is challenge material only.** Complied with: orientation
    preceded charter reading; every charter-derived probe in Section 5 is
    answered from basis evidence; two places where the review-package
    framing and the records diverge (condition 12's "six ACTIVE"; the
    charter's runtime-assignment framing vs the live ownership conflict)
    are themselves reported as evidence.

# Section 7 — Standing questions and UNKNOWNs

Stated as owner-decision or information requests; none is a new requirement.

1. **Runtime ownership end-state (owner decision).** Does the owner intend
   App deliverables to retain shared-runtime semantic ownership
   transitionally, and if so until what event? A one-row ruling naming the
   arrangement and its end condition would dissolve B-F-001's ambiguity
   without any scope change.
2. **Runtime mirror disposition (owner decision).** After the shared-runtime
   re-home, are the D-APP-48/D-APP-49 pinned-mirror obligations still live
   obligations, retired, or re-homed to runtime/ contracts? (B-F-004; the
   basis cannot decide which copy is meant to win.)
3. **Reusable work surface and application-environment profile (owner
   decision, PRD-level).** Whether the reusable work surface is a Root
   requirement, an App capability, or both — currently uncommitted anywhere;
   any instantiation must arrive through a PRD/governance act, not
   decomposition (charter assertion-status rules and my Section 5 Q4/Q5).
4. **Resource governance entry conditions (information request).** If ever
   instrumented: its lock/freeze authority must be attributable to accepted
   human/workflow authority (K-AUTH family), it must not overlap PEC's
   permanent "not a lock manager" non-goal, and its optionality needs a
   PEC-K-01-grade falsifiable absence test. The frozen basis cannot decide
   whether the service is wanted at all.
5. **Notice-channel closure (owner direction).** Should notice dispositions
   be a required receipt element (the D-APP-57 contract has no field for
   them)? The basis shows notices shipping and never being consumed
   (B-F-006); whether that is acceptable is an owner call.
6. **PEC §16 open decisions** — especially §16.8 (receipt-contract adoption
   by other ledgers) and §16.9 (event-contract home), which are the two with
   cross-product ownership consequences (B-F-021; SOW-074's deferred
   runtime/ write). The PRD correctly reserves these; they should be
   answered before P3, per its own fencing.
7. **UNKNOWN (frozen basis cannot decide):** whether the 416b29033bba…
   commit pinned by six App SOWs ever existed on any shared branch (it may
   be a rebased-away local commit; only reflog archaeology outside this
   repository could tell). The repair (B-F-002) does not depend on the
   answer.
8. **UNKNOWN:** the semantic content of the one missing verifying diff for
   Root's post-candidate amendments (condition 3); count-stability is
   verified but prose-level equivalence is not reconstructable from the
   freeze alone.
