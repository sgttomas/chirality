# Review 02 of PR #997, transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `0d26d83f85d711e1d3addd0bb3b40e130bca46fb`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `b2fbd4cbc280db8dc0dfe579524a22a64dfe9ba63accb442d88f5737c20d9324`.

## Report (verbatim)

**PR #997 review 02, head `0d26d83f85d711e1d3addd0bb3b40e130bca46fb`. Verdict: PASS WITH NOTES.** Nothing blocking. I made no edits and no git writes. I used my own `mktemp -d` directory under the scratchpad (`rev997b.XXXXXX`), set `TMPDIR` to it, and deleted it afterwards; nothing was written to `/tmp` or `/var/folders`. The worktree is clean.

Paths are relative to `projects/pec/execution/_Coordination/`. `DRAFT` means `PEC_D1_PREMISE_PREP_2026-09-26/DRAFT_D-PEC-105_d1_premise_amendment_proposal.md`, at head bytes.

## Reproduction
- **Harness.** `run_d1p_checks.sh` against `origin/main` `f0a6159c9`: **OVERALL PASS**, exit 0.
  - My `SUMMARY.out` is byte-identical to the committed `evidence/run_main/SUMMARY.out`.
  - The four `diff_*.diff.txt` files and both `checklist_diff_*.patch` files are byte-identical to the committed ones.
  - Script re-render at `f0a6159c9` matches. Ledger renderings match: 22 / 15 / 6 / 3 hunks.
  - Containment is exactly 3 files in mode A and 4 in mode AP.
  - Checklists: `a3bc80a0db9a…` and `6e99f93c37c7…`, each byte-identical on rerun.
  - Quotes 74/74; state claims 126/126.
  - Strict registers (0 errors, 26 warnings), harness and receipts are identical before and after. Quote currency 127/127, with 0 active rows citing a target.
  - Fault injection 24/24. New row 12 (stored evidence whitespace) finds 0 files.
- **SHA256SUMS.** `shasum -a 256 -c` passes: 102 entries, and the file list matches the folder exactly.
- **Hashes.** All match your list:
  - draft `4104a6df…53fd`, `apply_d1p.py` `952a7512…9d4d`, `run_d1p_checks.sh` `80714ae4…ed8e`;
  - DEL-00-03 SOW `0fed4ecb…e843`, ADRs `ad6bab7e…c49e`, P `3757632b…a647`, SPEC unchanged `f84c067b…f617`.
  - The four `TARGETS` postimages in `apply_d1p.py` match the candidates, and the grant table (L191–194, line counts 207/172/182/152) matches.
- **Whitespace and containment.** `git diff --check origin/main...0d26d83f8` exits 0. 106 files change, all in the prep folder plus the brief, the manager's return and `returns/REVIEW_PR997_01.md`. The files added since `26c38d6ce` are all in the prep folder, the return, or the transcription.
- **CI on `0d26d83f8`.** `pec`, `harness`, Harness pre-merge, Desktop E2E (source mode) and the Select App, PEC and source coverage jobs pass; the rest are skipping. GitHub reports `MERGEABLE`/`CLEAN`, review decision empty.

## Review-01 findings: repair status
- **NB-1 (whitespace): repaired.** Stored target diffs are now `diff_<KEY>.diff.txt`, and both they and the checklist diffs have trailing whitespace and trailing blank lines stripped (`run_d1p_checks.sh`, section 10 and the checklist-diff step). New runner row 12 fails on trailing whitespace or a blank line at EOF in any output it writes. Check 12 (DRAFT L271) and the run-root text (L289) say exactly what row 12 covers and that check 12 covers the whole run root.
- **NB-2 (variant): repaired, and it works.** DEFT L180 describes it: the act runs once on its branch as granted, checks 1–12 run on the act commit, and REVIEW and acceptance commits follow on the same branch under a separate authorization; the branch merges only after acceptance. That order never touches the pinned `_REVIEW.md` or `Review_Findings.csv` before or during the script run, so no re-pin is needed. It is consistent with check 8 (L267, scoped to the act commit), the Limits (L304, the REVIEW files are written only under the separate authorization) and L32. It also says plainly that a REVIEW before the act would need a re-rendered script, which is not granted.
- **NB-3 (reading 4(a)): repaired.** L7 and question 4(a) (L322) now state that the rebind goes beyond SCA-006 §B4's premise-only scope, citing the §B4 row, which is plan L307. AX-009 in the DEL-00-03 SOW candidate is tempered: "keeps its subject", with the beyond-scope change named and put to the owner.
- **NB-4 (posture 3): repaired, and it stays premise-only.**
  - Posture 3 (ADR candidate L155–163) now corrects only the elements the preimage premise listed (sessions, delegation, turn locks, credentials, interruption, model residency). The `codex app-server` child is gone.
  - "Tools" is added from K-RUNTIME-1's enumeration and disclosed as such in the DRAFT P05 row (L107) and in the ledger `why`.
  - P's CLM-005, REQ-004 and AX-008 now carry the same elements. New state claims S25 and S26 anchor them to `docs/CONTRACT.md` K-RUNTIME-1 and `docs/DIRECTIVE.md` L323–329, which I checked.
  - D-PEC-71's ratification of D-PEC-69 (L36) is confirmed in `_REGISTER.md`.

## Review-01 notes: repair status
- **Note 1: repaired.** L36 cites the D-PEC-69 R4 repair (`ea6b4b5d0`), ratified by D-PEC-71.
- **Note 2: repaired.** L173 cites SCA-005 plan L828.
- **Note 4: repaired.** The options are RR1–RR3 throughout the draft and the return. The only remaining bare "R3" is the work-graph node at DRAFT L12, and "R4" at L36 is the qualified D-PEC-69 phase.
- **Note 5: repaired.** L131 now dates L92–93 to `01199c851` and L94 to `ea6b4b5d0`, matching blame.
- **Note 7: repaired.** L162 names DEP-00-02-003 and DEP-01-01-003.
- **Note 8: repaired.** L110 says SCA-006 made no ADR premise false; NOTE-ONLY marks are added. I confirmed the ADR's only PEC-K-03 citation is at candidate L68, "not a new consumer duty".
- **Note 9: repaired.** The rollback text (L298) now covers RR2.
- **Note 6: partly repaired.** The scan counts are refreshed (82 = 69 + 13, broken down correctly). See NB-a below for the hash-anchor list.
- **Notes 3 and 10** needed no repair.

## Post-verdict-06 edits (`b1b84d890..92c0fe864`)
Text only, as the dispositions say: the draft (L7, L38, L107, L110, L271, L289, L331), one ledger `why` field (DEL-00-01 ADR, P05; not rendered, and the harness still passes), the return's supersession note, verdict 06 and `SHA256SUMS`. No candidate, claim, script, check aid or evidence file changed. Each edit is accurate:
- L110 matches SCA-006 plan L319 and IA §7.2.
- L331's dates are consistent with the run at `f0a6159c9`.

## Transcription (`returns/REVIEW_PR997_01.md`, file SHA-256 `7c09e9596a502cd4f0b8e7aa3f8a6e3a0f6e979c4281c0be1bd070e28de3d7fe`)
- **Hash.** The embedded report hash `5a2f6744…cfa9` recomputes exactly by the stated rule (10,030 characters, no trailing newline).
- **Verbatim.** The opening block (L9–30) diffs identical against my original report, and I compared the rest line by line against what I sent. It is verbatim, with no whitespace normalization.
- **Disposition.** Mostly truthful, with two inaccuracies (NB-b below).

## BLOCKING
None.

## NON-BLOCKING
- **NB-a. Review-01 note 6's third bullet was not repaired.** DRAFT L167 still says the hash anchors outside the concordance manifests are only "`_REVIEW.md`/`Review_Findings.csv`/run records of the two deliverables, the D-PEC-72/74/75/77/78 packets, DEL-08-02's D-PEC-74 activation record and the closed `loop/LOOP_RECEIPTS.md`". The scan also lists D-PEC-80/81, D83_D84, P1_PRODUCTION_PREP, the S2 records, the SCA plans and IA, and the TM-PEC-009/010 drafts. All of them are history, so nothing changes in substance. Neither the transcription's disposition nor the manager's supersession note records this bullet as declined.
- **NB-b. The transcription's disposition overstates in two places.**
  - L79: "All four candidates were re-rendered, re-hashed and re-verified." Only three candidates changed; the SPEC is unchanged at `f84c067b…`. DRAFT L38 says it correctly: "the three changed candidates".
  - L80: "Notes 1–9". The report has 11 notes. Note 11, a possible HELP_HUMAN cleanup of the child agent's `/var/folders/.../T/prd.md` left over from preparation, has no disposition.

## NOTES
1. **The beyond-scope lists are not uniform.** L7 lists OUT-002, REQ-001–003, AC-003, the production sequence and the re-resolved AC-002/AC-004/VER-002/VER-004. Question 4(a)'s new sentence (L322) and AX-009's beyond-scope sentence list only OUT-002, REQ-001–003 and AC-003, although both mention the other items nearby. The disclosure is fair; aligning the lists is optional. It would change the DEL-00-03 SOW candidate bytes, so I would not reopen them for this alone.
2. **P REQ-004 reads awkwardly** (candidate L99): "…for each App instance, credentials are custodied by Codex and local-model residency is retired (`D-GOV-43` A2); …" is a comma splice inside a semicolon list. The meaning is clear. Cosmetic only.
3. **P AX-008 path.** It cites `docs/DIRECTIVE.md` without the "Root" qualifier it gives `docs/CONTRACT.md`, while the same contract uses `docs/PRD.md` to mean the PEC PRD. It is unambiguous in practice, because `projects/pec/docs/` has no DIRECTIVE.md. Cosmetic.
4. **Verdict 06 reviewed `26c38d6ce..b1b84d890`.** Nothing independent covered the text-only commit `92c0fe864` before this review. I checked its edits (above), and they are accurate.
5. **Still true from review 01.** No CHECKING or lifecycle question is asked. The acceptance-lapse account and RR1/RR2/RR3 (RR3 as the default with no answer; RR2's departure disclosed) are unchanged and fair.

I did not rerun `negative_controls.sh`; the manager and verdict 06 report 6/6.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-a (the hash-anchor list at L167): repaired by HELP_HUMAN.** The list now also names:
  - the D-PEC-80 and D-PEC-81 packets;
  - the D83_D84 records;
  - the P1 production-preparation records;
  - the S2 preparation and act records;
  - the SCA plans and impact assessments;
  - the TM-PEC-009 and TM-PEC-010 drafts.

  All of these are history. The draft is now `077610057791063e2308d932cf08a7ac44cd02793fe60925c744d969fd6ba89f` (it was `4104a6df…53fd`), and `SHA256SUMS` is updated to match.
- **NB-b (the review-01 disposition overstated): repaired.** It now says three changed candidates and covers notes 10 and 11, with a dated correction line. The report text and its hash are unchanged.
- **Notes 1–3: no change.** They are cosmetic, and fixing them would reopen candidate bytes.
- **Notes 4 and 5:** recorded.

The repair head needs a fresh review before merge.
