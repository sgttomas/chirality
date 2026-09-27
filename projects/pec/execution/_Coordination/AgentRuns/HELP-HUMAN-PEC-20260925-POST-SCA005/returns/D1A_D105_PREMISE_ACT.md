# Return — D1A: D-PEC-105 act (premise-only amendment, A + P)

- **From:** WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking
  `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1 (the act), 2026-09-27.
- **Brief:** `briefs/D1A_D105_PREMISE_ACT.md`
  (`fbc69cee8a52530d8c8fbf33abf4a743d43eb83d7614974692cf3d8a097a3895`, copied unchanged).
- **Model:** `claude-opus-5-5` for the manager and the verifier (host-reported; `high`
  effort and role identity instruction-asserted).

## PR and head

- PR #1007, https://github.com/sgttomas/chirality/pull/1007, branch
  `claude/pec-d105-d1-premise-act` against `main`. **Not merged.**
- Head before this return: `7c15f26adb5e07a7c8cf7b1cca14ffecd0bfd5de`. This return is
  the only file added after it (the commit that adds it is the PR head at hand-back).
- Base: `origin/main` `0adfbc747` (merged without a rebase at `8d85a9b6e`; the act was
  cut from `c5d852c4a`, which carries the ruling and register row).
- CI on `70c4a1bca`: governance `harness`, Harness pre-merge, `pec`, Desktop E2E
  (source mode) and the three coverage selectors pass; the rest are skipped by design.

## Act report

1. **Preconditions met.** Fetched `origin/main` `c5d852c4a` contains the ruling
   (`401c2419…0bd0ef`) and the register row `D-PEC-105`
   `RULED A + P / RR1 / 4a, 4b CONFIRMED / M / EFFECTIVE ON MERGE`. The proposal hashes
   `07761005…ba89f`. The prep `SHA256SUMS` passes 102/102 with no prep file unlisted.
   `apply_d1p.py --with-addon-p --check-only` passed with all 4 preimages and all 18
   pins as tabled, including both deliverables' `_STATUS.md`, `_REVIEW.md` and
   `Review_Findings.csv`. No re-pin was needed or made.
2. **Reliance holds.** `pec_reliance_hold.py` (register `f877d931…c741cbc`, header only)
   returned `ALLOW` ×4 for `dispatch-for-production` at 17:36:57Z (before the act and
   the verifier dispatch), and `rely-for-production` ×4 at 17:38:29Z (before the act
   commit), 18:03:31Z (before the verdict 01 fan-in) and 18:19:42Z (before the verdict 02
   fan-in), each with a `date -u` line.
3. **Run root.** `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/`:
   the 28 bound files copied byte-identical (28/28 against prep `SHA256SUMS`). Write-set
   decision: the script excludes its own directory from its inventory, so the run-root
   copy was run and its output written beside it in the run root (`MANIFEST.md`).
   `TMPDIR` was in the session scratchpad throughout.
4. **A + P.** One real run of the run-root `apply_d1p.py` (`952a7512…9d4d`) with
   `--with-addon-p`, from the repository root: exit 0,
   `targets 4/4 byte-exact; write set = grant (0 created, 4 modified, 0 removed under
   projects/pec outside the run root); pinned 18/18 unchanged` (act commit `7c250e370`).
5. **Verification.** Checks 1–12 all pass on the act tree; the runner passes on exports
   of `c5d852c4a` and of `0adfbc747`; negative controls 6/6 (below).
6. **Base drift.** `origin/main` moved to `0adfbc747` (PR #1009, 312 paths, all
   `projects/chirality-app-dev/**`). Merged without a rebase; `--check-only` on a new-main
   export passes; runner, quotes and state claims rerun and pass; no pinned file or
   quoted locus changed.
7. **Add-on M:** not done, by design (node M1). No `MEMORY.md` exists.

## Written paths (SHA-256)

Product targets (under `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/`):

| Path | Preimage | Postimage |
|---|---|---|
| `DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` |
| `DEL-00-03_v2_SPEC_seed/ScopeOfWork.md` | `3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741` | `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` |
| `DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` |
| `DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md` (P) | `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` |

Run root (214 files; `SHA256SUMS` covers the other 213, all OK):

| File | SHA-256 |
|---|---|
| `MANIFEST.md` | `46103b7e5e800a559070ea62acb810a62424d7a8f6c051474c643254f79d24db` |
| `VALIDATION.md` | `91ec7ea375df93b0e827a0df1d35b68932170ed725a2e35cb81d573cdb4a418c` |
| `HANDOFF_STATE.md` | `a893885a90e1686fde5f3e0324e617ad3697e56a887ddc3566448ccbc71b8c20` |
| `VERIFIER_VERDICT_01.md` | `7cebb458ce89b226d9b2b30f71413785596f912bdb9245fd0d397085de40fb9a` |
| `VERIFIER_VERDICT_02.md` | `fac72693fa4a926dc91b6e29b6f3fe6c55cd6acbaf6db33f62f3698a9813fef5` |
| `SHA256SUMS` | `943a0dee77b182a82a9835bf2f4afd6361a080a61495a20afaf5b6cfc243fdb7` |
| `apply_d1p.py` | `952a7512fd74e1b77f2f6b948d3cf46c876448ee1dee5370759f627236399d4d` |
| `checklist_DEL-00-03_SOW.json` | `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1` |
| `checklist_DEL-00-01_SOW.json` | `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9` |

Brief copy: `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/D1A_D105_PREMISE_ACT.md`
`fbc69cee…3895`. This return: `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/D1A_D105_PREMISE_ACT.md`
(its hash is reported in the hand-back, since it cannot state its own).

## Check results (proposal checks 1–12)

| Check | Result |
|---|---|
| 1 Preconditions | ruling, register row, pins, preimages as tabled; `CHECK preflight passed`; `ALLOW` everywhere |
| 2 Ledger rendering | `RESULT PASS fails=0`; 4/4 targets equal candidates and postimages |
| 3 Validator ×2 | `PASS format=SOW_V1` (DEL-00-03, DEL-00-01) |
| 4 Checklists | DEL-00-03 `a3bc80a0…21b1`, DEL-00-01 `6e99f93c…8cf9`, equal to the prepared hashes, byte-identical on rerun |
| 5 Boundary owners | exit 0 ×2; 0 `UNRESOLVED_OWNER` / `UNDEFINED_CLAIM` / `NOT_CHECKABLE`; JSON identical to prepared |
| 6 Quotes | `RESULT PASS 74/74` |
| 7 State claims | `RESULT PASS 126/126` |
| 8 Lifecycle and review records | no `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `REV_*` or `MEMORY.md` change |
| 9 Registers and quote currency | identical before/after: strict exit 1, 0 errors, 26 `XRG-013`; 127/127; target-cited rows 0 |
| 10 Every-PR checks | harness self-check and receipts exit 0, identical before/after |
| 11 Containment | exactly the 4 targets, the brief copy and run-root files (+ this return) |
| 12 Whitespace | `git diff --check` clean; runner evidence whitespace 0 |
| Runner rerun | `OVERALL PASS` on `c5d852c4a` and `0adfbc747` exports (act modes A and AP, containment 3/4 files, fault injection 24/24) |
| Negative controls | `RESULT PASS negative controls 6/6` |

Informational: the external-quote scan at the current base lists 99 STALE lines (86 in
history records, 13 scanner artefacts); the 17 more than at preparation are all in this
packet's own published proposal, D1P return and PR #997 review 01.

## Verifier verdicts

- **`VERIFIER_VERDICT_01.md`** — fresh read-only `pec-reviewer` (agent
  `a0ca92e7a661911d8`) on candidate `c58a6b535`: **PASS WITH NOTES**, nothing blocking.
  Basis, byte identity (with its own independent renderer), `MODE=VERIFY` on both
  contracts, premise-only discipline on every hunk (22/15/6/3), readings 4(a) and 4(b),
  posture 3 and add-on P agreeing, coherence, reproduced finite verification,
  containment and the write-set decision all PASS. NB-1 (the `--no-kept` scan
  replacement undisclosed) repaired in `MANIFEST.md`; Note 1 acted on
  (`{REPO_ROOT}` rerun method); Notes 2–4 recorded.
- **`VERIFIER_VERDICT_02.md`** — the same verifier, resumed, backchecking the records at
  `70c4a1bca`: **PASS WITH NOTES**, nothing blocking. NB-1 (HANDOFF had filled the
  add-on M `{PR}`/`{D}` slots) repaired as a labelled reading; Notes 1–3 repaired; Note 4
  (return not yet written) acted on by this file. The post-verdict-02 record edits are
  confined to those dispositions and not separately re-verified.

## Containment

`git diff --name-status 0adfbc747...HEAD` at `7c15f26ad`: 4 `M` (the targets) and 215
`A` (the brief copy and 214 run-root files); with this return, 216 `A`. Nothing else:
no `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `REV_*`, `MEMORY.md`, register,
`Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md`, `_REFERENCES.md`, decomposition,
`v2/**`, PRD, `docs/**`, `README.md`, `_DECISIONS/**` or work-graph path. No write to
`/tmp` or `/var/folders` by the manager or the verifier.

## For the caller to resolve

1. **PR review and merge** of the complete candidate by a fresh reviewer; the manager
   does not merge. HELP_HUMAN adds the graph and STATUS records (under `D-PEC-88`).
2. **Base currency** if `origin/main` moves again (procedure in `HANDOFF_STATE.md`).
3. **Acceptance lapse on landing:** the DEL-00-03 SOW and SPEC `ACCEPT_EXACT_BYTES` of
   2026-08-09 and the DEL-00-01 AC-007 ADR acceptance lapse; AC-011 and AC-007 are
   unsatisfied for the new bytes; DEL-00-01's SELF_CHECK SOW basis describes superseded
   bytes. RR1's later REVIEW node is HELP_HUMAN's and grants nothing here.
4. **Add-on M at M1:** two `MEMORY.md` files per the proposal; confirm the `{D}` reading
   (act date 2026-09-27 or closeout date) and `{PR}` = #1007 when writing them.
5. **Downstream consequences and other findings** (DEL-01-01 CLM-009 hash anchors,
   DEL-01-05 TBD-005 "accepted", proposal "Other findings" 1–11): unchanged, for their
   own packets (`HANDOFF_STATE.md` items 6–7).

Nothing unresolved inside the grant. No lifecycle change, REVIEW act, acceptance, `CON`
resolution, dependency edge, registry tool, readiness, release or reliance claim.
