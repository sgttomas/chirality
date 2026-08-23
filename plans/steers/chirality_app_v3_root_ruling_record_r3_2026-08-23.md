# ROOT RULING RECORD R3 — SCA-004 Gate 3 and Gate 4 approvals — owner ruling of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: SCA-004 Gate 3 (exact amendment) and Gate 4 (propagation plan). Target workspace: Root governance loop (transcribed into Receipt 117). Supersedes nothing; the loop's instruments govern. Companion to `plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md`.


Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat, after
PR #626 merged as `b32ceb130351c1dc3a8dbbcbf9311a4a73dc350e` (Root Phase 0c).
HELP_HUMAN had byte-verified the Gate-3 candidate on `main` before the slate:
its own rerun of `validate_gate3_candidate.py` returned PASS 98/98 with a
byte-identical `Gate_3_Validation.json`; `Gate_3_Exact_Amendment.diff`
applied to the live revision-1.2 files with `git apply --unidiff-zero`
reproduces all seven `Gate_3_Candidate/` files byte-for-byte; topology
46→53, PKG-02 6→12, PKG-04 10→11. "[click]" marks the option the owner
selected.

R3-A — SCA-004 Gate 3 (exact amendment): [click] "Approve exact bytes".
  Subject bytes: the seven files under
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/`:
    `Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
      `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641`
    `chirality_root_deliverable_register_v1_0.csv`
      `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`
    `chirality_root_scope_ledger_v1_0.csv`
      `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc`
    `chirality_root_objective_register_v1_0.csv`
      `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f`
    `chirality_root_prd_coverage_forward_v1_0.csv`
      `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f`
    `chirality_root_trace_reverse_v1_0.csv`
      `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438`
    `chirality_root_coverage_telemetry_v1_0.md`
      `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765`
  together with `Gate_3_Exact_Amendment.diff` SHA-256
  `0724668f6fb85189f4c3ee142a21cef938c8dd47373be543d8b108c8e934637b`,
  `Gate_3_Validation.json` SHA-256
  `dc5fe4355322a96b7da61606fff7d8dd51943a7d606f132966705bfb70b9f129`
  (PASS, 98 checks, 0 failures), and `Amendment_Preview.md` SHA-256
  `ff7743554270aee177feed4226a4fa35fd503ce34760f69644176878bcffdca4`
  (status `awaiting_gate_3_approval`), over accepted basis revision 1.2
  working surface SHA-256
  `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`.
  Recorded form: the owner approves these exact bytes as the SCA-004
  revision-1.3 amendment — the eight R1-C actions (MODIFY DEL-02-06; ADD
  DEL-02-07..DEL-02-12; ADD DEL-04-11), DEC-025, the exact scope-ledger and
  objective-register allocations, and the recomputed forward trace, reverse
  trace, and telemetry. The owner was told, and approves with knowledge,
  that the reverse-trace recompute also corrects four inherited objective
  omissions (DEL-01-04, DEL-03-01, DEL-03-06, DEL-06-04) beyond the eight
  actions. Approval is of bytes, not application: no file under
  `execution/_Decomposition/`, no `_LATEST.md`, no folder, `_STATUS.md`,
  SOW, lifecycle, dependency, estimate, schedule, tool, runtime, or App
  surface changes by this ruling; Gate 5 is not executed; all ten DEL-02-06
  bindings remain `HELD_UNAVAILABLE`.

R3-B — SCA-004 Gate 4 (propagation plan): [click] "Approve with Gate-5
  header condition".
  Subject bytes: `Propagation_Plan.md` SHA-256
  `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`
  (status `awaiting_gate_4_approval`) and `Amendment_Actions.csv` SHA-256
  `4e623bcc5e69d056f71d9ed860ff729a0dfc9b8d8c635e7dd23b3c6b10d2871d`
  (eight ordered actions, `SupersessionBindingPresent=NO`), read against
  `Decision_Log.md` SHA-256
  `a35f2e13a70561b207092ff46d409525a2b7d4ebd14f3b938d06f253da5e4aec` and
  `Handoff_State.md` SHA-256
  `41cadc01f17642d8f8318bc18f60c39adecac40253351f5ac97ca85888178cfd`.
  Recorded form: the owner approves the propagation plan as written —
  Gate-5 exact copy of the seven approved surfaces, the seven PREPARATION
  INIT briefs as later PROJECT_SETUP/PREPARATION acts, the DEL-02-06
  `_CONTEXT.md` edit list, the dependency/estimate/schedule advisories, the
  graph and audit reruns, the closure-validation lane, the `_LATEST.md`
  pointer exclusion, and the rollback/stop rules — subject to one condition:
  CONDITION R3-B-1 (Gate-5 application append). Plan §1's "exact copy only;
  must not edit candidate contents" would leave the applied live working
  surface and telemetry describing themselves as a Gate-3 candidate that is
  "not approved or applied". Before any Gate-5 application, the Gate-5 brief
  must include an exact application append in the SCA-002 form — a
  zero-context patch over the approved candidate bytes, limited to the
  status, revision, run/amendment, and candidate-status slots across the
  seven files — together with the resulting per-file SHA-256 values, drafted
  as bytes and returned to the owner for approval before application. The
  append changes no row, mapping, count, or trace.
  Gate 5 is not authorized by this ruling; Gate-5 execution returns as a
  separate owner act after the append bytes are approved.

Not ruled here: Gate-5 execution authorization; the `_LATEST.md` pointer
treatment (its own accepted authority, plan §7); any PREPARATION INIT
dispatch; C1 (App Server 0.149.0 artifact download) remains not
authorized; no pin change (G0 B4; TM-ROOT-106/122 stay G1 blockers); no
App-loop act — SCA-APP-008 reciprocates under App authority.
