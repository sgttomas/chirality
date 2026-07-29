# Merge-and-Approval Matrix — 2026-07-28 closeout window (PRs #394–#408, context #389–#393)

**Artifact class:** derivative evidence. This document rules nothing. Every cell traces to
either GitHub API metadata or a path in the frozen checkout.

| Field | Value |
|---|---|
| Repository | `sgttomas/chirality` |
| Frozen basis | `main@85ea0628fa4e57dd6aae53b06139b2b8734a9612` (= PR #408 merge commit) |
| Reference checkout | `/private/tmp/chirality-program-final-verify` (verified `HEAD` == frozen basis) |
| GitHub auth | `gh` authenticated as `sgttomas`; all 20 PR queries and 20 review queries returned successfully; no rate-limit or auth failure |
| Collection date | 2026-07-28 |
| Invariant under test | K-MERGE-1, `docs/CONTRACT.md:115` — "Merge to main allowed only when **branch HEAD == approved SHA** for the relevant run." Enforcement column: "Human review; future CI check" |

## Method

Three independent checks per PR:

1. **Git structure (local, deterministic).** For every merge SHA: confirm the object exists,
   is a `commit`, is an ancestor of the frozen basis, and compare `merge^2` to `headRefOid`.
2. **GitHub semantic approval.** `gh pr view --json reviews` plus
   `gh api repos/sgttomas/chirality/pulls/<n>/reviews`.
3. **In-repo approval vehicle.** Repo-wide grep at the frozen basis for the PR number, the
   full/abbreviated merge SHA, and the full/abbreviated head SHA.

**K-MERGE-1 result semantics used here:**

- `SATISFIED` — an in-repo record names a specific approved source-branch SHA
  (`ApplicationCommit` / `RecordCommit` / `PublicationSHA` / "Correction commit" /
  "Activation application commit"), **and** `merge^2` equals it.
- `NOT_EVIDENCED` — `merge^2 == headRefOid` is true in git, but **no in-repo record names any
  approved source SHA** for the run, so there is nothing to compare the branch HEAD against.
  The invariant is unfalsifiable from the record, not disproven.
- `VIOLATED` — `merge^2` differs from an approved SHA a record does name. **Zero rows.**

## Structural facts holding for all 20 PRs

- All 20 are `MERGED` into `main`, authored by `sgttomas`, merged by `sgttomas`.
- All 20 merge commits are **true two-parent merge commits** (no squash, no rebase).
- All 20 satisfy `merge^2 == headRefOid` exactly.
- All 20 merge commits are ancestors of the frozen basis.
- All 20 have **zero GitHub reviews** (`reviews: []`, `reviewDecision` empty, reviews API
  returns `[]`). No `APPROVED` state, no reviewer, no reviewed `commit_id` — anywhere.

## The 2026-07-28 blanket direction

Quoted verbatim in **32 files** across the checkout (Root, App, PEC, Piping, `_DomainEngines`):

> "Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for
> owners rulings, which should still be recorded in the usual manner with your recommendation
> standing as what I approved."

Representative locations: `execution/_Coordination/PROGRAM_ARCH_REMEDIATION_RECORD_CURRENCY_2026-07-28.md`,
`execution/_Coordination/CHIRALITY_PROGRAM_ARCH_REMEDIATION_CLOSEOUT_2026-07-28.md`,
`execution/_Coordination/ROOT_TRACE_MAINTENANCE_EFFECTIVE_STATE_CLOSEOUT_2026-07-28.md`,
`projects/pec/execution/_ScopeChange/_LATEST.md:22-25`,
`projects/pec/execution/_Coordination/D-PEC-70_PEC_HOLD_RELEASE_2026-07-28/CANDIDATE.md:20-23`.

Every per-decision ruling in the window (D-APP-78/79/80/81, D-T0-25, D-T0-26, D-PEC-69,
D-PEC-70, D-58/59/60/61) records the agent recommendation as standing approval under this
direction. **No ruling in the window rests on an independent per-decision owner act.**

## Matrix

| PR | Title | Branch | Head SHA (`merge^2`) | Merge SHA | Actor | Merged (UTC) | GH reviews | Approval vehicle | K-MERGE-1 |
|---|---|---|---|---|---|---|---|---|---|
| 389 | apply Root trace maintenance RT-A | `codex/root-trace-maintenance-rt-a` | `fe00bf7d4a56` | `d97c6131ae16` | sgttomas | 14:07:01 | NONE | blanket direction; PROJECT_SETUP recommendation | **SATISFIED** |
| 390 | accept Piping decomposition rev 0.11 | `codex/piping-sca-008-current-effect-reconciliation` | `9b52076701c2` | `380ea2a79458` | sgttomas | 14:10:31 | NONE | D-58 ruling + SCA-008 closeout | **SATISFIED** |
| 391 | adopt PEC PRD v2.2 | `codex/pec-prd-v2-2-dpec68` | `f22cfcc767ff` | `ec3bec922e2e` | sgttomas | 14:11:18 | NONE | D-PEC-68 ruling | NOT_EVIDENCED |
| 392 | record D-T0-25 residual classification | `codex/d-t0-25-residual-classification` | `1e08b927928f` | `2c8e41682204` | sgttomas | 14:08:39 | NONE | D-T0-25 ruling | **SATISFIED** |
| 393 | adopt App terminal decomposition basis | `codex/d-app-78-terminal-basis-application` | `63777c0f4475` | `23b3b07d1122` | sgttomas | 14:12:28 | NONE | D-APP-78 ruling | **SATISFIED** |
| 394 | preserve hold through contract repair | `codex/d-app-79-h0a-repair-hold` | `c19fa656a434` | `deb01644e324` | sgttomas | 14:25:57 | NONE | D-APP-79 ruling (H0-A) | **SATISFIED** |
| 395 | record D-T0-26 PEC profile demotion | `codex/d-t0-26-pec-profile-stale-demotion` | `7948eef43fe2` | `dc89356eb4db` | sgttomas | 14:45:05 | NONE | D-T0-26 ruling | **SATISFIED** |
| 396 | SCA-003 consumer-interface concordance | `codex/pec-sca-003` | `42e291db1d12` | `11a494e9ae0c` | sgttomas | 14:42:34 | NONE | SCA-003 standing approval after D-PEC-68 | NOT_EVIDENCED |
| 397 | reconcile App contract basis | `codex/d-app-80-contract-concordance-repin` | `0410a15df4c8` | `b0b673dc3d65` | sgttomas | 14:50:55 | NONE | D-APP-80 ruling | **SATISFIED** |
| 398 | close Root trace RT-A effective state | `codex/root-trace-maintenance-effective-state-closeout` | `d1b5486232f4` | `2d6adab3a9c7` | sgttomas | 14:57:37 | NONE | **none found** | NOT_EVIDENCED |
| 399 | activate v2.2 SOW reconciliation | `codex/pec-sow-v2-2-reconciliation-activation` | `9b6918e3b321` | `404e47c16a88` | sgttomas | 14:59:44 | NONE | D-PEC-69 ruling | NOT_EVIDENCED |
| 400 | close D-T0-25 / D-T0-26 effective state | `codex/d-t0-25-d-t0-26-effective-state-closeout` | `0ee72974e7b7` | `4cd25b348196` | sgttomas | 15:02:10 | NONE | OD7-G3 `OWNER_RULING.md` under blanket direction | NOT_EVIDENCED |
| 401 | release repaired App contract holds | `codex/d-app-81-app-hold-release` | `a149fb8d6a6e` | `826351b81075` | sgttomas | 15:20:36 | NONE | D-APP-81 ruling | **SATISFIED** |
| 402 | repin PEC references to SCA-003 basis | `codex/pec-reference-pointer-parity` | `b7d0450b1f3c` | `af62343d3af9` | sgttomas | 15:24:28 | NONE | reference-parity run under blanket direction | NOT_EVIDENCED |
| 403 | close SCA-008 maintenance, activate recon | `codex/piping-sca-008-maintenance-404e47c` | `eba66bfe6ef0` | `21e8e54e1f56` | sgttomas | 15:34:56 | NONE | D-59 + D-60 rulings | **SATISFIED** |
| 404 | close SCA-008 current-effect reconciliation | `codex/piping-current-effect-reconciliation-d60` | `ee683ef9d99a` | `ecfddf92a945` | sgttomas | 15:58:25 | NONE | D-61 ruling | NOT_EVIDENCED |
| 405 | close program architecture record currency | `codex/program-architecture-remediation-terminal-closeout` | `19eedd4a9290` | `db4d3e4a2ca0` | sgttomas | 16:09:09 | NONE | record-currency closeout under blanket direction | NOT_EVIDENCED |
| 406 | reconcile PEC v2.2 ScopeOfWork corpus | `codex/pec-sow-v2-2-reconciliation` | `ea6b4b5d0662` | `592ba2a3c276` | sgttomas | 17:03:17 | NONE | D-PEC-69 R4/R5; folded into D-PEC-70 | NOT_EVIDENCED |
| 407 | release PEC reconciliation hold | `codex/pec-hold-001-release` | `80d8c65c7b41` | `058b294c49fa` | sgttomas | 17:19:51 | NONE | D-PEC-70 ruling | **SATISFIED** |
| 408 | close Chirality program arch remediation | `codex/chirality-program-architecture-remediation-terminal` | `2fe16ae12055` | `85ea0628fa4e` | sgttomas | 17:43:25 | NONE | terminal closeout, "OWNER-APPROVED — EFFECTIVE ON MERGE" | NOT_EVIDENCED |

Full citing-record paths and per-row reasoning are in `merge_approval_matrix.csv`.

## Approval-recording pattern

Two distinct patterns are visible, and they split the window cleanly.

**Pattern A — SHA-pinned (10 rows: 389, 390, 392, 393, 394, 395, 397, 401, 403, 407).**
A record names the exact source-branch commit under a role label
(`ApplicationCommit`, `RecordCommit`, `PublicationSHA`, `Correction commit`,
`Activation application commit`) alongside the merge SHA (`EffectiveCommit` /
`EffectiveSHA` / `Durable merge`). Three of these are additionally machine-checked:
`validate_hold_release.py`, `validate_effective_closeout.py`, and
`validate_current_effect.py` hardcode the approved application SHAs.
`OD6-G5_APP_HOLD_RELEASE_2026-07-28/CLOSEOUT_IDENTITY.csv` is the single strongest artifact:
it tabulates `decision, application_commit, merge_commit, pr_number, ..., PASS` for
PRs 393/394/397.

**Pattern B — merge-SHA-only (10 rows: 391, 396, 398, 399, 400, 402, 404, 405, 406, 408).**
Records cite only the merge commit ("PR #N merge `<sha>`", "Durable merge", "Basis"). The
source-branch HEAD never appears in the checkout. Approval is recorded *after* integration
and identifies the integrated result rather than the pre-merge approved object. This
inverts the K-MERGE-1 ordering: the invariant requires an approved SHA to exist *before*
merge, and these rows have no such artifact.

A structural consequence worth naming: every closeout record is delivered by a *later* PR
than the one it ratifies (PR #398 ratifies #389; PR #400 ratifies #392/#395; PR #405
ratifies #401; PR #408 ratifies #404 and #407). The ratification chain therefore always
terminates in an unratified merge.

---

# DISCREPANCIES

**D1 — Zero semantic approval exists on GitHub for any PR in the window (20/20).**
All of PRs #389–#408 have `reviews: []`, empty `reviewDecision`, and an empty
`/pulls/<n>/reviews` API response. No `APPROVED` review, no reviewer login, no reviewed
`commit_id` exists for any PR. The entire approval record is in-repo Markdown authored by the
same agent run that produced the change.

**D2 — Author and merge actor are the same account on 20/20 PRs, against a transcribed
"never self-merge" constraint.** Every PR is authored by `sgttomas` and merged by `sgttomas`.
`docs/PRD_ROOT.md:454` records constraint **D-8**: "Git closeout runs through the
change-management role with human-gated PRs; **never self-merge**," and cross-references
K-MERGE-1 as its enforcement. The 2026-07-28 blanket direction explicitly overrides this
("...with self merge of PRs..."), so the merges are *authorized*; but D-8 remains live and
unamended in the Root PRD at the frozen basis, and the same text is carried forward unchanged
into the `D-GOV-28` candidate revision
(`docs/governance_harness/_PROPOSALS/D-GOV-28_root_runtime_stewardship/PRD_ROOT_REV6_CANDIDATE.md:454`).
The override is recorded in closeout prose but not reflected in the normative document it
contradicts.

**D3 — K-MERGE-1 is NOT_EVIDENCED on 10 of 20 PRs: #391, #396, #398, #399, #400, #402,
#404, #405, #406, #408.** For each, the source-branch HEAD SHA appears nowhere in the frozen
checkout — verified by repo-wide grep on the 9-hex abbreviation with zero hits. `merge^2 ==
headRefOid` is confirmed in git for all ten, but no record names an approved SHA to compare
against, so the invariant cannot be evaluated from the governed record. In the closeout
window proper (#394–#408) this is 8 of 15 rows.

**D4 — Two PRs have no citing record at all: #398 and #408.** Neither the head SHA nor the
merge SHA of either appears anywhere in the checkout.
- **#398** (`2d6adab3a9c7`) is a substantive miss: it merged the Root RT-A effective-state
  closeout, `HANDOFF_STATE.md`, and `LOOP_RECEIPTS.md`. It ratifies PR #389 but nothing
  ratifies it, and eight later PRs merged after it without picking it up.
- **#408** (`85ea0628fa4e`) is structurally uncitable — this merge *is* the frozen basis, so
  no in-tree record can postdate it. Its closeout self-declares "OWNER-APPROVED — EFFECTIVE
  ON MERGE."

**D5 — The terminal closeout act (#408) is self-ratifying.**
`execution/_Coordination/CHIRALITY_PROGRAM_ARCH_REMEDIATION_CLOSEOUT_2026-07-28.md` states
"Agent 0 recommends the disposition above. The recommendation stands as the owner-approved
ruling under the quoted direction," and is delivered by the same commit it approves. The
whole-program disposition `COMPLETE_FOR_ARCHITECTURE_REMEDIATION` /
`PASS_WITH_BOUNDED_WARNINGS` therefore has no approval evidence independent of the tranche
asserting it. Note the repo has previously flagged this exact pattern as a defect in a
different context — `plans/reviews/PR188_multi_agent_review_2026-07-11.md:422` objects to a
record that "points at this same PR's implementation commit... so the record is effectively
self-ratifying."

**D6 — Every per-decision ruling in the window derives from the same blanket direction, so
"per-decision ruling" and "blanket direction" are not independent approval vehicles.**
D-APP-78/79/80/81, D-T0-25, D-T0-26, D-PEC-69, D-PEC-70, and D-58/59/60/61 each record the
agent's own recommendation as the approval, with register phrasing such as "Agent 0
recommendation stands as owner approval" (`projects/pec/.../_DECISIONS/_REGISTER.md:88`) and
"Owner standing completion direction applied to the Piping Agent 1 recommendation"
(`projects/chirality-piping/.../_DECISIONS/_REGISTER.md:96-97`). The named ruling IDs are
recording vehicles, not separate authorizations. There is exactly one owner act behind all 20
merges.

**D7 — `D-APP-79` register row cites no candidate artifact.**
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md:94` carries `—
(recommendation and owner direction transcribed in the ruling)` in the candidate column, where
sibling rows D-APP-78/80/81 all name an immutable candidate file with a SHA-256. The H0-A vs
H0-B hold-posture selection has no immutable pre-decision candidate.

**D8 — `D-PEC-70` effective-state closeout pins SHAs at 9-hex, not 40-hex.**
`projects/pec/execution/_Coordination/D-PEC-70_PEC_HOLD_RELEASE_2026-07-28/D-PEC-70_EFFECTIVE_STATE_CLOSEOUT.md:4-5`
records `**Application commit:** 5fdbf6572` and `**Correction commit:** 80d8c65c7` while the
merge on line 7 is full 40-hex. Both abbreviations resolve correctly at the frozen basis
(`80d8c65c7` == PR #407 `headRefOid`; `5fdbf6572` == its parent), so PR #407 is scored
SATISFIED — but the pin is abbreviation-dependent, and truncated ruling SHAs are a defect
class the repo has flagged before (`plans/reviews/PR188_multi_agent_review_2026-07-11.md:422`,
"Its Ruling SHA is truncated").

**D9 — No GitHub-vs-in-repo metadata conflict was found.** Every PR number, branch name, head
SHA, and merge SHA asserted in an in-repo record matches the GitHub API and local git exactly.
Where records make explicit ancestry claims — e.g. D-APP-81's "has `a149fb8d6a6e...` as its
second parent," or the RT-A closeout's "whose second parent is the exact application commit" —
those claims were independently reverified against local git and **all hold**. This is a clean
result and is listed here only because the task asked for conflicts to be reported either way.

**Not a discrepancy (checked, negative):** no `VIOLATED` row. No merge commit's second parent
diverges from any SHA a record approves. No squash or rebase merge. No PR merged by an account
other than the repository owner. No merge commit missing from local history.
