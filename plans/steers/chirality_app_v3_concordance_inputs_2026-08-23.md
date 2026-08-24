# CONCORDANCE DECISION INPUTS — SCA-APP-008 contract group — assembled 2026-08-23

> **Plans-folder status:** ACTIVE decision-input package — non-governing evidence assembly. Prepared by HELP_HUMAN under ruling A3-C (`plans/steers/chirality_app_v3_app_ruling_record_a3_2026-08-23.md`, SHA-256 `91d6867286de465f56bb41a6de9e9d8657e6b63ddb009f294d81b3e6dcccded9`) against the workplan at `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Concordance/CONCORDANCE_WORKPLAN.md` (SHA-256 `c747a81b7fcca88dfebab8e2ed2345247af23063d9f48e3dd2e4bfa0a5af4185`). Every SHA-256 below was computed by HELP_HUMAN from `origin/main@1bd3eef47782f350de5714200206466c5d4b6b21`. This package records no ruling; every disposition is the owner's act (K-AUTH-1).

## C-01 — K-EVENT-4 exact live Root session path

**Finding: a single live Root value exists and is fully derivable from
ratified Root contract rows plus committed runtime source.** No accepted
Root surface pins the literal path bytes in one row; the ratified rows
anchor ownership and format, and the committed implementation fixes the
exact bytes.

Derived canonical identity (owner selection candidate):

```text
{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl
where {userData} = ~/Library/Application Support/Chirality
event schema:   chirality.event/v1
session record: chirality.session/v2  (session.json beside events.jsonl)
```

Byte-bound evidence chain:

| # | Claim | Source | Identity |
|---|---|---|---|
| 1 | Ratified ownership: one opt-in per-user daemon is the exclusive production owner of sessions (one-writer invariant) | `docs/CONTRACT.md` row **K-RUNTIME-1** (line 161) | blob SHA-256 `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`; RATIFIED 2026-07-11 (K-AUTH-1) |
| 2 | Ratified format and migration: central runtime sessions remain JSON/JSONL; legacy project-local sessions import lazily and non-destructively | `docs/CONTRACT.md` row **K-STORE-2** (line 164) | same blob |
| 3 | Ratified base notation `{userData}/runtime` | `docs/CONTRACT.md` row **K-CONTROL-1** (line 162, `{userData}/runtime/control.sock`) | same blob |
| 4 | `{userData}` resolves to `~/Library/Application Support/Chirality`; `runtimeDirectory = {userData}/runtime` | `runtime/packages/cli/src/config.ts` lines 19–21 | blob SHA-256 `40cec2df6c21fa10a5a053ff6e40ea0b6d9d4a352208660cc01eb22f5fc7523e` |
| 5 | Store layout `runtimeDirectory/projects/<projectId>/sessions/<sessionId>/` with `events.jsonl` and `session.json`; files mode 0600 under private directories | `runtime/packages/core/src/session-store.ts` lines 392–407 | blob SHA-256 `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` |
| 6 | Event schema identity `chirality.event/v1` | `runtime/packages/contracts/src/events.ts` line 17 | blob SHA-256 `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` |
| 7 | Session record identity `chirality.session/v2` | `runtime/packages/contracts/src/session.ts` line 5 | blob SHA-256 `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51` |
| 8 | Non-destructive legacy migration with `legacy.sourcePath` provenance; legacy layout `<root>/<sessionId>/events.jsonl` matches the App compatibility source `.chirality/sessions/<id>/events.jsonl` | `runtime/packages/core/src/session-store.ts` lines 240–270 (legacy import path at line 255) | same blob as #5 |
| 9 | Daemon sole-owner statement in runtime docs | `runtime/README.md` line 7 | blob SHA-256 `a90c9e19bb83c32229255db19102bc34095060a0fc2feeb4736f6ecd0370a7bb` |

App-side comparison (workplan item 5): the App legacy path is exactly the
K-STORE-2 lazy-import subject; the runtime migrates it non-destructively
into the central store and records provenance. One active writer (the
daemon) is preserved; App streaming/replay remain projections.

**Decision fork for the owner:**

- **Select the derived identity** above as the K-EVENT-4 canonical value,
  citing rows K-RUNTIME-1/K-STORE-2 for ownership/format and the three
  runtime blobs for exact bytes and versions. The App loop then regenerates
  the exact K-EVENT-4 candidate from the selected value (workplan item 6)
  for fresh Root/App review.
- **Or HOLD (`K_EVENT_4_PATH_UNRESOLVED`)** on the ground that no single
  *contract row* pins the literal bytes, directing Root to add such a row
  through its own instruments first (natural carrier: the accepted
  DEL-02-10 adapter/event-schema work). This sequences K-EVENT-4 behind a
  Root contract amendment.

## C-02 — cross-loop invariant-ID collision matrix

Inventories (deterministic extraction, pattern `K-[A-Z0-9]+-[0-9]+`):

| Surface | Identity | IDs |
|---|---|---|
| Root contract `docs/CONTRACT.md` | `ed87eaff…` (above) | 40 unique |
| App contract `projects/chirality-app-dev/docs/CONTRACT.md` | SHA-256 `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | 81 unique |
| App coverage register `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` | SHA-256 `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | 81 unique (matches the contract) |

Results:

1. **Proposed new IDs are unused in both loops.** `K-CONSENT-1` and
   `K-UNTYPED-1` appear in neither contract, neither register, nor any
   accepted surface searched. No occupation conflict.
2. **Of the eleven amendment-relevant IDs, only two exist in the Root
   contract:** `K-CONTROL-1` and `K-ROLE-2`. `K-NET-1`, `K-KEY-1`,
   `K-EVENT-3/4/6` are App-only rows. `K-SUBAGENT-1/2/3` (enforcement-map
   references) are App contract rows; on the Root side they appear only in
   the D-GOV-35 decision corpus, not in the ratified Root contract — no
   contract-row collision.
3. **K-ROLE-2 — classification: permitted App specialization.** The App
   post-image preserves Root's ratified core sentence (role names authority
   and responsibility, not a durable model assignment; runs record actual
   adapter/provider/model and substitutions) and adds App-side enforcement:
   role-posture digest, G-ROLE labeling, `role not mechanically enforced`,
   `instruction-asserted` evidence calibration, and the D-GOV-35-aligned
   clause that native descendants acquire no role by descent. Root's row
   would remain unchanged. Residual owner check: confirm Root sees the
   additions as compatible specialization.
4. **K-CONTROL-1 — classification: cross-loop tension requiring an owner
   disposition.** Root's ratified row (line 162) asserts runtime control
   uses the single authenticated socket `{userData}/runtime/control.sock`
   with no TCP listener. The App post-image asserts **exactly two**
   purpose-limited sockets — the existing daemon API plus a private
   daemon-to-Process-Supervisor socket — and describes the runtime
   directories as "app-owned". The second socket corresponds to the
   R7-accepted Root carrier DEL-02-07 (Process Supervisor and
   Purpose-Limited Control), which is accepted scope, not yet ratified Root
   contract truth; and "app-owned" sits uneasily beside Root K-RUNTIME-1's
   daemon-exclusive ownership. Applying the App row as written would have
   the App contract assert Root architecture ahead of Root's own contract.
   Owner dispositions available: (a) sequence — amend Root K-CONTROL-1
   through Root's instruments (natural carrier: DEL-02-07 output) before or
   together with the App application; (b) rule the App row a permitted
   forward-looking specialization grounded in R7-A acceptance, with the
   Root amendment to follow; (c) revise the App candidate wording to
   describe the supervisor socket conditionally on Root contract state.
5. **Remaining 25 shared IDs** (K-AUTH-1, K-DEP-1/2, K-DOMAIN-1..4,
   K-GATE-1, K-SEAL-1, K-SNAP-1, and companions) are pre-v3 shared
   governance vocabulary defined by each contract for its own loop; none is
   touched by the Gate-3 amendments, and no amendment repurposes an
   existing ID's meaning. Recorded as historical parallel definitions
   outside this amendment's scope.
6. **Reference integrity:** the committed Gate-3 candidate validator
   (rerun by HELP_HUMAN at the PR #647 head, verdict PASS) checks the
   9 contract candidates and the carrier package deterministically;
   the mechanical Gate-4 reconstruction matched N1's post-image hashes.

## C-03 — routing moment for `DRAFT_NOTICE_TO_ROOT.md`

Frozen draft: SHA-256
`8ebc728b6d6c408a3dfeb60ae07887dbe7d5b88ba8fe06c1b954e98e8a380f72`,
unrouted, written at assessment time (it describes SCA-APP-008 as assessed
but not yet accepted — now stale as notice content, exactly as the workplan
anticipated).

Current state satisfying workplan items 1–3: Gate-3/Gate-4 approved at A3
(`1a8048f4…` / `47daaedf…`); Gate 5 has not occurred; App `_LATEST.md`
remains `a0298fdc…` with no pointer move.

Alternatives for the owner:

- **Route after Gate-5 application (recommended by the evidence):** the
  regenerated notice can state applied identities and final contract
  outcomes; one routing act, no interim update needed. Matches the
  workplan's warning against stale "not yet accepted or applied" claims.
- **Route now, post-A3:** the notice must be regenerated to state
  approved-candidate (not applied) status and would need a second routed
  update after Gate 5. Earlier Root visibility; doubled routing surface.
- **Split:** a minimal coordination ping to Root now (via HELP_HUMAN
  reporting, no notice routing) with the formal notice after Gate 5 —
  Root's loop is already aware of SCA-APP-008 through the shared owner.

In every alternative the destination is a Root `_Coordination` surface, the
notice remains coordination rather than Root authority, and Root adopts,
amends, or declines under its own instruments. Routing requires a verbatim
owner instruction naming the moment, destination, and exact bytes
(workplan item 6); none exists yet.

## Suggested sequencing (evidence view, not a ruling)

1. Owner selects the C-01 canonical identity (or HOLD).
2. Owner disposes K-CONTROL-1 (sequence / specialize / revise) and confirms
   K-ROLE-2 as specialization.
3. App loop regenerates the resolved contract candidates and the rebuilt
   companion-register post-image; fresh Root/App review.
4. Owner approves the resolved exact identities; single Gate-5 act applies
   both groups; pointer moves under the Gate-4 plan.
5. Owner authorizes the regenerated notice routing after Gate 5.
