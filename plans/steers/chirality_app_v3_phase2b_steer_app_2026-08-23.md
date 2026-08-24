# APP-DEV LOOP STEER — v3 Phase 2b: K-CONTROL-1 regeneration against the ratified Root row and K-EVENT-4 re-pin — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: App-dev loop (`projects/chirality-app-dev/`). The loop's instruments govern; this steer directs one bounded phase under them. Companion instruments: ruling record A6 (SHA-256 recorded in the PR that published this steer — the files merged together), records A4 (SHA-256 `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`) and A5 (SHA-256 `1896d89200c4cd390b4606aed0229fe03bf7c5070f454e1dca5d6c6acde2bb9b`), and the Phase-2 steer (SHA-256 `5cd8e4ac4b6d77a2672f70218e27e18bfd3ac7cf5d1ddc57af608991260d9a5e`).

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge `a252502af5180290a0a50a128b414d5a3bd27bb5`
  (PR #657, the owner's ratification merge of Root's K-CONTROL-1 design
  amendment) and merge `699b3eae0829c8306dee9bcd2035ecb6dcf11260` (PR #656,
  the Phase-2 return, Receipt 197).
- Ratified Root contract `docs/CONTRACT.md` SHA-256
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`
  (differs from the prior pin
  `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679` at
  exactly line 162, the K-CONTROL-1 row; K-RUNTIME-1 line 161 and K-STORE-2
  line 164 are byte-identical to the prior pin).
- The other four A4-A Root source blobs unchanged:
  `runtime/packages/cli/src/config.ts`
  `40cec2df6c21fa10a5a053ff6e40ea0b6d9d4a352208660cc01eb22f5fc7523e`;
  `runtime/packages/core/src/session-store.ts`
  `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad`;
  `runtime/packages/contracts/src/events.ts`
  `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd`;
  `runtime/packages/contracts/src/session.ts`
  `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51`.
- The Phase-2 candidates at their Receipt-197 identities: K-EVENT-4
  transaction artifact
  `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`;
  companion-register candidate
  `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079`;
  Phase-2 handoff
  `119ac0b0af6ceae27eaebb04034c0ce3441756b23f470efc2a4fd1b7bee2343f`.
- Gate-3 `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`;
  Gate-4 `47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6`;
  concordance workplan
  `c747a81b7fcca88dfebab8e2ed2345247af23063d9f48e3dd2e4bfa0a5af4185`;
  the eleven frozen A2 assessment identities.
- App contract `projects/chirality-app-dev/docs/CONTRACT.md` SHA-256
  `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`;
  live companion register SHA-256
  `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`;
  `_LATEST.md` SHA-256
  `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`;
  App TM register SHA-256
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`
  (13 rows; byte-identity at close as well); frontend tree object
  `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.

## Authority context

A6-A authorizes this phase per step 6 of the approved concordance workplan.
A6-B directs the K-EVENT-4 re-pin as a re-grounding only. A4-A's selected
identity, A4-C's K-ROLE-2 confirmation, A5-C's single Gate-5, and the
Phase-2 candidates' review lineage all stand. This phase regenerates
candidates and evidence only. Nothing here applies a contract row, moves
the pointer, changes the register as truth, routes the notice, or claims
Gate-5 eligibility beyond the stated condition.

## N1 — regenerated K-CONTROL-1 (C-01) candidate

Produce the exact regenerated K-CONTROL-1 contract-row candidate replacing
the Gate-3 C-01 post-image, in the loop's own words, preserving all of:

1. Alignment with the ratified Root row (cite Root `docs/CONTRACT.md`
   `ad0a4e6a…` line 162): the two-socket topology is ratified accepted
   design; exactly one control socket is live today; the private
   daemon-to-Delegated-Harness-Process-Supervisor socket is never renderer-
   or CLI-callable and becomes live only through the separately gated
   DEL-02-07/WP-03 implementation pathway. No present-tense claim of
   two-socket operation.
2. Root-consistent ownership wording: the Root daemon exclusively owns the
   `{userData}/runtime` control surfaces per Root K-RUNTIME-1; no
   "app-owned" claim over runtime directories; the App is never a second
   owner or writer of runtime control state.
3. The Phase-1 candidate's App-side enforcement strengthenings retained:
   `0700` parent / `0600` socket, verified same-UID path ownership,
   owner/generation records, rotated high-entropy bearer tokens delivered
   only through app-private state, fail-closed on stale or mismatched
   identity, explicit stale-socket recovery, and the honest
   no-peer-credential disclaimer.
4. No third socket and no TCP control listener under any configuration.
5. Verification column: keep the live single-socket tests; make the
   supervisor-socket and two-listener-inventory tests design-gated,
   activating with DEL-02-07 implementation.

Carry the full transaction form: pre-image = the live App K-CONTROL-1 row
with SHA-256 and line cite; exact post-image bytes including the
terminating LF; post-image row SHA-256.

## N2 — re-pinned K-EVENT-4 candidate

Regenerate the K-EVENT-4 transaction artifact changing only its Root
grounding: bind Root `docs/CONTRACT.md` at the ratified identity
`ad0a4e6a…`, noting that K-RUNTIME-1 and K-STORE-2 are byte-identical to
the A4-A basis; the other four blob pins are unchanged. The resolved
K-EVENT-4 row post-image bytes must remain byte-identical to the Phase-2
resolved row, SHA-256
`92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`
(A6-B: a re-grounding, not a semantic change). Stop and report if
preserving the row would require any byte change.

## N3 — resolved contract and companion-register rebuild

Recompute the resolved full App-contract candidate by applying the Gate-3
transactions to the live pre-image with the regenerated C-01 post-image
(N1) and the resolved C-06 post-image (N2) substituted; record the new
full-file SHA-256 and byte count (this identity supersedes
`a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`).
Rebuild the full companion-register post-image candidate against that
identity: K-CONTROL-1 now recorded as design-mapped against the ratified
Root row (external Root authority; cite `ad0a4e6a…`; coverage claims
limited to the design-gated posture — no implementation-coverage claim),
every row re-bound to the new resolved contract identity, and the
83-ID/50-family accounting preserved with no stale coverage claim. This
register candidate supersedes `f2d2e904…`.

## N4 — review and return

Fresh independent review of all candidates against: the ratified Root row
bytes; the A4-A selected identity at its re-pinned sources; the approved
Gate-3 package (C-01 and C-06 as regenerated); the Gate-4 plan; and the
sequencing rules — Root ratification is now satisfied, so Gate-5
eligibility for the contract group requires exactly the owner's approval
of these regenerated candidates (A5-C: one Gate-5 act for both groups).
Unlimited repair with fresh re-review; every repair disclosed. Close
`AWAITING_OWNER_APPROVAL` with a four-state handoff naming every candidate
identity.

## Write set, exactly

- New files strictly inside
  `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/`
  (additions only; every existing file in the snapshot, including the
  Phase-2 candidates, is immutable — the regenerated candidates are new
  files, e.g. under a `Phase2b/` subfolder per house convention).
- Run/control evidence under
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE2B_2026-08-<DD>/`.
- One append to `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`
  (Receipt 198; parent Receipt-197; incorporate this steer and record A6 by
  immutable path and SHA-256).

Not selectable: `projects/chirality-app-dev/docs/CONTRACT.md`; the live
companion register; `_LATEST.md`; any register, SOW, `_STATUS.md`,
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
- Branch `codex/app-v3-phase2b-2026-08-<DD>`. Do not merge. If `main`
  advances, a routine non-rewriting sync merge is covered by the owner's
  standing authorization recorded verbatim in Receipt 197; record each
  sync, its incoming content, and that authority citation in Receipt 198.
  HELP_HUMAN byte-verifies before endorsement.
