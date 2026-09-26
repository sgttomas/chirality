# M1 verifier verdict 02: backcheck of the PEC development-loop adoption

> Transcribed verbatim by the M1 HELPS_HUMANS manager from the report of the
> same fresh read-only verifier (host type `pec-reviewer`, `model: opus`,
> agent id `ad2b41ddfeec8a218`), resumed for a backcheck and returned
> 2026-09-25. The verifier cannot write files; this transcription is the
> manager's. The report's one-line lead is kept as its first paragraph. The
> verifier then filed a formal hand-back that restates the same verdict
> (PASS for the manager's bytes at `2ae8b7f1a`; B1 precondition still open;
> no new blocking or non-blocking finding; the same three notes) in shorter
> form; the fuller message is the text transcribed here.

M1 verifier verdict 02 (backcheck of 2ae8b7f1acb0bbfe17df4ed126bea4b89b986137): PASS for the manager's bytes. Not yet merge-ready: the remaining part of B1 is outside the manager's write boundary and still open.

Reviewer: the same fresh, read-only TASK verifier as verdict 01. I did not author any of this change. I made no edits, staging, commits or pushes, and delegated nothing. `git status --short` was empty throughout.

- Candidate: branch `claude/pec-loop-migration`, HEAD `2ae8b7f1acb0bbfe17df4ed126bea4b89b986137`. This is PR #917, which `gh pr view 917` reports as OPEN, not a draft, base `main`, with that same head SHA.
- Commits since the base: `11be80113`, `9a20c86d0` (repairs from verdict 01), `2ae8b7f1a` (binds PR #917 into Receipt 197).
- Base: `eb56e108377c102ded295a39abcf91986da247aa`.
- I reviewed `git diff 11be80113..HEAD` in full and re-checked the whole diff from the base. There are now 9 paths; the new one is `returns/M1_VERIFIER_VERDICT_01.md`.

## Checks rerun

All commands ran from the worktree root with `PYTHONDONTWRITEBYTECODE=1`.

| # | Check | Exit | Result |
|---|---|---|---|
| 1 | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | 0 | `VALID … frozen through Receipt-166; versioned receipt contract satisfied` |
| 2 | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | 0 | 0 errors, 0 warnings |
| 3 | `git diff --check eb56e108…..HEAD` | 0 | no output |
| 4 | `python3 tools/validation/validate_instruction_entrypoints.py .` | 0 | `PASS: root instruction entrypoints are canonical` |
| 5 | `python3 tools/validation/validate_instruction_tranche_manifest.py --base eb56e108… --head HEAD --added-manifests-only` | 0 | `G4 PASS (diff mode)`; "9 changed path(s), 1 on the instruction surface" |
| 6 | `python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py` | 0 | 33 passed |
| 7 | `execution/_Scripts/pec_reliance_hold.py --operation exact-correction-preparation`, run from `projects/pec`, for `loop/LOOP_INIT.md`, `AGENTS.md`, `loop/LOOP_RECEIPTS.md` and `returns/M1_VERIFIER_VERDICT_01.md` | 0 each | `ALLOW` each; the hold register has only its header row |

Check 5 also printed the same non-blocking over-declaration INFO lines as in verdict 01.

**Append-only check on the receipts ledger.**
- The HEAD ledger is 501086 bytes.
- Its first 498288 bytes match the base blob exactly (`cmp`).
- SHA-256 of the base, and of the HEAD prefix: `1c228c9fa1fed1fd01222c6bdb7a4b3ccd903cbdfe3b879bc9229af9c8da67fc`.
- SHA-256 of the whole HEAD file: `9f766eb47fd38b2a7f9f8547bc02a54954907d8a05086e2985967e9b6b1ad7ec`.
- Receipt 197 was edited in place between `11be80113` and HEAD. That is allowed: it is new in this unmerged PR, and nothing that was on the base changed.

**Not rerun:** the harness self-check. Receipt 197's claim that it equals its recorded baseline remains unverified by me.

## How each verdict 01 finding was handled

### B1: D-PEC-88 part — repaired

- `AGENTS.md` (the new D-PEC-88 paragraph), manifest `supersession.D-PEC-88`, and the Root notice (line 15) no longer say D-PEC-88 continues.
- They now say item 6 leaves the carry-over to this migration, that D-PEC-94 records it, and that the trace rule applies "while D-PEC-88 applies". This matches `D-PEC-88_…:58-60` and D-PEC-86 I-7.
- Small wording difference (NOTE): `AGENTS.md` says D-PEC-94 "records" the disposition, while the manifest says it "must record" it. Both become true once D-PEC-94 exists.

### B1: remaining merge precondition — still open

This is not a defect in the manager's bytes; the missing records are outside its write boundary. Checked at HEAD:

- `_DECISIONS/_REGISTER.md` has no D-PEC-94 row, and there is no D-PEC-94 record file.
- `RUN.md` has no M1 node, and there is no M1 brief.
- `returns/M1_PEC_LOOP_MIGRATION.md` does not exist, although Receipt 197's Pointers and Checks cite it. Only `M1_VERIFIER_VERDICT_01.md` is present.

Before merge, the candidate needs all of the following:
1. A D-PEC-94 record and register row that name the exact changed paths, acts, verification and rollback, and record the D-PEC-88 item-6 disposition with its true basis.
2. The M1 node and brief in the run record.
3. The M1 return and this verdict 02 file.

Required review and CI must then cover the actual final head, including HELP_HUMAN's own additions, which this verdict does not cover.

### N1 — repaired

Receipt 197's Stale-Map-Delta and manifest `scope_limits` now name `init/taskmgmt-init-prompt.md`, together with `docs/STATUS.md` and `README.md`, as still describing the former loop.

### N2 — repaired

- The Root notice and manifest rationale now list four Root texts, adding `docs/PRD_ROOT.md` E-1. E-1's wording supports the notice's claim that each text "leaves other loops' … arrangements with those loops": it says "Other loops retain their accepted graph-recording basis".
- They also name the alignment manual's PEC row (`Consolidated_v2.md:60`), which is accurate.

### N3 — repaired

- PR #917 exists, and its head is the reviewed SHA.
- It is bound into Receipt 197's Pointers and Gate-Outcome.
- The verdict pointer now names `returns/M1_VERIFIER_VERDICT_*.md`.

### N4 — repaired; see the assessment of the new rule below

### N5 — repaired

The `AGENTS.md` D-PEC-80 paragraph and the manifest D-PEC-80 supersession now say that the Step 0 mechanical plan check is retired and the no-plan rule stands.

### Notes from verdict 01

| Note | Status |
|---|---|
| 1. Launcher difference | Now named in the Root notice (see minor note below) |
| 2. Closing receipt differs from App and Piping | Stated in `AGENTS.md`. Both claims are true: App and Piping's ledgers end without a closing receipt, and PEC's former procedure required a receipt at every closeout (old LOOP_INIT Step 5 and the §8 "Every closeout" row). The quoted header rule is an exact substring of ledger rule 2 |
| 3. Dropped protective clauses | Carried into the new "Selection and decisions" section (assessed below) |
| 4. Runtime wording | The D-T0-23 reading is now labelled an interpretation. The statement that D-GOV-43 does not cite D-T0-23 is accurate; grep of both D-GOV-43 files finds no match. "Daemon" became "Runtime and user-data state" |
| 5. Model attribution | The `pec-manager` definition is now named, consistent with D-PEC-86 I-8 |
| 7. `git diff --check` scope | Now scoped to base..HEAD |
| 8. Graph completion without a MEMORY grant | The rule now says the graph completes only after the grant is given and the row written, or after the owner decides to complete without it. This is consistent with LOOP_INIT Step 6, and stricter |

**Minor note on the launcher statement.** It says the only remaining difference from App and Piping is the closing phrase. Piping's launcher also wraps its `WORKING_ROOT` line, but that is a formatting difference, not a substantive one. It needs no action.

### Verdict 01 transcription

`returns/M1_VERIFIER_VERDICT_01.md` matches my verdict 01 text. I spot-checked its structure, headings, the B1 and N1–N5 text, and the closing verdict and file list. The manager's header labels the file as a transcription.

## Assessment of the new "Selection and decisions" section

I compared it with the old LOOP_INIT Step 1, Step 2, Step 3, §7 and the Step 0 bullets. It does not weaken anything.

**Carried over faithfully:**
- "Tracking row is not its ruling source", now with an instruction to read the packet and later owner records behind the row (old :36 and :193).
- "Open legacy rows do not revive retired work" (old :194).
- Material forks, source openings, scope amendments, profile changes and owner-shaped decisions go to the PEC register, and ordinary method choices within a grant are attributed to the agent (old :233-236, verbatim in substance).
- Record every gate outcome and reason, including no-ops (old :243-244). The record now goes in the graph.
- "Never record a ruling that did not occur; role assertion is not mechanical enforcement" (old :293-294, verbatim).
- The status and type semantics that decide blocking (old :211-217): ACTIVE PREREQUISITE rows block while TBD, PENDING or IN_PROGRESS; INTERFACE, HANDOVER, CONSTRAINT and ENABLES rows order work but never block; SATISFIED, WAIVED and NOT_APPLICABLE never block. A matching reliance-hold row still blocks separately. "Under the preflight below" correctly points to the later "Active Reliance Holds" section, which keeps the fail-closed rule.

**Changed, but not weakened:**
- The blocking condition changed from "the item's `Depends` line names its target" to "the work needs its target". This follows from Remaining no longer being the selection surface. It blocks at least as often as before, so it is not a relaxation. It is less mechanical, which is a NOTE only.
- The hash-recompute rule widened from "a selected Remaining item" to "a selected item or packet". That is stricter.

**Not carried over, and why that is acceptable (NOTE):**
- "Prioritize failing validation…" is gone; steering now selects the work.
- "Report a missing contract instead of inventing work from an OPEN lifecycle, a TM concern or a historical plan" is gone. Mostly covered by the steering model, the "legacy rows" sentence and LOOP_INIT Step 4.
- Old Step 3 "Preparation or a brief is never its own acceptance" is gone. Root `AGENTS.md` covers it: a brief is not an executing child, and acceptance is human.
- §7 "present a slate and stop; never manufacture work" is gone; steering-selected undertakings replace it.
- None of these touches a fence or a human gate.

## Assessment of the new "no new Remaining entry" rule

The rule says to record new open scope "in the graph and its governing records rather than as a new Remaining entry". It adds a PEC-local restriction but weakens no fence, gate or authority:

- It matches Piping's rule ("Do not add a new `Remaining` entry", Piping `AGENTS.md:80`) and App's retirement of its Remaining sections.
- Writing to `_STATUS.md` already needed a packet, so no agent had a standing ability to add entries that this rule removes.
- New open scope still has durable homes: the SOW, decision and scope-change records, LOOP_INIT Step 3 ("Preserve future requirements"), and LOOP_INIT Step 4, which routes a concern with no home to Task Management. So the risk of scope surviving only in a finished graph is covered.
- Existing items keep their gate markers, and the text now says to update them only under the packet that opens that `_STATUS.md`. That strengthens the rule.

One NOTE: D-PEC-87 offered the owner an option L-1c, "Replace the rows with new Remaining rows…". The owner chose L-1a, so no live packet conflicts with the new rule. A future owner packet could still choose to add Remaining rows. Adding "unless an owner-ruled packet directs otherwise" would make it explicit that the rule yields to the owner. That is optional, because later owner directions already prevail under Root governance.

## New findings

- **BLOCKING:** none in the manager's bytes.
- **NON-BLOCKING:** none.
- **NOTE:** the three items above — the "records" vs "must record" wording, the less mechanical blocking condition, and the optional owner-packet clause on the Remaining rule.

## Overall verdict 02

**PASS** for the manager's bytes at HEAD `2ae8b7f1acb0bbfe17df4ed126bea4b89b986137`. All verdict 01 repairs are made and truthful, and I found no new weakening or inaccuracy.

**Not merge-ready:** the remaining B1 precondition above is still open. The final merge candidate must add those records, and required review and CI must cover that actual final head.

Files, all under `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a8c7bf3fe7714f039/`:
- `projects/pec/AGENTS.md`
- `projects/pec/loop/LOOP_RECEIPTS.md`
- `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml`
- `execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md`
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/M1_VERIFIER_VERDICT_01.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-87_RULING_2026-09-24.md`
