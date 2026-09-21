# Brief — R0 calibration manager (WORKING_ITEMS, Type 1)

**Role:** WORKING_ITEMS. You own the R0 calibration undertaking. You dispatch bounded TASK
workers and one verifier, and you integrate their results. You never edit deliverables and
never run git. You return to HELP_HUMAN.

**Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128).

Placeholders are supplied at dispatch:

- `<FROZEN_TREE>`: read-only checkout at `00115c719`.
- `<RUN>`: the run folder in the working repository.
- `<APP_WORK>`: the working repository's `projects/chirality-app-dev`, used only to run the
  validator.

Read first:

- `agents/AGENT_WORKING_ITEMS.md` and `agents/AGENT_TASK.md` in `<FROZEN_TREE>`;
- `<RUN>/RUN_BASIS.md`;
- `<RUN>/CONVENTIONS_CANDIDATE.md`.

## Purpose

R0 tests the candidate method on a diverse sample before any scale-out. The owner decides
from your evidence whether each candidate convention is adopted, revised or dropped.
Measurement matters more than polish. Surface friction honestly.

## Units of work

All child outputs go under `<RUN>/R0_CALIBRATION/`.

| ID | Kind | Target | Output folder |
|---|---|---|---|
| F-01 | forward+reverse ledger | DEL-01-01 | `DEL-01-01/` |
| F-02 | forward+reverse ledger | DEL-02-05 | `DEL-02-05/` |
| F-03A | forward+reverse ledger (double-blind A) | DEL-03-01 | `DEL-03-01_A/` |
| F-03B | forward+reverse ledger (double-blind B) | DEL-03-01 | `DEL-03-01_B/` |
| F-04 | forward+reverse ledger | DEL-04-05 | `DEL-04-05/` |
| F-06 | forward+reverse ledger | DEL-06-04 | `DEL-06-04/` |
| F-08 | forward+reverse ledger | DEL-08-04 | `DEL-08-04/` |
| F-09 | forward+reverse ledger | DEL-09-07 | `DEL-09-07/` |
| F-10 | forward+reverse ledger | DEL-10-01 | `DEL-10-01/` |
| S-H | reverse-pass capability inventory | `frontend/src/lib/harness/**` (AREA `HARNESS`) | `SURFACES/` |
| V | verifier (after the above) | all of the above | `VERIFICATION.md` |

**Double-blind.** F-03A and F-03B get identical briefs apart from the output folder.
Neither may read the other's folder. Tell each only that another worker may exist.

## Concurrency and dispatch

- **Slot limit.** At most **12** of your children run concurrently. Suggested order:
  1. Launch S-H and the 9 forward workers together.
  2. Run pass 2 as each worker's forward ledger seals and S-H's capability file validates.
  3. Run V last.
- **Every spawn** uses the Agent tool with `model: "opus"`, a self-contained prompt that
  includes the placeholder values, and the worker brief below. Children are TASK (Type 2)
  and must not delegate.
- **APP-HOLD-1.** The dispatch preflight for all 8 targets returned `ALLOW`; see
  `<RUN>/PREFLIGHT/R0_*.json`. Confirm each file exists and says `ALLOW` before dispatching
  its unit. If any does not, do not dispatch that unit, and report it.
- **Pass 2.**
  - Prefer to resume the *same* worker with the capability file path, so it keeps its
    claim context. Load `SendMessage` via ToolSearch (`select:SendMessage`) and message the
    worker's agent ID.
  - If resuming is unavailable, dispatch a fresh worker with the sealed forward ledger and
    the capability file.
  - Record which mechanism was used for each unit.
- **Sealing.** When a forward ledger validates, compute its SHA-256 and append it to your
  state file *before* sending pass 2. After pass 2, recompute. A changed hash means the
  seal was broken: report it.
- **Validation.**
  - After each return, run `python3 <RUN>/_scripts/validate_ledger.py …` (§6 of the
    conventions) from `<APP_WORK>`.
  - A structurally failing output goes back to its worker once with the error list. If it
    fails again, a fresh worker reruns it.
  - Never patch a child's CSV yourself.
- **State.** Append one JSON line per dispatch or return to `<RUN>/R0_CALIBRATION/STATE.jsonl`:
  `{ts, unit, event, agent_id, model, mechanism, output_sha256, validator}`. You are its
  only writer.
- **Context discipline.**
  - Children return short summaries, not file contents.
  - Read child CSVs only through scripts: counts, histograms, comparisons.
  - Write any helper scripts under `<RUN>/R0_CALIBRATION/_scripts/`.

## Worker brief — forward and reverse ledger (F-units)

> You are a TASK (Type 2) worker in RUN_D128 R0 calibration. Do not delegate.
>
> **Target:** `<DEL-ID>` at `<FROZEN_TREE>/projects/chirality-app-dev/execution/<PKG>/1_Working/<DEL folder>/`.
> **Output folder:** `<RUN>/R0_CALIBRATION/<folder>/`.
>
> Read:
> - `<RUN>/CONVENTIONS_CANDIDATE.md`, all of it; it is your rulebook;
> - `<RUN>/RUN_BASIS.md` §3 and §5 (evidence roots, authority map);
> - your deliverable's rows in `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv`;
> - the two gate transcripts in `<RUN>/GATE_TRANSCRIPTS/`.
>
> Then read the deliverable's `ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`, `MEMORY.md`,
> `_DEPENDENCIES.md`/`Dependencies.csv`, `_REFERENCES.md` and `Assessment_INSP-03_*`.
> Consult `_SEMANTIC*.md` only if needed.
>
> Find implementation and verification evidence in the frozen tree's
> `projects/chirality-app-dev/frontend/` and `projects/chirality-runtime/{packages,tests}/`.
> For divergences, look for explaining direction in the CONTEXT sources of RUN_BASIS §5.
> Also look at `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/` for
> GOVERNING rulings.
>
> **Pass 1:**
> 1. Write `<DEL-ID>_claims.csv` and `<DEL-ID>_notes.md` in your output folder.
> 2. Run the validator until it reports zero errors.
> 3. Return: the file SHA-256; row count; disposition histogram; CauseTag histogram;
>    count of LOW rows; approximate files read; whether context was tight.
>
> **Pass 2** starts only when you are sent the capability file path. Then write
> `<DEL-ID>_reverse.csv` (and `<DEL-ID>_reverse_notes.md` if needed) and validate them.
> Never modify your sealed `_claims.csv`.
>
> **Rules:**
> - Read-only everywhere except your output folder.
> - No git, installs or test runs.
> - No absolute paths in outputs.
> - Do not read `projects/chirality-runtime/execution/**`.
> - Do not read the working repository's deliverable folders.
> - Do not read other workers' output folders.

## Worker brief — reverse-pass capability inventory (S-H)

> You are a TASK (Type 2) worker. Do not delegate.
>
> Inventory the implemented capabilities of `<FROZEN_TREE>/projects/chirality-app-dev/frontend/src/lib/harness/**`
> (AREA `HARNESS`) from the code itself. Do not read deliverable folders: this pass must
> not be anchored to them.
>
> Follow `<RUN>/CONVENTIONS_CANDIDATE.md` §5:
> - one row per observable behavior or contract surface;
> - 20–60 rows;
> - `CoveringTests` from `projects/chirality-app-dev/frontend/src/__tests__/**`;
> - `PostReleaseBasis=YES` if the behavior depends on `da95ec194`, `cb08dbe2f`,
>   `9ecbdecdf` or `ccb95e06a` (check with `git -C <FROZEN_TREE> log` read-only if
>   needed).
>
> Write:
> - `<RUN>/R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv`, ending with `#END`;
> - `HARNESS_notes.md`, covering the granularity rationale, files covered versus total, and
>   dead or unreferenced code observed.
>
> Validate with `validate_ledger.py capabilities`.
>
> **Return:** row count, SHA-256, and files covered out of total.

## Verifier brief (V)

> You are a fresh, evidence-only TASK (Type 2) verifier. Do not delegate. **Never edit any
> ledger.**
>
> Inputs: every `R0_CALIBRATION/*/` ledger, notes and reverse file; `SURFACES/`; the
> conventions; the frozen tree.
>
> Recheck:
> - (a) every non-ALIGNED, LOW-confidence or self-flagged row;
> - (b) a deterministic 15% sample of ALIGNED rows: select rows whose
>   `sha256(ClaimKey)` hex ends in `0`, `1` or `2`, then top up by lexical order to
>   reach 15%;
> - (c) 20% of `CLAIMED_BY`/`PARTIAL` responses, selected the same way on
>   `CapabilityID + ClaimKey`;
> - (d) 10 capability rows, for accuracy and granularity.
>
> For each rechecked item, open the cited evidence at the frozen tree and record
> `CONFIRMED`, `REFUTED` (with the correct reading) or `CONTESTED` (reasonable either way;
> give both readings).
>
> Write `<RUN>/R0_CALIBRATION/VERIFICATION.md`:
> - roster and source-state binding;
> - §1 the structural validator result for all files;
> - §2 a recheck table per unit (rows checked / CONFIRMED / REFUTED / CONTESTED);
> - §3 every REFUTED and CONTESTED item with evidence;
> - §4 systematic patterns: which conventions workers misapplied or found ambiguous.
>
> **Return:** counts and the three most important patterns.

## Your integration outputs

1. **`R0_CALIBRATION/DOUBLE_BLIND_COMPARISON.md`.** Script-derived from F-03A against
   F-03B:
   - agreement on base keys for `ClaimType`, `Disposition`, `AuthorityTier` and `CauseTag`;
   - split-rate difference;
   - agreement on reverse `Response`;
   - every disagreement listed with both readings.
   - Save the script.
2. **`R0_CALIBRATION/R0_CALIBRATION_REPORT.md`,** addressed to the owner through
   HELP_HUMAN:
   - §1 sample and roster: actual model and mechanism per unit;
   - §2 per-deliverable census: rows, dispositions, causes, LOW counts;
   - §3 validator and verifier outcomes;
   - §4 double-blind variance;
   - §5 reverse-pass findings: capability granularity; `CLAIMED_BY`/`PARTIAL`/`NOT_MINE`
     distribution; capabilities that no calibration deliverable claims;
   - §6 effort and context data, with a proposed **oversize threshold** (for example, claims or
     SoW bytes beyond which a manager should pre-gather evidence), justified by data;
   - §7 **convention verdicts:** a table covering every MR-1..MR-11 and every [EXT] rule,
     each marked `ADOPT` / `REVISE: <exact revised text>` / `DROP`, with the evidence;
   - §8 findings requiring owner attention (no action taken), including early cause
     clusters;
   - §9 a proposed R2 plan adjustment (worker sizing, manager span, wave order).
   - This report is agent judgment, never a ruling.
3. **Return to HELP_HUMAN, in 15 lines or fewer:**
   - completion state;
   - paths and SHA-256 of the report, verification and comparison files;
   - headline numbers;
   - any seal break, preflight problem or rerun.
