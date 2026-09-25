# Return F17 — independent review of the D-PEC-93 proposal publication (PR #913)

Reviewer: fresh read-only TASK (`pec-reviewer`, `model: opus`; host-reported `claude-opus-5-5`), dispatched by HELP_HUMAN. HELP_HUMAN transcription, condensed.

## Review of head `171e545a0a16b4c08ab03a8c6e613b5be65e314f` (base `6dac281c679e779e9e8507add693554f102242d2`)

**Verdict: PASS, no blocking findings.** Reproduced option A on a `git archive` export at act date 2026-09-25: exactly the 31 proposal paths with every postimage matching the table; stdout identical to `evidence/genA.tsv`; strict registers 0 errors / 0 warnings (66 registers, 263 rows); `analyze_dep_closure.py` 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs, isolated DEL-00-03, DEL-01-05 and the four retired deliverables, outputs identical to the evidence; schema VALID for all 8 registers; fileset check PASS; second run fails closed with the tree unchanged; `protoA_vs_base.diff` blob hashes match. Accuracy: all preimages match base; the folder-name rule reproduces all 64 existing folders; the retirement representation, the `[E-P25]` replacement, the new rows and the mirrors follow the plan (eight rows spot-checked); the dependency-extract and `_STATUS.md` order claims are fair; finding-1 counts reproduced. Boundaries, HELP_HUMAN records and Receipt 195 correct; live-tree strict validator unchanged.

| # | Finding | Disposition |
|---|---|---|
| N1 (medium) | "Fails closed, nothing written" is overstated: folder creation and scaffolding precede the writes and the fileset check follows them | Clarified in the D-PEC-93 ruling record: the act runs in an isolated worktree, discarded on any failure |
| N2 (medium) | Cross-day reproduction needs clock manipulation because the generator enforces the local date | Clarified: same-day reproduction, or comparison with recorded postimage hashes under the slot rule; no clock manipulation |
| N3 | Receipt 195's whitespace description incomplete | Receipt wording completed |
| N4 | `SHA256SUMS` lists the draft, which is not in the preparation folder | Receipt notes that entry is the proposal filed under `_DECISIONS/` at the same hash; evidence kept verbatim |
| N5 | "A later dependency-extract UPDATE keeps the rows" imprecise | Clarified in the ruling record as a known property |
| N6 | Rollback by removing created files versus the plan's no-deletion rule | Clarified: post-merge rollback is a revert PR; SCA-005's non-destructive retirement rule is separate and stays in force |
| Info | F17 absent at the reviewed head; one unwrapped mirror line | This file; cosmetic |

The review covered `171e545a0` only; the ruling commit `c257e2254` and this repair commit are covered by the re-review below.

## Re-review of `cfb5da49a64e84c2d1494535950cf32f5cc3f679` (covers `c257e2254` and `cfb5da49a`)

Same reviewer. **Verdict: PASS, no blocking findings.** The ruling quotes "D-PEC-93: A." exactly; its five question resolutions follow from option A's definition and the proposal's recommendations without enlargement; the clarifications add constraints and open no paths, and are sound against `gen_d93.py` and the plan; proposal and generator bytes unchanged and the preparation folder byte-identical; register row, RUN.md G20/C5, STATUS and Receipt 195 truthful, receipt append-only and VALID; `git diff --check` clean for the delta. Notes and HELP_HUMAN dispositions: (1) the N2 fallback read literally is circular; the independent method is to take the tabled 2026-09-25 postimages, substitute the act date at the slot loci and hash — the act is scheduled for 2026-09-25, where the fallback is unused, and the act brief names that method; (2) the N6 text answers the retirement rule rather than plan §"Failure and rollback" ("No Git reset, deletion … is a rollback mechanism"), which governs SCA-005's own Lane A failures, while this packet's revert rollback is the owner-selected D-PEC-93 instrument; (3) RUN.md G20 lists README though README needed no change. This section is added append-only after that head; no other byte changes.
