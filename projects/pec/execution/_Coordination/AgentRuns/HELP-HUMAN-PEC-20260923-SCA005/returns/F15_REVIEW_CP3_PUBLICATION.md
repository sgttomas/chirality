# Return F15 — independent review of the checkpoint-3 publication (PR #911)

Reviewer: fresh read-only TASK (`pec-reviewer`, `model: opus`; host-reported `claude-opus-5-5`), dispatched by HELP_HUMAN. HELP_HUMAN transcription, condensed.

## Review of head `653e645a656d5858dcd2d98b1d69566675b0f52c` (base `2b0572fe049c8ffaa02d61b7dbbc3ae41bc589f6`)

**Verdict: PASS, no blocking findings.** Verified: the four live registers and `docs/PRD.md` equal the group-2 manifest candidates; live `SOFTWARE_DECOMP.md` is the pre-acceptance variant `37ea1084…a6cc`, differing from `dc2b8479…` only at lines 5 and 8, with date slots at 2026-09-25; all 26 Lane A2/A3 targets match plan preimages at the base and postimages at the head; both `_LATEST.md`, all checkpoint snapshots, SOWs, `_REFERENCES.md`, dependency files, `v2/**`, `software-workflow.json` and `projects/pec/AGENTS.md` unchanged; no DEL-02-08/09 folder; the only foreign paths are the four notice files, non-binding, with spot-checked claims confirmed; the audit reports BLOCKERS by the count rule without downgrade, the expected-consequence classification is honest, the 42-context census confirmed, COV-076 carried into rollback; the checkpoint-3 question is decidable and A6 follows the preview and plan; HELP_HUMAN's records accurate; the audit return body hashes to its declared value and its table matches the COV files; Receipt 193 VALID and append-only; decomposition `--strict` 0 errors with the two DRB-008 warnings; the `git diff --check` CRLF lines are the deterministic accumulator output, match 10 of 29 committed maps, and no CI gate runs `diff --check`.

| # | Finding | Disposition |
|---|---|---|
| N1 | PRD v2.3 vs v2.2 currency stated inconsistently (group-2 `DECISION.md` "v2.2 … remain current until … checkpoint 3 is accepted"; STATUS/README "v2.3 is the definition of record"; rollback restores v2.2) | STATUS/README now say v2.3 is adopted and live but settled by the checkpoint-3 acceptance, and a refusal would return it to v2.2; put to the owner in one sentence |
| N2 | STATUS/README not fully present-current (lifecycle census, "none applied yet", `_ScopeChange/` row, TM-PEC-023 line) | All four updated |
| N3 | F15 must exist before merge | This file |
| N4 | `RUN_SUMMARY.md` rollback reaches further than the plan's "kept as non-current evidence", and does not say whether the restore needs an owner act | Package bytes left as verified; HELP_HUMAN states to the owner that a refusal would be followed by a restore only on the owner's direction, recorded as its own act |
| N5 | The Root `LOOP_INIT` notice said App and Piping "now write" central receipts; only one exists | Notice reworded (prescribed by their `LOOP_INIT.md` §5; one existed at the survey) before publication |
| N6 | `RUN_SUMMARY.md` and `Handoff_State.md` still say the notices are to be written | Superseded by commit `653e645a6`; stated to the owner and carried into the group-3 record |
| N7 | Root `.gitattributes` CSV rule does not cover `projects/pec/`; "adjusted reading WARN" is not a contract value | Noted; labelled as a reading |

## Final-head confirmation of `259a76b39f7f6c3f7812eea36aa3f77b5eeb4246`

Same reviewer, re-reviewing the repair commit `653e645a6..259a76b39`. **Verdict: PASS.** Only the Root `LOOP_INIT` notice, README, STATUS and this file changed; no Lane A path, snapshot, COV file, pointer or accepted byte moved. N1, N2 and N5 repairs are true against the files (census recounted at the head: 28 OPEN / 26 INITIALIZED / 4 CHECKING / 2 IN_PROGRESS / 4 RETIRED; the central-receipt statement matches the tree). This transcription is fair. Nit: the owner-facing wording of N4 should match STATUS's "a refusal would return" (a refusal is itself an owner act). Receipts validator VALID; `git diff --check` flags only the known `Supersession_Map.csv` CRLF lines. This section is added append-only after that head; no other byte changes.
