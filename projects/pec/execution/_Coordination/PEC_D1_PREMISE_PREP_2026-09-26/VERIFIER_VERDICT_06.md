# Verifier verdict 06 — PR #997 review-round delta

Reviewer: fresh read-only `pec-reviewer` TASK (agent `a2a0b1f8540a96bc0`), `claude-opus-5-5`, high reasoning; brief `VERIFIER_BRIEF.md` (`2f7abd50…4af`); D1P.md and COMMON.md hashes confirmed. Reviewed the delta `26c38d6ce..b1b84d890` (HELP_HUMAN's merge of `origin/main` `f0a6159c9` to the manager's repairs); no fetch, no checkout, scratch in its own `mktemp -d` and removed. Transcribed by WORKING_ITEMS from the reviewer's hand-back (findings as given; the "checked" section condensed); the manager's dispositions follow.

---

**VERDICT: PASS WITH NOTES.** Nothing blocking. All four repairs HELP_HUMAN's PR #997 review asked for are present in the delta, true and complete, and every check rerun reproduces the stored evidence. Five NON-BLOCKING findings:

1. **The return record is partly updated and partly stale.** The delta renamed R1–R3 in `returns/D1P_PREMISE_PROPOSAL.md` but left superseded values (the `4141b6428` draft hash and "final at" line, the old postimage hashes and 183 ADR lines, the old script and checklist hashes, "pre-act REVIEW variant", posture 3 "owns the `codex app-server` child", "75 STALE lines", "124/124" at `6c6cc1b00`). Repair: restore it to its historical form or add a dated supersession note with the current values.
2. **Draft L110 attributes a check to verdict 02 that verdict 02 does not contain** ("the drafter and verdict 02 confirmed no SCA-006-changed text …"; verdict 02 never mentions SCA-006, K-03 or §12, and its "cited PRD rows byte-equal v2.2 → v2.4 except STR-002" is inexact — PEC-K-03 changed and the ADR cites it at L68). The substance is true (checked independently: the ADR cites PEC-K-03 only as "not a new consumer duty", which v2.4 K-03 still supports, and states no §12 gate or operational-reliance text). "Leaves the ADRs `CURRENT`" means it leaves them untouched, which should be said. Repair: drop "and verdict 02", or cite this verdict's check.
3. **The Actors paragraph (L38) and date (L331) predate the PR #997 round.** L38 still calls verdict 05's delta "that final delta"; L331 says "local date 2026-09-26", but the final run at `f0a6159c9` could only have happened on 2026-09-27. Repair: add the review round and verdict 06; correct the date.
4. **Posture 3 wording "only the premise's own elements".** The premise listed "sessions, delegation, turn locks, credentials, interruption, and model residency"; the amended posture adds "tools" (from K-RUNTIME-1). The ledger `why` for P05 omits "tools" and its first sentence still says the service "owns the codex app-server child"; draft L107 says "only the premise's own elements are corrected". "Tools" is defensible (the old list followed "generic runtime semantics including…"). Repair: say "tools" comes from K-RUNTIME-1's enumeration of those semantics; align the ledger `why`.
5. **Check 12 and the run-root text (L271, L289) slightly overclaim.** Row 12 checks only the runner's own outputs, only for trailing whitespace and EOF blank lines, not space-before-tab or files it does not write (`MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, verdicts); `checklist_diff_*.patch` is stripped but keeps its name. Minor: the L7 framing lists OUT-002, REQ-001–003 and AC-003; the production sequence and the rebound resolution of AC-002, AC-004, VER-002, VER-004 are also beyond §B4 scope (disclosed in AX-009 and question 4(a)).

## What was checked (condensed)

- `git diff --check origin/main...b1b84d890`: exit 0, no output; stored diffs are `diff_<KEY>.diff.txt`; runner row 12 "PASS evidence whitespace: 0 file(s)".
- REVIEW-before-merge variant (L180) workable and consistent with check 8 (L267), check 11, the Limits (L304) and L32; no re-pin implied (`apply_d1p.py` pins both deliverables' `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`).
- Reading 4(a) stated as beyond premise-only scope at L7 and question 4(a) (L322); the quoted SCA-006 §B4 row is plan L307; AX-009 tempered (DEL-00-03 SOW candidate L156).
- Posture 3 no longer names the `codex app-server` child; P's CLM-005 (L81), REQ-004 (L99), AX-008 (L142) carry the same elements; new claims S25/S26 substantive (K-RUNTIME-1 `docs/CONTRACT.md` L168; DIRECTIVE L323–329).
- `render_candidates.py` PASS (DEL-00-03 SOW `0fed4ecb…`, ADR `ad6bab7e…`, P `3757632b…`, SPEC `f84c067b…f617`); ADR max width 79; line counts 207/172/182/152; `MODE=VERIFY` on a `f0a6159c9` export: validators PASS, checklists twice byte-identical `a3bc80a0…121b1` / `6e99f93c…8cf9`, boundary exit 0; quotes 74/74 (on both `f0a6159c9` and `6c6cc1b00` exports); state claims 126/126.
- Notes confirmed: D-PEC-69 R4 (`ea6b4b5d0`) wrote the DEL-00-01 SOW bytes, ratified by D-PEC-71; SCA-005 plan L828 is in §B4; RR1–RR3 everywhere ("R3" only in the graph-node text at L12); ordering sentence confirmed by blame; 82 STALE = 69 + 13 (9 inventory, 56 concordance, 1 each D-PEC-90 proposal, SCA-006 plan, TM handoff, checklist JSON; artefacts 6 S4 prep, 6 S4 act run root, 1 DEL-08-01 L214); NOTE-ONLY marks correct (INV-131, 132, 179–182, 184; INV-130, 178, 183 are MODIFY); RR2 rollback statement sound; DEP-00-02-003 and DEP-01-01-003 are the only ACTIVE rows targeting DEL-00-01/03 and take evidence from `SOFTWARE_DECOMP.md` OI-012.
- `build_apply_d1p.py --basis f0a6159c9` byte-identical (`952a7512…`); a `6c6cc1b00` rendering differs only in the comment line; all 18 pins and aid hashes match the draft; runner hash `80714ae4…`; `SHA256SUMS` exit 0; negative controls rerun 6/6 byte-identical; optional full rerun of `run_d1p_checks.sh` at `f0a6159c9` OVERALL PASS with SUMMARY.out byte-identical; reliance preflight `candidate-validation` ALLOW ×4; no CHECKING question and no invented ruling.

---

## Manager dispositions (WORKING_ITEMS)

1. **Accepted; repaired** by a dated supersession note at the head of the return listing the current values (the sections below it stay as the `4141b6428` return).
2. **Accepted; repaired** (L110 now cites this verdict's check, says what the ADR's K-03 citation is, and says the SCA-006 plan leaves `ADRs.md` untouched and `CURRENT`, §B5 / IA §7.2).
3. **Accepted; repaired** (Actors records the PR #997 review round and verdict 06; the evidence line gives local dates 2026-09-26 and 2026-09-27).
4. **Accepted; repaired** (draft P05 row and the ledger `why` say "tools" is carried from K-RUNTIME-1's enumeration and the `codex app-server` child is not added; the ledger's `why` is not rendered, so no candidate changes — `render_candidates.py` still PASS).
5. **Accepted; repaired** (L289 and check 12 state exactly what row 12 checks and that check 12 is the whole-run-root check; `checklist_diff_*.patch` named; the L7 framing adds the production sequence and the re-resolved AC-002, AC-004, VER-002, VER-004).

These dispositions change text only (the draft, one ledger `why` field, the return, this file); no candidate, claim, script, check aid or evidence file changed after verdict 06.
