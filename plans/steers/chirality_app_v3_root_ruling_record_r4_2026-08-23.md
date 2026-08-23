# ROOT RULING RECORD R4 — SCA-004 Gate-5 append approval, Gate-5 execution authorization, pointer deferral — owner ruling of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: SCA-004 Gate 5 (application). Target workspace: Root governance loop (transcribed into Receipt 118). Supersedes nothing; the loop's instruments govern. Companion to `plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md`.


Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat, after
PR #628 merged as `4fbbb57999f1acf390fc2218a78b1a30249fd600` (Root Phase 0d).
HELP_HUMAN had byte-verified the published package on `main` before the
slate: applying `Gate_5_Application_Append.diff` to the R3-A-approved
`Gate_3_Candidate/` files with `git apply --unidiff-zero` reproduces all seven
`Gate_5_Applied_Candidate/` files byte-for-byte; deliverable count, per-package
distribution, deliverable-ID set, and the row counts of every companion and
trace file are identical before and after the append; `validate_gate5_package.py`
returned PASS 64/64 with `Gate_5_Validation.json` byte-identical. "[click]"
marks the option the owner selected.

R4-A — SCA-004 Gate-5 application append: [click] "Approve as published".
  Subject bytes, all under `execution/_ScopeChange/SCA-004_2026-08-22_1749/`:
    `Gate_5_Application_Append.diff`
      `336405845dde5a3ae406b46c750c38a88c1b366f69bdaa74b4078679e04fe6a8`
    `Gate_5_Slot_Inventory.md`
      `79929dfd8a299904d95fa0ab83b7b044452528ecf6e39bc57717675e39928e22`
    `Gate_5_Applied_Preview.md`
      `eb4a9236e7b6d007ebf11aff75bc3e86884d7158d7b753933b3130d523423d03`
    `Gate_5_Validation.json`
      `4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`
      (PASS, 64 checks, 0 failures)
  Resulting applied identities (`Gate_5_Applied_Candidate/`), which Gate 5 must
  produce exactly at the live paths under `execution/_Decomposition/`:
    `Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
      `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986`
    `chirality_root_deliverable_register_v1_0.csv`
      `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`
    `chirality_root_scope_ledger_v1_0.csv`
      `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417`
    `chirality_root_objective_register_v1_0.csv`
      `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f`
    `chirality_root_prd_coverage_forward_v1_0.csv`
      `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f`
    `chirality_root_trace_reverse_v1_0.csv`
      `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438`
    `chirality_root_coverage_telemetry_v1_0.md`
      `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c`
  Recorded form: the owner approves the append as published — all eighteen
  hunks, being the status, revision, run, and amendment slots of the working
  surface and telemetry, and the two inventoried scope-ledger `Notes` cells
  (SL-001 `SOW-083`, SL-002 `SOW-103`). The owner was told, and approves with
  knowledge, that those two cells carry wording inherited from revision 1.0
  through 1.2 rather than SCA-004 candidate status, and that the append
  modernizes them to applied-revision wording. The append changes no row,
  mapping, count, ID, or trace. CONDITION R3-B-1 is satisfied by these bytes.

R4-B — SCA-004 Gate-5 execution: [click] "Authorize now".
  Subject bytes: `Gate_5_Brief.md`
  `7f0ab64a16d70c7b48c7f51ed4bbfc3bbd5569bed3fdd05343de1ffe2b7d01de`, read
  against `Decision_Log.md`
  `c0e45e18b06ee2f415552aee10c6053e5dd887649bb3dc5accf6411943a23375` and
  `Handoff_State.md`
  `86825f84d6c9e7c6b38efe98319b67fb000676f37027d0c89b666216c3ab1d12`
  (status `AWAITING_OWNER_GATE_5_APPEND_APPROVAL`).
  Recorded form: the owner authorizes the Root loop to execute the brief's
  exact sequence, steps 1–9, once: reverify the seven live revision-1.2 SHAs
  and the seven approved candidate SHAs; fresh `validate_gate5_package.py`
  PASS; copy the seven approved files to their live paths; apply the approved
  append; require exact equality with the R4-A applied identities; write
  `Gate_5_Application_Record.md` with every before/after SHA, the R4-A and
  R4-B references, the validator result, and the Git-effect slot `TBD`; run
  the closure-validation lane of `Propagation_Plan.md` §6 items 1–6 (applied
  hashes, applied-state Gate-3 equivalent, post-application scoped
  `AUDIT_DECOMP` backcheck against the Gate-1 baseline, no folder/SOW/status/
  dependency created, all ten holds `HELD_UNAVAILABLE`, derivative
  currentness); return the applied state for the owner's Gate-5 confirmation
  (§6 item 7). This authorization is for this exact package identity only; any
  SHA drift, validator failure, or out-of-scope write stops the act.
  Gate-5 confirmation remains a later owner act against the applied live
  bytes and the closure-lane evidence.

R4-C — `_LATEST.md` pointer: [click] "Rule after Gate-5 confirmation".
  Subject bytes: `Gate_5_Pointer_Candidate.md`
  `5918e7bff305bfc0a22c4a4fd172a2ad7bf013a217a778d6ca3797ce773dfabf`.
  Recorded form: the pointer is not written by the Gate-5 act. The candidate
  returns for its own ruling after the owner confirms the applied state
  (`Propagation_Plan.md` §7). `execution/_ScopeChange/_LATEST.md` remains
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` through
  Phase 0e.

Not ruled here: Gate-5 confirmation; pointer approval; any PREPARATION INIT
dispatch, SOW, dependency, estimate, schedule, graph, or audit-snapshot act
beyond the closure lane; the `AGENT_SCOPE_CHANGE.md` application-append
Task Management candidate (routed to triage); C1 (App Server 0.149.0
artifact download) remains not authorized; no pin change (G0 B4;
TM-ROOT-106/122 stay G1 blockers); no App-loop act.
