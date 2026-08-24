# APP-DEV LOOP STEER — v3 Phase 2: K-EVENT-4 regeneration and companion-register rebuild — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: App-dev loop (`projects/chirality-app-dev/`). The loop's instruments govern; this steer directs one bounded phase under them. Companion instruments: ruling records A4 (SHA-256 `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`) and A5 (SHA-256 recorded in the PR that published this steer — the files merged together), the decision-input package (SHA-256 `4d16cefae5dc672376a62ae00437c27ff857e7d994206549e888da3409f40c2a`), and the concordance workplan inside the SCA-APP-008 snapshot.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `d548be045c0d31b5b4c8d944507d57abd5d8f049` (PR #652, ruling record A4).
- The SCA-APP-008 Phase-1 package at its A3-approved identities: Gate-3 `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`; Gate-4 `47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6`; concordance workplan `c747a81b7fcca88dfebab8e2ed2345247af23063d9f48e3dd2e4bfa0a5af4185`.
- The eleven frozen assessment identities from ruling record A2.
- App contract `projects/chirality-app-dev/docs/CONTRACT.md` SHA-256 `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`.
- Companion register `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` SHA-256 `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`.
- `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`.
- `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6` (13 rows; byte-identity at close as well).
- Frontend tree object `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- Root sources for the selected identity, at the A4-A pinned blobs: `docs/CONTRACT.md` `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`; `runtime/packages/cli/src/config.ts` `40cec2df6c21fa10a5a053ff6e40ea0b6d9d4a352208660cc01eb22f5fc7523e`; `runtime/packages/core/src/session-store.ts` `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad`; `runtime/packages/contracts/src/events.ts` `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd`; `runtime/packages/contracts/src/session.ts` `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51`. If any Root blob has changed on `main`, stop and report — the selection is bound to these bytes.

## Authority context

A4-A selects the canonical Root session-store identity:

```text
{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl
where {userData} = ~/Library/Application Support/Chirality
event schema:   chirality.event/v1
session record: chirality.session/v2  (session.json beside events.jsonl)
```

A4-C confirms K-ROLE-2 as a permitted specialization (candidate unchanged).
A4-B sequences Root's K-CONTROL-1 amendment ahead of App application; A5-B
directs that Root design amendment; A5-C keeps the single Gate-5. This
phase regenerates candidates and evidence only. Nothing here applies a
contract row, moves the pointer, changes the register as truth, routes the
notice, or claims eligibility the sequencing rules deny.

## N1 — regenerated K-EVENT-4 candidate

Produce the exact regenerated K-EVENT-4 contract-row candidate from the
selected identity, replacing the question-bearing candidate: the Root-owned
shared-runtime session store at the exact selected path and schema/version
identities is the canonical runtime audit record; one writer (the Root
daemon per Root K-RUNTIME-1); project-local
`.chirality/sessions/<id>/events.jsonl` is a legacy App compatibility
source read and lazily migrated non-destructively (Root K-STORE-2), never a
second active writer or authority replacement; App `UIEvent` streaming and
replay remain projections of accepted runtime records. Carry the full
transaction form (pre-image = the live App K-EVENT-4 row with SHA and line
cite; exact post-image bytes; new post-image SHA-256). State the A4-A
binding (record SHA and the five Root blob identities) in the candidate's
grounding.

## N2 — companion-register rebuild

Produce the exact companion invariant-coverage register post-image
candidate covering the resolved amendment set: the regenerated K-EVENT-4
row; new rows K-CONSENT-1 and K-UNTYPED-1; the confirmed K-ROLE-2 update;
K-NET-1, K-KEY-1, K-EVENT-3, K-EVENT-6 and the consequential
enforcement-map rows as approved in Gate 3; and **K-CONTROL-1 marked
`PENDING_ROOT_AMENDMENT`** — the register candidate must not claim
coverage or eligibility for K-CONTROL-1 until Root's ratified row is
amended (A4-B/A5-B). Preserve the register's 81-ID/48-family accounting
discipline: every changed or added row exact, no stale coverage claim,
full-file candidate with pre/post SHA-256.

## N3 — review and return

Fresh independent review of both candidates against: the A4-A selected
identity and its Root source bytes; the approved Gate-3 package; the
Gate-4 plan's companion-register requirement; and the sequencing rules
(K-CONTROL-1 ineligible; single Gate-5). Unlimited repair with fresh
re-review; every repair disclosed. Close `AWAITING_OWNER_APPROVAL` with a
four-state handoff naming the two candidate identities and restating that
Gate-5 eligibility for the contract group begins only when the Root
K-CONTROL-1 amendment is ratified and the owner approves these exact
candidates.

## Write set, exactly

- New files strictly inside
  `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/`
  (additions only; every previously approved or frozen file in the
  snapshot is immutable — the regenerated candidates are new files, e.g.
  under a `Phase2/` or `Resolved/` subfolder per house convention).
- Run/control evidence under
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE2_2026-08-<DD>/`.
- One append to `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`
  (Receipt 197; parent Receipt-196; incorporate this steer and records A4
  and A5 by immutable path and SHA-256).

Not selectable: `projects/chirality-app-dev/docs/CONTRACT.md`; the
companion register itself; `_LATEST.md`; any register, SOW, `_STATUS.md`,
`_DEPENDENCIES.md`, `_Evaluation`, or `_Decomposition` file; anything
under `projects/chirality-app-dev/frontend/` or
`projects/chirality-app-dev/docs/`; any Root-loop path; any other project.

## Discipline

- Run the candidate-whitespace validator before generating any artifact
  that pins another artifact's hash; on later repair, regenerate the
  pinning artifact or record exact pre→post lineage in the receipt.
- Run before pushing: candidate whitespace (base = the basis merge
  commit), agent instructions, instruction entrypoints, CI-form G4 (expect
  zero instruction-surface paths and zero required manifests), taskmgmt
  validate (register byte-identity preserved), the App receipts validator,
  frontend tree identity, and `git diff --check`.
- Branch `codex/app-v3-phase2-2026-08-<DD>`. Do not merge. If `main`
  advances, request sync authorization from the owner and record the grant
  verbatim in the receipt. HELP_HUMAN byte-verifies before endorsement.
