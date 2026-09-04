# STEP 0 DISCOVERY — APPDEV_V3_NODE_M_2026-09-04

Recorded before the first repository mutation on 2026-09-04.

## Basis and isolation

- `git rev-parse HEAD` and `git rev-parse origin/main` both returned
  `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge).
- Branch:
  `codex/app-v3-nodeM-a15-owner-rulings-2026-09-04`.
- Scratch worktree:
  `/private/tmp/chirality-app-v3-a15-20260904/nodeM`.
- `git status --short --branch` was clean.
- The current ledger tail was Receipt 219. The provisional closeout
  assignment was therefore Receipt 220 with Parent-Receipt Receipt-219,
  subject to re-evaluation before freeze.

## Required discovery checks

| Discovery | Command / evidence | Result |
|---|---|---|
| Receipt contract | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` | VALID |
| Authority corpus | from `projects/chirality-app-dev`: `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` | v20; all references MATCH; no drift |
| Git status | `git status --short --branch` | clean basis branch |
| Decision-register scan | searched `execution/_Coordination/_DECISIONS/_REGISTER.md` for `AWAITING_RULING` and `NOT_PREPARED` | no matching open row |
| APP-HOLD reliance | from `projects/chirality-app-dev`: `python3 execution/_Scripts/app_hold.py check --operation reliance --entry-path loop/LOOP_INIT.md --target DEL-09-05 --target DEL-09-06` | ALLOW for both targets |
| APP-HOLD dispatch | same command with `--operation dispatch` | ALLOW for both targets |
| APP-HOLD integrity | `python3 execution/_Scripts/app_hold.py scan --require-register-match` | PASS; register SHA `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `1f6685f6e64619e4fb39fffde12b6f5981ae163b15a8298252467a8558fb8bff` |
| Pinned completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, exact match |
| A14 | `shasum -a 256 plans/steers/chirality_app_v3_app_ruling_record_a14_2026-09-03.md` | `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`, exact match to Node I manifest |
| Harness status | `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3 tools/practitioner_harness/harness.py status --project chirality-app-dev` | PASS; no finding severities |
| Harness self-check | `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3 tools/practitioner_harness/harness.py self-check` | PASS; unchanged baseline findings |

An initial harness-status invocation omitted the required `--project`
argument and exited with a usage error. The command shape was corrected and
the required invocation above passed; no pass was inferred from the rejected
invocation.

## Live ruling and state verification

- A14 is immutable dated history: on 2026-09-03 it deferred the Syft
  `v1.18.1` owner-host install and the disposable identity owner-host act.
  A15 may lift those deferrals prospectively without invalidating A14.
- `syft` was not found on the host, so Syft `v1.18.1` is not observable.
- `security find-identity -v -p codesigning` reported no valid identities,
  so the required owner-created disposable identity is not observable. No
  private key material was read or changed.
- DEL-04-05 `_STATUS.md` records `DEL-04-05-V3-01` landed on 2026-09-03.
- The live app tree contains exactly four packaged route pages:
  `frontend/src/app/page.tsx`, `chat/page.tsx`, `pipeline/page.tsx`, and
  `workbench/page.tsx`, corresponding to `/`, `/chat`, `/pipeline`, and
  `/workbench`.
- DEL-09-06-V3-04 was gated on the nonce/rendering-mode ruling. A15 can make
  it selectable; the work itself is not executed here.
- DEL-09-06-V3-03 remains a separate item and is not retagged or split by
  this tranche.

## Scope and fence declarations

- Record-only write set: one A15 record, the two named `_STATUS.md` files,
  this node M run record, and one append-only ledger receipt.
- No `frontend/` path is touched. The A1 re-stage rule is not applicable and
  no re-stage declaration is needed.
- No product, host, Root, lifecycle, Checking Approval SHA, register,
  decomposition, or SCOPE_CHANGE mutation is authorized.
- F-APP-2 remains intact: no Developer ID signing, notarization, Apple call,
  distribution, publication, release-readiness, or production identity act
  or claim.
