# App post-Root integration and login-proof enablement — orchestration plan v1

Status: `FROZEN BEFORE NODE DISPATCH`

## Activation identity

- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- Parent: `HELP_HUMAN`
- Selection authority: `HUMAN`
- Branch: `codex/app-post-root-login-proof`
- Accepted basis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
  (`origin/main` after fetching; contains PR #602 merge
  `adf805e0d9ac55787e8ac815c3018467babb7f50`)
- Pattern: `TERMINAL_FAN_OUT_IN`, owner-directed `N=3`, followed by serialized
  shared-surface fan-in and CHANGE closeout.
- Authority transcription: `CHAT_TRANSCRIPTION.md` in this run root.

## Basis gate

- `agents/AGENT_HELP_HUMAN.md`: Git blob
  `a9e538c0d9603e18d9884e9f60489be6df8ba1ff`, SHA-256
  `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`.
- `tools/validation/validate_agent_instructions.py` admits Agent 0 to canonical
  TASK and Agent 0/1 generalist opt-in while retaining the named failure paths.
- Both routed Root notices are present; the TM117 notice SHA-256 is
  `fd587b676a55c42feecd2c0e9dbcb96d67a1f2bcff3d5ab66d6fdb78826fdaf0`.
- Receipt validator passes through the live Receipt 184 ledger; authority
  corpus v18 has no drift; practitioner status has no findings; repository
  self-check exits zero with only the pre-existing non-App baseline.

## Work graph

### N1 — PKG-08 / DEL-08-04 post-Root integration

- Manager: `WORKING_ITEMS`; instance `WI-PKG08-POST-ROOT-INTEGRATION-01`.
- Objective: execute and evidence all four owner-enumerated cross-surface
  admission/fail-closed/check groups against App commit `ac2cd801...`, remove
  only the satisfied post-Root Remaining item, retain D-APP-103, and
  acknowledge the TM125 notice through App instruments.
- Write owner: DEL-08-04 status/memory/run records and this instance's unique
  run-control directory. Root surfaces are read-only.
- Return: validated PASS or calibrated failure matrix, exact commands/results,
  changed paths, and remaining blockers.

### N2 — App Task Management / TM-APP-032 re-scope

- Manager: `TASK_MANAGEMENT`; instance `TM-APP-032-RESCOPE-01`.
- Objective: run federation preflight, apply the owner-directed byte-exact
  trigger replacement while keeping the row DEFERRED, disposition the
  TM-ROOT-117 closure echo, supersede the held draft notice, and record the
  shared DEL-02-06 acceptance gate without accepting a successor identity.
- Write owner: App `_TaskManagement/**` only plus this instance's unique
  run-control directory. Shared receipt is reserved to fan-in.
- Return: validated row/notice dispositions with source and evidence hashes,
  federation coverage, changed paths, and closure-echo result.

### N3 — PKG-09 / DEL-09-04 packaged owner-procedure staging

- Manager: `WORKING_ITEMS`; instance `WI-PKG09-LOGIN-STAGING-01`.
- Objective: build the unsigned app with `npm run desktop:pack`, bind it to the
  exact 40-character build commit, prove the frontend-tree diff condition, and
  stage the concrete owner-only procedure without executing prepare, bootstrap,
  kickstart, logout/login, or capture.
- Write owner: DEL-09-04 status/memory/run records and this instance's unique
  run-control directory. Operator LaunchAgent and launcher paths are forbidden.
- Return: packaged app path, build commit, frontend-diff proof, concrete
  `PROOF_*` values, expected launcher-effect note, checks, and blockers.

## Dependencies, concurrency, and failure isolation

- N1, N2, and N3 have no semantic dependency on one another and have disjoint
  project-truth write surfaces. They may execute concurrently.
- All nodes read the same frozen basis. No node may commit, stage, push, open a
  PR, write `loop/LOOP_RECEIPTS.md`, or write shared completion surfaces.
- A failed review returns to the affected node for no more than two repair and
  fresh-review cycles. Failure holds only that node; passing nodes remain
  eligible for landing.
- Any mid-run `main` advance is reported to the owner; no sync occurs without
  owner authorization and any allowed sync must be non-rewriting.

## Fan-in and human gates

- HELP_HUMAN accepts only validated manager returns, then serializes shared
  surfaces once. CHANGE performs commit ordering N1, N2, N3, then after-the-fact
  receipt/fan-in, exact project-only staging verification, push, and one PR
  against `main`. No merge.
- Login/logout/capture, prepare, bootstrap, kickstart, operator deployment,
  signing, notarization, distribution, publication, issuance, release-readiness
  claims, provider expansion, and every not-selectable row/item remain outside
  this run.
