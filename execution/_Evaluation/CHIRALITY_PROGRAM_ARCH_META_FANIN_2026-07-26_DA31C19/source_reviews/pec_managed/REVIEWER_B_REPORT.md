# REVIEWER B — PASS-1 REPORT

Horizontal lens: architecture, boundaries, adversarial concordance.

---

## 1. Header

| Field | Value |
|---|---|
| Reviewer | **B** (horizontal lens: Root/App/PEC/runtime/domain ownership; producer–consumer–fallback relations; duplicated truth; circular dependency; self-authorization; cross-product gaps; misplaced scope; adversarial concordance) |
| Basis commit | `da31c19b5656dd74615e308c4215688971d33dc9` (frozen checkout `/Users/ryan/dev/chirality-review-frozen-da31c19`, detached) |
| Charter | `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`, sha256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f` — **verified at the frozen checkout**; read in full before any other review action |
| Common basis manifest | `/Users/ryan/dev/chirality-tandem-review-2026-07-26/FROZEN_BASIS_MANIFEST.md`, read second |
| Date | 2026-07-26 |
| Primary checkout | **Not read.** `/Users/ryan/dev/chirality` was not accessed at any point. |

### 1.1 Manifest identity verification

Every sha256 prefix the manifest asserts for a document I relied on was independently recomputed at the frozen checkout and **matches**:

| File | Manifest prefix | Recomputed |
|---|---|---|
| `docs/PRD_ROOT.md` | `82f7ea2944e7` | `82f7ea2944e7` ✓ |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `14067a7d97c9` | `14067a7d97c9` ✓ |
| `projects/chirality-app-dev/docs/PRD.md` | `ef638f43ccae` | `ef638f43ccae` ✓ |
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `952d3cbf81b0` | `952d3cbf81b0` ✓ |
| `projects/pec/docs/PRD.md` | `de0a969cad15` | `de0a969cad15` ✓ |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `3e5be4e453ed` | `3e5be4e453ed` ✓ |

Counts I independently recomputed and which **match** the manifest: Root 45 live `ScopeOfWork.md` under `execution/PKG-01_*`..`PKG-06_*`; App 53; PEC 32. **No manifest error was found.** One near-miss is recorded for honesty: an initial filter of mine under-counted Root at 43 because two live contracts carry `Evaluation` in their deliverable names (`DEL-05-05_Audit_and_Evaluation_Surface_Governance`, `DEL-05-08_Evidence_Linkage_Completeness_and_Retrieval_Evaluation`) and were caught by a path exclusion intended for evaluation snapshots. The manifest is correct; my filter was not.

### 1.2 Read and sample disclosure

**Read in full (100%):** all three PRDs (`docs/PRD_ROOT.md` 1056 ll.; App `docs/PRD.md` — §§1–9 and §§14–17 in full, §§10–13 by section map and targeted read; PEC `docs/PRD.md` 491 ll.); all three decompositions in full including register structure (Root 616 ll., App 614 ll., PEC 663 ll.); the Root forward-coverage register `chirality_root_prd_coverage_forward_v1_0.csv` (all 84 rows, key columns); the Root scope ledger and deliverable register (targeted, full-column, on every runtime- and boundary-relevant row); the charter in full; the manifest in full.

**Also read in full:** `runtime/README.md`; `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md`; `docs/CONTRACT.md` §1.12–§1.13 and §2 enforcement map; `docs/SPEC.md` §0.2.1–§0.2.2; `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §§1–6; `_DomainEngines/_DECISIONS/_REGISTER.md` rows D-T0-12..D-T0-23; `_DomainEngines/profiles/pec.yaml` (control fields and open-issue block); `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md` (boundary rows).

**ScopeOfWork sampling — exact sample, and what it cannot establish.**

*Root — 45 contracts. Sample: 18 read at frontmatter + section depth (≥ one third), plus one read in full, plus a mechanical scan of all 45.*
- Full text: `DEL-02-02`.
- Frontmatter + interface/dependency/candidate-marker extraction: `DEL-01-03`, `DEL-01-08`, `DEL-02-01`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-03-01`, `DEL-03-03`, `DEL-03-04`, `DEL-03-05`, `DEL-03-06`, `DEL-04-04`, `DEL-04-07`, `DEL-05-01`, `DEL-06-04`, `DEL-06-05`, `DEL-01-02` (targeted, on the invariant-catalog question).
- Every package represented: PKG-01 (3), PKG-02 (5 of 5), PKG-03 (5 of 6), PKG-04 (3), PKG-05 (2), PKG-06 (2). Weighted to PKG-02/PKG-03 as directed.
- Corpus-wide mechanical scan of all 45 for `runtime|daemon` and for `chirality-app|projects/pec|PEC`.

*App — 53 contracts. Sample: all 53 at frontmatter + primary-output (`OUT-001`) depth; 2 read at body depth (`DEL-00-02`, `DEL-03-01`); corpus-wide mechanical scan of all 53 for `D-GOV-20|root-owned|runtime-daemon|daemon`.* Every one of the 11 package groups represented; the frontmatter+OUT-001 pass is a census, not a sample, for identity and scope-reference questions.

*PEC — 32 initialized contracts. Sample: all 32 at frontmatter depth; 3 read at body depth (`DEL-08-01`, `DEL-10-02`, `DEL-00-03`).* **Package representation is structurally impossible to complete:** the 32 initialized contracts cover PKG-00, 01, 02, 03, 04, 08, 10 only. **PKG-05, PKG-06, PKG-07 and PKG-09 have zero ScopeOfWork contracts.** The brief directed me to weight toward PEC PKG-07/PKG-08; PKG-08 is fully sampled (4 of 4, one at body depth), and **PKG-07 — the manifest's named "principal shared-runtime seam" — cannot be sampled because it does not exist as contracts.** This is disclosed manifest condition PEC-2/basis-14 (deliberate P2–P4 sequencing); its cross-product consequence is finding **RB-011**.

**What the sample cannot establish.** (a) I did not read every `AC-*`/`VER-*` body in every contract, so I make no claim about the internal soundness of individual acceptance criteria — only about identity, basis pinning, ownership statements, and cross-product references, for which the App and PEC passes are censuses and the Root pass is a >⅓ sample plus a full-corpus mechanical scan. (b) I did not read `_STATUS.md` bodies at scale and make no lifecycle-state claims beyond the manifest's. (c) Absence claims from mechanical scans are bounded to the literal terms scanned; each such claim below names its terms.

**Tool basis (method rule 5).** **I ran no repo script, validator, or generator.** I relied on no validator PASS. Every mechanical statement below comes from provably read-only shell computation over the frozen checkout (`find`, `grep`, `wc`, `sed`, `shasum`). Where the manifest records a validator result (Root's 45 SOWs passing pre-v6/v6.1; PEC's 32 repaired and validated under the current method; Root's G1–G4 passing), I cite it **as a manifest-recorded result under its stated tool-version era** and draw no independent conformance conclusion from it (manifest §4 version-skew condition; basis-wide condition 15).

**Orientation order (method rule 1).** I formed the account below from the governed records first — PRDs, decompositions, registers, contracts, decision records, profiles — and only then used the charter's §02–§03 architecture sections to challenge it. Where I report agreement with a charter proposition, it is because a governed record independently supports it, and I cite that record, never the charter. Two charter propositions are **contradicted by the governed record** and are reported as such (RB-001, and M3-Q1).

---

## 2. Findings register

### 2.1 Declared observation boundary

My observation boundary is: **the frozen checkout at `da31c19b`, read-only, plus provably read-only shell computation over it.** Within that boundary:

- **BLOCK** — an accepted instrument is contradicted by another accepted instrument, or an accepted-basis commitment is left without any executable coverage anywhere in the corpus, such that a reader relying on the accepted basis could act on an ownership or compatibility assumption the corpus does not support.
- **REVIEW** — needs an owner ruling or a governed-workflow disposition; the corpus is internally survivable but a boundary, owner, or routed path is undeclared or stale.
- **WARN** — a defect whose consequence is contained within one instrument or one loop.
- **INFO** — observation; no action asserted.

I do not observe: runtime behaviour, test results, validator output, git history beyond the frozen HEAD, or the primary checkout. **A severity is a statement about the record, never about the software.** No finding here is a professional-safety verdict (K-DOMAIN-4; D-GOV-02).

Findings are **most severe first**. IDs `RB-###` are stable and not reused.

---

### RB-001 — Two accepted instruments name different semantic owners of the shared runtime

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT (ROOT ↔ APP) |
| **Class** | **Authority conflict** |
| **Severity** | **BLOCK** |
| **Confidence** | **HIGH** |

**Assertion.** The App's accepted decomposition states that App retains *semantic* ownership of the shared runtime and that Root's ownership is merely an implementation location, which directly contradicts D-GOV-20's ruled architecture, `docs/CONTRACT.md` §1.13 K-RUNTIME-1, and the App PRD's own §17 amendment.

**EvidenceRefs.**
- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §13 *Downstream Execution Notes*, line 611, verbatim: *"Shared runtime promotion preserves this decomposition's existing package/deliverable topology. Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership and acceptance evidence through the SCA-APP-003 impact map."*
- Against: `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` §Ruled architecture items 1–2 — the harness *"becomes a root-owned `runtime/` workspace"*, and one daemon *"exclusively owns runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency."*
- Against: `docs/CONTRACT.md` §1.13 **K-RUNTIME-1** — *"Desktop, CLI, and project proxies MUST NOT construct a competing runtime"*, enforcement *"Runtime daemon singleton; client conformance; packaged-process inspection."*
- Against: `projects/chirality-app-dev/docs/PRD.md` §17 (second, *Shared Runtime and Local-Agent Pilot Amendment*), line 1694: *"D-GOV-20, D-APP-73, and SCA-APP-003 make the provider-neutral runtime a root-owned product subsystem rather than a frontend-owned singleton."*
- `_DomainEngines/_DECISIONS/_REGISTER.md` row **D-T0-23**: *"app-dev and PEC become registered clients of one daemon."*
- The App decomposition's own conflict-surfacing duty is unexercised on this point: §2.1 *"If a downstream task discovers conflict among these documents, it must surface the conflict rather than silently reconcile it"*, and PRD §16: *"If this PRD and the active SOFTWARE_DECOMP snapshot disagree about package topology, deliverable IDs, coverage telemetry, or decomposition method, the conflict must be surfaced and resolved through governed PRD/decomposition amendment before scaffold or REVIEW closure."*

**Consequence.** The App decomposition is the accepted basis a Type-2 executor and a REVIEW gate read. A reader who takes it at its word concludes that App may continue to define runtime semantics and that Root holds only a directory. A reader of D-GOV-20/K-RUNTIME-1 concludes the opposite. That is precisely the condition under which a second runtime loop, a divergent protocol version, or a competing session/credential owner can be built *while every party believes it is conforming*. K-RUNTIME-1's stated enforcement ("client conformance") presupposes a settled contract owner; the corpus does not currently supply one. This is the charter's accepted-basis proposition (§04: *"Runtime ownership must land at Root; consumer products cannot redefine it silently"*), and it is contradicted by a governed record, which per the brief is itself the evidence.

**SmallestAction/Owner.** The least expansive lawful correction is **an App `SCOPE_CHANGE` amendment (SCA-APP, ruled by a `D-APP-*` record) that replaces the line-611 sentence** with the distinction the rest of the corpus already draws: App retains ownership of *client integration, presentation, packaging, and conformance evidence*; Root owns the runtime contract and its semantics. Owner: `projects/chirality-app-dev/execution/_ScopeChange/` + App decision register. A routed coordination notice to the Tier-0 surface and the PEC loop is required in the same tranche under the `AGENTS.md` change-notice rule / Root PRD D-11. **Do not** fix this by editing the decomposition prose without a ruling; D-9 and the charter's routing rule both forbid it.

---

### RB-002 — Root `runtime/` has no owning package, deliverable, write locus, or SOW anywhere in the accepted Root decomposition

| Field | Value |
|---|---|
| **Product/Surface** | ROOT (`execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`; upstream `docs/PRD_ROOT.md` §5.2 O-2) |
| **Class** | **Ownership gap** (upstream cause: PRD omission) |
| **Severity** | **BLOCK** |
| **Confidence** | **HIGH** |

**Assertion.** `runtime/` — a live seven-package executable workspace ruled Root-owned — is covered by the accepted Root decomposition only as an *authority-boundary statement*. No Root package scope, no Root deliverable, no `AnticipatedWriteLocus`, and no Root ScopeOfWork contract owns the runtime contract, its versioning, its client-compatibility obligation, its migration, its security review, or its release evidence.

**EvidenceRefs.**
- The artifact exists: `runtime/` contains `packages/{contracts,core,daemon,client,cli,engine-claude,engine-pi-omlx}`, `tests/`, workspace `package.json`. `runtime/README.md`: *"The daemon is the sole owner of engines, credentials, sessions, delegation, turn locks, interruption, tools, and local-model residency."*
- Root decomposition §2.1 **DEC-001 / REF-001**: `docs/PRD_ROOT.md` is the **sole** scope source; §2.3 lists `AGENTS.md`, `DIRECTIVE`, `CONTRACT`, `TYPES`, D-GOV-21 §5 and the live registries as *"non-source, generates no scope"*. **D-GOV-20 is not even in the interpretive list.**
- The PRD's entire runtime commitment is `§5.2 O-2(c)` — the substrate *"which executes and carries work but whose transport never grants project authority and whose user-data state is operational, not project truth"* — plus `O-10`'s closed-boundary clarification.
- Normalization: `chirality_root_scope_ledger_v1_0.csv` **SOW-027** carries all three O-2 layers as **one** scope item; **SOW-035** carries O-10. Both map to **`DEL-02-02` alone**.
- `chirality_root_deliverable_register_v1_0.csv` **DEL-02-02**: Type `REQ_SLICE`; artifacts *"Layer boundary register; runtime transport/authority separation notes; fourth-substrate guard note"*; envelope note *"Three bounded layers with one authority rule; **no implementation change implied**"*; write locus *"execution-tree; instruction-surface (M2) if a layer statement must change."*
- **Asymmetry of the decomposition's own splitting rule.** DEC-004/DEC-005 split N-1 and N-5 into separate scope items *"because their clauses have different maintenance loci"*; DEC-004's rationale is explicit that *"the exception's maintenance locus is the variant/domain boundary … not the normative corpus."* O-2's three layers have three plainly different maintenance loci (`agents/`+`docs/`; `tools/`; `runtime/`) and were **not** split. The runtime clause therefore inherited an instruction-surface-shaped write locus.
- Mechanical scan of all 45 Root SOWs for `runtime|daemon`: **4 hits** — `DEL-02-02` (6), `DEL-01-06` (2), `DEL-02-03` (1), `DEL-04-07` (1). Full read of `DEL-02-02/ScopeOfWork.md` confirms its three outputs (`OUT-001`..`OUT-003`) are a layer register, separation notes, and a guard note; its Write-locus gate section states *"This Scope of Work grants no such authorization."*
- Mechanical scan of the Root deliverable register for `runtime|daemon|credential|adapter|protocol` across all 45 rows: **no row carries `runtime/` as an `AnticipatedWriteLocus`.** The declared loci are `execution-tree`, `instruction-surface (M2)`, `tools/ (M2)`, `exports/ (M2)`, `execution/_harness`.
- **No M2 gate covers it either:** `docs/SPEC.md` §0.2.1 enumerates the instruction surface as `AGENTS.md`, `CLAUDE.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`. `runtime/` is **not** a member. So changing `runtime/` is neither an M2 governance tranche nor a deliverable-scoped act.
- The obligations left unowned are real and accepted: `docs/CONTRACT.md` §1.13 defines **K-RUNTIME-1, K-CONTROL-1, K-PROJECT-1, K-STORE-2, K-RESIDENCY-1, K-ROLE-2, K-EXPORT-1** with live enforcement points, and §2's map row *"Shared runtime daemon and clients (runtime)"* binds them. D-GOV-20 §Implementation gates names *"Daemon/client/CLI, Desktop migration, PEC migration, security review, and regression review"* and gates public export on *"the app-dev and PEC vertical slices"*. None of these appears as a Root deliverable.
- Root covers the invariant catalog only as a **register**: `DEL-01-02_Invariant_Catalog_Conformance_Register`'s SOW explicitly reaches §1.13 (*"§1.13 defines seven further …; the live catalog is recorded as holding 34 across 13"*) — mapping, not production.

**Consequence.** Root's F4 registers close (83 COVERED / 1 deferred / 0 UNCOVERED) because F4 is computed **PRD-item → decomposition**, and the PRD item is thin. The decomposition is internally faithful; the accepted *basis* is larger than its sole scope source. The practical effect is that the one function two other products are ruled to be clients of has **no producer** in any accepted scope, no declared write target, and no governance gate — while `AGENTS.md` §Shared Runtime Doctrine, D-GOV-20, D-T0-23 and both consumer PRDs all rely on it existing. It is also the exact shape of PRD falsifier **F3** (self-authorization): root development already consumes a runtime capability that was never accepted through a root deliverable stream. The Root decomposition's own OI-013 precedent shows the mechanism — *"the gap is inside the objective, where the registers cannot see it."* The same blindness applies to O-2.

**SmallestAction/Owner.** This is a **PRD gap, not a decomposition gap**, and per the charter must not be invented downstream. Smallest lawful sequence: **(1)** an amendment to `docs/PRD_ROOT.md` — an M2 instruction-surface tranche under D-13/D-16 with independent owner authorization — adding one operative commitment that the root runtime contract, its version/compatibility obligation to declared clients, and its release evidence are Root-owned; **(2)** a Root `SCOPE_CHANGE` splitting SOW-027 by maintenance locus and adding the corresponding deliverable(s) to PKG-02 or a new package, with `runtime/` as a declared write locus. Owner: Root PRD / `D-GOV-*` for (1); `AGENT_SCOPE_CHANGE` + Root decomposition registers for (2). An acceptable interim is an **explicit recorded deferral** in the forward register — which would at least make the gap machine-visible, as OI-013's deferral did for OBJ-2.

---

### RB-003 — Tier-0 D-T0-23 still preserves PEC capabilities that PEC's later-adopted PRD permanently retired, with no supersession recorded at the Tier-0 surface

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT (`_DomainEngines/_DECISIONS/_REGISTER.md` row D-T0-23 ↔ `projects/pec/docs/PRD.md` v2.1) |
| **Class** | **Authority conflict** |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** D-T0-23 (RULED 2026-07-22) records as accepted cross-project basis the preservation of PEC's *"deterministic adapter service … RBAC … scratch/demo pilot fence"*; PEC PRD v2.1 (adopted 2026-07-24 by D-PEC-58) retires exactly those. The Tier-0 register records no supersession.

**EvidenceRefs.**
- `_DomainEngines/_DECISIONS/_REGISTER.md`, D-T0-23 ruling cell: *"**RULED 2026-07-22: accepted Shared Runtime and Local-Agent Pilot plan** — retire PEC's independent LLM/session/delegation ownership prospectively; **preserve its deterministic adapter service, human acts, visibility basis, scratch/demo pilot fence**, and open production gates"*; scope cell: *"project/domain authority, deterministic acts, **RBAC**, data boundaries … remain independently governed."*
- `projects/pec/docs/PRD.md` §8: *"the prototype's implemented 14-role RBAC set … are retired; access classes are owner, harness, and admin."*
- §13 (Prototype disposition): *"Domain-engine registration (`pec.yaml`, L3 import lane) — L3 operation-proposal lane sunset with the old product"*; *"Demo DB, fixtures, seed/drill tooling — Retired."*
- §15: *"**`D-PEC-56` — partially superseded on adoption (2026-07-24).** Its ruled behavior 1 (retain PEC's deterministic acts, RBAC, reporting, and domain tools as a project adapter service) **does not survive the product retirement in §8/§13**."* — the supersession is declared against `D-PEC-56` only; **D-T0-23 is not named anywhere in the PEC PRD.**
- Ordering is unambiguous: D-T0-23 is dated 2026-07-22; D-PEC-58 adoption 2026-07-24.

**Consequence.** The Tier-0 register is the corpus's declared home for cross-project coupling (manifest §Cross-product control surfaces; D-T0-19 was created precisely as a *"new coupling row (no prior register home)"*). It currently asserts, as ruled cross-project basis, the continued existence of a PEC adapter service that PEC's product definition of record has retired. Anything reading D-T0-23 for the App↔PEC↔runtime relation — including App's reliance-boundary register, which does (RB-006) — inherits the stale description. Because the PEC loop holds **no** routed D-GOV/D-T0 notices (RB-012), no mechanism currently exists by which this reaches PEC.

**SmallestAction/Owner.** A **Tier-0 residual row** in `_DomainEngines/_DECISIONS/_REGISTER.md` recording that D-T0-23's PEC-preservation clause is partially superseded by D-PEC-58 / PRD v2.1 §8/§13/§15, on the same "residual of D-T0-NN" convention the register already uses (D-T0-17, D-T0-18, D-T0-20, D-T0-21). No PEC or App instrument need change. Owner: Tier-0 decision register (owner ruling).

---

### RB-004 — The adopted PEC domain-engine profile is a live control surface asserting an integration level and data-residency basis the adopted PEC PRD forbids

| Field | Value |
|---|---|
| **Product/Surface** | PEC / CROSS_PRODUCT (`_DomainEngines/profiles/pec.yaml`) |
| **Class** | **Authority conflict** (machine surface carrying stale authority) |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** `_DomainEngines/profiles/pec.yaml` remains `profile_status: ADOPTED` with `integration_level: OPERATION_PROPOSAL` (L3) and `data_residency: OPEN_ENUMERATED`, and carries an `operation_proposal_contract` and RBAC-scoped agent visibility — all of which PEC PRD v2.1 retires as permanent non-goals.

**EvidenceRefs.**
- `_DomainEngines/profiles/pec.yaml` l.26 `profile_status: "ADOPTED"`; l.27 `integration_level: "OPERATION_PROPOSAL"  # L3, imports scope — D-T0-18 O-A + D-PEC-12`; l.28 `data_residency: "OPEN_ENUMERATED"` … *"LLM-hosted agent sessions may read, and route to the owner-configured model provider, exactly the enumerated surface … under the agent person's RBAC visibility, is_admin=0"*; l.141 `operation_proposal_contract:`; l.147 *"engine-controlled apply through PEC's RBAC API with append-only history/audit evidence."*
- Against `projects/pec/docs/PRD.md` §4.2 permanent non-goals: *"Not an orchestrator … Not a ruling surface. No write path records adoption, ruling, or direction"*; §8 RBAC retired; §13 *"L3 operation-proposal lane sunset with the old product; profile superseded when v2 has shape"*; **PEC-K-10** *"Content-minimal … never file or diff content."*
- The profile's own open-issue block (l.177) still records the pre-adoption reading: *"Shared runtime migration: RULED 2026-07-22 by D-T0-23/D-PEC-56. **PEC retains deterministic acts, RBAC, human-only acts, visibility, and data boundaries as a project adapter**"* — i.e. it mirrors RB-003's stale text.
- **Direct governance precedent for treating this as a rulable conflict, not agent-normalizable drift:** `docs/governance_harness/_DECISIONS/D-GOV-06_domain_profile_current_truth.md` — *"a human must rule the fact (K-CONFLICT-1)"* — ruled exactly this class of defect for the `open_pipe_stress` profile (stale `profile_status`, stale banner, stale header comments).
- PEC has recorded the obligation but scheduled no instrument: PEC decomposition SSOW **SOW-090**, `OUT`, *"Supersession of the `pec.yaml` domain-engine profile (L3 lane sunset) — **Deferred**: named open follow-on once v2 has implementation shape."*

**Consequence.** Manifest condition PEC-1 discloses that the profile "awaits full v2 supersession"; the consequence to assess is that this is **not documentation lag — it is an ADOPTED machine-readable control surface**. Domain-engine workflows read `integration_level` and `data_residency` to decide what a harness may read, propose, and validate, and what may egress to a model provider. As it stands, the accepted profile grants an agent-visible, provider-egressing surface and an operation-apply lane to a product whose adopted PRD forbids both. That is the charter's *"machine surfaces acquiring authority"* condition with a live blast radius, and D-GOV-06 establishes that the corpus already treats this class as owner-rulable. The deferral condition ("once v2 has implementation shape") is a *later* trigger than the harm, because the stale grant is in force now.

**SmallestAction/Owner.** Do **not** wait for v2 shape. The smallest lawful act is an **interim owner ruling on the D-GOV-06 pattern** recording the divergence and, at minimum, demoting the grant-bearing fields (`integration_level`, `data_residency`) or marking the profile `SUPERSEDED_PENDING_V2`. Owner: `DOMAIN_ENGINE` (Agent 1) proposing; owner ruling in `_DomainEngines/_DECISIONS/` or `projects/pec/.../_DECISIONS/`. Full supersession remains SOW-090's deferred work.

---

### RB-005 — The App ScopeOfWork layer was never propagated for the shared-runtime rehoming; the executable contract still delivers an App-owned runtime engine contract

| Field | Value |
|---|---|
| **Product/Surface** | APP — `PKG-03`, principally `DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite` |
| **Class** | **Trace gap / ownership gap** |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** Of 53 App ScopeOfWork contracts, exactly one mentions the daemon or D-GOV-20; `DEL-03-01`'s primary output is still *"A product-owned AgentEnginePort / RuntimeEngineContract"* delivered under App scope item SOW-037, with no reference to Root ownership.

**EvidenceRefs.**
- Mechanical scan of all 53 App SOWs for `D-GOV-20|root-owned|runtime-daemon|daemon`: **one** file matches — `DEL-05-05_ToolResultStore_and_Session_Artifacts` (6 hits).
- `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/ScopeOfWork.md` — frontmatter `project_scope_refs: [SOW-037]`, `decomposition_basis: …Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb`; `OUT-001` verbatim: *"A product-owned AgentEnginePort / RuntimeEngineContract, runtime contract documentation, and conformance tests for stub and provider/SDK-backed adapters."* Type `API_CONTRACT`.
- App decomposition SSOW `SOW-037`, unchanged by SCA-APP-003: *"Define product-owned `AgentEnginePort` / `RuntimeEngineContract`. | SDK APIs do not define public semantics."*
- The rehoming reached only three surfaces of the decomposition and none of the contracts: Open Issue **OI-007** (`SHARED_RUNTIME`, still open), **DEC-019**, and §13 line 611 (which asserts the opposite — RB-001). Change Log 2026-07-22: *"SCA-APP-003 prospectively activated the shared-runtime extraction … **without changing package/deliverable topology or lifecycle state**."*
- Corroborating drift in the same layer: several App SOW directory names still carry the pre-SCA-APP-004 identities the decomposition renamed — e.g. `DEL-02-01_Desktop_Shell_and_Matrix_Navigation` (decomposition: *Woven Dialogue Shell and Compatibility Navigation*), `DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision` (decomposition: *First-Adapter Probe…*), `DEL-05-04_Runtime_Replay_and_Transcript_View` (decomposition: *Runtime Replay, Dialogue, and Agent Transcript Projection*). The contract bodies were updated (their `OUT-001` text matches the new names) while the directory identities were not.

**Consequence.** The ScopeOfWork layer is the layer a bounded Agent 2 executor actually reads, and the layer REVIEW's checklist is compiled from. It currently instructs an executor to build and conformance-test an App-owned runtime engine contract — the artifact D-GOV-20 ruled Root-owned. Combined with RB-002 (no Root owner) the practical outcome is that the *only* executable instruction in the corpus to produce a runtime engine contract sits in the consumer product. That is scope which has migrated to the wrong product and has not been migrated back.

**SmallestAction/Owner.** An App `SCOPE_CHANGE` amending **SOW-037's statement** and `DEL-03-01`'s `OUT-001`/`REQ-*` to scope App's deliverable to *client conformance against the Root-owned contract*, or an explicit recorded deferral if the owner intends App to hold it until Root's package exists. Directory-name realignment should ride the same tranche only if the owner authorizes renumbering-adjacent renames (I5 stability caution applies to IDs, not names). Owner: `projects/chirality-app-dev/execution/_ScopeChange/` + `D-APP-*`.

---

### RB-006 — The only live register of shared-runtime reliance boundaries is owned by a consumer, and its PEC row describes a retired product

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT — `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md` (artifact of App `DEL-01-02_Reliance_Boundary_Register`) |
| **Class** | **Ownership gap + semantic conflict** |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** The corpus's only register of runtime reliance boundaries lives inside the App working root, asserts boundaries about Root's daemon and about PEC, and its PEC row describes capabilities PEC PRD v2.1 retired.

**EvidenceRefs.**
- `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md` (163 ll.), rows:
  - `RB-DAEMON` — *"Exactly one runtime owner per user. | Daemon singleton, restart recovery, **Desktop/CLI/PEC clients**. | GUI, route, CLI, or PEC sidecar may not construct a second engine/session loop."*
  - `RB-PROJECT-REGISTRATION` — manifest authority identity vs user-data resolution.
  - `RB-PEC-ADAPTER` — *"PEC remains project authority over acts/data. | **PEC adapter RBAC**, human-only act exclusion, **scratch/demo fence**. | Generic runtime mutation bypass or production dual execution loop."*
- Its owning contract is App-side and P0: App decomposition `DEL-01-02` (`REQ_SLICE`, artifacts *"`docs/harness/reliance_boundary_register.md`; enforcement matrix; test index"*); App PRD FR-124 *"A reliance-boundary register shall identify ownership for product-critical semantics … P0 boundaries cannot be prompt-only."*
- `RB-PEC-ADAPTER`'s content is retired by `projects/pec/docs/PRD.md` §8 (RBAC retired), §13 (demo/fixtures retired; L3 lane sunset), §15 (D-PEC-56 behaviour 1 does not survive) — the same staleness chain as RB-003/RB-004.
- No corresponding Root-side register exists: mechanical scan of all 45 Root SOWs for `chirality-app|projects/pec|PEC` returns only `DEL-04-07` (export boundary), `DEL-06-05` (domain-engine truth boundary) and `DEL-01-08` (non-goal register) — none is a reliance-boundary register, and none names App or PEC as a runtime consumer with a compatibility obligation.

**Consequence.** A boundary register is the artifact by which "who enforces what" is answerable. Here the enforcement claim about a Root-owned singleton, and a claim about a second product's authority, are maintained by a third party in its own working root — with no routed path to either. `RB-PEC-ADAPTER` therefore asserts a P0 boundary that its subject no longer implements, and App's own conformance tests would be testing against a description PEC has retired. This is duplicated truth with divided ownership in the charter's exact sense: *"'Shared' describes use; it does not authorize divided ownership."*

**SmallestAction/Owner.** Two-part, both small: **(a)** ship a routed coordination notice for the `RB-PEC-ADAPTER` row to `projects/pec/execution/_Coordination/` under the `AGENTS.md` change-notice rule, so PEC can adopt, amend, or decline it under its own instruments; **(b)** when RB-002's Root package exists, re-home `RB-DAEMON`/`RB-PROJECT-REGISTRATION` to it and leave App holding the client-side rows. Until (b), the App register should state that it is a **consumer-side** register and is not the semantic owner of the daemon boundary. Owner: App `DEL-01-02` remediation + App PRD/SCOPE_CHANGE for the ownership statement.

---

### RB-007 — The runtime event-contract home and the daemon global event feed are declared cross-loop decisions with no owning instrument on the producing side

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT (PEC `PKG-00`/`PKG-07` ↔ Root `runtime/`) |
| **Class** | **Ownership gap** |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** PEC declares two cross-loop dependencies on the Root runtime, names the closing act as a cross-loop ruling, and correctly fences itself out of the producing side — and no Root or App instrument carries a matching producer obligation.

**EvidenceRefs.**
- `projects/pec/docs/PRD.md` **PEC-STR-002**: *"Event contract types shall be versioned and consumable by daemon, hooks CLI, and adapters alike; their home (shared runtime contracts vs a PEC-local schema with a pinned mirror) is a cross-loop placement decision (§16) — **writes into root `runtime/` are outside PEC's fences and require their own coordination.**"*
- PRD §16 open decisions **2** (*"Design and ownership of a daemon global event feed (today: per-session SSE only)"*), **6** (auth reuse: PEC tokens vs the daemon's project-scoped token registry), **9** (event-contract home + transport).
- PEC decomposition: **SOW-074** `OUT` *"Writes into root `runtime/`, including placing the event contracts there — **Deferred**, not permanent … requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home, that write becomes required work under its own instrument."*; **SOW-076/OI-002** closing act *"§16 ruling (**cross-loop**)"*; **SOW-083/OI-009**; **SOW-080/OI-006**.
- Risk already priced by PEC: §8 Context Budget QA — *"Two OI-coupled MEDIUM risks … DEL-00-02 (event-contract schema — OI-009 decides its home) and DEL-08-01 (socket + tokens — OI-006 decides the auth mechanism)."* Confirmed in `DEL-08-01/ScopeOfWork.md` REQ-005/REQ-006, CON-001/CON-002, TBD-002.
- Consuming deliverables exist: `DEL-07-02_Daemon_SSE_subscriber_bridge` (SOW-035), `DEL-07-05_Shared-runtime_client_seam_(v2)` (SOW-087) — **both in PKG-07, which has zero SOWs** (see RB-011).
- Producing side: no Root deliverable (RB-002); mechanical scan of Root SOWs finds no PEC-facing obligation; the Tier-0 register's most recent runtime row is D-T0-23, which is itself stale (RB-003).

**Consequence.** PEC's fencing is exemplary — it is the model behaviour the charter asks for, and it is why this is not a PEC defect. But a dependency that is correctly fenced on the consumer side and unowned on the producer side is still an unowned dependency. The named closing act ("§16 ruling (cross-loop)") has no addressee: `§16` is PEC's own open-decision list, and PEC cannot lawfully rule on `runtime/`. Concretely, PEC-STR-003's *"runtime-daemon SSE subscriber"* bridge presumes a daemon feed shape that PEC records as *undesigned and unowned*; PEC's own assessment is that this *"affects SOW-035 efficiency, not correctness"*, which is a defensible bound on PEC's side and says nothing about who builds the feed.

**SmallestAction/Owner.** Record the three items (event-contract home, daemon global event feed design+ownership, auth-token reuse) as a **Tier-0 coupling row** in `_DomainEngines/_DECISIONS/_REGISTER.md` — the register's own precedent for exactly this (D-T0-19 was created as a *"new coupling row (no prior register home)"* for the pec↔app-dev bridge). That routes them to an instrument that can rule across loops without creating scope in either product. Owner: Tier-0 register + owner ruling. If RB-002 is fixed first, the producer obligation lands naturally in the new Root runtime deliverable and this row becomes a pointer.

---

### RB-008 — The ratified ScopeOfWork standard has no interface, consumer, or dependency element, so cross-product relations have no home in the executable contract layer

| Field | Value |
|---|---|
| **Product/Surface** | ROOT — `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (ratified; D-GOV-16) |
| **Class** | **Omission** |
| **Severity** | **WARN** |
| **Confidence** | **HIGH** |

**Assertion.** The standard's canonical form specifies six required level-two headings and a six-field YAML subset, none of which declares interfaces, consumers, producers, or cross-deliverable dependencies; consequently no ScopeOfWork in any of the three products declares a cross-product producer/consumer relation.

**EvidenceRefs.**
- `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §3: YAML subset is `schema`, `deliverable_id`, `package_id`, `decomposition_basis`, `project_scope_refs`, `package_objective_refs`. Required headings: *Purpose and Objective Traceability; Deliverable Definition — Ontology; Completion and Reliance Basis — Epistemology; Production and Verification Method — Praxeology; Governing Values and Decisions — Axiology; Output and Evaluation Matrix*.
- §4 identifier grammar: `OUT`, `CLM`, `REQ`, `AC`, `VER`, `AX`, `TBD`, `CON`, `REM`. **No interface or dependency prefix.**
- §5 matrix columns: `Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation`. Evidence is required; **interfaces are not.**
- Observed effect: zero of 45 Root SOWs names App or PEC as a runtime consumer; zero of 53 App SOWs (bar one incidental) names the Root daemon as the contract's counterparty; PEC's three body-read SOWs carry their cross-product dependencies only as `CON-*`/`TBD-*` prose (`DEL-08-01` CON-001/CON-002), which is the best the grammar permits.
- PEC uses a separate per-deliverable mechanism instead — `Dependencies.csv` in all 64 deliverables (manifest §PEC) — which is intra-product and, by K-DEP-1/K-DEP-2, deliberately deliverable-local.

**Consequence.** The charter's SOW test ("name interfaces and evidence") is only half-satisfiable by construction. More importantly, this is the *mechanism* by which RB-002, RB-005 and RB-007 remain invisible to deterministic checking: because no contract declares a counterparty, no validator can detect a producer obligation with no producer, or a consumer contract pointed at the wrong owner. The corpus's cross-product relations currently live only in decision records, PRD prose, and open-issue tables — surfaces no gate reads.

**SmallestAction/Owner.** Add an **optional** `interfaces:` / `consumers:` block (or an `IFC-*` identifier prefix) to the standard's canonical form, so that a deliverable *may* declare a counterparty and a validator *can* check it. Optional, not required — making it mandatory would retroactively invalidate 130 contracts. Route as an M2 instruction-surface tranche against `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`; owner: the D-GOV-16 instrument. **This is a proposal, not a finding of non-conformance against any contract** — every contract I sampled conforms to the standard as written.

---

### RB-009 — App PKG-00 control contracts pin a package README as their `decomposition_basis` and carry scope/objective references that exist in no accepted decomposition

| Field | Value |
|---|---|
| **Product/Surface** | APP — `DEL-00-01`, `DEL-00-02` (PKG-00 DAG Closure and Project Control) |
| **Class** | **Overreach** (bounded self-authorization) |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** Two of App's 53 contracts derive their basis, scope items, and objectives from a README inside the execution tree rather than from an accepted decomposition.

**EvidenceRefs.**
- `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-0{1,2}/ScopeOfWork.md` frontmatter: `decomposition_basis: projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/README.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb`; `project_scope_refs: [CONTROL-SCC-002]` / `[CONTROL-SCC-001]`; `package_objective_refs: [DAG-CLOSURE]`.
- The standard's stated form for that field is `decomposition_basis: path/to/accepted/decomposition@<commit>` (`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §3).
- `CONTROL-SCC-001`, `CONTROL-SCC-002` and `DAG-CLOSURE` appear nowhere in `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (78 `SOW-*`, 10 `OBJ-*`, 10 `PKG-*`, 51 `DEL-*`).
- The contracts are self-aware about the boundary: `DEL-00-02` CLM-003 `GraphParticipation: EXCLUDED_CONTROL_DELIVERABLE`; `StructuredDependencyRegister: Intentionally absent`; CLM-004 *"This deliverable is a PKG-00 control artifact, not a product implementation deliverable … PKG-00 and DEL-00-* control deliverables are outside the strict product dependency graph … Any approved row change must be applied in the owning product deliverable register, not in this control deliverable."*
- The cited authority is responsibility-only: CLM-002 `ResponsibleParty` — *"Ryan Tufts (K-AUTH-1) — assigned 2026-07-18 by D-APP-65 (demonstrator scope; the assignment names the accountable human only and renders no acceptance, issuance, or sign-off)."*
- Also observed and material to reliance: `DEL-00-02` currently reports `StrictSCCCount 0`, `SCC_Size 0`, *"No active SCC-001 closure artifacts remain"* — i.e. the cycle it exists to close is closed, and the contract is a live container for a discharged condition.

**Consequence.** Manifest condition App-8 discloses the 51-vs-53 count and says it "requires the PKG-00 explanation"; the consequence to assess is *what the explanation costs*. The explanation is that a project loop authored a package README, pinned it as a decomposition basis, and minted a scope-item namespace (`CONTROL-*`) and an objective (`DAG-CLOSURE`) from it. That is the shape of self-authorization the charter asks about — a product creating its own scope basis outside the decomposition pipeline (Root PRD D-9: *"packages and deliverables come only from an accepted decomposition. Nothing authorizes inventing packages from discussion"*). It is genuinely bounded — control-only, graph-excluded, explicitly forbidden from mutating product registers — which is why this is REVIEW and not BLOCK. But the bound is asserted *by the artifacts themselves*, which is exactly the reasoning the corpus otherwise rejects.

**SmallestAction/Owner.** Record an explicit owner ruling that PKG-00 is a **control overlay outside decomposition truth**, naming its authorizing decision and its permanent exclusion from product scope — or, equivalently, add a `CONTROL_PACKAGE` provision to the SOW standard so the `decomposition_basis` field has a lawful non-decomposition value. Given `DEL-00-02` reports its SCC closed, a retirement disposition is also available and may be the smaller act. Owner: App decision register (`D-APP-*`), or `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` via M2 for the general provision.

---

### RB-010 — App's required invariant-coverage register is absent with no deferral, leaving the runtime and engine invariant families owned only at family-prose level

| Field | Value |
|---|---|
| **Product/Surface** | APP — `contract_invariant_coverage_register.csv` (required companion register of decomposition v3.2) |
| **Class** | **Omission** |
| **Severity** | **REVIEW** |
| **Confidence** | **HIGH** |

**Assertion.** The register that v3.2 declares required-or-explicitly-deferred does not exist and no deferral ruling was found, so the `K-CORE/K-ENGINE/K-RELIANCE/K-SDK` and runtime-adjacent invariant families have per-family prose ownership only.

**EvidenceRefs.**
- `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §2.2: *"`contract_invariant_coverage_register.csv` | Planned authoritative companion register | … **It must be created or explicitly deferred before REVIEW closure**."*
- §10B Acceptance Checklist: *"CONTRACT invariant coverage | `contract_invariant_coverage_register.csv` is created, synchronized with this decomposition, or explicitly deferred before REVIEW closure."*
- **DEC-015**: *"`contract_invariant_coverage_register.csv` is a planned required companion register until the artifact exists … this decomposition should not claim an authoritative companion CSV has already been created."*
- What exists instead is §10A.1's ten-row *"Compact invariant-family ownership"* table, e.g. *"`K-CORE`, `K-ENGINE`, `K-RELIANCE`, `K-SDK` | PKG-01, PKG-03, PKG-04, PKG-09 | Product-owned terms, engine contract, provider/SDK adapter isolation, first-adapter conformance, fallback."*
- Manifest conditions App-4 and basis-9 disclose the absence.

**Consequence.** Assessing the consequence rather than rediscovering the fact: the missing register is the one artifact that would have mapped **each** `K-*` invariant to a single owning deliverable and enforcement surface. Its absence is why the runtime-ownership question in RB-001/RB-002 has no App-side machine record to contradict or confirm: `K-RUNTIME-1`, `K-CONTROL-1`, `K-PROJECT-1`, `K-STORE-2`, `K-RESIDENCY-1`, `K-ROLE-2` are framework invariants that constrain App as a client, and §10A.1's family table does not list them at all (its rows stop at App-local families). So the invariant family most affected by the shared-runtime rehoming is the one the coverage surface does not reach — in either product. Note the asymmetry with Root, which *does* carry this work as a deliverable (`DEL-01-02_Invariant_Catalog_Conformance_Register`, whose SOW explicitly reaches CONTRACT §1.13).

**SmallestAction/Owner.** Either produce the register, or record an **explicit deferral ruling** naming REVIEW closure as its gate — the decomposition already specifies both options, so no new commitment is created either way. If produced, it should include the §1.13 framework families as *consumed* invariants. Owner: App decomposition companion registers + `D-APP-*` for the deferral.

---

### RB-011 — The shared-runtime seam has no ScopeOfWork contract in any of the three products

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT (PEC `PKG-07`; Root; App) |
| **Class** | **Observation with cross-product consequence** |
| **Severity** | **WARN** |
| **Confidence** | **HIGH** |

**Assertion.** No contract anywhere in the corpus specifies the runtime↔client seam: PEC PKG-07 is uninitialized by design, Root has no runtime deliverable at all, and App's runtime contracts describe an App-owned artifact.

**EvidenceRefs.**
- PEC: `PKG-07_Event_Ingest_&_Bridges` (6 deliverables incl. `DEL-07-02` daemon SSE bridge, `DEL-07-05` shared-runtime client seam) has **0** ScopeOfWork files; the 32 initialized contracts cover PKG-00/01/02/03/04/08/10 only. `PhaseHint` P3/P4 (decomposition §5).
- Root: RB-002.
- App: RB-005.
- Manifest conditions PEC-2 and basis-14 record the PEC deferral as deliberate sequencing and explicitly state it is *"not, by itself, a coverage gap."* I accept that: **this finding does not contest the PEC deferral.**

**Consequence.** The consequence I assess is the *conjunction*, which no single product's record can see. Each product's own posture is defensible in isolation — PEC sequences P3/P4 lawfully, Root faithfully decomposed a thin PRD clause, App preserved topology across an in-place amendment. Together they produce a corpus in which the one seam three products depend on is specified nowhere. This is the fan-in condition the charter's ownership test exists to catch, and it is only visible cross-product.

**SmallestAction/Owner.** None inside PEC. This is discharged by RB-002 (Root ownership) and RB-007 (Tier-0 routing of the contract home and feed ownership); it is recorded separately so the conjunction is not lost when the individual items are dispositioned.

---

### RB-012 — PEC's kill test — the executable form of its graceful-absence invariant — has no accepted release path to bind into

| Field | Value |
|---|---|
| **Product/Surface** | PEC — `DEL-10-02_Kill_test_standing_release_gate` (PEC-K-01 / PEC-SVC-004) |
| **Class** | **Trace gap** |
| **Severity** | **WARN** |
| **Confidence** | **HIGH** |

**Assertion.** PEC's optionality guarantee is well-specified and testable, but the contract that would make it a *standing* gate records that no accepted release path exists to bind it into.

**EvidenceRefs.**
- `projects/pec/docs/PRD.md` **PEC-K-01** *"No governed act may require a PEC read or write. Deleting PEC blocks nothing. The kill test (§12) passes at every release."*; **PEC-SVC-004** *"a standing release gate."*
- `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md` `OUT-002`: *"the gate wiring: the binding that makes OUT-001 a standing release gate rather than a script someone remembers to run … **Whether an accepted release path exists to bind into is not established by any accepted source; CON-002 carries that gap and REQ-010 requires it to be reported rather than papered over.**"*
- The contract is otherwise exemplary: REQ-001 names the three-part property; REQ-002/REQ-003 externalise the workflow set and the blocking test; AC-001 requires a naming failure mode.

**Consequence.** This is the brief's optionality test applied to PEC, and PEC passes it on substance: the fallback owner is explicit (files and Git, D-GOV-01, PEC-K-02), absence is survivable as recorded, and the falsification clause (§11) is armed with a deletion consequence. What is *not* established is the enforcement point — a standing gate with no release path is an assertion, not a gate. Given RB-002 leaves Root's release evidence for the runtime unowned too, the corpus currently has no accepted release path for either the runtime or its optional coordination plane.

**SmallestAction/Owner.** None yet — `CON-002` and `REQ-010` already require this to be *reported* rather than assumed, which is the correct posture pre-P1. Flagged so the owner sees that PEC's optionality guarantee and Root's release-authority gate (PRD §8.3, `DEL-06-07_Release_Authority_Gate`) are two halves of one unbuilt path. Owner: PEC `DEL-10-02` at execution; Root `DEL-06-07` for the release-act half.

---

### RB-013 — App's D-APP-48 SHA-pinned contract mirror is entirely stale, so App's own compatibility mechanism toward the runtime cannot currently verify anything

| Field | Value |
|---|---|
| **Product/Surface** | APP — D-APP-48 pinned harness-contract mirror (`frontend/packages/harness-contract/`) |
| **Class** | **Trace gap** |
| **Severity** | **WARN** |
| **Confidence** | **MEDIUM**; the 12/12 count is **UNKNOWN** to me independently |

**Assertion.** The mechanism by which App verifies that it still matches the harness contracts it pinned is inoperative, at the same moment the semantic owner of those contracts is in dispute (RB-001).

**EvidenceRefs.**
- Manifest §App integration and drift surfaces: *"D-APP-48's 12-file SHA-pinned harness-contract pull is 12/12 stale after the shared-runtime tranche rewrote those files to deprecation shims without repinning"* (conditions App-5, basis-10). **I did not independently verify the 12/12 count or the shim rewrite** — marked **UNKNOWN**.
- What I did verify: the pin target is the intra-App package `frontend/packages/harness-contract/`, and App's own concordance evidence records post-D-APP-48 path refactors into it — e.g. `execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/MANIFESTS/PKG-07_claims.csv` rows DEL-07-04-REQ-009/010: *"the assessment's cited paths … were refactored into the pinned `frontend/packages/harness-contract` package per D-APP-48; behavior unchanged"*; and `PKG-03_NOTES.md` l.67: *"Prior note that `runtime_engine_contract.md` cites pre-D-APP-48 paths was not [re-verified]."*
- `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md` exists as a live seam document (manifest §Runtime/client seams).

**Consequence.** Assessing consequence, not rediscovering the condition: a stale pinned mirror is normally a hygiene defect. Here it is load-bearing, because it is App's *only* declared mechanism for detecting that the runtime contract it consumes has changed. With the mirror stale and with no Root-side compatibility obligation (RB-002), App currently has **no** working detection path for runtime-contract drift — neither its own pin nor a producer-side notice. That is the charter's "compatibility … owned?" question answered *no* from both directions simultaneously.

**SmallestAction/Owner.** Repin or formally retire the D-APP-48 mirror in the same tranche that dispositions RB-001, since the repin target depends on who owns the contract. Owner: `D-APP-*` / App SCOPE_CHANGE.

---

### RB-014 — Root's declared scaling path for governance attribution runs through a product whose permanent non-goals forbid it

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT (`docs/PRD_ROOT.md` §9.2 RD-2 ↔ `projects/pec/docs/PRD.md` §4.2) |
| **Class** | **Semantic conflict** (latent) |
| **Severity** | **WARN** |
| **Confidence** | **HIGH** |

**Assertion.** The Root PRD's ruled evolution path for multi-practitioner attribution names "the PEC interface and a database" as the mechanism; PEC's adopted PRD makes recording adoption, ruling, or direction a permanent non-goal.

**EvidenceRefs.**
- `docs/PRD_ROOT.md` §9.2, owner verbatim: *"A1+B2 could seemingly be scaled up to multi-practitioner using the PEC interface and a database, and attribution can be done more securely that way. If you agree I would go that way. And that database and PEC interface are not current scope."*
- Root's own hedge, same section: *"The referent of 'the PEC interface' is not resolved in this document; it is `TBD` rather than guessed (K-INVENT-1)"*; carried as ledger `SOW-094` (`OUT`) and open issue **OI-009** (`SCOPE_TBD`, `OPEN`), and reconciled against D-GOV-01 as *"mechanism"* vs *"record"*.
- `projects/pec/docs/PRD.md` §4.2: *"**Not a system of record.** Files and Git remain the sole authority (`D-GOV-01`). PEC output is never citable as authority. **Not a ruling surface.** No write path records adoption, ruling, or direction. Rulings are file-native (K-AUTH-1)."*; **PEC-K-02**; **PEC-GAT-004** *"PEC shall provide no write path that records adoption, ruling, or direction."*
- Neither document cites the other on this point. PEC PRD §16's nine open decisions do not include "serve Root governance attribution."

**Consequence.** Severity is WARN, not higher, because Root expressly marks this **not current scope** and `TBD`, and the item is carried `OUT` — so nothing relies on it today. The consequence worth surfacing is the *shape* of the future collision: the RD-2 B/C-stage machinery, if opened as written, would ask PEC to mediate attribution of binding governance records — the one function PEC's invariants permanently exclude. Because the incompatibility lives in two documents that do not reference each other, it would surface only at the moment the scope is opened, i.e. at maximum cost. Root's own D-GOV-01 reconciliation (*"supplies the attribution **mechanism** while the authoritative **record** stays file-native"*) is a plausible reading under which PEC-K-02 survives, but it is Root's reading of PEC's product, recorded in Root's instrument, and PEC has never dispositioned it.

**SmallestAction/Owner.** Add a note to Root open issue **OI-009** / `SOW-094` recording that the referent decision must start from PEC-K-02 and PEC PRD §4.2, so the constraint is inherited rather than rediscovered. The registers are the amendment surface for their data, so this is a note, not a scope change, and creates no commitment. Owner: Root decomposition companion registers.

---

### RB-015 — Root-doctrine change notices reached App and one domain pack but not PEC or Piping, so RB-003/RB-004 have no routed arrival path

| Field | Value |
|---|---|
| **Product/Surface** | CROSS_PRODUCT (change-notice routing under `AGENTS.md` agent-index change-notice rule / Root PRD D-11) |
| **Class** | **Observation** |
| **Severity** | **INFO** |
| **Confidence** | **HIGH** |

**Assertion.** Routed root-doctrine notices are asymmetric: App holds four `D-GOV-*` notices, `domains/chirality` holds three, PEC holds none, Piping holds none.

**EvidenceRefs.** Enumerated at the frozen checkout:
- `projects/chirality-app-dev/execution/_Coordination/`: `NOTICE_D-GOV-21_ROOT_DOCTRINE_AMENDMENT.md`, `NOTICE_D-GOV-23_DIRECTIVE_GENUS_SUPERSESSION.md`, `NOTICE_D-GOV-24_OPERATING_SYSTEM_PROSE_PROPAGATION.md`, `NOTICE_D-GOV-26_SPEC_CONTRACT_AMENDMENTS.md`, plus two HELPS_HUMANS notices.
- `domains/chirality/_Coordination/`: D-GOV-21, D-GOV-23, D-GOV-24 (**no D-GOV-26**).
- `projects/pec/execution/_Coordination/`: `NOTICE_2026-07-25_helps_humans_p1_p7_applied.md`, `NOTICE_2026-07-25_helps_humans_oi013_response.md` — **no `D-GOV-*` notice**.
- Piping: none found.
- Disclosed as manifest conditions Root-13 and basis-13.

**Consequence.** Restated only for its bearing on my lens: PEC is a ruled runtime client (D-T0-23) and a Tier-0 counterparty, and it is the loop with zero routed root-doctrine notices. The change-notice rule exists so that detection *"does not depend on"* downstream drift checks alone (`AGENTS.md`, agent-index change-notice rule). For RB-003 (stale D-T0-23 text) and RB-006 (the `RB-PEC-ADAPTER` row), the routing path that would deliver them to PEC is the one path the corpus shows as unused for that loop. The corrective actions in RB-003/RB-006 already route through it; this finding records why they must.

**SmallestAction/Owner.** Carried by RB-003 and RB-006. Owner: `AGENTS.md` change-notice rule as exercised by the tranche that dispositions those findings.

---

### 2.2 Severity tally

| Severity | Count | IDs |
|---|---:|---|
| **BLOCK** | 2 | RB-001, RB-002 |
| **REVIEW** | 7 | RB-003, RB-004, RB-005, RB-006, RB-007, RB-009, RB-010 |
| **WARN** | 5 | RB-008, RB-011, RB-012, RB-013, RB-014 |
| **INFO** | 1 | RB-015 |
| **Total** | **15** | RB-001 … RB-015, no ID reused |

Severity discipline note: the two BLOCKs are both statements about **the record** — an accepted instrument contradicted (RB-001) and an accepted-basis commitment with no executable coverage anywhere (RB-002). Neither is a claim about running software, and neither is a safety verdict (K-DOMAIN-4; D-GOV-02). Nothing was inflated to BLOCK to attract attention: every other runtime-family finding is REVIEW or below precisely because its consequence is contained or already recorded by its own loop.

---

## 3. M1 — Trace matrix, per product

Disposition vocabulary: `COVERED` / `COVERED_WITH_RECORDED_DEFERRAL` / `TRACE_GAP` / `CONTRADICTED` / `NOT_EXECUTABLE`.

### 3.1 ROOT — 7 objectives + the forward-coverage register's admitted items

I used `chirality_root_prd_coverage_forward_v1_0.csv` as the register directs (84 rows; header + 84 = 85 lines) and verified a sample of rows against the PRD text I read in full.

**Objectives.**

| PRD item | Register status | My disposition | Evidence / note |
|---|---|---|---|
| OBJ-1 | COVERED | **COVERED** | Ledger→DEL-01-01/02/03/07/08, DEL-02-01, DEL-02-05, DEL-04-07, DEL-04-09. Its condition *"no ratified clause has an unrecorded conflicting live variant"* is satisfied because C-1 is **recorded** (§10.2) and carried by DEL-01-01. |
| OBJ-2 | COVERED_WITH_RECORDED_DEFERRAL | **COVERED_WITH_RECORDED_DEFERRAL** | Verified: the situated-working-root half is deferred by owner decision 1 of D-GOV-25, recorded at §12.1 with three-reason rationale and machine-visible in `DeferralReason`. `DEL-03-06` carries the root half. This is the corpus's best example of a gap made visible rather than closed. |
| OBJ-3 | COVERED | **COVERED** | 14 mapped deliverables incl. DEL-05-08 (linkage completeness + pre-registered retrieval sample). |
| OBJ-4 | COVERED | **COVERED, with a recorded risk** | DEL-02-04, DEL-03-01/04/05/06, DEL-05-06, DEL-06-01/07. **Risk:** OBJ-4's condition is *"every root capability consumed by root development was accepted through the basis or an explicitly accepted predecessor"* (falsifier F3). Root development consumes the `runtime/` daemon, which no accepted Root deliverable produced (**RB-002**). F3-observation is `DEL-06-01`'s work; the register cannot see this because runtime is not a scope unit. |
| OBJ-5 | COVERED | **COVERED** | DEL-06-04/05/06/08. |
| OBJ-6 | COVERED | **COVERED** | DEL-03-03, DEL-05-01, DEL-06-02; population bounded to root-product runs by the PRD itself. |
| OBJ-7 | COVERED | **COVERED** | DEL-01-05, DEL-03-01. |

**Admitted major commitments — register population (84 rows), verified sample.** All 84 rows carry `COVERED` except OBJ-2. I verified these rows against PRD text: `N-1` (split SOW-014/015 per DEC-004 — confirmed against §5.1 N-1's domain-engine exception), `N-5` (split SOW-019/020/021 per DEC-005 — confirmed), `O-1` (SOW-026; note the §5.2 six-member enumeration is superseded by the pointer block + `docs/SPEC.md` §0.2.1's eight members — manifest condition Root-10; the ledger's SOW-026 carries only the release-managed/read-mostly clause, so the enumeration divergence is not carried as a scope item, which is consistent with the supersession being an instrument-level fact), `O-2`/`O-10` (SOW-027/035→DEL-02-02 — see below), `D-14` (split SOW-048/049 per DEC-005; OI-005 records the check is unbuilt), `D-15` (§11.2 four-category table, all four `COVERED`, no deferral), `RD-2` (SOW-094 `OUT`, OI-009 `OPEN`), `obl-a/b/c` (§9.1 concordance obligations, carried as standing verification per DEC-009/OI-001), `C-1..C-4`.

| Commitment class | Rows | Disposition | Note |
|---|---:|---|---|
| `N-1`..`N-9` | 9 | **COVERED** | Two splits by maintenance locus. |
| `O-1`..`O-10` | 10 | **COVERED at register granularity; `O-2` is a TRACE_GAP inside the item** | **This is the one place I depart from the register.** `O-2` has three layers with three maintenance loci; unlike N-1/N-5/D-14 it was **not** split, so its third clause (`runtime/`) is covered only by an authority-boundary `REQ_SLICE` with *"no implementation change implied"* and no `runtime/` write locus. F4 is not tripped because objectives and commitments are traced as whole units — the identical mechanism the decomposition itself documents at OI-013 (*"the gap is inside the objective, where the registers cannot see it"*). **→ RB-002.** |
| `D-1`, `D-2`, `D-4`..`D-16` | 15 | **COVERED** | `D-3` deliberately absent and never reassigned — verified. |
| `E-1`..`E-8` | 8 | **COVERED** | |
| Directions (§3 v1 boundary, objective discipline; §4 categories/loop/judgments/non-prescription; §5 registry discipline; §6 ×4; §7 ×2; §8.3 release) | 15 | **COVERED** | |
| Non-goals §8.1 | 1 | **COVERED** | 9 `OUT` ledger items retained and package-assigned (DEC-007). |
| Falsifiers `F1`..`F6` | 6 | **COVERED** | `F3` carries the RB-002 risk noted at OBJ-4. |
| Rulings `RD-1`..`RD-5` | 5 | **COVERED** | |
| Obligations `obl-a/b/c`, `annex-10.1` | 4 | **COVERED** | Standing verification, not re-performance (DEC-009); OI-001 `CLOSED_CONFIRMED`. |
| Conflicts `C-1`..`C-4` | 4 | **COVERED** | C-2/C-3/C-4 remain `HumanRuling = TBD`. |
| `adoption-10.3` | 1 | **COVERED** | |

**Root M1 verdict.** The forward register is internally sound and its single deferral is exemplary. **One disposition differs from the register:** `O-2` reads `COVERED` at item granularity and is a `TRACE_GAP` at clause granularity. That single clause is the whole of RB-002.

### 3.2 APP — 10 objectives + §16/§17-class commitments

| PRD item | My disposition | Evidence |
|---|---|---|
| OBJ-001 Dialogue-centred governed harness | **COVERED** | Decomp §6 → SOW-001–008, 023; PKG-02 deliverables; 5 SOWs present. |
| OBJ-002 Product-owned runtime contracts before adapter default | **CONTRADICTED** | Its scope items (SOW-009–018, 037–040) and PKG-03 assert App ownership of the runtime contract, which App PRD §17 and D-GOV-20 assign to Root. The objective as written cannot both be met and conform. **→ RB-001, RB-005.** |
| OBJ-003 Auditable turns/messages/outcomes/replay | **COVERED** | PKG-05, 5 SOWs. |
| OBJ-004 Provider-adapter architecture, first adapter replaceable | **COVERED** | PKG-04, 5 SOWs; OI-001/OI-006 open and recorded. |
| OBJ-005 Tools only via capability policy + hard-deny precedence | **COVERED** | PKG-06, 6 SOWs. |
| OBJ-006 Filesystem project truth | **COVERED** | PKG-07, 6 SOWs. |
| OBJ-007 Agent-suite integrity + governed delegation | **COVERED** | PKG-08, 5 SOWs; `DEL-08-04` OUT-001 names `delegate_agent`. |
| OBJ-008 Validation/packaging/release/network/key checks | **COVERED** | PKG-09, 6 SOWs. |
| OBJ-009 Professional boundary, product identity, reliance-boundary ownership | **COVERED_WITH_RECORDED_DEFERRAL** | PKG-01, 4 SOWs. Reliance-boundary *ownership* is delivered but is consumer-owned and partly stale — **RB-006**. |
| OBJ-010 Future domain-engine compatibility without absorbing solvers | **COVERED** | PKG-10, 5 SOWs; OI-005 keeps it future-boundary. |

**§16/§17-class commitments.**

| Commitment | Disposition | Evidence |
|---|---|---|
| §16 — v3.2 is the authoritative decomposition (78/10/51/10) | **COVERED** | §10B checklist; counts verified against §5/§7/§8/§10. |
| §16 — *"If this PRD and the active SOFTWARE_DECOMP snapshot disagree … the conflict must be surfaced and resolved through governed PRD/decomposition amendment before scaffold or REVIEW closure"* | **CONTRADICTED** | Such a disagreement exists (PRD §8.16/FR-122–128 + PKG-03 vs PRD §17-dup) and has not been surfaced or resolved through amendment. **→ RB-001.** |
| §16 package→PRD coverage table (10 rows) | **COVERED** | Each row's FR ranges reconcile with §8. |
| §17 (first) Approval and Change Control | **COVERED** | DEC-017 (SCA-APP-001), DEC-018 (002), DEC-019 (003), DEC-020 (004) all recorded with rulings. |
| §17 (second) *Shared Runtime and Local-Agent Pilot Amendment* — root-owned subsystem; per-user daemon; one authenticated Unix-socket API; one canonical SSE protocol; tracked manifests; central lazily-migrating sessions; the `REQUIRED_DELEGATION_MISSING` acceptance path; export eligibility | **NOT_EXECUTABLE** | No App deliverable carries any of it. It appears in the decomposition only as **OI-007** (`SHARED_RUNTIME`, **still open**) and **DEC-019**, and in §13 in a form that contradicts it. **→ RB-001, RB-005.** |
| §2.2 required companion register `contract_invariant_coverage_register.csv` | **TRACE_GAP** | Absent; no deferral ruling found. **→ RB-010.** |
| §15 KG-033 (Woven Dialogue residuals), KG-034 (coordination projection completeness) | **COVERED_WITH_RECORDED_DEFERRAL** | Both carry named residuals and explicit product decisions. |
| PRD duplicate `## 17` numbering | **Observation** | Two distinct sections share the heading number; manifest condition App-2. Consequence: a citation of "PRD §17" is ambiguous, and the ambiguity falls precisely across the runtime-ownership question — the first §17 says the PRD does not supersede the decomposition, the second reassigns runtime ownership. |

### 3.3 PEC — PEC-K-01..11 + PRD v2.1 objectives

| Invariant | Disposition | Evidence |
|---|---|---|
| PEC-K-01 Graceful absence | **COVERED** | C1; SOW-055 → `DEL-10-02` (SOW present, read at body depth). Gate-wiring caveat: **RB-012**. |
| PEC-K-02 Files govern | **COVERED** | C2; SOW-010 → DEL-03-01; SOW-025/066 twinning (DL-8) → DEL-10-03 (SOW present). |
| PEC-K-03 Harness-owned consumption | **COVERED_WITH_RECORDED_DEFERRAL** | C3, carried as constraint per DL-7; OI-011 resolved the polling-moment reading at Gate 2. The **producer half** (daemon polling) is outside PEC and unowned — **RB-007**. |
| PEC-K-04 Staleness is a comparison | **COVERED** | SOW-006 → DEL-04-03 (SOW present). |
| PEC-K-05 Two trust tiers | **COVERED** | SOW-032 → DEL-06-05 (**no SOW; PKG-06 uninitialized, P3**). |
| PEC-K-06 Observation not participation | **COVERED** | SOW-031/067/068 → DEL-06-06 (**no SOW**). |
| PEC-K-07 Ingest best-effort, reconciliation guaranteed | **COVERED** | SOW-038 → DEL-03-05 (**no SOW**; moved P4→P3 at DL-14 *"so ingest never runs without its PEC-K-07 safety invariant"* — good sequencing discipline). SOW-063 intentionally objective-unmapped (DL-14), disclosed. |
| PEC-K-08 Everything derived is explainable | **COVERED** | SOW-023 → DEL-05-01 (**no SOW**); SOW-050 → DEL-09-06 (**no SOW**). |
| PEC-K-09 Declared surface | **COVERED** | SOW-039 → DEL-07-01 (**no SOW**). |
| PEC-K-10 Content-minimal | **COVERED** | SOW-056/073 twinning → DEL-01-03 (SOW present). Contradicted **externally** by the stale `pec.yaml` residency grant — **RB-004**. |
| PEC-K-11 Mode-proportional | **COVERED as constraint** | C15 only; added at DL-9 adversarial verification; no dedicated deliverable, consistent with DL-7. |

| PRD v2.1 objective | Disposition | Evidence |
|---|---|---|
| OBJ-001 sub-second cited orientation (§3.1) | **COVERED** | PKG-02/04/08 + instruments SOW-058/059; 15 of its mapped deliverables have SOWs. |
| OBJ-002 structural staleness (§3.2) | **COVERED** | |
| OBJ-003 declared durable presence surface (§3.3) | **COVERED** | All mapped deliverables are in PKG-06/07/09/10 → **only the PKG-10 instruments have SOWs**; the presence surface itself is uninitialized by design. |
| OBJ-004 one live owner view (§3.4) | **COVERED** | PKG-09 uninitialized; DEL-01-06 SOW present. |
| OBJ-005 deletability without blocking (§3.5) | **COVERED** | DEL-00-01, 01-03, 01-05, 03-01, 03-06, 10-02, 10-03 — all seven have SOWs. **Optionality is the best-contracted property in the corpus.** |
| OBJ-006 measurable and falsifiable thesis (§11) | **COVERED** | DEL-10-01/04/05/09/10/11/12; four have SOWs. |
| Residue: 11 IN items without objective mapping | **COVERED_WITH_RECORDED_DEFERRAL** | §3 mapping notes + §7 metric; SCA-002/DL-17 confines the amendment to wave scope and retains the intentional rationale verbatim. Disclosed and reasoned. |

**PEC M1 verdict.** No trace gap found. PEC is the only product whose decomposition records what it *cannot* decide (nine §16 TBD items as first-class scope), refuses to pre-decide them (intake posture 3), and prices the resulting risk (§8 OI-coupled MEDIUM). Its exposure is entirely on the producer side of boundaries it does not own.

---

## 4. M2 — Cross-product ownership matrix

Each cell is evidenced or marked **UNKNOWN**. "Semantic owner" = who may change the meaning; "accepted record" = the instrument that fixes it.

| Shared function | Semantic owner | Accepted record | Producers | Consumers | Fallback / degraded behaviour | Compatibility obligation | Routed change path |
|---|---|---|---|---|---|---|---|
| **Runtime protocol / daemon** | **DISPUTED** — D-GOV-20 §1–2 + CONTRACT §1.13 K-RUNTIME-1 + App PRD §17-dup say **Root**; App decomp §13 l.611 says App retains semantic ownership (**RB-001**) | D-GOV-20; K-RUNTIME-1/K-CONTROL-1; D-T0-23 | **NONE in any accepted decomposition** (**RB-002**). `runtime/packages/*` exists with no owning deliverable | App (`frontend/src/lib/runtime-client/*`, `frontend/electron/runtime-host.ts`); PEC (`DEL-07-05`, no SOW); CLI | **UNDECLARED.** No instrument states what a client does when the daemon is absent or version-skewed | **UNOWNED.** No Root compatibility deliverable; App's own pin mechanism (D-APP-48) is stale (**RB-013**) | **UNDECLARED.** `runtime/` is outside SPEC §0.2.1's instruction surface, so not even the M2 gate applies |
| **Sessions** | **Root daemon** | K-RUNTIME-1; K-STORE-2 (*"Central runtime sessions remain JSON/JSONL and import legacy project-local sessions lazily and non-destructively"*); D-GOV-20 §5 | No Root deliverable; App `DEL-05-01/05-02` produce the App-side canonical session layout | App PKG-05; PEC presence tier (`PEC-PRS-001`: *"session identity and lifecycle remain daemon-owned"*) | App keeps `.chirality/sessions/<id>/events.jsonl` as its own audit mirror (FR-121) — a genuine, recorded fallback | K-STORE-2 states non-destructive lazy import; **no deliverable owns proving it** | App SCOPE_CHANGE for the App half; **none for the daemon half** |
| **Credentials** | **Root daemon** (exclusive) | D-GOV-20 §2–3; K-RUNTIME-1 | **NONE** | App (Electron `safeStorage`, PRD §7.7/FR-034-class); PEC (`SOW-080`/OI-006 undecided) | App PRD §7.7 acceptance: *"If secure storage is unavailable, UI reports an error"* — a declared degraded mode on the App side only | **UNKNOWN** — no instrument states the credential-boundary compatibility obligation between daemon and clients | **UNDECLARED** |
| **Delegation** | **Root** as authority contract (D-GOV-20 §7–8; `AGENTS.md` §Delegation and Entry Rules); **daemon** as transport | D-GOV-11/12/13; K-SEAL-1, K-GHOST-1; `AGENTS.md` | App `DEL-08-04` (`delegate_agent` admission bridge), `DEL-08-05` (child run records) | App; PEC hierarchy edges (`DEL-06-04`, no SOW) | `AGENTS.md`: *"If no executable child mechanism is available, defer the multi-agent stage or continue only genuinely single-agent work"* — **explicit, well-owned degraded mode** | `AGENTS.md` names both the app harness (`delegate_agent`) and a project's native facility as conforming | Root `AGENTS.md` (M2) for the contract; App SCOPE_CHANGE for the bridge |
| **Instruction surface** | **Root** | `docs/SPEC.md` §0.2.1 (8 members, ruled by D-GOV-26/27); Root PRD O-1 as superseded | Root `DEL-02-01` (membership + release management) | All working roots; App packages it (`DEL-08-01`, `DEL-09-04`) | Working roots MAY overlay, MUST NOT weaken (`docs/CONTRACT.md` §1; K-AGENTS-1) | Explicit non-weakening rule + integrity verification in packaged builds | M2 tranche + routed notices (D-11) — **the best-owned function in the matrix** |
| **SOW method layer** | **Root** | `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (D-GOV-16); `skills/scope-of-work/`; `tools/scope_of_work/`; `tools/validation/validate_decomposition_registers.py` | Root | Root (45), App (53), PEC (32) | Not applicable | **Version-skew is disclosed and unmanaged**: PEC validated under current method, Root under pre-v6/v6.1 (manifest §4; basis condition 15). No compatibility statement binds the two eras | M2 tranche on the standard. **Gap:** no interface/consumer element exists (**RB-008**) |
| **Coordination / PEC** | **PEC** | `projects/pec/docs/PRD.md` v2.1 (D-PEC-58/61); PEC-K-01..11 | PEC (32 of 64 deliverables contracted) | Harnesses on behalf of agents (PEC-K-03); human owner | **Best-declared fallback in the corpus**: PEC-K-01 graceful absence; kill test PEC-SVC-004; §11 falsification clause with deletion consequence; *"every consumer has a file-native fallback"* | PEC parity-diffs against the practitioner harness permanently (PEC-RCN-005) | PEC SCOPE_CHANGE (SCA-001/002 precedent). **But** its Tier-0 description (D-T0-23) and its domain profile are stale (**RB-003, RB-004**) |
| **Reusable work surface** | **NO OWNER — the concept does not exist in any governed record** | **NONE** | — | — | — | — | — |
| | *Evidence:* a corpus scan for `reusable work surface` / `work surface` across `docs/`, all three PRDs and all three decompositions returns only unrelated senses: `docs/SPEC.md` l.258 (`_STATUS.md ## Remaining` as *"the sole deliverable-local executable work surface"*), `docs/TYPES.md` l.307 (same), PEC PRD l.60 (*"the live lawful work surface"*, prose). The charter's App dual-identity framing is **clarified framing**, so per §05 its absence is a **concordance question, not a gap**. | | | | | | |
| **Domain-truth boundary** | **Domain engines** | K-DOMAIN-1..4 (`docs/CONTRACT.md` §1.12) + the D-GOV-01 scope note exempting engine-owned stores; Root PRD N-1 exception (stated in-body deliberately, *"because the annex is never adopted"*) | Root `DEL-06-05_Domain_Engine_Truth_Boundary`; App PKG-10 (5 SOWs, future-boundary) | Root, App, PEC | Domain engines own authoritative truth; Chirality *"governs the work around the engine … is not the solver"* | K-DOMAIN-2 write-quarantine; K-DOMAIN-3 OperationProposal + human acceptance; K-DOMAIN-4 green ≠ certification | DOMAIN_ENGINE profiles + Tier-0. **Well-owned in doctrine; one live profile is stale (RB-004)** |
| **Evidence conventions** | **Root** | Root PRD E-1..E-8; `docs/SPEC.md` §9.8; `AGENTS.md` snapshot/handoff/closure rules; K-SNAP-1 | Root PKG-05 (8 deliverables, all with SOWs) | All loops | E-7 closure rule: files written ≠ closed | Derivative-package rule requires citing accepted upstream snapshots | M2 + Root SCOPE_CHANGE |
| **Export / release** | **Root** | K-EXPORT-1; `exports/chirality-app/export_public.py` (allowlist includes `runtime`, l.41/127); D-GOV-20 §10 | Root `DEL-04-07_Public_Export_Boundary_Conformance` | App (public repo snapshot); PEC (excluded as private adapter) | Profile *"fails on forbidden paths or leaks"* (Root PRD D-10) | D-GOV-20 gates export on *"the app-dev and PEC vertical slices"* — **an obligation with no owning deliverable** (RB-002) | M2 on the profile. Root PRD **C-4** records `README.md` omits `runtime/` while the profile includes it — `HumanRuling = TBD` |
| **Resource governance** | **N/A — absent by design** | **NONE** | — | — | — | — | — |
| | *Evidence:* a corpus scan for `resource governance` across `docs/`, `execution/_Decomposition/`, and all three products' `docs/` returns **zero** matches. The manifest is explicit (consulted-only context; basis condition 19): *"not accepted Root, App, or PEC scope, a source of authority, a system of record, or a correctness dependency."* Per charter §05, **candidate architecture — absence is not a gap.** I raise no finding. | | | | | | |

**Matrix reading.** Of twelve shared functions, four are cleanly owned end-to-end (instruction surface, evidence conventions, domain-truth boundary, delegation-as-contract). Two are correctly absent (reusable work surface, resource governance). One is well-owned but externally misdescribed (coordination/PEC). **Five runtime-family rows — protocol/daemon, sessions, credentials, export gating, and the compatibility obligation cutting across them — have no producer, no declared fallback, and no routed change path.** They are the same gap seen from five angles.

---

## 5. M3 — The charter's 13 review questions

Each answered from governed records, with a disposition. Charter propositions are treated as challenge material, never evidence.

**Q1 — Root: Shared runtime ownership.** *Does one Root package own runtime protocol, daemon, clients, sessions, tools, delegation, credentials, adapters, compatibility, security, migration, and release evidence?*
**Answer: NO. Disposition: FAILS — accepted-basis conformance finding.** `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers` is named for the runtime layers but owns, across five deliverables, only: instruction-surface membership, the three-layer *authority boundary*, delegation doctrine, write-scope controls, and registry discipline. `DEL-02-02` — the sole runtime-bearing deliverable — is a `REQ_SLICE` whose register note reads *"no implementation change implied"*. No deliverable, and no `AnticipatedWriteLocus` in the 45-row register, names `runtime/`. Of the enumerated list, **zero** of protocol, daemon, clients, sessions, credentials, adapters, compatibility, security, migration, or release evidence has a Root owner; tools and delegation are owned but as instruction-surface doctrine, not runtime implementation. **→ RB-002.** The charter's §03 callout (*"Root runtime ownership is not optional … The Root decomposition must assign its contract and continuing conformance work to a Root package and deliverables"*) is **correct as a diagnosis but wrong about the routing**: the Root PRD does *not* already carry the commitment in a form decomposition could execute. `O-2(c)` is an authority-boundary clause, not a production commitment. Fixing it in the decomposition would be inventing scope, which D-9 and the charter both forbid — hence RB-002's PRD-first sequence.

**Q2 — Cross-product: Producer, consumer, and fallback.** *For every shared function, are the semantic owner, consuming products, accepted basis, fallback, and routed-change obligations explicit?*
**Answer: For 6 of 12, yes; for 5 runtime-family functions, no; 1 is disputed. Disposition: PARTIAL — see M2.** The explicit ones are genuinely explicit (instruction surface, evidence conventions, domain-truth boundary, delegation contract, coordination/PEC, SOW method layer). The runtime family lacks producers and fallbacks entirely. **→ RB-001, RB-002, RB-006, RB-007.** Structural cause: the executable contract layer has no element in which a producer/consumer relation can be written (**RB-008**).

**Q3 — Root: Four-category coverage without folder mimicry.**
**Answer: YES — and this is done well. Disposition: PASSES.** Root decomposition §11.2 shows all four §4.1 categories `COVERED` with **no deferral**, spread across 4–6 packages each (normative basis 41 scope items / 6 packages / 21 deliverables; operative 26/5/18; developmental 59/5/25; evidence 18/4/16). DEC-003 records the deliberate refusal to partition by category, citing PRD §4.3's express prohibition; §8's *"Why six and not four"* demonstrates non-identity. D-12 is honoured directly — developmental machinery is decomposed as product scope (PKG-04, 10 deliverables), not exempted as overhead. **No folder mimicry.** The one caveat is that category *coverage* is computed from the same scope ledger that under-represents `runtime/` (Q1), so "operative product COVERED" is true of the operative product as the PRD defines it, not of the operative product as it exists on disk.

**Q4 — Cross-product: Application composition boundary.** *Does the corpus provide a lawful home for reusable work-surface and application-integration contracts, or reveal a genuine PRD gap that decomposition may not invent?*
**Answer: It reveals a genuine PRD gap — and the corpus is right not to have invented one. Disposition: HELD OPEN (see §6).** No governed record contains the concept of a reusable work surface (M2, evidenced by corpus scan). Application-integration contracts exist only in fragments: `chirality.project.json` + K-PROJECT-1 (registration identity), the App runtime-client seams, PEC's `DEL-07-05` client seam. The charter's *application environment profile* is **candidate architecture**; per §05 its absence is **not** a gap and I raise no finding. What *is* a finding is narrower and different: the fragments that exist have no owner (RB-002, RB-007). The charter's own instruction applies exactly — *"Look for an application-integration home; do not force one topology from the metaphor."* There is no home; there is also no accepted requirement for one.

**Q5 — App: Standalone product and reusable work surface.**
**Answer: The standalone half is coherent; the reusable half is not instantiated anywhere. Disposition: CONCORDANCE QUESTION ONLY — no failure asserted.** App PRD §2/§3.1/§6.1 describe a coherent standalone desktop product with a concrete release target (macOS 15+ arm64 unsigned DMG), and the decomposition's ten packages partition it cleanly. Nothing in App's PRD, decomposition, or 53 contracts describes an embedded, companion, or sidecar reuse of its human–agent surface. The charter's dual-identity framing is **clarified framing**; §05 forbids failing a product for not instantiating it, and I do not. The concordance question for the owner: App PRD principle 26 (*"Dialogue is the primary collaboration workspace"*), FR-001's Woven Dialogue shell, and `DEL-02-01`'s explicit boundary (*"Shell integration owns presentation only"*) are all written as product-internal. If reuse is intended, App's current presentation/evidence separation is a good foundation, but the intent exists in no instrument.

**Q6 — App: Faithful human/agent mediation.**
**Answer: YES, with strong evidence. Disposition: PASSES.** The PRD separates UI and runtime authority repeatedly and checkably: principle 15 (*"Separate UI events from runtime events"*), principle 28 (*"Coordination is projection, not authority"*), principle 30 (*"Replay is observational"*); FR-008 (a recorded-session selection *"does not resume, switch, merge with, or mutate the primary session"*); FR-009 (every work item shows source class, status basis, currency); non-goals §3.2 forbidding the Coordination Panel from creating/approving plans, inferring parentage, transitioning lifecycle, or authenticating a human act. Prerequisites/authority/state/provenance/interruption/recovery/errors/outcomes each have named FRs (FR-087–FR-095, FR-101–FR-102, FR-120) and owning deliverables (`DEL-06-01`, `DEL-08-04/05`, `DEL-05-04`). Neither surface bypasses governance: hard-deny precedence (FR-089) overrides *"persona, session, operator, or adapter permission-mode allow decision"* and even developer bypass. **This is the App's strongest area.**

**Q7 — App ↔ Root: Runtime client, not runtime authority.**
**Answer: NO — App's accepted decomposition and its contracts retain runtime authority. Disposition: FAILS.** `PKG-03` is named *"Runtime Engine Contract and Turn Lifecycle"*; `SOW-037` reads *"Define product-owned `AgentEnginePort` / `RuntimeEngineContract`"*; `DEL-03-01` delivers it as an `API_CONTRACT`; and §13 l.611 asserts App *"retain[s] semantic ownership."* App's PRD §17-dup says the opposite. The corpus therefore contains both the correct posture and its negation, in the same product, with no supersession. **→ RB-001, RB-005.** Mitigating and worth recording: App's PRD is otherwise scrupulous about not claiming authority it lacks (§17 first: *"This PRD is a product requirements artifact. It does not supersede DIRECTIVE/SPEC/TYPES/CONTRACT [or] active decomposition and scope-change records"*), and the reliance-boundary register's `RB-DAEMON` row states the correct rule (*"GUI, route, CLI, or PEC sidecar may not construct a second engine/session loop"*). The failure is a propagation failure, not a posture failure.

**Q8 — PEC: Coordination without authority.**
**Answer: YES, emphatically, in PEC's own instruments. Disposition: PASSES — with an external contradiction not of PEC's making.** PRD §4.2 makes system-of-record, ruling-surface, orchestrator, lock-manager, harness-replacement, and Git-actor **permanent** non-goals; PEC-K-02 (never citable as authority), PEC-K-06 (*"conflicts surfaced, never prevented"*), PEC-K-08 (Explain-shaped, *"Drill-down never dead-ends"*), PEC-GAT-004 (no ruling write path). The decomposition operationalises this with the IN/OUT twinning convention (DL-8): each permanent boundary stays `OUT` as the boundary record while a separate IN item states the *verified* obligation — `SOW-025 ↔ SOW-066`, `SOW-056 ↔ SOW-073` — producing `DEL-10-03_No_ruling_write_verification` as a tested property. Rebuildability: PEC-RCN-001 one-command rebuild → `DEL-03-01`. File-fallback safety: PEC-K-01 + `DEL-10-02`. **The one authority-bearing PEC surface in the corpus is not PEC's**: the ADOPTED `pec.yaml` profile still grants an L3 operation-proposal lane and a provider-egressing residency basis (**RB-004**), and Tier-0 still describes the retired adapter service (**RB-003**).

**Q9 — PEC ↔ environment: Complexity-dependent availability.**
**Answer: YES. Disposition: PASSES.** The modes ladder (PRD §5) is explicitly proportional — Pipeline and unscoped Conversation are *"zero-contact"*; PEC is *"essential for throughput (not for soundness — file fallback remains)"* only at concurrent Agent 0s. PEC-K-11 makes this an invariant, carried as constraint C15. Identities are declared: PRD §8 access classes owner/harness/admin; PEC-K-09 *"Every coordination message is durable and attributable; no ephemeral relay."* Graceful absence is not merely asserted but has an executable gate (`DEL-10-02`) whose contract refuses to assume a release path exists (**RB-012**). **Degraded-mode test per brief item 8:** fallback owner = files and Git under D-GOV-01; absence survivable = yes, as recorded — PEC-K-01, the §11 falsification clause (*"PEC is deleted and, by PEC-K-01, nothing breaks"*), and `DEL-10-02`'s named-failure requirement. **No silent mandatory coupling found**: I checked whether any Root or App instrument requires a PEC read/write, and found none — App's `RB-PEC-ADAPTER` row governs a PEC *adapter*, not a PEC dependency, and Root's only PEC reference is the `OUT`-scoped RD-2 evolution path (**RB-014**).

**Q10 — Resource governance ↔ environment: Optional planning and resource service.**
**Answer: Absent from the corpus entirely. Disposition: NO FINDING — candidate architecture; absence is not a gap.** Corpus scan for `resource governance` across `docs/`, `execution/_Decomposition/`, and all three products' `docs/` returns zero matches. The manifest states it is *"candidate program architecture described only by the charter … not accepted Root, App, or PEC scope, a source of authority, a system of record, or a correctness dependency"* (basis condition 19). Per charter §05 I may return an evidence-linked proposal only where the candidate would resolve a demonstrated problem, and must not count absence as a gap. **I demonstrate no such problem and propose nothing.** For the owner's benefit, one observation: the charter's own ownership table requires that resource governance never gain *"authority to … freeze work"*, and the corpus already contains a well-formed precedent for exactly that constraint — PEC's advisory-blocker posture (*"Blocker state is visibility, not work authority"*, manifest §PEC; PEC-K-06). If the candidate is ever opened, that precedent, not a new mechanism, is the nearest accepted pattern. **Decision criteria** are recorded in §6.

**Q11 — All: Human judgment remains the hinge.**
**Answer: YES across all three products. Disposition: PASSES.** Root: K-AUTH-1/K-AUTH-2/K-GATE-1; PRD §4.2's three non-collapsible judgments (evaluation / iteration / release) with *"None is delegated to machinery"*; D-GOV-02's observation boundary (*"BLOCK never means globally proven safe or unsafe"*); D-GOV-17 (*"a validator finding may never mechanically reject content the owner has ruled — where ruled text trips a validator, the validator is defective"*); §8.3 release as a separately human-gated act. App: principle 4; non-goals forbidding autonomous approval records; FR-120 (`canUseTool` persists the decision *before* returning allow/deny); lifecycle approval-SHA gates. PEC: PEC-GAT-002 verdicts *"advisory only"*; PEC-GAT-004 no ruling write path; blockers as visibility. **Contrary evidence considered and rejected:** the two candidate counter-examples are (a) `pec.yaml`'s ADOPTED status conferring a live grant (**RB-004**) and (b) App PKG-00's self-minted scope namespace (**RB-009**). Both are surfaces acquiring *procedural* force without a current human ruling — which is why both are findings — but neither substitutes for an acceptance, reliance, or release judgment. The hinge holds.

**Q12 — All: Domain truth remains situated.**
**Answer: YES in doctrine and in scope; one live profile is stale. Disposition: PASSES with RB-004.** K-DOMAIN-1..4 are unambiguous and Root PRD N-1 deliberately carries the domain-engine exception in-body *"because the annex is never adopted"* — a small but telling instance of the corpus refusing to let a derivative package hold a load-bearing clause. Root `DEL-06-05_Domain_Engine_Truth_Boundary` owns the boundary; App PKG-10's five deliverables are all future-boundary with `OI-005` holding them there, and App non-goals forbid becoming a solver and forbid agents writing protected domain paths; PEC retires its own domain-engine lane (§13). No product absorbs protected domain state, deterministic domain acts, or professional authority. The exception is `pec.yaml`, which still declares an operation-proposal contract and an agent-visible residency surface (**RB-004**) — a stale grant, not an absorption.

**Q13 — Deliverable SOW: Executable and warranted scope.**
**Answer: Substantially yes for Root and PEC; yes-with-two-exceptions for App. Disposition: PARTIAL.**
- *Traces to accepted product scope:* Root 45/45 pin `Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8…` and carry non-empty `project_scope_refs`/`package_objective_refs` (verified across the sample; frontmatter verified on all 45 via the mechanical pass). PEC 32/32 pin `SOFTWARE_DECOMP.md@3623b958b…`. App **51/53** pin the v3.2 decomposition; **2 pin a package README** (**RB-009**).
- *One primary owner:* `ResponsibleParty` is `Ryan Tufts` across Root (assigned by the D-GOV-27 tranche) and `TBD` across App/PEC pending WORKING_ITEMS activation — a declared, not accidental, state (PEC decomposition §5; App DEC-013(c)).
- *Names interfaces:* **NO, structurally** — the standard has no such element (**RB-008**).
- *Names evidence:* **YES** — the Output and Evaluation Matrix with its `Evidence expectation` column is required (§5) and present in every contract I read.
- *Fits its context envelope:* Root S=14/M=30/L=1/XL=0; App S=9/M=40/L=2/XL=0; PEC S=28/M=34/L=2/XL=0. **No XL anywhere**, and both PEC `L` items carry mandatory envelope notes with named split lines.
- *Avoids introducing new product commitments through implementation prose:* **Root is exemplary** — every sampled contract carries an explicit write-locus gate (*"This Scope of Work grants no such authorization"*) and marks every `AC-*`/`VER-*` a candidate. **PEC is exemplary** — `DEL-00-03` REQ-007 requires the SPEC seed to *"leave every open owner decision open"* and AC-008 verifies the open-issue register is unchanged after publication; `DEL-08-01` REQ-006 requires the auth mechanism to sit behind a seam *"so that a later OI-006 ruling reworks the auth half without reworking the socket-and-access-class core"*, explicitly *"it does not choose a mechanism."* **App has one exception**: `DEL-03-01` carries a runtime-ownership commitment that its own PRD §17 reassigns (**RB-005**).
- *Machine-opaque candidate status (Root):* manifest condition Root-8/basis-6 — confirmed in my sample; candidate status is expressed in varied prose (*"is a candidate authored under MODE=INIT"*, *"are candidate criteria"*, *"candidates for owner review"*) with no metadata field. Consequence for my lens: a deterministic fan-in cannot distinguish accepted from candidate acceptance criteria across 45 contracts, so REVIEW's checklist compilation depends on prose parsing. This bears on Q13's warrant question and is recorded here rather than as a separate finding, since Reviewer A's lens owns acceptance-status discipline.

---

## 6. Held-open questions

The charter names six intentionally-open questions. For each: what the basis says, what it cannot decide, and the criteria a decision would turn on. **I close none by preference.**

**H1 — Whether the reusable work surface is a Root requirement, an App capability, or both under different ownership.**
*Basis says:* nothing. The concept appears in no governed record (M2, corpus scan). Root PRD §7.1 establishes one instruction root serving many working roots *"without per-workspace instruction drift"* and permits overlay/specialization but not weakening — a downward-service model that is *about instructions*, not about a UI surface. App PRD's surface is described entirely as product-internal.
*Cannot decide:* whether the owner intends reuse at all. The manifest states App UI/API semantic-parity work *"has not yet been established through a repository instrument"* (App condition 1, basis condition 18).
*Decision criteria:* (i) does a second consumer exist or is one planned (Piping is the only situated-product exemplar, and it is consulted-only)? (ii) if reused, does the surface export presentation assumptions — App's `DEL-02-01` note (*"Shell integration owns presentation only; work, hierarchy, transcript, and artifact facts remain governed by their existing semantic owners"*) suggests the separation needed already exists; (iii) ownership follows the answer to Q1: if Root owns the runtime contract, a Root-owned surface contract is coherent; if it does not, a Root-owned surface would be a second unowned function.

**H2 — The exact authority and schema of an application environment profile.**
*Basis says:* fragments with real authority already exist — `chirality.project.json` under **K-PROJECT-1** (*"stable identity and relative authority references only … Authority-affecting manifest drift disables adapters until explicit re-registration"*) and `_DomainEngines/profiles/*.yaml` under D-GOV-06/D-GOV-07.
*Cannot decide:* whether these compose into one profile, and at what authority level. The charter's profile is **candidate**; absence is not a gap.
*Decision criteria:* (i) **RB-004 is the cautionary datum** — the corpus already has a profile whose adopted status outran its product, so any new profile class must specify its supersession trigger *before* adoption, not after; (ii) whether a profile *grants* or merely *declares* — K-PROJECT-1 declares, `pec.yaml` grants, and only the granting kind creates the RB-004 failure mode; (iii) whether it would resolve a demonstrated problem — RB-007's unowned event-contract home is the nearest live candidate.

**H3 — When PEC is available, recommended, or required by complexity.**
*Basis says:* the modes ladder (PRD §5) already answers "recommended" with unusual precision — a six-row table keyed to concurrent coordination contexts, ending at *"essential for throughput (not for soundness)"*. PEC-K-11 makes proportionality an invariant. **"Required" is answered permanently and negatively** by PEC-K-01.
*Cannot decide:* the threshold at which the owner *should* run it, which the PRD deliberately leaves to measurement — §11 metric 4 (harness poll adoption) and the §11 falsification clause are the instruments.
*Decision criteria:* the PRD supplies them: measured Step-0 cost delta (metric 1, baselined pre-P1 by `DEL-10-01`), collision incidents (metric 3), and poll adoption (metric 4). **This question is better instrumented than any other held-open item and needs no reviewer input.** One doctrinal residue is genuinely open and PEC flags it: *"Whether concurrent Agent 0 operation without a common parent is lawful is an open `AGENTS.md` question"* (§15), carried as `SOW-086` `OUT` (*"Deferred, not permanent … owner act on the root doctrine surface"*). That is a Root doctrine decision, not a PEC one.

**H4 — The product home, service contract, lock/freeze authority boundary, and fallback behaviour of optional resource governance.**
*Basis says:* nothing (Q10). **Absence is not a gap.**
*Cannot decide:* everything about it.
*Decision criteria*, stated so alternatives are preserved rather than closed: (i) **the freeze question is the load-bearing one** — the charter's own ownership table forbids authority to *"freeze work"*, and the corpus's only accepted pattern for a service that surfaces pressure without exercising it is PEC's advisory-blocker posture (*"visibility, not work authority"*) plus PEC-K-06 (*"conflicts surfaced, never prevented"*); (ii) **the fallback question is answerable in advance** — PEC-K-01 plus the executable kill test is a complete, transferable template for an optional service, and any resource-governance proposal that cannot state its own kill test has not met the standard the corpus already applies to optional services; (iii) **the home question depends on RB-002** — a new optional service should not be placed until the runtime family it would consume events from has an owner; (iv) budgets and cost attribution touch financial commitment, which App non-goals already exclude (*"Conduct financial transactions or binding commitments"*), so a scope statement would need to say explicitly that forecasting is not authorizing.

**H5 — Logical composition versus physical bundling and update cadence.**
*Basis says:* the corpus has already chosen *logical composition with physical co-location* in one case and left it undeclared: `runtime/` is a root workspace consumed by App through `frontend/electron/runtime-host.ts` and `frontend/src/lib/runtime-client/*`, with D-GOV-20 §3 requiring the *"packaged Electron application supplies daemon mode so the existing app identity and encrypted safeStorage credential boundary remain single-owner"* — i.e. one binary, two logical owners. K-CONTROL-1 fixes the transport (Unix socket, no TCP). K-EXPORT-1 makes the generic runtime separately exportable, which is a composition signal.
*Cannot decide:* update cadence — nothing states whether a runtime protocol change forces an App release, and **nothing can, while RB-002 leaves the compatibility obligation unowned.**
*Decision criteria:* (i) whether a protocol version exists as a declared artifact (today: `@chirality/runtime-contracts` exists as a package but no instrument declares it the versioned contract); (ii) whether clients can be version-skewed from the daemon at all — K-RUNTIME-1's singleton rule constrains this but does not answer it; (iii) **this question is not decidable before RB-002**, and I record that dependency rather than guessing.

**H6 — Which cross-client conformance proofs are release requirements.**
*Basis says:* D-GOV-20 §Implementation gates is the closest thing to an answer — *"Public export occurs only after the app-dev and PEC vertical slices pass"*, with *"Daemon/client/CLI, Desktop migration, PEC migration, security review, and regression review remain separately bounded."* K-RUNTIME-1's enforcement column names *"client conformance"*. App FR-123 requires an adapter to pass engine conformance tests *"before becoming the default production path"*.
*Cannot decide:* which of these are **release** requirements versus development gates, because **no accepted release path exists** — PEC's `DEL-10-02` records exactly this (`CON-002`: *"Whether an accepted release path exists to bind into is not established by any accepted source"*), and Root's release authority is a `PROPOSED` PRD commitment (§8.3) whose deliverable (`DEL-06-07_Release_Authority_Gate`) is unexecuted.
*Decision criteria:* (i) define the release act first — Root PRD §8.3 already insists release is a *distinct* judgment from iteration, so the gate list should be derived from it, not from CI convenience; (ii) D-GOV-20's five separately-bounded items are the natural candidate list and already carry owner ruling; (iii) whoever owns the runtime contract (RB-002) should own the conformance suite, otherwise the proof and the thing proved have different owners — which is today's condition (App owns `DEL-03-01`'s conformance suite for a contract App does not own).

---

## 7. Summary for fan-in

Ranked by what I consider consequential enough for owner judgment.

**1. RB-001 (BLOCK) — Two accepted instruments name different semantic owners of the shared runtime.** App's accepted decomposition states at §13 l.611 that *"Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership."* D-GOV-20, `CONTRACT` §1.13 K-RUNTIME-1, App's own PRD §17, and Tier-0 D-T0-23 all say Root owns it. Both are live at the frozen basis; neither is marked superseded. This is the single sentence most likely to cause a wrong build. **Smallest act: an App SCOPE_CHANGE amending that sentence to the client-integration/conformance formulation the rest of the corpus already uses, with a routed notice to Tier-0 and PEC.**

**2. RB-002 (BLOCK) — `runtime/` has no owner anywhere in accepted Root scope.** Seven packages of executable code, ruled Root-owned, consumed by two products, governed by seven `K-*` invariants — and covered by exactly one `REQ_SLICE` marked *"no implementation change implied"*, with no deliverable, no `runtime/` write locus, and no M2 gate (it is outside SPEC §0.2.1's instruction surface). Root's F4 closes because the PRD clause is thin, not because the work is covered — the same register blindness the corpus already documented at OI-013. **This is a PRD gap and must not be fixed in decomposition. Smallest act: a Root PRD amendment adding one operative runtime-ownership commitment, then a Root SCOPE_CHANGE splitting SOW-027 by maintenance locus.** An explicit recorded deferral in the forward register is an acceptable interim and would at least make the gap machine-visible.

**3. RB-005 (REVIEW) — the App contract layer never received the rehoming.** One of 53 App contracts mentions the daemon; `DEL-03-01` still delivers *"a product-owned AgentEnginePort / RuntimeEngineContract."* Because contracts are what executors and REVIEW actually read, the corpus's only executable instruction to build a runtime contract currently sits in the consumer product.

**4. RB-003 + RB-004 (REVIEW, paired) — the PEC description of record is stale in two places PEC does not own.** Tier-0 D-T0-23 (ruled 07-22) still preserves the deterministic adapter service, RBAC, and scratch/demo fence that PEC PRD v2.1 (adopted 07-24) retired; `_DomainEngines/profiles/pec.yaml` remains ADOPTED at L3 with an `OPEN_ENUMERATED`, provider-egressing residency grant that PEC-K-10 forbids. **The profile is the urgent half** — it is a live grant, not documentation lag, and D-GOV-06 is direct precedent that this class requires an owner ruling rather than agent normalization. PEC has already recorded the obligation (`SOW-090`) but with a trigger later than the harm.

**5. RB-007 (REVIEW) — the event-contract home and the daemon global event feed have a named closing act with no addressee.** PEC fenced itself out correctly (*"writes into root `runtime/` are outside PEC's fences"*) and named the act as a *"§16 ruling (cross-loop)"* — but §16 is PEC's own list and PEC cannot rule on `runtime/`. **Smallest act: a Tier-0 coupling row, on the D-T0-19 precedent.**

**6. RB-006 (REVIEW) — the only runtime reliance-boundary register is consumer-owned and its PEC row is stale.** `RB-PEC-ADAPTER` asserts a P0 boundary — PEC adapter RBAC, scratch/demo fence — that PEC retired. It has never been routed to PEC, which holds zero root-doctrine notices (RB-015).

**7. RB-009 (REVIEW) — App PKG-00 pins a package README as `decomposition_basis` and mints its own `CONTROL-*` scope namespace.** Bounded and self-aware (graph-excluded; forbidden from mutating product registers), but the bound is asserted by the artifacts themselves. `DEL-00-02` now reports its SCC closed, so a retirement disposition may be the smallest act available.

**8. RB-010 (REVIEW) — App's required invariant-coverage register is absent with no deferral,** leaving the engine/runtime invariant families with family-prose ownership only — and §10A.1's family table does not reach the `§1.13` framework invariants at all, so the family most affected by the rehoming is the one the coverage surface does not cover.

**9. RB-008 (WARN) — the ratified SOW standard has no interface or consumer element.** This is the mechanism behind items 1, 2, 3, 5 and 6: because no contract can declare a counterparty, no deterministic check can detect a producer obligation with no producer. An *optional* `interfaces:`/`consumers:` block would make the whole class checkable without invalidating 130 existing contracts.

**Two things worth recording positively, because a review that only reports defects misdescribes this corpus.** PEC's decomposition is the strongest artifact I read: it records nine owner decisions it refuses to pre-decide, twins every permanent boundary with a verified obligation (DL-8), prices the resulting risk (§8 OI-coupled MEDIUM), corrects itself through two rounds of adversarial verification with the defects named in the log (DL-9, DL-14), and its contracts actively verify that open issues remain open after publication (`DEL-00-03` AC-008). And Root's OBJ-2 deferral (§12.1, D-GOV-25 decision 1) is a model of the distinction the whole system depends on — a gap made machine-visible in the register rather than closed by prose. **Both are the pattern the runtime family lacks.**

**Coverage limitation to carry into fan-in.** PEC PKG-05/06/07/09 have no ScopeOfWork contracts (deliberate P2–P4 sequencing, manifest condition PEC-2), so the PEC half of the runtime seam could not be reviewed at contract depth by anyone at this basis. I ran no validators and relied on no validator PASS; where the manifest records one, I cite it as a manifest-recorded result under its stated tool era and draw no conformance conclusion from it.
