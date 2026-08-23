# A2 fresh review — repaired SCA-004 Gate 2

Verdict: `NOT_READY_FOR_GATE_2_OWNER_REVIEW`

The repaired candidate now satisfies the structural Gate-2 requirements, the
verbatim R1-C record, the ten-binding preservation check, the protected-byte
checks, and the Gate-3 stop. Two residual omissions prevent a clean finding
that the **full** G0 A3/A4/A7 semantics are carried.

## Blocking findings

1. **G0 A3 hard-containment continuity is omitted.**
   `execution/_ScopeChange/SCA-004_2026-08-22_1749/Impact_Assessment.md:66`
   correctly carries always-offered Agent 0/1/2 entry, labelled Agent 2/TASK
   fallback, `instruction-asserted` governed evidence, and the
   instruction+config versus mechanism-proof calibration. It does not carry
   the final controlling A3 clause that hard filesystem/network/process
   containment is unchanged
   (`plans/steers/chirality_app_v3_g0_record_2026-08-22.md:37-40`). Add that
   clause to the A3 disposition.

2. **G0 A7's exact grouping/proof obligation is abbreviated away.**
   `execution/_ScopeChange/SCA-004_2026-08-22_1749/Impact_Assessment.md:68`
   says only `destination-grouping caveat` and later names G-APPR generically
   at line 193. It does not state that a grant may unblock queued requests to
   the same destination, nor that G-APPR must prove prompt delivery and observe
   grouping empirically at the exact pin
   (`plans/steers/chirality_app_v3_g0_record_2026-08-22.md:69-78`). Add both
   obligations to the A7 disposition. The three per-root postures, host/protocol
   display, explicit `acceptForSession`, labelled `network_access = true`, and
   separate OpenAI service-endpoint enumeration are already present.

## Passed checks

- `Decision_Log.md:15-16` contains `G1-ACCEPTED` and
  `PENDING_OWNER_ACCEPTANCE`; its lines 26-39 are byte-identical to R1-C lines
  49-62, including all three subject SHA-256 identities.
- `Impact_Assessment.md:49-58` has exactly eight action rows: one `MODIFY`, six
  PKG-02 `ADD`s, and one PKG-04 `ADD`; every row covers decomposition
  structure, variant-local metadata, downstream consumers/workflows, and
  invariant/telemetry risk.
- Separate derivative-package and derivative-surface tables exist at lines
  98-109 and 111-132.
- Orphan/mapping risk, estimate/schedule staleness, active snapshot/handoff
  impact, and workflow-owned reruns are explicit at lines 134-194.
- G0 A4 is complete at lines 56 and 67: retirement/crash terminalization,
  conditional `thread/resume` under canonical-root/account/policy-digest
  continuity with canonical cwd, fresh-thread fallback, and no in-flight
  re-attach.
- `Impact_Assessment.md:81-92` reproduces exactly the ten accepted binding
  paths, each still `HELD_UNAVAILABLE`, matching
  `DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md:49-58`.
- `Handoff_State.md` uses the four-state form, records D-GOV-35 as `RULED` with
  its application executing in sibling N1, stops at
  `AWAITING_OWNER_GATE_2_ACCEPTANCE`, sets `ReadyForNextPhase=NO`, and keeps
  Gate 3 closed.
- Protected hashes pass and match `origin/main` byte-for-byte:
  - `Brief.md` — `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126`
  - `Gate_1_Validation.md` — `812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14`
  - `Parsed_Actions.csv` — `a89b77dc1ce478f7ea5bbc3ebb12706d69e93876e6a7f4cca0cfd5ea5a9e738b`
  - `WORK_GRAPH.json` — `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9`
  - `DAG.md` — `fc805333b84ed647605241aacd63fd2731890886385439587f1109140e045450`
  - `_LATEST.md` — `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`
- Because `WORK_GRAPH.json` is unchanged, no AUDIT_DEP_CLOSURE rerun is
  required.
- The visible N2 candidate diff is limited to `Decision_Log.md`,
  `Impact_Assessment.md`, and `Handoff_State.md`; N2 run evidence remains
  inside its instance folder. No decomposition, Task Management register,
  `_STATUS.md`, pointer, runtime, tools, or foreign-loop byte is an N2 write.

## Required next act

Repair the two clauses in `Impact_Assessment.md`, then dispatch a fresh
non-delegating review. Do not open Gate 3.
