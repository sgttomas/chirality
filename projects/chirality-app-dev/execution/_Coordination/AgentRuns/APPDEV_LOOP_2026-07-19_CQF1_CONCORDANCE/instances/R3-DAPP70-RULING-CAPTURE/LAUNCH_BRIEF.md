# R3-DAPP70-RULING-CAPTURE Launch Brief

- **Role:** RECONCILIATION (Agent 1; load and obey
  `agents/AGENT_RECONCILIATION.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Instance:** `R3-DAPP70-RULING-CAPTURE`
- **Live basis:** `9783e9ac6108dfd8738f0815fe8271af464dcaf1`
- **Decision:** D-APP-70
- **Owner text:** `APPROVE: D-APP-70 Option A`
- **Owner-text SHA-256:**
  `2cadfff68d2aafc381cd82178d635a706587d07f1dfd6b9888b6c547754f1014`
- **Scope:** owner-act transcription and next-gate handoff only
- **Mapping application / W1 / Git authority:** none

## Objective

Faithfully transcribe the exact owner act into a separate D-APP-70 ruling
record, transition the existing register row to `RULED (Option A)`, append
Receipt-79, and produce an exact next-gate analysis and handoff. Preserve the
packet's 22-path/nine-group boundaries and every prohibition. Do not perform
mapping application or repair.

## Mandatory preflight

Before any write:

1. require clean branch `codex/app-dev-dapp70-option-a-20260720` with
   `HEAD == origin/main == 9783e9ac6108dfd8738f0815fe8271af464dcaf1`;
2. hash the exact UTF-8 owner text without a trailing newline and require
   `2cadfff68d2aafc381cd82178d635a706587d07f1dfd6b9888b6c547754f1014`;
3. require the D-APP-70 packet hash
   `94b01c68e0611c6f2b0a13f6e1087830876d62aab4bfcda2c386aceb721f4b16`,
   exact Option-A response syntax, status `AWAITING_RULING`, and no existing
   ruling record;
4. require the register hash
   `c6f8722cbb792785ddd1ec7f918c8613238b28a26340eec6b8c45871b4c31f32`,
   exactly one D-APP-70 row at `AWAITING_RULING`, and no other open D-APP row;
5. require Receipt-78 is unique/latest and receipt-ledger hash
   `d8c4032519453d3e7e6c9778c08b0af0547b5b19f6c632660ab42cfc8c7ca0c7`;
6. bind R2 handoff/return/status to
   `2bbbed251da9e1ef6889e9665bca5473e8d0994261bf33f03160d7ba4003fb22`,
   `686e2432bdaefe210481e6df242408c5e281952b3ae4a25f6fb48a81e5d803de`,
   and `330f051d32f7a06fc7a81c2e82ebe21b3acbc4769c39f90baa5fc5ff88e9d12b`;
7. bind V1 return/status and both child returns to the hashes in released
   `STATUS.json`; require terminal `ACCEPT`, no blockers/unknowns/waivers;
8. recompute the complete 14-file activated-package hash map from released
   `STATUS.json`, 22 unique/current source paths, ordered manifest hash
   `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`,
   22 proposal rows, nine groups `5+4+6+1+1+1+1+1+2`, and the five exact
   Remaining-container hashes; and
9. run the receipt validator and authority-corpus status check, then record a
   before-write containment inventory.

Fail closed with no partial shared-file write on any mismatch.

## Ruling record requirements

Create
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-70_RULING_2026-07-20.md`.
It must:

- identify D-APP-70 and the exact packet/hash;
- quote the owner text verbatim and record its canonical SHA-256;
- attribute the ruling only to the owner, never to an agent;
- state `Option A — recommendations 1–9 exactly as stated`;
- enumerate all nine recommendation outcomes and bind all 22 paths without
  paraphrasing away retained boundaries;
- distinguish owner selection from later mapping application;
- state that recommendation 6 accepts only the shared preload implementation
  boundary and leaves the physical integration lead unnamed;
- explicitly preserve DEL-02-03 `selectDirectory`, DEL-02-05 `apiKey`, and
  DEL-09-06 `safeStorage`/security interests;
- state that preload repair/path-level application requires a later owner
  choice of physical lead; and
- restate that mapping application, subject/package repair, W1, lifecycle,
  release, issuance, publication, hard-fence crossing, and Git action remain
  separately gated and are not authorized by this capture.

Do not edit the proposal packet.

## Register, receipt, analysis, and handoff

1. Update exactly the existing D-APP-70 register row: status becomes
   `RULED (Option A)` and the ruling-record column points to the new record.
   Preserve the packet path and affected-scope clause, adding only concise
   ruling disposition text that records recommendation 6's unnamed lead and
   the separately gated effects. No row append, reordering, or unrelated edit.
2. Append exactly Receipt-79 with parent Receipt-78, Examined-Through
   `9783e9ac6108dfd8738f0815fe8271af464dcaf1`, verbatim owner direction and
   canonical hash, exact ruling/packet/V1/R2/package pointers, checks, no stale
   map unless actually observed, RECONCILIATION attribution, and gate outcome
   `RULED_CAPTURED_AWAITING_SEPARATE_APPLICATION_GATES`.
3. Write `NEXT_GATE_ANALYSIS.md` distinguishing:
   - procedural later W1 application for recommendations 1–5 and 7–9 plus
     recommendation 6's already-selected shared-boundary annotation, after
     ruling capture is on shared main; from
   - owner-class selection of recommendation 6's physical preload lead.
   Route later preparation of a decision-ready D-APP-71 proposal packet with
   DEL-02-03, DEL-02-05, DEL-09-06, and deferral options. Do not create or
   register that packet here and do not recommend by silently selecting a lead.
4. Write `HANDOFF.md`, `RETURN.md`, and terminal `STATUS.json`, binding every
   output hash and declaring mapping application false, mappings not yet
   applied, preload lead absent, W1 false, lifecycle/release/hard-fence/Git
   false.

Return exactly `RULED_CAPTURED | BLOCK`.

## Write authorization and prohibitions

Write only the new ruling record, the existing D-APP-70 register row,
append-only Receipt-79, and this instance's four terminal/control outputs.
Do not edit the proposal packet, activated derivative, any of 22 source paths,
five Remaining containers, SOW/dependencies, prior R1/V1/R2/evaluation
records, plan/graph, authority, lifecycle, W1 reservation, or Git state. Do
not create D-APP-71 or another packet. Do not delegate. Waivers: none.
