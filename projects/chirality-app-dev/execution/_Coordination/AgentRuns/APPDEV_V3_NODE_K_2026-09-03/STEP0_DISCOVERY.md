# Step 0 — Discovery (before product/test edit)

Run: `APPDEV_V3_NODE_K_2026-09-03` · Date: 2026-09-03 · Agent:
OpenAI / Codex / GPT-5 family (exact model identifier not exposed to the agent runtime),
bounded ephemeral Agent 2 under HELP_HUMAN.

## Basis and loader

- Scratch worktree is clean on branch
  `codex/app-v3-nodeK-security-proof-negative-tests-2026-09-03` at exact basis
  `fe0ce926d4475fa41cb91933ad1218b95083889b` (PR #690 merge).
- `LOOP_INIT.md` selection over committed HEAD chose exactly
  `loop/WORKPLAN_2026-09-03_app_dev_loop.md`, mode `100644`, type `blob`, object
  `5049fdbd3018a11050b4f8013d73311346b843cc`; bytes were read through `git show`.
- Receipts validator: PASS (`VALID`, frozen through Receipt-52; versioned
  receipt contract satisfied). Live receipt cursor supplied by HELP_HUMAN is Receipt-216.
- Pinned completion reference SHA-256: PASS,
  `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`.
- Authority corpus: PASS, current v20, all eight members match, no drift.
- APP-HOLD dispatch preflight for DEL-09-06: PASS / ALLOW; no held deliverables.
- Harness self-check: initial `/usr/bin/python3` invocation was an environment
  setup failure because that interpreter lacks PyYAML; rerun with the host's
  dependency-capable Python 3.13 interpreter passed at the unchanged baseline
  (INFO 14, NOT_APPLICABLE 1, REVIEW 4, WARN 43). The final registered run will
  place that interpreter first on PATH and records its own result.

## Live selectability and dependencies

- `_STATUS.md` records DEL-09-06-V3-06 as `SELECTABLE`, with no owner gate.
- V3-05 is landed and its History entry records the Node G proof and review.
- `Dependencies.csv` and `_DEPENDENCIES.md` identify no additional blocker for
  this tests-only follow-on. The existing test path and Vitest command resolve
  the old generic TBD test-framework slot for this item without editing the
  dependency files.
- The cited Node G review G1-F1 directly exercised the real summarizer and found
  both requested cases already fail closed; this node asserts those behaviours
  in the unit suite and does not alter the summarizer.

## A1 re-stage declaration

This tranche mutates
`projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`.
Under the owner-recorded A1 rule, **any mutation under
`projects/chirality-app-dev/frontend/` invalidates the staged R20 procedure for
any future proof claim and requires a newly staged revision and a fresh
owner-executed proof**. Historical R20 evidence remains historical only. This
tests-only tranche makes no fresh proof, release, signing, notarization,
distribution, publication, release-readiness, acceptance, certification, or
professional claim.

## Sealed write locus

Before review: the one named test file, this AgentRuns packet, and the required
DEL-09-06 TASK run record. No product source, summarizer, package configuration,
plans, register, decision, Root, other deliverable, `_STATUS.md`, `MEMORY.md`,
receipt, final handoff, or final manifest byte is writable before `REVIEW_PASS`.
