# Orchestration Plan v1 — D-APP-71 Application

- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION`
- **Plan version:** 1
- **Selection authority:** HELP_HUMAN / Agent 0
- **Posture:** `SERIALIZED_R5_APPLICATION`
- **Branch:** `codex/app-dev-dapp71-application-20260720`
- **Shared-main basis:** `3346120cb7c765aa7a230ee4c579ecd14f2cb022`
- **Parent receipt:** Receipt-81
- **Authority:** D-APP-71 Option 2 — DEL-02-05 physical lead
- **Lifecycle transition:** prohibited
- **Frontend/runtime source writes:** prohibited
- **Hard-fence or waiver effects:** prohibited

This plan releases one RECONCILIATION integration owner to apply the already
ruled D-APP-71 coordination mapping to documentary truth. It is a control
record, not a new decision, scope source, decomposition source, or lifecycle
act. V1 EVALUATION and CHANGE are represented only as dependency-gated future
nodes and are not released by plan v1.

## Frozen accepted basis

The strict-JSON basis manifest is `BASIS.json`, SHA-256
`3ef9c6e03fe6d58e1db67227c5826b87426033fef44bae732279b1de82df372e`.
Its 20 direct-file bindings and three frozen-tree bindings reproduced at
release. The load-bearing bindings are:

| Input | SHA-256 |
|---|---|
| D-APP-71 ruling | `153de2b988eee9eb99c4c6996cf4045b9e553fccd76cc6c0791f4fc32d71de4e` |
| D-APP-71 packet | `711cd2e238362819f601c838c807f729e873c4a05ce478a3de4615ce6985f18c` |
| Decision register | `af1a6dec6f30e81fc19a1aab4ecf2f99874c35c97e8d83aafadeb18ebcb33920` |
| `frontend/electron/preload.ts` | `189b0d30bd8f6daf84862e14cfc3ec68c2c211b5c123283c7108c50c3b750ba0` |
| Receipt ledger through unique latest Receipt-81 | `599e12e2606530be853ff0ac600f7f4377413f4e165e343bcc127ee2bef6f2b1` |
| DEL-02-05 `_STATUS.md` | `bcb26d3e17e3ac278846a1a3a94ec376b555272ffaff904e9335bdea5fdc548e` |
| DEL-09-04 `_STATUS.md` | `e571ae16bc62800f6d14ce33630a6d7b1414fdebcccc35b6bb11c0be93c476f3` |

The immutable upstream derivative is
`execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/APPLIED_DAPP70_36A422AC/`.
It contains exactly seven files. Its sorted path-list SHA-256 is
`bdbf139da07a5a00ef90bf0b78b00c24bb48e64e4a6f8433026fe5c14f1fa9bd`;
its sorted content-manifest SHA-256 is
`82d585a2a22aac4a27dbee39461917077f80a7b5b9f4cbff75750332f930df16`;
and its `MANIFEST.json` SHA-256 is
`40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e`.
Every file remains immutable.

## Exact application

R1 applies DEL-02-05 as the physical coordination lead for the one path
`projects/chirality-app-dev/frontend/electron/preload.ts`. This does not
transfer semantic responsibility: DEL-02-03 retains `selectDirectory`,
DEL-02-05 retains `apiKey`, and DEL-09-06 retains `safeStorage` and security.
No source repair is implied or authorized.

R1 creates a new additive seven-file derivative only at:

`execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/APPLIED_DAPP71_3346120C/`

Its exact filenames are `RUN_BASIS.md`, `APPLIED_MAPPING.csv`,
`RETAINED_BOUNDARIES.md`, `REMAINING_DISPOSITION.csv`, `QA.md`, `HANDOFF.md`,
and `MANIFEST.json`. The schemas and required headings are frozen in the R1
launch brief.

R1 may edit only the DEL-02-05 and DEL-09-04 `_STATUS.md` files, create exactly
one new local record beside each, append exactly Receipt-82, create the new
derivative, and complete its own return/handoff/status files. DEL-02-05 gets
one history entry recording coordination-lead application; its empty
`Remaining` section and lifecycle fields remain unchanged. DEL-09-04 loses
only its D-APP-71 preload residual, receives one history entry, and preserves
its packaging/release Remaining line byte-for-byte.

The exact local-record basename in both deliverables is
`R1_DAPP71_PRELOAD_PHYSICAL_LEAD_APPLICATION_2026-07-20.md`.

## Frozen work graph

| Node | Role | State | Depends on | Fan-in gate |
|---|---|---|---|---|
| R1-DAPP71-APPLICATION | RECONCILIATION | `READY_RELEASED` | frozen basis | Terminal `ACCEPT \| BLOCK` with RETURN/HANDOFF/STATUS; HELP_HUMAN validates exact application, hashes, schemas, preservation, receipt, and containment |
| V1-DAPP71-APPLICATION-BACKCHECK | EVALUATION | `PLANNED_HELD_NOT_RELEASED` | accepted R1 fan-in | A separate versioned release is required |
| G1-DAPP71-PUBLISH | CHANGE | `PLANNED_HELD_NOT_RELEASED` | accepted V1 and closeout checks | A separate versioned release is required |

R1 is the sole serialized integration owner and may not delegate. Failed or
stale input returns `BLOCK` before shared-file writes. Plan v1 authorizes no V1
or CHANGE action, staging, commit, push, PR, merge, branch deletion, or cleanup.

## Validation and rerun rules

Before writing, R1 must reproduce `BASIS.json`, all direct bindings, all three
frozen trees, exact branch/HEAD, unique latest Receipt-81, D-APP-71's ruled row,
receipt validation, authority corpus v9 no-drift, repository self-check exit
zero at the existing 3 REVIEW / 6 WARN baseline, and a complete containment
inventory. After writing it must validate strict duplicate-key JSON, exact CSV
schemas and populations, all frozen no-change hashes, receipt/corpus/self-check,
`git diff --check`, no-index whitespace checks for every new file, and final
write containment.

Any basis hash change, prior-derivative mutation, source/status/Remaining
change, register/ruling conflict, receipt cursor change, unexplained baseline
change, unauthorized path, validation failure, or ambiguous retained boundary
invalidates the release and requires terminal `BLOCK`. Waivers: none.
