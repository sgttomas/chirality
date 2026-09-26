# M1 verifier verdict 01: PEC development-loop adoption

> Transcribed verbatim by the M1 HELPS_HUMANS manager from the final report of
> the fresh read-only verifier (host type `pec-reviewer`, `model: opus`),
> agent id `ad2b41ddfeec8a218`, returned 2026-09-25. The verifier cannot write
> files; this transcription is the manager's.

Reviewer: fresh, read-only TASK verifier (Type 2). I did not author this change. I edited, staged and committed nothing, and delegated nothing. `git status --short` was empty before and after the review.

- Candidate: branch `claude/pec-loop-migration`, HEAD `11be801130add3bbf2da6bcd19e18fd87ff1e4d3` (one commit, "docs(pec): adopt the shared development loop").
- Base: `eb56e108377c102ded295a39abcf91986da247aa`.
- Diff: 8 paths, 548 insertions and 366 deletions.
  - A `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml`
  - A the four `NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md` files (Root, App, Piping and Runtime `execution/_Coordination/`)
  - M `projects/pec/AGENTS.md`
  - M `projects/pec/loop/LOOP_INIT.md`
  - M `projects/pec/loop/LOOP_RECEIPTS.md`

I read Root `AGENTS.md`, `agents/AGENT_TASK.md` and the candidate `projects/pec/AGENTS.md` first.

## Checks I reran

All run from the worktree root with `PYTHONDONTWRITEBYTECODE=1`.

| # | Command | Exit | Key output |
|---|---|---|---|
| 1 | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | 0 | `VALID … frozen through Receipt-166; versioned receipt contract satisfied` |
| 2 | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | 0 | 0 errors, 0 warnings |
| 3 | `git diff --check eb56e108…..HEAD` | 0 | no output |
| 4 | `python3 tools/validation/validate_instruction_entrypoints.py .` | 0 | `PASS: root instruction entrypoints are canonical` |
| 5 | `python3 tools/validation/validate_instruction_tranche_manifest.py --base eb56e108… --head HEAD --added-manifests-only` | 0 | see note below |
| 6 | `python3 tools/validation/validate_instruction_tranche_manifest.py` (full mode) | 0 | `G4 PASS (CI mode)` |
| 7 | `python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py` | 0 | `33 passed` |
| 8 | `execution/_Scripts/pec_reliance_hold.py --operation exact-correction-preparation` for `loop/LOOP_INIT.md`, `AGENTS.md` and `loop/LOOP_RECEIPTS.md`, run from `projects/pec` | 0 each | `ALLOW` each; the hold register has only its header row |

Check 5 printed `G4 PASS (diff mode)` and `8 changed path(s), 1 on the instruction surface`. It also printed INFO lines saying seven of the manifest's declared paths do not intersect the instruction surface. The validator treats that over-declaration as non-blocking.

**Append-only proof for `LOOP_RECEIPTS.md`:**
- The base file is 498288 bytes and HEAD is 500930 bytes.
- `head -c 498288` of HEAD is byte-identical (`cmp`) to the base blob.
- SHA-256 of the base and of the HEAD prefix is `1c228c9fa1fed1fd01222c6bdb7a4b3ccd903cbdfe3b879bc9229af9c8da67fc`.
- SHA-256 of the whole HEAD file is `2632d77617efda78edc94dc8654ca02aaa8732dd223f4f52c293b0f3f23be423`.

**Not rerun by me:** the harness self-check (skipped as the brief allowed). Receipt 197's claim that it is "equal to its recorded baseline" is therefore unverified here.

## Findings

### BLOCKING

**B1. The authority records this tranche relies on are absent at HEAD.** This is a merge precondition. It is not a defect in the manager's bytes, since these records are outside its write boundary, but HEAD cannot merge as-is.

Why it blocks:
- `projects/pec/loop/**` is not a default-writable surface. `projects/pec/AGENTS.md:118-126` requires "an owner-ruled `D-PEC` packet naming the exact paths, acts, verification, and rollback". The preimage LOOP_INIT:259 also stated "the packet requirement for loop-ledger writes".
- The only authority cited for these writes is `D-PEC-94`. It is not in `_DECISIONS/_REGISTER.md` (the last row is D-PEC-93), and there is no D-PEC-94 record anywhere in the tree.
- These places cite it as though it exists: `projects/pec/AGENTS.md:186-188,221`, the manifest (lines 24, 66), `LOOP_RECEIPTS.md:2191,2196`, and all four notices at lines 17-18 (Root notice line 18).

Other missing records the candidate points to:
- `AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/RUN.md` has no M1 node, and `briefs/` has no M1 brief. The manifest's claim at lines 26-28 that "node M1 is this instruction change's authorized scope" therefore has no file-native record.
- `returns/M1_PEC_LOOP_MIGRATION.md` and `returns/M1_VERIFIER_VERDICT_*.md` do not exist. They are referenced at `LOOP_RECEIPTS.md:2192` and manifest lines 16-17. Receipt 197's Checks line (2194) defers its results to that absent return.
- The owner quotation at `LOOP_RECEIPTS.md:2191` and manifest lines 20-23 appears nowhere except in the candidate's own texts. I treat it as unverified.

The merge candidate must include (or rest on an `origin/main` that already has):
1. The D-PEC-94 record and register row. It must name every changed path (including both `loop/` files, the three off-project notices and the manifest), the acts, the verification and the rollback.
2. The M1 node and brief in the run record.
3. The M1 return and verdict files.

**B1 also covers D-PEC-88 item 6.** The candidate states as settled that D-PEC-88 continues:
- `AGENTS.md:275` ("D-PEC-88 continues under this loop")
- manifest lines 62-66 ("…decided at this migration… D-PEC-94 is its record")
- Root notice lines 15-16 ("…D-PEC-88 are unchanged")

The sources say the carry-over is still an owner decision:
- `D-PEC-88_standing_status_readme_maintenance_2026-09-24.md:58-60` says whether the grant carries into a migrated loop "is decided at that migration".
- `D-PEC-86` §3 I-7 lists the migration under "Later owner ruling".
- The quoted owner direction does not mention D-PEC-88.

D-PEC-94 must dispose of item 6 explicitly and state its true basis: the owner's decision, or a HELP_HUMAN interpretation labelled as such. Otherwise these three texts assert a continued write grant (for `README.md` and `docs/STATUS.md`) that no record supports.

### NON-BLOCKING (should fix or disclose)

**N1. A stale PEC instruction file is neither updated nor disclosed.** `projects/pec/init/taskmgmt-init-prompt.md:7-8` says: "This pointer does not adopt the App/Piping development loop or retire PEC's Remaining-based selection." That is literally still true, but after this tranche it misleads. No validator binds it (`validate_instruction_entrypoints.py` does not check it), and it is not on the manager's allowed list. Either add it to the Receipt 197 Stale-Map-Delta (`LOOP_RECEIPTS.md:2193`) and the manifest `scope_limits`, or bring it into scope under D-PEC-94.

**N2. The Root notice and manifest undercount the Root texts that name only App and Piping.**
- The Root notice (`execution/_Coordination/NOTICE_…:20-23`) and manifest lines 45-48 say "Three Root texts": SPEC §9.8, the 2026-09-22 amendment, and the graph workflow with its template.
- `docs/PRD_ROOT.md:536` (E-1) is a fourth. It says "For adopting App/Piping local development…", and the amendment record itself pairs it with SPEC §9.8 (AMENDMENT…:44).
- Root's alignment manual `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.md:60` still describes PEC's loop as `Remaining`-based.
- Name E-1 in the notice and manifest, and optionally the manual row, so Root can dispose of them.

**N3. Receipt 197 makes claims that are not yet true.** Line 2196 says "verified and opened as a PR", but `gh pr list --head claude/pec-loop-migration --state all` returns `[]`. It also has no PR pointer, whereas the adopted LOOP_INIT Step 5 (lines 128-129) binds the PR URL before final checks. Make both true in the final candidate: add the PR number to Pointers, and have the verdict files exist.

**N4. Nothing says how Remaining items are maintained after this change.**
- The preimage Step 5 (old LOOP_INIT:268-269) required updating `Remaining` when work completed.
- `AGENTS.md:240-245` keeps the sections as "deliverable-local records of open scope" and says the graph "accounts for" the items it touches. It does not say whether an undertaking that completes an item updates it (under the packet that opens that `_STATUS.md`) or leaves it.
- Unlike Piping's `AGENTS.md`, it also does not say whether new Remaining entries may be added.
- One sentence would prevent silent drift.

**N5. The mechanical workplan-retirement check was dropped without disclosure.**
- The D-PEC-80 D record (`D-PEC-80_loop_home_and_instruction_surface_2026-09-05.md:249-251`) made the committed-HEAD loader a retirement check that "must print 'no committed plan: deliverables alone'".
- The preimage ran it at old LOOP_INIT:146-148.
- Now only the prose rule survives (`AGENTS.md:291-293`). `validate_instruction_entrypoints.py:199-207` treats workplans as optional overlays and does not enforce PEC's retirement.
- The rule itself survives, so this is low risk. The manifest's D-PEC-80 supersession text (lines 51-61) and `AGENTS.md:285-298` should still say that the mechanical check is retired.

### NOTE

1. **The launcher decision was right and is disclosed.** `validate_instruction_entrypoints.py:224-232` requires `projects/pec/init/dev-loop-init-prompt.md` to byte-match Root `init/dev-loop-init-prompt.md` §4 (lines 111-128), and Root `init/**` is outside the manager's boundary. The decision is disclosed in manifest line 92 and Root notice lines 28-29. The only remaining difference from App and Piping is the phrase "within the owner's steering and live authority". The Root notice could name that phrase so Root can decide whether to align §4.

2. **The receipt freeze differs from App and Piping, and the difference is not stated.** App and Piping froze their ledgers without a closing receipt; their AGENTS say historical validation "does not require new entries". PEC appended a closing Receipt 197. That is defensible: the preimage required a receipt at every closeout, and ledger rule 2 makes the ledger the durable home for chat-only directions. It is consistent in substance, since `AGENTS.md:280-283` says the validator requires no new entries. The differing choice is not stated anywhere. The ledger header (lines 3-4, "Append-only") and rule 2 ("the one place chat-only directions become durable") cannot be edited; `AGENTS.md:267-270,280-283` supersede them in practice. Closure is prose-only, because no validator refuses a Receipt 198 (the same is true for App and Piping).

3. **Protective clauses of the preimage LOOP_INIT that were dropped without a named home.** Most are covered by Root governance or the shared method, and none weakens a fence. Consider whether any belongs in AGENTS:
   - "Recompute any hash pinned by the selected Remaining item; stop on mismatch" (old :191-192)
   - "A tracking row is not its ruling source" (old :36)
   - "Open legacy rows do not revive retired work" (old :194)
   - material forks, source openings and profile changes go to the PEC decision register (old :233-236)
   - "Record every gate outcome and reason, including no-ops" (old :243-244)
   - "Never record a ruling that did not occur; role assertion is not mechanical enforcement" (old :293-294)
   - the PREREQUISITE / SatisfactionStatus blockedness semantics (old :209-217). A Remaining item's own gate markers are kept at `AGENTS.md:244`.

4. **Shared Runtime Boundary wording.**
   - `AGENTS.md:146-147`, "D-T0-23's convergence … is read as amended", is an agent reading. D-GOV-43 does not cite D-T0-23, and D-T0-25 preserved D-T0-23 unchanged. The reading parallels App's "read as amended" (App `AGENTS.md:377-379`) and is reasonable, but should be labelled as an interpretation.
   - The supersession of D-GOV-20 items 2-4 is stated in the ruled record (`D-GOV-43_codex_host_replatform.md:73-74`), not in the A2 supplement. The sentence at `AGENTS.md:141-143` is accurate as written.
   - `AGENTS.md:159` still says "Daemon and user-data state", which is stale wording after A2.

5. **Model attribution.** "HELPS_HUMANS manager instance" (`LOOP_RECEIPTS.md:2195`; manifest line 32) cannot be checked against any committed record. Earlier receipts named the host type (`pec-manager`) under D-PEC-86 I-8; naming it here would match.

6. **"SCA-005 closed".** Manifest lines 25-26 and receipt line 2191 say D-PEC-86 I-7 deferred the migration "until SCA-005 closed". I-7 does defer it (recommendation 4, D-PEC-86:48), and SCA-005 is `CLOSED_FOR_SCOPE_CHANGE_ONLY` (`_ScopeChange/_LATEST.md`) with Lane B and A4 still open. The owner's direction to start the migration makes this moot. The record is accurate.

7. **Manifest check wording.** Manifest line 73 lists `git diff --check` without a commit range, which checks nothing on a committed candidate. It should be `git diff --check <basis>..HEAD`.

8. **Graph completion when MEMORY rows lack a grant.** LOOP_INIT Step 6 (lines 135-136) requires memory entries before the graph completes. `AGENTS.md:263-265` gives a fallback when no packet grants the `MEMORY.md` path. It does not say whether that fallback allows the graph to complete. A short clarification would help.

## Verification by category

**1. Fidelity to the shared method**
- `LOOP_INIT.md` Steps 0-6 (lines 26-147) are byte-identical to App and Piping (`diff` shows no Step differences).
- The only differences are the title, `WORKING_ROOT`, and the project pointers at lines 14-24. The pointers follow App's form, with PEC's `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md`, `Dependencies.csv`/`_DEPENDENCIES.md`, deliverable folders with MEMORY and `_STATUS.md`, decisions register and `NOTICE_*` files, `software-workflow.json`, and the TM register. All of these targets exist.
- The first, fourth and fifth paragraphs of `AGENTS.md` "Deliverable records and loop ownership" (lines 223-238, 247-257) match Piping word for word. PEC adds its own Remaining, fence, owner-direction, D-PEC-88, ledger and D-PEC-80 paragraphs.
- The development checks paragraph at `AGENTS.md:357-362` matches App and Piping on independent review and on protected checks.

**2. Fences and authority**
- The old §3 fences now live in `AGENTS.md:116-137` (the new "parked until packet" paragraph at 133-137 was carried over and tightened), with the frozen corpus at 56-73, data residency at 163-175, no second loop at 150-151, K-AUTH-1 at 40-41 and 270, and PEC-K-06 at 44-46.
- Old §8 (checks table and preflight) now lives at `AGENTS.md:339-374`; nothing is weakened, and a decomposition-registers row was added.
- Old §9 (evidence) now lives at 376-382.
- Old §10 (historical mapping) now lives at 384-397. Its section attributions are accurate.
- The Step 1 rule that owner acts are observable only on `origin/main` survives at `AGENTS.md:271-273`.
- The MEMORY-row fence treatment at 259-265 is correct.
- The D-PEC-80 D owner-intent record's cited homes ("LOOP_INIT §3/§8") resolve through the historical-references paragraph and the kill/parity row.
- No Root governance is weakened.

**3. Evergreen wording**
- `LOOP_INIT.md` has no undertaking-specific pointer or state.

**4. Receipt freeze**
- The append is pure and VALID, and it chains to Receipt-196.
- It states where handoff records now go (line 2193).
- Its truthfulness depends on B1 and N3.

**5. Manifest**
- Its paths match the diff exactly.
- It records authority (D-PEC-94 and D-PEC-86 I-7), checks, and a rollback that is accurate: removing Receipt 197 restores the Receipt-196 bytes, as verified above.
- Its supersession statements match D-PEC-80 items A-D (`D-PEC-80_…:26-41,161-175,249-251`), except as noted in N5.

**6. Notices**
- All four are marked NON-BINDING, ask for no write, and close with the no-grant clause.
- Their factual content is accurate, except for the omission in N2.
- App and Piping do use `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` and `AgentRuns/<RunID>/RECEIPT.md`.

**7. Truthfulness of cited facts**
- PRD v2.3 was adopted through checkpoint group 2: `docs/PRD.md` header and the D-PEC-92 register row.
- Revision 1.5 was accepted at checkpoint 3: `_Decomposition/_LATEST.md:3`.
- D-GOV-43 supersedes D-GOV-20 items 2-4 "on the App MVP Codex path".
- D-PEC-83 is the Remaining-carrier decision, and 57 `_STATUS.md` files carry `## Remaining`.
- D-PEC-88 item 4 is the trace clause and item 6 the migration clause.
- D-PEC-86 I-7 is the deferral.
- `_COORDINATION.md` contains no loop-procedure line made false by this change, so the manager was right to leave it unchanged.
- The D-PEC-90 text and D-PEC-80 are untouched.

**8. Containment**
- All 8 changed paths are inside the stated write boundary.
- No forbidden path is touched: `_DECISIONS/**`, RUN.md, STATUS, README, decomposition, registers, SOW, `_STATUS.md`, `MEMORY.md`, `v2/**`, `software-workflow.json`, Root `AGENTS.md`, `workflows/**`, `tools/**`.

## Overall verdict

**FAIL** for merging HEAD `11be801130add3bbf2da6bcd19e18fd87ff1e4d3` as it stands. The FAIL rests only on B1: the D-PEC-94 record and register row (including the D-PEC-88 item-6 disposition), the M1 run-record node and brief, and the M1 return and verdict files are absent.

The content review of the manager's bytes found no blocking defect. The shared-method fidelity, fence preservation, append-only receipt, manifest, notices and containment all check out.

When HELP_HUMAN adds the B1 records and N1-N5 are fixed or disclosed, the combined candidate needs a fresh backcheck at its actual HEAD. I would expect that backcheck to pass.

Files relevant to this verdict (under `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a8c7bf3fe7714f039/`):
- `projects/pec/AGENTS.md`
- `projects/pec/loop/LOOP_INIT.md`
- `projects/pec/loop/LOOP_RECEIPTS.md`
- `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml`
- `execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md` (and the App, Piping and Runtime copies)
- `projects/pec/init/taskmgmt-init-prompt.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-88_standing_status_readme_maintenance_2026-09-24.md`
- `docs/PRD_ROOT.md`
