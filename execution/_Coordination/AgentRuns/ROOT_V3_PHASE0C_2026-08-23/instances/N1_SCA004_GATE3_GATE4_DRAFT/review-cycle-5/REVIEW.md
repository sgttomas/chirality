# Fresh Review — N1 SCA-004 Gate 3 / Gate 4 drafts, cycle 5

Verdict: `FAIL — TWO ACTIONABLE FINDINGS`

Review basis: `origin/main@8635e40995b05f494ae35c6083dabdd50068bb52`

Review posture: fresh independent, read-only, non-delegating Agent-2 review.
No N1 output was repaired or modified.

This review does not approve Gate 3, approve Gate 4, open Gate 5, amend live
decomposition truth, materialize a deliverable, lift a hold, or confer
implementation, pointer, App-loop, publication, release, commit, push, or
merge authority.

## Actionable findings

### N1-R5-F1 — HIGH — DEL-02-07 omits the accepted socket-token control from the exact carrier bytes

The owner-accepted Gate-2 assessment makes the process-supervisor carrier's
security boundary exact. `Impact_Assessment.md:52` requires the later exact
bytes to retain one daemon as runtime broker, Unix-only `0700`/`0600`
controls, **token/owner/generation/stale-recovery rules**, and no TCP
listener.

The candidate DEL-02-07 row at
`Gate_3_Candidate/chirality_root_deliverable_register_v1_0.csv:16` carries
the daemon, Unix socket, ownership modes, generation fencing, stale recovery,
and no-TCP boundary, but neither its description, anticipated artifacts, nor
Context Envelope notes names any socket token/authentication-token rule. A
generic `purpose-limited Unix-socket protocol` does not preserve the accepted
token requirement in exact decomposition bytes. The builder has the same
omission at `build_gate3_candidate.py:48-53`.

The 95-check validator does not assert the Gate-2 token control, so its PASS
does not close this gap.

Bounded repair: add the explicit token rule to the deterministic DEL-02-07
carrier description/artifact set without weakening the existing owner,
generation, stale-recovery, permission, sole-broker, non-renderer/CLI, and
no-TCP controls. Add a semantic validator assertion for the complete accepted
socket-control set, then regenerate the candidate register, exact diff,
validation JSON/check count, preview/evidence identities, handoff, and
instance return. No live decomposition or implementation write is needed.

### N1-R5-F2 — HIGH — DEL-02-10 does not preserve the exact closed-union terminal event identifiers

The accepted Gate-2 assessment at `Impact_Assessment.md:55` requires the
closed HarnessEvent v2 union to retain these four exact terminal event names:
`turn.completed`, `turn.failed`, `turn.interrupted`, and `turn.cancelled`.

The candidate DEL-02-10 row at
`Gate_3_Candidate/chirality_root_deliverable_register_v1_0.csv:19` says only
`completed failed interrupted and cancelled terminals`. None of the seven
candidate surfaces contains any of the four exact `turn.*` identifiers. For
an `API_CONTRACT` carrier, removing the event namespace leaves the exact wire
union underspecified and does not satisfy the accepted exact-byte
requirement. The builder repeats the shortened form at
`build_gate3_candidate.py:90-95`.

The 95-check validator does not assert either the closed-union statement or
the four accepted event identifiers.

Bounded repair: put all four exact `turn.*` terminal identifiers into the
deterministic DEL-02-10 description or anticipated-artifact contract and add
a validator assertion that the set is exact and closed. Preserve attributed
approvals, unknown-payload reject/project/redact behavior, A3/A7 carriage,
and the no-provider-shaped-persistence boundary. Regenerate the candidate
register, exact diff, validation JSON/check count, preview/evidence
identities, handoff, and instance return. No live API or runtime write is
authorized.

## Prior-cycle findings — closure check

- `N1-R1-F1` remains closed. A fresh all-row derivation found exact reverse
  inverse consistency across all 6 packages and 53 deliverables, including
  the repaired OBJ-3/OBJ-4 omissions and PKG-04's E-2 consequence.
- `N1-R1-F2` remains closed for the recorded A3 and A7 carrier allocation.
  The candidate carries role parity, labelled fallback, evidence calibration,
  instruction+config assertion, hard containment, all three command-network
  postures, explicit-user-act `acceptForSession`, grouping caveat,
  enumerated service endpoints, and exact-pin G-APPR proof.
- `N1-R1-F3` remains closed. `DerivativePackageState=INCOMPLETE` uses the
  fixed SCOPE_CHANGE vocabulary.
- `N1-R2-F1` remains closed. `Amendment_Actions.csv` has the exact current
  nine-column schema, eight ordered actions, and 8/8 evidence-supported
  `SupersessionBindingPresent=NO` dispositions.
- `N1-R3-F1` remains closed. All 53 deliverables assign Ryan Tufts and OI-011
  is concordant across the current working-surface and telemetry assertions.
- `N1-R4-F1` remains closed. The candidate says PKG-04 has 11 deliverables
  and records DEL-04-09's accepted D-GOV-25/OI-010 state without reopening
  owner acceptance.

## Independent checks that passed

- Every bound live decomposition/register/trace/telemetry SHA-256 and
  `execution/_ScopeChange/_LATEST.md` reproduces the Phase-0c basis.
- `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`,
  `WORK_GRAPH.json`, `DAG.md`, `Impact_Assessment.md`, and the Gate-1
  AUDIT_DECOMP coverage summary remain byte-identical to their protected
  bases.
- A fresh deterministic build in an isolated temporary root reproduced all
  seven candidate SHA-256 identities and `Gate_3_Exact_Amendment.diff`
  byte-for-byte.
- Applying the exact diff with `--unidiff-zero` to isolated bound-input copies
  reproduced every candidate byte exactly.
- An isolated execution of `validate_gate3_candidate.py` reproduced
  `PASS: 95 checks, 0 failures`; the regenerated JSON was byte-identical to
  `Gate_3_Validation.json`.
- Independent full-register derivation confirmed 53 unique deliverables, 104
  scope items, 7 objectives, 85 forward rows, 59 reverse units, PKG-02=12,
  PKG-04=11, Context Envelopes S=14/M=38/L=1, and zero dangling or asymmetric
  scope, objective, forward, or reverse relationships.
- DEL-02-06 retains SOW-104, OBJ-001/002/004/007, REQ-027, D-GOV-20, and its
  standing integration/release-assurance role. The accepted compatibility
  JSON remains SHA-256
  `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`
  with exactly ten `HELD_UNAVAILABLE` objects and null identities.
- G0 A4's retirement/restart semantics are explicit in DEL-02-11: active-turn
  terminalization, conditional `thread/resume` under canonical-root/account/
  policy-digest continuity with canonical cwd, fresh-thread fallback, and no
  in-flight re-attach or automatic replay claim.
- R2-A is reproduced byte-verbatim in `Decision_Log.md`; Gate 3 and Gate 4
  remain separately `PENDING_OWNER_APPROVAL`.
- Gate-4 planning covers all seven four-file PREPARATION INITs, DEL-02-06
  context propagation, dependency/estimate/schedule advisories, graph and
  audit reruns, a separate closure-validation lane, pointer quarantine, and
  stop rules.
- The candidate current-state sweep found no remaining stale 46/52-unit,
  PKG-02=6, PKG-04=10, M=31, OI-011, or DEL-04-09 acceptance assertion in a
  current-state section. Preserved predecessor decision and change-log text
  remains identifiable as historical lineage.
- Candidate whitespace, `git diff --check`, literal diff apply-check,
  protected-byte fences, candidate-folder absence, `_STATUS.md` protection,
  and Gate-5 fences pass.
- No live decomposition, companion register, pointer, `_STATUS.md`, package
  folder, SOW, dependency, estimate, schedule, runtime, tool, App, hold, pin,
  or Gate-5 surface changed. Concurrent N2 governance-harness work was outside
  this review and was not touched.

## Disposition

N1 is not ready for HELP_HUMAN fan-in because two explicit, owner-accepted
Gate-2 controls are absent from the exact authoritative carrier rows. Repair
only `N1-R5-F1` and `N1-R5-F2`, refresh the deterministic identities and
evidence claims, and submit the complete N1 package to a fresh independent
review.
