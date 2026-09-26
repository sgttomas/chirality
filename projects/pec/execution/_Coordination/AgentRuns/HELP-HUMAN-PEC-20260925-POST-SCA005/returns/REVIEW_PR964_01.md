# Review 01 of PR #964 (D-PEC-100 preparation), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `fb25ce08ba26c1bde47cbb06bd72ac767d69ef72` (base `origin/main` `121900105`). Repairs: `f69ad691c`; this file is added after that.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `09a5e85bca4ea264de9fa219ab0b0add08724b0b0cc8b0d90b1c924c4617549d`.

## Report (verbatim)

**Verdict: PASS WITH NOTES.** Nothing blocks. I found two NON-BLOCKING wording issues in the draft and a few NOTEs.

**What I reviewed.**
- PR #964 head `fb25ce08ba26c1bde47cbb06bd72ac767d69ef72`. Current `origin/main` after `git fetch` is `121900105d93d9458a4680d7d4cfc37c93e6ca0c` (PR #966), which is the merge-base.
- I read `agents/AGENT_TASK.md`, root `AGENTS.md` and `projects/pec/AGENTS.md` first.
- All work ran on `git archive` exports in a `mktemp -d` under the session scratchpad. No checkout was modified: `git status --short` is empty. I deleted my exports afterwards.
- The reliance preflight (`pec_reliance_hold.py` at `121900105`, `--operation candidate-validation`) returned `ALLOW` with rc 0 for all 7 targets.

Paths below are relative to `projects/pec/execution/_Coordination/`. The prep folder is `PEC_SOW_REBUILD_S2_PREP_2026-09-26/`. Draft line numbers refer to `DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md` at the head.

## 1. Changes since verdict 04 (review target `dafce6d7e`)

- **Nothing unexpected changed.** `git diff --quiet dafce6d7e fb25ce08b` gives rc 0 for `candidates/`, `quotes/`, `claims/`, `test_apply_s2p.py`, `run_s2p_checks.sh` and the three verifiers plus the scan tool.
- **What did change:**
  - the draft;
  - `SHA256SUMS`;
  - the new `VERIFIER_VERDICT_04.md`;
  - `apply_s2p.py`, one comment line only (L62, the pin note now names `121900105`), which is why the script was rebound to `42dc9553…3d20`;
  - `evidence/run_main/{SUMMARY,containment,receipts_pre,receipts_post}.out` (basis line and export paths only);
  - the return. The last commit `541090b00..fb25ce08b` touches only the return.
- **Hashes recomputed:** draft `a6d9abe8…afe8e` and act script `42dc9553…3d20`, both as stated. Draft L178 and `SHA256SUMS` agree.
- **The four repairs are correct:**
  - **Convention (L28).** I compared every kept ID byte-for-byte between the preimages and the candidates. For the listed requirements, the only matrix-linked `AC`/`VER` that are unchanged are exactly the named exceptions: DEL-01-06 `AC-001`/`VER-001` and `AC-004`/`VER-004`, and DEL-01-01 `VER-008`. All 48 listed IDs exist before and after and did change.
  - **Added IDs (L31, L34).** DEL-02-06 `REQ-007`/`AC-007`/`VER-007` and `REQ-009`/`AC-009`/`VER-009`, and DEL-02-03 `REQ-005` and `REQ-010`/`VER-010`, all changed as described. I read the pre and post text of each.
  - **QA 21 note (L235).** It now cites verdicts 01, 02 and 04, which matches what verdict 04 says it checked.
  - **Preflight (L186).** The new run-root clause matches the guard in `apply_s2p.py` (L163–170). See N1 for one literal gap.
- **Refreshed basis.** Every "at `121900105`" claim I checked holds: the 23 pins, the basis table at L343–350, the tools, the work graph `5cee83f9…`, and the absence of a D-PEC-100 register row.

## 2. Check runner reproduced on current `origin/main`

I ran `run_s2p_checks.sh <repo> 121900105… <head PREP> <out>` with Python 3.13.7. **OVERALL PASS, rc 0**:
- act: check-only 0, apply 0, second run refuses 1;
- containment: 7 files differ, all `ScopeOfWork.md`;
- `PASS format=SOW_V1` ×7; checklists rerun byte-identical; boundary check with no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`;
- quotes 460/460, state claims 1280/1280, sibling IDs 92/92;
- strict registers, harness and receipts identical before and after. Strict exits 1 with 0 errors and 28 warnings (26 `XRG-013`, 2 `DRB-008`);
- whitespace clean; fault injection 9/9.

Every raw output matches the committed `evidence/run_main/*` byte for byte, once the export path is normalized (52 of 52 files).

Also checked:
- `shasum -a 256 -c SHA256SUMS`: 87 of 87 OK. The listed paths equal the tracked files minus `SHA256SUMS`.
- **Extra layout probe.** Script placed in a run root `…/_Coordination/SOW_REBUILD_S2_2026-09-27/`: check-only rc 0, apply writes 7/7 with write set equal to the grant, rerun refuses. Script placed in `…/_Coordination/` itself: refused by the guard.

## 3. MODE=VERIFY spot checks

- **DEL-02-07 (Part B).** The exhibit hashes `69b646f8…f45e` at `121900105`. For all four items, `DEL-02-07-REM-001..004`, the "Carry-forward" line and the "Gate" line appear verbatim in the candidate's blockquotes (L141/143, L149/151, L157/159, L165/167). REM-002 carries both gate groups. The two exhibit phrases quoted in `CLM-016` are verbatim. The gates are stated as still binding at candidate L137 and in `AX-011` (L268). The draft's line table (L82–87) is accurate.
- **DEL-01-06.** `CLM-015` (candidate L116–124) matches `v2/config/loops.json` at `121900105` (`fd342b4f…`): schema version 2; `pec` → `projects/pec/loop/LOOP_INIT.md`; `shared-dev-loop` v1 live, `loop-receipts-ledger` v1 historical, `agentruns-json` v1 historical, with the same basis paths. The schema, port and adapter hashes match. `remaining-loop` appears only as quoted stale design text (L94, `CLM-020`, `CON-003`). `REQ-011` rejects version 1.
- **DEL-01-01 anchors.** All 7 ACTIVE `Dependencies.csv` rows whose `EvidenceFile` is an S2 contract keep their `EvidenceQuote` as a raw substring of the postimage. DEP-02-01..06-003 land in `CLM-012` (candidate L113). DEP-02-07-003 lands in DEL-01-06 `CLM-006` (L105).

## 4. The draft

- **Options (L103–110):** present.
- **Grant (L116–124):** 7 paths, preimages and postimages. I recomputed all 14 hashes against `121900105` and the candidates.
- **Method (L26–27):** exact-bytes replacement under INIT discipline, with the departure from D-PEC-98 disclosed. REVISE appears only as the one-line disclosure at L27, besides the amendment's provenance at L22 and a limit at L273. REVISE adoption is not an owner question.
- **Lifecycle:** none. All seven are `INITIALIZED` at `121900105`, and the act pins every `_STATUS.md`.
- **Verification (L206–219), rollback (L255–259), limits (L263–276):** present.
- **Owner questions (L280–283):** A; the Part B reading; add-on M with the exact 7 files and the row (DEL-01-06 `MEMORY.md` `035ecb86…` exists, the other six are absent at `121900105`, template `5a9564f4…`); models.
- Nothing prompts about CHECKING (L269 is a limit), and nothing enlarges the grant.

## 5. Downstream consequence (L97): accurately stated

- My reproduced scan gives exactly the 15 named contracts with STALE lines (`SUMMARY stale=31 kept=32`).
- The examples hold. DEL-03-01 quotes the prior DEL-01-06 `REQ-005` "version-1" sentence. DEL-04-05 L137 quotes the prior DEL-02-03 `REQ-001`. DEL-10-10 quotes DEL-02-05. DEL-02-08 `CLM-008` and DEL-02-09 `CLM-007` cite `43f1f57a13bb…`. DEL-02-01 `REQ-002` names DEL-02-07 as the feed-manifest supplier.
- All 15 are `INITIALIZED`.

## 6. Containment

- `git diff --name-status 121900105...fb25ce08b` shows only additions: the prep folder plus `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S2P_SOW_REBUILD_PROPOSAL.md`, `briefs/S2P_DRAFTER_BRIEF.md` and `returns/S2P_SOW_REBUILD_PROPOSAL.md`.
- `git diff --check 121900105...fb25ce08b` gives rc 0.

## Findings

- **NON-BLOCKING 1. Draft L352 says "one read-only reviewer".** There were four separate fresh reviewers, one per verdict. That is what draft L43 ("Fresh read-only `pec-reviewer` TASKs") and return L134 ("Four fresh read-only `pec-reviewer` TASKs") say, and the verdict headers agree. This line predates verdict 04 and was not flagged there. Repair: say "four read-only reviewers".
- **NON-BLOCKING 2. The new L186 clause is literally wider than the guard.** It says the directory must be a run root "if the script itself sits under `projects/pec/`". The code tests whether the script's directory path starts with `projects/pec/`. So a script placed directly in `projects/pec/` passes the guard, as do miscased paths and a nested subdirectory of a run root. This is the gap verdict 04 recorded for the docstring. Verdict 04's probes showed it fails closed through the write-set inventory, so it is harmless. Repair (optional): "if the script's directory lies below `projects/pec/`, it must be under a run root".
- **NOTE 3. PR #969 (open, not merged) will make some wording stale.** It records the D-PEC-101 ruling ("K4 with C; K1; V; Notes a; defaults") and adds a register row reserving D-PEC-100 as `NOT_PREPARED`. Once it merges, draft L99 ("not ruled"), the L8 register sentence and return L116 (which cites PR #962) will be out of date. Nothing substantive changes:
  - K1 and K4 touch no file this act pins. K1 modifies `Dependencies.csv` only for DEL-04-03, DEL-08-03, DEL-09-06 and DEL-10-03, and adds no row citing an S2 contract.
  - PR #969 leaves the work graph's S2 row unchanged.
  - The strict-register before/after identity check absorbs the change in baseline.

  Refresh this text at the next re-render or at publication.
- **NOTE 4. Draft L99 lists K1's `_DEPENDENCIES.md` changes as those of DEL-02-03..06.** K1 also modifies them for DEL-02-01, DEL-02-02, DEL-02-08, DEL-02-09 and others. The statement is true as far as it goes, and none of these files is pinned.
- **NOTE 5. The brief (L19) allowed only a copy of that brief under `briefs/`.** `S2P_DRAFTER_BRIEF.md` is also committed there. You said this is acceptable, and the draft cites it (L42) as the drafters' rules.
- **NOTE 6. The four post-verdict-04 wording repairs have now been reviewed here.** They hold, apart from N2.

**Relevant paths:**
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md` (at the PR head)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/apply_s2p.py`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S2P_SOW_REBUILD_PROPOSAL.md`

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| NON-BLOCKING 1 (one vs four reviewers) | Repaired in `f69ad691c`: "four fresh read-only reviewers (one per verdict)" |
| NON-BLOCKING 2 (guard wording wider than code) | Repaired: the preflight line states the path-prefix test literally and that a placement the guard does not refuse fails closed at the write-set inventory |
| NOTE 3 (stale after PR #969) | Repaired: the status line says the register reserved D-PEC-100 in PR #969; the D-PEC-101 paragraph records the ruling and the act in progress. The manager's return keeps its hand-back wording with a HELP_HUMAN note naming the new draft hash |
| NOTE 4 (K1's `_DEPENDENCIES.md` changes) | Repaired: "mirrors (among them DEL-02-03..06)" and the four `Dependencies.csv` named |
| NOTE 5 (drafter brief committed) | No change: accepted by HELP_HUMAN; cited by the draft as the drafters' rules |
| NOTE 6 | Recorded |
