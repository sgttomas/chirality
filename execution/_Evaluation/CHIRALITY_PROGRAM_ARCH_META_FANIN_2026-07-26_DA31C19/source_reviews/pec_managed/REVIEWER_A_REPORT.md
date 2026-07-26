# REVIEWER A — PASS-1 REPORT

**Reviewer:** A
**Lens:** vertical — authority, intent, traceability (status and provenance; PRD commitment → objective → scope item → package → deliverable → SOW trace; human gates; non-goals; falsifiers; accepted-versus-proposed discipline; stable IDs; preservation of owner intent)
**Basis commit:** `da31c19b5656dd74615e308c4215688971d33dc9` (frozen checkout `/Users/ryan/dev/chirality-review-frozen-da31c19`, detached; verified by `git rev-parse HEAD`)
**Charter:** `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`, sha256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f` — **verified at the frozen checkout and read in full before any other review action.**
**Common basis manifest:** `/Users/ryan/dev/chirality-tandem-review-2026-07-26/FROZEN_BASIS_MANIFEST.md` — read second.
**Date:** 2026-07-26
**Primary checkout `/Users/ryan/dev/chirality` was not read.**

---

## 0. Read and sample disclosure

### 0.1 Identity verification performed before reliance

Every manifest sha256 prefix I relied on was recomputed at the frozen checkout. **All six verified:**

| File | Manifest prefix | Recomputed | Result |
|---|---|---|---|
| `docs/PRD_ROOT.md` | `82f7ea2944e7` | `82f7ea2944e7…` | MATCH |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `14067a7d97c9` | `14067a7d97c9…` | MATCH |
| `projects/chirality-app-dev/docs/PRD.md` | `ef638f43ccae` | `ef638f43ccae…` | MATCH |
| `…/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `952d3cbf81b0` | `952d3cbf81b0…` | MATCH |
| `projects/pec/docs/PRD.md` | `de0a969cad15` | `de0a969cad15…` | MATCH |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `3e5be4e453ed` | `3e5be4e453ed…` | MATCH |

Manifest headline counts independently recomputed and confirmed: Root 6 packages / 45 deliverables / 103 scope items / 7 objectives / **45 live ScopeOfWork.md**; App 78 scope items / 10 packages / 51 decomposition deliverables / 10 objectives / **53 live ScopeOfWork.md**; PEC 11 packages / 64 deliverables / 94 scope-ledger rows / **32 live ScopeOfWork.md**. **I found no manifest error.** One apparent discrepancy I raised mid-review (43 vs 45 Root SOWs) was my own filter defect, corrected before it entered this register; it is recorded here for honesty, not as a finding.

### 0.2 Read in full

- Charter (1,449 lines) — complete, including all 13 review questions in the lens grid.
- `docs/PRD_ROOT.md` — complete (1,055 lines).
- `projects/chirality-app-dev/docs/PRD.md` — complete (1,720 lines).
- `projects/pec/docs/PRD.md` — complete (490 lines).
- `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` — complete (615 lines).
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` — complete (662 lines).
- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` — complete for §1–§4, §5 SSOW, §6–§7, §9 scope ledger, §10/§10A/§10B, §11–§13; §8 deliverable tables read as parsed rows (all 51) rather than as prose.
- **All registers, in full, by row:** Root `chirality_root_scope_ledger_v1_0.csv` (103), `…deliverable_register…` (45), `…objective_register…` (7), `…prd_coverage_forward…` (84), `…trace_reverse…` (51); PEC `ScopeLedger.csv` (94), `Deliverables.csv` (64).
- Supporting governed records: `docs/SPEC.md` §0.2.1; `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md`; `D-GOV-26_owner_gated_closeout.md`; `D-GOV-27_initialization_closing_rulings.md`; `runtime/README.md`; `AGENTS.md`; `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (structure).

### 0.3 ScopeOfWork sample — exact and disclosed

The brief requires ≥1/3 of each product's SOW contracts with every package represented, plus every SOW the trace matrix flags.

**Two reading modes were used, and I distinguish them:**
- **(F) Full read** — entire file.
- **(N) Normative read** — frontmatter plus every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, `AX-*`, `CON-*`, `TBD-*` statement and the complete Output-and-Evaluation Matrix, extracted deterministically. This is the contract's normative content; the CLM blockquote document-kit restatements were not read line-by-line in mode N.

| Product | Sampled | Threshold | Packages covered | Contracts |
|---|---|---|---|---|
| **Root** | 16 / 45 (36%) | ≥15 | 6 / 6 | DEL-01-01 (N), DEL-01-02 (F), DEL-01-04 (N), DEL-01-08 (N), DEL-02-01 (F), DEL-02-02 (N), DEL-02-04 (N), DEL-03-04 (N), DEL-03-05 (N), DEL-03-06 (N), DEL-04-08 (N), DEL-04-09 (N), DEL-05-05 (N), DEL-05-08 (N), DEL-06-04 (N), DEL-06-07 (N) |
| **App** | 19 / 53 (36%) | ≥18 | 11 / 11 dirs | DEL-00-01 (F), DEL-00-02 (N), DEL-01-01 (N), DEL-01-02 (N), DEL-01-04 (N), DEL-02-01 (N), DEL-02-02 (N), DEL-02-04 (N), DEL-03-01 (N+`_STATUS` F), DEL-03-02 (N), DEL-03-04 (N), DEL-04-01 (N), DEL-04-02 (N), **DEL-06-02 (F)**, DEL-06-03 (N), DEL-07-01 (N), DEL-08-02 (N), DEL-08-03 (N), DEL-09-02 (N) |
| **PEC** | 11 / 32 (34%) | ≥11 | 7 / 7 with SOWs | DEL-00-01 (N), DEL-00-03 (F), DEL-01-01 (N), DEL-02-03 (N), DEL-03-01 (N), DEL-04-03 (N), DEL-08-01 (F), DEL-08-02 (F), DEL-10-01 (N), DEL-10-02 (N), DEL-10-10 (N) |

Every contract flagged by my trace matrices is in the sample (App DEL-06-02/06-03 for SOW-064; the six dangling-pin contracts DEL-02-01/02-02/02-04/05-04/08-02/08-03 — five read, DEL-05-04 covered by frontmatter-only inspection; Root DEL-02-01 for O-1; PEC DEL-08-01/08-02/00-03 for the recorded residuals).

**Machine-checked across 100% of contracts** (all 130): frontmatter `decomposition_basis`, `project_scope_refs`, `package_objective_refs`, `schema`; AC/VER counts; presence of `HUMAN_REVIEW`, `CON-*`, and candidate-status wording; `_STATUS.md` `Current State`.

### 0.4 What the sample cannot establish

- Whether the un-sampled ~64% of contracts contain defects **inside prose I did not read in mode N** (document-kit CLM blockquote bodies, guidance/trade-off narrative). All *structural and normative* properties I assert are machine-checked at 100%.
- Whether any contract's stated requirements are *technically adequate* to satisfy its PRD commitment — that is an engineering-fitness judgment outside a documentary review and outside my lens.
- Whether the `runtime/` code in the tree conforms to D-GOV-20. I read `runtime/README.md` only; I ran no build, test, or validator.
- Nothing about **execution quality** of any deliverable: all Root and PEC contracts are `INITIALIZED` and all App contracts are `IN_PROGRESS`; **none is ISSUED**, so no issuance judgment is under review.

### 0.5 Tool basis (charter §5 / manifest §4 version-skew condition)

**I ran no repo script and relied on no validator PASS.** Every quantitative claim in this report was produced by provably read-only computation I performed myself — `shasum`, `git cat-file`/`rev-parse`/`show`/`rev-list` (read-only plumbing), `grep`, `awk`, and `python3` over `csv`/`re` reading files on stdin. Where the corpus records a historical validator result I cite it as a recorded result and name its era: **Root's 45 SOWs passed before the v6/v6.1 QA-item-20 harmonization; PEC's 32 were repaired and validated under the current method** (manifest §4). I therefore make **no claim that any Root SOW would pass the current tool**, and I treat no such rerun as evidence. App's SOW validation era is **UNKNOWN** — the manifest states eras for Root and PEC only, and I found no App record fixing one, though all three products declare the same `chirality-deliverable-sow/v1` schema (verified across all 130 contracts).

### 0.6 Method discipline applied

I oriented from the governed records first and used the charter only afterward to challenge my own account. Charter propositions are treated by their declared status: **accepted basis** → conformance findings; **clarified framing** → concordance questions only; **candidate architecture** (including resource governance) → proposals only, absence never a gap; **open design questions** → alternatives preserved. The manifest's 20 disclosed conditions are assessed for **consequence** and cited by number; I do not present rediscovery of a disclosed condition as a new finding.

---

## 1. Findings register

### 1.1 Declared observation boundary (stated once, governs every severity below)

My observation boundary is **the documentary and register layer of the frozen corpus at `da31c19b`**: PRDs, decompositions and their companion registers, ScopeOfWork contracts and `_STATUS.md` files, the decision records and coordination surfaces I cite, and git object existence/identity. Within that boundary:

- **BLOCK** — the accepted basis is contradicted, or an accepted-basis pointer is unresolvable, such that unsafe reliance could follow if the artefact were relied on as it stands.
- **REVIEW** — needs an owner or governed-workflow disposition; the corpus cannot settle it and proceeding without a ruling risks divergence.
- **WARN** — a defect with contained consequence, correctable inside an existing instrument.
- **INFO** — observation, including positive verification results.

**Outside my boundary** (never a basis for any severity here): code correctness, runtime behaviour, engineering adequacy, test results, and anything requiring execution. A BLOCK here is a **documentary** BLOCK; it is not a statement that any system is unsafe, and per D-GOV-02 it is bounded to this declared boundary and is never a global verdict.

---

### RA-001 — BLOCK

- **FindingID:** RA-001
- **Product/Surface:** APP — `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-05-04`, `DEL-08-02`, `DEL-08-03` ScopeOfWork contracts
- **Assertion:** Six App ScopeOfWork contracts declare `decomposition_basis: …@416b29033bbacb0bc3648d84033272b7ab4e6e11`, and that object does not exist in the repository, so the accepted basis those six contracts bind themselves to cannot be resolved or verified.
- **EvidenceRefs:**
  - `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation/ScopeOfWork.md` line 5 (and the same field in the other five contracts).
  - `git cat-file -e 416b29033bbacb0bc3648d84033272b7ab4e6e11` → **fails** ("DOES NOT EXIST"); `git cat-file -t` → `fatal: git cat-file: could not get object info`.
  - Not a shallow clone (`git rev-parse --is-shallow-repository` → `false`; 127,064 packed objects; 84 refs), so absence is not a fetch artefact.
  - A *different* object, `416b290334049762fe0b0c2a43df373c8da230ab`, shares only the first 9 hex characters — a prefix coincidence, not the pinned SHA.
  - The other four App pins (`0724f26f6`, `2770fda4c`, `b4d2c9ab2`, `ff59428ff`) all resolve to commits, so the failure is specific.
- **Class:** trace gap (authority-chain break)
- **Severity:** **BLOCK**
- **Consequence:** K-AUTH-2 binds approval to a specific SHA. These six contracts assert a basis that no one — human or tool — can retrieve, so their declared provenance is unfalsifiable and their conformance to the accepted decomposition cannot be checked at all. The affected set is not random: it is almost exactly the deliverables SCA-APP-004 rescoped (Woven Dialogue shell, coordination/Workbench/Pipeline UX, toolkit state, replay, routing, dispatch). Anyone reconstructing what these contracts were written against, or re-reviewing them after a further amendment, has no anchor. Mitigating: five of the six carry an explicit `## SCA-APP-004 Gate-5 Current Contract (Controlling)` section, so their *content* was updated even though the pin was not — the defect is in the basis pointer, not evident content abandonment.
- **SmallestAction/Owner:** Re-pin the six `decomposition_basis` fields to a resolvable commit that actually contains the intended decomposition state, in one bounded correction tranche. Owner: the App loop's CHANGE/closeout workflow under `projects/chirality-app-dev/execution/_Coordination/`; no PRD or decomposition amendment is required, because nothing about scope changes.
- **Confidence:** **HIGH** (deterministic; object existence tested four ways).

---

### RA-002 — REVIEW

- **FindingID:** RA-002
- **Product/Surface:** CROSS_PRODUCT (ROOT primary)
- **Assertion:** D-GOV-20 rules the executable agent runtime a **root-owned `runtime/` workspace**, yet the accepted Root decomposition assigns no package, deliverable, or scope item to it — 0 of 103 scope items and 0 of 45 deliverables reference daemon, credentials, residency, turn locks, engine adapters, or socket protocol — while the continuing runtime-conformance work is carried in an **App** deliverable's open-work list.
- **EvidenceRefs:**
  - `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` §Ruled architecture items 1–2: "Chirality's executable agent harness becomes a root-owned `runtime/` workspace…"; "One opt-in per-user headless daemon exclusively owns runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency." Status RULED, 2026-07-22.
  - `runtime/README.md`: "The daemon is the sole owner of engines, credentials, sessions, delegation, turn locks, interruption, tools, and local-model residency" — the subsystem exists in the tree with six packages.
  - `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`: regex over all 103 `ScopeItemStatement` values for `daemon|credential|residency|turn lock|engine adapter|socket` → **0 matches**.
  - `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`: same regex over all fields of all 45 rows → 2 incidental hits on the word "session" only (`DEL-01-01`, `DEL-04-05`); no runtime ownership.
  - Root's only runtime coverage is `SOW-027` (PRD §5.2 O-2) → `DEL-02-02_Three_Layer_Authority_Boundary_Conformance`, a *boundary conformance* slice, and `docs/PRD_ROOT.md` §5.2 O-2(c) states only that the substrate's "transport never grants project authority" and its user-data state "is operational, not project truth."
  - `projects/chirality-app-dev/execution/PKG-03_.../DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/_STATUS.md` §Remaining: "Promote provider-neutral runtime contracts to root `runtime/`, preserve the deprecated app import path for one cycle, and expand conformance for daemon/client/project/residency behavior (gated: serialized core integration owner)."
  - Root decomposition DEC-001 explains the mechanism: `docs/PRD_ROOT.md` is the **sole** scope source and D-GOV-* rulings are "interpretive context" generating no scope (§2.3).
- **Class:** ownership gap
- **Severity:** **REVIEW**
- **Consequence:** This is not an F4 failure — F4 tests PRD items, and the decomposition covers O-2 faithfully. The gap is between an accepted **governance ruling** and the accepted **decomposition**: a ruled, existing, credential-holding Root subsystem has no Root deliverable, hence no Root acceptance evidence, conformance obligation, compatibility/migration obligation, or release-evidence obligation. Because the only unit actually carrying the work is an App deliverable, the practical owner of Root's runtime conformance is currently the App loop — precisely the "must not become … an App-owned implementation detail" boundary the charter's ownership table names, and the condition the charter's callout anticipates. Reliance risk: a reader taking the Root decomposition as the complete statement of Root product work would conclude Root does not own the runtime.
- **SmallestAction/Owner:** Owner decision on which of two lawful routes applies, then execute only that one: **(a)** a Root PRD amendment adding a runtime-ownership commitment (D-13/D-16 route — an M2 instruction-surface tranche), after which a SCOPE_CHANGE extends the decomposition; or **(b)** an explicit recorded deferral, on the OI-013/§12.1 pattern already used for OBJ-2, stating that runtime ownership is deliberately outside the v1 Root decomposition and naming where it is carried meanwhile. **Not** a decomposition edit alone — D-9 forbids decomposition inventing scope, and the charter forbids smuggling architecture through decomposition prose.
- **Confidence:** **HIGH** on the register facts (exhaustive, deterministic). **MEDIUM** on characterising it as a gap rather than a deliberate sequencing choice: the corpus records no reasoned deferral for runtime ownership, but **UNKNOWN** whether one was intended — the basis cannot decide this, which is why it routes to the owner.

---

### RA-003 — REVIEW

- **FindingID:** RA-003
- **Product/Surface:** APP — `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §13 Downstream Execution Notes
- **Assertion:** The App decomposition asserts in prose that root `runtime/` ownership "is an implementation-location change" and that "app-dev deliverables retain semantic ownership," which conflicts with D-GOV-20's ruling and with App's own PRD §17 amendment; the assertion exists only in decomposition prose and in no accepted instrument.
- **EvidenceRefs:**
  - `…/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §13, line 611: "Shared runtime promotion preserves this decomposition's existing package/deliverable topology. Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership and acceptance evidence through the SCA-APP-003 impact map."
  - Against: `projects/chirality-app-dev/docs/PRD.md` §17 (second §17, lines 1692–1706): "D-GOV-20, D-APP-73, and SCA-APP-003 make the provider-neutral runtime **a root-owned product subsystem rather than a frontend-owned singleton**. A per-user daemon … **exclusively owns** engines, encrypted credentials, sessions, tools, delegation, turn locks, interruption, and local-model residency."
  - Against: `D-GOV-20` §Ruled architecture items 1–2 (quoted at RA-002).
  - Partially mitigating: App decomposition §11 OI-007 (`SHARED_RUNTIME`) records the promotion as an open issue over SOW-009–011, 037, 043, 046, 063, 072, and directs "prove one runtime owner … before export."
- **Class:** semantic conflict (ownership)
- **Severity:** **REVIEW**
- **Consequence:** "Semantic ownership" is the exact term the charter's ownership test turns on, and here the App decomposition claims it for app-dev deliverables over a subsystem an accepted ruling assigns to Root. A charitable reading — that app-dev *deliverables* remain the accountable units for work they already did, not that App owns the runtime contract — is available and is probably what was meant. But the sentence as written is the only decomposition-level statement of runtime semantic ownership anywhere in the corpus, it points the wrong way, and combined with RA-002's Root-side silence it is the only thing a reader would find. Left standing, it is the mechanism by which a temporary migration arrangement becomes permanent divided ownership.
- **SmallestAction/Owner:** One-sentence clarification in App decomposition §13 distinguishing *deliverable accountability and acceptance evidence* (app-dev retains) from *runtime semantic ownership* (Root, per D-GOV-20), cross-referencing OI-007. Owner: App SCOPE_CHANGE (an editorial clarification within OI-007's existing scope, not new scope).
- **Confidence:** **HIGH** that the texts conflict as written; **MEDIUM** that a substantive ownership claim rather than loose drafting was intended.

---

### RA-004 — REVIEW

- **FindingID:** RA-004
- **Product/Surface:** APP — scope item `SOW-064`
- **Assertion:** `SOW-064` ("MCP extension boundaries" — catalog MCP tools and extension boundaries, collision prevention required) is an IN-scope item that no App ScopeOfWork contract executes, although the accepted decomposition's ledger maps it to two deliverables and its telemetry asserts zero unmapped scope items.
- **EvidenceRefs:**
  - `…SOFTWARE_DECOMP_v3_2.md` §9 line 448: `| SOW-064 | IN | MCP extension boundaries. | REF-006 Section 8.15 | PKG-06 | DEL-06-02, DEL-06-03 | OBJ-005 | DEC-005 | FALSE | |`
  - §8 deliverable tables: `DEL-06-02` `CoversScopeItems` = `SOW-047, SOW-049, SOW-050` (line 331); `DEL-06-03` = `SOW-048, SOW-050` (line 332). **Neither lists SOW-064.**
  - `DEL-06-02/ScopeOfWork.md` line 6: `project_scope_refs: [SOW-047, SOW-049, SOW-050]` (read in full).
  - `grep -l "SOW-064"` across all 53 App ScopeOfWork contracts → **no match**.
  - §10 telemetry line 477: `ScopeItemsWithoutDeliverableMapping | 0`; §10B acceptance check: "Every scope item has … at least one mapped deliverable."
  - Upstream commitment: PRD FR-064 (P1), FR-103/FR-105, and runtime phase **R6 — Extensibility and MCP Boundaries** (tool catalog, `mcp__chirality__*` naming convention, collision prevention).
- **Class:** trace gap
- **Severity:** **REVIEW**
- **Consequence:** A PRD-derived scope item with an accepted objective mapping (OBJ-005) has no executing contract, so no deliverable will produce the MCP tool catalog or collision-prevention evidence R6 requires — while the decomposition's own coverage telemetry and acceptance checklist certify full coverage. The certification is what makes this consequential: a reviewer relying on §10/§10B would not look. The defect is asymmetric — the ledger direction (§9) claims coverage the deliverable direction (§8) does not carry, and the executable layer follows §8.
- **SmallestAction/Owner:** Add `SOW-064` to `DEL-06-02` and/or `DEL-06-03`'s `CoversScopeItems` in §8 and to the corresponding contract `project_scope_refs`, or record a reasoned deferral for R6-class scope. Owner: App SCOPE_CHANGE (this is register repair within accepted scope, not new scope — SOW-064 is already IN and already objective-mapped).
- **Confidence:** **HIGH** (deterministic, verified in both directions and at the executable layer).

---

### RA-005 — REVIEW

- **FindingID:** RA-005
- **Product/Surface:** APP — `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §8 vs §9
- **Assertion:** The App decomposition's §9 scope ledger and §8 deliverable tables disagree about coverage for seven scope items, and because App maintains **no companion register file**, the decomposition's two internal surfaces are the only machine truth and nothing arbitrates between them.
- **EvidenceRefs:** Bidirectional comparison of all 78 ledger rows against all 51 §8 rows:

  | Scope item | §9 ledger says | §8 tables say | Direction |
  |---|---|---|---|
  | SOW-002 | DEL-07-01 | DEL-02-03, DEL-07-01 | §8 adds (ledger Notes explain: "UI touchpoint covered by DEL-02-03") |
  | SOW-023 | DEL-02-05, DEL-09-06 | DEL-09-06 | ledger adds |
  | **SOW-064** | DEL-06-02, DEL-06-03 | **(none)** | ledger adds — see RA-004 |
  | SOW-075 | DEL-01-01, DEL-07-01 | DEL-01-01 | ledger adds |
  | SOW-076 | DEL-01-04, DEL-04-02 | DEL-01-04 | ledger adds |
  | SOW-077 | DEL-01-04, DEL-07-06 | DEL-01-04 | ledger adds |
  | SOW-078 | DEL-01-04, DEL-09-04 | DEL-01-04 | ledger adds |

  Contrast — the same test run against the products that maintain authoritative CSVs: **Root 0 mismatches** across 103 ledger rows vs 45 register rows; **PEC 0 mismatches** across 94 vs 64. Directory listing confirms `projects/chirality-app-dev/execution/_Decomposition/` contains exactly one file.
- **Class:** semantic conflict (register integrity)
- **Severity:** **REVIEW**
- **Consequence:** DEC-011/DEC-015 planned a companion register precisely because "invariant coverage is machine-truth heavy and better handled as a companion surface than as prose"; without it, the coverage claim in §10 is only as good as hand-maintained markdown, and it is demonstrably not consistent. Six of the seven are benign (coverage survives via the other deliverable), but the seventh is RA-004. The structural point is that App has no mechanism that would have caught it, whereas Root and PEC do — and both come out clean.
- **SmallestAction/Owner:** Reconcile the seven rows in one editorial pass and record which surface is authoritative for assignment fields (PEC's DL-15 is a usable precedent: "Any conflict resolves to the register for assignment fields and to this document for statement text"). Owner: App SCOPE_CHANGE. The separate question of creating `contract_invariant_coverage_register.csv` is manifest condition 9 and is dispositioned at RA-014.
- **Confidence:** **HIGH**

---

### RA-006 — REVIEW

- **FindingID:** RA-006
- **Product/Surface:** ROOT — `DEL-02-01_Instruction_Surface_Membership_and_Release_Management/ScopeOfWork.md`
- **Assertion:** `DEL-02-01`'s `CON-001` presents instruction-surface membership as an unresolved six-versus-seven conflict between the PRD and the deliverable's own `_CONTEXT.md`, omits `CLAUDE.md` from both enumerations, and declares settlement "an owner act" — when D-GOV-26/D-GOV-27 have already ruled the authoritative enumeration at **eight** members in `docs/SPEC.md` §0.2.1.
- **EvidenceRefs:**
  - `execution/PKG-02_.../DEL-02-01_.../ScopeOfWork.md` `CLM-002`: "The adopted PRD item O-1 enumerates the shared instruction surface as `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and `init/`." (six)
  - Same file `CON-001`: "Unresolved membership conflict: the adopted PRD item O-1 enumerates six instruction-surface members (`CLM-002`), while this deliverable's `_CONTEXT.md` write-locus note enumerates the same six plus `.github/workflows/`. The two authorized sources disagree on membership. This conflict is surfaced, not resolved here; it is exactly the question `OUT-001` exists to settle, and **settling it is an owner act**."
  - Same file `AC-001` requires the register to record `CON-001` "as an open membership question rather than silently adopting either enumeration."
  - Against — `docs/SPEC.md` §0.2.1 (line 44): the instruction surface is "`AGENTS.md`, `CLAUDE.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`" — **eight members**.
  - Against — `D-GOV-26_owner_gated_closeout.md` lines 35–48: `CLAUDE.md` added to the guarded set; the enumeration "lives at `docs/SPEC.md` §0.2.1"; "From this tranche's effect onward, changes to `CLAUDE.md` and `.github/workflows/` are M2 instruction-surface tranches **by doctrine**, not only by guard behavior."
  - Against — `docs/PRD_ROOT.md` pointer block lines 15–24, "Amendment of record (D-GOV-27)": O-1's enumeration is "**superseded by instrument**," authoritative enumeration is SPEC §0.2.1 with eight members.
  - Manifest conditions **10** and **2** disclose the pointer/instrument mechanism and SHA-role terminology; this finding assesses their **consequence** at the executable layer.
- **Class:** authority conflict
- **Severity:** **REVIEW**
- **Consequence:** The contract that exists specifically to settle instruction-surface membership is working from a superseded enumeration and from the wrong pair of sources. It treats the deliverable's own `_CONTEXT.md` as one of "two authorized sources" while never citing SPEC §0.2.1 or D-GOV-26/27, and it omits `CLAUDE.md` — the file that imports `AGENTS.md` into every session — from every enumeration it considers. If executed as written, `OUT-001` would produce a membership register of at most seven entries and `AC-001` would certify a ruled question as open. That inverts the supersession the PRD's own pointer block records, and it is F6-adjacent (a settled status being carried as unsettled). This is the sharpest demonstration in the corpus that "superseded only through the pointer/instrument mechanism" (condition 10) does not reliably reach the executable layer.
- **SmallestAction/Owner:** Amend `DEL-02-01`'s `CLM-002`/`CON-001` to cite `docs/SPEC.md` §0.2.1 and D-GOV-26/D-GOV-27 as the governing enumeration (eight members) and re-scope `CON-001` to whatever genuinely remains open — at most, propagating the ruled enumeration back into PRD O-1's body, which D-13 forbids doing by edit. Owner: Root deliverable remediation under the Root loop; no new instrument is needed because the ruling already exists.
- **Confidence:** **HIGH**

---

### RA-007 — REVIEW

- **FindingID:** RA-007
- **Product/Surface:** APP — all 53 ScopeOfWork contracts
- **Assertion:** App's deliverable acceptance criteria do not test deliverable fitness against product commitments; 48 of 53 contracts carry exactly one `AC-*` and one `VER-*`, at least 13 state acceptance as document-conversion fidelity, and **0 of 53** name a human acceptance gate inside the contract — against 41 of 45 (Root) and 28 of 32 (PEC).
- **EvidenceRefs:** Measured across 100% of contracts in each product:

  | Metric | ROOT (45) | APP (53) | PEC (32) |
  |---|---|---|---|
  | mean `AC-*` per contract | 3.3 | **1.1** | 12.3 |
  | mean `VER-*` per contract | 2.3 | **1.1** | 10.9 |
  | contracts with exactly 1 AC | 0 | **48** | 0 |
  | contracts naming a `HUMAN_REVIEW` gate | 41 | **0** | 28 |
  | contracts declaring a `CON-*` conflict | 14 | **0** | 31 |
  | contracts whose AC is conversion/preservation-shaped | 0 | **13** | 0 |

  Representative App AC text: `DEL-01-01` AC-001 — "The converted contract preserves all legacy source content and traceability to SOW-074, SOW-075, and OBJ-009 **without changing lifecycle or dependency state**"; `DEL-02-02` AC-001 — identical wording with different IDs; `DEL-01-04` AC-001 — "Preservation and traceability … are demonstrated **without adding scope, reliance claims, lifecycle meaning, or obligations**."
  Contrast, Root `DEL-01-02` AC-001: "OUT-001 contains exactly one row per `K-*` invariant defined in the catalog, contains no `K-*` identifier absent from the catalog, and every row carries either a named enforcement point or an explicit `TBD`."
  **Counter-evidence I weighed:** App locates its human gate and open work elsewhere and does so with real rigour — `projects/chirality-app-dev/execution/PKG-03_.../DEL-03-01/_STATUS.md` carries `Authorization Basis: D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8…`, `Checking Approval SHA: 8c6d55d3e8…`, a `## Remaining` list (present in 53/53 `_STATUS.md`), and a human-attributed transition history marked `(HUMAN)` citing owner rulings. PRD FR-054 and F-APP-4 fence `CHECKING`→`ISSUED` on approval-SHA evidence.
- **Class:** omission
- **Severity:** **REVIEW**
- **Consequence:** Because acceptance is stated as "the document was converted faithfully," a deliverable can satisfy `AC-001`/`VER-001` in full while the product commitment behind it remains unmet — the criterion is satisfied by the SOW's own existence, not by the deliverable. The lifecycle gate does exist and is properly evidenced, but at `CHECKING`/`ISSUED` the approver has **no per-requirement acceptance statement to check against**: fitness rests on a prose `Remaining` list that is not traced to FR/NFR IDs or to AC IDs. That is the charter's SOW question ("Does each SOW … name interfaces and evidence") failing on the acceptance half, and it weakens — without removing — the human hinge, because the human is asked to approve without a checkable contract. It is also the clearest instance where the shared SOW method layer produced materially different rigour in different loops.
- **SmallestAction/Owner:** For the P0 reliance-boundary deliverables first (`DEL-01-02`, `DEL-03-01`, `DEL-06-01`, `DEL-06-04`, `DEL-09-02`), replace conversion-fidelity ACs with per-output acceptance criteria traced to the FR/NFR IDs the decomposition already maps, and add a `HUMAN_REVIEW` row to the Output and Evaluation Matrix on the Root/PEC pattern. Owner: App deliverable remediation, sequenced by WORKING_ITEMS; no PRD or decomposition amendment is required because the requirement IDs already exist.
- **Confidence:** **HIGH** on the measurements (100% census). **MEDIUM** on severity: this may be a deliberate, recorded consequence of the D-APP-54 lifecycle rebaseline and the legacy-conversion route rather than a defect, and the corpus does not say — which is why it routes to the owner rather than being asserted as a failure.

---

### RA-008 — REVIEW

- **FindingID:** RA-008
- **Product/Surface:** APP — all 51 decomposition-derived ScopeOfWork contracts
- **Assertion:** No App ScopeOfWork contract pins a decomposition basis later than 2026-07-13, so all 51 predate the two most recent accepted scope changes (SCA-APP-003, 2026-07-22; SCA-APP-004, 2026-07-23), and the contracts collectively pin **five different** basis commits rather than one accepted basis.
- **EvidenceRefs:**
  - Census of `decomposition_basis` across all 53 contracts: `0724f26f6…` ×10 (+×2 for PKG-00), `2770fda4c…` ×6, `416b29033…` ×6 (unresolvable — RA-001), `b4d2c9ab2…` ×15, `ff59428ff…` ×14.
  - Commit dates: `2770fda4c` 2026-07-12; `0724f26f6` 2026-07-13; `b4d2c9ab2` 2026-07-13; `ff59428ff` 2026-07-13.
  - At **every** resolvable pin the decomposition blob is `680b7e8a1e0f7da05d2f93f03a1e306cd7c59dfb`; the blob at `da31c19b` is `b3af4ed677659aa1dd478bba3857c7e1817dd3ab`. The pinned content is therefore uniformly superseded.
  - Decomposition Change Log records SCA-APP-003 landing 2026-07-22 and SCA-APP-004 landing 2026-07-23 — both after the newest pin.
  - **Contrast:** Root — all 45 pin one commit, `653fabc9b3e8…` (the D-GOV-25 EffectiveSHA and stated SOW basis). PEC — all 32 pin one commit, `3623b958b`, at which the decomposition blob is `8aab8caa74…`, **identical to the blob at `da31c19b`**. PEC is the only product whose SOW basis is current.
  - Mitigating: SCA-APP-004 is `GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING`, and five affected contracts carry an explicit `## SCA-APP-004 Gate-5 Current Contract (Controlling)` section, so content propagation is partly done.
- **Class:** trace gap (basis currency)
- **Severity:** **REVIEW**
- **Consequence:** There is no single answer to "what decomposition state is the App SOW layer accepted against." Five answers exist, one is unresolvable, and all are superseded. Because the two missing amendments are exactly the ones that changed the target UI architecture and moved the runtime to Root, the SOW layer's declared basis is stale in precisely the areas under most active change — including the area of RA-002/RA-003. Re-review after any further amendment cannot mechanically determine which contracts need rerunning.
- **SmallestAction/Owner:** As part of closing SCA-APP-004's pending implementation, re-pin all 51 contracts to one post-SCA-APP-004 commit and record that commit as *the* App SOW basis, on the Root/PEC single-pin pattern. Owner: App loop closeout under SCA-APP-004's existing pointer; no new instrument needed.
- **Confidence:** **HIGH**

---

### RA-009 — WARN

- **FindingID:** RA-009
- **Product/Surface:** APP — six materialized deliverable directories
- **Assertion:** Six App deliverable folder labels still carry pre-SCA-APP-004 names, diverging from the accepted v3.2 deliverable names, so the `DEL-XX-YY_{DelLabel}` identity in the filesystem no longer matches decomposition truth.
- **EvidenceRefs:** Comparison of all 51 §8 names against materialized folder labels:

  | ID | Accepted v3.2 name | Materialized folder label |
  |---|---|---|
  | DEL-02-01 | Woven Dialogue Shell and Compatibility Navigation | `Desktop_Shell_and_Matrix_Navigation` |
  | DEL-02-02 | Work/Agents Coordination, Workbench, and Pipeline UX | `Workbench_and_Pipeline_Selection_UX` |
  | DEL-02-04 | Dialogue Toolkit, Context, and Local UI State | `Toolkit_Options_and_Local_UI_State` |
  | DEL-04-01 | First-Adapter Probe and Version-Pinned Adoption Decision | `SDK_Probe_and_Version_Pinned_Adoption_Decision` |
  | DEL-05-04 | Runtime Replay, Dialogue, and Agent Transcript Projection | `Runtime_Replay_and_Transcript_View` |
  | DEL-08-02 | Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract | `Persona_Alias_and_Agent_Matrix_Routing_Contract` |

  Also: `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/` retains the pre-SCA-APP-004 package label against v3.2's "Woven Dialogue Shell, Navigation, and Operator State". Remaining 45 labels match. **Numeric IDs are stable throughout** — I found no renumbering, and SCA-APP-004 expressly preserved topology (DEC-020).
- **Class:** observation (identifier drift)
- **Severity:** **WARN**
- **Consequence:** Contained: `DEL-XX-YY` numeric identity is intact and every contract resolves, so no trace is broken. But `docs/SPEC.md` makes the label part of the canonical folder name, and four of the six labels still name the *superseded* architecture ("Matrix", "Desktop Shell", "SDK") that SCA-APP-004 and SCA-APP-001 replaced. A reader navigating the filesystem sees the old product; the same six overlap heavily with RA-001 and RA-008.
- **SmallestAction/Owner:** Either rename the six folders in the same tranche that re-pins them (RA-008), or record a deliberate decision that materialized labels are frozen at creation and only IDs are canonical. Owner: App loop closeout; label changes need no scope amendment since topology and IDs are unchanged.
- **Confidence:** **HIGH**

---

### RA-010 — WARN

- **FindingID:** RA-010
- **Product/Surface:** APP — `PKG-00_DAG_Closure_and_Project_Control`, `DEL-00-01`, `DEL-00-02`
- **Assertion:** Two App control deliverables occupy the `DEL-XX-YY` namespace and the shared SOW schema while deriving from a package README rather than an accepted decomposition, and their `project_scope_refs`/`package_objective_refs` name identifiers that exist in no accepted register.
- **EvidenceRefs:**
  - `…/PKG-00_.../1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/ScopeOfWork.md` frontmatter: `decomposition_basis: projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/README.md@0724f26f6…`; `project_scope_refs: [CONTROL-SCC-002]`; `package_objective_refs: [DAG-CLOSURE]`; `schema: chirality-deliverable-sow/v1`.
  - Neither `CONTROL-SCC-002` nor `DAG-CLOSURE` appears in the decomposition's 78-row ledger or 10-objective table.
  - `PKG-00/README.md`: "`PKG-00` is a meta/control package for project-level dependency closure… **not a decomposed product implementation package** and is not part of the strict deliverable dependency graph," with declared non-goals ("Do not use this package to invent dependency edges").
  - This is the explanation manifest condition **8** points at (51 decomposition deliverables vs 53 filesystem contracts); I assess consequence only.
- **Class:** observation (namespace/authority boundary)
- **Severity:** **WARN**
- **Consequence:** Contained by an explicit, well-drafted self-limitation — the README states the boundary and the non-goals, and the deliverables are honestly labelled control records. The residual consequence is that the `DEL-*` namespace and the SOW schema no longer imply "derived from an accepted decomposition," so any count, validator, or reviewer comparing SOW contracts to decomposition truth gets 53 vs 51 and cannot resolve `CONTROL-SCC-002`/`DAG-CLOSURE` against any register. Root's D-9 discipline ("packages and deliverables come only from an accepted decomposition") is a Root commitment and does not bind the App loop, so this is not a violation — but it is the one place where an identifier grammar shared across all three products carries different meaning.
- **SmallestAction/Owner:** Record in the App decomposition (or the PKG-00 README) that `DEL-00-*` is a reserved control namespace outside decomposition truth, with its own identifier grammar, so downstream counts and validators can exclude it deterministically. Owner: App loop coordination; no scope change.
- **Confidence:** **HIGH**

---

### RA-011 — WARN

- **FindingID:** RA-011
- **Product/Surface:** CROSS_PRODUCT — routed change notices to PEC and Piping
- **Assertion:** No routed D-GOV-26 or D-GOV-27 doctrine notice reached the PEC loop, and the Piping domain pack cites no D-GOV-20..27 record at all, although both are downstream of instruction-surface and runtime doctrine changes.
- **EvidenceRefs:**
  - `grep -rl "D-GOV-26\|D-GOV-27" projects/pec/` → **no match**.
  - Files citing `D-GOV-2[0-7]`: `projects/chirality-app-dev/execution/_Coordination` = 20; `projects/pec/execution/_Coordination` = 2; `domains/chirality` = 4; `domains/chirality-piping` = **0**.
  - Governing rule: `AGENTS.md` §Governance Integration Rules, agent-index change-notice rule — a tranche changing surfaces downstream loops pin or mirror "must … ship, in the same tranche, a routed coordination notice to each affected project loop's coordination surface"; Root PRD D-11 carries the same commitment as TRANSCRIBED.
  - Manifest condition **13** discloses uneven notice coverage; this finding assesses consequence and cites it.
- **Class:** omission
- **Severity:** **WARN**
- **Consequence:** D-GOV-26 changed what counts as the instruction surface (adding `CLAUDE.md` and `.github/workflows/`) and made changes to them M2 tranches by doctrine. PEC is a distinct client of the Root runtime (D-T0-23) and Piping is the situated-product exemplar; neither has been told. The change-notice rule exists precisely so detection does not depend on drift checks alone, and here the fallback is also weak — Root's own `domains/chirality` source manifest shows 93 DRIFT and 6 MISSING ACTIVE pins (condition 12). Contained for now because neither loop is currently acting on instruction-surface membership, and because a notice is coordination rather than authority (the receiving loop may decline). But RA-006 shows the same supersession failing to reach even a *Root* contract, so the propagation weakness is not confined to notice routing.
- **SmallestAction/Owner:** Ship the routed D-GOV-26/27 notices to `projects/pec/execution/_Coordination/` and the Piping coordination surface. Owner: Root loop, under the `AGENTS.md` change-notice rule and PRD D-11 (`DEL-04-04_Governance_Integration_Rules_and_Change_Notice_Routing` is the deliverable that already owns this).
- **Confidence:** **HIGH** on the absence; **MEDIUM** on materiality, since neither downstream loop currently depends on the changed enumeration.

---

### RA-012 — WARN

- **FindingID:** RA-012
- **Product/Surface:** PEC — invariants `PEC-K-03` and `PEC-K-11`
- **Assertion:** Two of PEC's eleven product invariants impose obligations on **consumers** (harnesses and agent instructions) rather than on PEC, and neither the PEC decomposition nor any routed obligation assigns those consumer-side obligations to an owner.
- **EvidenceRefs:**
  - `projects/pec/docs/PRD.md` §6 `PEC-K-03` "Harness-owned consumption. **Polling is performed by harnesses** at moments of consequence … and injected as labeled non-authoritative data. The only agent behavior is verify-before-rely."; `PEC-K-11` "Mode-proportional. Consumption follows §5; **zero-coordination modes remain zero-contact**."
  - §8: "**Agents** — never call PEC directly by instruction; they receive harness-injected orientation as labeled data (PEC-K-03)."
  - PEC decomposition DL-7 carries PEC-K invariants as constraints C1–C16 "not scope items, except where they require built or verified behavior." `PEC-K-03`→C3 and `PEC-K-11`→C15 generate no scope item stating the consumer obligation.
  - The consumer surfaces are Root-owned (the runtime daemon and hooks CLI, D-GOV-20) or agent-instruction-surface-owned (`AGENTS.md`), and `SOW-086` places the one relevant `AGENTS.md` amendment **OUT** as "Deferred, not permanent: … owner act on the root doctrine surface."
  - PEC's own decomposition owns the *producer* halves properly: `SOW-036`/`DEL-07-03` (hooks CLI bridge), `SOW-008`/`DEL-04-04` (scope parameterization per the modes ladder).
- **Class:** ownership gap
- **Severity:** **WARN**
- **Consequence:** PEC can build every producer-side capability and still have `PEC-K-03`/`PEC-K-11` unsatisfied, because satisfaction depends on harness polling discipline and agent instructions that PEC does not own and cannot change within its fences. No routed obligation exists to the owner who could. Contained because both invariants are honesty/proportionality properties rather than correctness dependencies — nothing breaks if they lapse, consistent with `PEC-K-01` — and because PEC has correctly fenced itself out of the doctrine surface rather than reaching into it.
- **SmallestAction/Owner:** Record, in the PEC decomposition's open-issue register alongside OI-001..OI-009, that `PEC-K-03` and `PEC-K-11` have consumer-side halves owned outside PEC, naming the owning surface. Owner: PEC loop (register annotation, no scope change); any actual amendment remains the owner's act on `AGENTS.md` per SOW-086.
- **Confidence:** **MEDIUM** — the reading that these are wholly PEC-internal design constraints is available; the basis does not decide it, so I mark the ownership question **UNKNOWN** and route it.

---

### RA-013 — WARN

- **FindingID:** RA-013
- **Product/Surface:** ROOT — scope item `SOW-026` / PRD item `O-1`
- **Assertion:** PRD `O-1` contains two clauses, and the Root scope ledger normalized only the second into `SOW-026`; the instruction-surface **membership enumeration** clause has no scope item anywhere in the 103-row ledger, while the forward register nonetheless marks O-1 fully `COVERED`.
- **EvidenceRefs:**
  - `docs/PRD_ROOT.md` §5.2 O-1: "The shared instruction surface **is `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and `init/`.** It **is release-managed and read-mostly**; changing it is a repo-wide governance action…" — two clauses.
  - `chirality_root_scope_ledger_v1_0.csv` `SOW-026` statement: "The shared instruction surface **is release-managed and read-mostly**, and changing it is a repo-wide governance action rather than ordinary working-root execution." — second clause only.
  - Search of all 103 statements for the enumeration or `init/` returns only `SOW-022` (N-6, authority chain), `SOW-026`, `SOW-080` (F1) — none carries membership.
  - `chirality_root_prd_coverage_forward_v1_0.csv`: `O-1 | commitment | §5.2 | COVERED | DEL-02-01…`.
  - `DEL-02-01`'s register row nonetheless anticipates an "Instruction-surface membership register" as its artifact, and its contract carries membership as `CLM-002`/`CON-001` prose.
  - The decomposition splits three other commitments explicitly for exactly this reason (DEC-004: N-1; DEC-005: N-5; D-14) — so the mechanism to handle O-1 the same way existed and was not applied.
- **Class:** trace gap (clause granularity)
- **Severity:** **WARN**
- **Consequence:** Structurally identical to the gap OI-013 recorded for OBJ-2 — a gap *inside* an item, where the registers cannot see it — but unlike OI-013 it is not recorded anywhere. The authoritative membership enumeration therefore enters the executable layer only as contract prose, which is what allows RA-006's error to occur without any register contradicting it. F4 is not tripped, because coverage is traced at item granularity and O-1 has coverage.
- **SmallestAction/Owner:** Record the clause-level gap as an open issue against `SOW-026`/`DEL-02-01` on the OI-013 pattern, or split `SOW-026` on the DEC-004/DEC-005 precedent so membership is a scope item citing SPEC §0.2.1. Owner: Root SCOPE_CHANGE (splitting an existing IN item, not new scope).
- **Confidence:** **HIGH** on the clause omission; **MEDIUM** that it is consequential independently of RA-006.

---

### RA-014 — WARN

- **FindingID:** RA-014
- **Product/Surface:** APP — `contract_invariant_coverage_register.csv`
- **Assertion:** The App decomposition names this register "required-or-deferred before REVIEW closure," the file does not exist, and no deferral ruling exists — so an acceptance condition the decomposition set for itself is unmet and undispositioned.
- **EvidenceRefs:**
  - `…SOFTWARE_DECOMP_v3_2.md` §2.2: "`contract_invariant_coverage_register.csv` | **Planned authoritative companion register** | … **It must be created or explicitly deferred before REVIEW closure.**"
  - §10B acceptance checklist: "CONTRACT invariant coverage | `contract_invariant_coverage_register.csv` is created, synchronized with this decomposition, **or explicitly deferred** before REVIEW closure."
  - DEC-011 and DEC-015 establish the intent and the honest interim posture.
  - Directory listing: `projects/chirality-app-dev/execution/_Decomposition/` contains only `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
  - Manifest condition **9** discloses the absence; I assess consequence.
- **Class:** omission
- **Severity:** **WARN**
- **Consequence:** §10A.1 substitutes a compact ten-row invariant-*family* ownership table, which is real coverage but at family granularity — it maps `K-AUTH`, `K-BIND`, `K-GATE`, `K-PROF` jointly to "PKG-01, PKG-07, PKG-10" without per-invariant enforcement or validation surfaces. So REVIEW has no per-`K-*` way to check the safety, permission, lifecycle, and human-gate obligations §10A.1 says it should be able to check. This compounds RA-007: neither the invariant layer nor the acceptance layer gives a reviewer a checkable per-obligation surface. Contained because REVIEW closure has not been claimed — no App deliverable is `ISSUED`.
- **SmallestAction/Owner:** Either create the register or record an explicit deferral naming what REVIEW may rely on meanwhile. The decomposition already frames both as acceptable; what is missing is the choice. Owner: App loop, before any REVIEW closure.
- **Confidence:** **HIGH**

---

### RA-015 — WARN

- **FindingID:** RA-015
- **Product/Surface:** ROOT — `D-GOV-27`, and the 45 Root SOW basis pins that depend on the chain below it
- **Assertion:** `D-GOV-27`'s `EffectiveSHA` is an unbound prose placeholder, and the Root SOW layer pins a decomposition state predating `D-GOV-27`'s own amendment, so the Root basis chain has an unclosed link at its most recent decision.
- **EvidenceRefs:**
  - `docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md` line 6: `EffectiveSHA: (merge of the closing-tranche PR into 'main'; backfilled by a later tranche per precedent)` — a description, not a SHA. Line 47 repeats "the EffectiveSHA above, backfilled on merge"; line 99 carries a further D-GOV-26 EffectiveSHA backfill item.
  - All 45 Root SOWs pin `653fabc9b3e8…` (uniform); the decomposition blob at that commit is `1378c6b601…`, whereas at `da31c19b` it is `121d2274209f…` — the difference being the D-GOV-27 DEC-021 objective propagation.
  - Manifest conditions **1** and **3** disclose the unbound EffectiveSHA and the missing verifying diff; Receipt 52 records the debt. I assess consequence only.
  - **Counter-evidence, verified:** the DEC-021 propagation *did* reach the contracts. `package_objective_refs` for the four amended deliverables match the register exactly — `DEL-01-04` `[OBJ-002, OBJ-003]`, `DEL-03-01` `[OBJ-004, OBJ-007]`, `DEL-03-06` `[OBJ-002, OBJ-004]`, `DEL-06-04` `[OBJ-004, OBJ-005]` — against register `SupportsObjectives` `OBJ-002;OBJ-003`, `OBJ-004;OBJ-007`, `OBJ-002;OBJ-004`, `OBJ-004;OBJ-005`. Content is current; only the pin metadata is behind.
- **Class:** trace gap (SHA binding)
- **Severity:** **WARN**
- **Consequence:** K-AUTH-2 makes an approval's SHA the thing that binds it and voids it on content change; E-3 requires the three SHA roles to be recorded distinctly. An unbound EffectiveSHA leaves the applied state of the Root loop's most recent decision unidentified, and the SOW pins name a state that no longer matches the decomposition. Materially contained — I verified the contracts carry the amended content, so no executor is working from wrong objectives — but the corpus cannot *demonstrate* that without the check I just ran by hand, which is the debt. This also sits directly on `DEL-05-03_SHA_Role_Register`, the deliverable that exists to keep SHA roles distinct, and compounds condition 2 (the decomposition header calling `ea0ad7a56…` "EffectiveSHA" against D-GOV-25's more precise assignment).
- **SmallestAction/Owner:** Backfill `D-GOV-27`'s EffectiveSHA per the precedent the record itself names, and either advance the 45 SOW pins to the post-DEC-021 state or record that `653fabc9b` is the intended stable SOW basis with DEC-021 applied additively above it. Owner: Root loop closeout; Receipt 52 already carries the debt.
- **Confidence:** **HIGH**

---

### RA-016 — INFO

- **FindingID:** RA-016
- **Product/Surface:** ROOT
- **Assertion:** Root's candidate AC/VER status is expressed in at least five distinct prose forms across the 45 contracts with no machine-readable field, so candidate status cannot be determined deterministically.
- **EvidenceRefs:** All 45 contracts mention "candidate"; distinct declaration forms include "Every `AC-*` and `VER-*` below is a **candidate**." (×4), "**AX-001** — Candidate status." (×4), "**AX-004** — Every `AC-*` and `VER-*` defined here is a candidate." (×3), the same statement as `AX-005` (×1) and as `AX-002` (×1), "definitions below are candidate content for owner review." (×4), and "criteria above are therefore candidate definitions authored under this contract." (×2). Only 13 of 45 use the explicit `AC-*`/`VER-*` formulation. Frontmatter keys across all 45 are exactly `schema`, `deliverable_id`, `package_id`, `decomposition_basis`, `project_scope_refs`, `package_objective_refs` — **no status field**. Manifest conditions **6** and **8** disclose this; I assess consequence.
- **Class:** observation
- **Severity:** **INFO**
- **Consequence:** F6 guards against a provenance label changing without an instrument, and the Root decomposition took considerable care at OI-002/DEC-017 to annotate rather than overwrite PROPOSED labels. That discipline is not carried into the SOW layer's own status representation: no tool can enumerate which acceptance criteria are candidate, so the F6 check over the 45 contracts is necessarily manual. Low consequence today — all 45 are `INITIALIZED` and nothing is issued — but it grows monotonically with the number of contracts.
- **SmallestAction/Owner:** Add one optional frontmatter field (e.g. `acceptance_status: CANDIDATE`) to the shared SOW schema. Owner: the shared SOW method layer (`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` / `skills/scope-of-work/`) under D-GOV-16 — a method change, not a product change, and it would serve all three loops.
- **Confidence:** **HIGH**

---

### RA-017 — INFO (positive verification)

- **FindingID:** RA-017
- **Product/Surface:** ROOT and PEC
- **Assertion:** Root's and PEC's decomposition registers are fully internally consistent under exhaustive bidirectional checking, and their SOW layers reproduce register truth exactly.
- **EvidenceRefs:**
  - **Root:** 103 ledger rows / 45 deliverable rows / 7 objective rows / 84 forward rows / 51 reverse rows. Every scope item carries exactly one `PackageID` (103/103); every IN item maps to ≥1 deliverable (94/94); ledger `DeliverableIDs` ↔ register `CoversScopeItems` **0 mismatches**; objective register ↔ deliverable register `SupportsObjectives` **0 disagreements**; forward-register objective rows ↔ objective register **0 disagreements**; all 9 OUT items retained and package-assigned per DEC-007.
  - **PEC:** 94 ledger rows / 64 deliverable rows. IN items without package **0**; without deliverable **0**; ledger ↔ `Deliverables.csv` **0 mismatches**; the 11 IN items lacking objective mapping are exactly the declared SCA-002 residue (`SOW-022, 023, 033–038, 044, 063, 087`), matching §3's stated list and §7's count of 11 item-for-item.
  - **All three products:** SOW frontmatter `project_scope_refs` vs register/decomposition coverage — Root **0/45** mismatches, PEC **0/32**, App **0/51**; App objective-ref mismatches **0/51**.
- **Class:** observation
- **Severity:** **INFO**
- **Consequence:** The register discipline works where authoritative companion registers exist. This is the direct control for RA-005: the same test that found seven App disagreements found none in Root or PEC, which is evidence that App's defect is attributable to the absent companion register rather than to reviewer method. It also means the coverage claims in Root's §11.3 and PEC's §7 are verifiable rather than asserted.
- **SmallestAction/Owner:** None. Recorded so fan-in does not read this review as uniformly negative.
- **Confidence:** **HIGH**

---

### RA-018 — INFO (positive verification)

- **FindingID:** RA-018
- **Product/Surface:** PEC
- **Assertion:** PEC is the only product whose SOW layer pins a decomposition basis identical to the current accepted decomposition, and its contracts carry the richest acceptance and conflict discipline in the corpus.
- **EvidenceRefs:** All 32 PEC contracts pin commit `3623b958b`, whose decomposition blob `8aab8caa747ab2dc70e45d18807d57079b16d4eb` equals the blob at `da31c19b` — byte-identical. 31 of 32 declare at least one `CON-*` conflict; 28 of 32 carry `HUMAN_REVIEW` acceptance gates; mean 12.3 `AC-*` and 10.9 `VER-*` per contract. Representative: `DEL-08-01` `AC-005` fences an unruled §16 decision ("no delivered artifact presumes the outcome of `SOW-083` / `OI-009`; CON-002 remains open") and `AC-007` forbids scope absorption from named siblings; `DEL-08-02` `AX-006` cites `C-10 STRATUM_RULE` and holds three `PROPOSAL`-stratum edges — one flagged `LOW_CONFIDENCE`, "owner may decline" — as "provenance for an expected consumption pattern [that] impose[s] no obligation." The three residuals disclosed at manifest condition PEC-3 are recorded exactly as described; `DEL-00-03`'s `CLM-001` is indeed unreferenced in its Output matrix, and is a pure identification claim.
- **Class:** observation
- **Severity:** **INFO**
- **Consequence:** PEC demonstrates that the shared SOW method layer can produce contracts that fence unruled decisions, refuse to absorb sibling scope, distinguish provenance from authority, and name the human gate per output. That materially strengthens the routing recommendations in RA-007 and RA-008: the target state is already exhibited inside the corpus and need not be designed. It also supplies the honest comparator for the version-skew condition — PEC's contracts were repaired under the current method, and the quality difference is visible.
- **SmallestAction/Owner:** None. Cite as the in-corpus pattern when dispositioning RA-007 and RA-008.
- **Confidence:** **HIGH**

---

## 2. M1 — Trace matrix (per product)

Dispositions: **COVERED** / **COVERED_WITH_RECORDED_DEFERRAL** / **TRACE_GAP** / **CONTRADICTED** / **NOT_EXECUTABLE**.

### 2.1 ROOT — 7 objectives

| PRD objective | Decomp | Deliverables (register-verified) | Disposition | Evidence / note |
|---|---|---|---|---|
| **OBJ-1** Coherent and discoverable normative authority | OBJ-001 | DEL-01-01, -01-02, -01-03, -01-07, -01-08, -02-01, -02-05, -04-07, -04-09 | **COVERED** | Objective register + forward register agree; 9 deliverables verified. Quality caveat at RA-006/RA-013 (DEL-02-01 works from a superseded enumeration). |
| **OBJ-2** Governed production of professional knowledge work | OBJ-002 | DEL-01-04, -01-06, -02-02, -02-03, -03-02, -03-06, -04-02, -04-06 | **COVERED_WITH_RECORDED_DEFERRAL** | Forward register `CoverageStatus = COVERED_WITH_RECORDED_DEFERRAL`; the situated-working-root half deferred by owner decision 1 of D-GOV-25, reasoned at §12.1 with three recorded grounds, tracked at OI-013 (`CLOSED_DEFERRED_BY_RULING`). **This is the model disposition** — machine-visible, reasoned, and explicit that "OBJ-2 remains partly undemonstrated." |
| **OBJ-3** Human evaluation and iteration loops close | OBJ-003 | 14 deliverables incl. DEL-04-01/-03/-04/-05/-08/-10, DEL-05-02/-03/-04/-05/-07/-08 | **COVERED** | Largest mapping; DEL-05-08 carries the sampled retrieval-usability half. |
| **OBJ-4** Safe self-application without self-authorization | OBJ-004 | DEL-02-04, -03-01, -03-04, -03-05, -03-06, -05-06, -06-01, -06-07 | **COVERED** | Includes the three DEC-021 additions. F1–F3 owned by DEL-06-01. |
| **OBJ-5** Situated specialization with governed convergence | OBJ-005 | DEL-06-04, -06-05, -06-06, -06-08 | **COVERED** | Smallest mapping (4); OBJ-5(i) is satisfiable by a rejection or reasoned deferral per the PRD's own text. |
| **OBJ-6** Coordination remains intelligible | OBJ-006 | DEL-03-03, -05-01, -06-02 | **COVERED** | Population bounded to root-product runs by the PRD itself. |
| **OBJ-7** File-native continuity and recoverability | OBJ-007 | DEL-01-05, -03-01 | **COVERED** | `UnmappedObjectives = 0` verified independently. |

**Root — the forward-coverage register's 84 admitted items.** Full census by `ItemKind`, recomputed from `chirality_root_prd_coverage_forward_v1_0.csv`: 7 objectives, 42 commitments (N-1..N-9, O-1..O-10, D-1, D-2, D-4..D-16, E-1..E-8), 13 directions, 6 falsifiers (F1–F6), 5 rulings (RD-1..RD-5), 4 obligations (obl-a, obl-b, obl-c, annex-10.1), 4 conflicts (C-1..C-4), 1 non-goal block. **83 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL, 0 UNCOVERED, 0 CONTRADICTED** — I verified this distribution myself rather than accepting §11.3. `D-3` is correctly absent (retired, never reassigned).

**Sample of forward rows verified against PRD text** (as the brief requires): `O-1` — **narrowing found**, RA-013; `OBJ-2` — deferral confirmed against §3 and §12.1; `D-15` → DEL-04-10 confirmed against §5.3 and demonstrated at §11.2 (all four categories COVERED, none deferred); `F5` → DEL-01-01 confirmed against §8.2 and C-1; `obl-a/b/c` → DEL-01-01 confirmed against §9.1's three obligations; `C-1..C-4` → confirmed against §10.2 with `HumanRuling = TBD` preserved for C-2/C-3/C-4; `release-8.3` → DEL-06-07 confirmed against §8.3; `E-5` → DEL-05-05 confirmed against §5.4. **One of nine sampled rows (O-1) was narrower than its PRD clause**; the other eight traced faithfully.

### 2.2 APP — 10 objectives

| PRD objective (decomp §6) | Mapped scope items | Disposition | Evidence / note |
|---|---|---|---|
| **OBJ-001** Governed local desktop harness centred on dialogue | SOW-001–008, 023 | **COVERED** | Ledger and §8 agree except SOW-023's UI half (RA-005); coverage survives via DEL-09-06. |
| **OBJ-002** Product-owned runtime contracts and thin route boundaries | SOW-009–018, 037–040 | **COVERED** | Carries the runtime seam; see RA-002/RA-003 for the ownership question, which is not a coverage gap. |
| **OBJ-003** Auditable turns, messages, outcomes, replay | SOW-014–015, 039–046, 059, 061 | **COVERED** | |
| **OBJ-004** Provider-adapter architecture, first adapter replaceable | SOW-016–021, 044–046, 051 | **COVERED** | OI-001/OI-006 open against SOW-018/044/045. |
| **OBJ-005** Tools only through deterministic capability policy | SOW-047–064, 076 | **TRACE_GAP** | **SOW-064 is inside this objective's range and has no executing contract** — RA-004. The objective is otherwise covered. |
| **OBJ-006** Filesystem project truth | SOW-024–034, 075, 077 | **COVERED** | |
| **OBJ-007** Agent-suite integrity and governed subagent delegation | SOW-005–006, 017, 030–031, 063 | **COVERED** | |
| **OBJ-008** Validation, packaging, release, network, key checks | SOW-019–022, 035–036, 072–073, 078 | **COVERED** | SOW-073 is TBD (OI-004 source completeness). |
| **OBJ-009** Professional boundary, product identity, reliance ownership | SOW-065, 071, 074, 076–077 | **COVERED** | |
| **OBJ-010** Future domain-engine compatibility | SOW-066–071 | **COVERED** | All six flagged `OpenIssue = TRUE` (OI-005, future amendment) — a lawful, recorded posture. |

**App — §16/§17-class commitments.**

| Commitment | Disposition | Evidence |
|---|---|---|
| §16: active decomposition is v3.2 with **78 / 10 / 10 / 51** topology | **COVERED** | Independently recomputed: 78 ledger rows, 10 packages, 10 objectives, 51 deliverable rows. Exact match. |
| §16: "If this PRD and the active SOFTWARE_DECOMP snapshot disagree … the conflict must be surfaced and resolved through governed PRD/decomposition amendment before scaffold or REVIEW closure" | **COVERED (self-executing) — and now triggered** | This clause is the lawful route for RA-003 and RA-009: a live PRD↔decomposition/filesystem disagreement exists and must be surfaced under App's own rule. |
| §16 package→PRD-coverage table (10 rows) | **COVERED** | Each package row's cited FR/Goal ranges resolve; PKG-00 is absent from the table, consistent with RA-010. |
| §16 runtime-roadmap traceability R0–R7 → FR IDs | **COVERED, one exception** | R0–R5, R7 resolve. **R6** cites FR-103–FR-105, whose decomposition carrier is SOW-064 — the orphan of RA-004. R6 is therefore **NOT_EXECUTABLE** as decomposed. |
| §17 (first) Approval and Change Control — PRD does not supersede DIRECTIVE/SPEC/TYPES/CONTRACT or active decomposition/scope-change records | **COVERED** | Consistent with decomposition §2.1 source-authority ordering. |
| §17 (second) Shared Runtime amendment — runtime is "a root-owned product subsystem"; daemon exclusively owns engines, credentials, sessions, tools, delegation, turn locks, interruption, residency | **CONTRADICTED** | Directly contradicted by decomposition §13's "implementation-location change … app-dev deliverables retain semantic ownership" — **RA-003**. Also unowned on the Root side — **RA-002**. |
| §17 (second) generic runtime/CLI/contracts/safe adapters export-eligible; credentials, machine state, private adapters excluded | **COVERED** | Matches `runtime/README.md` and D-GOV-20 item 10; tracked at OI-007 ("prove one runtime owner and both pilots before export"). |
| **Duplicate `## 17` heading** (lines 1676 and 1692) | **WARN-level defect** | Manifest condition **2**. Consequence: "§17" is ambiguous as a citation target, and both §17s bear on authority — one on change control, one on runtime ownership, the subject of the corpus's sharpest conflict. Smallest action: renumber the second to §18. Owner: App PRD editorial amendment. |

### 2.3 PEC — PEC-K-01..11 and PRD v2.1 objectives

**Invariants.** Per DL-7, PEC-K invariants are carried as constraints C1–C16 binding every scope item, and become scope items only where they require built or verified behaviour. Dispositions below reflect that ruled design.

| Invariant | Constraint | Built/verified carrier | Disposition |
|---|---|---|---|
| **PEC-K-01** Graceful absence | C1 | SOW-055 → DEL-10-02 (kill test, standing release gate); OBJ-005 | **COVERED** |
| **PEC-K-02** Files govern | C2 | SOW-010 → DEL-03-01; SOW-021, SOW-025 → DEL-10-03 | **COVERED** |
| **PEC-K-03** Harness-owned consumption | C3 | Producer half: SOW-036 → DEL-07-03. **Consumer half unowned** | **TRACE_GAP** — RA-012 |
| **PEC-K-04** Staleness is a comparison | — | SOW-006 → DEL-04-03 | **COVERED** |
| **PEC-K-05** Two trust tiers | C4 | SOW-032 → DEL-06-05; SOW-010 → DEL-03-01 | **COVERED** |
| **PEC-K-06** Observation, not participation | C5 | SOW-031 → DEL-06-06; boundary rows SOW-067, SOW-068 (OUT, permanent) | **COVERED** |
| **PEC-K-07** Ingest best-effort, reconciliation guaranteed | — | SOW-038 → DEL-03-05; instrument SOW-063 → DEL-10-08 | **COVERED_WITH_RECORDED_DEFERRAL** — SOW-063 is deliberately objective-unmapped because no §3 outcome states PEC-K-07 (DL-14, restated at §3 and §7). Recorded, reasoned, machine-visible. |
| **PEC-K-08** Everything derived is explainable | — | SOW-023 → DEL-05-01; SOW-050 → DEL-09-06 | **COVERED** |
| **PEC-K-09** Declared surface | — | SOW-039 → DEL-07-01 | **COVERED** |
| **PEC-K-10** Content-minimal | C6 | SOW-056 → DEL-01-03; twin boundary row SOW-073 (OUT, permanent) per DL-8 | **COVERED** |
| **PEC-K-11** Mode-proportional | C15 | Producer half: SOW-008 → DEL-04-04. **Consumer half unowned** | **TRACE_GAP** — RA-012 |

**Objectives** (PEC PRD has no section titled "objectives"; the decomposition derives them from §3 outcomes plus §11, and states so):

| Objective | Source | Disposition | Note |
|---|---|---|---|
| OBJ-001 sub-second cited orientation | §3.1 | **COVERED** | 14 deliverables + instruments SOW-058/059 |
| OBJ-002 structural staleness detection | §3.2 | **COVERED** | |
| OBJ-003 declared durable presence surface, pre-Git collision surfacing | §3.3 | **COVERED** | Instruments SOW-061/062/084 |
| OBJ-004 one live owner view | §3.4 | **COVERED** | |
| OBJ-005 deletable without blocking any governed act | §3.5 | **COVERED** | The graceful-absence objective; kill test is its executable form |
| OBJ-006 thesis remains measurable and falsifiable | §11 | **COVERED** | Both falsification limbs instrumented: limb 1 SOW-060, limb 2 SOW-085 |

**PEC residue.** 11 IN items carry no objective — verified identical to the declared list (`SOW-022, 023, 033–038, 044, 063, 087`). Nine are ingest/bridge or out-of-wave items deliberately left to the packet that authors their deliverables; SOW-063 is the intentional PEC-K-07 case. **All 11 have package and deliverable coverage** — this is objective attribution residue, not a coverage gap, and §3/§7 say so in terms. **Not a finding.** The 32 absent P2–P4 SOWs are deliberate sequencing (manifest condition 14) and likewise not a gap.

---

## 3. M2 — Cross-product ownership matrix

Each cell is evidenced or marked **UNKNOWN**. "Semantic owner" = the party whose accepted record governs meaning, distinct from code location and from client integration.

| Shared function | Semantic owner | Accepted record | Producers | Consumers | Fallback / degraded behaviour | Compatibility obligation | Routed change path |
|---|---|---|---|---|---|---|---|
| **Runtime protocol / daemon** | **Root** | D-GOV-20 items 1–2, 4; `AGENTS.md` §Shared Runtime Doctrine; Root PRD O-2(c) | `runtime/` packages (`runtime-contracts`, `-core`, `-daemon`, `-client`, `-cli`) | App (Electron composition root), PEC (D-T0-23), CLI, future domain apps | **UNKNOWN** — no accepted record states behaviour when the daemon is absent; D-GOV-20 calls it "opt-in" but no degraded-mode contract exists | Declared at D-GOV-20 item 4 (authenticated Unix socket, no TCP control listener) | **GAP — RA-002.** No Root package/deliverable owns it; work sits in App `DEL-03-01` Remaining. Change path currently runs through the App loop, not Root. |
| **Sessions** | **Root** (daemon "exclusively owns … sessions") | D-GOV-20 item 2; App PRD §17(2) | runtime-core registries | App (`.chirality/sessions/<id>/`), PEC presence tier | App keeps its own audit mirror canonical (PRD FR-121, NFR-029) — an explicit, evidenced fallback | Central sessions "lazily consume legacy project-local records without bulk rewrite or destructive move" (App PRD §17(2)) | Root, per D-GOV-20; **no Root deliverable** — RA-002 |
| **Credentials** | **Root** daemon; Electron supplies encrypted material | D-GOV-20 items 2–3; `runtime/README.md` | Electron `safeStorage` composition root | daemon | App PRD NFR-002/FR-031: never project truth, never logged | Single-owner boundary preserved via packaged app identity (D-GOV-20 item 3) | Root; **no Root deliverable** — RA-002 |
| **Delegation** | **Root** — authority contract | `AGENTS.md` §Delegation and Entry Rules; Root PRD O-3, O-4; D-GOV-20 items 7–8 | `AGENTS.md`; runtime-core `delegate_agent` | App (`ManagedDelegationService`, FR-060, R5), PEC (none — PEC is not an orchestrator, `SOW-067` OUT) | App FR-060/FR-102 fail closed; legacy SDK Agent adapter disabled | Agent 0/1/2 remain "authority and responsibility contracts independent of engine or model" (D-GOV-20 item 7) | Root instruction surface (M2 tranche); Root `DEL-02-03` owns the hierarchy and entry rules — **covered** |
| **Instruction surface** | **Root** | `docs/SPEC.md` §0.2.1 (8 members) as ruled by D-GOV-26, superseding record D-GOV-27; Root PRD O-1 as superseded | Root `docs/`, `agents/`, `skills/`, `tools/`, `AGENTS.md`, `CLAUDE.md`, `init/`, `.github/workflows/` | every loop and working root | Working roots may extend the invariant catalog but MUST NOT weaken it (PRD §7.1; `docs/CONTRACT.md` §1) | M2 tranche required; changes to `CLAUDE.md` and `.github/workflows/` are M2 by doctrine (D-GOV-26) | Root `DEL-02-01` — **but it works from the superseded 6-member enumeration, RA-006; membership has no scope item, RA-013** |
| **SOW method layer** | **Root** | D-GOV-16; `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`; `skills/scope-of-work/`; `tools/scope_of_work/` | Root | **all three products** — schema `chirality-deliverable-sow/v1` verified across all 130 contracts | Not a correctness dependency; contracts are readable without tooling | **Version skew is a live condition**: PEC validated under the current method; Root passed pre-v6/v6.1 (manifest §4); **App era UNKNOWN** | Root method change (D-GOV-16). RA-016's fix belongs here. |
| **Coordination / PEC** | **PEC** | PEC PRD v2.1 (D-PEC-58, D-PEC-61); `PEC-K-01`; D-T0-15 fences F-PEC-1..4 | PEC record + presence tiers | harnesses on behalf of agents; the human owner via dashboards | **Strongest fallback in the corpus** — `PEC-K-01`: "No governed act may require a PEC read or write. Deleting PEC blocks nothing," with the kill test as a standing release gate (`SOW-055` → `DEL-10-02`) and a falsification clause that deletes the product | Parity-diffable against the practitioner harness permanently (`PEC-RCN-005`) | PEC loop; each build tranche needs its own owner-ruled packet (F-PEC-1, C14) |
| **Reusable work surface** | **UNKNOWN** | **No accepted record assigns ownership.** Charter lists App's dual identity as *clarified framing* only, and lists this among questions "intentionally held open" | App implements the surface (PRD Goal 4, FR-001, PKG-02) | none declared — no other product consumes an App-provided surface in the corpus | n/a | n/a | **Held open — §5.1 below.** Absence is not a gap: no accepted instrument creates the obligation, and a review may not create one. |
| **Domain-truth boundary** | **Domain engines** | `K-DOMAIN-1`..`K-DOMAIN-4`; Root PRD N-1 stated exception and §7.1; App FR-106–FR-115; PEC §4.2 | domain engines (canonical model files, solver outputs) | Root (governs work *around* the engine), App PKG-10, PEC (models other loops' lifecycle units only) | App: protected paths write-quarantined (FR-110), proposals are agent-writable, accepted state is not | App `DomainEngineProfile` gated to future amendment (OI-005); Root `DEL-06-05` owns the boundary | Root `DEL-06-05_Domain_Engine_Truth_Boundary` — **covered**; App PKG-10 — **covered, deferred** |
| **Evidence conventions** | **Root** | Root PRD E-1..E-8; `AGENTS.md` snapshot/handoff/closure rules; `K-SNAP-1` | Root `_Coordination/AgentRuns/`, receipts, snapshots | all loops (App `_STATUS.md` + `_Coordination`; PEC receipts, `_LATEST.md`) | Files and Git remain sole authority (D-GOV-01) in every loop | PEC parses per-loop receipt grammars and states coverage limits (`PEC-ORI-006`); only the app-dev ledger is schema-validated (D-APP-57) | Root PKG-05 (8 deliverables) — **covered**. §16.8 open decision on whether other ledgers adopt the D-APP-57 contract. |
| **Export / release** | **Root** | `K-EXPORT-1`; Root PRD D-10, §8.3; D-GOV-20 item 10 | `exports/chirality-app/export_public.py` (allowlist profile) | App (separate public repo), runtime | Fails on forbidden paths or leaks | Profile is the boundary contract, incorporated by reference; C-4 records a README-vs-profile divergence over `runtime/`, `HumanRuling = TBD` | Root `DEL-04-07_Public_Export_Boundary_Conformance` and `DEL-06-07_Release_Authority_Gate` — **covered** |
| **Resource governance** | **n/a — absent by design** | **No accepted record.** Manifest §Consulted-only: "not accepted Root, App, or PEC scope, a source of authority, a system of record, or a correctness dependency"; charter status **candidate capability** | none | none | n/a | n/a | **Absence is not a gap** (charter §5: candidate architecture — absence must not be counted as a scope gap). Any adoption would require its own service, authority, data, and degraded-mode contract before entering product scope. **No finding raised.** |

**Cross-cutting reading.** Of twelve shared functions, nine have a clear semantic owner with an accepted record. One (**reusable work surface**) is genuinely UNKNOWN and correctly held open. One (**resource governance**) is absent by design and correctly generates no finding. One — the **runtime cluster** (protocol/daemon, sessions, credentials) — has a clear *accepted record* naming Root as owner but **no Root decomposition unit implementing that ownership**, with the work resident in an App deliverable and one App decomposition sentence pointing the other way. That single cluster is the source of RA-002 and RA-003 and is the corpus's one live ownership question.

---

## 4. M3 — Charter question set (all 13)

Answered from governed records; the charter is the challenge set, never the evidence.

**Q1 — Root: Shared runtime ownership.** *Does one Root package own runtime protocol, daemon, clients, sessions, tools, delegation, credentials, adapters, compatibility, security, migration, and release evidence?*
**Disposition: NO — ownership gap (RA-002).** D-GOV-20 assigns the subsystem to Root and `runtime/README.md` confirms the daemon's exclusive ownership, but no Root package, deliverable, or scope item carries it: 0/103 scope items and 0/45 deliverables match `daemon|credential|residency|turn lock|engine adapter|socket`. Root's only coverage is O-2's three-layer *boundary* conformance at `DEL-02-02`. Delegation (`DEL-02-03`) and release authority (`DEL-06-07`) are separately owned and covered. Routes to owner decision: PRD amendment or recorded deferral.

**Q2 — Cross-product: Producer, consumer, and fallback.** *For every shared function, are the semantic owner, consuming products, accepted basis, fallback, and routed-change obligations explicit?*
**Disposition: PARTIAL.** See M2. Nine of twelve fully explicit. PEC's fallback (`PEC-K-01` plus the kill test as a standing release gate) is the strongest and most testable in the corpus. **The runtime cluster's fallback is UNKNOWN** — no accepted record states what happens when the "opt-in" daemon is absent, even though optionality is asserted. The reusable work surface has no owner (held open); resource governance is absent by design.

**Q3 — Root: Four-category coverage without folder mimicry.** *Are normative, operative, developmental, and evidence functions covered or reasonedly deferred without simply creating four packages named after the categories?*
**Disposition: YES — exemplary.** PRD §4.3 forbids reading the categories as a partition; DEC-003 declines it explicitly; §11.2 demonstrates all four COVERED with none deferred, and every category spans four or more of the six packages, participation ranging from two categories (PKG-02) to all four (PKG-01, PKG-04, PKG-06). D-12 is honoured directly — developmental machinery is decomposed as product scope (PKG-04, 10 deliverables), not exempted as overhead. This is the clearest case in the corpus of decomposition preserving rather than replacing owner intent.

**Q4 — Cross-product: Application composition boundary.** *Does the corpus provide a lawful home for reusable work-surface and application-integration contracts, or reveal a genuine PRD gap that decomposition may not invent?*
**Disposition: NO LAWFUL HOME — and correctly not invented.** No accepted instrument assigns ownership of a reusable work surface or an application environment profile. The charter's application-environment profile is **candidate architecture**, so its absence is **not** a scope gap. Critically, no decomposition invented one: Root's PKG-06 handles variant service and promotion without claiming a work-surface contract; App's PKG-02 scopes its shell to itself; PEC declares itself optional. The corpus behaved correctly. Held open at §5.1/§5.2.

**Q5 — App: Standalone product and reusable work surface.** *Can the App remain a coherent standalone product while its human–agent surface is reused as embedded, companion, or sidecar capability without exporting incidental presentation assumptions?*
**Disposition: UNRESOLVED — concordance question only** (charter status: *clarified framing*; I may not fail App for not instantiating it). The App PRD supports the standalone identity fully (§2, Goals 1–8, §6.2 release target). It does **not** claim the reusable-surface identity: no FR, objective, or scope item states it. §17(2) does establish the *runtime* as reusable and root-owned, which is the substrate half — but the presentation half is unclaimed. Principle 29 ("Visible material is not automatic context") and Goal 25 (compatibility period) suggest presentation assumptions are being deliberately contained, which would help if reuse were later adopted. No finding; the question needs an owner decision before it can be tested.

**Q6 — App: Faithful human/agent mediation.** *Do UI and direct-agent paths preserve prerequisites, authority, state effects, provenance, interruption, recovery, errors, and outcomes without either surface bypassing governance?*
**Disposition: YES at the PRD layer; WEAK at the acceptance layer.** The PRD is strong and specific: FR-008/FR-009 (replay is read-only, never resumes or mutates the primary session), FR-021 (`turn.accepted` persisted before model execution), FR-087–FR-092 (structured, persisted permission decisions), FR-089/FR-125 (hard denies override all allows, including developer bypass), Principle 17, Principle 28 ("Coordination is projection, not authority"), and the §3.2 non-goal forbidding the Coordination Panel from creating plans, inferring parentage, transitioning lifecycle, or authenticating a human act. But **RA-007**: the deliverables that must implement this carry conversion-fidelity acceptance criteria, and 0/53 contracts name a per-output acceptance gate. The commitments are sound; the contracts do not make them checkable.

**Q7 — App ↔ Root: Runtime client, not runtime authority.** *Are App deliverables limited to client integration, presentation, packaging, and conformance rather than retaining permanent semantic ownership of the shared Root runtime?*
**Disposition: NOT DEMONSTRATED — RA-003, compounded by RA-002.** App PRD §17(2) states the correct posture ("root-owned product subsystem rather than a frontend-owned singleton"). App decomposition §13 states the opposite ("Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership"), and only in prose. Meanwhile App `DEL-03-01`'s Remaining carries the actual promotion and conformance work while Root carries none. OI-007 tracks the sequence and requires proving "one runtime owner … before export," which is the right gate — but the ownership statement itself points the wrong way and needs correction.

**Q8 — PEC: Coordination without authority.** *Does PEC remain advisory, explainable, rebuildable, and file-fallback-safe — never a ruling surface, system of record, dispatcher, lock manager, or Git actor?*
**Disposition: YES — strongest boundary discipline in the corpus.** Every prohibition has both a permanent OUT boundary row and a built/verified twin per DL-8: system-of-record `SOW-065` OUT; ruling surface `SOW-066` OUT twinned with `SOW-025` (verified as a tested property of the API surface) → `DEL-10-03`; orchestration `SOW-067` OUT; lock management `SOW-068` OUT; Git actions `SOW-070` OUT; harness replacement `SOW-069` OUT. `PEC-GAT-004` provides no write path recording adoption, ruling, or direction. `PEC-K-08` makes every verdict Explain-shaped with rule, threshold, and cited sources. The one tension I tested is §5's doctrine note — that a declared durable surface is "what makes [concurrent Agent 0 operation] lawful," which would make PEC a lawfulness dependency and sit awkwardly with `PEC-K-01`. **PEC handles it correctly**: the note is marked "future `AGENTS.md` amendment, not made by this PRD," §15 records the lawfulness question as an open `AGENTS.md` matter "not resolved by this PRD," and `SOW-086` places the amendment OUT as deferred, an owner act on the root doctrine surface. Flagged, fenced, not asserted.

**Q9 — PEC ↔ environment: Complexity-dependent availability.** *Is PEC optional for correctness and available where concurrency warrants it, with declared identities and graceful absence rather than silent mandatory coupling?*
**Disposition: YES, with one unowned edge (RA-012).** The §5 modes ladder scales consumption from zero (pipeline, unscoped conversation) to "essential for throughput (**not for soundness** — file fallback remains)" for concurrent Agent 0s. `PEC-K-01` and the standing kill test make optionality executable rather than asserted, and the §11 falsification clause commits to deleting the product if adoption is negligible. Identities are declared (`PEC-K-09`, `PEC-PRS-001`). The edge: `PEC-K-03` and `PEC-K-11` bind *consumers*, and no owner holds those halves.

**Q10 — Resource governance ↔ environment: Optional planning and resource service.** *Does resource governance consume accepted system information … while remaining optional, replaceable, and unable to create authority or become the system of record?*
**Disposition: NOT IN SCOPE — no finding, by charter rule.** Resource governance is **candidate capability** (charter §4) and the manifest is explicit that it "is not accepted Root, App, or PEC scope, a source of authority, a system of record, or a correctness dependency" (condition 19). Its absence from all three decompositions is therefore correct and must not be counted as a gap. I confirmed no decomposition has invented it: no scope item, deliverable, or objective in any of the three products addresses estimates, sequencing, locks/freezes, budgets, usage, cost, or forecast monitoring as a service. **Observation for the owner, not a finding:** if it is ever adopted, the corpus already contains the pattern it would need — PEC's `PEC-K-01` plus kill test plus falsification clause is a working template for an optional service that cannot become a correctness dependency, and the lock/freeze authority boundary the charter flags would need exactly PEC's IN/OUT twinning discipline (DL-8) to keep "surface a conflict" separate from "prevent work."

**Q11 — All: Human judgment remains the hinge.** *Do validators, runtime state, UI controls, coordination projections, cost thresholds, and agent capability remain evidence or objective gates rather than substitutes for acceptance, reliance, iteration, or release judgment?*
**Disposition: YES in doctrine; UNEVEN in the contracts.** Doctrine is consistent and strong across all three: K-AUTH-1 (only humans author binding approvals); D-GOV-02 (a BLOCK is bounded to its declared observation boundary, never a global verdict); D-GOV-17 (a validator finding may never mechanically reject owner-ruled content — "where ruled text trips a validator, the validator is defective"); Root PRD §4.2's three judgments (evaluation, iteration, release) explicitly not collapsed and none delegated to machinery; §8.3 release as a separate human gate; PEC-K-06 and PEC-GAT-002 (advisory only); App NFR-023 (human approval non-delegable) and FR-054 (approval SHA for human-gate transitions). Root's `DEL-01-04` implements the three-judgment separation directly, with `AX-004` requiring that no non-overridable machine BLOCK exist on the issuance judgment. **The unevenness is at the contract layer**: 41/45 Root and 28/32 PEC contracts name a `HUMAN_REVIEW` gate per output; **0/53 App contracts do**, and App's acceptance criteria largely test document conversion (RA-007). App's human gate is real but lives in `_STATUS.md` (approval SHAs, `(HUMAN)`-attributed transitions, `Authorization Basis`), untraced to requirement IDs. The hinge holds; in one loop the human is asked to turn it without a checkable contract.

**Q12 — All: Domain truth remains situated.** *Do Root, App, runtime, and PEC govern work around domain engines without absorbing protected domain state, deterministic domain acts, or professional authority?*
**Disposition: YES — consistently.** Root PRD N-1 carries the K-DOMAIN-1 exception **in the PRD body rather than only in the annex**, with the stated reason that "the annex is never adopted" — a deliberate and correct provenance choice; §7.1 states the root "governs the work around them without becoming the solver"; `DEL-06-05_Domain_Engine_Truth_Boundary` owns it. App Principle 24 and FR-106–FR-115 keep profiles, protected paths, and `OperationProposal` records gated to future amendment (OI-005), with FR-110 write-quarantining protected paths and FR-115 forbidding any representation of domain output as professional approval or solver truth; the §3.2 non-goals forbid becoming a solver and forbid agents writing protected model paths. PEC models *other loops'* `Package`/`Deliverable` lifecycle units as record-tier entities and disambiguates that sense explicitly in its Vocabulary Map, holds `PEC-K-10` content-minimality so no domain content is ingested, and retires its own L3 domain-operation lane (`SOW-090`, deferred). I found no instance of generic infrastructure absorbing domain truth.

**Q13 — Deliverable SOW: Executable and warranted scope.** *Does each SOW trace to accepted product scope, have one primary owner, name interfaces and evidence, fit its context envelope, and avoid introducing new product commitments through implementation prose?*
**Disposition: MIXED — strong on trace, weak in two specific places.**
*Trace:* excellent and machine-verified — `project_scope_refs` match register truth with **0 mismatches in all three products** (45/45, 32/32, 51/51), and objective refs likewise.
*Primary owner:* `ResponsibleParty` is `TBD` across Root (OI-011, carried open by ruling) and PEC (assignment deferred to WORKING_ITEMS activation) — a recorded, deliberate posture, not a defect; Root's register has since recorded `Ryan Tufts` per D-GOV-27 while contracts retain `TBD` pending human assignment.
*Interfaces and evidence:* strong in Root and PEC (deterministic `VER-*` naming commands and paths, explicit `Records` sections carrying `TBD` where paths are unassigned — e.g. App `DEL-06-02` correctly refuses to infer implementation paths from planned artifact names, citing K-INVENT-1). Weak in App generally (RA-007).
*Context envelope:* no XL in any product; Root S=14/M=30/L=1 with the single L accepted at Gate 5 (OI-010); PEC 28/34/2 with both L carrying mandatory envelope notes and named split lines; App S=9/M=40/L=2 — all three conform.
*New commitments in prose:* **two instances found.** (i) App decomposition §13's runtime-ownership sentence — RA-003. (ii) App `DEL-06-02`'s `CLM-035`/`AC-002` assign ownership of four coordination MCP tools (`delegate_agent`, `report_coordination_notice`, `send_agent_update`, `ack_agent_update`) on the authority of D-APP-68 — the commitment **is** routed to a decision record, so it is lawful, but it has not been propagated back into the accepted decomposition's scope ledger, so decomposition truth does not know about it. That is the recurring pattern of this review: rulings land in records and contracts but do not reliably return to decomposition truth (cf. RA-006, RA-013, RA-015).

---

## 5. Held-open questions

The charter names six intentionally-open questions. For each: what the basis says, what it cannot decide, and the decision criteria. **I close none of these by preference.**

### 5.1 Whether the reusable work surface is a Root requirement, an App capability, or both under different ownership

**What the basis says.** No accepted instrument assigns ownership. App builds a human–agent surface (PRD Goal 4, FR-001, PKG-02, five deliverables) but claims only the standalone identity. Root PRD §7.1 serves variants with instruction basis and (via D-GOV-20) runtime, but names no work-surface obligation; Root's registries govern `agents/`, `skills/`, `tools/` — instruction resources, not presentation. PEC explicitly declines to be a work surface (`SOW-071` OUT, the human-PM lineage retired).
**What it cannot decide.** Whether a second consumer of an App-provided surface will ever exist. The corpus contains exactly one situated-product exemplar (Piping, consulted-only), and it has no recorded dependency on an App surface.
**Decision criteria.** (a) Does a second consumer exist or is one committed? Absent one, Root ownership would be speculative generalization. (b) Can presentation be separated from governance in App's PKG-02 without exporting incidental assumptions — testable against Principle 29 and Goal 25's compatibility period. (c) Which loop would carry compatibility and migration obligations for a surface consumed by others. **Downstream work affected:** App PKG-02 (5 deliverables) and any future domain-application decomposition. **Note:** the App UI/API semantic-parity work the charter mentions is *not* an established instrument (manifest conditions 1-App and 18) and cannot be used to answer this.

### 5.2 The exact authority and schema of an application environment profile

**What the basis says.** Nothing. This is charter **candidate architecture**; no PRD, decomposition, or decision record defines it. Its absence is correctly not a gap, and — importantly — no decomposition invented one.
**What it cannot decide.** Everything about it: authority, schema, and whether it should exist.
**Decision criteria.** The charter's own three groupings are a reasonable starting slate (basis/identity-and-compatibility; capabilities/declared composition; boundaries/authority-and-fallback), but adopting them requires a Root PRD amendment — never decomposition or SOW prose. A prerequisite: §5.1 must resolve first, since the profile's capability section presupposes an answer about the work surface. **Would resolve:** RA-002's fallback UNKNOWN (a profile would force a declared degraded-mode contract for the runtime).

### 5.3 When PEC is available, recommended, or required by complexity

**What the basis says.** The §5 modes ladder is precise about *consumption* — zero for pipeline and unscoped conversation, through package-scoped, loop-scoped, fan-in, up to "essential for throughput (not for soundness)" for concurrent Agent 0s. `PEC-K-01` and `PEC-K-11` make "required" impossible by construction: no governed act may require PEC, and zero-coordination modes stay zero-contact.
**What it cannot decide.** Where "recommended" begins. The ladder gives a qualitative gradient, not a threshold, and §16.3 leaves the loop registry's home and shape open (today five loops, local config default per `SOW-094`).
**Decision criteria.** The §11 metrics are designed to answer this empirically: harness poll adoption (metric 4, `SOW-060`), collision incidents per week of concurrent operation (metric 3, `SOW-084`), and Step-0 cost before/after (metric 1, `SOW-058`, baselined pre-P1). **The right posture is to let P3 measure rather than to decide now** — and the falsification clause means a negative answer deletes the product, which is a stronger commitment than most optionality claims. **Interaction:** RA-012's unowned consumer-side halves would need an owner before "recommended" could be operationalized, since recommendation acts on harnesses.

### 5.4 The product home, service contract, lock/freeze authority boundary, and fallback behaviour of optional resource governance

**What the basis says.** Nothing — candidate architecture only (manifest condition 19).
**What it cannot decide.** All four.
**Decision criteria.** Before entering any product scope it would need, at minimum: a named semantic owner; a declared service contract; an explicit statement that locks and freezes are *projections of accepted human or workflow authority* rather than sources of it; and a degraded-mode contract. The charter's own framing is the binding constraint — it must be "unable to create authority or become the system of record." **In-corpus template:** PEC's `PEC-K-01` + kill test + DL-8 IN/OUT twinning is a working pattern for exactly this shape. **Nothing in the three products depends on this being answered.**

### 5.5 Logical composition versus physical bundling and update cadence

**What the basis says.** Partially answered, in one direction only. D-GOV-20 rules the physical arrangement for the runtime: one per-user daemon, supplied by the packaged Electron application without a window, authenticated Unix socket, **no TCP control listener**, with Desktop/CLI/project integrations as clients. PEC keeps a parallel question open at §16.9 (event-contract home: shared `runtime/packages/contracts` vs a PEC-local schema with a pinned mirror; Unix socket only vs an additional loopback listener) and at §16.5 (whether the PEC web UI folds into the desktop app), and fences itself to build local-first either way (`SOW-083` TBD, `SOW-074` OUT-deferred).
**What it cannot decide.** Update cadence — no record states how a runtime protocol version change propagates to App and PEC clients, or who declares compatibility. This is the practical residue of RA-002: without a Root owner, cadence has no owner either.
**Decision criteria.** One runtime owner (the charter's own constraint, and OI-007's gate); declared protocol compatibility; no duplicative daemon or governance fork. PEC's §16.9 should not be ruled before RA-002 is dispositioned, since the contract home depends on who owns `runtime/`.

### 5.6 Which cross-client conformance proofs are release requirements

**What the basis says.** Fragments, unassembled. App FR-123 requires a provider/SDK adapter to pass engine conformance tests *before becoming the default production path*, and enumerates nine areas. D-GOV-20 item 9 defines an initial vertical slice (one Agent 1 run delegating one bounded read-only task to a Pi/oMLX Agent 2 with canonical evidence and actual-model attribution). App OI-007 requires proving "one runtime owner and both pilots before export." PEC's parity diff (`PEC-RCN-005`) is permanent but is a *product* obligation, not a cross-client one. Root PRD §8.3 makes release a separate human judgment informed by validation, coverage, and guard state — but names no cross-client proof.
**What it cannot decide.** Whether any cross-client conformance proof is a *release* requirement, and for which release. The fragments live in three different loops with no assembling instrument.
**Decision criteria.** Which client behaviours, if divergent, would break a governed act (those are release requirements) versus merely degrade throughput (those are not) — the same soundness/throughput distinction PEC already draws at §5. **Owner:** Root release authority (`DEL-06-07_Release_Authority_Gate`) is the natural home, and it currently has no cross-client input, which is a consequence of RA-002 worth weighing when dispositioning it.

---

## 6. Summary for fan-in

Rank-ordered by what I judge consequential enough for owner judgment. Full detail and evidence above; nothing here is new.

**1. RA-001 (BLOCK) — Six App SOW contracts pin a decomposition-basis commit that does not exist.** `416b29033bbacb…` fails `git cat-file -e`; a different object shares only its 9-char prefix; the repo is not shallow. Affected: `DEL-02-01`, `-02-02`, `-02-04`, `-05-04`, `-08-02`, `-08-03` — nearly exactly the set SCA-APP-004 rescoped. Their declared basis is unverifiable, so K-AUTH-2 binding cannot be checked at all. Smallest fix: re-pin in one bounded tranche; no scope change.

**2. RA-002 + RA-003 (REVIEW, paired) — The shared runtime has an accepted Root owner and no Root implementation of that ownership, plus one App sentence pointing the other way.** D-GOV-20 rules `runtime/` root-owned and the daemon the exclusive owner of engines, credentials, sessions, delegation, tools, turn locks, interruption, and residency. Root's decomposition contains **zero** matching scope items (0/103) or deliverables (0/45); its only runtime coverage is O-2's boundary-conformance slice. The actual promotion and conformance work sits in App `DEL-03-01`'s Remaining, and App's decomposition §13 says root ownership "is an implementation-location change; app-dev deliverables retain semantic ownership" — contradicting App's own PRD §17. This is the corpus's one live ownership question and the only place where a temporary migration arrangement could harden into permanent divided ownership. **Owner decision needed on route**: a Root PRD amendment (M2 tranche) versus an explicit recorded deferral on the OBJ-2/§12.1 pattern. A decomposition edit alone is not lawful (D-9).

**3. RA-006 (REVIEW) — The contract that exists to settle instruction-surface membership works from the superseded enumeration.** Root `DEL-02-01` frames the conflict as six-versus-seven between the PRD and its own `_CONTEXT.md`, omits `CLAUDE.md` entirely, and calls settlement "an owner act" — when D-GOV-26/27 already ruled eight members at SPEC §0.2.1, as the PRD's own pointer block records. Executed as written it would certify a ruled question as open. This is the sharpest evidence that supersession-by-pointer does not reach the executable layer (condition 10's consequence), and RA-013 shows why nothing caught it: O-1's membership clause has no scope item at all.

**4. RA-004 + RA-005 (REVIEW) — App scope item SOW-064 has no executing contract, while coverage telemetry certifies zero gaps.** Confirmed in both register directions and at the executable layer (`grep` across all 53 contracts: no match). It carries PRD FR-064/FR-103/FR-105 and runtime phase **R6**, which is therefore not executable as decomposed. It is one of seven §8-versus-§9 disagreements that exist because App maintains no companion register — the same exhaustive test found **0** mismatches in Root and **0** in PEC.

**5. RA-007 (REVIEW) — App's deliverable acceptance criteria test document conversion, not deliverable fitness.** 48/53 contracts carry exactly one AC and one VER; at least 13 state acceptance as preserving legacy source content "without changing lifecycle or dependency state"; **0/53** name a human acceptance gate, against 41/45 Root and 28/32 PEC. App's human gate is genuinely present but lives in `_STATUS.md` (approval SHAs, `(HUMAN)`-attributed transitions) and is untraced to requirement or AC IDs — so at CHECKING/ISSUED the approver has no per-requirement statement to check. I hold this at MEDIUM confidence on severity: it may be a recorded consequence of the D-APP-54 rebaseline, and the corpus does not say.

**6. RA-008 (REVIEW) — App's SOW layer has five different declared bases, all superseded.** No pin is later than 2026-07-13, so all 51 predate SCA-APP-003 (07-22) and SCA-APP-004 (07-23) — the two amendments that moved the runtime to Root and replaced the target UI. Root pins one commit; PEC pins one commit whose blob is **byte-identical** to the current decomposition, the only product whose SOW basis is current.

**Cross-cutting pattern worth the owner's attention.** Five separate findings (RA-004, RA-006, RA-008, RA-013, and Q13's D-APP-68 case) are the same failure in different places: **rulings and amendments land in decision records and in individual contracts, but do not reliably return to decomposition truth.** Root's DEC-021 propagation shows this can be done well — I verified the four amended deliverables' objectives match the register exactly — and PEC's SCA-001/SCA-002 amendments likewise carried into ledger, registers, and contracts together. The corpus contains its own remedy; it is applied unevenly.

**What I found sound, and would not want lost at fan-in.** Root's four-category coverage demonstration (Q3) is exemplary and resists the folder-mimicry failure explicitly. Root's OBJ-2 deferral is the model disposition in the corpus — reasoned, machine-visible, and honest that the objective "remains partly undemonstrated." Root and PEC registers are **fully internally consistent** under exhaustive bidirectional checking, and all three products' SOW frontmatter reproduces register truth with **zero** mismatches across 128 checked contracts. PEC's boundary discipline (Q8) — every prohibition twinned with a verified obligation, optionality made executable by a standing kill test, and a falsification clause that deletes the product — is the strongest such discipline here, and its contracts are the in-corpus pattern I would cite when fixing RA-007 and RA-008. Domain truth remains situated in all three products (Q12) with no instance of infrastructure absorbing it. And no decomposition invented an application environment profile, a reusable-work-surface obligation, or resource governance — the three candidate architectures stayed out of product scope, which is exactly right.

**Severity counts:** BLOCK 1 · REVIEW 7 · WARN 7 · INFO 3 (18 findings, RA-001..RA-018).

**Coverage:** complete. No blocker prevented any part of the assigned review.
