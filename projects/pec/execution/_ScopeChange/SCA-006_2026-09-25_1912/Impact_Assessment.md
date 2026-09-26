---
amendment_id: SCA-006
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-25
status: awaiting_checkpoint_1_acceptance
authority: D-PEC-90 R-A grant item 3 and D-PEC-94 (Gate 1 opened by owner direction; see Decision_Log.md SCA006-G1); checkpoint group 1 NOT accepted
workflow: chirality-root:bundled:workflow:scope-change
---

# SCA-006 — Checkpoint-group-1 Impact Assessment

> **Status: PROPOSED, awaiting owner acceptance.** This document proposes a
> change set and states its impact. It changes no PRD, `projects/pec/AGENTS.md`,
> decomposition, register, pointer, Scope of Work, SPEC, `_CONTEXT.md`,
> `_STATUS.md`, `v2/**` or foreign byte. The owner accepts it, if at all, by
> the exact SHA-256 of this file as quoted in `Decision_Log.md` row
> SCA006-CP1 and the run return (a file cannot quote its own hash). Nothing
> here is a ruling. Exact amendment prose belongs to checkpoint group 2.

Abbreviations: **Seq n** = row n of `Amendment_Actions.csv` in this snapshot;
**D90-P** = `_DECISIONS/D-PEC-90_agent_reliance_on_pec_data_proposal_2026-09-25.md`;
**D90-R** = `_DECISIONS/D-PEC-90_RULING_2026-09-25.md`; **Lnnn** = a line of
the file named, at `origin/main` `13df8b795e47ab2284018eeefc9d5473d00c232d`;
**recommended set** = DQ-a + ENV-a + BUD-a + GATE-a + INS-a (§12).

## 1. Impact verdict

SCA-006 is a **product-authority and constraint amendment with a small,
topology-preserving decomposition delta**. It writes the owner's D-PEC-90
direction into PEC's product definition and instructions:

- **Operational reliance replaces verify-before-rely.** An agent, directly or
  through its harness, may act on a PEC record-tier claim as true as of the
  examined-through commit, within the pin, coverage and tier the response
  declares, with file fallback (PEC-K-03, C3, §8, AGENTS.md K-02 gloss).
- **Authority is unchanged.** PEC output stays non-authoritative in the
  authority sense and never citable; PEC-K-01, PEC-K-02, K-AUTH-1, `D-GOV-01`
  and Root PRD N-1 stand. R-C stays excluded.
- **Direct query through tool calls** enters §8 and a new PEC-API-007, with a
  read-only `agent` access class (recommended DQ-a). The token mechanism stays
  the open §16.6 decision.
- **The reliance envelope** (PEC-ORI-007) and **response-size budgets**
  (PEC-API-006, the D-PEC-91 carry-forward) become requirements.
- **A standing §12 gate** bars any release from advertising reliance until
  parity, coverage honesty, the envelope, parser fixtures and the kill test are
  proved. Reliance begins at such a release, not now (D90-R).

In the recommended set it keeps all 11 packages and 6 objectives, preserves
every stable ID, adds 4 scope items (`SOW-097..100`, all IN) and 2 deliverables
(`DEL-08-06`, `DEL-10-13`), modifies 3 deliverable rows, 3 packages, 2 objective
views, 5 other ledger/constraint/issue rows and 1 vocabulary term, adds 3
vocabulary terms, and records 13 PRD and 4 instruction loci as
product-authority and instruction inputs outside the decomposition. Its main
cost is derivative: **9 of the 32 existing Scope of Work contracts** (§7.1),
the DEL-00-03 SPEC, four dependency EvidenceQuotes, two new deliverables to
set up, and consumer notices.

Checkpoint group 1 is **not accepted** by this document.

## 2. Evidence basis

| Evidence | SHA-256 / result |
|---|---|
| Brief B4 (manager scratchpad; not in the repository) | `87612acaa41fb3975a87fddd6a97803a4968e0f0d1d1df837ce0373e82d0ae90`, plus two HELP_HUMAN addenda received in-session (quoted in `Brief.md`) |
| D-PEC-90 ruling / proposal | `43a0c663c1a57a95001f0470cabb0d36bab098754867ecfe6c30127e7de5efab` / `b04a8aa25c1d402fb03f6f15b6fb1eb27a0110e5cd3f3ded1db3717649a5e147` (the ruling's selected hash; match) |
| D-PEC-91 ruling (carry-forward) | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| D-PEC-94 record | `eb9793aaaf3b618c911f34db43220d8bf5bf7093fafb0ac9c375a5f6456a5e81` |
| D-PEC-67 record / K03-A accepted input | `c04f8ddd90cfe4ca3ecdabad8f48b4820c9952c9c4515655dc8ed21304d9d9a8` / `7f43efe4b963e73bcda49777ca38d54c3f4989f1cfb8c39e93b22b2c8b31f200` |
| D-PEC-70 (PEC-HOLD-001 release) | `eff5f66b1ba5198321c19f3507822dbb25f70f08683fafe85ca0dcf9231991eb` |
| SCA-005 group-2 decision (D-PEC-92; grant precondition) | `checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md` `ca88f6a8f9bca197f64a56f07c73364cd8f7533acb7bf64206a34e0e1fba3d66` |
| PRD v2.3 live | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` (= `_Decomposition/_LATEST.md` basis) |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| SOFTWARE_DECOMP revision 1.5 | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` (match) |
| `ScopeLedger.csv` / `Deliverables.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` / `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` (match) |
| `ContextBudgetQA.csv` / `Companion_Inventory.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` / `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| DEL-04-01 SOW / DEL-00-03 SPEC | `6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae` / `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` (both equal D90-P's pins) |
| Root `AGENTS.md` / `docs/PRD_ROOT.md` / `docs/CONTRACT.md` | `c8ce87ef…ffd` / `b6fa4e3d…931` / `64747d2a3c58ae93194bd5c7118d89a591b7b4ebe8cec7e88cb6a95dc55895bd` (full hashes in `Handoff_State.md`) |
| D-GOV-43 A2 supplement | `fa3756ad3bdf02104da47fc5ba697b4f96d8a02029f008b32bd96a094ec46cb2` |
| Runtime `APPLICATION_TOOLS.md` / `APPLICATION_CONSUMER_GUIDE.md` | `59e401d14d566814983ba4c242b8449b71ecdb6f3dec1134289c51f836cc307b` / `2f9f37788a17be9c5030c631dbb53be2f1b59a325bd51bc5bf6ac4e86a781865` |
| Tier-0 profile `_DomainEngines/profiles/pec.yaml` | `6858d567ee27bae9b832115a40a41b106a9a2a58a62d661ca0e0c2acff9b314f` |
| Locus inventory (TASK child A1; manager scratchpad, not committed) | `INVENTORY.csv` 232 rows `bfcad344…c682`; `SOW_POPULATION.csv` 32 rows `5829902f…4143`; quote verifier `failures=0` (264 checks). Every locus this document relies on is re-cited here by file, line and quotation. The child classed 7 SOWs AFFECTED; the manager classes 9, adding DEL-04-03 (scope growth) and DEL-00-03 (stale requirement-count premise), see §7.1 |
| Pre-change baseline | `Pre_Change_Coverage.json` = byte copy of `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/coverage_summary.json` (`b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d`, `cmp` identical); reuse justified in §2.1 |
| Baseline result | `WARNINGS`: 0 blockers / 3 warnings / 70 info; 11/11 packages; 66/66 deliverables and contexts (62 active, 4 retired); 96 ledger rows (70 IN / 18 OUT / 8 TBD); 0 IN rows and 0 active deliverables without an objective |
| Strict register validator (before) | 66 registers / 263 dependency rows / 0 errors / 0 warnings, exit 0 |
| Reliance-hold preflight | `ALLOW` (exit 0), operation `exact-correction-preparation`, for `docs/PRD.md`, `AGENTS.md`, `SOFTWARE_DECOMP.md`, `ScopeLedger.csv`, `Deliverables.csv` and this snapshot; the register has a header and no rows |

### 2.1 Pre-change baseline: reuse, not a fresh run

The method (part A step 5) asks for a pre-change `audit-decomp` baseline.
`COV_SCA005_POSTSETUP_2026-09-25_1606` is the latest audit and the
`_Evaluation/DecompCoverage/_LATEST.md` target. It audited commit
`995af4f368d0d8cc0b3134eef484b4b9618aa8ac`, an ancestor of `origin/main`
`13df8b795`. `git diff --name-only 995af4f36 13df8b795` over every audit input
(`_Decomposition/`, `_ScopeChange/`, `docs/PRD.md`, every `execution/PKG-*`
folder and `v2/`) is **empty**. The only PEC changes since are the loop
migration (`AGENTS.md`, `loop/`, `init/`), `README.md`, `docs/STATUS.md` and
`_Coordination/**` records, none of which the audit reads. The audited state
is therefore the current pre-change state byte for byte, and a fresh run would
re-audit identical inputs. The baseline is reused, and no pre-change audit
folder is created. A post-change audit remains mandatory at checkpoint 3.

### 2.2 Basis drift during preparation

The package was prepared against `origin/main` `13df8b795`, and every line
number and hash above is a pin at that commit. Before publication the branch
merged `origin/main` `bec8bdd65` (PRs #919 and #920). That merge changed these
files:

- `D-PEC-94`: an owner-confirmation section was added about `D-PEC-88`, taking
  the file from `eb9793aa…5e81` to
  `b6814e902c23f24020337ab925a7c287b66b5ee485785bee07b042e25e1e5a6b`. The
  direction quoted in `Decision_Log.md` is unchanged.
- `_DECISIONS/_REGISTER.md`: `031adae3…a2f7` →
  `19a385c898d50b9dfc8d754a5cc9c84c29f0116e321eeafe29eed21a00dc64a3`.
- The work graph, which is now on `main`:
  `WORK_GRAPH.md` `f669ebe53d483419799e5c947ea903996187570e608f3ee2b849030c0ec00f78`.
- PEC records: `docs/STATUS.md`, the prior run's `RUN.md`, and review returns
  for PR #919.
- Unrelated research-workflow files: Root skill, workflow and tranche-manifest files, and one App-loop notice (`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-26_RESEARCH_CONTRACT_ALIGNMENT.md`).

No PRD, `projects/pec/AGENTS.md`, decomposition file, companion or dependency
register, Scope of Work, SPEC or `_CONTEXT.md` changed, so every locus in this document still
holds at `bec8bdd65`. The drift is not material.

## 3. Parsed change set and part-A validation

`Amendment_Actions.csv` holds **54 PROPOSED actions** for the recommended set.
Every Description is prefixed `PROPOSED`. `SupersessionBindingPresent = NO` for
every row, because `Supersession_Delta.csv` is a checkpoint-2 artifact; the
candidate bindings are listed in §9.3.

| By ActionType | Count | | By EntityType | Count |
|---|---:|---|---|---:|
| ADD | 12 | | OTHER (PRD, instruction, ledger, constraint, issue, section, derivative rows) | 31 |
| MODIFY | 42 | | DELIVERABLE | 14 |
| REMOVE / RECLASSIFY / MERGE / SPLIT | 0 | | VOCAB_TERM | 4 |
| | | | PACKAGE | 3 |
| | | | OBJECTIVE | 2 |

Cross-tab: ADD 3 PRD requirements (OTHER) / 4 scope items (OTHER) / 2
DELIVERABLE / 3 VOCAB_TERM; MODIFY 10 PRD loci / 4 instruction loci / 6
decomposition OTHER rows (C3, §1.2, SOW-003, SOW-060, SOW-080, OI-006) /
2 section rows (telemetry, traceability) / 3 DELIVERABLE register rows /
3 PACKAGE / 2 OBJECTIVE / 1 VOCAB_TERM / 11 derivative advisories (9
DELIVERABLE Scope of Work rows, the SPEC, the EvidenceQuotes).

| Group | Seq | Content | Surface class |
|---|---|---|---|
| K — PRD | 1–13 | PEC-K-03; §8 Agents and access classes; §1.1; new PEC-ORI-007, PEC-API-006, PEC-API-007; §12 reliance gate and P3 row; §11 metric 4; §15; §16.6; header v2.4 | product authority, outside the decomposition |
| I — instructions | 14–17 | `projects/pec/AGENTS.md` K-02 gloss, consumer-use bullet, lineage and pointers, checks table | PEC instruction file, outside the decomposition |
| D — decomposition | 18–43 | C3; §1.2; SOW-003/060/080; OI-006; new SOW-097..100; new DEL-08-06, DEL-10-13; DEL-04-03/08-01/08-03 rows; PKG-04/08/10; OBJ-001/002 views; vocabulary; telemetry; traceability | canonical working package |
| S — derivative | 44–54 | nine Scope of Work contracts, the DEL-00-03 SPEC, four EvidenceQuotes (three registers) | derived artifacts; rerun advisories only |

**Part-A validation** (deterministic script over the live registers and PRD;
per-action table in Annex A): **54/54 PASS**. The script checks the following
mechanically for every row: enums, file existence, ID presence or absence,
parent presence, the K-03 clause and the vocabulary terms. For 18 rows (Seq
2–4, 8–17, 19, 42, 43, 53, 54) it confirms only enums and file existence. Their
loci rest on Annex B and on the child inventory's byte-exact quote verifier
(264 checks), and the independent verifier spot-checked them. For the group-S
deliverable rows (44–52) the script checks that each deliverable exists; the
quote verifier checks their Scope of Work loci.

- Every MODIFY target exists: SOW-003 (IN), SOW-060 (IN), SOW-080 (TBD),
  C3, OI-006, PKG-04/08/10, OBJ-001/002, the `harness` term, DEL-04-01/02/03,
  DEL-08-01/03/04, DEL-03-04, DEL-10-03 and DEL-00-03. PEC-K-03 and its
  verify-before-rely clause are present at PRD L212. Loci addressed by
  section are pinned to the lines in Annex B.
- The ADD IDs are unused and well-formed. `PEC-ORI-007`, `PEC-API-006` and
  `PEC-API-007` are absent from the PRD; the PRD holds 46 `PEC-*-NNN`
  requirements, and the ORI and API families already exist, so PRD §14's
  family list is unaffected. `SOW-097..100` append after `SOW-096`.
  `DEL-08-06` follows `DEL-08-05` and `DEL-10-13` follows `DEL-10-12`; their
  parents PKG-08 and PKG-10 exist. The three new vocabulary terms are absent
  from §9. None of these IDs occurs anywhere under `_Decomposition/`,
  `PKG-*` or `docs/`.
- Each new scope item is co-added with its covering deliverable (SOW-097 →
  DEL-04-03, SOW-098 → DEL-08-03, SOW-099 → DEL-08-06, SOW-100 → DEL-10-13) and
  objective.
- Every `AffectedFiles` path exists.
- Columns and enums match the contract schema.
- `AMENDMENT_ID = SCA-006`: `tools/query/scan_next_amendment_id.sh` (zsh)
  returned `SCA-006` before this folder existed, and PEC's `_ScopeChange/`
  held SCA-001..SCA-005. Cross-loop readers should qualify it as PEC's.

**Contract-type notes.**

- PRD and instruction loci are recorded as `OTHER` rows whose application is
  outside the decomposition, following the SCA-005 precedent (its Seq 75–76).
  PRD text is product authority. The amendment to it is accepted at
  checkpoint 2 and applied with the decomposition at checkpoint 3, as SCA-005
  did for v2.3.
- The new PRD requirements are `ADD` of `OTHER` entities. They create no
  decomposition entity until their SOW rows (Seq 24–27) are added.
- The 11 group-S rows are `MODIFY` with a rerun-advisory propagation effect
  (contract Action Types table). Their `AffectedFiles` name the derivative
  file that the **owning workflow** changes later, under its own packet. SCA-006
  writes none of them. This keeps every consequence in the register without
  presenting it as a Lane A write.

**Parent-closure and variant-local rules.**

- No package is removed, merged, split or reclassified. No REMOVE action
  exists, so no child-closure set is open.
- Package-discipline isolation (DL-3, DL-12): DEL-08-06 is a read-side PKG-08
  slice that writes nothing and consumes only the versioned API. DEL-10-13 is a
  PKG-10 validation deliverable that composes other packages' evidence and
  consumes no internals, like DEL-10-02.
- Artifact-kind granularity: each new deliverable holds one artifact kind (a
  tool-call query adapter, a gate test suite).
- DL-6 convention: the §12 gate enters as its own IN item (SOW-100), distinct
  from the behaviours it tests (SOW-020, SOW-009, SOW-097, SOW-055), and its
  Notes cross-link them.
- DL-7: PEC-K-03 stays a constraint (C3), not a scope item.
- Context envelopes: no deliverable reaches XL. DEL-08-03 S → M is
  recommended (§8.2).

## 4. Impact summary by action

| Seq | Action | Sections / files | Workflows affected |
|---|---|---|---|
| 1 | PEC-K-03 → operational reliance | PRD §6 L212 | PRD amendment; C3 (Seq 18); SOW re-quotes (44–47); SPEC (53); App/Root/Runtime notices (R4) |
| 2 | §8 Agents: act on data and query through tool calls | PRD §8 L273–282 | DEL-04-02, DEL-08-01, DEL-08-03 SOWs |
| 3 | §8 access classes + `agent` | PRD §8 L283–286 | SOW-003 (20), DEL-08-01 row (31), DEL-08-01/08-03/08-04/10-03 SOWs |
| 4 | §1.1 thesis | PRD L74–78 | §1.2 mirror (19) |
| 5 | + PEC-ORI-007 reliance envelope | PRD §9.1 | SOW-097 (24), DEL-04-03 (30, 48), PKG-04 (33), OBJ-001/002 |
| 6 | + PEC-API-006 response budgets | PRD §9.6 | SOW-098 (25), DEL-08-03 (32, 47) |
| 7 | + PEC-API-007 tool-call surface | PRD §9.6 | SOW-099 (26), DEL-08-06 (28), PROJECT_SETUP |
| 8 | §12 reliance-advertisement gate | PRD §12 | SOW-100 (27), DEL-10-13 (29), DEL-03-04 SOW (49), AGENTS checks (17) |
| 9 | §12 P3 row | PRD L415 | none beyond Seq 7 |
| 10 | §11 metric 4 candidate consumers | PRD L391–404 | SOW-060 (21); DEL-10-12 (no SOW yet) |
| 11 | §15 D-PEC-67 bullet + D-PEC-90 bullet | PRD L513–516 | none (lineage) |
| 12 | §16.6 premise | PRD L563–567 | SOW-080 (22), OI-006 (23) |
| 13 | header v2.4 | PRD L1–62 | AGENTS lineage (16); decomposition front matter (43) |
| 14–17 | AGENTS.md | `projects/pec/AGENTS.md` L39–50, L26–33, L180–189, L409 | instruction tranche, notices |
| 18–23 | C3, §1.2, SOW-003/060/080, OI-006 | `SOFTWARE_DECOMP.md`, `ScopeLedger.csv` | AUDIT_DECOMP |
| 24–29 | four SOW rows, two deliverables | `ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv`, `SOFTWARE_DECOMP.md` §2/§5 | PROJECT_SETUP (folders), dependency-extract, SOW authoring |
| 30–32 | DEL-04-03/08-01/08-03 rows | `Deliverables.csv`, three `_CONTEXT.md` | AUDIT_DECOMP; context mirrors |
| 33–41 | packages, objective views, vocabulary | `SOFTWARE_DECOMP.md` §3, §4, §9 | AUDIT_DECOMP |
| 42–43 | telemetry, traceability | §5–§8, front matter, `Companion_Inventory.csv`, pointers | AUDIT_DECOMP, HELP_HUMAN (after checkpoint 3) |
| 44–54 | derivative advisories | nine SOWs, SPEC, four EvidenceQuotes in three `Dependencies.csv` | WORKING_ITEMS (S1/S4), DEL-00-03 owner (D1), dependency-extract |

## 5. Expected decomposition-state delta (recommended set)

| Measure | Revision 1.5 (now) | Revision 1.6 (after SCA-006) |
|---|---|---|
| Packages | 11 | 11 |
| Objectives | 6 | 6 (statements unchanged) |
| Scope items | 96 (70 IN / 18 OUT / 8 TBD) | 100 (74 IN / 18 OUT / 8 TBD) |
| Deliverable rows | 66 (62 active, 4 retired) | 68 (64 active, 4 retired) |
| Envelopes, active S / M / L | as `ContextBudgetQA.csv` | +DEL-10-13 S; +DEL-08-06 M; DEL-08-03 S → M |
| Constraints | C1–C16 | C1–C16 (C3 re-expressed) |
| Open issues | 10 open / 3 resolved | unchanged count; OI-006 premise extended |
| Vocabulary | 26 terms | 29 terms (+3; `harness` modified) |
| IN items / active deliverables without objective | 0 / 0 | 0 / 0 |
| Stable IDs reused or renumbered | — | none |
| PRD | v2.3, 46 requirements | v2.4, 49 requirements (+ORI-007, API-006, API-007) |

## 6. Package-role and derivative-surface classification

| Surface | Package role | SCA-006 treatment | Authority basis |
|---|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | working surface | DIRECT_EDIT at checkpoint 3 | accepted checkpoint-2 amendment |
| `ScopeLedger.csv`, `Deliverables.csv` | authoritative companion registers | DIRECT_EDIT | same |
| `ContextBudgetQA.csv` | authoritative companion register | RECOMPUTE (three rows) | same |
| `Companion_Inventory.csv` | authoritative companion register | RECOMPUTE (counts) | same |
| `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` | snapshot / handoff artifacts | DIRECT_EDIT after checkpoint-3 acceptance only | checkpoint 3 |
| This snapshot folder | snapshot / handoff artifact | written now (checkpoint-1 files only) | Gate 1 |
| `docs/PRD.md` | product authority outside the decomposition | exact v2.4 candidate at checkpoint 2, applied at checkpoint 3 | checkpoint 2 |
| `projects/pec/AGENTS.md` | PEC instruction file | exact text at checkpoint 2; applied as an instruction tranche (INS-a) | checkpoint 2 + tranche manifest |
| `_CONTEXT.md` of DEL-04-03, DEL-08-01, DEL-08-03 | variant-local metadata (SOFTWARE propagation default) | DIRECT_EDIT of mirrored description only | checkpoint 2 propagation plan |
| Nine `ScopeOfWork.md` (§7.1) | derived publication artifacts | NO_CHANGE by SCA-006; STALE for their owners | owning WORKING_ITEMS packets |
| DEL-00-03 `artifacts/v2/SPEC.md` | derived artifact (CHECKING) | NO_CHANGE by SCA-006; STALE_REVIEW_REQUIRED | DEL-00-03 owner, exact-byte gate |
| Four `Dependencies.csv` EvidenceQuotes (DEP-09-06-003/-004, DEP-10-03-003, DEP-10-12-004) | derived register cells | NO_CHANGE by SCA-006; refresh advisory | dependency-extract |
| `_REFERENCES.md` (66) | variant-local metadata | NO_CHANGE: all cite the PRD by path only; version re-pin is graph node N2 | — |
| Other `_CONTEXT.md` (63) | variant-local metadata | NO_CHANGE: none quotes K-03 or the access classes | — |
| `v2/contracts/api/v1/schema.json`, `v2/docs/*` | source tree (fenced) | NO_CHANGE; additive schema evolution can carry budgets and envelope later | own D-PEC packet |

## 7. Derivative packages and owning reruns

### 7.1 Scope of Work population, deliverable by deliverable

Scope: all 32 existing `ScopeOfWork.md` files. The other 34 deliverables have
no Scope of Work. The two new deliverables will need first ones. A contract is
`AFFECTED` when it quotes or restates text that SCA-006 changes, or when the
scope it covers changes. Classification is for the recommended set; the
option column gives the change under other options. Line numbers are at
`13df8b795`.

| Deliverable | Class | SOW locus (line, text) | PRD / decomposition text SCA-006 changes | Under other options |
|---|---|---|---|---|
| DEL-04-01 | **AFFECTED** (fixed member) | CLM-016 L266 "and any injection is optional and subject to verify-before-rely"; AX-007 L363 "may choose whether to inject subject to verify-before-rely"; REQ-010 L290 and trace L400 cite CLM-016 | PEC-K-03 L212 (Seq 1); §8 L279–282 (Seq 2). D90-P locus table; D90-R grant item 1 bars rebuilding it around verify-before-rely | always affected |
| DEL-04-02 | **AFFECTED** | CLM-016 L225 "and optional injection is subject to verify-before-rely" and "the accepted corpus names possible consumers only at one remove"; REQ-013 L252; L363 provenance note claims §8 quotations the file does not contain | PEC-K-03 L212; §8 L279–282 (direct query makes "one remove" false) | always affected |
| DEL-08-01 | **AFFECTED** | CLM-004 L92 "...optionally injects labeled non-authoritative data are consumer-owned decisions subject to verify-before-rely"; L55 "access classes are owner, harness, and admin."; REQ-003 L107 "exactly owner, harness, and admin"; REQ-004 L108 | PEC-K-03; §8 L283–286 (Seq 3); SOW-003 (Seq 20) | DQ-b/c: still AFFECTED through CLM-004 |
| DEL-08-03 | **AFFECTED** | REQ-005 L256 (labeled non-authoritative injection; harnesses as the machine consumers); REQ-006 L257 "No accepted source states a size metric, threshold, or budget for compactness"; AC-006 L274; CON-001 L286; VER-006 L321; CLM-009 L229 "the three token-scoped access classes" | PEC-K-03; §8; PEC-API-006 (Seq 6); SOW-098 added to its coverage | BUD-b: still AFFECTED (PEC-API-004 re-expressed) |
| DEL-04-03 | **AFFECTED** (scope growth) | quotes no changed text (L146 cites SOFTWARE_DECOMP §8 Context Budget QA; L220 names access classes only as DEL-08-01's act) | its coverage gains SOW-097 / PEC-ORI-007 (Seq 24, 30) | ENV-b: still AFFECTED (PEC-ORI-003 extended) |
| DEL-03-04 | **AFFECTED** (review level) | CON-001 L248 "Whether this deliverable's parity gate carries *release-gating authority* is unconfirmed."; CON-002 L249 "or explained" undefined; AC-016 L296 | §12 reliance gate (Seq 8) makes both load-bearing | GATE-b: still AFFECTED (P1 row) |
| DEL-08-04 | **AFFECTED** (DQ-a) | CLM-011 L288 "implementing the three token-scoped access classes is `DEL-08-01`"; L266 and REQ-007 L314 assign size metrics to DEL-08-03 (true under BUD-a); L274 cites PRD §8 (true); CLM-010 L287 quotes the §12 P1 row, which GATE-a leaves unedited | §8 class count (Seq 3) | DQ-b/c: NOT_AFFECTED unless GATE-b; GATE-b: AFFECTED through L287 |
| DEL-10-03 | **AFFECTED** (DQ-a) | CLM-008 L191 "exactly one of the access classes owner, harness, and admin" | §8 class count (Seq 3); the new class must also be in the no-ruling-write negative surface | DQ-b/c: NOT_AFFECTED |
| DEL-00-03 | **AFFECTED** (review level, premise only) | CLM-006 L77 "The 46 PEC-\*-NNN requirements"; CLM-004 L70 "(46 requirements / 64 deliverables)". Both quote sources SCA-006 does not edit (the §1.4 intake posture and a `Deliverables.csv` cell), so both quotes stay verbatim. The classification rests only on the contract's premise that the PRD holds 46 requirements | requirement count 46 → 49 (Seq 5–7) | ENV-b + BUD-b + DQ-c: NOT_AFFECTED (no new requirement) |
| DEL-01-05 | NOT_AFFECTED | L66 cites PRD §8 only for the local-only, token-scoped posture via PEC-API-001 | none (PEC-API-001 unchanged; its v2.2 quotation is SCA-005 residue) | same |
| DEL-01-06 | NOT_AFFECTED | no K-03, verify-before-rely, §8, access-class, auth, size or parity text; AX-001/AX-002 (L93–94) cite K-01/K-02 in the authority sense | none | same |
| DEL-01-01 | NOT_AFFECTED | L90 (CLM-007) cites SOFTWARE_DECOMP §8 Context Budget QA, not PRD §8; REQ-006 "non-authoritative" concerns Runtime user data | none | same |
| DEL-02-03 | NOT_AFFECTED | L104 (CLM-007) cites SOFTWARE_DECOMP §8 | none | same |
| DEL-10-11 | NOT_AFFECTED | CON-004 L213 and AC-015 L255 leave gating to a later ruling; the gate is defined over DEL-03-04's parity output, not the metric; L185 quotes DEL-03-04 CON-001, which quotes the unedited P1 row | none (GATE-a does not gate on metric 5) | AFFECTED if the gate is defined over metric 5, or under GATE-b (L185) |
| DEL-10-01 | NOT_AFFECTED | L77 quotes §11 metric 1 and the falsification clause | Seq 10 edits metric 4 only; the falsification clause keeps its meaning | same |
| DEL-10-02 | NOT_AFFECTED | kill test (PEC-K-01) unchanged; CLM-004 L125 quotes the §12 P1 row, which GATE-a leaves unedited; "fault injection" unrelated | none | GATE-b: AFFECTED (L125) |
| DEL-10-10 | NOT_AFFECTED | "relied on" (L339, L354) means DAG nodes consuming accepted capabilities (C16); L137 quotes the §12 P1 row, which GATE-a leaves unedited | none | GATE-b: AFFECTED (L137) |
| DEL-03-01 | NOT_AFFECTED | CON-005 L405 quotes the P1 exit fragment "rebuild-from-scratch ≤ bound", which GATE-a leaves unedited | none | GATE-b: AFFECTED (L405) |
| DEL-03-06 | NOT_AFFECTED | CLM-016 L373 quotes the §12 P1 exit test, which GATE-a leaves unedited | none | GATE-b: AFFECTED (L373) |
| DEL-00-01 | NOT_AFFECTED | cites K-02 only (L45, L82); its ADR artifact cites K-03/K-11 for "not a new consumer duty", which stays true | none | same |
| DEL-04-05 | NOT_AFFECTED | states coverage honesty (PEC-ORI-006) with no non-reliance premise; the gate cites it as an input | none | GATE-b: AFFECTED (it becomes a P1 exit proof) |
| DEL-01-03, DEL-01-04, DEL-02-01, DEL-02-02, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07, DEL-03-02, DEL-03-03, DEL-08-02 | NOT_AFFECTED (11) | no verify-before-rely, K-03, PRD §8, access-class, auth-reuse, response-size or parity-gate text; "reliable input" and "Completion and Reliance Basis" are template boilerplate in the professional sense | none | same |

Totals (recommended set): **9 AFFECTED, 23 NOT_AFFECTED** of 32.

**Proposed S4 set.** The work graph on `origin/main` `bec8bdd65`
(`WORK_GRAPH.md` `f669ebe5…0f78`) defines S4 as "The set that checkpoint 2
fixes". It lists candidates from a grep of `5570fd095`: DEL-04-01, DEL-04-02,
DEL-08-01, DEL-08-03, DEL-01-01, DEL-01-05, DEL-02-03, DEL-04-03 and
DEL-08-04. This table is the checkpoint-1 proposal for that set:

- **Proposed S4:** DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04 and
  DEL-04-03.
- **Review-level (S1 or D1):** DEL-03-04, DEL-10-03 and DEL-00-03.
- **Grep candidates found not affected:** DEL-01-01, DEL-02-03 and DEL-01-05.
  The first two cite SOFTWARE_DECOMP §8; DEL-01-05 cites only the unchanged
  local-only posture.
- **DEL-01-06** is NOT_AFFECTED on its own evidence. This matches the graph,
  which places it in S2 after G1.

DEL-08-06 and DEL-10-13 need first Scope of Work contracts after
PROJECT_SETUP. The child inventory classed 7 of these SOWs AFFECTED. The
manager adds DEL-04-03 (its scope grows) and DEL-00-03 (its premise goes
stale).

### 7.2 Other derivative packages

| Package | Owner | Status after SCA-006 | Required action |
|---|---|---|---|
| DEL-00-03 `SPEC.md` (CHECKING) | DEL-00-03 owning workflow (graph D1) | `STALE_REVIEW_REQUIRED` (already so under SCA-005) | premise-only amendment: K-03 row L46, counts L23/L62, API row L73, release list L78 (Seq 53) |
| DEL-00-01 `ADRs.md` | DEL-00-01 owner | `CURRENT` for SCA-006 | none |
| `Dependencies.csv` EvidenceQuotes DEP-09-06-003, DEP-10-03-003, DEP-10-12-004, and DEP-09-06-004 (BUD-a, if the checkpoint-2 wording changes the DEL-08-03 sentence it quotes) | dependency-extract | `STALE_REBUILD_REQUIRED` once Seq 31, 32 or 34 apply | verbatim refresh (Seq 54) |
| New DEL-08-06, DEL-10-13 folders and registers | PROJECT_SETUP under its own D-PEC packet | absent | create folders, `_CONTEXT/_STATUS/_REFERENCES/_DEPENDENCIES`, extract dependencies |
| `_REFERENCES.md` PRD version pins (66) | graph node N2 | stale on version only | re-pin with N2 or after checkpoint 3 |
| Post-change `audit-decomp` | TASK audit-decomp | `NOT_RUN` | at checkpoint 3 |
| `docs/STATUS.md`, `README.md` | HELP_HUMAN under `D-PEC-88` | may name PRD v2.3 or verify-before-rely | refresh at closeout; STATUS L48 uses "professional reliance" in another sense |

### 7.3 Downstream sequence (recommended; none authorized here)

1. Owner accepts checkpoint 1 → group-1 decision snapshot.
2. Checkpoint 2: PRD v2.4 exact candidate, decomposition revision 1.6 text,
   AGENTS.md text with its tranche manifest, `Supersession_Delta.csv`, and the
   propagation plan.
3. Checkpoint 3: apply; post-change audit; independent review.
4. Graph R4: notices. Then S4 (the K-03-bound SOWs), D1 (SPEC), PROJECT_SETUP
   for DEL-08-06 and DEL-10-13, and the dependency refresh.

### 7.4 Surfaces PEC cannot write (notice only)

| Surface | Owner | Relation to SCA-006 |
|---|---|---|
| Root `AGENTS.md` L54–55 "Search results and derived graphs help locate evidence; reliance remains grounded in the source records and their authority." | Root | Arguably compatible: a pinned, cited, deterministic derivation from source records is reliance grounded in them. That reading is Root's to confirm. PEC sends a notice (R4). A Root instruction change would need Root's own scope |
| Root `docs/PRD_ROOT.md` N-1 "rebuildable gitignored projections are permitted and never citable as authority; if a decision is not in a versioned file it does not exist for purposes of reliance" | Root | Unaffected: PEC stays uncitable; decisions stay file-native. "Reliance" here is authority reliance, not operational reliance |
| Root `docs/CONTRACT.md` K-AUTH-1 "No agent may claim to certify, approve, sign, seal, or issue work for reliance." | Root | Unaffected: operational reliance issues nothing and approves nothing. The new vocabulary term keeps the senses apart |
| Root `docs/CONTRACT.md` K-RUNTIME-1 and D-GOV-43 A2 | Root / Runtime loop | Unaffected. The Runtime owns sessions, tools and turn admission. A Runtime-hosted PEC tool would be an application's registration (Runtime `APPLICATION_TOOLS.md`), and the consumer guide forbids pointing a new consumer at the running App's socket or token file. PEC supplies a tool surface; it never adds a Runtime path |
| App loop consumers of PEC-K-03 (the row adopted by D-PEC-67 K03-A in coordination with consumer loops) | App loop | Notice (R4). Each consumer decides its own adoption; K-03 and K-11 keep consumer-owned use |
| Runtime loop | Runtime | Graph R4 sends a Runtime notice only if the checkpoint-2 plan names one. The manager recommends that the plan name it, because PEC-API-007 touches the tool path that K-RUNTIME-1 and the Runtime's application-tools interface own. Any notice is non-binding |
| `_DomainEngines/profiles/pec.yaml` L81 "profile amendment before any runtime, adapter-client, mutating, proposal, or external-result tool is declared or invoked" | tier-0 (D-T0-27) | Implementing or invoking the PEC-API-007 tool surface needs that separate tier-0 act. SCA-006 states the requirement only |

## 8. Authority boundary and governance compliance

### 8.1 What changes and what does not

| Stays exactly as it is | Changes |
|---|---|
| PEC-K-01 graceful absence, and the kill test at every release | PEC-K-03's verify-before-rely clause gives way to operational reliance within the declared pin, coverage and tier |
| PEC-K-02: output never citable as authority; rulings and lifecycle file-native | "non-authoritative" is kept, in the authority sense only |
| K-AUTH-1: only humans author binding approval records | §8: agents may act on PEC data and query through tool calls |
| `D-GOV-01` Option A: rebuildable projection, never cited as authority | §9: new envelope and budget requirements; §12: new gate |
| Root PRD N-1 | AGENTS.md K-02 gloss |
| PEC-K-06: no dispatch, no leases, gate verdicts advisory | — |
| PEC-K-11 byte-identical to the D-PEC-67 row | — |
| The L-A1 reliance-hold control (`ACTIVE_RELIANCE_HOLDS.csv`, `pec_reliance_hold.py`; PEC-HOLD-001 released by D-PEC-70) | — |
| §16 decisions open (C12), including §16.6 | §16.6 premise widened to agent credentials only |

**Why this stays within `D-GOV-01`, N-1 and K-AUTH-1.** These instruments bar
projections from being authority. They do not bar acting on a derivation.
Under SCA-006 a governed record still cites the file, never PEC (PEC-K-02).
A ruling, acceptance, lifecycle transition or merge still rests on the
file-native record. Deleting PEC still blocks nothing (PEC-K-01), because every
reliance is bounded by a file fallback. "Operational reliance" is a product
behaviour of PEC's consumers. It is not "issuing work for reliance" (K-AUTH-1),
nor reliance on a decision that exists only outside versioned files (N-1).
R-C, reliance including authority, would need Root governance acts and would
give up the kill test. It stays excluded.

**Gate verdicts.** D90-P lists "which gate preconditions hold" as a reliance
use, while PEC-GAT-002 and §4.1 keep verdicts advisory. The two agree: an agent
may act on a verdict operationally (for example, choosing what to prepare),
but the governed gate is decided from the files. No action is proposed.

### 8.2 PEC-owned versus notice-only surfaces

PEC-owned and amended through SCA-006: `docs/PRD.md`, `projects/pec/AGENTS.md`,
the decomposition package, the `_CONTEXT.md` mirrors, and later, by their
owners, the Scope of Work contracts, SPEC and registers named in §7.
Notice-only: Root and the App loop, per the D-PEC-90 grant, and the Runtime loop if the checkpoint-2 plan names it (§7.4). The tier-0 profile
needs its own act. D-PEC-90 grant item 2's notices were already sent for the
direction. The R4 notices announce the adopted text.

### 8.3 Instruction change

Seq 14–17 amend PEC's instruction file. Root `AGENTS.md` requires "their own
authorized scope and tranche manifest" for instruction changes, and notices
to each affected loop. INS-a carries them at checkpoint 3 as a tranche with a
manifest, prepared at checkpoint 2 (the D-PEC-94 precedent). Graph node I1 may
ride the same tranche. The K-02 gloss must not tell agents to rely on PEC
today: no consumer surface exists, so the new text scopes reliance to a
release whose gate has passed.

## 9. Orphan, invariant and telemetry risk

### 9.1 Structural and register invariants

- No orphan: every new SOW has a package, deliverable and objective. Every new
  deliverable has a parent package, covers a scope item and supports OBJ-001.
  No REMOVE exists.
- Dependency closure: DEL-08-06 and DEL-10-13 enter with no register until
  PROJECT_SETUP. They must not be reported as isolated defects in the
  post-change audit before setup. Expected edges, for extraction:
  - DEL-08-06 on DEL-08-01, DEL-08-02, DEL-08-03 and DEL-04-01;
  - DEL-10-13 on DEL-03-04, DEL-04-03, DEL-04-05, DEL-10-02 and the PKG-02
    parser deliverables.
  The closure tool must stay acyclic.
- Strict register validator: expected unchanged at 0/0. Dependency registers
  change only in their four EvidenceQuote cells, and only after the refresh.
- Objective invariant: 0 IN items and 0 active deliverables unmapped, before
  and after.

### 9.2 Context-envelope risk

DEL-08-03 grows from one requirement (compact, cited responses) to two, and
the budget adds pagination, continuation and stated-truncation semantics.
AX-002 already warns that a cap must never be met by dropping citations or
stated absences. S → M is recommended, with risk LOW. DEL-04-03 stays M with
one added claim class. DEL-08-01 stays M/MEDIUM: the agent class is one more
enumeration, and OI-006 still governs the token half.

### 9.3 Supersession and authority-conflict risk (candidate bindings for checkpoint 2)

| Candidate | Action | Superseded authority fact | Type |
|---|---|---|---|
| SB-1 | Seq 1 | the PEC-K-03 row in `docs/PRD.md` (L212 at v2.3), whose bytes D-PEC-67 K03-A adopted: "If it injects PEC data, verify-before-rely is an interface precondition; injection is not required." The K03-A accepted input (`OD7-G3_APPLICATIONS/D-PEC-67/sections/05_K03-A/ACCEPTED_INPUT.md` L20–21) says the same thing in other words: "If a consumer injects PEC data, verify-before-rely is an interface precondition; it does not require injection." Checkpoint 2 binds the PRD row's exact value | SUPERSESSION (owner ruling D-PEC-90 R-A authorizes) |
| SB-2 | Seq 2 | D-PEC-68 v2.2 §8 Agents concordance "never call PEC directly by instruction under the current access classes" | SUPERSESSION |
| SB-3 | Seq 3 | PRD v2.0 §8 (D-PEC-58) "access classes are owner, harness, and admin" | SUPERSESSION (DQ-a) or SUPPLEMENTARY_EXTENSION (DQ-b clarifies) |
| SB-4 | Seq 18 | C3 wording derived from SB-1 | SUPERSESSION (derived) |
| SB-5 | Seq 5–8 | none contradicted (new requirements and gate) | SUPPLEMENTARY_EXTENSION |
| SB-6 | Seq 11 | PRD §15 claim of K-03 byte identity | SUPERSESSION (lineage statement) |

D-PEC-67's required route ("PEC SCOPE_CHANGE must propagate C3 and C15 and
every mapped affected surface") applies again. C15 (K-11) does not change.

### 9.4 Terminology risk

"Reliance" already carries three other senses in PEC and Root text:

- the L-A1 hold (AGENTS.md L362–387, `rely-for-production`, DL-18);
- professional reliance (K-AUTH-1, AGENTS.md L419, STATUS L48,
  `v2/docs/SERVICE_CORE_POSTURE.md`);
- authority reliance (N-1, Root AGENTS.md L55).

Unqualified "reliance" in the new text would blur them. Seq 38 adds
"operational reliance" with a disambiguation, and checkpoint-2 text must
always qualify the word. None of the other uses changes.

### 9.5 Observed-fact risks

- **Stale line citations.** The D90-P line numbers are v2.2 lines: K-03 was
  L177 and is now L212; §8 was L240–243 and is now L279–282. D90-R paraphrases
  §16.6 as "the daemon's token registry", but v2.3 reads "reuse of a Runtime
  token registry". Checkpoint-2 text quotes v2.3.
- **Loci the D-PEC-90 table did not name.** C3, the DEL-04-02 and DEL-08-01
  SOWs, the DEL-08-03 size clauses and PRD §15 were found by the inventory and
  are carried here.
- **SCA-005 residue** is corrected only where SCA-006 already edits the same
  text: PRD P3 "daemon consumers" (Seq 9), SOFTWARE_DECOMP L45 "PRD v2.2"
  (Seq 19), DEL-08-01 L48/L127 and DEL-03-04 L105 (advisories). The rest stays
  with its owners.

## 10. Estimate, schedule and phase effects

- **Estimate and schedule.** None exists for PEC v2 yet, so nothing goes
  stale. Two deliverables are added (DEL-08-06 at P3, DEL-10-13 from P1) and
  one envelope grows.
- **Phase effects.** P1 deliverables gain scope: DEL-04-03 takes the reliance
  envelope (SOW-097), and DEL-08-03 takes the response budgets (SOW-098; S →
  M), with numeric budgets confirmed at P1 (PEC-API-006). Both carry PhaseHint
  P1. Only the reliance gate (DEL-10-13) is conditional: it binds a release
  that advertises reliance. P3 gains the tool-call surface. §16 "None of the remaining open decisions
  blocks P0–P2" stays true.
- **Reliance timing.** Nothing is relied on now. The first release that
  advertises reliance must pass DEL-10-13.

## 11. Active snapshot and handoff impact

`_ScopeChange/_LATEST.md` keeps naming SCA-005 (`CLOSED_FOR_SCOPE_CHANGE_ONLY`)
until SCA-006 checkpoint 3 is accepted. This folder is an interim checkpoint-1
package, not an active snapshot. The pointer posture for a later checkpoint 3
is `ACCEPTED_PREDECESSOR` (SCA-005). SCA-005's own open derivative items (N1–N3
currency, SOW currency, D1) are not closed by SCA-006. Several of them (S4, D1)
now wait on both.

## 12. Recommended downstream reruns

| Rerun | When | Owner |
|---|---|---|
| audit-decomp post-change | checkpoint 3 | TASK (WORKING_ITEMS dispatch) |
| strict register validator; dependency closure | checkpoint 3 and after setup | WORKING_ITEMS |
| PROJECT_SETUP for DEL-08-06, DEL-10-13 + dependency-extract | after checkpoint 3, own D-PEC packet | PROJECT_SETUP |
| EvidenceQuote refresh (4 cells) | after checkpoint 3 | dependency-extract |
| SOW currency for the 9 AFFECTED contracts; first SOWs for DEL-08-06 and DEL-10-13 | after checkpoint 3 (graph S4/S1) | WORKING_ITEMS per packet |
| SPEC premise amendment | after checkpoint 3 (graph D1) | DEL-00-03 owner |
| Notices to Root and App (D-PEC-90 grant); Runtime if the checkpoint-2 plan names it (recommended) | after checkpoint 3 (graph R4) | HELP_HUMAN |

## 13. Option deltas (so the owner can switch at checkpoint 1 without a re-run)

Recommended: **DQ-a + ENV-a + BUD-a + GATE-a + INS-a** (54 actions: 12 ADD /
42 MODIFY).

### 13.1 Direct query through tool calls (CP1-DQ)

| Option | What it says | Action-set delta vs DQ-a | SOW population delta |
|---|---|---|---|
| **DQ-a (recommended)** — specify now, with a read-only `agent` access class | Least privilege: an owner can enable agent query without giving the tool host harness ingest rights. Calls are attributable per class (PEC-K-09). §16.6 still decides the token mechanism | — | — |
| DQ-b — specify now, riding the `harness` class | The tool host is treated as a harness acting for the agent; no fourth class | drop Seq 20 (SOW-003) and 31 (DEL-08-01 row), 41 (`harness` term), 50 and 51 (DEL-08-04, DEL-10-03 advisories); Seq 3 becomes a clarifying MODIFY ("tool hosts query under the harness class"). **49 actions** (12 ADD / 37 MODIFY) | DEL-08-04 and DEL-10-03 → NOT_AFFECTED (7 AFFECTED) |
| DQ-c — defer behind a new §16 access-class decision | §8 records the direction ("may eventually query directly through tool calls; access class and surface open"); no tool surface now | drop Seq 3, 4, 7, 9, 10, 15, 20, 21, 28, 31, 41, 50, 51; Seq 26 becomes `ADD SOW-099` **TBD** with a new `OI-014` (+1 ADD OI row) and a new PRD §16 item 10 (+1 ADD); PKG-08 and OBJ-001 lose SOW-099/DEL-08-06. **43 actions** | DEL-08-04, DEL-10-03 → NOT_AFFECTED; DEL-00-03 stays AFFECTED if ENV-a or BUD-a |

### 13.2 Reliance envelope (CP1-ENV)

- **ENV-a (recommended):** a new PEC-ORI-007 → SOW-097 → DEL-04-03. The
  envelope is a separately testable declaration, distinct from stamping.
- **ENV-b:** fold it into PEC-ORI-003 (MODIFY) and SOW-006 (MODIFY), with no
  new ID. Delta:
  - Seq 5 ADD → MODIFY PEC-ORI-003, and Seq 24 ADD → MODIFY SOW-006;
  - drop Seq 33 (the PKG-04 count) and Seq 37 (the OBJ-002 view);
  - Seq 30 keeps its description edit, but coverage is unchanged.

  The action count is 52, and the requirement count becomes 48.

### 13.3 Response-size budgets (CP1-BUD)

- **BUD-a (recommended):** a new PEC-API-006 → SOW-098 → DEL-08-03. Numeric
  values are confirmed at P1, since no measurement exists to set them now.
- **BUD-b:** extend PEC-API-004 "compact" (MODIFY) and SOW-043 (MODIFY). Delta:
  Seq 6 and Seq 25 become MODIFYs, and Seq 32 has no coverage change.
  The action count stays 54, with one fewer ADD per replaced row.
- **Not offered:** stating numeric budgets now, with no evidence behind them.

### 13.4 Reliance gate (CP1-GATE)

- **GATE-a (recommended):** a standing gate that binds any release
  advertising reliance, through SOW-100 and DEL-10-13. It is re-proved at each
  such release, which matches D90-R's "a PEC release whose gates prove the
  conditions".
- **GATE-b:** extend the §12 P1 exit test to add coverage and envelope proofs,
  with no new deliverable. Delta:
  - drop Seq 27, 29 and 35;
  - Seq 8 re-targets the P1 row;
  - add MODIFY rows for SOW-009 and SOW-020 notes, and for the DEL-04-05 and
    DEL-03-04 descriptions (+4);
  - add group-S advisories for the SOWs that quote the P1 row, whole or as a
    fragment, or become P1 exit proofs: DEL-04-05, DEL-10-02 (L125),
    DEL-10-10 (L137), DEL-03-06 (L373), DEL-10-11 (L185) and DEL-03-01
    (L405) (+6). DEL-08-04 (L287) is already an advisory under DQ-a; under
    DQ-b or DQ-c it is added (+1). DEL-03-04 (L105, L223, L248) already has
    one.

  The action count is 61 with DQ-a. The SOW population becomes **15 AFFECTED**
  (the 9 above plus DEL-04-05, DEL-10-02, DEL-10-10, DEL-03-06, DEL-10-11 and
  DEL-03-01).
  Risk: reliance is proved only once, at P1, and later phases would need their
  own restatement. Under GATE-a the P1 row text is not edited, so these
  quoting SOWs stay current.

### 13.5 Instruction route (CP1-INS)

- **INS-a (recommended):** checkpoint 3 applies Seq 14–17 as an instruction
  tranche with its own manifest and notices, so PEC's instructions never lag
  the PRD. I1 may join the same tranche.
- **INS-b:** a separate tranche after checkpoint 3. The action set is
  unchanged, but for a window the PRD says operational reliance while
  AGENTS.md still says "verified against its cited source before reliance".
  That window is harmless while no consumer surface exists.

### 13.6 R-C (CP1-RC)

R-C is excluded under D-PEC-90, where the owner selected R-A. Including it
would add Root amendments to `D-GOV-01` and N-1 (outside PEC), remove the
PEC-K-02 "never citable" clause and weaken PEC-K-01. It is not priced as an
option.

## 14. Candidates considered and not carried

- **§11 metric 2 (spot-check defect rate).** It becomes the quality measure for
  reliance, but its text stays true. No action; DEL-10-04 (no SOW) may note it.
- **PEC-RCN-005, PEC-ORI-006 and C10.** They stay true. The gate (Seq 8) gives
  them their new role without editing them.
- **PEC-GAT-002 and §4.1 "advisory".** Consistent; see §8.1.
- **§1.4 Gate-1 intake posture ("PRD v2.2 … 46 requirements").** This is
  history, and SCA-005 left it too. The traceability row (Seq 43) records the
  choice.
- **§14 identifier families.** No new family is used.
- **`v2/contracts/api/v1/schema.json`.** It has no pagination, size,
  access-class or envelope fields. Additive evolution (PEC-API-003) allows
  them later under a source packet.
- **`docs/STATUS.md` and `README.md`.** HELP_HUMAN maintains them under
  `D-PEC-88`, outside this snapshot.
- **`_REFERENCES.md` version pins.** These belong to graph N2, not SCA-006.

## 15. Checkpoint-group-1 owner question set

Answer these at checkpoint 1. The manager's recommendation is in brackets.

1. **CP1-A — change set.** Confirm or modify the parsed change set in
   `Amendment_Actions.csv` (54 PROPOSED actions at the SHA-256 quoted in
   `Decision_Log.md`). [confirm]
2. **CP1-B — impact.** Accept this Impact Assessment at its exact SHA-256, as
   quoted in `Decision_Log.md` row SCA006-CP1 and the run return. [accept]
3. **CP1-DQ — direct query.** Should §8 direct query through tool calls be
   specified now with a read-only `agent` access class (a), specified now
   under the `harness` class (b), or deferred behind a new §16 access-class
   decision (c)? The token mechanism stays §16.6 in every case. [a]
4. **CP1-ENV — reliance envelope.** A new PEC-ORI-007 mapped to DEL-04-03 (a),
   or folded into PEC-ORI-003 (b)? [a]
5. **CP1-BUD — response budgets.** A new PEC-API-006 mapped to DEL-08-03, with
   numbers confirmed at P1 (a), or folded into PEC-API-004 (b)? [a]
6. **CP1-GATE — reliance gate.** A standing gate for any release that
   advertises reliance, with SOW-100 and DEL-10-13 (a), or an extension of
   the P1 exit test (b)? [a]
7. **CP1-INS — instruction route.** Carry the AGENTS.md change at checkpoint 3
   as an instruction tranche (a), or as a separate tranche afterwards (b)? [a]
8. **CP1-RC — R-C.** Confirm that R-C (PEC output citable as authority) stays
   excluded, as D-PEC-90 selected R-A. [confirm excluded]

To take every recommendation, the owner could answer:
"SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded."
This asks nothing about CHECKING, ISSUED or acceptance of any deliverable.

## Annex A — Part-A validation per action

Deterministic validation over the live PRD, `SOFTWARE_DECOMP.md`,
`ScopeLedger.csv` and `Deliverables.csv` at `13df8b795`. The result is 54/54
PASS, with 0 failures. Rows whose Basis column gives only line ranges (Seq
2–4, 8–17, 19, 42, 43, 53, 54) were checked mechanically for enums and file
existence only. Their loci rest on Annex B and on the child's quote verifier,
as §3 explains. Eight quote spot-checks were also byte-present: the
K-03 clause, the §8 Agents and access-class sentences, the §15 D-PEC-67
bullet, §16.6, the P3 row, the C3 clause and the AGENTS.md gloss.

| Seq | Type | Entity | EntityID | Group | Option tag | Result | Basis |
|---:|---|---|---|---|---|---|---|
| 1 | MODIFY | OTHER | PEC-K-03 | K | all | PASS | K-03 row and clause present (L212) |
| 2 | MODIFY | OTHER | PRD-S8-Agents | K | all | PASS | L273–282 |
| 3 | MODIFY | OTHER | PRD-S8-AccessClasses | K | DQ-a | PASS | L283–286 |
| 4 | MODIFY | OTHER | PRD-S1.1-Thesis | K | DQ-a/b | PASS | L74–78 |
| 5 | ADD | OTHER | PEC-ORI-007 | K | ENV-a | PASS | ID unused; §9.1 L292 |
| 6 | ADD | OTHER | PEC-API-006 | K | BUD-a | PASS | ID unused; §9.6 L345 |
| 7 | ADD | OTHER | PEC-API-007 | K | DQ-a/b | PASS | ID unused; §9.6 L345 |
| 8 | MODIFY | OTHER | PRD-S12-RelianceGate | K | GATE-a | PASS | §12 L408–440 |
| 9 | MODIFY | OTHER | PRD-S12-P3 | K | DQ-a/b | PASS | L415 |
| 10 | MODIFY | OTHER | PRD-S11-Metric4 | K | DQ-a/b | PASS | L391–404 |
| 11 | MODIFY | OTHER | PRD-S15-Governance | K | all | PASS | L513–516 |
| 12 | MODIFY | OTHER | PRD-S16.6 | K | all | PASS | L563–567 |
| 13 | MODIFY | OTHER | PRD-Header-v2.4 | K | all | PASS | L1–62 |
| 14 | MODIFY | OTHER | PEC-AGENTS-K02-gloss | I | all | PASS | AGENTS.md L40–43 |
| 15 | MODIFY | OTHER | PEC-AGENTS-ConsumerUse | I | DQ-a/b | PASS | L47–50 |
| 16 | MODIFY | OTHER | PEC-AGENTS-Lineage | I | all | PASS | L27–32, L180–189 |
| 17 | MODIFY | OTHER | PEC-AGENTS-ChecksTable | I | GATE-a/b | PASS | L409 |
| 18 | MODIFY | OTHER | C3 | D | all | PASS | row present L118 |
| 19 | MODIFY | OTHER | S1.2-Intake | D | all | PASS | L43–86 |
| 20 | MODIFY | OTHER | SOW-003 | D | DQ-a | PASS | present (IN) |
| 21 | MODIFY | OTHER | SOW-060 | D | DQ-a/b | PASS | present (IN) |
| 22 | MODIFY | OTHER | SOW-080 | D | all | PASS | present (TBD) |
| 23 | MODIFY | OTHER | OI-006 | D | all | PASS | row present L642 |
| 24 | ADD | OTHER | SOW-097 | D | ENV-a | PASS | unused; > SOW-096 |
| 25 | ADD | OTHER | SOW-098 | D | BUD-a | PASS | unused |
| 26 | ADD | OTHER | SOW-099 | D | DQ-a/b | PASS | unused |
| 27 | ADD | OTHER | SOW-100 | D | GATE-a | PASS | unused |
| 28 | ADD | DELIVERABLE | DEL-08-06 | D | DQ-a/b | PASS | unused; PKG-08 present |
| 29 | ADD | DELIVERABLE | DEL-10-13 | D | GATE-a | PASS | unused; PKG-10 present |
| 30 | MODIFY | DELIVERABLE | DEL-04-03 | D | ENV-a | PASS | present |
| 31 | MODIFY | DELIVERABLE | DEL-08-01 | D | DQ-a | PASS | present |
| 32 | MODIFY | DELIVERABLE | DEL-08-03 | D | BUD-a | PASS | present |
| 33 | MODIFY | PACKAGE | PKG-04 | D | ENV-a | PASS | L382 |
| 34 | MODIFY | PACKAGE | PKG-08 | D | all | PASS | L386 |
| 35 | MODIFY | PACKAGE | PKG-10 | D | GATE-a | PASS | L388 |
| 36 | MODIFY | OBJECTIVE | OBJ-001 | D | all | PASS | L335 |
| 37 | MODIFY | OBJECTIVE | OBJ-002 | D | ENV-a | PASS | L336 |
| 38 | ADD | VOCAB_TERM | operational reliance | D | all | PASS | absent from §9 |
| 39 | ADD | VOCAB_TERM | reliance envelope | D | ENV-a/b | PASS | absent |
| 40 | ADD | VOCAB_TERM | response budget | D | BUD-a/b | PASS | absent |
| 41 | MODIFY | VOCAB_TERM | harness | D | DQ-a | PASS | present L619 |
| 42 | MODIFY | OTHER | S7-S8-telemetry | D | all | PASS | L392, L530, L536–601 |
| 43 | MODIFY | OTHER | SCA-006 | D | all | PASS | traceability loci |
| 44 | MODIFY | DELIVERABLE | DEL-04-01 | S | all | PASS | present; SOW L266, L363 |
| 45 | MODIFY | DELIVERABLE | DEL-04-02 | S | all | PASS | SOW L225 |
| 46 | MODIFY | DELIVERABLE | DEL-08-01 | S | all | PASS | SOW L92, L55, L107 |
| 47 | MODIFY | DELIVERABLE | DEL-08-03 | S | all | PASS | SOW L256, L257, L274, L286, L321, L229 |
| 48 | MODIFY | DELIVERABLE | DEL-04-03 | S | ENV-a/b | PASS | coverage change |
| 49 | MODIFY | DELIVERABLE | DEL-03-04 | S | all | PASS | SOW L248, L249, L296 |
| 50 | MODIFY | DELIVERABLE | DEL-08-04 | S | DQ-a | PASS | SOW L288 |
| 51 | MODIFY | DELIVERABLE | DEL-10-03 | S | DQ-a | PASS | SOW L191 |
| 52 | MODIFY | DELIVERABLE | DEL-00-03 | S | all | PASS | SOW L70, L77 |
| 53 | MODIFY | OTHER | DEL-00-03-SPEC | S | all | PASS | SPEC L46, L23, L62, L73, L78 |
| 54 | MODIFY | OTHER | DEP-EvidenceQuotes | S | all | PASS | three `Dependencies.csv` paths (four cells) exist |

## Annex B — PRD and instruction loci (current text; needed change; no bytes changed here)

| Locus (v2.3 line) | Current text (exact, abridged with …) | Needed change (Seq) |
|---|---|---|
| PRD L5 / L7 | "**Version** \| 2.3"; "**Adopted 2026-09-25** by owner acceptance of SCA-005 checkpoint group 2" | v2.4; SCA-006 adoption act (13) |
| PRD L74–75 | "It is available to explicitly PEC-enabled consumers, including harnesses acting on behalf of agents" | add agents querying through tool calls (4) |
| PRD L212 | "If it injects PEC data, verify-before-rely is an interface precondition; injection is not required." | operational reliance within pin, coverage and tier; file fallback (1) |
| PRD L279–282 | "never call PEC directly by instruction under the current access classes. They may receive orientation as labeled, non-authoritative data only if an explicitly enabled consumer chooses to inject it" | act on data received through an enabled consumer; query directly through tool calls (2) |
| PRD L285–286 | "…are retired; access classes are owner, harness, and admin." | + read-only `agent` (3, DQ-a) |
| PRD §9.1 (after L301) | no reliance-envelope row | + PEC-ORI-007 (5) |
| PRD §9.6 (after L353) | "PEC-API-004 \| Responses are compact, machine-first, and citation-bearing." — no size budget anywhere | + PEC-API-006 (6), + PEC-API-007 (7) |
| PRD L391–396 | "Candidate consumers are registered loops or harnesses for which PEC exposes a compatible interface" | + enabled agent tool-call surfaces (10) |
| PRD §12 (L408–440); P1 L413 "Parity-diff vs harness clean or explained; rebuild-from-scratch ≤ bound; kill test passes" | no coverage or reliance gate | + standing reliance-advertisement gate (8) |
| PRD L415 | "PEC-side interfaces/adapters usable by hooks CLI or daemon consumers" | + tool-call surface; "daemon" re-expressed (9) |
| PRD L513–516 | "PEC-K-03 and PEC-K-11 remain byte-identical to the rows adopted by D-PEC-67." | K-11 only; K-03 amended under D-PEC-90; + D-PEC-90 compliance bullet (11) |
| PRD L563–567 | "6. Auth reuse: PEC tokens vs reuse of a Runtime token registry." | premise includes agent tool-call credentials; stays open (12) |
| AGENTS.md L40–43 | "PEC output is never citable as authority. … A PEC value, view, or verdict is labeled non-authoritative data, verified against its cited source before reliance." | keep the first sentence; replace the second with gated operational reliance (14) |
| AGENTS.md L47–50 | "PEC is pull-oriented, mode-capable, and never forced. An explicitly enabled consumer owns whether and when it consumes and whether it injects labeled PEC data" | + agent tool-call consumers; envelope (15) |
| AGENTS.md L26–32; L180–189 | "`docs/PRD.md` v2.3 is the product definition of record"; register pointer list | v2.4, D-PEC-90, SCA-006 (16) |
| AGENTS.md L409 | "Product release/reconciliation work \| The packet's standing kill test and practitioner-harness parity diff" | + reliance gate for reliance-advertising releases (17) |
| SOFTWARE_DECOMP L118 (C3) | "and any injection is optional and verify-before-rely" | operational reliance (18) |
