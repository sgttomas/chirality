# Return — RV1A: REVIEW of the D-PEC-105 bytes for DEL-00-01 and DEL-00-03

- **From:** WORKING_ITEMS (Type 1), node RV1 of
  `HELP-HUMAN-PEC-20260927-RV1-INTAKE`. **To:** HELP_HUMAN.
- **Brief:** `../briefs/RV1A_D1_REVIEW.md`
  (`3212458cbeabd09d5590c5a9efc694f087f3c4b8b35c38909ef2ccd478ad5d32`).
- **Run folder:** `../../../RV1_D1_REVIEW_2026-09-27/` (`MANIFEST.md`,
  `SHA256SUMS`, briefs, checklists, evidence, verdicts).
- **PR:** https://github.com/sgttomas/chirality/pull/1023 (open; not merged by
  this manager). Head: the commit that adds this file; the manager's handback
  states the exact SHA.
- **Date:** 2026-09-27. Model: Opus 5.5 (`claude-opus-5-5`), host-reported, for
  the manager and every child.

## Verdict

The REVIEW is complete for both deliverables. Both stay `CHECKING`; no
transition was attempted and Gate 5 was not entered.

- **DEL-00-01 (`SELF_CHECK`): one MAJOR finding (RF-001), open.** There is no
  CRITICAL finding.
- **DEL-00-03 (`PEER_REVIEW`): no CRITICAL or MAJOR finding.**
- The owner's `ACCEPT_EXACT_BYTES` of the reviewed hashes has **not** been
  given. DEL-00-01 AC-007 and DEL-00-03 AC-011 stay unsatisfied until that
  owner act, which is the next step (graph node ACC). Both are READY FOR OWNER
  DECISION.
- Independent verification: one fresh read-only `pec-reviewer` gave
  verdict 01 **PASS WITH NOTES** on `d6ed711f6`, with no blocking finding.
  Its backcheck of the repairs gave verdict 02 **PASS WITH NOTES** on
  `0a0408e9c`, again with no blocking finding. The notes were repaired in
  text only; `RV1_D1_REVIEW_2026-09-27/VERIFIER_VERDICT_0{1,2}.md` records
  them with the manager's dispositions.

## Findings

All are `Origin=AGENT_CHECK`, `Status=OPEN`, `HumanDisposition=TBD`, with
proposals labelled PROPOSAL. None is proposed or recorded as `DEFER`. Every
correction is recorded only, not prepared (`D-PEC-107` §"Freeze point"). A
`ScopeOfWork.md` or artifact change needs an owner-ruled correction packet
before re-acceptance.

**DEL-00-01** (reviewer `REVIEW-SELF-DEL-00-01-20260927-RV1`; SELF_CHECK, not
independent review)

| ID | Severity | Finding | Proposal |
|---|---|---|---|
| RF-001 | MAJOR | AC-002 is partly met. ADR-PEC-V2-001's Context (L30–50) omits CLM-006's element "nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply", which appears nowhere in the ADR. The lighter functional-core element appears only outside the Context (Decision item 5, L78–82; Alternatives, L110–113). The gap has existed since `5942c5033`, the `D-PEC-105` hunks did not touch it, and the 2026-08-01 SELF_CHECK recorded AC-002 as met. The verifier judged MAJOR "defensible, but borderline"; MINOR is the stated alternative reading, and the call is the owner's | REVISE (artifact change) |
| RF-002 | MINOR | SOW authoring-time state wording ("No ADR exists", `INITIALIZED`; AX-006; CON-001 "undecided"), stale since D-PEC-72. This is proposal Other finding 1 | REVISE (SOW change) |
| RF-003 | MINOR | SOW objective warrant and basis note ("revision 1.3, the current successor"), false since SCA-004. This is Other finding 8 | REVISE (SOW change) |
| RF-004 | OBSERVATION | AX-002's present-tense "accepted basis is revision 1.3". The owner-confirmed reading 4(b) keeps it as the birth basis. This is Other finding 7 | ACCEPT_AS_IS |
| RF-005 | MINOR | REQ-005's literal path `projects/pec/docs/.archive/adr/ADR.md` is not cited in the ADR, though AC-003 and VER-002 still pass. This is Other finding 10 | REVISE (artifact change) or ACCEPT_AS_IS |

**DEL-00-03** (reviewer `REVIEW-PEER-DEL-00-03-20260927-RV1`: a fresh, agent-performed peer review, independent of the `D-PEC-105` authors)

| ID | Severity | Finding | Proposal |
|---|---|---|---|
| RF-004 | MINOR | SPEC §2 omits the PRD v2.4 §4.2 non-goal "Not a Git actor" (SOW-070). This is Other finding 6 | REVISE (SPEC change) or ACCEPT_AS_IS |
| RF-005 | MINOR | SOW L59 and AX-003 cite `3623b958b`, which does not resolve. This is Other finding 4 | REVISE (SOW change) or ACCEPT_AS_IS |
| RF-006 | OBSERVATION | Quotation case and quote-style rendering. This is Other finding 5 | ACCEPT_AS_IS |
| RF-007 | OBSERVATION | AC-002 and VER-002's "64 deliverables" is now the active count of 68 rows, and the SOW does not say so | ACCEPT_AS_IS |
| RF-008 | OBSERVATION | CLM-011 is anchored "at revision 1.4" in a contract bound to revision 1.6. It is still true | ACCEPT_AS_IS |
| RF-009 | OBSERVATION | SPEC §7's uncited "D1 decomposition" step; the token "D1" now has two senses | ACCEPT_AS_IS |
| RF-010 | OBSERVATION | SPEC §6's "complete structural index" does not reach 10 OUT items. SOW-087's deferral is described without its ID | ACCEPT_AS_IS |

The historical RF-001..RF-003 (MAJOR) stay `REVISE / RESOLVED` and describe
the prior bytes.

**CU-001 (DEL-00-03).** It is not carried forward as an active item; it is
kept as history. Its revision-1.4 totals (72 / 14 / 8) no longer describe
the bytes after the owner's rebind to revision 1.6: the SPEC and SOW now state
100 items, 74 / 18 / 8. The old method also reserves `CU-*` items to the human,
so an agent may not restate one. Assessed verbatim for information only, its
open-issue clauses hold and its totals clause fails, because of the rebind and
not a defect. A successor custom item is named as a proposal only, and only
the owner can add it.

**Proposal "Other findings" and CAND-01.**
- Other findings 1, 4, 5, 6, 7, 8 and 10 became the findings above.
- Other findings 2, 3, 9 and 11 are outside these bytes (decomposition, instruction or PRD surfaces).
- CAND-PEC-2026-09-27-01 item 8 is fully covered by the findings above.

## Consequences for HELP_HUMAN and the owner (recorded, no prompt)

1. **C-05.** `D-PEC-72` records the owner's closure of `C-05` on the exact
   accepted fan-in at `411cbe6ce`, and later P1 slices cite it. That closure
   rested on DEL-00-01 AC-007 at ADR `f63ecc27…5db5`, an acceptance that has
   now lapsed. It also rested on DEL-00-03 AC-011 at the 2026-08-01 bytes
   (SPEC `8b25a0d1…2315`, SOW `0e2cfad8…9f54`), which the 2026-08-09 currency
   repair superseded. The 2026-08-09 DEL-00-03 re-acceptance, now lapsed,
   made no C-05 act. Neither record decides whether these changes bear on
   the closure. The owner-decision text below offers an optional line.
2. **Root SPEC §3.4.** It says reversal to `IN_PROGRESS` is the only edit
   path in `CHECKING` and that a failed formal check returns through reversal.
   Its carve-out for earlier pinned criteria covers entry criteria only. The `D-PEC-105` act and any `REVISE` correction packet
   are in-place amendments under an owner-ruled packet (the 2026-08-09
   practice). This is recorded in both records as a consequence. It is not a
   question.
3. **Revised `review` edition** (not adopted). Both deliverables entered
   `CHECKING` under the D-PEC-72 override without a recorded frozen SHA. This
   is recorded once in each record for the owner's reserved decision if PEC
   ever adopts that edition.
4. **DEL-01-05 TBD-005 and DEL-01-01 CLM-009** describe the prior ADR
   acceptance and hashes until the owner re-accepts. They belong to those
   deliverables' own packets.

## Checklists

Each was derived twice with `tools/scope_of_work/derive_review_checklist.py`
(`bfb64dc9…0109`, CPython 3.13.7). Both runs gave exit 0 and byte-identical
output, and each performer re-derived it byte-identical. Both equal the
`D-PEC-105` proposal's expectation, so there is no difference to explain.

| Deliverable | Path | Criteria | SHA-256 |
|---|---|---|---|
| DEL-00-01 | `RV1_D1_REVIEW_2026-09-27/checklists/checklist_DEL-00-01.json` | 7 | `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9` |
| DEL-00-03 | `RV1_D1_REVIEW_2026-09-27/checklists/checklist_DEL-00-03.json` | 11 | `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1` |

## Method basis and substitutions

The bundled `review` workflow as of `2f825f180`, read with `git show`:

| File | SHA-256 |
|---|---|
| `WORKFLOW.md` | `f8a8f240a034395dd1d069799449215eca29ce14887a20653f1cec9a674906bc` |
| `execution.json` | `d1c668ae85f9f5a0edf2ecb312a449e21aa9101f99da9997fc4a7805677074df` |
| `resources/contract.md` | `d3d7eb27993068fbdf4ea3b06c78a19106ff4d145f149d5cf50040756144b328` |
| `resources/method.md` | `63c8a3959cd6286f95acf30ae87e42a5dd99d951b2ae2ab3ec6212a81f930daa` |

The revised edition (`77dbfcb72` onward) was not applied. Substitutions:
1. The `audit-decomp` TASK was replaced by the strict register validator plus
   a direct identity check, because Type 2 performers cannot delegate.
2. The performers drafted the review files and the manager placed them.
3. Review-type rows use review-local `SC-*` and `PEER-*` IDs.
4. Gate 5 was not entered. Snapshot finalization and the `_LATEST.md` move
   followed the 2026-08-09 precedent.
5. No CRITICAL or MAJOR finding may be deferred (SPEC §3.4).
6. Gate 1 was taken from `D-PEC-107`. No new owner confirmation of either
   checklist was given.
7. The manager's brief glossed MAJOR as "a criterion the bytes fail". That is
   disclosed as the manager's gloss, not the method text.

Instruction sources relied on:
- root `AGENTS.md` `c8ce87ef…1dffd`
- `projects/pec/AGENTS.md` `df9196d1…5eb8`
- `agents/AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`
- `D-PEC-107` `403a0497…def346`
- `D-PEC-105` ruling `401c2419…d0ef`
- `D-PEC-105` proposal `07761005…ba89f`
- root `docs/SPEC.md` `feb5e79c…109e`

## Children

All children were harness-native descendants launched with the Agent tool
(`D-GOV-35`), all on opus, each in its own scratch directory:
- `pec-task` SELF_CHECK performer (`rv1-selfcheck-0001.HqYj70`);
- `pec-task` PEER_REVIEW performer (`rv1-peer-0003.9trXkn`);
- `pec-reviewer` verifier (`rv1-verify.6yRbSx`).

**Boundary incident (disclosed).** The PEER_REVIEW performer wrote one
gitignored `__pycache__` file into the worktree, from a `--help` run made
before it had set `PYTHONDONTWRITEBYTECODE`. No tracked file changed. The
manager removed the file.

## Written paths (relative to `projects/pec/execution/`)

Every written path and its SHA-256 is listed in
`_Coordination/RV1_D1_REVIEW_2026-09-27/SHA256SUMS`, which covers this return
and excludes itself. The principal records:

| Path | SHA-256 |
|---|---|
| `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REVIEW.md` | `7b90e32f8455001e38cac56ea76bd31b32f2932d5ac77fd5fd1cfb7f4033ad32` |
| `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/Review_Findings.csv` | `a1e42d110dd4bc8f196dc3fa28ad1eafc0170eea6b9ff38e7b3001885e2f996b` |
| `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_REVIEW.md` | `22331d6e9e1e51fdccef4510348e138d542d480987ae2343357a68427f5073b3` |
| `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/Review_Findings.csv` | `7348c8ead4c9258a466349e91d61e8a0a28de2a96b0e48edbe86dc588e479483` |
| `_Evaluation/Reviews/_LATEST.md` | `d0c3f28590e0fa17f79a5940dfe9da8d2a163a335a7a66ee0063c1eb1ac4244d` |
| `_Evaluation/Reviews/REV_DEL-00-01_2026-09-27_1554/` (Brief, RUN_SUMMARY, Review_Summary, Decision_Log, QA_Report) | see `SHA256SUMS` |
| `_Evaluation/Reviews/REV_DEL-00-03_2026-09-27_1555/` (Brief, RUN_SUMMARY, Review_Summary, Decision_Log, QA_Report) | see `SHA256SUMS` |
| `_Coordination/RV1_D1_REVIEW_2026-09-27/MANIFEST.md` | `72f64eb3e22c389299d59be22d66322b90cb13a74c2029855048b194e1c9286f` |
| `_Coordination/RV1_D1_REVIEW_2026-09-27/VERIFIER_VERDICT_01.md` | `f158e19e00042dede1a415719e65fb02e0ffbbcb5710fe2fd23f2adf4826028d` |
| `_Coordination/RV1_D1_REVIEW_2026-09-27/VERIFIER_VERDICT_02.md` | `9e864e4a0c93a9d06c73c18aff64cd2fe585e054e0bde60da86e2a3629546f22` |
| `_Coordination/RV1_D1_REVIEW_2026-09-27/checklists/checklist_DEL-00-01.json` | `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9` |
| `_Coordination/RV1_D1_REVIEW_2026-09-27/checklists/checklist_DEL-00-03.json` | `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1` |
| `_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/RV1A_D1_REVIEW.md` | `3212458cbeabd09d5590c5a9efc694f087f3c4b8b35c38909ef2ccd478ad5d32` |

## Checks

Candidate output is identical to `origin/main`, whose baseline was run in a
clean detached worktree. It matched `acc7d3cc7` before the base-currency
merge `2a4140ca2`, and the final candidate matches `d39daf548`:

| Check | Exit | Output |
|---|---|---|
| strict registers | 1 | 0 errors, 26 warnings, same as `origin/main` |
| `harness.py self-check` | 0 | same as `origin/main` |
| `validate_pec_loop_receipts.py` | 0 | VALID |

`git diff --check` is clean. The outputs are in
`RV1_D1_REVIEW_2026-09-27/evidence/checks/`. The reliance-hold preflight gave
`ALLOW` for all eight target and operation pairs.

## Exact owner decision text (for HELP_HUMAN to present once this REVIEW merges)

Take the dispositions as written, or change any bracketed alternative.

Note 1: if RF-001 or any other finding is ruled `REVISE`, the correction
changes the bytes. Under the freeze point that correction packet is not
prepared. The corrected bytes would then need their own REVIEW and exact-byte
act. The owner may still accept the current bytes now, but that acceptance
would lapse when a correction lands. DEL-00-03 can be accepted independently
of DEL-00-01.

```text
D-PEC-105 RR1 / RV1 — owner decision on the reviewed bytes

RV1 finding dispositions:
- DEL-00-01 RF-001 (MAJOR, AC-002): ACCEPT_AS_IS        [alternative: REVISE — see note 1]
- DEL-00-01 RF-002, RF-003, RF-005 (MINOR): ACCEPT_AS_IS [or REVISE, each]
- DEL-00-01 RF-004 (OBSERVATION): ACCEPT_AS_IS
- DEL-00-03 RF-004, RF-005 (MINOR): ACCEPT_AS_IS         [or REVISE, each]
- DEL-00-03 RF-006, RF-007, RF-008, RF-009, RF-010 (OBSERVATION): ACCEPT_AS_IS
- DEL-00-03 CU-001: retired as history, not carried forward.
  [optional: add a successor custom item confirming the revision-1.6 totals
  (100 items, 74 IN / 18 OUT / 8 TBD; 68 deliverable rows, 64 active) and the
  preserved open-issue dispositions]

ACCEPT_EXACT_BYTES for:
DEL-00-01 ADRs: ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e
DEL-00-01 SOW: 3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647
DEL-00-03 SOW: 0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843
DEL-00-03 SPEC: f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617

DEL-00-01 AC-007 — ACCEPT.
I accept artifacts/v2/ADRs.md at SHA-256
ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e
as fit for DEL-00-01. I confirm ports-and-adapters / hexagonal
isolation as PEC v2's selected core-isolation style and confirm
that no governed act depends on PEC-held state.

DEL-00-03 AC-011 — ACCEPT.
I confirm that the published seed artifacts/v2/SPEC.md at SHA-256
f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617
(with ScopeOfWork.md at SHA-256
0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843)
is the v2 SPEC of record born from the accepted decomposition, and
that its single-objective attribution to OBJ-001 remains acceptable
given the recorded LOW-confidence qualification and the unadopted
alternatives.

[optional, only if the owner so decides: The C-05 closure recorded
under D-PEC-72 stands on these re-accepted bytes.]

This accepts these exact bytes only. It does not advance DEL-00-01
or DEL-00-03 to ISSUED, enter Gate 5, change lifecycle, authorize
P1 or production, or impose this architecture on another loop.
```

## What the caller must resolve

1. Review and merge PR #1023 under the standing Git authorization. It needs
   fresh-context independent review of the complete candidate diff, plus CI.
2. Present the owner decision above (graph node ACC), including RF-001's
   disposition and the optional C-05 line. Nothing here prompts about
   CHECKING.
3. Update the work graph and central receipt. RV1's records are complete once
   the PR merges. This manager wrote no graph, receipt, STATUS or register row.
4. Keep the snapshot nit in view: `REV_DEL-00-03_2026-09-27_1555/Review_Summary.md`
   says "Remaining gate: … only". The `_REVIEW.md` states the full next step.
   The snapshot is left immutable.
