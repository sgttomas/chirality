# CHALLENGE — Reviewer A on Reviewer B's frozen pass-1 report

| Field | Value |
|---|---|
| **Challenger** | **A** (vertical lens: authority, intent, traceability) |
| **Report under challenge** | `REVIEWER_B_REPORT.md`, sha256 **verified** `5c20315e9ad7829afff0cfc021bf928a4ee05fbce8a7d2a10f1e63d69ba61cbf` — matches the value in my sealed challenge brief |
| **Challenge brief** | `CHALLENGE_BRIEF_A.md`, sha256 **verified** `b1aeac525b6413c4f79f5a41424a31530b204b09968545160b0f3461c8d39204` |
| **Evidence basis** | `/Users/ryan/dev/chirality-review-frozen-da31c19` @ `da31c19b5656dd74615e308c4215688971d33dc9` — the only source consulted. `/Users/ryan/dev/chirality` was not read. |
| **Date** | 2026-07-26 |
| **My own pass-1 report** | `REVIEWER_A_REPORT.md` (`ee39da9fc11d…`) — **not edited, appended to, or rewritten.** |

## Scope of this challenge

B's report carries **15** findings. By B's own severity tally (§2.2) and by my reading of each finding's severity field, the **BLOCK + REVIEW** set is:

**RB-001, RB-002** (BLOCK) and **RB-003, RB-004, RB-005, RB-006, RB-007, RB-009, RB-010** (REVIEW) — **nine findings**.

My brief anticipated this set as "RB-001…RB-009" and warned me not to trust its arithmetic. It is wrong: **RB-008 is WARN**, not REVIEW, and **RB-010 is REVIEW**, not WARN. I challenged the nine findings identified from B's report itself, not the brief's range.

Plus a **sample of four WARN/INFO** findings (minimum three required): **RB-008, RB-011, RB-013, RB-015**. Selection rationale is recorded at §3.

**Method.** I re-opened every load-bearing file at the frozen corpus and recomputed every count, quote, line number, and hash I rely on. I did not accept B's citations on faith and did not rely on my own pass-1 memory without re-checking. I ran no repo script and relied on no validator PASS; all computation was read-only (`grep`, `find`, `sed`, `awk`, `wc`, `shasum`, `python3` over `csv`/`json`/`hashlib`, and read-only `git` plumbing). I mint no new findings; genuinely new material is confined to §4.

---

## 1. Challenged findings — BLOCK and REVIEW

### RB-001 — Two accepted instruments name different semantic owners of the shared runtime

**Verdict: CONFIRM**

**Re-verification.** Every cited artefact resolves and every quotation is exact:

- `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §13, **line 611** — verbatim as B quotes, including *"Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership and acceptance evidence through the SCA-APP-003 impact map."*
- `D-GOV-20_shared_runtime_local_agent_pilot.md` §Ruled architecture **items 1–2** — *"becomes a root-owned `runtime/` workspace"*; *"exclusively owns runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency."* Status RULED, 2026-07-22.
- `docs/CONTRACT.md` §1.13 **K-RUNTIME-1** — exists, at line 155, with B's text verbatim including the enforcement column *"Runtime daemon singleton; client conformance; packaged-process inspection."*
- `projects/chirality-app-dev/docs/PRD.md` **line 1694** — verbatim: *"…make the provider-neutral runtime a root-owned product subsystem rather than a frontend-owned singleton."*
- `_DomainEngines/_DECISIONS/_REGISTER.md` **line 32**, D-T0-23 — verbatim: *"app-dev and PEC become registered clients of one daemon."*

**Severity/class commentary.** I rate the same conflict **REVIEW** in my own report (RA-003); B rates it BLOCK. I do **not** treat that as grounds to refute. The divergence is entirely a boundary-definition difference and both are internally consistent: B's declared BLOCK threshold is *"an accepted instrument is contradicted by another accepted instrument"*, which this plainly meets; mine required that the basis be contradicted or unresolvable *such that unsafe reliance could follow*, and I judged the charitable reading (app-dev deliverables retain **deliverable accountability**, not runtime contract ownership) available enough to hold at REVIEW. **New evidence found during this challenge moves me toward B** — see §4, first item: the App's own shipped facade file states that *"Runtime contract ownership moved to the repository-root workspace"*, which makes the §13 sentence the outlier against three governed instruments **and** the codebase, and materially raises the chance a reader is misled. I record the divergence for the manager as a calibration question rather than a disagreement on fact.

One limb of B's assertion is weaker than the other two and should not carry weight at fan-in: **K-RUNTIME-1 forbids constructing a *competing runtime***, which the §13 sentence does not assert. The decisive contradictions are with D-GOV-20 item 1 and App PRD §17, both of which speak directly to *ownership*. B's conclusion survives on those two limbs without needing the third.

**Confidence: HIGH.**

---

### RB-002 — Root `runtime/` has no owning package, deliverable, write locus, or SOW in the accepted Root decomposition

**Verdict: NARROW**

**What survives — the entire assertion and all of its structural evidence.** I re-verified every mechanical claim and each is exact:

| B's claim | My recomputation | Result |
|---|---|---|
| `runtime/` is a seven-package workspace | `runtime/packages/` = `cli, client, contracts, core, daemon, engine-claude, engine-pi-omlx` — **7** | **exact** |
| Root SOW scan for `runtime\|daemon` → 4 hits: DEL-02-02 (6), DEL-01-06 (2), DEL-02-03 (1), DEL-04-07 (1) | identical, case-insensitive, across all 45 | **exact** |
| No Root deliverable-register row carries `runtime/` as `AnticipatedWriteLocus` | **0 of 45**; declared loci are `execution-tree` (37), `instruction-surface` (11), `tools/` (5), `exports/` (1), `execution/_harness` (1) | **exact** |
| `runtime/` is outside `docs/SPEC.md` §0.2.1, so no M2 gate applies | §0.2.1 line 44 enumerates 8 members; `runtime` occurs **0** times | **exact** |
| CONTRACT §1.13 defines K-RUNTIME-1, K-CONTROL-1, K-PROJECT-1, K-STORE-2, K-RESIDENCY-1, K-ROLE-2, K-EXPORT-1 with live enforcement, bound by §2's map row *"Shared runtime daemon and clients (runtime)"* | all seven present (lines 155–161); §2 map row present at line 184 binding six | **exact** |
| Root decomposition §2.3 does not list D-GOV-20 even as interpretive context | confirmed — §2.3 lists `AGENTS.md`, DIRECTIVE, CONTRACT, TYPES, D-GOV-21 §5, live registries only | **exact** |

This overlaps my own RA-002, but **B's evidence is stronger than mine on two points I did not reach**: the seven `K-*` runtime invariants with a dedicated enforcement-map row, and the observation that `runtime/` falls outside the instruction surface so **not even the M2 governance gate covers it**. Both are correct and both materially strengthen the finding. I adopt neither as my own; I record that B established them.

**What does not survive — one inference in the Consequence paragraph.** B writes: *"It is also the exact shape of PRD falsifier **F3** (self-authorization): root development already consumes a runtime capability that was never accepted through a root deliverable stream."*

F3 (`docs/PRD_ROOT.md` §8.2) is: *"A root node consumes a capability produced by root development before that capability was accepted."* B's claim requires two facts it does not evidence and cannot evidence within its own declared boundary:

1. **That root development consumes the runtime.** B cites nothing for this. It is a claim about how root sessions actually execute — i.e. runtime behaviour — which B's own observation boundary (§2.1) expressly excludes: *"I do not observe: runtime behaviour, test results, validator output…"*. I searched and found no record establishing it either.
2. **That the capability was "produced by root development."** The record indicates the opposite provenance: the runtime was extracted from the App loop under SCA-APP-003 / D-APP-73 and rehomed, which is not root development producing a capability for itself.

The ownership gap is real and fully proven; **"F3 is tripped" is not proven** and would be a materially graver claim if carried unqualified into fan-in, since F3 is one of three falsifiers of the containment of self-application. I mark NARROW so the gap goes forward at full strength and the falsifier inference goes forward flagged.

**Severity/class commentary.** My own RA-002 rated this REVIEW; B rates it BLOCK. Same boundary-definition difference as RB-001 — B's threshold includes *"an accepted-basis commitment left without any executable coverage anywhere in the corpus"*, which this meets on B's own verified evidence. I note, in B's favour, that the M2-gate point (which I missed) is the strongest argument for BLOCK: a subsystem covered by neither a deliverable nor a governance gate has no change path at all. B's routing (**PRD amendment first, not a decomposition edit**, per D-9 and the charter) is correct and matches my RA-002 independently.

**Confidence: HIGH** on the confirmed portion; **HIGH** that the F3 inference is unestablished.

---

### RB-003 — Tier-0 D-T0-23 preserves PEC capabilities PEC's later PRD retired, with no supersession recorded

**Verdict: CONFIRM**

**Re-verification.**
- `_DomainEngines/_DECISIONS/_REGISTER.md` **line 32** carries D-T0-23 verbatim as B quotes, including *"preserve its deterministic adapter service, human acts, visibility basis, scratch/demo pilot fence, and open production gates"* and the scope cell *"project/domain authority, deterministic acts, **RBAC**, data boundaries … remain independently governed."*
- **No supersession or residual row anywhere in the register references D-T0-23** — I grepped the register for `supersede`/`residual` and cross-filtered for `T0-23`: zero matches. B's claim is exact.
- B's proposed remedy relies on the register's own residual convention; I verified the convention exists (8 occurrences of "residual" in the register), so the smallest-action proposal is well-founded in precedent.
- Ordering verified from the documents themselves: D-T0-23 RULED 2026-07-22; PEC PRD v2.1 adopted 2026-07-24 by D-PEC-58. The retiring instrument is later.
- PEC PRD §15 declares partial supersession **against `D-PEC-56` only**; I confirmed `D-T0-23` appears nowhere in the PEC PRD.

**Severity/class commentary.** REVIEW is right. Nothing currently executes against D-T0-23's stale clause, so this is not BLOCK; but it is the cross-project register of record and it misdescribes a live counterparty, so it needs an owner disposition rather than agent normalization.

**Confidence: HIGH.**

---

### RB-004 — The adopted PEC domain-engine profile asserts an integration level and residency basis the adopted PEC PRD forbids

**Verdict: NARROW**

**What survives — the authority conflict, exactly as asserted, with every line number correct.**

- `_DomainEngines/profiles/pec.yaml` **l.26** `profile_status: "ADOPTED"`; **l.27** `integration_level: "OPERATION_PROPOSAL"  # L3, imports scope — D-T0-18 O-A + D-PEC-12`; **l.28** `data_residency: "OPEN_ENUMERATED"` with the text *"LLM-hosted agent sessions may read, and route to the owner-configured model provider, exactly the enumerated surface … under the agent person's RBAC visibility, is_admin=0"*; **l.141** `operation_proposal_contract:`. All four verified at the stated lines.
- Against PEC PRD §4.2 permanent non-goals, §8 (RBAC retired), §13 (L3 lane sunset), PEC-K-10 — all verified in my own full read of the PEC PRD.
- **D-GOV-06 precedent verified**: `docs/governance_harness/_DECISIONS/D-GOV-06_domain_profile_current_truth.md` line 15 — *"a human must rule the fact (K-CONFLICT-1)"*. B's characterisation of it as direct precedent for treating stale profile status as owner-rulable rather than agent-normalizable is accurate.
- `SOW-090` verified `OUT`/Deferred with the trigger *"once v2 has implementation shape"*.

**This is the most valuable finding in B's report that has no counterpart in mine.** My pass-1 did not examine `_DomainEngines/profiles/pec.yaml` at all. The conflict is real and I confirm it in full.

**What does not survive — the blast-radius characterisation.** B's Consequence states the profile *"grants an agent-visible, provider-egressing surface and an operation-apply lane to a product whose adopted PRD forbids both"*, that this is *"not documentation lag — it is an ADOPTED machine-readable control surface"* with *"a live blast radius"*, and that *"the stale grant is in force now"* — hence the recommendation not to wait for v2 shape.

The grant's own terms and the subject product's state bound this more tightly than B allows:

- The same `data_residency` clause B quotes **ends**: *"Everything unenumerated stays CLOSED. **Mutation basis unchanged: scratch/demo only** (real/non-scratch DB operation needs its own future row)."* The grant is self-limited to scratch/demo mutation.
- `projects/pec/docs/PRD.md` §13, verbatim: *"There is nothing to migrate: the v0.4-baseline application **has no users, no production data (scratch/demo only by ruling)**, and no dependents beyond a scratch-only validation bridge."*
- The surfaces the profile enumerates belong to the frozen v0.4 prototype, which the manifest's do-not-mistake list places outside current PEC basis.

So the residency grant is a **standing grant over a retired, dataless, scratch-only prototype**, not a live provider-egress channel over operating data. The **authority defect is exactly as B states** — an ADOPTED machine surface asserting a level its product's PRD forbids, correctly routed to an owner ruling on the D-GOV-06 pattern. The **urgency argument is overstated**, and with it B's fan-in ranking of this as *"the urgent half"* of the RB-003+RB-004 pair.

**Severity/class commentary.** REVIEW remains correct on the narrowed basis — indeed the narrowing supports REVIEW over anything higher. B's smallest action (interim ruling, or demote the grant-bearing fields / mark `SUPERSEDED_PENDING_V2`) stands unchanged and is still the right act; only the "do not wait" urgency should be re-weighed against the fact that the grant currently reaches no production data.

**Confidence: HIGH** on both the confirmed conflict and the narrowing (both rest on verbatim text in the two cited documents).

---

### RB-005 — The App ScopeOfWork layer never received the shared-runtime rehoming

**Verdict: CONFIRM**

**Re-verification.**
- Scan of **all 53** App ScopeOfWork contracts for `D-GOV-20|root-owned|runtime-daemon|daemon`: **exactly one** file matches — `DEL-05-05_ToolResultStore_and_Session_Artifacts`, 6 hits. B's count is exact.
- `DEL-03-01`'s `OUT-001`, line 16, verbatim: *"A product-owned AgentEnginePort / RuntimeEngineContract, runtime contract documentation, and conformance tests for stub and provider/SDK-backed adapters."* Frontmatter `project_scope_refs: [SOW-037]` and `decomposition_basis: …@0724f26f6ef79d733c8f1c513b29d837fd43c8eb` both exact.
- App SSOW `SOW-037` unchanged: *"Define product-owned `AgentEnginePort` / `RuntimeEngineContract`."*
- The rehoming's reach into the decomposition — OI-007, DEC-019, §13 — verified; Change Log 2026-07-22 verbatim *"without changing package/deliverable topology or lifecycle state."*
- B's corroborating directory-name drift examples verified: `DEL-02-01_Desktop_Shell_and_Matrix_Navigation`, `DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision`, `DEL-05-04_Runtime_Replay_and_Transcript_View` all diverge from the v3.2 names. (My own pass-1 measured six such divergences across all 51; B's three are a correct subset.)

**Strengthened by challenge evidence.** §4's first item — the shipped facade stating *"Runtime contract ownership moved to the repository-root workspace"* — confirms B's central characterisation precisely: the **code** completed the rehoming while the **contract** did not. B calls this "a propagation failure, not a posture failure" (M3-Q7); that reading is now directly evidenced.

**Severity/class commentary.** REVIEW is right. I note one nuance B did not surface and which slightly softens the practical picture without touching the finding: `DEL-03-01`'s `_STATUS.md` carries, under `## Remaining`, *"Promote provider-neutral runtime contracts to root `runtime/`, preserve the deprecated app import path for one cycle, and expand conformance for daemon/client/project/residency behavior (gated: serialized core integration owner)."* So the rehoming **is** recorded as open work in the lifecycle layer — just not in the ScopeOfWork contract B correctly identifies as the layer executors and REVIEW actually read. This makes the defect a layer-propagation gap rather than a total omission.

**Confidence: HIGH.**

---

### RB-006 — The only live register of shared-runtime reliance boundaries is consumer-owned, and its PEC row describes a retired product

**Verdict: ADD-MISSING-EVIDENCE**

**The assertion is correct and I verify it in full.**
- `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md` exists, **163 lines** exactly as B states.
- `RB-DAEMON` (l.141), `RB-PROJECT-REGISTRATION` (l.143), `RB-PEC-ADAPTER` (l.147) all present with B's quoted text verbatim, including `RB-PEC-ADAPTER`'s *"PEC adapter RBAC, human-only act exclusion, scratch/demo fence."*
- It is App-owned (path is inside the App working root; its owning contract is App `DEL-01-02`, artifact list *"`docs/harness/reliance_boundary_register.md`; enforcement matrix; test index"*).
- **No Root-side equivalent exists**: a corpus-wide search for `*reliance*` returns only this file and its App test (`frontend/src/__tests__/docs/reliance-boundary-register.test.ts`).
- The staleness of `RB-PEC-ADAPTER` against PEC PRD §8/§13/§15 is verified (same chain as RB-003/RB-004).

**The evidence B supplies for one supporting bullet is wrong, and correcting it strengthens the finding.** B writes: *"mechanical scan of all 45 Root SOWs for `chirality-app|projects/pec|PEC` returns only `DEL-04-07` (export boundary), `DEL-06-05` (domain-engine truth boundary) and `DEL-01-08` (non-goal register)."*

My recomputation over all 45:

| Contract | hits | what actually matches |
|---|---:|---|
| `DEL-01-01` | 1 | — |
| `DEL-01-03` | 3 | — |
| `DEL-01-08` | 2 | `exports/chirality-app/export_public.py` (the export script path) |
| `DEL-04-07` | 6 | `exports/chirality-app/export_public.py`, `export-manifest.csv`, `export-report.md` |
| `DEL-04-08` | 1 | — |
| **`DEL-06-05`** | **0** | **does not match at all** |

So B **named a contract that does not match** (`DEL-06-05`) and **omitted three that do** (`DEL-01-01`, `DEL-01-03`, `DEL-04-08`). The corrected set is five files, not three.

**The correction cuts in B's favour.** The bulk of the matches are the **export-profile file path** `exports/chirality-app/export_public.py` — a script name, not a reference to the App product as a runtime consumer. So B's conclusion — *"none is a reliance-boundary register, and none names App or PEC as a runtime consumer with a compatibility obligation"* — is **more strongly supported by the corrected evidence than by the evidence B gave**. I supply the corrected scan so the finding is not challengeable on a detail that does not affect it.

**Severity/class commentary.** REVIEW is right; the class ("ownership gap + semantic conflict") is apt.

**Confidence: HIGH.**

---

### RB-007 — The event-contract home and daemon global event feed are cross-loop decisions with no owning instrument on the producing side

**Verdict: CONFIRM**

**Re-verification.**
- `projects/pec/docs/PRD.md` **line 280**, PEC-STR-002 — verbatim as B quotes, including *"writes into root `runtime/` are outside PEC's fences and require their own coordination."*
- PEC decomposition **SOW-074** (l.264) `OUT` — verbatim *"Writes into root `runtime/`, including placing the event contracts there … **Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination."*
- **SOW-076** (l.275) TBD, daemon global event feed, *"affects SOW-035 efficiency, not correctness"*; **SOW-083** (l.282) TBD, event-contract home + transport. All exact.
- Consuming deliverables `DEL-07-02` and `DEL-07-05` exist in PKG-07 and PKG-07 has **0** ScopeOfWork contracts — verified independently (see RB-011).
- **B's precedent citation is exact.** `_DomainEngines/_DECISIONS/_REGISTER.md` D-T0-19 reads *"New coupling row (no prior register home, verified 2026-07-05): the **pec ↔ chirality-app-dev harness bridge lane**…"* — so the proposed remedy (a Tier-0 coupling row) has a directly analogous precedent in the same register.

**Severity/class commentary.** REVIEW is right, and I endorse B's reasoning that this is *not* a PEC defect: PEC fenced itself out of `runtime/` correctly and named the closing act. B's point that the named act — *"§16 ruling (cross-loop)"* — has **no addressee**, because §16 is PEC's own list and PEC cannot rule on `runtime/`, is precise and well-evidenced. This is the cleanest illustration in either report of a dependency correctly declared on one side and unowned on the other.

**Confidence: HIGH.**

---

### RB-009 — App PKG-00 control contracts pin a package README as `decomposition_basis` and carry scope/objective references in no accepted decomposition

**Verdict: CONFIRM**

**Re-verification.**
- `DEL-00-01` and `DEL-00-02` frontmatter — both verbatim as B states: `decomposition_basis: projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/README.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb`; `project_scope_refs: [CONTROL-SCC-002]` / `[CONTROL-SCC-001]`; `package_objective_refs: [DAG-CLOSURE]`.
- **B's standard-form point verified independently**: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §3 gives the field's form as `decomposition_basis: path/to/accepted/decomposition@<commit>` — so a README value does depart from the stated form, not merely from convention.
- `CONTROL-SCC-001`, `CONTROL-SCC-002`, `DAG-CLOSURE` appear nowhere in the accepted decomposition — confirmed against its 78 `SOW-*`, 10 `OBJ-*`, 10 `PKG-*`, 51 `DEL-*`.
- The self-limiting quotes verified at their lines: `GraphParticipation | EXCLUDED_CONTROL_DELIVERABLE` (l.52); *"This deliverable is a PKG-00 control artifact, not a product implementation deliverable"* (l.71).
- **B's discharged-condition observation verified**: `StrictSCCCount | 0` (l.56), `SCC_Size | 0` (l.59), and `AnticipatedArtifacts | No active SCC-001 closure artifacts remain` (l.62). B's inference that a retirement disposition may be the smaller act is well-founded.

**Severity/class commentary.** REVIEW and the class "overreach (bounded self-authorization)" are both apt, and B's own reasoning for holding it at REVIEW rather than BLOCK — *"the bound is asserted by the artifacts themselves, which is exactly the reasoning the corpus otherwise rejects"* — is the right calibration. My own RA-010 rated the same surface WARN; B's REVIEW is the better call, because B correctly identifies the D-9 self-authorization dimension (a loop minting its own scope namespace) that I treated only as a namespace-hygiene issue. I record that as a point where B's lens saw further than mine.

**Confidence: HIGH.**

---

### RB-010 — App's required invariant-coverage register is absent with no deferral

**Verdict: CONFIRM**

**Re-verification.**
- `projects/chirality-app-dev/execution/_Decomposition/` contains exactly one file, the decomposition `.md`. The register does not exist.
- §2.2 (*"must be created or explicitly deferred before REVIEW closure"*), §10B acceptance checklist, and DEC-015 all verified verbatim.
- **B's sharpest sub-claim verified**: §10A.1's ten-row family table does **not** reach the CONTRACT §1.13 framework invariants. Its rows cover `K-PRD/K-HIER/K-ID/K-PATH/K-FS/K-GIT/K-NOMEM`, `K-AUTH/K-BIND/K-GATE/K-PROF`, `K-ROOT/K-PACKAGE`, `K-CORE/K-ENGINE/K-RELIANCE/K-SDK`, `K-EVENT`, `K-PERM/K-TOOL/K-MCP/K-HOOK/K-PATH/K-BASH`, `K-STATUS/K-DEP/K-PROV/K-INVENT/K-CONFLICT/K-SNAP/K-REF`, `K-WRITE/K-SEAL/K-GHOST/K-SUBAGENT`, `K-NET/K-KEY/K-ATTACH/K-RELEASE/K-VALIDATE/K-RETIRED`, `K-DOMAIN`. **`K-RUNTIME-1`, `K-CONTROL-1`, `K-PROJECT-1`, `K-STORE-2`, `K-RESIDENCY-1`, `K-ROLE-2` appear in none of them** — exactly as B asserts. So the invariant family most affected by the rehoming is the one the substitute coverage surface does not reach.
- B's asymmetry point verified: Root does carry this as a deliverable (`DEL-01-02_Invariant_Catalog_Conformance_Register`).

**Severity/class commentary.** My own RA-014 rated this WARN; B rates it REVIEW. **B is better calibrated and I concede the point.** I weighted "REVIEW closure has not been claimed, so the consequence is contained." B weighted the §1.13 blind spot — which I did not check — and that materially changes the picture: this is not merely a missing artefact but the specific reason the runtime-ownership dispute has no App-side machine record either way. REVIEW is right.

**Confidence: HIGH.**

---

## 2. Challenged findings — WARN/INFO sample

### RB-008 (WARN) — The ratified ScopeOfWork standard has no interface, consumer, or dependency element

**Verdict: CONFIRM**

**Re-verification, all three structural claims exact:**
- §3 YAML subset is exactly `schema`, `deliverable_id`, `package_id`, `decomposition_basis`, `project_scope_refs`, `package_objective_refs` — six fields, none declaring a counterparty.
- §4 identifier grammar yields exactly `AC, AX, CLM, CON, OUT, REM, REQ, TBD, VER` — **no interface, consumer, producer, or dependency prefix**.
- §5 matrix columns are exactly `Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation` — evidence required, interfaces absent.
- The observed effect is consistent with my own pass-1 census: all 130 contracts across the three products declare exactly those six frontmatter keys and no counterparty field.

**Severity/class commentary.** B rates this WARN while simultaneously identifying it (fan-in item 9) as *"the mechanism behind items 1, 2, 3, 5 and 6."* Those two statements sit awkwardly together: a defect that structurally prevents deterministic detection of the report's two BLOCKs is arguably more than "contained within one instrument." I do not propose a severity — that is the manager's call — but I flag the tension for fan-in, because B's own framing makes this the highest-leverage *fixable* item in the report while its severity ranks it ninth. B's restraint is defensible on the ground that no contract violates the standard as written (B says so explicitly: *"This is a proposal, not a finding of non-conformance"*), and the proposed remedy is correctly scoped as **optional** so as not to retroactively invalidate 130 contracts.

**Confidence: HIGH.**

---

### RB-011 (WARN) — The shared-runtime seam has no ScopeOfWork contract in any of the three products

**Verdict: CONFIRM**

**Re-verification.** PEC ScopeOfWork coverage by package, recomputed directly:

| Package | SOWs | deliverable dirs |
|---|---:|---:|
| PKG-00 | 2 | 3 |
| PKG-01 | 5 | 6 |
| PKG-02 | 7 | 7 |
| PKG-03 | 5 | 6 |
| PKG-04 | 4 | 5 |
| **PKG-05** | **0** | 2 |
| **PKG-06** | **0** | 6 |
| **PKG-07** | **0** | 5 |
| PKG-08 | 4 | 5 |
| **PKG-09** | **0** | 7 |
| PKG-10 | 5 | 12 |
| **total** | **32** | 64 |

B's claim that PKG-05, PKG-06, PKG-07 and PKG-09 have zero contracts is **exact**, and the 32 initialized contracts do cover PKG-00/01/02/03/04/08/10 only.

**One factual correction.** B states PKG-07 has *"6 deliverables incl. `DEL-07-02` … `DEL-07-05`."* PEC's `Deliverables.csv` shows PKG-07 has **5**: `DEL-07-01` … `DEL-07-05`. The "6" is the count of **scope items** assigned to PKG-07 in the decomposition's §4 table (`SOW-033, 035..037, 039, 087 (6)`), not deliverables. The named deliverables and the zero-contract conclusion are unaffected.

**Severity/class commentary.** WARN is right, and B's handling is exemplary in one respect worth preserving at fan-in: B explicitly states *"this finding does not contest the PEC deferral"* and accepts manifest condition PEC-2/basis-14 that the absence is deliberate sequencing and *"not, by itself, a coverage gap."* The finding is about the **conjunction** across three products, which is genuinely invisible from inside any one of them. That is a legitimate horizontal-lens contribution and is correctly not charged against PEC.

**Confidence: HIGH.**

---

### RB-013 (WARN) — App's D-APP-48 SHA-pinned contract mirror is entirely stale

**Verdict: ADD-MISSING-EVIDENCE**

**B marked the load-bearing count UNKNOWN.** B wrote: *"I did not independently verify the 12/12 count or the shim rewrite — marked **UNKNOWN**"*, and rated the finding MEDIUM confidence on that basis. **I located the pin contract B could not find and verified both claims.**

The artefact is `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json` (`schemaVersion: chirality.flowA.harnessContractPull.v1`, `decisionIds: [D-APP-48, D-T0-09]`). Its `exports` array has **exactly 12 entries**, each carrying a `sourcePath` and a pinned `sha256`.

I recomputed the sha256 of all 12 pinned files at the frozen basis:

| # | Pinned file | Result |
|---:|---|---|
| 1 | `harness-contract/src/index.ts` | **STALE** |
| 2 | `harness-contract/src/agent-engine-port.ts` | **STALE** |
| 3 | `harness-contract/src/engine-conformance.ts` | **STALE** |
| 4 | `harness-contract/src/errors.ts` | **STALE** |
| 5 | `harness-contract/src/event-schema.ts` | **STALE** |
| 6 | `harness-contract/src/mcp/tool-names.ts` | **STALE** |
| 7 | `harness-contract/src/sdk-version.ts` | **STALE** |
| 8 | `harness-contract/src/tool-catalog.ts` | **STALE** |
| 9 | `harness-contract/src/tool-descriptor.ts` | **STALE** |
| 10 | `harness-contract/src/transcript-replay.ts` | **STALE** |
| 11 | `harness-contract/src/types.ts` | **STALE** |
| 12 | `harness-contract/package.json` | **STALE** |

**Result: 12 stale, 0 matching, 0 missing — of 12.** The manifest's "12/12 stale" (conditions App-5 / basis-10) is now independently verified at the frozen corpus rather than accepted on disclosure.

**The shim rewrite is also verified.** `harness-contract/src/index.ts` reads, in full at its head:

> `@deprecated Import from '@chirality/runtime-contracts'.`
> *"This package remains only as a source-compatible facade for one migration cycle. **Runtime contract ownership moved to the repository-root workspace.**"*
> `export * from '@chirality/runtime-contracts';`

**Consequence for B's finding.** B's assertion — that App's only declared mechanism for detecting runtime-contract drift is inoperative — **stands, and its confidence should rise from MEDIUM to HIGH**. B's UNKNOWN marking was appropriate given what B found; the evidence simply existed elsewhere in the corpus.

**Severity/class commentary.** WARN is defensible but sits at the boundary. On the now-verified evidence the mirror is not partially drifted but *wholly* superseded, and its replacement is explicitly a one-cycle facade — so the detection path is not degraded, it is gone, with a stated expiry. Combined with RB-002 (no producer-side compatibility obligation), B's conclusion that App has *no* working drift-detection path in either direction is fully evidenced. The manager may wish to weigh WARN against that.

**Confidence: HIGH** (was MEDIUM in B's report; the upgrade is the substance of this verdict).

---

### RB-015 (INFO) — Root-doctrine change notices reached App and one domain pack but not PEC or Piping

**Verdict: CONFIRM**

**Re-verification by direct enumeration.**
- `projects/chirality-app-dev/execution/_Coordination/`: `NOTICE_D-GOV-21_ROOT_DOCTRINE_AMENDMENT.md`, `NOTICE_D-GOV-23_DIRECTIVE_GENUS_SUPERSESSION.md`, `NOTICE_D-GOV-24_OPERATING_SYSTEM_PROSE_PROPAGATION.md`, `NOTICE_D-GOV-26_SPEC_CONTRACT_AMENDMENTS.md` — **four `D-GOV-*` notices**, exactly as B states.
- `domains/chirality/_Coordination/`: D-GOV-21, D-GOV-23, D-GOV-24 — **three, and no D-GOV-26**, exactly as B states.
- `projects/pec/execution/_Coordination/`: two notices, both HELPS_HUMANS-sourced — **no `D-GOV-*` notice**. Exact.
- Piping: no coordination notice surface. The only `*notice*` matches under `domains/chirality-piping/` are unrelated source-asset manifests and skeletons for a document template whose name contains "NOTICE". B's "none found" is correct.

**One minor correction.** B describes App's two non-`D-GOV` notices as *"two HELPS_HUMANS notices."* One is `NOTICE_2026-07-25_helps_humans_p1_p7_applied.md`; the other is `NOTICE_2026-07-25_CONTRACT_INDEX_CORRECTION.md`, which is not HELPS_HUMANS-titled. Immaterial to the finding.

**Severity/class commentary.** INFO is right given B's framing (B restates it *"only for its bearing on my lens"* and assigns the corrective action to RB-003/RB-006 rather than raising a separate remedy). I reached the same facts independently in my own pass-1 and rated the equivalent observation WARN because I weighted the missing D-GOV-26 notice to PEC against PEC's status as a ruled runtime client. The difference is presentational, not factual: B folds the remedy into other findings; I carried it as its own. No disagreement on evidence.

**Confidence: HIGH.**

---

## 3. WARN/INFO sample record

Four sampled, against a minimum of three. Selection was made before verification, on these stated grounds:

| Finding | Why sampled |
|---|---|
| **RB-008** | B identifies it as *"the mechanism behind items 1, 2, 3, 5 and 6"* — it is the structural claim underpinning B's entire cross-product thesis, so if it failed, several higher-severity findings would lose their explanatory frame. It is also purely documentary and cheaply falsifiable. |
| **RB-011** | It is the only finding that is explicitly a **conjunction** across all three products, and it rests on a count (PEC packages with zero contracts) that is trivially checkable and would be embarrassing if wrong. |
| **RB-013** | B self-marked its load-bearing count **UNKNOWN** and rated confidence MEDIUM — the highest-value target in the report for a challenger, since resolving it either upgrades or collapses the finding. It also bears directly on both BLOCKs. |
| **RB-015** | My own pass-1 covered the same ground independently, so it permits a genuine cross-check of B's enumeration method against mine on shared facts. |

Not sampled: **RB-012** and **RB-014**. Both are latent/forward-looking (an unbuilt release path; a not-current-scope evolution path), both are self-limiting in B's own text, and neither bears on the disputed runtime-ownership cluster. Recording the omission so the sample is auditable.

---

## 4. Out-of-scope observations for fan-in

No IDs, no severities. These are neither confirmations nor new findings; the manager dispositions them.

**(a) The App's own shipped facade states the ownership conclusion that its decomposition denies.** `projects/chirality-app-dev/frontend/packages/harness-contract/src/index.ts` reads: *"This package remains only as a source-compatible facade for one migration cycle. **Runtime contract ownership moved to the repository-root workspace.**"* Neither reviewer's pass-1 report cites this. It bears on RB-001 and RB-005 from a direction neither of us used: the migration is complete in code and in the deprecation notice, and incomplete only in the governed documents — with the decomposition's §13 sentence now the sole artefact in the corpus asserting the contrary. Caveat on admissibility: this is a source file, and both reviewers declared observation boundaries that exclude runtime *behaviour*. I offer it as a **text artefact** (a docblock assertion), not as evidence about how any software runs.

**(b) A machine-readable boundary-declaration pattern already exists in the corpus, and it is close to what RB-008 proposes.** The same `D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json` carries a `boundaries` object with six explicit flags — `registryPublicationAuthorized`, `externalDistributionAuthorized`, `f2CrossingAuthorized`, `f3LiveBindingAuthorized`, `lifecycleTransitionAuthorized`, `releaseOrProfessionalClaimAuthorized` — **all `false`** — alongside a per-file `sourcePath`+`sha256` export list and a named `validation.dependencyLintCommand`. That is, in substance, a machine-checkable declaration of counterparties and boundaries between two surfaces. If the manager takes up RB-008's proposal for an optional `interfaces:`/`consumers:` element in the SOW standard, this artefact is an in-corpus precedent for its shape and should not have to be designed from scratch.

**(c) A convergence worth recording for fan-in classification.** B and I reached the two runtime findings by different routes and from different lenses, and neither of us saw the other's report before freezing. The overlap is close to total on fact (RB-001/RA-003; RB-002/RA-002) and differs only on severity threshold — B's boundary makes "accepted instrument contradicted" and "accepted commitment with no executable coverage" BLOCK; mine required unresolvable or unsafe reliance and returned REVIEW. That is a `STANDING_DIVERGENCE` on calibration over an `AGREED` factual core, and I flag it as such so the manager does not have to infer it. It is also a candidate `SHARED_BLIND_SPOT_RISK` in the opposite direction: **both** of us treated the ownership question as documentary and neither of us examined whether any governed run has actually consumed the daemon — the fact that would settle B's F3 inference at RB-002.

---

**Challenge complete.** Findings challenged: **13** — all 9 BLOCK/REVIEW (RB-001–007, RB-009, RB-010) plus 4 WARN/INFO (RB-008, RB-011, RB-013, RB-015). No new findings minted. `REVIEWER_A_REPORT.md` was not modified.
