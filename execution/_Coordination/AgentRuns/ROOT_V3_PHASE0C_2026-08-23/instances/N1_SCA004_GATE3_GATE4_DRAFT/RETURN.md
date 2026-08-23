# Return — N1 SCA-004 Gate 3 / Gate 4 drafting

InstanceID: `N1_SCA004_GATE3_GATE4_DRAFT`

Result: `PASS — REVIEW CYCLES 1 THROUGH 5 REPAIRED`

Basis: `8635e40995b05f494ae35c6083dabdd50068bb52`

Role evidence: Agent 2 ephemeral generalist; `role not mechanically enforced`; non-delegation instruction-asserted.

## Outcome

The exact SCA-004 Gate-3 candidate and the separately approvable Gate-4
propagation plan are drafted. No Gate-5 application occurred. Live
decomposition truth, all six live companion/trace/telemetry files,
`execution/_ScopeChange/_LATEST.md`, every `_STATUS.md`, and every live
package/deliverable folder remain unchanged.

The candidate projects 46 to 53 deliverables, including PKG-02 6 to 12 and
PKG-04 10 to 11, while retaining 6 packages, 104 scope items, and 7
objectives. DEL-02-06 retains SOW-104, OBJ-001/002/004/007, REQ-027, and the
ten `HELD_UNAVAILABLE` bindings. DEL-02-07 through DEL-02-12 are candidate
PKG-02 carriers; DEL-04-11 is a candidate PKG-04 `TEST_SUITE` allocated to
SOW-041 and SOW-053.

Review cycle 1's three findings are repaired without widening the write set:
the reverse register is now a full deterministic inverse of candidate
forward/scope/objective truth; the exact carrier rows fully and explicitly
carry accepted G0 A3/A7 semantics; and the fixed
`DerivativePackageState` uses the allowed `INCOMPLETE` value.
Review cycle 2's action-register finding is also repaired: the exact current
STRUCTURE schema has nine columns, and all eight structural/allocation
actions record `SupersessionBindingPresent=NO` because the accepted evidence
identifies no admitted-authority fact supersession.
Review cycle 3's OI-011 finding is repaired in the deterministic candidate:
the working surface and coverage telemetry now both account for all 53 Ryan
Tufts assignments — the original 45 under D-GOV-27, DEL-02-06 under SCA-001,
and the seven SCA-004 candidate rows.
Review cycle 4's current-state finding is repaired: the D-12 explanation now
states PKG-04 has 11 deliverables, and telemetry records DEL-04-09's existing
D-GOV-25 Gate-5 acceptance at Context Envelope `L` with OI-010 closed rather
than reopening it as proposed.
Review cycle 5's two accepted-control findings are repaired in the exact
carrier rows. DEL-02-07 now requires authentication-token validation for
every private-socket request, binds tokens to socket owner and worker
generation, and invalidates them during stale-socket recovery while retaining
Unix `0700`/`0600`, sole-broker, renderer/CLI exclusion, and no-TCP controls.
DEL-02-10 now names the closed HarnessEvent v2 terminal set exactly as
`turn.completed`, `turn.failed`, `turn.interrupted`, and `turn.cancelled`
while preserving the approval, payload, A3, A7, and persistence boundaries.

## Outputs

- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Candidate/`
  contains exact candidate copies of the working surface and all six
  companion/trace/telemetry files.
- `Gate_3_Exact_Amendment.diff` is the complete zero-context patch from the
  seven bound inputs to the seven candidate files; SHA-256
  `0724668f6fb85189f4c3ee142a21cef938c8dd47373be543d8b108c8e934637b`.
- `Amendment_Preview.md` contains the Gate-3 exact-amendment presentation and
  question; SHA-256
  `ff7743554270aee177feed4226a4fa35fd503ce34760f69644176878bcffdca4`.
- `Propagation_Plan.md` and `Amendment_Actions.csv` contain the Gate-4 plan
  and eight controlled actions; SHA-256 values
  `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`
  and
  `4e623bcc5e69d056f71d9ed860ff729a0dfc9b8d8c635e7dd23b3c6b10d2871d`.
- `build_gate3_candidate.py` deterministically rebuilds the candidate and
  exact diff; SHA-256
  `246453b5335580372f69b4beff411d990de42537d1f8ba93248fe518c1205f26`.
- `validate_gate3_candidate.py` validates basis protection, topology,
  mappings, traces, telemetry, exact-diff fidelity, and forbidden writes;
  SHA-256
  `5a394c7bb53abb7cd4e58e34b712ed50eb1aef00306c95730489f728114d2ee1`.
- `Gate_3_Validation.json` records `PASS`, 98 checks, 0 failures; SHA-256
  `dc5fe4355322a96b7da61606fff7d8dd51943a7d606f132966705bfb70b9f129`.
- `Decision_Log.md` records R2-A verbatim as `G2-ACCEPTED-001`, with Gate 3
  and Gate 4 separately pending; post-draft SHA-256
  `a35f2e13a70561b207092ff46d409525a2b7d4ebd14f3b938d06f253da5e4aec`.
- `Handoff_State.md` carries the four-state Gate-3/Gate-4 draft handoff;
  post-draft SHA-256
  `41cadc01f17642d8f8318bc18f60c39adecac40253351f5ac97ca85888178cfd`.

## Exact candidate identity

| Candidate surface | SHA-256 |
|---|---|
| Working surface | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` |

## Protected basis hashes reverified

| Live surface | SHA-256 |
|---|---|
| Working surface | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| Deliverable register | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` |
| Scope ledger | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` |
| Objective register | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` |
| Forward trace | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` |
| Reverse trace | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` |
| Coverage telemetry | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` |
| `_LATEST.md` | `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` |
| `Brief.md` | `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126` |
| `Gate_1_Validation.md` | `812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14` |
| `Parsed_Actions.csv` | `a89b77dc1ce478f7ea5bbc3ebb12706d69e93876e6a7f4cca0cfd5ea5a9e738b` |
| `WORK_GRAPH.json` | `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9` |

The scoped pre-write basis gate passed without drift, so the Gate-1
AUDIT_DECOMP baseline was not rerun. The final protected-surface checks also
confirm no deleted or transiently moved live file remains.

## Validation

- `python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate3_candidate.py`
  — `PASS: 98 checks, 0 failures`.
- `git apply --unidiff-zero --check execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Exact_Amendment.diff`
  — PASS.
- Literal scratch application of that diff to copies of all seven protected
  live inputs — PASS; every resulting file is byte-identical to its
  `Gate_3_Candidate/` counterpart.
- `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`
  — PASS; zero skipped binary/symlink paths.
- `git diff --check` — PASS.

The exact diff uses zero context and preserves the live inputs' native line
endings. The review-cycle-1 reverse check derives and compares every package
and deliverable row. It confirms inherited objective omissions were repaired
for DEL-01-04, DEL-03-01, DEL-03-06, and DEL-06-04 and that PKG-04 now carries
the E-2 consequence of DEL-04-11's cross-package mapping. Dedicated semantic
checks confirm complete A3 allocation to DEL-02-07/09/10/12 and complete A7
allocation to DEL-02-08/09/10/12.
Four further checks enforce the exact nine-column `Amendment_Actions.csv`
schema, eight ordered entity/action rows, and 8/8 evidence-supported `NO`
supersession-binding dispositions.
Three additional checks require exactly 53 Ryan Tufts assignments, the
OI-011 working-surface affected count of 53, and exact responsibility-lineage
concordance between the working surface and telemetry.
Three further checks enforce the D-12 PKG-04=11 narrative, DEL-04-09's
accepted/closed telemetry disposition, and a broader scan of current
topology/status claims for stale pre-candidate values.
Three final semantic checks enforce DEL-02-07's complete accepted private-
socket control set, DEL-02-10's complete approval/payload/A3/A7/persistence
boundary set, and the exact closed four-member HarnessEvent v2 terminal set.

The local `origin/main` tracking ref advanced to
`a702dd6ec5005b361c8c023b12b599a425e5e2b8` during repair. Per parent
direction, this repair remains frozen on `8635e40995b05f494ae35c6083dabdd50068bb52`;
no fetch, sync, rebase, commit, push, or merge was performed.

## Exact write set

Modified within SCA-004:

- `Decision_Log.md`
- `Handoff_State.md`

Added within SCA-004:

- `Amendment_Actions.csv`
- `Amendment_Preview.md`
- `Propagation_Plan.md`
- `Gate_3_Exact_Amendment.diff`
- `Gate_3_Validation.json`
- `build_gate3_candidate.py`
- `validate_gate3_candidate.py`
- the seven files under `Gate_3_Candidate/`

Added within the instance folder:

- `RETURN.md`
- terminal update to `STATUS.json`

No other write belongs to this instance. Concurrent N2 governance-harness
changes visible in the shared worktree were not touched.

## Blockers and required reruns

1. Owner Gate-3 approval, correction, or decline is required against the
   exact candidate bytes.
2. Owner Gate-4 approval, correction, or decline is a separate act against
   the exact propagation-plan bytes.
3. Gate 5 remains closed. Live copy, seven folder INITs, SOWs, dependencies,
   estimates, scheduling, graph re-derivation, audits, `_LATEST.md` treatment,
   implementation, App acts, hold lifts, cutover, and release remain
   unauthorized.
4. Before any application, reverify all seven protected live SHA-256 values,
   candidate identity, candidate-ID absence, and `_LATEST.md`; rerun the
   98-check validator.
5. After any approved application, run deterministic register/trace/telemetry
   validation and fresh scoped AUDIT_DECOMP; after folders are live,
   re-derive the graph and rerun AUDIT_DEP_CLOSURE.
