# ROOT RULING RECORD R5 — SCA-004 Gate-5 second attempt: method correction and re-authorization — owner ruling of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: SCA-004 Gate 5 (application), second attempt. Target workspace: Root governance loop (transcribed into Receipt 119). Supersedes nothing; the loop's instruments govern. Companion to `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`.


Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat, after
PR #630 merged as `3bb3d50550b9fbdbdea67f41fa2ed108024cb43b` (Root Phase 0e,
recovered Gate-5 stop; Receipt 118). HELP_HUMAN had byte-verified the stop
record and rehearsed the corrected method on `main` before the slate. "[click]"
marks the option the owner selected.

Facts of record (from the Phase-0e return, verified by HELP_HUMAN):
  The one R4-B attempt materialized the seven Gate-3 candidate surfaces by
  re-expressing the approved zero-context diff as patch-edit hunks rather than
  by byte copy; five of seven intermediate identities missed R3-A; the stop
  rule fired before the append was checked or applied; all seven live files
  were restored and byte-verified at revision 1.2; no SCA record was written.
  The approved package is unchanged and undrifted.
  HELP_HUMAN's scratch rehearsal of the corrected method on the `main` tree:
  `/bin/cp` of the seven `Gate_3_Candidate/` files to their live paths
  reproduced all seven R3-A identities; `git apply --unidiff-zero --check`
  then `git apply --unidiff-zero` of `Gate_5_Application_Append.diff`
  reproduced all seven R4-A applied identities. The same rehearsal showed
  that `validate_gate5_package.py` is a pre-application validator (it asserts
  `live_basis_untouched` and `candidate_ids_absent_from_live_register`) and
  returns 13 failures by design once the live files are the applied state; a
  post-application validator is therefore required before the closure lane
  can pass.

R5-A — Gate-5 second attempt: [click] "One tranche: rehearse, then execute".
  Recorded form: the owner authorizes one further Gate-5 execution attempt,
  in one tranche, under these conditions:
  (1) Materialization method, mandatory: byte copy of the seven exact
      `Gate_3_Candidate/` files to their live paths by shell copy
      (`/bin/cp`) or by `git show <basis>:<candidate path>` redirected to the
      live path; then `git apply --unidiff-zero --check` and one
      `git apply --unidiff-zero` of `Gate_5_Application_Append.diff` from the
      repository root. Patch editing, editor tools, `apply_patch`, or any
      re-expression of the approved diffs is forbidden for these writes.
  (2) Post-application validator: before the live act, the loop adds
      `validate_gate5_applied.py` to the SCA-004 snapshot — deterministic,
      reproducible — asserting that the seven live files equal the R4-A
      applied identities byte-for-byte, the structural Gate-3 checks hold on
      the applied state (53 deliverables; PKG-02 12; PKG-04 11; packages 6;
      scope items 104; objectives 7; ID set, mappings, and 85/59 trace rows
      identical to `Gate_5_Applied_Candidate/`), all approved package bytes
      are unchanged, `_LATEST.md` is unchanged, and no folder, SOW,
      `_STATUS.md`, or `_DEPENDENCIES.md` was created.
  (3) Rehearsal gate: before the live act, the full sequence — copy, hash,
      apply-check, apply, hash, `validate_gate5_applied.py` — is executed in
      a scratch worktree outside the governed checkout and recorded in
      `Gate_5_Rehearsal_Record.md` with every observed hash. The live act
      proceeds only if the rehearsal's intermediate identities equal R3-A,
      its final identities equal R4-A, and the applied validator passes with
      zero failures. Otherwise the tranche stops at the rehearsal with no
      live write and returns the blocker.
  (4) The live act is executed once, exactly as R4-B's sequence with the
      method of (1) and the validator of (2) substituted for the brief's
      step 8 "applied-state equivalent"; a live identity mismatch restores
      revision 1.2 bytes and stops; a closure-lane failure is recorded and
      returned, not silently reverted.
  R4-A (append bytes and applied identities) and R4-C (pointer deferred)
  stand unchanged. Gate-5 confirmation remains a later owner act against the
  applied live bytes and the closure-lane evidence.

Not ruled here: Gate-5 confirmation; pointer approval; any PREPARATION INIT
dispatch, SOW, dependency, estimate, schedule, graph, or audit-snapshot act
beyond the closure lane; a Task Management candidate that sealed briefs for
exact-byte materialization must name the byte-level method and forbid
patch-edit re-expression (routed to triage); C1 (App Server 0.149.0
artifact download) remains not authorized; no pin change (G0 B4;
TM-ROOT-106/122 stay G1 blockers); no App-loop act.
