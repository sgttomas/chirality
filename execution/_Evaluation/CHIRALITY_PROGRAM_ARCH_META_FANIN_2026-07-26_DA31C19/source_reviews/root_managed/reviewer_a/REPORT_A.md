# REPORT A — Reviewer A, vertical lens (authority, intent, traceability)

Run: TANDEM-REVIEW-20260726 · Pass 1 (independent). Bounded read-only Agent 2; no delegation performed.

> Manager filing note (not reviewer content): Reviewer A's harness blocked the report-file
> write required by brief §8; the reviewer returned this report in its terminal response
> with an explicit deviation disclosure (structural summary and §8). The supervising
> manager persisted the returned content verbatim to this path and froze it by hash on
> receipt. Channel-introduced HTML entity escapes (&amp; &lt; &gt;) were normalized to their
> literal characters; no other change. The reviewer's structural summary stated finding
> counts of 9 REVIEW / 12 WARN; the manager's deterministic tally of the register is
> 8 REVIEW / 13 WARN (see VALIDATION_REPORT_A.md); finding content is unaffected.

Reviewer's structural summary (returned with the report):

- **Sections present:** all 7 required (reviewed-basis statement; product accounts; coverage matrices; boundary/ownership matrix; findings register; disclosed-conditions assessment; open questions/UNKNOWNs).
- **Findings:** 29 total — **0 BLOCK, 9 REVIEW, 12 WARN, 8 INFO** (ROOT 11, APP 10, PEC 4, CROSS_PRODUCT 4).
- **Coverage totals:** Root 84/84 PRD items dispositioned (83 COVERED, 1 recorded deferral, 0 gaps); App 159/159 requirements dispositioned (136 covered, **23 trace-gap**) plus 25 goals / 44 known gaps; PEC 57/57 dispositioned (0 gaps).
- **Deviations:** one — report delivered as text, not as a file at the brief §8 path. No other deviation: read-only throughout, no Git/worktree changes, no contact with the other reviewer, primary checkout never read.

---

## 1. Reviewed-basis statement

**Freeze commit.** `da31c19b5656dd74615e308c4215688971d33dc9` — verified via `git rev-parse HEAD` in the detached worktree `…/scratchpad/frozen-da31c19b5`.

**Product-basis commit.** `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6` (relied on the manifest's dispatch-time verification; worked from the freeze throughout).

**Charter.** SHA-256 recomputed at freeze: `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f` — matches. Read in full (1449 lines) before any finding. Treated as **non-governing guidance**: no charter proposition is cited as evidence anywhere below.

**Brief.** SHA-256 recomputed: `f87028cef7143ce4a48cf3ccbd6c016cb226eae0dfe7411c670b1bf0a9ec9ffa` — matches.

**Manifest.** Read in full (521 lines) before any finding.

**Orientation order.** Charter → manifest → independent account from the governed records (PRDs, authority chains, decompositions, registers, decision records, receipts, SOWs, guard source) → charter as challenge set.

### Tool basis (all at the freeze commit)

`git status --porcelain` was re-checked after every execution and remained empty: **no tool wrote into the worktree.**

| Tool | Result relied on |
|---|---|
| `git rev-parse` / `show` / `log -S` / `log --format` | All blob and SHA comparisons below |
| `shasum -a 256` | Charter, brief, PRD, decomposition hashes |
| Inline `python3` (csv/hashlib/re/json; no files written) | All register parsing, pin recomputation, coverage matrices |
| `tools/coordination/validate_harness_contract_pull.py` @ freeze | **PASS, exit 0** — see A-014 for its observation boundary |
| `tools/validation/validate_path_anchors.py` @ freeze | **PASS** ("no literal home-dir absolute paths found in 1100 live path-anchor surfaces") — see A-018 for its selection boundary |

Both validators were confirmed read-only by source inspection before execution (no `open(...,'w')`, `write_text`, `mkdir`, `shutil`).

**Version-skew condition observed.** I did **not** rerun the SOW validator or `validate_decomposition_registers.py` over Root's 45 contracts. Root's 45 passed pre-v6/v6.1; a current-tool rerun would show tool drift, not falsification. Root SOW facts below are derived structurally (frontmatter parsing, cross-register comparison), which is basis-independent.

**Observation boundary (declared once; governs the whole findings register).** Confined to file content, register content, git history, and read-only tool output resolvable at `da31c19b5`. I do not observe runtime behavior, CI results, owner intent beyond what a record states, or work performed but unrecorded. "Absent" means **absent from the frozen basis**, never "was never done". Severity reflects *reliance risk at this basis*: **BLOCK** = a governed act would rely on something the basis contradicts; **REVIEW** = an owner decision is required before reliance; **WARN** = a real defect not by itself blocking reliance; **INFO** = observation of record.

## 2. Product accounts

### 2.1 Chirality Root

Root is the repository-root product. Its identity is the RD-1 ruled two-level genus at `docs/PRD_ROOT.md` §1.1 ID-0, now carried verbatim in `docs/DIRECTIVE.md` §1: the canonical human-governed application environment and generative operating form, *containing* a filesystem-native agent operating system together with the normative basis, developmental machinery, evidence, and human judgment by which that OS is formed and governed. Constituted by four functional categories (§4.1) in a generative loop whose closing step is a human judgment no agent performs (§4.2); it develops itself under the governance it prescribes (ID-1, D-GOV-21).

**Authority chain, each link verified mechanically:**

| Link | Instrument | Verification at freeze |
|---|---|---|
| PRD adopted | D-GOV-22 | Adopted bytes at `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md` hash **d85ac3f941ee…**, exactly what D-GOV-22 binds. **Verified.** |
| Adopted bytes preserved at placement | RD-4-D | `docs/PRD_ROOT.md` contains the candidate bytes **verbatim** (byte-substring test passes). Its own byte-identity claim **holds**. |
| Genus concordance | D-GOV-23 (obl. a), commit `05c18c23d` (obl. b), D-GOV-24 (obl. c) | DIRECTIVE §1 and README line 3 both carry the ruled genus. **Verified.** C-1 closed. |
| Decomposition accepted | D-GOV-25 | REF-001 pins `docs/PRD_ROOT.md`@sha256 `e98031c14b4c…` **at named basis commit `24726a73c`** — recomputed at that commit, **exact match**. |
| SOWs bound | Owner merge of PR #354 (K-AUTH-2) | 45/45 pin `…@653fabc9b3e8…` = D-GOV-25 EffectiveSHA. Uniform. **Verified.** |
| Initialization closed | D-GOV-27 | PublicationSHA `3ed5153275…` present; **EffectiveSHA unbound** (prose placeholder). |

**Current state.** 6 packages / 45 deliverables / 103 scope items (94 IN, 9 OUT) / 7 objectives. All 45 materialized with `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`; all 45 `_STATUS.md` = `INITIALIZED` with Authorization Basis and Accepted Basis SHA. `ResponsibleParty` = `Ryan Tufts` on all 45 register rows and `_CONTEXT.md` headers. AC/VER remain candidate. Open: OI-005, OI-008, OI-009, OI-011 (stale — A-006).

**Assessment.** Strongest provenance discipline of the three: single adopting instrument per stage, exact-candidate-SHA binding, immutable adopted bytes, bidirectional F4 register pair, uniform downstream pinning. Its defects are **propagation** defects — rulings that landed centrally and did not fully reach operative contracts (A-001, A-003, A-004, A-006) — plus one closure claim that outran its evidence (A-002).

### 2.2 Chirality App

A registered project loop producing the Chirality Desktop Harness: local-first Electron/Next agent harness over a user-selected working root, with a product-owned runtime contract (`AgentEnginePort`), provider adapters (Claude Agent SDK first; bounded Pi/oMLX per D-APP-72), Chirality-owned audit JSONL, capability-policy permission governance with explicit deny precedence, and — since D-APP-74/SCA-APP-004 — a Woven Dialogue information architecture.

**Authority chain — materially weaker, unverifiable at three links:**

| Link | Verification at freeze |
|---|---|
| PRD identity | **No internal version**; hash `ef638f43ccae…`; identity rests on `AUTHORITY_CORPUS.json` v17. v17's 8 pins recomputed **8/8 CLEAN**. |
| Decomposition accepted | "Gates 1-7 accepted by implicit human approval per user instruction". **No ruling file, no verbatim owner text, no date, no SHA.** |
| Decomposition ↔ PRD | REF-006 sha256 **STALE**: pinned `d9bcdcb701de…`, actual `ef638f43ccae…` since `da7ea2064`. |
| SOWs bound | 51 SOWs pin **five different** decomposition commits; **none** matches the freeze blob. |
| Lifecycle | 53/53 `_STATUS.md` = `IN_PROGRESS`; none ISSUED; F-APP-4 fences CHECKING→ISSUED. |

**Current state.** 78 scope items / 10 packages / 51 decomposition deliverables + 2 PKG-00 control = 53 live SOWs / 10 objectives. `ResponsibleParty` = `TBD` on all 51. Decision register: 74 D-APP rows, self-described "Non-governing tracking surface". Project `AGENTS.md` carries `status: draft`.

**Assessment.** App's substantive work is extensive and its scope-change discipline (SCA-APP-001…004, each with a D-APP ruling) is real. What is weak is the **identity and pinning layer**: the PRD cannot be named by version, the decomposition cannot be shown to derive from the PRD of record, the contracts cannot be shown to derive from one decomposition state, and the 159 numbered requirements have no register mapping them to deliverables. App is where my lens finds the most.

### 2.3 PEC

The optional Chirality coordination plane: a deterministic, rebuildable projection over file/Git truth plus an ephemeral presence tier, under PRD v2.1 (`de0a969cad15…`, matching the manifest prefix) and eleven invariants PEC-K-01…K-11, of which PEC-K-01 (graceful absence — "no governed act may require a PEC read or write; deleting PEC blocks nothing") is constitutive. Fenced by F-PEC-1…F-PEC-4 (D-T0-15); a distinct client of the Root runtime (D-GOV-20, D-T0-23).

**Authority chain — cleanest gate provenance of the three:** rev 1.0 accepted by D-PEC-60 with the Gate Log carrying **seven per-gate verbatim owner confirmations with dates**; rev 1.1/1.2 via SCA-001/D-PEC-61 and SCA-002/D-PEC-64. 32/32 SOWs pin `SOFTWARE_DECOMP.md@3623b958b`, whose blob is **byte-identical to the freeze** — the only fully current pin in the program.

**Current state.** 11 packages / 64 deliverables / 94 ledger rows (71 IN, 14 OUT, 9 TBD). 32 INITIALIZED with SOWs; 32 OPEN without — verified as exactly the `pre-P1`(3)+`P1`(29) vs `P2`(12)+`P3`(14)+`P4`(6) split, **zero violations**. All 64 local `Dependencies.csv` present; **254 rows, 135 ANCHOR / 119 EXECUTION** — matching the manifest exactly. `ResponsibleParty` = `TBD` on all 64.

**Assessment.** Strongest traceability in the program. Weaknesses are provenance *form* (no SHA pins on decomposition references — A-022) and a stale domain-engine profile (A-023). The deferred-SOW posture is fully substantiated and is **not** a coverage gap.

## 3. Coverage matrices

### 3.1 Root — 84 rows, complete enumeration

**Grouping rule:** none needed; the accepted forward register enumerates every addressable PRD item at row granularity. I **tested** it rather than assuming it. Dispositions are my verdict.

**Independent integrity tests (all PASS):** 0 unknown deliverable refs across 103 ledger rows; 0 unmapped IN-scope items of 94; exactly one `PackageID` per item 103/103; 0 unknown refs across 84 forward rows; reverse register = 51 = 6 packages + 45 deliverables with no orphans either direction; objective→deliverable mapping agrees across objective register, inverted deliverable register, and forward register for **7/7 objectives, 0 differences**; SOW `project_scope_refs` == register `CoversScopeItems` **0 mismatches/45**; SOW `package_objective_refs` == register `SupportsObjectives` **0 mismatches/45**.

| PRD item(s) | Kind | Disposition |
|---|---|---|
| OBJ-1, OBJ-3…OBJ-7 | objective | COVERED (9, 14, 9, 4, 3, 2 deliverables respectively) |
| **OBJ-2** | objective | **DEFERRED (partial)** — situated-working-root clause deferred by D-GOV-25 owner decision 1, recorded at §12.1 and OI-013; root half carried by DEL-03-06 |
| N-1 … N-9 | commitment | COVERED 9/9 |
| O-1 … O-10 | commitment | COVERED 10/10 |
| D-1, D-2, D-4 … D-16 | commitment | COVERED 15/15 |
| E-1 … E-8 | commitment | COVERED 8/8 |
| v1 boundary, obj-discipline, §4.1, §4.2 loop, §4.2 judgments, §4.3, §5 registry, §6.1, §6.2 ×2, §6.3, §7.1, §7.2, §8.3, §10.3 | direction (15) | COVERED 15/15 |
| §8.1 non-goals | non-goal | COVERED — **single row for the whole set** (see A-028) |
| F1 … F6 | falsifier | COVERED 6/6 |
| RD-1 … RD-5 | ruling | COVERED 5/5 |
| obligations (a)(b)(c) | obligation | COVERED 3/3 — all three **discharged in fact** (D-GOV-23, `05c18c23d`, D-GOV-24); carried as standing verification per DEC-009/OI-001 |
| §10.1 annex | obligation | COVERED |
| C-1 … C-4 | conflict | COVERED 4/4. C-1 closed by D-GOV-23; C-3 at D-GOV-22; C-2 corrected at `941221cfc` (verified: CONTRACT now reads 34/13 and holds exactly 34 IDs across 13 subsections); **C-4 correction incomplete — A-002** |

**Root totals: 84/84 dispositioned — 83 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL, 0 GAP.** F4 closes both directions; I confirmed it independently.

### 3.2 App — full coverage

**Grouping rule (stated explicitly).** App has **no forward-coverage register and no reverse-trace register** — no artifact maps a requirement to a deliverable. I built the matrix from the only two surfaces carrying PRD→work linkage: (i) PRD §16 Execution Package Traceability Summary (PRD-side, FR/NFR/Goal/KG ranges), and (ii) the decomposition SSOW `SourceRef` column (decomposition-side, source document + section). I enumerate every family completely and group by **defining PRD section**, because that is the granularity at which the decomposition side actually traces. COVERED = cited by ID in §16 **or** defining section cited in the SSOW; TRACE-GAP = neither.

| PRD block | n | §16 by ID | SSOW section | Disposition |
|---|---|---|---|---|
| §8.1–§8.5, §8.7–§8.15, §8.17 (FR) | 106 | yes | yes | COVERED |
| §8.6 Attachments (FR-036–040) | 5 | **no** | yes | COVERED (section only) |
| §8.16 Runtime engine boundary (FR-122–128) | 7 | yes | **no** | COVERED (§16 only) |
| FR-103–105 extensibility | 3 | roadmap row only | no | COVERED (weak) |
| **§11.1 Security & privacy** (NFR-001–007, 028–030) | 10 | partial (006,007,028–030) | **no** | **PARTIAL TRACE-GAP** (001–005) |
| **§11.2 Reliability** (NFR-008–013) | 6 | partial (010,013) | **no** | **TRACE-GAP** (008,009,011,012) |
| **§11.3 Performance** (NFR-014–018, 031) | 6 | partial (031) | **no** | **TRACE-GAP** (014–018) |
| **§11.4 Accessibility/UX** (NFR-019–022) | 4 | **no** | **no** | **TRACE-GAP** (all 4) |
| **§11.5 Auditability & compliance** (NFR-023–027) | 5 | **no** | **no** | **TRACE-GAP** (all 5) |
| §3.1 Product Goals 1–25 | 25 | 11 of 25 | n/a | 14 untraced by ID |
| §3.2 Non-Goals (~27 bullets) | 27 | via PKG-01 | 4 OUT items + 3 §3.2 rows | COVERED (block-level) |
| §15 Known Gaps KG-001–044 | 44 | 27 of 44 | n/a | 17 untraced by ID |

**App totals: 159 requirements — 136 COVERED, 23 TRACE-GAP** (NFR-001–005, 008, 009, 011, 012, 014–027). Deterministic corroboration: the string `NFR` occurs **0 times** in the entire accepted decomposition. Recorded as a **trace** gap, not a scope gap — substantive work plainly exists (DEL-09-06, DEL-05-02/03).

### 3.3 PEC — 57 IDs, complete enumeration

**Integrity tests (all PASS):** 0 unknown deliverable refs across 94 ledger rows; 0 IN-scope items without a deliverable; 23 rows with blank `PackageID` = exactly the 14 OUT + 9 TBD (base-standard behavior — A-029).

| Family | n | Cited in `ScopeLedger.SourceRef` | Disposition |
|---|---|---|---|
| PEC-ORI, RCN, GAT, PRS, STR, API, DSH, SVC | 46 | 46/46 | COVERED |
| PEC-K-01…K-11 | 11 | K-10 + K-01,02,04–09 in ledger fields; **K-03, K-11 not in ledger** | COVERED — K-03 → hard constraint **C3**; K-11 → **C15** (added by the Phase-2 adversarial verification, DL-9, which recorded "PEC-K-11 unrepresented" and fixed it) |

**PEC totals: 57/57 dispositioned — 0 gaps.** The 32 absent P2–P4 SOWs are verified deliberate sequencing.

## 4. Boundary and ownership matrix (cross-product)

| Shared function | Semantic owner | Producers | Consumers | Authoritative record | Compatibility obligation | Fallback / degraded | Routed change path |
|---|---|---|---|---|---|---|---|
| **Shared runtime** (`runtime/`) | **Root** — PRD O-2(c) places the executable substrate in the operative product; `AGENTS.md` §Shared Runtime Doctrine; D-GOV-20 | Root `runtime/`; `@chirality/runtime-contracts` | App, PEC (D-T0-23), CLI, future domain apps | D-GOV-20; `runtime/README.md`; `AGENTS.md` | "transport never grants project authority"; adapters retain own gates/permissions/data boundaries/evidence | **UNKNOWN** — no record states client behavior when the daemon is absent or version-incompatible | Root governance + M2 |
| **Work-surface / UI** | **App**, for its own product. A *reusable* surface as a separate owned function: **UNKNOWN** | App PKG-02 | App users; potential embedded/sidecar consumers | App PRD §8.1–8.2; PKG-02; D-APP-74 | PKG-02 exclusions: shell "owns presentation only" | Legacy loop-first UI retained; "do not retire without a separate owner decision" (KG-033) | App PRD / SCA-APP-* + D-APP ruling |
| **Coordination projection** | **PEC** | PEC reconciler over file/Git truth | Harnesses at moments of consequence (PEC-K-03) | PEC PRD v2.1; PEC-K-01…K-11 | PEC-K-04: every response carries examined-through SHA + per-feed freshness | **Fully declared, strongest in program** — PEC-K-01 graceful absence + kill test every release; PEC-K-11 zero-coordination modes zero-contact | PEC PRD / SCA + D-PEC ruling; F-PEC-1…4 |
| **Dependency truth** | **Deliverable-local registers** (K-DEP-1/2; PRD O-8) | Each `Dependencies.csv` | Aggregators, blocker computation, work graphs | `docs/CONTRACT.md` K-DEP-1/2; PEC: 64 registers, 254 rows, **no central register by owner decision** | "No central dependency graph is *authoritative*"; derived graphs lawful | Advisory blocker state (24 BLOCKED/40 UNBLOCKED) is "visibility, not work authority" | CONTRACT amendment (M2); per-project for storage |
| **SOW method layer** | **Root** | `skills/scope-of-work/`, `tools/scope_of_work/`, `validate_decomposition_registers.py`, the SOW standard | Root 45, PEC 32, App 53 | D-GOV-15, D-GOV-16 | method v1→v6.1; **corpus split across validation eras** | Historical validation remains accepted | Root governance (D-GOV-15/16) |
| **Authority-corpus pinning** | **Each consuming loop** | App `AUTHORITY_CORPUS.json` v17 (D-APP-38 Option D); `domains/*/Source_Manifest.csv` | App reconciliation; domain packs | D-APP-38; per-manifest | loops re-pin on own cadence; notices are coordination not authority | corpus-drift status is the detector | owning loop's instruments |
| **Notice routing** (D-11) | **Root** (rule owner); **each receiving loop** (disposition) | Root tranches emit `NOTICE_*` | app-dev, domains/chirality, pec, piping | `AGENTS.md` §Governance Integration Rules; PRD D-11; D-GOV-21 M6 | "coordination, not authority: the receiving loop adopts, amends, or declines" | each loop's own corpus-drift check | Root `AGENTS.md` (M2) |
| **Domain-engine profiles** | **Tier-0 / `_DomainEngines/`** | `profiles/*.yaml` | domain engines; PEC | `_DomainEngines/_DECISIONS/_REGISTER.md` (23 records, verified) | K-DOMAIN-1: engines own domain truth | `pec.yaml` binds only the **frozen v0.4 instance**; supersession "a planned act" | D-T0 decision |
| **Resource governance** | **Not owned — does not exist in the basis** (charter-only candidate) | — | — | — | — | — | Would require a PRD amendment. **Absence is not a scope gap.** |

**Duplicate-ownership check.** No shared function has two claimed semantic owners at the freeze. The one genuinely undetermined ownership is the *reusable* work surface — recorded UNKNOWN and routed as an owner-decision request (§7), not as a gap.

## 5. Findings register

### ROOT

**A-001 · ROOT · trace gap · REVIEW · HIGH**
**Assertion.** The instruction-surface enumeration governing write-locus boundaries in Root's operative contracts omits `CLAUDE.md`, though D-GOV-26/27 ruled the authoritative enumeration to be `docs/SPEC.md` §0.2.1's eight members including it.
**Evidence.** SPEC §0.2.1 line 44 lists eight: `AGENTS.md`, `CLAUDE.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`. Against this: decomposition §9 preamble enumerates seven (has `.github/workflows/`, omits `CLAUDE.md`); **45/45** `_CONTEXT.md` carry the seven-member list (45/45 include `.github/workflows/`, **0/45** include `CLAUDE.md`); of 45 SOWs, 36 carry an enumeration, 31 include `.github/workflows/`, **0 include `CLAUDE.md`**; only 2 of 45 SOWs mention `CLAUDE.md` at all. The guards are correct: `validate_root_surface_ownership.py:103`, `validate_root_work_graph_dispatch.py:109`, `validate_instruction_tranche_manifest.py:127` each define `INSTRUCTION_SURFACE_FILES = ("AGENTS.md", "CLAUDE.md")`.
**Consequence.** D-GOV-26 item 2 ruled two additions in one act; only one propagated. Every contract's "any locus naming the instruction surface … requires an independently authorized M2 tranche" clause under-states the protected set. An executor reading only its contract would not know that editing `CLAUDE.md` — which determines what every session loads — is an M2 act. The machine gate is stricter than the written authority, inverting the intended relation and making conformance depend on the guard rather than the contract.
**Smallest action / owner.** One corrective tranche adding `CLAUDE.md` to the decomposition §9 preamble, the 45 `_CONTEXT.md` boilerplate, and the 36 SOW write-locus paragraphs. Root loop; M2 where root `docs/` is touched, execution-tree otherwise. No register or ID change.

**A-002 · ROOT · authority conflict · REVIEW · HIGH**
**Assertion.** C-4 is recorded as closed, and "every conflict the adopted PRD surfaced (C-1..C-4) is resolved" is asserted of record, but the divergence C-4 names is still present.
**Evidence.** PRD §10.2 states C-4 as "`README.md`'s **public-export section** omits `runtime/`, which the export profile's root-directory allowlist includes." At the freeze: `export_public.py` `ROOT_DIRS` (lines 34–42) includes `"runtime"`; `README.md` "## Public Export Boundary" list (lines 178–185) has no `runtime/`. Commit `941221cfc` added `runtime/` only to the *root-surface directory table* (line 63) and the *summary sentence* (line 5). Receipt 44 states "**C-4 CORRECTED (this commit)**" and "**With C-2 and C-4 closed, every conflict the adopted PRD surfaced (C-1..C-4) is resolved.**" README is now also internally inconsistent: line 63 says `runtime/` is "Included in the public export" while the export-boundary section omits it.
**Consequence.** A closure claim of record does not satisfy its own stated condition. OBJ-1's v1 condition is "No ratified clause has an unrecorded conflicting live variant"; the variant is now *recorded as resolved*, which is worse than being recorded open, because closure suppresses the standing verification DEL-01-08 would perform. C-2's half of the same commit **does** verify (CONTRACT reads 34/13 and holds exactly 34 IDs across 13 subsections), so this is partial execution, not fabrication.
**Smallest action / owner.** Add `runtime/` to README's Public Export Boundary list; append a correcting line to Receipt 44 or a new receipt. README is non-binding, so the PR merge is the gate — the same vehicle as the original correction. Root loop / CHANGE.

**A-003 · ROOT · trace gap · REVIEW · HIGH**
**Assertion.** Four Root SOWs declare objective references unsupported by the decomposition state at the `decomposition_basis` SHA they pin, and no successor SHA exists to repin to because D-GOV-27's EffectiveSHA is unbound.
**Evidence.** The four contracts amended by commit `3ed515327` now carry DEL-01-04 `[OBJ-002, OBJ-003]`, DEL-03-01 `[OBJ-004, OBJ-007]`, DEL-03-06 `[OBJ-002, OBJ-004]`, DEL-06-04 `[OBJ-004, OBJ-005]`, while all four still pin `…@653fabc9b3e8…`. Diffing the decomposition blob at `653fabc9b` vs the freeze shows 7 hunks — exactly the DEC-021 additive propagation; at `653fabc9b`, DEL-01-04's `SupportsObjectives` is `OBJ-002` only. `D-GOV-27_initialization_closing_rulings.md:6` records `EffectiveSHA: (merge of the closing-tranche PR into main; backfilled by a later tranche per precedent)` — a prose placeholder.
**Consequence.** Compounds disclosed conditions 1 and 3 into a defect neither describes alone. `decomposition_basis` is the mechanism making a contract's scope checkable; for these four it no longer does, and the unbound EffectiveSHA means the correct repin target does not exist as a citable value. Any deterministic basis-currency check will either pass falsely (comparing to the pinned commit) or fail with no remedy available.
**Smallest action / owner.** Backfill D-GOV-27's EffectiveSHA in the next tranche (already owed per Receipt 52), then repin the four contracts. Root loop; follows the established `f1549afb1` precedent, no new ruling needed.

**A-004 · ROOT · semantic conflict · WARN · HIGH**
**Assertion.** DEC-021 states the D-GOV-27 propagation updated "this surface's two tables"; the §7 objective table was not fully updated.
**Evidence.** Machine comparison of §7, the §9 deliverable tables, and the objective register: OBJ-001/002/003/005/006/007 agree across all three (9, 8, 14, 4, 3, 2). **OBJ-004 does not**: objective register 9, §9 tables 9, **§7 table 8 — missing `DEL-06-04`**. DEL-06-04's §9 row correctly reads `OBJ-004, OBJ-005`.
**Consequence.** The authoritative companion registers are correct (§3 makes them authoritative for their data), so no downstream mapping is wrong. The defect is that the accepted working surface contradicts its own change-log entry on a ruled propagation, and a reader orienting from §7 would under-count OBJ-004's coverage. DEC-021's completeness claim is not verifiable as written.
**Smallest action / owner.** Add `DEL-06-04` to the §7 OBJ-004 row. Execution-tree edit, no M2, no register change. Root loop.

**A-005 · ROOT · semantic conflict · WARN · HIGH**
**Assertion.** The accepted decomposition's header assigns "EffectiveSHA" to a commit the accepting decision assigns a different role, contradicting PRD E-3 on the very artifact E-3's deliverable governs.
**Evidence.** Decomposition line 9: `**EffectiveSHA:** ea0ad7a566… (merge of PR #347)`. `D-GOV-25` lines 5–8 assign four roles: `AcceptedCandidateSHA ec62af070…`, `CandidateMergeSHA ea0ad7a566…` ("merge of PR #347"), `PublicationSHA ed5dc0a87…`, `EffectiveSHA 653fabc9b…` ("merge of PR #348"). PRD E-3 requires the three SHA roles be "distinct and recorded distinctly"; its carrying deliverable is `DEL-05-03_SHA_Role_Register`.
**Consequence.** The artifact most read for the Root basis mislabels a load-bearing SHA's role. All 45 SOWs pin `653fabc9b` — the correct value — so operative pinning is unaffected; the risk is a reader citing `ea0ad7a56`. It is a live counter-example to a commitment the same package establishes, which is what DEL-05-03's standing verification should catch.
**Smallest action / owner.** Correct line 9 to `CandidateMergeSHA` and add the `EffectiveSHA 653fabc9b…` line citing D-GOV-25. Execution-tree edit; within DEL-05-03's declared scope. Root loop.

**A-006 · ROOT · semantic conflict · WARN · HIGH**
**Assertion.** After D-GOV-27 assigned `ResponsibleParty = Ryan Tufts`, 91 governed surfaces still assert the opposite, and 45 instruct downstream work to preserve the superseded value.
**Evidence.** Assigned: deliverable register 45/45 `Ryan Tufts`; every `_CONTEXT.md` header `**Responsible:** Ryan Tufts`. Contradicting at the same freeze: (a) decomposition §9 — "`ResponsibleParty` is `TBD` for every deliverable — this run holds no assignment authority (OI-011)"; (b) §12 OI-011 `OPEN` — "`ResponsibleParty` is `TBD` throughout"; (c) §14 — executors should "preserve `ResponsibleParty: TBD` until a human assigns it"; (d) **all 45** `_CONTEXT.md` footers — "Downstream work must preserve `ResponsibleParty: TBD` until a human assigns ownership" (each file contradicting its own header); (e) **34 of 45** SOWs assert it remains TBD (e.g. DEL-01-01 AX-005).
**Consequence.** Disclosed condition 4 is **materially worse than described**: not one stale row but 91 surfaces, 45 carrying an *instruction* to preserve the superseded value. An executor following its `_CONTEXT.md` footer would revert the owner's accountability assignment. Accountability attribution is what RD-2's B2 makes load-bearing, so this is not cosmetic.
**Smallest action / owner.** One propagation tranche: close OI-011 citing D-GOV-27, correct §9 and §14, replace the `_CONTEXT.md` footer sentence and the 34 SOW clauses. Execution-tree only. Root loop.

**A-007 · ROOT · omission · WARN · HIGH**
**Assertion.** The D-GOV register's D-GOV-26 row repeats a section reference the D-GOV-26 record expressly corrected.
**Evidence.** `_REGISTER.md:39`: "`.github/workflows/` added to the SPEC **§0.2.2** instruction-surface enumeration". `D-GOV-26_owner_gated_closeout.md` lines 36–43 records the opposite as a fan-in correction: the recommendation "said '§0.2.2', but the instruction-surface enumeration lives at `docs/SPEC.md` **§0.2.1** (line 44); §0.2.2 carries only the narrower working-root write-prohibition list … and §0.2.2's prohibition list was deliberately not expanded."
**Consequence.** Low direct risk — PRD D-1 makes the register navigational and records governing. Recorded because it is the register-vs-record divergence class D-1 exists to bound, on the exact label the record fixed. Note I verified §0.2.2's narrower list is **deliberate**, so the §0.2.1/§0.2.2 asymmetry is **not** a finding.
**Smallest action / owner.** Amend the register row to §0.2.1. Root loop / CHANGE.

**A-008 · ROOT / CROSS_PRODUCT · trace gap · WARN · HIGH**
**Assertion.** The D-GOV-18 ORCHESTRATOR→PROJECT_SETUP rename never propagated to the `domains/chirality` authority-reference corpus, which still pins the retired file as ACTIVE and has no row for its successor or two other live agent contracts.
**Evidence.** `domains/chirality/_Sources/Source_Manifest.csv` row `SRC-AGENTS-AGENT-ORCHESTRATOR`: `agents/AGENT_ORCHESTRATOR.md`, `IncludeInIndex YES`, `ArchiveState ACTIVE`, `ExpectedSha256 5182e82c…` — file absent at the freeze. `agents/AGENT_PROJECT_SETUP.md` exists; manifest contains **0** `PROJECT_SETUP` rows. 33 live `agents/AGENT_*.md`; unpinned live files: `AGENT_PROJECT_SETUP.md`, `AGENT_RESEARCH.md`, `AGENT_RESEARCHER.md`. The `AGENT_SCHEDULING` row's note ("scheduling workflow moved to ORCHESTRATOR") is doubly stale. `AGENTS.md` lists all three as live. No D-GOV-18 notice in `domains/chirality/_Coordination/` (its four notices are D-GOV-21, D-GOV-23, D-GOV-24, and an AGENT_CHANGE merge-verdict notice).
**Consequence.** A live instance of the D-11 change-notice rule not firing. D-GOV-18 renamed a file in `agents/` — a surface this pack demonstrably pins — and the rule requires a routed notice *in the same tranche*. The pack's ACTIVE pin now points at nothing while three live contracts are invisible to it.
**Smallest action / owner.** Route a D-GOV-18 notice to `domains/chirality/_Coordination/`; the pack re-pins on its own cadence. Root loop for the notice; `domains/chirality` for the manifest.

**A-009 · ROOT · observation · INFO · HIGH**
**Assertion.** `AGENTS.md` contains no reference to the accepted Root decomposition, its packages, deliverables, or the materialized execution tree.
**Evidence.** `grep -c` over `AGENTS.md`: `PKG-0` → **0**; `DEL-0` → **0**; `execution/` → **0**.
**Consequence.** Confirms disclosed condition 7. Under my lens: K-AGENTS-1 makes `AGENTS.md` an authoritative governance surface and PRD O-3/O-5 incorporate membership *by reference to it*, yet a reader orienting from the instruction surface cannot reach the accepted decomposition; discoverability (OBJ-1) currently depends on `LOOP_INIT.md`, a coordination surface carrying no authority merely by existing (D-7). An orientation gap, not a conformance failure — nothing requires `AGENTS.md` to enumerate deliverables.
**Smallest action / owner.** Owner decision: add a pointer (M2 tranche) or record that discoverability is deliberately routed through `LOOP_INIT.md`. Both lawful; I recommend neither.

**A-010 · ROOT · observation · INFO · HIGH**
**Assertion.** Candidate AC/VER status is expressed across the 45 contracts in at least 87 distinct prose formulations with no metadata field, and the marker token is overloaded, so no reliable text proxy exists either.
**Evidence.** SOW frontmatter is uniform with exactly six keys across 45/45 — `schema`, `deliverable_id`, `package_id`, `decomposition_basis`, `project_scope_refs`, `package_objective_refs`. **No status or candidate field.** Extracting every sentence containing "candidate"/"CANDIDATE" yields **87 distinct sentences**; the most frequent appears 5 times. Every SOW marks candidacy somewhere (0 unmarked), but the token also denotes: the exact-candidate-SHA procedure, an "M2 tranche candidate", a promotion candidate, a "candidate weakening" of governance, and "lower or candidate document" in the authority-chain clause.
**Consequence.** Confirms and deepens disclosed condition 8: the status is not merely machine-opaque but **not recoverable by text matching**, since a grep for the marker returns mostly false positives. Any future deterministic AC/VER gate must add a field. Positively, no contract omits the marking.
**Smallest action / owner.** If a deterministic gate is wanted, add one frontmatter field. That amends `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` — Root governance (D-GOV-16 lineage), M2. **Routed as an owner-decision request, not asserted.**

**A-011 · ROOT · observation · INFO · HIGH**
**Assertion.** Root's PRD immutability and adoption chain verifies end to end.
**Evidence.** Adopted bytes sha256 `d85ac3f941ee…` = exactly what D-GOV-22 binds. `docs/PRD_ROOT.md` contains those bytes **verbatim** as a byte-substring, so its byte-identity claim holds. REF-001's PRD pin `e98031c14b4c…` recomputes exactly at its named basis commit `24726a73c`. All 45 SOWs pin one decomposition SHA.
**Consequence.** The control case making A-013 and A-016 meaningful: D-13's "adopted bytes are never overwritten at their path" is mechanically verifiable here, and Root demonstrates a fully checkable PRD→decomposition→SOW chain is achievable within this method.

### APP

**A-012 · APP · trace gap · REVIEW · HIGH**
**Assertion.** None of the 31 App NFRs has a trace to any scope item, package, or deliverable in the accepted decomposition, and 23 of 31 have no ID-level trace on either side.
**Evidence.** `grep -c "NFR"` over the decomposition = **0**. No SSOW `SourceRef` cites `REF-006 Section 11` (inventory contains REF-006 §3.2, 6.2, 6.4, 8.1–8.15, 8.17, 15 — no §11.x). §16 cites only NFR-006, 007, 010, 013, 028, 029, 030, 031 = 8 of 31. Untraced on both sides: NFR-001–005, 008, 009, 011, 012, 014–027 (**23**). Whole subsections untraced: §11.4 Accessibility and UX Quality and §11.5 Auditability and Compliance have **zero** ID citations anywhere.
**Consequence.** A trace gap, not necessarily a scope gap — substantive work exists (DEL-09-06; DEL-05-02/03). But no instrument establishes which deliverable discharges which NFR, so no reviewer can determine whether an NFR is covered, deferred, or dropped, and no deliverable acceptance can be said to have accepted an NFR. §11.5 Auditability is the most consequential block to leave untraceable, since auditability is what the program's reliance argument rests on. The structural cause: App is the only product with **no forward-coverage and no reverse-trace register**; its telemetry (`UnassignedScopeItems 0`, etc.) measures decomposition-internal completeness and says nothing about PRD coverage.
**Smallest action / owner.** Extend the SSOW `SourceRef` (or add rows) so PRD §11.1–§11.5 are cited, and record any NFR judged out of current scope as an explicit deferral. Decomposition repair within existing topology — no new requirement, no renumbering. App loop via SCA-APP-* with a D-APP ruling. **This creates no commitment**; the NFRs are already admitted PRD content.

**A-013 · APP · trace gap · REVIEW · HIGH**
**Assertion.** The 51 decomposition-derived App SOWs pin five different decomposition basis commits, none matching the accepted decomposition's content at the freeze.
**Evidence.** `decomposition_basis` across 53 SOWs: `@2770fda4c` (6), `@0724f26f6` (10), `@b4d2c9ab2` (15), `@ff59428ff` (14), `@416b29033` (6); plus 2 PKG-00 SOWs pinning `PKG-00…/README.md@0724f26f6`. Decomposition blob at freeze = `b3af4ed677…`; the blob at each pinned commit **differs**. Dates: `2770fda4c` 2026-07-12; `0724f26f6`/`b4d2c9ab2`/`ff59428ff` 2026-07-13; `416b29033` 2026-07-23. PKG-02 is itself split (DEL-02-01/02/04 @ `416b29033`; DEL-02-03/05 @ `0724f26f6`). Contrast Root 45/45 and PEC 32/32 on single pins.
**Consequence.** No single accepted basis exists against which the App deliverable corpus can be stated. 45 of 51 contracts predate SCA-APP-003 (shared-runtime extraction) and SCA-APP-004 (Woven Dialogue IA) — the two amendments that most changed what packages mean — so those contracts were written against a decomposition whose PKG-02 scope and deliverable names have since been rewritten. Because the decomposition is amended **in place** with no revision bump, a reader cannot tell from a pin which content it names without git archaeology. This is App's analogue of the M3 frozen-basis mechanism, and it is not holding.
**Smallest action / owner.** Repin all 53 to one current decomposition commit in a single tranche and record in the change log which SOWs were authored under which prior state. No scope/topology/ID change. App loop; the repin needs no new ruling, but re-verifying the 45 pre-SCA contracts against current PKG-02/PKG-05 semantics is an owner-gated judgment.

**A-014 · APP / CROSS_PRODUCT · authority conflict · REVIEW · HIGH**
**Assertion.** The registered validator for the D-APP-48 Flow-A pull contract returns PASS while all 12 of its SHA pins are stale, because it verifies content at the pinned commit rather than in the working tree.
**Evidence.** Recomputing the 12 `exports[].sha256` values in `D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json` against live files: **CLEAN 0 / STALE 12 / MISSING 0**. Running the contract's own declared command at the freeze prints "harness contract pull validation passed", exit 0. Source explains it: line 31 `git_blob(repo_root, commit, repo_path)` reads content **at `source.commitSha = 55a066fdf…`**, and line 93 compares the manifest hash to that historical content. Live files are deprecation shims, e.g. `src/agent-engine-port.ts` in full: `/** @deprecated Import from '@chirality/runtime-contracts/agent-engine-port'. */` + `export * from '@chirality/runtime-contracts/agent-engine-port';`.
**Consequence.** The validator is not defective — within its boundary it correctly verifies manifest↔pinned-commit consistency. The defect is **reliance**: this is the contract by which `projects/chirality-piping` consumes the Flow-A spine (D-APP-48, D-T0-09), its PASS is the evidence a consumer would cite for currency, and that PASS is invariant under arbitrary drift of the files it names. D-GOV-02's own rule is that a result is bounded to its declared observation boundary; here the boundary is not declared in the contract, so a consumer cannot know the PASS says nothing about the live package. The sharpest instance in the corpus of a machine gate's output being available to carry more assurance than it holds.
**Smallest action / owner.** Either add a live-tree comparison mode and declare both boundaries in output, or state the observation boundary explicitly in the pull-contract JSON and any evidence citing it; then repin or formally retire the contract given the shared-runtime rehome. App loop with Tier-0 concurrence (D-T0-09 owns the contract version); piping is an affected consumer and should receive a routed notice.

**A-015 · APP · authority conflict · REVIEW · HIGH**
**Assertion.** The App decomposition's seven-gate acceptance rests on "implicit human approval" of 2026-05-20 and has never been re-gated across four subsequent in-place amendments.
**Evidence.** Line 9: "Gates 1-7 accepted by implicit human approval per user instruction"; §1 Gate Log records all seven `PASSED` with **no owner quote, no per-gate date, no SHA**; DEC-002 confirms. No gate-acceptance ruling file exists. The document has since been amended in place four times — DEC-017/SCA-APP-001 (2026-06-13), DEC-018/SCA-APP-002 (07-21), DEC-019/SCA-APP-003 (07-22), DEC-020/SCA-APP-004 (07-23) — Gate Log unchanged, header date still 2026-05-20. Contrast PEC (seven verbatim owner confirmations with dates) and Root (seven gates ruled together by D-GOV-25 against an exact candidate SHA with the ruling recorded verbatim).
**Consequence.** Disclosed condition 8 is **worse than described**: the weakness is not only the vehicle but its *currency* — the acceptance attaches to a state superseded four times, including amendments that rewrote a package's entire scope description (PKG-02 under SCA-APP-004). Under K-AUTH-2 an approval binds to content and is voided by content change; there is no SHA here for it to bind to, so whether the gates still hold cannot be answered from the basis. Each SCA carried its own D-APP ruling, which materially mitigates this — the amendments are not ungoverned — but no ruling re-affirms the gates.
**Smallest action / owner.** One owner act recording that Gates 1–7 hold for current content at a named SHA, or identifying which require re-running after SCA-APP-003/004. App loop, D-APP ruling. No re-decomposition implied.

**A-016 · APP · trace gap · WARN · HIGH**
**Assertion.** The App decomposition's pin for its sole product-requirements source is stale by one PRD revision.
**Evidence.** REF-006 pins `docs/PRD.md` at `d9bcdcb701de…`; actual at freeze is `ef638f43ccae…`. REF-001–005 and 007 recompute **CLEAN**. Git bisection: at `a02d92f8e` (07-23) pin and actual both `d9bcdcb701de0894`; at `da7ea2064` (07-24) the PRD moved to `ef638f43ccae1cd7` and REF-006 was not updated; divergence persists at the freeze. `da7ea2064` is also the commit that bumped the corpus to v17 — so the loop's corpus mechanism tracked the change while the decomposition's reference table did not.
**Consequence.** Bounded, and I state the bound rather than inflating it: diffing requirement sets across the untracked revision shows **no requirement added or removed** (159 → 159). The single change was one row in §15 narrowing KG-033. So the coverage claim is not substantively invalidated. The real consequence is mechanical: the pin makes derivation checkable, it has failed once silently, and because the decomposition is amended in place it will fail the same way on a larger delta. Severity WARN for this instance; the risk is the mechanism.
**Smallest action / owner.** Update REF-006 to `ef638f43ccae…` and add the currency check to the tranche checklist. App loop; no ruling needed for a pin refresh changing no scope.

**A-017 · APP · omission · WARN · MEDIUM**
**Assertion.** The required companion invariant-coverage register does not exist and no deferral ruling records its absence; whether the obligation is yet breached depends on whether REVIEW closure has occurred, which the basis does not settle.
**Evidence.** §2.2 declares `contract_invariant_coverage_register.csv` a "Planned authoritative companion register" that "must be created or explicitly deferred **before REVIEW closure**"; §10B repeats it; DEC-011/DEC-015 confirm. `ls .../execution/_Decomposition/` returns **only the .md** — no CSV companions. No deferral ruling found in the D-APP register.
**Consequence.** Confirms disclosed conditions 9 / App-4, with two mitigations I verified: (i) §10A.1 carries **family-level** invariant ownership mapping every `K-*` family to primary packages, so coverage is absent at member granularity, not wholly; (ii) the obligation is conditioned on "before REVIEW closure", and the latest coverage package closes with WARNINGS at `READY_FOR_IMPLEMENTATION_HANDOFF`, which is not that act. **MEDIUM confidence** because the basis cannot tell me whether REVIEW closure occurred; if not, the obligation is pending, not breached.
**Smallest action / owner.** Create the register or record an explicit deferral with a resolution condition — the decomposition names both as acceptable. App loop; a deferral needs a D-APP ruling, creation does not.

**A-018 · APP · overreach · WARN · HIGH**
**Assertion.** The accepted App decomposition embeds a machine-absolute path in its header, and no registered check covers that surface.
**Evidence.** Line 8: `**Method Reference:** /Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` — the only `/Users/ryan` occurrence across the three products' `_Decomposition/` trees. Root PRD O-6 and SPEC §0.2.4 require that instruction, coordination, and plan files embed no machine-absolute paths. `validate_path_anchors.py` returns **PASS** over 1100 surfaces; its `is_live_surface` selector (lines 68–99) admits, under `projects/`, only `projects/<name>/init/**.md` and exactly 5-part `projects/<name>/execution/_Coordination/<ACTIVE_COORDINATION_FILES>` — so `projects/*/execution/_Decomposition/*.md` is outside its boundary. The path is also stale (`ai-env/projects/chirality` is not this layout).
**Consequence.** The PASS is correct within its boundary — **not** a validator defect, and I record it as such. The finding is the embedded path plus the fact that no deterministic check would surface it, leaving human reading as the only detection route. With A-014, the second case where a green check does not mean what a reader would naturally take it to mean.
**Smallest action / owner.** Replace line 8 with the repo-relative `agents/AGENT_SOFTWARE_DECOMP.md` (already REF-007's path). App loop. Optionally route an owner-decision request to extend the path-anchor selector — **a proposal, not an assumed requirement**.

**A-019 · APP · ownership gap · WARN · HIGH**
**Assertion.** No App deliverable has an assigned responsible party, and the decomposition instructs downstream execution to keep it that way.
**Evidence.** `ResponsibleParty` = `TBD` on **51/51** rows in §8. §13: agents "should execute one deliverable at a time, **preserve the `ResponsibleParty: TBD` field until a human assigns ownership**." All 53 `_STATUS.md` are `IN_PROGRESS`. (PEC is 64/64 `TBD` too — but PEC's deliverables are pre-production; App's are all in progress.)
**Consequence.** App is the only product with work formally in progress and no accountable party on any unit. RD-2's B2 means accountability is not undefined at root level, so this is an attribution gap at unit level — which matters because F-APP-4 fences CHECKING→ISSUED and issuance is where an accountable human must be identifiable. Root closed the equivalent gap via D-GOV-27; App has not.
**Smallest action / owner.** One owner act assigning `ResponsibleParty` across the register (D-GOV-27 is the precedent and pattern), plus updating §13. App loop, D-APP ruling.

**A-020 · APP · authority conflict · WARN · HIGH**
**Assertion.** Notice-routing determinations in the App/Root seam are unstable: two receipts in the same Root loop reach opposite conclusions about what the App corpus pins, and the notice shipped states a consequence that is false at the freeze.
**Evidence.** `NOTICE_2026-07-25_CONTRACT_INDEX_CORRECTION.md` states "The `AUTHORITY_CORPUS.json` sha256 pin for `docs/CONTRACT.md` is now stale and re-pins on this loop's own cadence." Receipt 44 gives the same premise as justification ("its `AUTHORITY_CORPUS.json` pins CONTRACT"). But all 8 v17 pins recompute **CLEAN**, because `docs/CONTRACT.md` in the corpus resolves to `projects/chirality-app-dev/docs/CONTRACT.md` (App's own governance document), not root `docs/CONTRACT.md`. Receipt 52's M6 survey reaches the correct conclusion — "app-dev corpus pins resolve to project-local docs copies, verified by hash" — and returned `none-required` for D-GOV-27.
**Consequence.** Harmless in direction here (an unnecessary notice; a notice is coordination, not authority). The finding is the **mechanism**: whether a downstream loop pins a touched surface was determined twice by hand with opposite results within one day and one loop. D-11 makes routing a same-tranche obligation, so the determination is on the critical path; an error the other way is under-notification, which is silent — A-008 is exactly that. Structurally: because App's corpus pins **zero** root governance documents (only two root agent-instruction files, both CLEAN), its corpus-drift check cannot detect root DIRECTIVE/CONTRACT/SPEC/TYPES changes at all.
**Smallest action / owner.** Derive the M6 pin survey mechanically from each loop's manifest (resolving relative paths) rather than by hand; correct the shipped notice's "now stale" sentence. Root loop.

**A-021 · APP · observation · INFO · HIGH**
**Assertion.** The App project agent overlay operates as an active instruction surface while marked `draft`, and the decision register self-describes as non-governing.
**Evidence.** `projects/chirality-app-dev/AGENTS.md` frontmatter: `status: draft`, `created: 2026-06-15`, `doc_kind: governance.agent_index`. `_DECISIONS/_REGISTER.md:4`: "**Status:** Non-governing tracking surface." 74 distinct D-APP IDs verified.
**Consequence.** Confirms disclosed condition App-11. The register's self-description is correct and healthy — it mirrors Root's D-1 discipline. The `draft` overlay is the live issue: it maps the general agent framework onto the App loop, and a `draft` label on an operative instruction surface makes its authority status unresolvable from the file itself.
**Smallest action / owner.** Flip `status` or record why `draft` is intended. App loop.

### PEC

**A-022 · PEC · trace gap · WARN · HIGH**
**Assertion.** The accepted PEC decomposition pins none of its references by content hash, so derivation from PRD v2.1 cannot be verified against exact bytes.
**Evidence.** §1.5 References R1–R9 carry `Ref | Path | Role` only — **no SHA-256, no basis commit**. R1 identifies the source as "`projects/pec/docs/PRD.md` (v2.1; v2.0 adopted 2026-07-24 by `D-PEC-58`, directed-bootstrap clarification adopted by `D-PEC-61`)". Contrast Root (sha256 + basis commit, verified) and App (sha256, six clean one stale).
**Consequence.** PEC substitutes versioned identity plus adoption instruments for byte pinning — materially better than App (whose PRD has no version at all), and PEC's PRD carries internal version 2.1 with two adopting decisions, so identity is determinate. What is lost is falsifiability: if the PRD were edited without a version bump, nothing in the decomposition would detect it, whereas Root's pin would. A gap in one layer of an otherwise exemplary chain.
**Smallest action / owner.** Add a sha256 (and basis commit) column to §1.5 R1–R3 at the next amendment. No scope change. PEC loop.

**A-023 · PEC / CROSS_PRODUCT · authority conflict · WARN · HIGH**
**Assertion.** The Tier-0 domain-engine profile for PEC is `ADOPTED` while binding only the retired v0.4 prototype, so the cross-product profile registry describes a superseded product basis.
**Evidence.** `_DomainEngines/profiles/pec.yaml`: `profile_version: "0.2"`, `profile_status: "ADOPTED"`; its own notes record the 2026-07-24 pivot and that "the v0.4-baseline application this profile binds is a frozen reference corpus … This profile remains the binding for the frozen engine instance only; **full profile supersession is a planned act once PEC v2 has implementation shape**." Implementation references point into `projects/pec/core/src/…`, which the manifest lists as frozen prototype and not-basis.
**Consequence.** Confirms disclosed condition PEC-1, **accurately described**. Risk is reading order: a consumer orienting through the Tier-0 registry — the natural entry point for domain-engine integration — receives an `ADOPTED` profile describing a retired product. Mitigation is real and in-file: the profile states its own limitation explicitly, which is K-CONFLICT-1 working. The deferral is reasoned — supersession depends on v2 implementation shape, which F-PEC-1 holds back.
**Smallest action / owner.** No action required now. Optionally add a `profile_status` qualification so the limitation is machine-visible rather than prose-only. Tier-0 (D-T0 decision).

**A-024 · PEC · observation · INFO · HIGH**
**Assertion.** PEC's deliberate P2–P4 deferral, uniform current basis pin, and dependency state all verify exactly.
**Evidence.** **32/32** SOWs pin `SOFTWARE_DECOMP.md@3623b958b`, whose blob (`8aab8caa747a…`) is **byte-identical to the freeze**. Phase alignment: SOWs exist for exactly `pre-P1`(3)+`P1`(29); absent for exactly `P2`(12)+`P3`(14)+`P4`(6) — **zero violations**. 64 local `Dependencies.csv`, **254 rows, 135 ANCHOR / 119 EXECUTION**, all `Status ACTIVE` — matching the manifest exactly. 0 unknown deliverable refs across 94 ledger rows; 0 IN-scope items without a deliverable.
**Consequence.** The control case for coverage-deferral discipline. The absence of 32 SOWs is fully substantiated as sequencing and is **not** a coverage gap. PEC demonstrates a partially-initialized corpus can remain completely legible.

**A-025 · PEC · observation · INFO · MEDIUM**
**Assertion.** Two PEC product invariants reach the decomposition only through the hard-constraint table, not the scope ledger.
**Evidence.** `PEC-K-03` and `PEC-K-11` appear **0 times** in `ScopeLedger.csv`; they appear in `SOFTWARE_DECOMP.md` §1.3 as constraints **C3** and **C15**. `PEC-K-*` appears **0 times** in `Deliverables.csv`. DL-9 records the Phase-2 adversarial verification finding "PEC-K-11 unrepresented" and appending C15.
**Consequence.** Not a gap — §2 states the design explicitly: "Hard constraints C1–C16 (§1.3) bind every item and are not repeated as scope items unless they also require built or verified behavior (DL-7/DL-8)." Invariants bind globally by recorded decision. **MEDIUM** on consequence only: I cannot determine whether constraint-level binding suffices for PEC-K-01's kill test to be *verified* by a specific deliverable, since no deliverable row cites a `PEC-K-*`. Raised as an open question, not a finding of insufficiency.

### CROSS_PRODUCT

**A-026 · CROSS_PRODUCT · ownership gap · REVIEW · HIGH**
**Assertion.** The program has three mutually incompatible mechanisms for identifying "the PRD of record" and three levels of forward-coverage instrumentation, with no cross-product surface reconciling them.
**Evidence.**

| | PRD identity | Forward coverage | Reverse trace | SOW basis pin |
|---|---|---|---|---|
| Root | sha256 + named basis commit + D-GOV-22 + immutable adopted bytes — **all verified** | forward register, 84 rows | reverse register, 51 rows | 45/45 uniform |
| App | **no internal version**; identity via corpus v17; decomposition's own pin **stale** | **none** | **none** | 51 across **5** pins, none current |
| PEC | internal version v2.1 + D-PEC-58/61; **no sha256 pin** | `ScopeLedger.SourceRef` cites requirement IDs (47/57) + C1–C16 | none (compensated) | 32/32 uniform, current |

The Tier-0 register (23 records, verified) is the only cross-product control surface and governs contract versioning, fences, and bridge lanes; nothing addresses PRD identity or coverage instrumentation.
**Consequence.** The charter's closure criterion — every admitted PRD commitment has a trace disposition — is answerable for Root (84/84) and PEC (57/57) and **not answerable for App** (23 untraced, A-012), and the difference is structural: App alone has no coverage register. Since all three share one method layer (D-GOV-15/16), this is not a per-product choice that was ruled; it is an unrecorded inconsistency in how the shared method was applied. A program-level coverage statement cannot be made at all.
**Smallest action / owner.** Owner-decision request: decide whether a forward-coverage register is a required output of the shared method. If yes, that amends `docs/DECOMPOSITION_STANDARD.md` / the SOW standard (Root governance, M2), and App's register follows as decomposition repair. **Routed as a decision request, not asserted — a review may expose a candidate requirement, it cannot create one.**

**A-027 · CROSS_PRODUCT · trace gap · WARN · HIGH**
**Assertion.** Routed Root-doctrine notice coverage is uneven in a pattern the receiving loops' own detection cannot compensate for, and the most recent doctrine tranche shipped no notice to any loop.
**Evidence.** Complete inventory at the freeze (13 `NOTICE_*` files): `projects/chirality-app-dev` 6 (D-GOV-21, 23, 24, 26, + CONTRACT index correction); `domains/chirality` 4 (D-GOV-21, 23, 24 — **no D-GOV-26, no D-GOV-18**); `projects/pec` 2 (**no doctrine notices**); `projects/chirality-piping` 1 (**none**). D-GOV-27 — which amended DIRECTIVE §1/§2.6 and TYPES §1.4 — shipped **no** doctrine notice anywhere; Receipt 52 records the M6 survey as `none-required`.
**Consequence.** Confirms and quantifies disclosed condition 13. Two aspects go beyond it: (i) the `none-required` determination rests on the same hand-derived survey A-020 shows unstable, and is *correct* for App only because App pins project-local copies — meaning App's corpus check structurally cannot detect root DIRECTIVE/CONTRACT/SPEC/TYPES changes, so the stated safety net does not exist for that class; (ii) A-008 is a realised under-notification — D-GOV-18 changed `agents/`, `domains/chirality` pins `agents/`, no notice routed, dangling ACTIVE pin nine days later.
**Smallest action / owner.** Make the M6 pin survey deterministic (resolve every registered loop's manifest paths against the tranche's changed-file set) and record its output in the tranche manifest. Root loop; the survey is already required, so this is method repair, not a new obligation.

**A-028 · CROSS_PRODUCT · observation · INFO · HIGH**
**Assertion.** Root's forward register carries the entire §8.1 non-goal set as a single row, so non-goal coverage is not individually checkable.
**Evidence.** The forward register contains exactly one `ItemKind = non-goal` row (`nongoals-8.1`). PRD §8.1 contains a restated D-GOV-21 packet §4 set (five distinct non-goals) plus a separate "non-goals of this document specifically" paragraph enumerating eight or more. The scope ledger's 9 `OUT` items, each assigned to exactly one package (DEC-007), are the finer-grained surface.
**Consequence.** Not a defect — the ledger's 9 OUT items are checkable and F4 traces at objective/item granularity. Recorded because non-goals are the commitments most likely to erode silently, and OI-013's precedent shows these registers cannot see *inside* a row ("the gap is inside the objective, where the registers cannot see it"). The same blindness applies by construction. App's non-goals are similarly block-level (~27 bullets vs 3 SSOW rows + 4 OUT items).
**Smallest action / owner.** None required. If erosion becomes a concern, split the non-goal row per packet §4 item at the next regeneration. Root loop.

**A-029 · CROSS_PRODUCT · observation · INFO · HIGH**
**Assertion.** Root and PEC apply opposite rules for partitioning out-of-scope items under the same ratified standard, and only Root records the divergence.
**Evidence.** Root: exactly one `PackageID` per item **103/103**, including all 9 OUT items; recorded at DEC-007 and surfaced at OI-012 ("REF-002 permits a blank partition for OUT units while REF-003 requires every scope item to carry exactly one `PackageID`; REF-003 is stricter … the divergence is surfaced"). PEC: **23 ledger rows with blank `PackageID`**, exactly the 14 OUT + 9 TBD — the permissive standard reading. No corresponding divergence note in the PEC decomposition.
**Consequence.** Both readings are lawful. The observation is that one shared method yields two register shapes, with only one product surfacing it — so a cross-product register consumer cannot assume `PackageID` is populated. Minor; recorded for completeness of the shared-method picture.
**Smallest action / owner.** None required. Optionally record the reading in PEC's decision log. PEC loop.

## 6. Disclosed-conditions assessment

### 6.1 Manifest §5 — the 20 basis-wide conditions

| # | Verdict | Assessment |
|---|---|---|
| 1 D-GOV-27 EffectiveSHA unbound | **WORSE** | Verified: a prose placeholder, not even `TBD`. Beyond disclosure: it *blocks a remedy* — the four contracts amended by that tranche cannot be repinned because no successor SHA exists (A-003). Reach: 4 contracts + every Root SOW basis-currency check. |
| 2 SHA-role language conflicts | **ACCURATE** | Verified: header calls `ea0ad7a56` "EffectiveSHA"; D-GOV-25 calls it `CandidateMergeSHA` and assigns `EffectiveSHA` to `653fabc9b`. Operative pinning uses the correct value, so consequence is reader risk — but a counter-example to E-3 on the artifact E-3's deliverable governs (A-005). |
| 3 Amendments lack one supplied verifying diff | **ACCURATE** | I reconstructed it (`653fabc9b..da31c19b5` over the decomposition: 7 hunks, all DEC-021 objective additions, no scope/identifier change). The claim it supports is true. Compounds with #1 (A-003) and revealed A-004. |
| 4 Receipt 52 as handoff, not a HANDOFF_STATE file | **ACCURATE, IMMATERIAL** | Receipt 52 contains applied acts, battery results, gate, and a complete "Open after this receipt" list including the owed backfill. No reliance risk found. |
| 5 CURRENT_WORKPLAN ACTIVE but complete | **ACCURATE, minor** | Consistent with "next phase is owner-gated future work" — no successor exists to point to. D-7 already provides that coordination surfaces carry no authority merely by existing. |
| 6 Root AC/VER not deterministically represented | **WORSE** | Six frontmatter keys, no status field; **87 distinct prose sentences**; token overloaded across five senses, so no text-matching proxy is reliable either (A-010). Positively, 0 of 45 omit the marking. |
| 7 App PRD identity depends on corpus v17 | **ACCURATE** | No version string; v17's 8 pins recompute **8/8 CLEAN**, so the mechanism works. Fragility: identity is external to the artifact — and A-016 shows a second identity mechanism already diverged. |
| 8 App acceptance provenance weaker | **WORSE** | Not only "implicit approval" with no ruling/quote/date/SHA — the acceptance attaches to a state **superseded four times in place** with the Gate Log untouched (A-015). |
| 9 App lacks invariant-coverage register | **ACCURATE, partially mitigated** | Verified absent. Two mitigations omitted from disclosure: §10A.1 gives family-level ownership, and the obligation is conditioned on REVIEW closure, which may not have occurred (A-017). |
| 10 D-APP-48 mirror entirely stale | **WORSE** | Verified **12/12 STALE**, files now shims into `@chirality/runtime-contracts`. Worse: the contract's **own registered validator returns PASS** because it verifies at the pinned commit (A-014). The staleness is unobservable through the designated check. |
| 11 App domain source manifest heavily drifted | **ACCURATE (not re-derived)** | Manifest states 119/129/219. I did not recompute this pack (consulted-only; I prioritised the Root pack whose pins bear on the notice architecture). Accepted-not-verified. |
| 12 Root Chirality manifest: drift + six missing ACTIVE pins | **LESS SEVERE, with one real defect** | Recomputed: **126 CLEAN / 93 DRIFT / 6 MISSING** — totals match. But "six missing **ACTIVE**-pinned agent files" is **inaccurate**: 5 of 6 carry `ArchiveState = RETIRED` (CONTEXT_TRANSPOSE, DECOMP_BASE, SCHEDULING, SKILLMAKER, TOOLMAKER) and their absence is expected. Only `AGENT_ORCHESTRATOR.md` is genuinely ACTIVE — with a known cause (D-GOV-18 rename) never propagated, no successor row, and two other unpinned live contracts (A-008). Fewer real defects than disclosed; the one real defect is a live change-notice failure. |
| 13 Notices not reaching/dispositioned consistently | **WORSE** | Quantified in A-027. Beyond disclosure: D-GOV-27 shipped **no** notice anywhere; the `none-required` survey is hand-derived and unstable (A-020); and the stated fallback (loops detect via their own checks) **does not hold** for root DIRECTIVE/CONTRACT/SPEC/TYPES, because App pins project-local copies of those filenames. |
| 14 PEC's 32 absent P2–P4 SOWs deliberate | **ACCURATE** | Verified exactly; zero violations. Not a coverage gap (A-024). |
| 15 Root/PEC different SOW validation eras | **ACCURATE** | Respected: I did not rerun the SOW validator over Root. No finding depends on a validator era. |
| 16 Domain packs consulted-only but carry drift evidence | **ACCURATE** | Confirmed useful: the Root pack's manifest supplied A-008, the most concrete instance of change-notice failure. Treated as evidence about Root architecture effects, never as a reviewed product. |
| 17 Piping is a notice-coverage exemplar | **ACCURATE** | Piping holds exactly 1 notice, non-doctrine. It is also the downstream consumer of the D-APP-48 contract A-014 shows stale-but-passing — the exemplar function worked. |
| 18 Semantic-parity change not an accepted instrument | **ACCURATE** | Respected. Nowhere treated as scope; its absence nowhere counted as a gap. |
| 19 Resource governance is candidate, not accepted scope | **ACCURATE** | Respected. §4 records it unowned with every cell blank; absence explicitly **not** a gap. Nothing proposed. |
| 20 Charter is guidance to challenge, not evidence | **ACCURATE** | Respected. No charter proposition cited as evidence. Where my account converged (e.g. Root owning `runtime/`) I cite PRD O-2 and D-GOV-20. Divergences at §7.4. |

### 6.2 Root per-product conditions (1–10)

1. **WORSE** (A-003). 2. **ACCURATE** (A-005). 3. **ACCURATE**; diff reconstructed, claim true. 4. **WORSE** — not one stale row but **91 surfaces**, 45 *instructing* preservation (A-006). 5. **ACCURATE, IMMATERIAL**. 6. **ACCURATE, minor**. 7. **ACCURATE** — verified 0 occurrences of `PKG-0`, `DEL-0`, `execution/` (A-009). 8. **WORSE** (A-010). 9. **ACCURATE, not re-derived** — the AGENT_TASK absolute-path fields, `validate_id_format.sh`, SOW validator prefix set, and `tools/REGISTRY.md` conflicts are recorded in Receipt 51's fan-in list as owner items; already routed, so re-opening would be redundant rediscovery. Noted as standing. 10. **ACCURATE for the PRD; WORSE downstream** — the pointer mechanism is sound and correctly cites SPEC §0.2.1, but the superseding enumeration reached the decomposition and 90 operative contracts only **partially**: `.github/workflows/` propagated, `CLAUDE.md` did not (A-001).

### 6.3 App per-product conditions (1–12)

1. **ACCURATE**; respected as not-basis. 2. **ACCURATE** — verified two `## 17.` headings (lines 1676, 1692). 3. **WORSE** (A-015). 4. **ACCURATE, partially mitigated** (A-017). 5. **WORSE** (A-014). 6. **ACCURATE, not re-derived** — consistent with A-014 (pinned files now shims), but I did not audit D-APP-49 directly; marked UNKNOWN. 7. **ACCURATE, not re-derived**; respected as not-basis. 8. **ACCURATE and fully resolved** — the two extras are `DEL-00-01`/`DEL-00-02`, 53 distinct IDs, no duplication; **IMMATERIAL** as a defect. 9. **ACCURATE, not re-derived**. 10. **ACCURATE and extended** — the misidentifying notice is the CONTRACT index correction, whose stated consequence I verified false; the extension is that the same misdetermination appears in Receipt 44 and is contradicted by Receipt 52 (A-020). 11. **ACCURATE** (A-021). 12. **ACCURATE, not re-derived** — same class as #10 and A-020: the loop's coordination surfaces disagree about applied state.

**Additional App findings not disclosed:** A-012, A-013, A-016, A-018, A-019.

### 6.4 PEC per-product conditions (1–5)

1. **ACCURATE** (A-023); the profile states its own limitation, which is conflict-surfacing working. 2. **ACCURATE**, verified exactly against `PhaseHint`, zero violations (A-024). 3. **ACCURATE, not re-derived** — per manifest item 4 these are already recorded; I assessed rather than rediscovered. Their common shape is worth naming: all three are *intra-contract* linkage defects invisible to register-level checks — the same blindness OI-013 named for Root and A-028 names for non-goals. **That recurrence across two products is the signal, not the three instances.** 4. **Respected**; not presented as new. 5. **ACCURATE** — live local-register state recomputes to exactly 254 rows / 135 ANCHOR / 119 EXECUTION.

**Additional PEC findings not disclosed:** A-022, A-025.

## 7. Open questions, UNKNOWNs, and owner-decision requests

### 7.1 UNKNOWNs

| # | Question | Why the basis cannot decide |
|---|---|---|
| U-1 | **What does a runtime client do when the Root daemon is absent or version-incompatible?** | Searched `runtime/README.md`, D-GOV-20, `AGENTS.md` §Shared Runtime Doctrine, App PRD §8.16. Ownership and authority boundary are declared; **degraded-mode behavior is stated nowhere**. Marked UNKNOWN in §4 rather than inferred. Matters because PEC's fallback is fully specified (PEC-K-01 kill test) while the substrate both PEC and App depend on has none. |
| U-2 | **Has App REVIEW closure occurred?** | Determines whether the missing invariant register is a breach or a pending obligation (A-017). The basis records `READY_FOR_IMPLEMENTATION_HANDOFF` with WARNINGS, which is not that act. |
| U-3 | **Is constraint-level binding sufficient for PEC invariant verification?** | No PEC deliverable row cites a `PEC-K-*` (A-025). The design is recorded and coherent, but whether PEC-K-01's kill test has a verifying deliverable cannot be answered from the registers. |
| U-4 | **Do D-APP-49's mirror obligations still describe the rehomed architecture?** | Disclosed App-6. A-014 makes it likely they do not, but I did not audit D-APP-49 and will not assert it. |
| U-5 | **Which loops pin which root surfaces?** | No record enumerates this. A-020 and A-027 show it is determined by hand per tranche with at least one inconsistency. Until derived mechanically, notice-routing correctness is unverifiable in either direction. |
| U-6 | **Was App's basis-pin heterogeneity a decision or an omission?** | A-013 establishes the fact. No decision record addresses per-tranche repinning policy, so I cannot tell whether it was ruled or drifted. |

### 7.2 Owner-decision requests (routed, not asserted)

None is a requirement created by this review.

- **ODR-1 (A-026, A-012).** Decide whether a forward-coverage register mapping every admitted PRD requirement to a deliverable is a required output of the shared method. Criteria: Root and PEC already produce the equivalent and can answer the closure criterion; App cannot. Instrument: `docs/DECOMPOSITION_STANDARD.md` / the SOW standard (Root governance, M2). Downstream: App decomposition repair only if yes.
- **ODR-2 (A-010).** Decide whether SOW acceptance status should become a frontmatter field. For: any deterministic AC/VER gate needs it, since prose parsing is unreliable. Against: added schema surface for a status already reliably human-readable. Instrument: the SOW standard (M2).
- **ODR-3 (A-014, A-018).** Decide whether registered validators must declare their observation boundary in output. Criteria: D-GOV-02 already bounds results to their declared boundary; two validators return PASS where a reader would infer more. Instrument: D-GOV-02 lineage / `tools/REGISTRY.md` conventions.
- **ODR-4 (A-015).** Decide whether App's Gates 1–7 hold for current content, or which require re-running after SCA-APP-003/004. Instrument: D-APP ruling.
- **ODR-5 (A-027, A-020, U-5).** Decide whether the M6 pin survey becomes a deterministic, recorded step in every instruction-surface tranche. Instrument: `AGENTS.md` change-notice rule (M2) — the survey is already required; only its method would change.

### 7.3 Open design questions preserved

I close none of these.

- **The reusable work surface.** Whether it is a Root requirement, an App capability, or both under different ownership. **Basis position:** no instrument assigns ownership; App owns its own product surface, and PKG-02's exclusions state the shell "owns presentation only". **Criteria the basis supplies:** whether any consumer other than App is committed to depend on it; whether Root's export boundary would carry presentation assets; whether the M2 gate would apply to changes in it. **Downstream affected:** App PKG-02 scope, Root export profile, future domain-application integration home. §4 marks it UNKNOWN.
- **Application environment profile.** Exact authority and schema. **Basis position:** none exists; `_DomainEngines/profiles/*.yaml` is the nearest live analogue and is Tier-0-owned and domain-engine-scoped. Absence is **not** counted as a gap.
- **PEC availability thresholds.** **Basis position:** PEC-K-01 and PEC-K-11 fix the floor (never required; mode-proportional); the ladder above it is undetermined. Preserved.
- **Logical composition vs physical bundling.** **Basis position:** D-GOV-20 fixes one runtime owner and a per-user daemon; it does not fix packaging. U-1 shows the degraded-mode question is entangled with this and should be decided with it.
- **Resource governance.** Charter-only candidate. Preserved; **absence is not a gap** and I propose nothing.

### 7.4 Where my independent account diverged from the charter

- The charter asserts "Root runtime ownership is not optional … The Root decomposition **must** assign its contract and continuing conformance work to a Root package and deliverables." My independent reading: PRD O-2(c) does place `runtime/` in the operative product, and the forward register maps O-2 to `DEL-02-02_Three_Layer_Authority_Boundary_Conformance`, so the commitment **is** covered. But no Root package or deliverable is named for the runtime *contract and continuing conformance* as a distinct work domain — PKG-02 covers "the three operative layers" at authority-boundary level, not protocol/daemon/client/adapter conformance. I record this as an observation about coverage granularity, **not** a conformance finding, because O-2 is a boundary commitment the decomposition covers; the charter's stronger reading would create scope, which a review may not do. If the owner wants runtime conformance as an owned work domain, that is a PRD amendment, not decomposition repair.
- The charter frames PEC and resource governance symmetrically as "optional services". The basis supports this for PEC with unusual rigor (PEC-K-01, kill test, F-PEC-1..4) and says nothing at all about resource governance. I treated them asymmetrically for that reason.

## 8. Closing note

Pass-1 independent return, produced without contact with, knowledge of, or inference about any other reviewer's work. Every claim is anchored to `da31c19b5656dd74615e308c4215688971d33dc9`; where the basis could not decide, the report says UNKNOWN. Coverage is complete for all three products: Root 84/84, App 159/159 requirements plus goals/non-goals/known-gaps under a stated grouping rule, PEC 57/57. No Git or worktree state was altered and no file was written — the single deviation from the brief, imposed by the harness, is that the report is delivered as this message rather than at the brief §8 path.
