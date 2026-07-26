# Reviewer B — Independent Pass 1

## 1. Identity and basis attestation

I am Reviewer B, the bounded ephemeral Agent 2 assigned the horizontal architecture / boundaries / adversarial-concordance lens.

I reviewed only Git-object bytes reachable from review freeze `da31c19b5656dd74615e308c4215688971d33dc9`. The product-basis commit is `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`; the frozen evidence records that reviewed product files did not change between those commits. I verified:

- `FROZEN_BASIS_MANIFEST.json` SHA-256: `f569d994156f9585fd100286e43b325116ae473616b1d1bd4f169bd88d632386`.
- Charter blob: `25c19694b64edf4acfb76ac02ce57b23c52d1962`; SHA-256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`.
- Initiating request SHA-256: `cea3ab818161afdc0ada267e2a98c69552f99dac0daee426f49023247e92f9c5`.

I read the charter and initiating request in full, in the required order, before product assessment. The charter is cited only for candidate/procedural status, never as product proof. No other reviewer return, draft, directory, message, or reasoning was consulted. I did not delegate.

## 2. Independent orientation

My initial account from the governed evidence, before applying the charter propositions as challenges, was:

1. Chirality Root is the normative and generic-runtime product. It owns file-native governance, agent/runtime doctrine, and the reusable local runtime.
2. Chirality App is a situated client/work surface with its own authority, permission, evidence, packaging, and user-experience duties.
3. PEC is a separate, optional coordination-plane product: a deterministic projection over file/Git truth plus an explicitly lower-trust presence tier. It observes but does not govern or participate.
4. Domain engines and situated applications retain domain/project truth and human gates. Runtime transport cannot confer their authority.
5. The program's strongest property is explicit authority discipline. Its current architectural weakness is concordance after change: owner decisions, accepted decompositions, live SOW contracts, mirrors, current pointers, and downstream notices do not always converge in one tranche.

The charter challenge sharpened, but did not create, the two principal conclusions: Root runtime ownership is under-decomposed, and the App's retained runtime-shaped SOWs have not been reconciled to the Root-owner/App-client split.

## 3. Method and limits

I used read-only Git plumbing, deterministic CSV/JSON/text inspection, row/population counts, SHA-256 verification, and targeted commit-difference inspection. Evidence references in the CSVs are frozen-path references; wildcard notation in population rows is a compact reference to the complete frozen directory population, not a live-filesystem claim.

I tested:

- authority and identity chains;
- PRD objective/invariant to decomposition to deliverable to SOW or lawful deferral;
- complete Root/App/PEC SOW/status populations;
- accepted amendments and disclosed weaknesses;
- owner/producer/consumer/record/compatibility/fallback/change-route boundaries;
- current-state, notice, drift, migration, rollback, release, and conformance surfaces.

Limits:

- I did not rerun product validators. The Root and PEC SOW populations were validated under different method eras; a present-tool rerun could measure tool drift rather than historical invalidity.
- I did not infer acceptance from proposals, historical snapshots, evaluation packages, mutable pointers, or run evidence.
- Domain packs and Chirality Piping were consulted only for downstream pin/notice/drift effects.
- Missing evidence remains `UNKNOWN`; candidate architecture remains candidate.

## 4. Root depth and breadth

Root's core trace is structurally strong. The adopted PRD revision 5 reaches seven accepted objectives, six packages, 45 deliverables, 103 scope items, and 45 live SOWs. All 45 SOWs and statuses are present and `INITIALIZED`; package coverage is 8 + 5 + 6 + 10 + 8 + 8. All pin the D-GOV-25 effective decomposition basis `653fabc9…`. Objective mapping is bidirectional. OBJ-2's situated-working-root demonstration is explicitly and reasonedly deferred; it is not a silent gap.

The Root authority chain also correctly bounds known stale text. `docs/PRD_ROOT.md` points to the adopted candidate and records that D-GOV-26/D-GOV-27 supersede O-1's earlier six-member instruction enumeration with the eight-member `docs/SPEC.md §0.2.1` set. Root `AGENTS.md` predating the later package topology is not itself a defect: it is the live runtime/agent index, not a duplicate decomposition register.

Four reliance weaknesses remain:

- D-GOV-27 has no bound EffectiveSHA (`B-F-006`).
- The decomposition header mislabels `ea0ad7a56…` as EffectiveSHA even though D-GOV-25 calls it CandidateMergeSHA and reserves EffectiveSHA for `653fabc9…` (`B-F-007`).
- Initialization is terminal in Receipt 52 and the status population, but the current plan remains ACTIVE and the phase has no explicit closeout handoff (`B-F-008`).
- OI-011 and portions of the SOW population still describe ResponsibleParty as TBD after D-GOV-27 assigns the party (`B-F-009`).

The population-wide candidate status of AC/VER text is disclosed and therefore not an undisclosed acceptance claim. Its varied prose is still machine-opaque (`B-F-010`).

The largest Root architectural issue is not missing runtime code. It is missing semantic decomposition ownership. D-GOV-20 and Root PRD O-2 make `runtime/` a Root product function covering protocol, daemon, client, sessions, credentials, engines, tools, delegation, locks, interruption, and residency. Root decomposition SOW-027/DEL-02-02 reduces this to three-layer boundary conformance. No Root deliverable visibly owns continuing generic-runtime contract evolution, migration, or release compatibility. That gap matters because the App still carries implementation-shaped runtime work (`B-F-001`).

## 5. App depth and breadth

The App corpus has a usable exact identity: `AUTHORITY_CORPUS.json` v17 pins the six synchronized App documents plus the two Root agent contracts it consumes. Those pins were clean at the freeze. The App PRD has no internal version, but its exact v17 pin is a sufficient identity mechanism. Stale `docs/MANIFEST.json` is bounded because it is not the identity of record.

The current decomposition records ten objectives, ten accepted packages, 51 accepted deliverables, and 78 scope items. The live population is 53 SOWs/statuses: 51 decomposition deliverables plus two PKG-00 control SOWs. All 53 are `IN_PROGRESS`; none is `ISSUED`; each contract's Remaining section is the live work surface, and F-APP-4 fences CHECKING-to-ISSUED.

Objective-to-deliverable mapping is complete. However, reliance on the exact decomposition is weaker than the Root/PEC chains. The header says Gates 1–7 were accepted by “implicit human approval per user instruction,” the tracking register is explicitly non-governing, and no separate ruling binds the exact current v3.2 bytes and in-place SCA amendment chain (`B-F-003`).

The decomposition also self-requires `contract_invariant_coverage_register.csv` or an explicit deferral before REVIEW closure. Neither exists. The latest coverage package closes with WARNINGS and implementation-handoff readiness, but it cannot substitute for the missing CONTRACT K-* trace (`B-F-004`).

D-APP-73 and App PRD §17 correctly describe Root as shared-runtime owner and App as desktop client. Yet SCA-APP-003 preserves all affected App deliverables as remaining aligned, while live SOW language such as DEL-03-01 still describes a product-owned runtime boundary on an older contract basis. The result is a semantic, not merely textual, ownership conflict (`B-F-002`).

The compatibility path is also stale: D-APP-48's 12-file pinned pull contract remains ruled, every pin is stale after the files became deprecation shims, and SCA-APP-003 does not supersede or repoint it (`B-F-005`). Receipt 91 versus its pre-merge handoff is a smaller current-state conflict (`B-F-013`).

The project `AGENTS.md` overlay's `draft` frontmatter is an authority-clarity smell, but the frozen corpus does not establish that the status field alone invalidates its operative use. I treat it as a corroborated observation, not an additional finding. The orphan `PKG-03_Harness_Runtime_Core` evidence tree, historical SCAs, evaluation snapshots, retired queues, and unselected design packages do not enlarge accepted topology.

## 6. PEC depth and breadth

PEC has the clearest optionality contract of the three products. PRD v2.1's `PEC-K-01` through `PEC-K-11` explicitly require graceful absence, file authority, harness-owned consumption, structural freshness, separate trust tiers, observation-not-participation, reconciliation supremacy, explainability, durable messages, content-minimality, and mode-proportional contact.

The accepted revision 1.2 decomposition contains 11 packages, 64 deliverables, 94 scope items (71 IN / 14 OUT / 9 TBD), and six objectives. D-PEC-60 accepted the base; D-PEC-61 added directed FULL_GRAPH self-bootstrap; D-PEC-64 completed objective mapping. All six objectives and all eleven invariants have downstream dispositions in `TRACE_MATRIX.csv`.

Population accounting is exact: 64 status files and 64 local `Dependencies.csv` files; 32 `INITIALIZED` SOWs and 32 deliberately `OPEN` P2–P4 deliverables without SOWs. The absent SOWs are sequenced deferrals, not coverage gaps. Current calibrated dependency state is 254 rows (135 anchor + 119 execution), 62 nodes, 119 edges, two orphans, zero SCCs, zero waivers, and strict-clean. There is no central dependency register by owner decision.

The final coverage package supports all six objectives and covers 64/64 deliverables, but it records three reliance residuals: DEL-08-02's frozen-exhibit provenance, DEL-08-01 AC-005's indirect second clause, and DEL-00-03 CLM-001's missing reference (`B-F-014`). These are not grounds to collapse the whole coverage verdict; they are named review obligations at affected activation/release gates.

Nine intentionally unmapped deliverables and eleven IN ledger rows without objective mapping do not contradict complete objective coverage. Several carry invariants or supporting mechanics no §3 objective states directly. The accepted decomposition explicitly records that choice.

The registered domain-engine profile still binds frozen v0.4 and says full v2 supersession awaits implementation shape. No current profile-mediated v2 act is established, so this is not a present failure; it becomes consequential before such an act (`B-F-015`).

The frozen v0.4 prototype, archived v1 PRD, candidate placement, historical DAG exhibit, setup/wave/repair working files, and advisory blocker output are not current product truth.

## 7. Cross-product boundary analysis

The intended composition is non-circular:

`human/file authority → product-specific governed workflow → Root runtime transport → bounded client/adapters`

PEC reads file/Git truth and runtime presence as a separate optional projection. Domain engines retain domain truth and proposal gates. No accepted instrument gives PEC, the App, the runtime daemon, or a domain solver authority to accept product state.

The principal cross-product defect is the missing middle of the runtime boundary:

- Root clearly claims semantic ownership.
- App clearly claims client/product duties in D-APP-73.
- Root decomposition does not allocate continuing runtime work.
- App live SOWs have not relinquished or narrowed their generic-runtime wording.

That four-part mismatch can cause duplicate contract homes, silent responsibility absorption, and change routes that depend on institutional memory.

Fallback architecture is otherwise sound. App and Root governance do not require PEC. PEC itself has a standing kill test and rebuild semantics. Candidate resource governance is optional charter-only architecture and must remain absent from correctness, authority, and system-of-record chains unless a new owner instrument says otherwise.

Notices and drift are only partially effective. The doctrine correctly says notices coordinate but do not authorize, and receivers must adopt/amend/decline. In practice, notice coverage varies and the consulted manifests contain material DRIFT/MISSING populations (`B-F-011`). The initiating request overstates one case: domains/chirality has one missing ACTIVE/Include=YES pin (`AGENT_ORCHESTRATOR`), not six; the other five cited rows are RETIRED/Include=NO (`B-F-012`).

Migration/rollback and release/conformance duties are explicit as principles but partially allocated in decomposition. The SOW method-era split also prevents treating a current Root validator rerun as proof that the historical Root acceptance was false.

## 8. Complete coverage summary

`TRACE_MATRIX.csv` contains 88 rows:

- Root: all 7 accepted objectives; all 45 live SOWs grouped exhaustively by the 6 packages; PRD/decomposition decisions; amendments; identity, acceptance, responsibility, candidate-criteria, and handoff weaknesses.
- App: all 10 objectives; all 53 live SOWs grouped exhaustively as 51 accepted deliverables plus 2 PKG-00 control SOWs across 11 live packages; corpus identity; accepted SCAs; invariant-register, mirror, ownership, and handoff weaknesses.
- PEC: all 11 PEC-K invariants; all 6 objectives; all 64 deliverables grouped exhaustively by 11 packages with the 32 initialized / 32 deliberate-deferral split; accepted amendments; coverage residuals; profile status.
- Cross-product: method era, domain manifests/missing-pin framing, optional resource governance, future semantic parity, and bounded historical surfaces.

`BOUNDARY_MATRIX.csv` contains 22 rows covering every required function: Root authority and runtime; App client/work surface; PEC projection and presence; human judgment; domain truth; Git/file truth; delegation; tools/permissions; credentials/session state; notices/drift; application integration; optional fallbacks/candidates; migration/rollback; release/conformance; product acceptance; private mirrors; and current-state handoff.

## 9. Findings keyed to `FINDINGS.csv`

No `BLOCK` finding is issued. Seven findings are `REVIEW`, seven are `WARN`, and one is `INFO`.

- `B-F-001` — Root generic-runtime semantic ownership is under-decomposed. `HIGH`.
- `B-F-002` — App live runtime SOWs conflict with Root-owner/App-client semantics. `HIGH`.
- `B-F-003` — App exact decomposition acceptance provenance is not reconstructible. `HIGH`.
- `B-F-004` — Required-or-deferred App invariant coverage register is absent. `HIGH`.
- `B-F-005` — D-APP-48's 12-file compatibility pull is stale and not superseded. `HIGH`.
- `B-F-006` — D-GOV-27 EffectiveSHA remains unbound. `HIGH`.
- `B-F-007` — Root decomposition and D-GOV-25 use conflicting SHA-role names. `HIGH`.
- `B-F-008` — Root initialization lacks converged handoff/current-plan closure. `HIGH`.
- `B-F-009` — Root responsibility surfaces disagree after D-GOV-27. `HIGH`.
- `B-F-010` — Root candidate AC/VER status is disclosed but machine-opaque. `MEDIUM`, because the prose caveat is visible.
- `B-F-011` — Cross-loop notice/drift coverage is uneven. `MEDIUM`, because consulted manifests are derivative and loop-specific adoption evidence is incomplete.
- `B-F-012` — Request framing overstates six missing ACTIVE pins; the consequence is one active pin plus five retired rows. `HIGH`.
- `B-F-013` — App Receipt 91 and handoff lifecycle state conflict. `MEDIUM`, because the receipt is the stronger terminal evidence.
- `B-F-014` — PEC coverage has three recorded residuals. `HIGH`.
- `B-F-015` — PEC's v0.4-bound profile may become stale at v2 activation. `MEDIUM`, because no present profile-mediated v2 act was proved.

## 10. Disclosed-condition consequence ledger

| Disclosed condition | Disposition | Consequence |
|---|---|---|
| Freeze/product-basis split; product files unchanged | Corroborated observation | Exact frozen identity is usable. |
| Mutable pointers/candidates/plans are non-authority | Bounded non-issue | Applied throughout; no pointer was treated as independent acceptance. |
| Root PRD revision 5 adopted by D-GOV-22 | Corroborated observation | Strong PRD identity. |
| Root PRD O-1 enumeration superseded | Bounded non-issue | Pointer and decisions bound the stale body wording. |
| DIRECTIVE genus statement superseded by D-GOV-23 | Bounded non-issue | No conflicting live authority was inferred. |
| Root decomposition 6/45/103/7 and accepted amendments | Corroborated observation | Counts and objective mapping remain stable. |
| Root header SHA-role conflict | Finding `B-F-007` | Citation identity is ambiguous. |
| Root 45 SOWs INITIALIZED and pin 653f… | Corroborated observation | Complete population; no SOW omission. |
| Root AC/VER candidate status in varied prose | Finding `B-F-010` | Human-readable, machine-opaque. |
| D-GOV-27 EffectiveSHA placeholder | Finding `B-F-006` | Applied state is not bound in the ruling. |
| Root current plan ACTIVE after completion; Receipt 52 as handoff | Finding `B-F-008` | Current-state/handoff closure is incomplete. |
| Root G1–G4 passing; graph nodes pending | Corroborated observation | Initialization is not implementation/release. |
| Root runtime doctrine under `runtime/` | Finding `B-F-001` | Authority is clearer than decomposition ownership. |
| domains/chirality manifest 126 CLEAN / 93 DRIFT / 6 MISSING | Finding `B-F-011`; narrowed by `B-F-012` | Retrieval/notice debt, not product-authority failure. |
| Uneven D-GOV notice coverage | Finding `B-F-011` | Downstream awareness can lag. |
| Root historical proposals, old handoff, stale fixtures, AgentRun SOW copies | Bounded non-issue | Excluded from accepted product truth. |
| App PRD has no stated version; v17 pin governs | Bounded non-issue | Exact hash identity is sufficient. |
| App MANIFEST stale | Bounded non-issue | v17 corpus, not MANIFEST, governs identity. |
| App decomposition implicit acceptance/no separate ruling | Finding `B-F-003` | Exact accepted bytes/amendment chain are unclear. |
| App 10/51/78/10; topology preserved through SCA-003/004 | Corroborated observation | Counts stable; semantic propagation still incomplete. |
| Missing invariant coverage register/no deferral | Finding `B-F-004` | Formal REVIEW closure lacks required trace. |
| Latest App coverage closes WARNINGS/ready for implementation handoff | Corroborated observation | Readiness is not invariant-coverage closure or issuance. |
| 53 App SOWs/statuses, all IN_PROGRESS, none ISSUED | Corroborated observation | Full live population; 51 + 2 PKG-00 explained. |
| App decision register non-governing | Bounded non-issue | Used only for navigation; rulings were checked. |
| Receipt 91 terminal / run handoff pending | Finding `B-F-013` | Current-state conflict. |
| SCA-APP-004 governance-propagated, implementation-pending | Corroborated observation | No completion inferred. |
| D-APP-48 mirror 12/12 stale | Finding `B-F-005` | Compatibility route is stale. |
| App domain manifest 119 CLEAN / 129 DRIFT / 219 MISSING | Finding `B-F-011` context | Derivative retrieval debt; not App authority invalidation. |
| App overlay frontmatter `draft` | Corroborated observation | Authority clarity concern; evidence insufficient for a separate defect. |
| Semantic parity future SCA lacks instrument | Candidate decision question | Not current scope or conformance. Owner must instrument before reliance. |
| App historical/retired/unselected/orphan/evaluation surfaces | Bounded non-issue | Do not enlarge accepted topology. |
| PEC optional projection and presence | Corroborated observation | Boundaries and graceful absence are explicit. |
| PEC PRD v2.1 and PEC-K-01..11 | Corroborated observation | All invariants traced. |
| PEC decomposition 11/64/94/6 | Corroborated observation | Accepted lineage is reconstructible. |
| 32 initialized / 32 deliberately OPEN without SOW | Bounded non-issue | Sequenced deferral, not omission. |
| 64 local Dependencies.csv; no central register | Bounded non-issue | Owner-selected distributed truth. |
| 254 dependency rows; 62 nodes/119 edges; 2 orphans; 0 SCC/waiver | Corroborated observation | Current strict dependency calibration is clean. |
| Advisory blocker state | Bounded non-issue | Visibility, not authority. |
| F-PEC-1..4 and owner-gated build packets | Corroborated observation | Build remains fenced. |
| Current coordination item 9 supersedes item 8 | Corroborated observation | Used newer calibrated figures. |
| PEC v0.4-bound domain profile | Unknown/finding `B-F-015` | Consequence deferred until profile-mediated v2 act. |
| PEC is a distinct Root-runtime client | Corroborated observation | Does not grant PEC project authority. |
| PEC frozen prototype/archive/DAG exhibit/history | Bounded non-issue | Excluded from current truth. |
| Root vs PEC SOW validator eras | Unknown/tool-basis caution | No cross-era PASS equivalence asserted. |
| Root owns runtime; App/PEC are clients | Findings `B-F-001`/`B-F-002` | Accepted principle is not fully allocated in contracts. |
| Resource governance charter proposal | Candidate decision question | Optional and non-authoritative unless separately adopted. |
| Chirality Piping as situated exemplar | Corroborated observation | Consulted only; no fourth-product verdict. |
| SOLVER lineage | Bounded non-issue | Not governing evidence. |

## 11. Conflicts and unknowns

Standing evidence conflicts:

- Root SHA roles: D-GOV-25 versus decomposition header.
- Root closeout: Receipt/status population versus ACTIVE current plan and missing handoff.
- App runtime ownership: D-APP-73/PRD §17 versus live runtime-shaped SOW language.
- App current state: Receipt 91 versus pending-merge handoff.
- App compatibility: still-ruled D-APP-48 hashes versus post-extraction shims.

Unknowns:

- Whether a not-in-corpus App owner message was intended to bind the exact current decomposition. It cannot be substituted into this frozen review.
- Whether any present v2 operation actually consumes the stale PEC domain-engine profile.
- Whether a current-method Root SOW validator run would report only tool drift or a substantive current defect. No run was performed.
- The full consequence of missing/late notices for each receiving loop, because each loop retains independent adoption authority.

Candidate decision questions:

- If semantic parity is to become App scope, which owner instrument defines its objective, acceptance, and SOW impacts?
- If resource governance is adopted, who owns it, what exact records may it derive, and how are optionality/non-authority/kill-test properties enforced?
- Where should the PEC event-contract home and auth reuse settle? These remain explicit open decisions, not silent gaps.

## 12. Recommendations and smallest lawful routes

Recommended order:

1. Root owner gate: amend Root decomposition to allocate continuing generic-runtime semantic/conformance duties (`B-F-001`). This is the controlling ownership move.
2. App SCOPE_CHANGE: narrow impacted SOWs to App client/adapter/presentation/compatibility duties (`B-F-002`), then supersede D-APP-48 (`B-F-005`).
3. App decomposition owner gate: bind exact current bytes/amendment chain (`B-F-003`) and create or explicitly defer the invariant coverage register (`B-F-004`) before REVIEW closure.
4. Root governance closeout: bind D-GOV-27 EffectiveSHA, correct the decomposition SHA-role label, emit the initialization handoff, and close/repoint the active plan (`B-F-006` through `B-F-009`).
5. Carry PEC's three recorded residuals into the affected activations; supersede the v0.4 profile before its first v2-mediated use (`B-F-014`, `B-F-015`).
6. On the next agent-index change, execute the existing notice rule end-to-end and let each receiver reconcile its own manifest (`B-F-011`). Correct the six-missing-pins framing independently (`B-F-012`).

These are routing recommendations, not product amendments. Each consequential change must stop at its owning human gate.

## 13. Explicit no-score statement

No score, rating, grade, pass percentage, or product acceptance verdict is provided. No scoring rubric was authorized. This return is independent review evidence and advice only.
