# Fan-in classification — TANDEM-REVIEW-20260726 (charter step 6)

Classifier: HELP_HUMAN (Agent 0), supervising review manager, acting in the EVALUATION
capacity per owner direction. Inputs: the two frozen pass-1 reports, their validation
records, and the two frozen challenge returns (hashes in RUN_MANIFEST.md). Method: each
distinct issue classified per the charter — AGREED, RESOLVED_BY_EVIDENCE,
STANDING_DIVERGENCE, SHARED_BLIND_SPOT_RISK, or STALE_INPUT. Agreement is not proof;
disagreement is not failure; nothing was averaged. Both reviewers' pass-1 reports remain
frozen; challenge-stage revisions live only in the challenge records and are cited as such.

## 1. AGREED (independently found, or confirmed on challenge with evidence re-run)

| # | Issue | Findings | Severity of record | Note |
|---|---|---|---|---|
| 1 | **App decomposition §13 claims semantic ownership of the shared runtime against D-GOV-20 / D-T0-23 / AGENTS.md / App PRD §17** | B-001 (BLOCK); A challenge CONFIRM | **BLOCK** — the review's only BLOCK | A's pass-1 "no duplicate owners" statement is superseded by its own challenge confirmation (A did not sweep §13; admitted). Sole reviewed-basis contradiction between accepted instruments on ownership. |
| 2 | D-APP-48 pull-contract validator passes while all 12 pins are stale (undeclared observation boundary) | A-014 ≡ B-004; mutual CONFIRM | REVIEW | Found independently by both via the same measurements — strongest convergence in the review. |
| 3 | D-GOV-27 EffectiveSHA unbound; four Root SOWs un-repinnable until backfill | A-003 ≡ B-012+B-013; mutual CONFIRM | REVIEW | A's "7 hunks" corrected to 6 (B challenge); substance unchanged. |
| 4 | Root decomposition header mislabels `ea0ad7a56…` as EffectiveSHA (E-3 violated on DEL-05-03's own artifact) | A-005 ≡ B-011; mutual CONFIRM | REVIEW→WARN band (A: WARN, B: REVIEW) — both agree on facts; severity difference immaterial to routing | One-label correction. |
| 5 | Root-doctrine notice coverage: 0 notices for D-GOV-20/22/25/27; PEC and Piping 0 doctrine notices ever | A-027 ≡ B-007; mutual CONFIRM | **REVIEW** (converged: A revised WARN→REVIEW in challenge) | Identical 13-file inventory derived independently. |
| 6 | App's authority corpus pins only App-local docs — no deterministic detector for Root doctrine drift; D-GOV-26 notice misstates the detection path | B-006 ≡ A-020; mutual CONFIRM | REVIEW (B) / A adopted B's anchor and upgraded its related A-027 | Hash-proof reproduced by both. |
| 7 | Piping D-30 consumption record stale, fails validator, never notified; 8 tool-registry generations behind its declared source | B-005; A challenge CONFIRM | REVIEW | Two-hop inheritance (Root→App→Piping) with no owner for the second hop. |
| 8 | `flow-a.contract.v0.1.0` identity orphaned by the runtime rehome; second unreconciled version identity `@chirality/runtime-contracts@0.1.0` | B-003; A challenge CONFIRM (+ corroboration: same version string spans an 8-generation registry divergence) | REVIEW | Tier-0 decision required (D-T0-07). |
| 9 | App has no requirement-ID-level trace instrument; 23/31 NFRs untraced on both sides; §11.4/§11.5 zero citations | A-012 ≡ B-020(NFR half); mutual CONFIRM | REVIEW | B's own pass-1 NFR count (27) revised to A's 23 in challenge. |
| 10 | App shared-runtime client migration has no scope item/deliverable; visible only in 16 of 53 `_STATUS.md` Remaining blocks | B-022; A challenge CONFIRM (identical 16-ID list) | REVIEW | |
| 11 | App PRD duplicate §17 + unsuperseded App-ownership assertions (Principle 8, Goal 10, FR-122/124/126/128) vs the §17 amendment | B-025; A challenge CONFIRM (verbatim) | REVIEW | |
| 12 | App decomposition acceptance rests on implicit approval, never re-gated across four in-place amendments | A-015; B challenge CONFIRM | REVIEW | B endorses A's mitigation note (each SCA had its own ruling). |
| 13 | App 53 SOWs pin five decomposition commits, none matching the freeze; **one pin (`416b29033…`) unresolvable in the frozen repository** | A-013; B challenge CONFIRM + ADD-MISSING-EVIDENCE (the unresolvable pin; four others resolve to one identical historical blob) | REVIEW (strengthened) | Six named contracts carry the unresolvable basis. |
| 14 | `CLAUDE.md` missing from the instruction-surface enumeration in Root decomposition §9, 45/45 `_CONTEXT.md`, and all SOW write-locus clauses, while guards enforce it | A-001; B challenge CONFIRM | REVIEW | Machine gate stricter than written authority. |
| 15 | C-4 closure claim (Receipt 44) not satisfied — README Public Export Boundary still omits `runtime/`; README internally inconsistent | A-002; B challenge CONFIRM + B revised its own C-4 coverage row ("COVERED-BY-REGISTER but materially open") | REVIEW | |
| 16 | Root cross-product PRD-identity / coverage-instrumentation asymmetry (program-level coverage statement unanswerable for App) | A-026 ≡ B-024(partial); mutual CONFIRM | REVIEW | Routed as ODR, both reviewers. |
| 17 | ResponsibleParty contradiction across Root surfaces incl. 45 self-contradicting `_CONTEXT.md` and 34 SOWs | A-006 ≡ B-014; mutual CONFIRM | WARN | Count resolved: see §2. |
| 18 | App invariant-coverage register absent, no deferral ruling; breach-vs-pending turns on unestablished REVIEW closure | A-017 ≡ B-023; mutual CONFIRM | WARN (MEDIUM confidence, A's conditional adopted by B) | |
| 19 | Root working-surface propagation defects: §7 OBJ-004 row missing DEL-06-04 (A-004); D-GOV register row 39 cites §0.2.2 (A-007, unchallenged, manager-verified anchor) | A-004 CONFIRM by B; A-007 manager spot-verified | WARN | |
| 20 | `domains/chirality` dangling ACTIVE `AGENT_ORCHESTRATOR` pin; no successor row; no D-GOV-18 notice; 41% pin drift backlog | A-008 ≡ B-017 (+B-018); mutual CONFIRM | WARN | Both corrected the disclosed condition (see §5). |
| 21 | App REF-006 PRD pin stale by one revision (159→159 requirement sets identical; delta = one KG-033 row) | A-016 ≡ B-021(assertion); mutual CONFIRM | WARN | Causation claim resolved — see §2. |
| 22 | AGENTS.md has no path to the accepted Root decomposition | A-009 ≡ B-015; mutual CONFIRM | INFO/WARN band | Owner-choice framing (A's) adopted by B. |
| 23 | AC/VER candidate status machine-opaque; "candidate" token overloaded; 0/45 unmarked | A-010 ≡ B-016; mutual CONFIRM | WARN/INFO band | |
| 24 | App AGENTS.md overlay `status: draft` while operative | A-021 ≡ B-026; mutual CONFIRM | WARN/INFO band | |
| 25 | PEC profile ADOPTED but binds v0.4 corpus and names PRD v2.0 (one amendment behind) | A-023 ≡ B-030; mutual CONFIRM | WARN | Self-disclosed limitation in-file (K-CONFLICT-1 working). |
| 26 | PEC objective-mapping residue (11 rows / 9 deliverables) clusters on the Root-runtime seam | B-028; A challenge CONFIRM (identical ID sets) | WARN | PEC self-disclosed; finding is the clustering. |
| 27 | PEC event-contract home (PRD §16 item 9) open while the Root counterpart exists and is in use by App | B-029; A challenge CONFIRM | REVIEW (preserved open question) | Neither reviewer recommends an answer. |
| 28 | App ResponsibleParty TBD on 51/51 with work IN_PROGRESS | A-019; B challenge CONFIRM | WARN | D-GOV-27 is the precedent pattern. |
| 29 | **Positive conformance (evidenced, not absence-of-findings):** Root F4 closes both directions (84/84, 51/51, 0 gaps); PEC 57/57 with exactly-verified deliberate 32/32 sequencing and byte-identical basis pin; SOW method layer Root 45/45 + PEC 32/32 PASS at the freeze; PEC optionality uncontradicted (zero genuine dependencies); human-judgment hinge and domain-truth boundary hold; no self-authorizing loop found | A-011/A-024/A-028(part) ≡ B-031/B-032/B-033/B-034; mutual CONFIRM (incl. A running the validator it had declined, reproducing B's result) | INFO | |

## 2. RESOLVED_BY_EVIDENCE (challenge changed a claim; the evidence decides)

| # | Claim | Resolution |
|---|---|---|
| R1 | B-021's causal link "stale REF-006 pin excludes the §17 amendment → contributor to B-001" | **Refuted by extraction of the pinned bytes**: the §17 Shared Runtime Amendment (line 1692, "root-owned product subsystem") is inside the pinned PRD revision; the pin↔freeze delta is one KG-033 row, requirement sets identical. B conceded in its own revisions. B-021 stands only as the narrower stale-pin mechanism claim (= A-016). B-001 unaffected. |
| R2 | B-020's FR quantities | **43** multi-owned FRs, not 50; **FR-122..128 singly owned at ID level (PKG-03)** — PKG-01 reaches them only by section citation. The narrower claim (ID-vs-section ambiguity) stands; the B-020→B-001/B-025 link via a "double claim" does not. 8 unowned FRs and 27/31 NFR-unassigned confirmed exactly. |
| R3 | B-002's evidence sweep "2 of 103 scope items mention runtime (SOW-027, SOW-028)" | **8 of 103**; the substantive pair is **SOW-027 + SOW-035**. Assertion survives on corrected anchors (A: ADD-MISSING-EVIDENCE). |
| R4 | A-006's aggregate "91 contradicting surfaces" | **82** (45 `_CONTEXT` footers + 34 SOWs + 3 decomposition passages) — B's recount, consistent with A's own itemisation. Direction and reach otherwise stand. |
| R5 | A-003's "7 hunks" | **6 hunks** (16 insertions / 6 deletions); characterisation (pure DEC-021 propagation) unchanged. |
| R6 | B's pass-1 "27 of 31 NFRs unassigned anywhere" | **23 untraced both-sides / 8 traced** (A-012's fuller §16 read); B conceded. |
| R7 | A-024's blob citation | `8aab8caa…` is the git object id, not the content sha256; byte-identity conclusion unaffected (B verified the sha256 equality directly). |
| R8 | B-031's guard-state grep method | The 1 yaml hit is "SPEC" substring, not PEC; conclusion (zero PEC dependencies in Root guard state) reinforced (A's anchor correction). |

## 3. STANDING_DIVERGENCE (preserved for the owner; not averaged)

| # | Divergence | Position A | Position B | State after challenge |
|---|---|---|---|---|
| S1 | **Is the absence of a Root owner for shared-runtime contract/conformance work a finding?** (B-002 vs A §7.4/A-026) | Not a conformance finding: O-2/O-10 are boundary commitments the forward register covers via DEL-02-02; the charter's "must" would create scope. Concedes (challenge) it should be an explicit owner-decision request. | A REVIEW-severity ownership gap: D-GOV-20's ten ruled items and named-but-unowned security/conformance gates make it a real gap at PRD level. | **Facts unanimous; routing unanimous (Root PRD amendment or recorded reasoned deferral — never decomposition invention). Divergence is classification only: finding vs routed observation. Goes to the owner as ODR-1(b) either way.** |
| S2 | Severity of App's missing Root-doctrine drift detector (B-006 REVIEW vs A-020 WARN) | Instance harmless in direction; defect located in the hand-derived survey mechanism. | Defect located in the missing detection channel itself; single-channel + inconsistent use ⇒ REVIEW. | Largely converged — A upgraded its related A-027 to REVIEW and adopted B's anchor; residual difference is which surface carries the severity. Practical effect on the decision slate: none (both feed ODR-3). |

## 4. SHARED_BLIND_SPOT_RISK (neither reviewer examined; flagged, not asserted)

1. **Root condition #9's four instrument conflicts** (AGENT_TASK absolute-path fields, `validate_id_format.sh`, SOW-validator prefix set, `tools/REGISTRY.md`): A treated as already-routed standing items (Receipt 51); B declared UNKNOWN/not reached. Neither re-examined. Standing owner items; the review adds nothing and clears nothing.
2. **D-APP-49 mirror obligations** vs the rehomed architecture: both UNKNOWN; A-014/B-003 make staleness likely but unaudited.
3. **App/runtime degraded-mode contract** (daemon absent or version-incompatible): both flagged UNKNOWN — identified, but no reviewer searched beyond the named doctrine surfaces; runtime package code itself was not reviewed by either (both lenses treated `runtime/` as contract/ownership surface, not code).
4. **Unchallenged single-source findings** carried at reviewer confidence without adversarial verification: B-008 (path-collision ambiguity), B-009 (domain-profile shape duplication — contains its own UNKNOWN), B-010, B-018 (41% drift backlog: manager-verified totals only), B-019, and A-007, A-018 (manager spot-verified anchors), A-025, A-028, A-029. None is high-severity; all anchors that the manager or the opposite reviewer touched did verify, so residual risk is low but nonzero.
5. **`.github/workflows/` CI conformance and export tooling behavior** beyond A-002's specific README/export divergence: outside both reviewers' sweeps.

## 5. STALE_INPUT (dispatch-manifest statements corrected by the review)

1. **"The six missing ACTIVE-pinned agent files"** (manifest, Root integration/drift): both reviewers independently established that **5 of the 6 are RETIRED/IncludeInIndex=NO** (correctly recorded retirements) and exactly **one** — `agents/AGENT_ORCHESTRATOR.md` — is a genuinely dangling ACTIVE/YES pin. The disclosed condition overstates; the residual defect is real (A-008 ≡ B-017).
2. **App condition 10 "one notice that misidentifies its stale target"**: understates — the D-GOV-26 notice misidentifies the *detection architecture* (claims corpus-drift checks fire for Root docs; they cannot, since the pins are App-local). Deepened, not merely confirmed (B-006).
3. Charter propositions the governed record rejected (both reviewers, independently): the charter's "Root decomposition must assign runtime contract/conformance work" would mis-route the correction (it is PRD-level, not decomposition repair); the charter's symmetric "optional services" framing for PEC and resource governance is asymmetric in the basis (PEC rigorous; resource governance nonexistent). Used as challenge material only, per its banner.

## 6. Consolidated owner-decision slate (deduplicated; for the step-7 human gate)

Each item names its findings, its owning instrument, and the decision. None creates a requirement; all route through owning instruments.

1. **Shared-runtime ownership — the BLOCK.** (B-001 + A-challenge; S1; A-015/B-025 context)
   (a) Confirm semantic ownership sits with Root per D-GOV-20/D-T0-23 and direct correction of App decomposition §13 line 611 via App SCOPE_CHANGE + D-APP ruling (App retains client-integration + acceptance-evidence ownership) — or rule the opposite by amending D-GOV-20 at Root.
   (b) Decide the Root-side scheduling: Root PRD amendment adding a runtime-contract/conformance commitment (then SCOPE_CHANGE deliverables), or a recorded reasoned deferral via the existing OI-013/§12.1 mechanism.
   (c) Same act should name an owner for the D-GOV-20 "separately bounded" security review and cross-client conformance proofs (currently unowned).
2. **Contract identity.** (B-003, B-005, A-014/B-004) Tier-0 ruling under D-T0-07: bump `FLOW_A_CONTRACT_VERSION` for the Root-hosted contract and re-pin App + Piping, or record deliberate carry-forward and what the value now binds. Companion: amend D-APP-48 (or successor) to declare the validator's observation boundary; route a notice to Piping; Piping re-pins D-30 after.
3. **Notice-architecture repair.** (B-006/B-007 ≡ A-020/A-027; A-008) Decide: (a) ship the outstanding notices for D-GOV-18, 20, 22, 25, 27 to App, PEC, Piping, and the domain packs as one coordination tranche (Root DEL-04-04 owns it); (b) whether downstream loops must pin the Root doctrine surfaces they inherit (making the claimed deterministic backstop real); (c) make the M6 pin survey mechanically derived and recorded per tranche.
4. **App traceability instrument.** (A-012/B-020, A-026, B-023/A-017, B-024) Decide whether a forward-coverage register is a required output of the shared decomposition method (amends the Root-owned standard, M2); App then adds the FR/NFR→deliverable companion register (resolving the 8 unowned FRs, 43 multi-owned FRs to primary owners, and 23 untraced NFRs — coverage-or-explicit-deferral each) and creates-or-defers the invariant-coverage register.
5. **App basis integrity.** (A-013+B's unresolvable-pin evidence, A-015, A-016) One App tranche: re-pin all 53 SOWs to one current decomposition commit (recording authorship eras; owner-gated judgment on re-verifying the 45 pre-SCA contracts); refresh REF-006; one owner act recording whether Gates 1–7 hold at a named SHA or which re-run. Also: assign App ResponsibleParty (A-019, D-GOV-27 pattern) and resolve the draft overlay status (A-021/B-026).
6. **Root mechanical repairs (no ruling on substance needed; routes exist).** Backfill D-GOV-27 EffectiveSHA, then repin the four amended SOWs (A-003/B-012/B-013); fix the decomposition header SHA label (A-005/B-011); add DEL-06-04 to §7 OBJ-004 (A-004); close OI-011 and correct the 82 stale ResponsibleParty surfaces (A-006/B-014); fix register row 39 §0.2.1 (A-007); complete C-4 in README + correcting receipt (A-002); one tranche adding CLAUDE.md to the enumerations (A-001); fix the App decomposition's absolute path (A-018); `domains/chirality` re-pin + D-GOV-18 notice (A-008/B-017/B-018).
7. **SOW method schema.** (A-010/B-016 + version-skew condition) Decide whether to add machine-readable `claim_status` (and optionally method-version) frontmatter to the SOW standard (M2; applies to Root and PEC on next touch).
8. **Validator observation-boundary convention.** (A-014/B-004, A-018) Decide whether registered validators must declare their observation boundary in output/contract (D-GOV-02 lineage / `tools/REGISTRY.md`).
9. **PEC event-contract home.** (B-029, B-028) PRD §16 item 9, decided with knowledge that `runtime/packages/contracts` already exists and is consumed by App; alternatives and criteria preserved in both reports (adopt-shared / pinned-mirror-with-currency-check / defer-with-rising-foreclosure-cost). Route: D-PEC ruling + D-T0 coordination record. Complete the 11-row objective mapping at the next PEC wave.
10. **Held open, no action (both reviewers concur):** reusable work surface / application environment profile (decide only if a second consumer appears); PEC availability thresholds; physical bundling vs logical composition (entangled with the runtime degraded-mode UNKNOWN — decide together); resource governance (all seven ownership cells undefined; charter-only candidate; absence is not a gap).

## 7. Classification integrity statement

No disagreement was averaged: S1 and S2 are preserved with both positions and their
post-challenge state. No reviewer's frozen report was altered at any stage. Challenge-stage
revisions are recorded only in the frozen challenge returns. The classification above cites
which record carries each number where pass-1 and challenge figures differ (the challenge
figure governs where the evidence was re-run: 82, 43, 23, 6-hunks, 8-of-103).
