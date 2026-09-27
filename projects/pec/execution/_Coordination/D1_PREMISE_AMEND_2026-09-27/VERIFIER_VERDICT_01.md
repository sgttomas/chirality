# VERIFIER_VERDICT_01 — D-PEC-105 act (node D1), PR #1007, candidate `c58a6b535`

Verdict: **PASS WITH NOTES**

- **Verifier.** A fresh, read-only TASK (Type 2). I authored nothing in this act.
- **Candidate.** `c58a6b535af3b39eba476e143a6c2564e7286e6e` on branch `claude/pec-d105-d1-premise-act`.
- **Base.** `c5d852c4a95a478f34d9e4e4375d603e08245e25`. This is the local `origin/main` ref and the merge base. I did not fetch.
- **Worktree read in place.** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d105-act`.
- **Scratch.** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d105ver.zpaexX`, holding:
  - `git archive` exports of `c5d852c4a` and `c58a6b535`;
  - scratch-only `git init`s whose object stores borrow the repository's objects through alternates, as `run_d1p_checks.sh` does;
  - rerun outputs.

  It grew to 4.2G. I deleted it at the end and confirmed it is gone.
- **Footprint.** No repository write and no git write (no fetch, checkout, commit or stash). The worktree status is clean at HEAD `c58a6b535` before and after. Every python run used `PYTHONDONTWRITEBYTECODE=1`.

## Method files loaded (SHA-256 at the candidate)

All of these are unchanged since `6c6cc1b00`. They match the hashes the proposal records.
- `workflows/scope-of-work/WORKFLOW.md`: `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`
- `workflows/scope-of-work/resources/checks.md`: `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188`
- `workflows/scope-of-work/resources/tools.md`: `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7`
- `workflows/scope-of-work/execution.json` (hashed, not read): `4ad8b7eb42dba41f1609e6b3c61f14baa15ad82a1342f4ad12a095c4a570a26d`
- `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (§7 read): `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`
- Root `AGENTS.md`: `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/pec/AGENTS.md`: `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`

Wider consultation, recorded:
- Root `docs/CONTRACT.md` `510f6a84…3f71` (K-RUNTIME-1).
- Root `docs/DIRECTIVE.md` `b191750c…7fbf` (§7).
- The act brief copy.
- `apply_d1p.py` and the check aids.

Reliance-hold preflight for this verification entry path:
- Run on the candidate export, operation `candidate-validation`.
- Register `f877d931…741cbc` (header only); script `b1712e4b…d0e`.
- ALLOW ×4 (exit 0) at 2026-09-27T17:59:01Z.

## Results

### 1. Basis — PASS
- **Ruling and proposal hashes.** At both the base and the candidate:
  - the ruling hashes `401c2419…0bd0ef`;
  - the proposal hashes `07761005…ba89f`.
- **Register row.** `_REGISTER.md` L122 at `c5d852c4a` reads `RULED A + P / RR1 / 4a, 4b CONFIRMED / M / EFFECTIVE ON MERGE`.
- **Bound script.** The run-root `apply_d1p.py` hashes `952a7512…9d4d`, equal to the prep copy.
- **Run-root copies.** All 28 copied files are byte-equal to their prep counterparts. The only run-root files with no prep counterpart are the four check outputs (`checklist_*.json`, `boundary_*.json`) and `evidence/**`.
- **Prep `SHA256SUMS`.** 102/102 entries OK, and no prep file is unlisted.
- **Pins.** All 18 pins hash as tabled at `c5d852c4a`, at `c58a6b535` and at `6c6cc1b00`.

### 2. Byte identity — PASS

| Target | Preimage at `c5d852c4a` | Postimage at the candidate | Lines |
|---|---|---|---|
| DEL-00-03 SPEC | `cc9f4754…1bae` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` | 207 |
| DEL-00-03 SOW | `3e4f0efc…5741` | `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` | 172 |
| DEL-00-01 ADRs | `f63ecc27…5db5` | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` | 182 |
| DEL-00-01 SOW | `43346150…1740` | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` | 152 |

- Each postimage equals the proposal's tabled value, the run-root candidate and the live worktree bytes. Each preimage equals the tabled preimage.
- `render_candidates.py` gives `RESULT PASS fails=0` at each observation: `6c6cc1b00`, `c5d852c4a` and `189f205ff`.
- An independent renderer of my own gives the same result. It applies each ledger's hunks, requiring each `pre` to occur exactly once, to the `c5d852c4a` preimage. All four renderings equal the files at `c58a6b535`. Hunk counts are 22, 15, 6 and 3.

### 3. `MODE=VERIFY` on both contracts — PASS

Tools rerun on the candidate export:
- **Validator.** `PASS format=SOW_V1` for both, exit 0.
- **Checklist.** Derived twice, exit 0, byte-identical:
  - DEL-00-03 `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1`;
  - DEL-00-01 `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9`.

  Both equal the run-root `checklist_*.json`. Against the base (`1c4d4927…` and `bb815439…`), the only changes are:
  - DEL-00-03: AC-003's text (v2.2 → v2.4), line numbers and the source hash;
  - DEL-00-01: the source hash only.
- **Boundary owners.** `check_boundary_owner_resolution.py` exits 0 for both. It reports 0 `UNRESOLVED_OWNER`, 0 `UNDEFINED_CLAIM` and 0 `NOT_CHECKABLE`, with 0 requirements in its grammar.

Items:
- **1.** SOW_V1 is canonical under Standard §7, and the format resolves as SOW_V1. No pilot variance is required.
- **3.** Both `_STATUS.md` files hash as pinned (`CHECKING`).
- **4.** Validates.
- **8.** Every `OUT-*` row maps to `SOW-089 OBJ-001` or `SOW-088 OBJ-005`.
- **9 and 13.** The checklist carries every `AC-*` exactly once, in source order (11 and 7), each with its exact text, the production hash and a `VER-*` or `HUMAN_REVIEW` method.
- **16.** The findings below are separated into schema, content and substrate.
- **18.** Reruns are byte-identical. A damaged copy fails validation and derivation (exit 1) and writes no output file.
- **19.** The only locally defined ID added is AX-009 or AX-008, and no new bare foreign ID-shaped token appears.
- **20.** Matrix rows are unchanged, one AC per row.
- **21.** Checked by hand as well: the changed REQ-004 names the same owner as the CLM-005 it cites.

### 4. Premise-only discipline — PASS
- **Every hunk carries a cause.** Each has a cause and reason in its ledger, and the verifiers pass: quotes 74/74 and state claims 126/126.
- **Source spot-checks.**
  - PRD v2.4 has 49 `PEC-*-NNN` rows (ORI 7, RCN 6, GAT 4, PRS 7, STR 5, API 7, DSH 7, SVC 6).
  - The ScopeLedger has 100 items (74/18/8). `Deliverables.csv` has 68 rows, with the four retired rows in SOFTWARE_DECOMP §5 and §7.
  - SOW-029, SOW-035, SOW-037 and SOW-087 are OUT.
  - SOW-095 to SOW-100 exist and are homed as stated.
  - The OI-002, OI-006 and OI-008 re-expressions are in SOFTWARE_DECOMP §10.
  - The PKG-00 charter at revision 1.6 matches the CLM-009 quote verbatim.
  - HierarchyEdge is still in PRD §7.2.
  - `docs/` still holds only `PRD.md` and `STATUS.md` besides `.archive`.
- **Identifier resolution.** All 217 ID tokens in the amended SPEC resolve against the registers and the PRD. Retired DELs and OUT SOWs are labelled as retired or deferred.
- **IDs.** Only AX-009 and AX-008 are added; none is retired or reused.
- **History kept.** "Born from", §10's "revision 1.3" and ADR-002's Sources line all remain.
- **Operational reliance.** "verify-before-rely" is gone. The K-03 row states operational reliance as PRD v2.4 L230 does: within the pin, coverage and trust tier, only after the §12 gate, never authority, with file fallback.
- **No lifecycle, acceptance or readiness claim.** The notes say that no acceptance is recorded.
- **Owner confirmations still hold.** The ADR-PEC-V2-001 decision and the AC-007 confirmations remain true: the ADR diff touches only the note, one actor name, the bridge list, the ADR-002 boundary label and postures 3 and 4.
- **P02 label.** The DEL-00-03 SOW P02 SCA-004-era correction is labelled as such in the ledger (`premise/DEL-00-03_SOW.json` P02 `why`) and in proposal L85 and L322. The owner confirmed it under 4(a). See Note 3.

### 5. Readings 4(a) and 4(b) — PASS
- **4(a).**
  - The frontmatter is rebound to `@189f205ff02df4111b33c20be441ce06e65ada7a`, which is revision 1.6, `current_basis`, PR #954.
  - OUT-002, REQ-002, REQ-003, AC-003 and the production sequence now read v2.4.
  - REQ-001 now reads "as brought current to".
  - AX-009 (DEL-00-03 SOW L156) states that the change goes beyond the premise-only scope of SCA-006 §B4.
- **4(b).** The ADRs keep all of the following, and the DEL-00-01 contract's frontmatter and AX-002 remain `@11a494e9a` (revision 1.3):
  - "PEC is an optional client" (L159–160);
  - `D-PEC-56` behaviors 2, 4 and 7 (L162);
  - ADR-002's Sources line, "PRD v2.2 §§4, 10, 13, and 15" (L130–131).

### 6. Posture 3 and add-on P agree; coherence — PASS
- **Same owner and elements.** ADR posture 3 (L155–163), DEL-00-01 CLM-005 (L81) and REQ-004 (L99) all name:
  - the application-owned Runtime service, per App instance;
  - sessions, delegation, tools, turn locks and interruption;
  - credentials custodied by Codex;
  - local-model residency retired;
  - `D-GOV-43` A2.

  The ADR and CLM-005 also cite K-RUNTIME-1 and the superseding of `D-GOV-20` items 2–4. These match Root CONTRACT L168 and DIRECTIVE §7.
- **No `codex app-server` child.** It appears 0 times in either file.
- **Coherence.** The amended SPEC satisfies the inspection-checkable criteria of the amended DEL-00-03 contract:
  - AC-002, AC-003 and AC-005: all tokens resolve;
  - AC-004: the note names revision 1.6 at `189f205ff`, equal to the frontmatter;
  - AC-006 and AC-007: unchanged text;
  - AC-008: the act writes no decomposition file;
  - AC-010: no vocabulary change.

### 7. Finite verification reproduced — PASS
- **Quotes.** `verify_d1p_quotes.py --tree . --gitdir <repo> --prep <run root> --observation 6c6cc1b00` gives `RESULT PASS 74/74`.
- **State claims.** `verify_d1p_state_claims.py` gives `RESULT PASS 126/126`.
- Both outputs are identical to the stored `evidence/post/*.out` apart from the header lines.
- **Before and after** (the `c5d852c4a` export against the `c58a6b535` export, git-backed), every output identical:
  - strict registers: exit 1, 0 errors, 26 warnings, all `XRG-013`;
  - `harness.py self-check`: exit 0;
  - `validate_pec_loop_receipts.py`: exit 0;
  - quote currency: 127/127, target-cited active rows 0.
- **Reliance-hold preflight order.** `reliance_dispatch.out` shows ALLOW ×4 at 17:36:57Z. That is before `8043bb1e5` (17:38:07Z) and before the act (`apply_run.out`, 17:38:17Z). `reliance_rely.out` shows ALLOW ×4 at 17:38:29Z, before the act commit `7c250e370` (17:38:30Z). Register and script hashes are recorded.
- **Stored evidence also checked.** Negative controls 6/6, fault injection 24/24, and the rerun `SUMMARY.out` ending `OVERALL PASS`.

### 8. Containment and lifecycle — PASS
- **Diff contents.** `git diff --name-status c5d852c4a...c58a6b535` has 144 entries:
  - four `M` targets;
  - `A` of the brief copy `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/D1A_D105_PREMISE_ACT.md`, whose SHA-256 is `fbc69cee8a52530d8c8fbf33abf4a743d43eb83d7614974692cf3d8a097a3895`, as required;
  - 139 run-root `A` entries.
- **Nothing forbidden.** No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `REV_*`, `MEMORY.md` or `_Evaluation/**` path appears. Neither deliverable has a `MEMORY.md`.
- **Whitespace.** `git diff --check` is clean (exit 0).
- **Commit scopes.** `7c250e370` → `c58a6b535` touches the run root only. `8043bb1e5` → `7c250e370` touches the targets and run-root evidence only.

### 9. Manager decision — PASS
- **The script design.** `apply_d1p.py` L114–128 prunes `SELF_DIR` (the resolved script directory) from its write-set inventory, and L176–179 refuses an in-tree directory without the `D1_PREMISE_AMEND_` prefix.
- **The proposal agrees.** Generation method: "except its own directory". Administrative grant: all outputs go in the run root. `test_apply_d1p.py` also asserts that evidence written in a run root does not trip the inventory.
- **The run.** `apply_run.out` records a run from the repository root of the run-root copy, with `--with-addon-p`, exit 0. It reports "write set = grant … pinned 18/18 unchanged", and the output was written in the excluded run root. This is consistent.
- **The scan replacement.** Rerun on the `c5d852c4a` export:
  - the full `scan_external_quotes.py` output hashes `38095b883af8238b8aa2b55606215166bec1b7e923958efd2cca48d9c637bf29` and has 48,144 lines, matching the stated original;
  - the `--no-kept` output (L43, L108) is byte-equal to the stored `evidence/rerun_c5d852c4a/scan_external_quotes.out` (`0710d293…4d68`, 2,343 lines), as is the full output with its `KEPT` and `HISTORY-KEPT` lines filtered out;
  - the SUMMARY reads stale=99 kept=45801.
- **The 17 extra STALE lines.** Keyed by file and span, the STALE set against the prep `run_main` scan (82 lines) adds exactly 17 lines and loses none:
  - 13 in `_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md`;
  - 3 in `returns/D1P_PREMISE_PROPOSAL.md`;
  - 1 in `returns/REVIEW_PR997_01.md`.

## Findings

**BLOCKING:** none.

**NON-BLOCKING**

1. **(execution substrate) The scan replacement is not yet disclosed in any committed file.**
   - **Where.** `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/evidence/rerun_c5d852c4a/scan_external_quotes.out` L1.
   - **What.** The file is the manager's `--no-kept` rendering, not the runner's raw output. The runner header (`run_d1p_checks.sh` L11–13) says it "Writes all outputs", yet neither `rerun_c5d852c4a_console.out` nor `SUMMARY.out` says the file was replaced. The file itself has no header saying so.
   - **Impact.** The substitution is verified above and is lossless in its counts. It still needs recording.
   - **Repair.** When `MANIFEST.md` or `VALIDATION.md` is written, record: the replacement, the original's hash `38095b88…bf29` and 48,144 lines, and the regeneration command.

**NOTE**

1. **(substrate) The rerun script is tied to this worktree.** `evidence/post/verify_rows_2_12.zsh` L5 hard-codes `W=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d105-act`. Several evidence outputs also record that absolute `--repo` path: `apply_check_only.out`, `apply_run.out`, `post/rerun_refuses.out` and `receipts_*.out`. The script does not run from another checkout without an edit. Harness GEN-1 is unchanged before and after. The rule in `projects/pec/AGENTS.md` "Path Anchors" covers prompts and briefs, not evidence. Consider stating the rerun method with `{REPO_ROOT}` in `VALIDATION.md`.
2. **(content) REQ-004 cites the topology but not the contract clause.** DEL-00-01 `ScopeOfWork.md` L99 (REQ-004) cites `D-GOV-43` A2 only. It reaches K-RUNTIME-1 through "the accepted v2 boundary recorded in CLM-005" (L81), which cites it. The owner and elements are identical, so this is not a defect.
3. **(content) AX-009 does not repeat the P02 label.** DEL-00-03 `ScopeOfWork.md` L156 lists "the basis provenance note" among the loci "brought current" without repeating that its first sentence was stale since SCA-004. The label lives in the ledger (P02 `why`) and in proposal L85 and L322, which the owner confirmed under 4(a). The contract bytes are ruled exact, so no change is suggested.
4. **(content) The uniform ADR note names SCA-006.** `ADRs.md` L12 says "premises that SCA-005 and SCA-006 made false", while every ADR hunk is an SCA-005 cause (proposal L110). This is by design, and the statement is not false.

## Model identity
The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The `high` reasoning effort and the role identity are instruction-asserted.
