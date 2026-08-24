# ROOT LOOP STEER — K-CONTROL-1 design amendment — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: Root loop. The loop's instruments govern; this steer directs one bounded instruction-surface tranche under them. **Sequencing: initiate only after the in-flight Root v3 Phase 5 has merged** (A5-B). Companion instruments: ruling records A4 (SHA-256 `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`) and A5 (SHA-256 recorded in the PR that published this steer), the R7 record (SHA-256 `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53`).

## Basis gate (check before any write; stop and report if any line fails)

- The Root v3 Phase 5 PR has merged and its receipt (expected Receipt 125)
  is on `main`; record the actual merge SHA in the receipt.
- `docs/CONTRACT.md` SHA-256
  `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`
  (RATIFIED 2026-07-11; 40 invariants; K-CONTROL-1 defined in subsection
  1.13 at line 162). If the file has changed on `main`, stop and report —
  the pre-image below is bound to these bytes.
- The seven R7-accepted carrier SOWs at their Receipt-123 identities,
  including DEL-02-07
  `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5`.
- `execution/_Coordination/_TaskManagement/REGISTER.csv` byte-identity at
  open and close.

## Authority context

Owner rulings A4-B and A5-B (K-AUTH-1): Root's ratified K-CONTROL-1 row is
amended now as a **design amendment**, so that Root contract truth
describes the accepted two-socket design before any App application of the
App K-CONTROL-1 candidate. Grounding is the R7-A acceptance of the
DEL-02-07 scope contract (Process Supervisor and Purpose-Limited Control).
This tranche confers no implementation, activation, dispatch, App, pin,
hold, or release authority; the supervisor socket remains unimplemented
and its implementation remains separately gated on the WP-03 pathway.

## N1 — exact row amendment

Amend exactly one row of `docs/CONTRACT.md`: the **K-CONTROL-1**
definition row (line 162; subsection 1.13 Shared Runtime). Draft the exact
replacement text in the loop's own words, preserving all of the following
semantics:

1. The existing invariant stands: runtime control uses authenticated,
   project-scoped HTTP/1.1 over `{userData}/runtime/control.sock` beneath
   a `0700` directory with a `0600` socket; a TCP control listener is
   forbidden.
2. Add the accepted design: one additional private Unix-domain socket
   between the daemon and the Delegated-Harness Process Supervisor, never
   renderer- or CLI-callable, same `0700`/`0600` permission discipline,
   accepted by R7-A through the DEL-02-07 scope contract (cite the record
   SHA-256).
3. State honestly that the supervisor socket is **accepted design, not
   yet implemented**: exactly one control socket is live today, and the
   second socket becomes live only through the separately gated DEL-02-07
   implementation pathway; the row must not read as a claim of current
   two-socket operation.
4. No third socket and no TCP listener under any configuration.
5. Update the row's verification column to add supervisor-socket tests as
   design-gated (activating with DEL-02-07 implementation), keeping the
   existing socket-mode, authorization, stale-owner, and listener tests.

No other row, the K-* index, the invariant count (40 — no ID is added or
retired), the enforcement-map summary membership, or any other section may
change, except: if the document's own conventions require a dated
amendment note, add the minimal note the conventions require and no more.

## Write set, exactly

- `docs/CONTRACT.md` — the one row (plus any convention-required minimal
  amendment note).
- One new live manifest
  `docs/governance_harness/tranche_manifests/ROOT-CONTRACT-KCONTROL1-DESIGN-2026-08-<DD>.yaml`
  (schema v1; basis = current `main`; instruction-surface paths =
  `docs/CONTRACT.md` plus the manifest itself; `m2_gate` human-gated-pr,
  `self_merge: false`, authorization = this steer's N1 section verbatim;
  `m6_notice: pending`, `routed_to: []`).
- Run/control evidence under
  `execution/_Coordination/AgentRuns/ROOT_KCONTROL1_DESIGN_2026-08-<DD>/`.
- One append to `execution/_Coordination/LOOP_RECEIPTS.md` (the next
  sequential receipt — expected 126 after Phase 5's 125; incorporate this
  steer and records A4/A5 by immutable path and SHA-256).
- One dated append to `execution/_Coordination/HANDOFF_STATE.md`.

Not selectable: every other row and section of `docs/CONTRACT.md`; any
other `docs/**` file; `agents/**`, `tools/**`, `AGENTS.md`, `exports/**`;
any deliverable folder, register, pointer, or harness pin; any
`projects/**` path.

## Discipline

- The owner's merge of the PR is the ratification act for the amended row
  (the same K-AUTH-1 form as the 2026-07-11 ratification); the PR must
  present the exact pre-image and post-image row bytes with SHA-256 of the
  full file before and after.
- Run before pushing: candidate whitespace, agent instructions,
  instruction entrypoints, CI-form G4 (`--base origin/main --head HEAD
  --added-manifests-only`, PASS with the new manifest covering
  `docs/CONTRACT.md`), taskmgmt validate, the focused practitioner-harness
  pair (56 green, no repin), and `git diff --check`.
- Branch `codex/root-kcontrol1-design-2026-08-<DD>`. Do not merge. If
  `main` advances, request sync authorization from the owner and record
  the grant verbatim in the receipt. HELP_HUMAN byte-verifies before
  endorsement, including that no byte outside the declared row and note
  changed.
