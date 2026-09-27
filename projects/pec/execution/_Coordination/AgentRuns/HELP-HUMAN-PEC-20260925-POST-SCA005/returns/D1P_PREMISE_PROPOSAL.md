# Return — D1P: D1 derivative premise packet (provisional D-PEC-105), WORKING_ITEMS preparation

Manager: WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node D1. Brief `briefs/D1P_PREMISE_PROPOSAL.md` (`d1cdf4e3104d38a08e8bef8c3641070d942ec9ad2744bddeb9cadfb482cbc1f1`, copied unchanged) with `COMMON.md` (`51b70e46f1049696c456be1d4ab7b4b236e3cbfc6fa3a667ed0426035510b311`, session scratchpad); both hashes verified before reading. Model: Opus 5.5 (`claude-opus-5-5`), high, for the manager and every child (instruction-asserted). Preparation only: no production file was written; every check ran on `git archive` exports.

## Supersession note (2026-09-27, PR #997 review round)

The sections below were written at `4141b6428` and are kept as that return. HELP_HUMAN's independent review of PR #997 at `26c38d6ce` (PASS WITH NOTES) led to repairs verified by `VERIFIER_VERDICT_06.md` (PASS WITH NOTES). Where they differ, these current values supersede the values below:

- Candidates: DEL-00-03 SPEC `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` (unchanged, 207 lines); DEL-00-03 SOW `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` (172 lines; AX-009 tempered); DEL-00-01 ADRs `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` (182 lines; posture 3 names only the premise's own elements, no `codex app-server` child); add-on P `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` (152 lines; CLM-005/REQ-004 carry credentials custody and model-residency retirement, as posture 3 does).
- Act script `apply_d1p.py` `952a7512fd74e1b77f2f6b948d3cf46c876448ee1dee5370759f627236399d4d`, rendered at basis `f0a6159c9` (a `6c6cc1b00` rendering differs only in its comment line). Checklists: DEL-00-03 `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1`, DEL-00-01 `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9`. Runner `run_d1p_checks.sh` `80714ae4a69a8178d7726f095657e8c4297b8babbe9ed86933c2deacd8b0ed8e` (stores whitespace-clean `diff_<KEY>.diff.txt`).
- Checks at `origin/main` `f0a6159c9` (observation `6c6cc1b00`): OVERALL PASS; quotes 74/74; state claims 126/126; fault injection 24/24; evidence whitespace 0; negative controls 6/6; `git diff --check origin/main...HEAD` clean. External-quote scan: 82 STALE = 69 in history records + 13 scanner artefacts.
- The re-review options are named RR1–RR3; the variant is "REVIEW-before-merge" (act on the branch, then REVIEW and acceptance on that branch under a separate authorization, then merge); reading 4(a) is stated as beyond premise-only scope.
- The draft hash and final head are in the manager's final hand-back for this round.

## Publication

- **PR #997** (`https://github.com/sgttomas/chirality/pull/997`), base `main`, branch `claude/pec-d1-premise-proposal`, not merged. Head: see the final commit of this return on the branch (the draft and evidence are final at `4141b6428`). GitHub reported `mergeable: MERGEABLE`, `mergeStateStatus: BLOCKED` (checks pending / review required); no "Update the PR base" failure was seen.
- Worktree: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d1-premise-proposal` (own, from fresh `origin/main` `6c6cc1b00`).
- Prep folder: `projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/` (the session date when preparation began was 2026-09-26; the brief's placeholder said 2026-09-27, "use the actual date").

## Draft and candidates

- **Draft:** `PEC_D1_PREMISE_PREP_2026-09-26/DRAFT_D-PEC-105_d1_premise_amendment_proposal.md`, SHA-256 `710f2134ab5446ecddbffd6a28e3a3fc7608c5fbb9c7d4f6bd28c19e1f8b032f`.
- **Candidates** (each rendered from a premise ledger over the owner-accepted preimage; every byte outside the listed hunks is the preimage):

| Group | Target | Preimage | Postimage | Lines | Hunks |
|---|---|---|---|---|---|
| A | DEL-00-03 `artifacts/v2/SPEC.md` | `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` | 207 | 22 |
| A | DEL-00-03 `ScopeOfWork.md` | `3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741` | `a6b57d3f918931fe500559845a5d5beddfadbe75e797c8631c51f4abecd38156` | 172 | 15 |
| A | DEL-00-01 `artifacts/v2/ADRs.md` | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` | `9e6961ac0b1722e9df3496d46aed730f42fa5e037ec45c6598d290b04cff8387` | 183 | 6 |
| P (add-on) | DEL-00-01 `ScopeOfWork.md` | `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` | `f5090fb36fd739bc5db01ad08d0d53400854b46e78a53cc18dede77629fdf43f` | 152 | 3 |

- Bound act script `apply_d1p.py` `399a088b7b0e87176191326af3e1dfbc4258d9831548ce228859e109692f4f1a` (default writes group A; `--with-addon-p` writes A+P); checklists: DEL-00-03 `522917133070891145804df1a024bed8dfe17f83e93fb65ac6006e7ddef4fe11` (only AC-003's text changes, v2.2 → v2.4), DEL-00-01 `d48881d992bdd81bc7cc1916a68d5711872a7a40a631c95bf9a1c02fa011437f` (no AC text change).

## Recommendation

**A** (the three premise-only replacements, no lifecycle change), **with add-on P** (recommended together; see "For the caller"), **RR1** for re-review, readings 4(a) and 4(b) confirmed, **M** at closeout, default models.

## Owning-workflow identity

- Artifact production: WORKING_ITEMS under PKG-00 package activation `D-PEC-72-PKG-00-WI-01` (run `D-PEC-72-PRE-P1-FOUNDATION`; `DEL-00-01/_run_records/D-PEC-72_PKG-00_ACTIVATION.md`, authoritative copy), each artifact bound by its deliverable's `SOW_V1` contract, candidate-validated, then REVIEW (bundled `review`; DEL-00-01 `SELF_CHECK`, DEL-00-03 `PEER_REVIEW` rerun) and a separate owner act.
- Amendment practice: the 2026-08-09 route the owner named "the DEL-00-03 owning workflow" (TM-PEC-014: bounded WORKING_ITEMS candidate edit → deterministic checks → REVIEW rerun → owner `ACCEPT_EXACT_BYTES`; commit `e92a82ca9`). This packet follows it for the edit and checks; under ruling A the bytes land before any REVIEW (stated in the draft; a pre-act REVIEW variant is offered under Amend).
- Contracts: `chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT` discipline, exact-bytes act, `MODE=VERIFY`); REVISE disclosed in one line, not put to the owner.
- Hashes (at `6c6cc1b00`): `workflows/index.json` `2bfa2c5f…fb3`; `review/WORKFLOW.md` `99eae11d…07ab`, `execution.json` `d1c668ae…074df`, `resources/contract.md` `fdf25136…cb18`, `resources/method.md` `669f5585…52e`; `scope-of-work/WORKFLOW.md` `84dadde4…bc2b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`, `resources/checks.md` `44ab41ac…f188`, `resources/tools.md` `fbd07771…5cc7`; standard `26c8254a…433c`. No `MEMORY.md` exists in either deliverable.
- Instruction sources read (at `6c6cc1b00`): Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`; `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`; `agents/AGENT_WORKING_ITEMS.md` `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665`.

## Premise inventory (evidence in the draft's tables, the ledgers `premise/*.json`, and `quotes/`/`claims/`)

- **SPEC (22):** the uniform amendment note; PRD v2.2 → v2.4 and 46 → 49 (L17, L23, L62); the K-03 row (L46: operational reliance within the declared envelope, only past the §12 gate, never authority, file fallback); §3 rows ORI (+ORI-007, SOW-097), RCN scope (+SOW-095/096), PRS (live hierarchy deferred; SOW-029 OUT), STR (hooks CLI the only bridge; SOW-035/037 OUT), API (+API-006/007, SOW-098/099); release proof (+§12 gate, SOW-100); §4 (Workplan/Step/Gate historical grammar; +WorkGraph/WorkNode); §6 counts and rows (68 rows / 64 active; PKG-02, 04, 06, 07 [named: daemon/cmux/runtime-client], 08, 10; 100 items 74/18/8); §7 P3/P4; §8 OI-002/006/008 premises. Named by SCA-005 §B5 / SCA-006 §B5: note, L17/L23/L46/L62, API row, release proof, §4, PKG-07, §8; the rest found by the owning-workflow review.
- **DEL-00-03 SOW (15):** reading 4(a) rebind of `decomposition_basis` to `189f205ff` (revision 1.6) with its consequences (CLM-005 counts, AX-003, basis note — whose first sentence was also stale since SCA-004 and is disclosed as such — and REQ-001 "as brought current to"); PRD v2.4 as requirement source (OUT-002, REQ-002, REQ-003, AC-003, production sequence); CLM-004 and CLM-006 (named: the "46" premise; register quotations kept verbatim, premise corrected in own voice); CLM-009 re-quoted from revision 1.6 §4 ("consumed by the hooks CLI bridge, the only remaining bridge"); AX-009 provenance.
- **ADRs (6):** note; Decision 2 "daemon" → "application-owned Runtime service"; Consequences "daemon/hook/cmux bridges" → "the hooks CLI bridge"; ADR-002 context "Root-runtime" → "runtime-ownership"; posture 3 → `D-GOV-43` A2 / K-RUNTIME-1 (per-App Runtime service owns the `codex app-server` child with sessions, delegation, tools, turn locks, interruption; credentials custodied by Codex; local-model residency retired); posture 4 (client seam deferred behind T-RT; SOW-087 OUT). The hexagonal decision and AC-007's confirmations stay true.
- **Add-on P (3):** CLM-005 and REQ-004 ("Root owns generic runtime semantics" → the application-owned Runtime service's enumerated scope, `D-GOV-43` A2, K-RUNTIME-1); AX-008 provenance (scoped observation sentence; SCA-004-era currency wording and authoring-time lifecycle wording left and reported).
- **Other findings (11, not premises, not changed):** listed in the draft (e.g., DEL-00-01 SOW pre-D-PEC-72 wording; SOW-067 "Daemon owns execution"; register text still "46"/"PRD v2.2 alone"; unresolvable `3623b958b`; `projects/pec/AGENTS.md` client-seam sentence stale against PRD v2.4 §13).

## Lifecycle answer

Both targets are `CHECKING` (entered 2026-08-01 by the D-PEC-72 override); per the brief this does not stop the packet. No lifecycle change is proposed or implied; the act never writes `_STATUS.md`/`_REVIEW.md` and refuses if they differ from their pins; nothing asks the owner about CHECKING. The Root `review`-edition notice (SPEC34 reversal) is accounted for as a disclosed consequence only.

## `D-PEC-99` Part B landing

| Item | Destination | Implementing IDs |
|---|---|---|
| — | none: the exhibit (`69b646f8…f45e`) names Part B items only for nodes S1, S2 and S4 | — |

## Acceptance-lapse account and proposed re-review

- DEL-00-03: the owner's 2026-08-09 `ACCEPT_EXACT_BYTES` of SOW `3e4f0efc…` and SPEC `cc9f4754…` lapses on the record's own terms ("Any SOW or SPEC byte change invalidates this acceptance and requires a new checklist derivation and REVIEW rerun"); AC-011 becomes unsatisfied for the new bytes.
- DEL-00-01: the owner's AC-007 ACCEPT of ADR `f63ecc27…` (2026-08-01, "these artifact bytes only") lapses (hash-bound); with P, the SELF_CHECK's SOW basis describes superseded bytes. No acceptance of the DEL-00-01 SOW was found.
- Re-review offered, not assumed: **RR1** (recommended) later REVIEW rerun with fresh checklists, then owner `ACCEPT_EXACT_BYTES` with the AC-007/AC-011 confirmations — selecting it records a graph node for a later REVIEW packet; **RR2** owner exact re-acceptance in this ruling (discloses the departure from DEL-00-03's stated requirement; words must cover AC-007/AC-011); **RR3** neither now (default without an answer).

## Downstream and anchor accounts

- **Dependencies.csv:** no ACTIVE row (in any register) cites any target (`TARGET-cited active rows: 0`); corpus quote currency 127/127 identical before and after. No dependency row goes stale.
- **Other contracts:** DEL-01-01 CLM-009 (commit-anchored hashes at `aca930622`; stays true as an observation; describes superseded bytes after the act); DEL-01-01 REQ-009 cites `DEL-00-01/REQ-006`, `/AC-005` (byte-identical); DEL-01-05 TBD-005 "accepted `ADR-PEC-V2-001`" goes stale while the ADR acceptance is lapsed (for DEL-01-05's own packet; the S1 candidate keeps that text). No contract quotes SPEC or DEL-00-03 SOW text.
- **History records** quoting changed text (not edited): D-PEC-90 proposal L65; SCA-006 plan L319; TM-PEC-014 handoff L78 and checklist JSON L75; SCA-005 inventory rows; 2026-09-05 concordance CSVs; DEL-00-03 `_REVIEW.md` (old AC-003 text). Heuristic scan: 75 STALE lines (69 in these records, 6 scanner artefacts), 2,198 live / 30 history hash anchors (history records).

## Check results (all on exports; interpreter CPython 3.13.7)

- `run_d1p_checks.sh` at `6c6cc1b00`: **OVERALL PASS** — act check-only/apply/rerun-refuses in modes A and AP; containment exactly 3 / 4 files; validate `PASS format=SOW_V1`, checklists byte-identical on rerun, boundary clean; quotes **74/74**; state claims **124/124**; strict registers (0 errors, 26 `XRG-013` warnings, exit 1), harness and receipts identical before/after in both modes; quote currency 127/127; whitespace clean; fault injection **24/24**.
- Negative controls **6/6**. Reliance preflight `exact-correction-preparation` ALLOW ×10 (register `f877d931…`, script `b1712e4b…`).
- Rechecked at `origin/main` `78e74f590` and `f0a6159c9` (D-PEC-102 ruled, then its act landed): all 18 pinned files and 4 preimages unchanged.

## Verdicts (fresh read-only `pec-reviewer`, opus; files in the prep folder with dispositions)

- `VERIFIER_VERDICT_01.md` (DEL-00-03 `MODE=VERIFY`): FAIL — 1 blocking (false ground in question 4(a)); repaired.
- `VERIFIER_VERDICT_02.md` (DEL-00-01 `MODE=VERIFY`): FAIL — 2 blocking (INV-130 misstated; add-on P hunks fixing SCA-004-era staleness); repaired (hunks dropped, citation corrected).
- `VERIFIER_VERDICT_03.md` (packet review): FAIL — 2 blocking (same two themes); repaired.
- `VERIFIER_VERDICT_04.md` (re-verification): **PASS WITH NOTES**; notes applied (AX-008 scoped; candidate re-rendered).
- `VERIFIER_VERDICT_05.md` (final delta): **PASS WITH NOTES**; notes applied as draft text only. Nothing blocking remains.

## Owner questions (in the draft)

1. A, amend or defer (recommend A). 2. Add-on P (recommend include; it goes beyond the brief's touch limit). 3. Re-review RR1/RR2/RR3 (recommend RR1; default RR3). 4. Readings (a) DEL-00-03 rebind to revision 1.6 / PRD v2.4 and (b) ADR keeps "optional client", behaviors 2/4/7, the Sources line, and DEL-00-01's birth basis (recommend confirm). 5. Add-on M, two `MEMORY.md` at closeout (recommend). 6. Model steer.

## For the caller to resolve

1. **Add-on P is outside the brief's touch set.** The brief limits the packet to the named artifacts and, if needed, DEL-00-03's SOW. The DEL-00-01 SOW carries the same SCA-005 premise (REQ-004/CLM-005 "Root owns generic runtime semantics"), has no packet home (S1 excludes CHECKING DEL-00-01), and without it ruling A leaves the amended ADR contradicting its contract. It is prepared as a separately selectable add-on; decide whether to present it.
2. **Reading 4(a)** (rebinding the DEL-00-03 contract to revision 1.6) goes beyond SCA-006 §B4's "CLM-004/CLM-006, premise only" scope; it is needed so the amended SPEC can cite revision-1.6 and PRD v2.4 identifiers under AC-002/AC-003/AC-005. Disclosed to the owner.
3. **Brief citation:** commit `8f02609b5` is the DEL-01-06 RF-002 acceptance, not part of the SPEC re-acceptance (the draft says so; SCA-005 plan L964 has the same citation).
4. **Number:** `D-PEC-105` is provisional; no register row reserves it (checked at `origin/main` `f0a6159c9`: no row for D-PEC-104 or D-PEC-105).
5. **Graph/receipt items for HELP_HUMAN:** the DEL-01-05 TBD-005 consequence; `projects/pec/AGENTS.md` client-seam sentence (instruction surface; Other findings 9); the SOW-067 register note; the DEL-00-01 SOW pre-D-PEC-72 wording (a later packet).
6. **Boundary events by children (disclosed):** the DEL-00-01 drafter wrote one file outside its `mktemp` directory before exporting `TMPDIR` — a 49,640-byte copy of PRD v2.4 at `/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/prd.md` — and created and removed an empty `d1pd_scratch_dummy` directory in the shared scratchpad; the file was left (its brief permits deletion only inside its own `mktemp` directories; I did not delete it, as it is outside my write boundary). Reviewer 03 ran one `git fetch` (remote-tracking refs only). No other boundary event; no checkout was modified.
7. CI on PR #997 was still pending at return; required checks and independent PR review are HELP_HUMAN's.
