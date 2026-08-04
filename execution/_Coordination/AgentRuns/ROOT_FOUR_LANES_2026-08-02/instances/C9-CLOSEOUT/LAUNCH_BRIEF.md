# C9 CHANGE launch brief — exact ruled closeout for PR #491

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Node: `C9`
Role: `CHANGE` (Agent 1)
Plan: `ORCHESTRATION_PLAN_V22.md`
Work graph: `WORK_GRAPH_V22.json`

## Objective

Publish the exact already-validated W7 decision-support tranche, SCA-003
zero-action close record, DEL deferral/provenance hygiene, and routed G1-B App
notice to the existing branch and PR #491, then verify all three required
checks on the exact remote head. Do not merge.

## Required preflight

1. Load and follow `agents/AGENT_CHANGE.md` in full.
2. Verify branch `codex/root-four-lanes-20260802`, current local HEAD
   `c886cc136cd095dbdc6e6e5841e1a8f91c8c329c`, and PR #491.
3. Fetch remote refs. Confirm current `origin/main` is an ancestor of HEAD.
   If remote main advanced beyond contained `cf6bc15b…a5c3`, stop before
   staging and return exact drift; do not rebase, merge, or force.
4. Confirm no staged or unmerged paths and inventory every changed/untracked
   path in the tranche.

## Accepted inputs

- Owner ruling SHA-256
  `671dd05838c75a0e885052f52e951ab5609ac44b4db66a90f0fe283cba071aea`.
- S7 RETURN/STATUS:
  `13cbce630b1953848448a599b36f7bd5d2c90dca8c717a1b1354fdc63b76a034` /
  `8a2daaa30524f834c96dde58562402fe4f4138f34b789469a1f60baf50a7e904`.
- W8 RETURN/STATUS:
  `6ec5ee9e02855887d4957e3885d3f1ea72bf446b65bcdc3d07ed9cd64e32635a` /
  `b4762146a6bd94a381c35c10d3587f1629d18b3a1a819d714cb4b4345e405711`.
- H5 RETURN/STATUS:
  `12ef39533deffcb1a22e407573c9691ef693d1a2e1ba89d8a344182fd6fad0b8` /
  `a31388dc25e21f57df2668691c394fd38d7111ee63a0b265e767fefdb567ac7e`.
- W7 admitted manifest:
  `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`.
- SCA closure record:
  `a57833a661d1f9690f7d83662ee3e97c92fc85a76774333f10de5e02023b600a`.
- Routed App notice:
  `618c5c3edbf55a04eeefbf513e08a566fa1ef751febb3f6dcbe2c07e453af6b4`.
- `_ScopeChange/_LATEST.md` protected SHA-256:
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.

## Validation before staging

- Reproduce all accepted manager and artifact hashes.
- Verify the decision-support manifest against all three members.
- Run `python3 tools/validation/validate_candidate_whitespace.py --base-ref HEAD`.
- Parse governed JSON/JSONL in the changed tranche.
- Run `git diff --check`.
- Confirm no changed Task Management register, `_ScopeChange/_LATEST.md`,
  Root PRD/decomposition, runtime implementation, or App source/dependency
  path.

These are closeout checks, not another semantic verification round.

## Git and PR action

After the validation passes, stage the exact tranche, create one ordinary
commit, and push the existing branch without amend, rebase, force-push, or
direct main mutation. Update PR #491's body with:

- SCA-003 closed zero-action/no-change; Gate 2 unopened; `_LATEST` unchanged;
- W7 manifest accepted as decision support only; DEL owner selection deferred
  to a dedicated session against committed main after PR #491 merges;
- no selection, adoption, implementation, or N0 restart;
- exactly three EOF bytes normalized with 3/3 preimage proof and no third
  semantic verifier;
- G1-B App notice routed for PIA-U20–U25; no App acceptance/work dispatch, Pi
  approval/supersession, or PIA-U30 dispatch;
- exact validation evidence and all remaining owner gates.

Wait for all three required checks on the exact remote source head. Return the
branch/head/commit, PR URL, check names and conclusions, changed-path count,
and explicit confirmation that PR #491 remains open and unmerged.

## Forbidden

No semantic edit or repair, merge, rebase, force-push, amend, register write,
SCA Gate 2, DEL selection/adoption/implementation/N0 restart, App acceptance
or dispatch, Pi approval/supersession, PIA-U30, lifecycle/release/reliance, or
professional act.
