# CHALLENGE — Reviewer B on Reviewer A's frozen pass-1 report

Charter protocol step 5 (reciprocal challenge). Marks only; no new findings.

---

## Header

| Field | Value |
|---|---|
| Challenger | **B** (horizontal lens: architecture, boundaries, adversarial concordance) |
| Input report | `/Users/ryan/dev/chirality-tandem-review-2026-07-26/REVIEWER_A_REPORT.md` |
| Input hash **verified before reliance** | `ee39da9fc11d9e56d9c7db8ab5bd458252519a1acd66e8504ec9c52fe650ee3e` — **recomputed and MATCHES** the hash supplied in my challenge brief |
| Challenge brief hash verified | `1b2ed0e424c52a4c6a0889afd633c19ef4e5bac67a4e648a83b987ae744bce11` — MATCHES |
| Evidence basis | `/Users/ryan/dev/chirality-review-frozen-da31c19` @ `da31c19b5656dd74615e308c4215688971d33dc9` — the only source consulted; working tree verified clean and HEAD unchanged |
| Primary checkout | **Not read.** `/Users/ryan/dev/chirality` was not accessed. |
| Not read | `CHALLENGE_A_ON_B.md`, `CHALLENGE_BRIEF_A.md`, `BRIEF_REVIEWER_A.md` |
| My own pass-1 report | `REVIEWER_B_REPORT.md` (`5c20315e9ad7…`) — **not edited, appended to, or rewritten** |
| Date | 2026-07-26 |

**Findings identified from the report itself** (not from the brief's arithmetic): RA-001 is the sole **BLOCK**; RA-002…RA-008 are **REVIEW** (7); RA-009…RA-015 are **WARN** (7); RA-016…RA-018 are **INFO** (3). Total 18. This matches A's own tally at §6 (*"BLOCK 1 · REVIEW 7 · WARN 7 · INFO 3"*). **All 8 BLOCK/REVIEW findings are challenged below, plus a recorded sample of 5 WARN/INFO findings** (minimum 3).

**Method.** I re-derived every load-bearing quantitative claim myself rather than accepting A's citation, and I did not rely on my own pass-1 memory: every file cited below was re-opened at the frozen corpus during this challenge pass. Where A's claim was a census or a bidirectional register comparison, I wrote my own independent parser rather than reusing A's stated method, so agreement is reproduction and not restatement. **I ran no repo script and relied on no validator PASS**; all computation was read-only (`shasum`, `git cat-file`/`rev-parse`/`show`, `grep`, `sed`, `python3` over `csv`/`re`). Assertion-status discipline and the manifest's 20 disclosed conditions continue to apply; where A assesses the consequence of a disclosed condition rather than rediscovering it, I say so.

---

## Challenged findings — BLOCK and REVIEW (all 8)

---

### RA-001 — BLOCK — Six App contracts pin a non-existent decomposition-basis object

**Verdict: ADD-MISSING-EVIDENCE**
**Confidence in my verdict: HIGH**

**Core assertion — independently re-verified, fully correct.**

| Check | A's claim | My independent result |
|---|---|---|
| Object `416b29033bbacb0bc3648d84033272b7ab4e6e11` exists? | No | `git cat-file -t` → `fatal: git cat-file: could not get object info` — **does not exist** |
| Shallow clone artefact? | No | `git rev-parse --is-shallow-repository` → `false` |
| Prefix coincidence | A different object shares "only the first 9 hex characters" | `git rev-parse --disambiguate=416b2903` → `416b290334049762fe0b0c2a43df373c8da230ab`. Common prefix is `416b29033` = **exactly 9 hex characters**. Correct. |
| Number of contracts affected | 6 | **6** |
| Which contracts | `DEL-02-01`, `-02-02`, `-02-04`, `-05-04`, `-08-02`, `-08-03` | **Identical set** |
| Other four pins resolve | Yes | `2770fda4c`, `0724f26f6`, `b4d2c9ab2`, `ff59428ff` all → `commit`. Failure is specific. |
| Full pin census | `0724f26f6`×10 (+×2 PKG-00), `2770fda4c`×6, `416b29033`×6, `b4d2c9ab2`×15, `ff59428ff`×14 | `b4d2c9ab2`×15, `ff59428ff`×14, `0724f26f6`×12, `416b29033`×6, `2770fda4c`×6 — **sums to 53, matches exactly** |

**The evidence A lacks / one correction to A's mitigating clause.**

A writes: *"five of the six carry an explicit `## SCA-APP-004 Gate-5 Current Contract (Controlling)` section."* **That count is wrong.** Only **three** carry that section, and in all three it is a genuine level-two heading at line 18:

- `PKG-02_.../DEL-02-01_Desktop_Shell_and_Matrix_Navigation/ScopeOfWork.md:18`
- `PKG-02_.../DEL-02-02_Workbench_and_Pipeline_Selection_UX/ScopeOfWork.md:18`
- `PKG-02_.../DEL-02-04_Toolkit_Options_and_Local_UI_State/ScopeOfWork.md:18`

The other three (`DEL-05-04`, `DEL-08-02`, `DEL-08-03`) contain **no such section** — I enumerated their level-two headings and each carries exactly the six canonical headings the ratified standard specifies, and nothing else.

**A's substantive point nevertheless survives, by a different mechanism, and is if anything better supported than A stated.** All six contracts *do* show SCA-APP-004 content propagation — the other three carry it as row-level source citations inside the canonical sections, e.g. `DEL-05-04` line 72 (*"Selected-session replay posture … | SCA-APP-004 Amendment Preview and Propagation Plan"*) and line 171 (`DEL-05-04-REQ-014 … | SCA-APP-004; SOW-006`); `DEL-08-02` lines 49–57; `DEL-08-03` lines 49, 75–77, 206. So A's conclusion — *"the defect is in the basis pointer, not evident content abandonment"* — holds for **6 of 6**, not 5 of 6. The correction changes the count and the mechanism, not the conclusion.

**Severity / class commentary.** **I agree with BLOCK**, and I agree with A's class (*trace gap / authority-chain break*). Under A's declared boundary an unresolvable accepted-basis pointer is the paradigm BLOCK case, and K-AUTH-2 makes the SHA the thing that binds. I add that this finding is well-placed as A's only BLOCK: it is the one defect in either report that no amount of reading can repair, because the referent is absent from the object store. A's smallest action (re-pin in one bounded tranche, no scope change) is correct and proportionate.

**Disclosure.** I did not make this finding in my own pass 1. My App pass extracted `project_scope_refs` and primary outputs across all 53 contracts but did not test `decomposition_basis` object resolvability. **This is a genuine gap in my pass-1 coverage that A's lens caught**, and I record it rather than absorb it.

---

### RA-002 — REVIEW — D-GOV-20 rules `runtime/` root-owned; the Root decomposition assigns nothing to it

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Every load-bearing claim independently re-derived and correct.**

| Check | A's claim | My independent result |
|---|---|---|
| Regex `daemon\|credential\|residency\|turn lock\|engine adapter\|socket` over all 103 `ScopeItemStatement` values | 0 matches | **0 matches** (parsed the CSV myself; 103 rows confirmed) |
| Same regex over **all fields** of all 45 deliverable-register rows | 0 runtime hits; "2 incidental hits on the word *session* only (`DEL-01-01`, `DEL-04-05`)" | Runtime regex → **0 rows**. Separate `session` regex → **exactly 2 rows: `DEL-01-01_Genus_Concordance…`, `DEL-04-05_Root_Governed_Loop…`**. Matches precisely. |
| D-GOV-20 §Ruled architecture items 1–2 quotes | as quoted | Verbatim match, incl. *"becomes a root-owned `runtime/` workspace"* and *"exclusively owns runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency."* Status RULED 2026-07-22. |
| `runtime/README.md` quote | as quoted | Verbatim match. |
| App `DEL-03-01/_STATUS.md` §Remaining | as quoted | **Verbatim match at line 13**, including *"Promote provider-neutral runtime contracts to root `runtime/` … expand conformance for daemon/client/project/residency behavior (gated: serialized core integration owner)."* |
| Root's only runtime coverage is `SOW-027` → `DEL-02-02` | yes | Confirmed. |
| Mechanism: DEC-001 makes the PRD the sole scope source | yes | Confirmed at §2.1/§2.3. |

**One factual correction (does not affect the assertion).** A states the subsystem *"exists in the tree with six packages."* `runtime/packages/` contains **seven**: `cli`, `client`, `contracts`, `core`, `daemon`, `engine-claude`, `engine-pi-omlx`. The error understates the finding.

**Evidence that materially strengthens A's MEDIUM-confidence qualifier.** A marks **MEDIUM** on *"characterising it as a gap rather than a deliberate sequencing choice"* and marks the intent **UNKNOWN** — properly calibrated. I add one datum A did not use, which bears directly on that question: the Root decomposition's §2.3 *"Interpretive context — non-source"* list enumerates the documents that were read and deliberately excluded from generating scope — `AGENTS.md`, `DIRECTIVE`, `CONTRACT`, `TYPES`, the D-GOV-21 packet §5, and the live registries. **D-GOV-20 does not appear on that list.** So the runtime ruling was not a known input consciously excluded; it was not enumerated as an input at all. That does not prove the omission was unintended — the basis still cannot decide intent, and A's routing to the owner remains right — but it removes the reading that D-GOV-20 was weighed and set aside.

**Severity commentary — recorded divergence.** A grades this **REVIEW**; I graded the same condition **BLOCK** (my RB-002). The **facts are identical and now jointly re-verified**; the divergence is purely on severity and is traceable to differently drawn observation boundaries. A's BLOCK threshold requires the accepted basis to be *contradicted* or an accepted-basis *pointer to be unresolvable*; on that threshold an uncovered ruling is REVIEW, and A is internally consistent. My threshold also admits *"an accepted-basis commitment left without any executable coverage anywhere in the corpus"*, which this is. My reason for the higher grade: two products are **ruled clients** of this subsystem (D-T0-23), `docs/CONTRACT.md` §1.13 binds seven `K-*` invariants to it with declared enforcement points, and `runtime/` is outside `docs/SPEC.md` §0.2.1's instruction surface — so no M2 gate reaches it either. I do not ask the manager to resolve this in my favour; I ask that it be recorded as **agreed-on-fact, divergent-on-severity**, since both reviewers reached it independently from opposite lenses.

---

### RA-003 — REVIEW — App decomposition §13 claims app-dev retains semantic ownership of the runtime

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Re-verified verbatim.** `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` line 611 reads exactly as A quotes it:

> Shared runtime promotion preserves this decomposition's existing package/deliverable topology. Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership and acceptance evidence through the SCA-APP-003 impact map.

Counter-authorities re-checked and correct as quoted: App PRD §17 (second) lines 1692–1706 (*"a root-owned product subsystem rather than a frontend-owned singleton"*, *"exclusively owns"*); D-GOV-20 items 1–2; and the mitigating OI-007 (`SHARED_RUNTIME`, still open, over SOW-009–011, 037, 043, 046, 063, 072, directing *"prove one runtime owner … before export"*).

**Evidence A did not use, which bears on A's own MEDIUM-confidence caveat.** A allows a charitable reading — that app-dev *deliverables* remain accountable units rather than App owning the runtime contract — and marks **MEDIUM** that a substantive claim was intended. Two governed obligations, both internal to the App loop, complicate that reading:

- The decomposition's own §2.1: *"If a downstream task discovers conflict among these documents, it must surface the conflict rather than silently reconcile it."*
- App PRD §16: *"If this PRD and the active SOFTWARE_DECOMP snapshot disagree about package topology, deliverable IDs, coverage telemetry, or decomposition method, the conflict must be surfaced and resolved through governed PRD/decomposition amendment before scaffold or REVIEW closure."*

Neither was exercised for this sentence. If the sentence were loose drafting, the conflict-surfacing duty would still have applied once it diverged from PRD §17. That weakens the loose-drafting reading without settling it — A's MEDIUM remains the right calibration, and I do not upgrade it.

**Severity commentary — recorded divergence.** A grades **REVIEW**; I graded the same sentence **BLOCK** (my RB-001), for the same boundary reason given at RA-002. A's smallest action (a one-sentence clarification within OI-007's existing scope, no new scope) is materially smaller than mine and, if the charitable reading is correct, is exactly right. **I regard A's routing as superior to my own on this finding** and note it for fan-in: whichever severity the manager adopts, A's correction is the cheaper lawful act and should be preferred.

---

### RA-004 — REVIEW — App scope item `SOW-064` has no executing contract

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Re-verified.** Ledger line 448 reads exactly as A quotes:

> `| SOW-064 | IN | MCP extension boundaries. | REF-006 Section 8.15 | PKG-06 | DEL-06-02, DEL-06-03 | OBJ-005 | DEC-005 | FALSE |  |`

§8 `CoversScopeItems` — `DEL-06-02` = `SOW-047, SOW-049, SOW-050`; `DEL-06-03` = `SOW-048, SOW-050`. **Neither lists SOW-064.** `grep -l "SOW-064"` across all 53 App contracts → **0 files**. Across the whole App execution tree, `SOW-064` appears only in SCA-APP-001 evidence (`Amendment_Preview.md`, `Impact_Assessment.md` ×2 each), `D-APP-14_RULING_2026-06-17.md`, and the decomposition itself — i.e. nowhere in the executable layer.

**Evidence I add that independently proves A's mechanism.** A asserts *"the executable layer follows §8."* I tested this directly rather than inferring it: across all **51** decomposition-derived App contracts, frontmatter `project_scope_refs` matches §8 `CoversScopeItems` with **0 mismatches**, and `package_objective_refs` matches §8 `SupportsObjectives` with **0 mismatches**. So the contracts reproduce §8 perfectly and §9 not at all — which is precisely why a scope item present only in §9 has no contract. A's mechanism is confirmed by construction, not by inference.

**Severity / class commentary.** **REVIEW is right**, and A's class (*trace gap*) is right. I note one nuance in A's favour that A stated but could have pressed harder: the decomposition's telemetry line 477 (`ScopeItemsWithoutDeliverableMapping | 0`) is **not false** — it is true *of the ledger*, which does map SOW-064 to two deliverables. The defect is that the metric is computed against the surface that is not the executable one. A recognises this (*"the ledger direction (§9) claims coverage the deliverable direction (§8) does not carry"*), and the finding is correctly framed as an asymmetry rather than as a false telemetry claim.

---

### RA-005 — REVIEW — Seven §8-versus-§9 coverage disagreements, with no companion register to arbitrate

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Independently reproduced with my own parser** (I parsed §8 deliverable rows and §9 ledger rows separately and inverted the §8 mapping, rather than following A's stated method):

```
parsed §8 deliverables: 51   §9 ledger rows: 78
MISMATCHES: 7
  SOW-002   IN   ledger=DEL-07-01              tables=DEL-02-03,DEL-07-01
  SOW-023   IN   ledger=DEL-02-05,DEL-09-06    tables=DEL-09-06
  SOW-064   IN   ledger=DEL-06-02,DEL-06-03    tables=(none)
  SOW-075   IN   ledger=DEL-01-01,DEL-07-01    tables=DEL-01-01
  SOW-076   OUT  ledger=DEL-01-04,DEL-04-02    tables=DEL-01-04
  SOW-077   OUT  ledger=DEL-01-04,DEL-07-06    tables=DEL-01-04
  SOW-078   OUT  ledger=DEL-01-04,DEL-09-04    tables=DEL-01-04
```

**Item-for-item identical to A's table, including every direction.** A's control also reproduces exactly: **Root 0 mismatches** (103 ledger rows vs 45 register rows) and **PEC 0 mismatches** (94 vs 64), under the same test. Directory listing confirms `projects/chirality-app-dev/execution/_Decomposition/` contains exactly one file.

**One refinement A's table omits.** Three of the seven — **SOW-076, SOW-077, SOW-078** — are `OUT` boundary items, not IN production scope. For an OUT item the deliverable mapping is a boundary-guard record rather than a coverage claim, so a discrepancy there is materially less consequential. This *strengthens and sharpens* A's own "six of the seven are benign" judgement: besides SOW-064, only **three IN items** (SOW-002, SOW-023, SOW-075) disagree, and each retains real coverage through the other mapped deliverable. A's conclusion is right; the residual IN-item exposure is smaller than the raw count of seven suggests.

**Severity / class commentary.** **REVIEW is right.** I note that A's structural point is the load-bearing one and is fully supported: App is the only product of the three lacking an authoritative companion register, and the identical exhaustive test finds zero mismatches in both products that have one. That is a genuine control, not a rhetorical contrast.

---

### RA-006 — REVIEW — Root `DEL-02-01` settles instruction-surface membership from a superseded enumeration

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Re-verified verbatim in the contract** (`execution/PKG-02_.../DEL-02-01_Instruction_Surface_Membership_and_Release_Management/ScopeOfWork.md`):

- `CLM-002` (lines 64–66) enumerates **six** members: `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`.
- `CON-001` (lines 74–79) frames an *"Unresolved membership conflict"* between PRD O-1's six and the deliverable's own `_CONTEXT.md` six-plus-`.github/workflows/`, calls them *"the two authorized sources"*, and states *"settling it is an owner act."*
- `AC-001` (lines 80–83) requires the register to record `CON-001` *"as an open membership question rather than silently adopting either enumeration."*

**Counter-authorities re-verified verbatim:**

- `docs/SPEC.md` §0.2.1 line 44: the shared instruction surface is *"(`AGENTS.md`, `CLAUDE.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`)"* — **eight members**.
- `D-GOV-26_owner_gated_closeout.md` lines 33–48: the enumeration *"lives at `docs/SPEC.md` §0.2.1 (line 44)"*; `CLAUDE.md` joined the guarded set with regression tests; *"From this tranche's effect onward, changes to `CLAUDE.md` and `.github/workflows/` are M2 instruction-surface tranches by doctrine, not only by guard behavior."*
- `docs/PRD_ROOT.md` pointer block: O-1's enumeration is *"superseded by instrument"*, authoritative enumeration is SPEC §0.2.1.

**Evidence I add — the omission is total, not partial.** I grepped the entire contract for `SPEC.md`, `D-GOV-26`, `D-GOV-27`, and `CLAUDE.md`: **zero occurrences of any of them.** The governing enumeration and both ruling instruments are absent from the file entirely, not merely subordinated to the PRD. That closes the one reading under which the contract might be said to have weighed and set aside the ruled source.

**Severity / class commentary.** **REVIEW is right**, and A's class (*authority conflict*) is right. I record that I considered BLOCK and rejected it: `AC-001` would certify a ruled question as open, which is close to the line, but nothing is `ISSUED`, the ruling already exists so no new instrument is needed, and A's smallest action (amend `CLM-002`/`CON-001` to cite SPEC §0.2.1 and D-GOV-26/27) is a contained deliverable remediation. REVIEW is proportionate.

**Disclosure.** **I did not make this finding.** My pass 1 read `DEL-02-01`'s frontmatter and candidate-status markers but not its `CON-001` body. This is the strongest finding in A's report that my lens missed, and it is a direct counterexample to my own RB-008 framing: I argued the executable layer cannot express cross-product relations because the standard lacks the element — A shows that even a *single-product* supersession fails to reach the executable layer through a mechanism the standard does support. Both are true; A's is the more immediate defect.

---

### RA-007 — REVIEW — App acceptance criteria test document conversion, not deliverable fitness

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Census independently reproduced across 100% of all 130 contracts, with my own extraction code. Every one of A's six metrics matches to the digit:**

| Metric | A | My recount |
|---|---|---|
| mean `AC-*` — Root / App / PEC | 3.3 / **1.1** / 12.3 | **3.3 / 1.1 / 12.3** |
| mean `VER-*` | 2.3 / **1.1** / 10.9 | **2.3 / 1.1 / 10.9** |
| contracts with exactly 1 AC | 0 / **48** / 0 | **0 / 48 / 0** |
| contracts naming `HUMAN_REVIEW` | 41 / **0** / 28 | **41 / 0 / 28** |
| contracts declaring a `CON-*` | 14 / **0** / 31 | **14 / 0 / 31** |
| contract counts | 45 / 53 / 32 | **45 / 53 / 32** |

A's *"at least 13"* conversion-shaped claim is a lower bound and holds: a broader pattern over all `AC-*` text returns **16** App contracts whose acceptance criteria are stated in conversion/preservation/lossless-migration terms. Representative quotes spot-checked and correct (`DEL-01-01` AC-001 *"The converted contract preserves all legacy source content … without changing lifecycle or dependency state"*; `DEL-01-04` AC-001 *"Preservation and traceability … without adding scope, reliance claims, lifecycle meaning, or obligations"*).

**A's counter-evidence re-verified and correct** — and A deserves credit for weighing it. `PKG-03_.../DEL-03-01/_STATUS.md` carries, verbatim: `**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20` and `**Checking Approval SHA:** 8c6d55d3e8…`, with `(HUMAN)`-attributed transitions. `## Remaining` is present in **53 of 53** `_STATUS.md` files, exactly as A states. App's human gate is real; A does not overstate.

**Evidence that complicates (not refutes) the finding.** A's own §0.5 records that **App's SOW validation era is UNKNOWN** — the manifest fixes eras for Root (pre-v6/v6.1) and PEC (current method) only (basis condition 15). Since the shared SOW method layer changed through amendments v1–v6.1, some of the 45/53/32 divergence may be a method-era artefact rather than a difference in loop rigour. A's decision to hold severity at **MEDIUM confidence** and route to the owner rather than assert a failure is, in my judgement, the correct call, and this datum supports it. It does not weaken the underlying measurement, which is exact.

**Severity / class commentary.** **REVIEW is right**, class *omission* is right. The metric I regard as most load-bearing is **0/53 `HUMAN_REVIEW` against 41/45 and 28/32** — this is the human-hinge question at the executable layer, and it is the one place in either report where the three products diverge sharply on a charter-central property.

---

### RA-008 — REVIEW — App's SOW layer declares five different bases, all superseded

**Verdict: CONFIRM**
**Confidence in my verdict: HIGH**

**Every claim independently re-derived and exact:**

| Check | A's claim | My result |
|---|---|---|
| Distinct App pins | 5 | **5** |
| Census | `b4d2c9ab2`×15, `ff59428ff`×14, `0724f26f6`×12, `416b29033`×6, `2770fda4c`×6 | **Identical; sums to 53** |
| Commit dates | 2770fda4c 07-12; 0724f26f6 07-13; b4d2c9ab2 07-13; ff59428ff 07-13 | **2026-07-12 21:11; 07-13 05:55; 07-13 10:18; 07-13 15:14** — none later than 2026-07-13 |
| Decomposition blob at every resolvable pin | `680b7e8a1e0f7da05d2f93f03a1e306cd7c59dfb` | **Identical at all four** |
| Blob at `da31c19b` | `b3af4ed677659aa1dd478bba3857c7e1817dd3ab` | **Confirmed** — pinned content uniformly superseded |
| Root contrast | all 45 pin `653fabc9b3e8…` | **45/45** |
| PEC contrast | all 32 pin `3623b958b`, blob **identical** to `da31c19b` | **32/32**; blob `8aab8caa747ab2dc70e45d18807d57079b16d4eb` at both — **byte-identical, confirmed** |

A's conclusion that **PEC is the only product whose SOW basis is current** is correct and is the sharpest single comparator in either report.

**Severity / class commentary.** **REVIEW is right**, class *trace gap (basis currency)* is right. I add one observation supporting A's consequence paragraph: because the two missing amendments are SCA-APP-003 (runtime to Root) and SCA-APP-004 (target UI), the stale-basis region coincides exactly with the region under active dispute at RA-002/RA-003 and at my own RB-001/RB-005. The staleness is not uniformly distributed; it is concentrated where change is fastest.

---

## WARN/INFO sample — 5 findings (minimum 3)

**Sampling record and rationale.** I sampled 5 of the 10 WARN/INFO findings, chosen on stated criteria rather than at random: **RA-011** and **RA-012** because they sit on cross-product boundaries where my horizontal lens is best placed to test A's vertical reasoning; **RA-013** because it asserts the same *clause-granularity* failure mechanism my own M1 identified on a different commitment, so it tests whether the mechanism generalises; **RA-016** because it is a fully machine-checkable census over all 45 Root contracts and therefore audits A's measurement method itself; and **RA-017** because it is a *positive* verification claim and positive claims deserve challenge as much as negative ones — it is also the control on which RA-005 depends. I did not sample RA-009, RA-010, RA-014, RA-015, or RA-018; of these, RA-010 and RA-014 overlap my own RB-009 and RB-010 closely enough that independent challenge would add little, and RA-015's blob claim I incidentally verified while testing RA-008 (Root `653fabc9b3e8` blob `1378c6b6012f235a52fcd60fd0a3b0fec39b1c3d` vs `da31c19b` blob `121d2274209f08a7175ede015b80fa63196cb3f5` — as A states).

---

### RA-011 — WARN — No routed D-GOV-26/27 notice reached PEC; Piping cites no D-GOV-20..27 record

**Verdict: CONFIRM** · **Confidence: HIGH**

Re-verified: `grep -rl "D-GOV-26\|D-GOV-27" projects/pec/` → **0 files**. Files citing `D-GOV-2[0-7]`: `projects/chirality-app-dev/execution/_Coordination` = **20**; `projects/pec/execution/_Coordination` = **2**; `domains/chirality` = **4**; `domains/chirality-piping` = **0**. **All four counts match A exactly.**

**Severity commentary.** **WARN is right**, and A's MEDIUM on materiality is well-calibrated (neither downstream loop is currently acting on instruction-surface membership). I note the finding gains force from A's own RA-006: the same supersession failed to reach a *Root* contract, so the propagation weakness is not confined to inter-loop notice routing — which is A's point and is correct.

---

### RA-012 — WARN — `PEC-K-03` and `PEC-K-11` impose obligations on consumers with no assigned owner

**Verdict: CONFIRM** · **Confidence: MEDIUM** (matching A's own calibration)

Re-verified: PEC PRD §6 `PEC-K-03` (line 158) — *"Polling is performed by harnesses at moments of consequence … The only agent behavior is verify-before-rely"*; `PEC-K-11` (line 166) — *"Consumption follows §5; zero-coordination modes remain zero-contact"*; §8 line 222 — *"Agents — never call PEC directly by instruction."* The decomposition carries both as constraints only: `C3` (line 109) and `C15` (line 121), under DL-7's rule that invariants become scope items only *"where they require built or verified behavior."* `SOW-086` (line 265) is `OUT`, **Deferred**, *"owner act on the root doctrine surface."*

**A's characterisation holds.** Both invariants are satisfied by behaviour on surfaces PEC does not own (the runtime daemon and hooks CLI under D-GOV-20; agent instructions under `AGENTS.md`), and no routed obligation reaches an owner who could. A's **MEDIUM** and explicit **UNKNOWN** on whether these are wholly PEC-internal design constraints is the right calibration and I do not upgrade it.

**Commentary — complementary, not duplicative.** This finding is the mirror image of my own RB-007 and the manager should not treat them as one issue: A found **consumer-side** obligations of PEC invariants unowned; I found **producer-side** dependencies of PEC deliverables unowned (the event-contract home, the daemon global event feed, auth-token reuse — PEC `SOW-074`/`SOW-076`/`SOW-080`/`SOW-083`). Together they establish that the PEC↔runtime boundary is unowned in *both* directions, which neither finding shows alone. **WARN is right** for A's half, since these are honesty/proportionality properties rather than correctness dependencies — consistent with `PEC-K-01`.

---

### RA-013 — WARN — Root PRD `O-1`'s membership clause has no scope item

**Verdict: CONFIRM** · **Confidence: HIGH**

Re-verified: `SOW-026`'s statement is *"The shared instruction surface is release-managed and read-mostly, and changing it is a repo-wide governance action rather than ordinary working-root execution."* — the **second** clause of O-1 only, with `SourceRef: PRD §5.2 O-1 [TRANSCRIBED]`. The forward register marks `O-1` `COVERED`.

**Evidence I add — stronger than A stated.** A reports that a search of the 103 statements returns `SOW-022`, `SOW-026`, `SOW-080`, *"none carries membership."* I ran the complementary test: searching all 103 `ScopeItemStatement` values for **any instruction-surface member name** (`init/`, `AGENTS.md`, `skills/`, `CLAUDE`) returns **zero rows**. Not one of the 103 scope items names a single member of the surface whose membership `DEL-02-01` exists to register. The enumeration is absent from the ledger entirely, which is a stronger statement than "no row carries membership."

**Severity commentary.** **WARN is right** as A grades it, and A's **MEDIUM** on whether it is consequential independently of RA-006 is fair. I record that this is structurally the same defect my own M1 identified on `O-2` — a multi-clause commitment normalized into one scope item, where the register cannot see the missing clause, while `N-1`, `N-5` and `D-14` *were* split for exactly this reason (DEC-004/DEC-005). Two reviewers found the same mechanism on two different commitments independently. That convergence is itself worth carrying to fan-in: it suggests the defect is systematic in the normalization step, not incidental to either commitment.

---

### RA-016 — INFO — Root candidate AC/VER status is not machine-determinable

**Verdict: CONFIRM** · **Confidence: HIGH**

Re-verified across all 45 Root contracts. Frontmatter keys are exactly `schema`, `deliverable_id`, `package_id`, `decomposition_basis`, `project_scope_refs`, `package_objective_refs` — **no status field**, as A states. All **45** contain the word "candidate". Distinct declaration forms and their counts:

```
5  Every `AC-*` and `VER-*` defined here is a candidate.        (A: AX-004 ×3 + AX-005 ×1 + AX-002 ×1 = 5 ✓)
4  definitions below are candidate content for owner review.
4  Every `AC-*` and `VER-*` below is a **candidate**.
4  Candidate status.
2  criteria above are therefore candidate definitions authored under this contract.
```

A's sub-claim that *"only 13 of 45 use the explicit `AC-*`/`VER-*` formulation"* reproduces exactly: **13 of 45**.

**Severity commentary.** **INFO is right** — consequence is genuinely low while nothing is `ISSUED`, and A says so. A's smallest action (one optional frontmatter field in the shared SOW method layer under D-GOV-16) is well-routed and would serve all three loops. I note it is the same instrument my own RB-008 targets for a different optional field; the manager may wish to consider whether one method-layer tranche should carry both.

---

### RA-017 — INFO (positive) — Root and PEC registers are fully internally consistent; SOW layers reproduce register truth

**Verdict: CONFIRM** · **Confidence: HIGH**

I tested this positive claim as adversarially as the negative ones, with my own parsers.

| Check | A's claim | My result |
|---|---|---|
| Root ledger `DeliverableIDs` ↔ register `CoversScopeItems` | 0 mismatches | **0** across 103 ledger / 45 register rows |
| PEC ledger ↔ `Deliverables.csv` | 0 mismatches | **0** across 94 / 64 rows |
| Root SOW frontmatter `project_scope_refs` vs register | 0/45 | **0/45**; objective refs also **0/45** |
| PEC SOW frontmatter vs register | 0/32 | **0/32**; objective refs also **0/32** |
| App SOW frontmatter vs §8 | 0/51 | **0/51**; objective refs also **0/51** |

All confirmed. A's characterisation of this as *the control for RA-005* is methodologically sound: the identical test that produced 7 App mismatches produces 0 in both products that maintain an authoritative companion register, which is real evidence that the App defect is attributable to the missing register rather than to reviewer method.

**Commentary.** **INFO is right.** I want to record explicitly that a reviewer publishing a positive verification result, and using it as a control against their own negative finding, is good practice and materially raised my confidence in A's App findings. The App result (0/51 frontmatter agreement with §8) is also what independently proves the mechanism in RA-004.

---

## Verdict tally

| Verdict | Count | Findings |
|---|---:|---|
| **CONFIRM** | **12** | RA-002, RA-003, RA-004, RA-005, RA-006, RA-007, RA-008, RA-011, RA-012, RA-013, RA-016, RA-017 |
| **ADD-MISSING-EVIDENCE** | **1** | RA-001 |
| **REFUTE** | **0** | — |
| **NARROW** | **0** | — |
| **Total challenged** | **13** | 8 BLOCK/REVIEW (all) + 5 WARN/INFO (sampled) |

**No finding of A's was refuted or narrowed.** Every load-bearing quantitative claim I re-derived reproduced exactly, including two full censuses (130 contracts) and three bidirectional register comparisons. The only errors found were two non-load-bearing details in A's evidence — the "five of six" section count at RA-001 (actually three, with the mitigating conclusion holding for all six by a different mechanism) and "six packages" at RA-002 (actually seven, which understates the finding). Neither affects any assertion.

**Severity divergences recorded (not resolved):** RA-002 and RA-003 — A grades REVIEW, I graded the same two conditions BLOCK in my own pass 1. The facts are identical and now jointly re-verified from opposite lenses; the divergence follows from differently drawn observation boundaries, both internally consistent and both declared. **Agreed-on-fact, divergent-on-severity.**

---

## Out-of-scope observations for fan-in

No IDs, no severities — offered for the manager's disposition, not asserted as findings.

1. **A seventh level-two heading in three App contracts.** `DEL-02-01`, `DEL-02-02` and `DEL-02-04` each carry `## SCA-APP-004 Gate-5 Current Contract (Controlling)` at line 18, in addition to the six level-two headings the ratified standard specifies *"in order"* (`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §3). Neither report's register covers heading-set conformance, so neither reviewer tested whether this is permitted. Surfaced because it emerged while correcting RA-001's mitigating clause.

2. **Both reports converge on the missing App companion register from opposite directions.** A reaches it as register-integrity failure (RA-005, RA-014); I reached it as the absent surface that would have mapped invariants to owners (my RB-010). The manager may wish to classify these as one shared root cause rather than parallel findings, since a single corrective act discharges both.

3. **Two independent findings of the same clause-granularity normalization defect.** A found it on Root PRD `O-1` (RA-013); I found it on `O-2` in my M1. Both are multi-clause commitments collapsed into a single scope item where the register cannot see the omission, in a decomposition that split `N-1`, `N-5` and `D-14` for precisely that reason. Whether this is systematic in the normalization step is not something either report tested, and it may deserve a targeted check across the remaining 100 scope items.

4. **App's SOW validation era remains UNKNOWN.** A records this at §0.5 and it is not resolved by the manifest, which fixes eras only for Root and PEC (basis condition 15). It bears directly on how much of RA-007's measured divergence is method-era rather than loop rigour, and neither reviewer could settle it from the frozen basis.

5. **A pass-1 coverage gap of mine, disclosed.** I did not test `decomposition_basis` object resolvability in my own pass, which is why RA-001 does not appear in any form in my report. Recorded so fan-in does not read my silence on it as disagreement.

---

**Boundary compliance.** Evidence drawn only from `/Users/ryan/dev/chirality-review-frozen-da31c19` @ `da31c19b` (verified clean, HEAD unchanged, no git-state change, no repo script run). Exactly one file written: this one. `REVIEWER_B_REPORT.md` not modified. `CHALLENGE_A_ON_B.md`, `CHALLENGE_BRIEF_A.md` and `BRIEF_REVIEWER_A.md` not read. No new findings minted.
