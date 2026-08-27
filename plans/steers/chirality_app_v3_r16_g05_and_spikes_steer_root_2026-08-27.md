# ROOT v3 STEER — R16 G0.5 disposition transcription, OUT-002 completion attempt, and bounded feasibility spikes — 2026-08-27

## OWNER ACT — TRANSCRIBE VERBATIM

I approve R16-A through R16-F as proposed, amended to require transcription
node N0 before spike execution; fresh re-download only under the complete
R12-A terms and accepted 0.149.0 identities; exact evidence citations for
`features.plugins` and the three observed destinations; and explicit
preservation of TM-ROOT-106 and TM-ROOT-122 as open, unruled G1 blockers. I
knowingly adopt R16-B’s
`CONTINUE_SEPARATE_WITH_EXPLICIT_COORDINATION_ONLY` Tier-0 relationship
disposition.

## END OWNER ACT

The complete operative meaning of “R16-A through R16-F as proposed” is the
text in
`plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md`.
Read that record in full. This steer is the contract; read it in full before
acting. No remembered digest, summarized instruction, chat message, or prior
tranche grants authority beyond these bytes.

## BASIS GATE

1. Fetch current remote state without rebasing or rewriting history.
2. Require commit `b9960755bb7cbeed02e69591a2fcd51eaf2caf60` to be an
   ancestor of `origin/main`. Its tree must be
   `8465d017dab901b6d1fe1b4b0def047d64eec7aa`, and its parents must be:
   - `baa29d22fa034784cda221b2929061213e83ec91`
   - `5a78bc23547159992ed294bbc8d9633862555b14`
3. Require the first-parent delta from that basis to the merge that published
   R16 to contain only these two new paths:
   - `plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md`
   - `plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md`
4. Recompute the SHA-256 of both merged R16 instruments from actual bytes and
   record them before execution. Confirm that the OWNER ACT block above is
   byte-identical in the R16 ruling record, this steer, the N0 transcription,
   and the appended Root receipt.
5. Require the current Root workplan pointer and idle workplan to remain
   byte-identical to the pins below. No workplan activation is authorized.
6. Confirm `TM-ROOT-106` and `TM-ROOT-122` are still `OPEN` and no intervening
   act has disposed, commissioned, closed, or lifted either row.
7. If main has moved beyond the exact two-instrument merge, any pin differs,
   either blocker changed, or the owner act cannot be transcribed verbatim,
   stop before writing and return the discrepancy for a successor steer.

## PREDECESSOR AND SUBJECT PINS — RECOMPUTE FROM ACTUAL BYTES

Require these SHA-256 values at the R16 predecessor basis:

| Path | SHA-256 |
|---|---|
| `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |
| `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` | `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b` |
| `plans/steers/chirality_app_v3_root_ruling_record_r12_2026-08-24.md` | `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd` |
| `plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md` | `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391` |
| `plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md` | `a8463a7f0392978325e8d25558332e72868271e9c4d99ac26c7425bb3a448301` |
| `plans/steers/chirality_app_v3_g2_acceptance_transcription_steer_root_2026-08-25.md` | `a0d14e05b7749c06605bdfce5d978058b4bea999569f94d0a918a5f2bad6eb76` |
| `execution/_Coordination/CURRENT_WORKPLAN.md` | `efaea5b88a58e9fe408efffde3ac92ae3c4ec55fdde43b6c61f8add7d3913776` |
| `execution/_Coordination/WORKPLAN_2026-07-27_root_idle.md` | `f75497926a2ba74ae9038b4e09a06eb951bb8b86d41d6672894c79e6b9f3318d` |
| pre-R16 `execution/_Coordination/LOOP_RECEIPTS.md` | `fbe95c603a15fd155426482b36db65d8e259ae405049beded164d8e924b63b30` |
| `execution/_Coordination/_TaskManagement/REGISTER.csv` | `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` |
| accepted DEL-02-06 compatibility snapshot | `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4` |
| accepted compatibility-completion JSON | `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c` |
| accepted semantic owner-decision candidate V2 | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` |

The full accepted compatibility paths are:

- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-COMPATIBILITY-COMPLETION-004/candidate/COMPATIBILITY_COMPLETION_CANDIDATE.json`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md`

Require the accepted carrier Scope of Work pins:

| Carrier | SHA-256 |
|---|---|
| DEL-02-07 `ScopeOfWork.md` | `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5` |
| DEL-02-08 `ScopeOfWork.md` | `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430` |
| DEL-02-09 `ScopeOfWork.md` | `e0cf3285f36c4397840d4875641d48bae53c493cff1bc065c3315e6575478176` |
| DEL-02-10 `ScopeOfWork.md` | `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29` |
| DEL-02-11 `ScopeOfWork.md` | `abd5dcef7a835bafac3e1dd29d7f7b6771ad0aeb60e4af9c25734bfa2534ab02` |
| DEL-02-12 `ScopeOfWork.md` | `62bcfbdd6a20b647f15594fdd35b312d62942f85cf96aedb4aae5db12ea04663` |

Never copy a digest from memory into resulting records. Recompute every cited
identity from actual bytes before relying on it.

## EXACT G2 ARTIFACT IDENTITIES AND FRESH DOWNLOAD AUTHORITY

If and only if an authorized node needs the App Server binary, R16 extends
fresh access for this tranche under every R12-A term. The only permitted
release is official OpenAI `rust-v0.149.0` for macOS arm64, and the only
permitted assets are:

| Asset | Bytes | SHA-256 |
|---|---:|---|
| `codex-app-server-aarch64-apple-darwin.tar.gz` | `71843308` | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` |
| `codex-app-server-aarch64-apple-darwin.zst` | `50359498` | `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677` |
| `codex-app-server-package-aarch64-apple-darwin.tar.gz` | `93775517` | `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2` |

Every accepted asset contains the same App Server payload, SHA-256
`b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`.

Before download, identify the current official release channel and record its
metadata. Download only the minimum accepted asset set required for the
authorized node into a newly created untracked quarantine outside committed
evidence. Immediately verify name, size, and SHA-256 before extraction or
execution; then verify the extracted payload identity. If exact 0.149.0 is no
longer offered or any identity differs, delete quarantine and stop. Do not
substitute, update, repin, or accept another version. Commit evidence only,
never artifact bytes. Delete and verify absence of every quarantine and
disposable-state byte at closeout and after any stop.

## EXACT EMPIRICAL PINS FOR PLUGIN STARTUP AND OUT-002

Under the G2 candidate root
`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/APP-SERVER-0.149.0-G2-CANDIDATE-2026-08-24/`, require:

| Evidence | SHA-256 |
|---|---|
| `03_EMPIRICAL_EVIDENCE/CONFIG_READBACK_AND_PRECEDENCE.json` | `3eea0e0f075a8cbd0f143f5a0bc6b441ddb9691aca4c9a7d1d6d921d42581a93` |
| `03_EMPIRICAL_EVIDENCE/PLUGIN_SYNC_SWITCH.md` | `c3024e555589995acc685d2feb15d1ca38db2d4e9fa2855eb1a3f7d4e025928c` |
| `03_EMPIRICAL_EVIDENCE/DENIED_EGRESS_INVENTORY.json` | `abf745deb28f57c74eccac0d9f0f68c6bd5b07e7646cde66e5b6ea3d83d4b513` |
| `OUT-002_ENDPOINT_INVENTORY.md` | `fd6bd4e4dd7c2a0dc477e567becd5d2d092514db36dfedaf2fa2a529798d9f47` |

Those exact bytes establish for 0.149.0 that:

- `features.plugins` is the whole-plugin feature switch observed through
  runtime feature and configuration readback;
- its baseline current/default state was enabled;
- `-c features.plugins=false` read back as false and two independent runs
  suppressed every observed plugin-startup attempt; and
- exactly three plugin destinations were attempted in the baseline evidence,
  sandbox-denied, and completed no connection.

Current official documentation did not identify a dedicated curated-plugin
sync switch; do not misstate the empirical switch as a documentation claim.

## GLOBAL CONTAINMENT

Every binary-execution node uses a fresh disposable working directory and
fresh disposable `CODEX_HOME`, with no credentials, tokens, accounts, login,
device-code flow, Keychain access, ambient user Codex state, or copied/symlinked
configuration. Command network is off. Grant no approval to a network request.
Permit no write outside the disposable workspace and the exact evidence write
set. Use non-login shells only. Capture process lineage, arguments, effective
environment, exit status, stdout/stderr, filesystem delta, and denied egress.
Tear down the disposable state after every node.

The official release metadata and minimum authorized asset download are the
only approved external connections in this tranche. The vendor process may
complete no external connection. An attempted connection must remain denied,
be captured, and stop that limb if continued execution could widen exposure.

## WRITE SET

The Root session may write only:

1. an immutable successor DEL-02-06 R16 disposition packet under
   `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/`;
2. one new, uniquely named R16 evidence-only `_run_records/` subtree in each
   of these accepted Root carriers only when its mapped node produces evidence:
   - `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/_run_records/`:
     the supervisor/containment aspects of `G-SBX`, `G-PROT`, `G-ENV`, and
     `G-ROLE`;
   - `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/`:
     OUT-002 and the exact-pin/supply aspects of deterministic `G-APPR` and
     `G-WIRE`;
   - `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/_run_records/`:
     the account/consent/private-home aspects of `G-ENV`, `G-ROLE`, and
     deterministic `G-SENT`;
   - `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/_run_records/`:
     the API/event/approval aspects of `G-ROLE`, deterministic `G-APPR`, and
     deterministic `G-WIRE`; and
   - `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/_run_records/`:
     the cross-carrier feasibility fan-in and conformance-status matrix.
   DEL-02-11 is read-only basis in this tranche: no retirement/restart
   execution is authorized.
   Each claim has one primary evidence file; other carrier packets cite it by
   path and SHA-256 rather than duplicating competing truth.
3. run evidence under
   `execution/_Coordination/AgentRuns/ROOT_V3_R16_G05_SPIKES_2026-08-27/`;
4. one pure append, Receipt 131, to
   `execution/_Coordination/LOOP_RECEIPTS.md`; and
5. manifests, validation records, and handoff records inside those exact new
   packets.

Do not modify the accepted compatibility-completion JSON, its acceptance
snapshot, the G2 candidate packet, any existing immutable run record, any
`ScopeOfWork.md`, Task Management register, workplan, pin, runtime source,
tool source, App surface, Piping surface, Tier-0 surface, agent instruction,
or other file.

## N0 — GOVERNED TRANSCRIPTION — MUST COMPLETE BEFORE ANY SPIKE BINARY

1. Create branch `codex/root-r16-g05-spikes-2026-08-27` from the exact R16
   instrument merge on `main`.
2. Create an immutable DEL-02-06 successor disposition packet that:
   - cites the accepted compatibility-completion JSON without modifying it;
   - transcribes the ten-row R16-A routing matrix exactly;
   - materializes R16-B as the Root relationship record
     `CONTINUE_SEPARATE_WITH_EXPLICIT_COORDINATION_ONLY`;
   - records that the Tier-0 relationship alone is substantively disposed;
   - keeps the other nine bindings held and preserves their owners/gates;
   - records that `source_identity` and `implementation_act` remain
     unavailable and therefore G0.5 has not passed; and
   - creates no foreign-loop truth or work.
3. Create the N0 basis, owner-act transcription, manifest, validation, and
   handoff evidence under the authorized Root run directory.
4. Append Receipt 131 as a pure append to the pinned pre-image. Transcribe the
   OWNER ACT block verbatim; record the actual R16 ruling and steer SHA-256
   values, every predecessor pin, the ten-row disposition, all retained
   blockers and negative grants, and state `N0_TRANSCRIBED_SPIKES_PENDING`.
5. Validate N0, including byte-identical preservation of every accepted input
   and proof that only the Tier-0 relationship received a substantive
   disposition.
6. Commit and push N0 before downloading or executing any spike binary. Record
   that commit identity in the run evidence. Do not amend, squash, rewrite, or
   abandon the N0 commit during later nodes.

If N0 cannot complete exactly, stop without beginning N1 or any spike.

## N1 — FRESH ARTIFACT ACQUISITION WHEN REQUIRED

After the pushed N0 commit only, re-download the minimum accepted 0.149.0
asset set needed by the remaining nodes under the exact access and quarantine
terms above. Reuse no prior deleted artifact or disposable state. Record the
fresh official metadata, receipt identities, extraction identities, and
quarantine path. No binary may run before its exact accepted payload identity
is proved.

## N2 — OUT-002 COMPLETION ATTEMPT

Produce an OUT-002 endpoint-policy candidate that separately enumerates, with
evidence and epistemic status:

1. exact account service destinations;
2. exact model service destinations;
3. exact turn service destinations;
4. the three observed plugin-sync destinations;
5. the configured-but-not-attempted
   `https://chatgpt.com/backend-api/` base; and
6. every source used to infer or observe each row.

The policy must not treat account/model/turn service destinations as command
network authority. It must designate the three observed plugin-sync
destinations `NOT_REQUIRED_FOR_RC_MANAGED_PROFILE__NO_NETWORK_AUTHORITY` and
record `features.plugins = false` as the proposed RC managed-profile posture,
grounded in the exact empirical pins above. This is policy/evidence work only;
do not change a production configuration.

Declare OUT-002 complete only if the exact account/model/turn enumeration is
evidence-backed and the accepted DEL-02-08 completion criteria are met. If
authentication, credentials, an external connection beyond the download, or
unavailable schema/types are necessary for exhaustive enumeration, preserve
the completed rows, mark the missing rows and overall output
`UNAVAILABLE_UNDER_BOUNDS`, and do not infer endpoints.

## N3 — BOUNDED NON-HOST-MUTATING FEASIBILITY NODES

Run each limb independently. A stopped limb must not invalidate N0 or erase
completed sibling evidence. For each limb, state `SUPPORTED_FOR_DESIGN`,
`REJECTED`, or `UNAVAILABLE_UNDER_BOUNDS`; never state that the release-plan
gate passed.

### N3.1 — G-SBX feasibility

Using only the exact accepted App Server and disposable state, determine which
restricted read-only/workspace-write policy properties can be demonstrated
without a packaged App build, credentials, host mutation, or network. Test
`includePlatformDefaults: false`, root-only writes, temporary-root denial,
client process/shell surface denial, and exact immutable runtime-read needs
only where the current binary and bounds permit. Treat packaged Electron
fuse/entitlement proof and signed-bundle proof as unavailable in this tranche.

### N3.2 — G-PROT feasibility

Create evidence-only deterministic fixtures for representative protected-path
rules, including mid-path globs. Determine whether each rule can round-trip
through the available read, file-change, and shell-write policy representations
for primary and descendant actions. Do not implement a production compiler.
Any inexpressible or untestable rule is a blocking result, not an accepted
subset.

### N3.3 — G-ENV feasibility

Inspect and exercise disposable daemon/server/worker environment boundaries
available without launchd mutation: allowlisted variables, ambient secret and
home exclusion, login-shell denial, timeout bounds, temporary-root denial, and
root-local private scratch creation/cleanup. Effective plist/launchd,
supervisor, and packaged-bypass limbs remain unavailable unless provable
without touching host state.

### N3.4 — G-ROLE feasibility

Within Chirality's hard outer filesystem, network, process, canonical-root,
account-identity, and policy envelope, test only the presently available role
and delegated-harness-native evidence surfaces. Calibrate mechanism-proven,
configuration-asserted, instruction-asserted, and unavailable claims
separately. Do not claim mechanical Agent 2/TASK non-delegation unless the
mechanism proves it, and create no foreign-loop work.

### N3.5 — deterministic G-APPR feasibility

Produce exact-pin deterministic fixtures for the three accepted per-root
postures and attributed `networkApprovalContext` routing. Do not enable
network, emit a live request, grant an approval, or claim empirical prompt
delivery/destination grouping. Those live limbs remain separately gated.

### N3.6 — deterministic G-SENT feasibility

Produce deterministic, no-account fixtures for root/account/consent/policy/
generation/cwd preflight and positive outside-root/read/write/temp/login-shell/
command-network attempts only where they remain fully denied inside the hard
outer envelope. Do not authenticate or claim a live production `turn/start`
sentinel. Mark actual-turn and live-account limbs unavailable.

### N3.7 — deterministic G-WIRE feasibility

Using only synthetic non-secret fixtures, evaluate the available closed-event
v2, four-terminal, validation-before-coordinator, redaction-before-sink, and
multi-sink scan design. Generated schema/types remain unavailable unless
lawfully produced inside this tranche. Do not use real credentials or device
ceremony values, and do not change a production adapter or event consumer.

## N4 — FAN-IN, VALIDATION, AND RETURN

1. Produce a fan-in matrix mapping every N2/N3 claim to exact evidence,
   unavailable limb, stop reason, and implementation implication.
2. Recompute every cited SHA-256 and produce sorted manifests for each new
   immutable packet.
3. Prove the N0 commit remains an ancestor of final HEAD and its tree delta is
   unchanged.
4. Prove all quarantines and disposable states are absent and no artifact byte
   is tracked.
5. Verify the accepted compatibility JSON, accepted snapshots, G2 packet,
   workplan pointer, workplan, pins, Task Management register, runtime/tool/App/
   Piping/Tier-0 surfaces, and existing immutable records are byte-identical.
6. Update Receipt 131 only by appending a continuation to the N0 receipt entry
   or, if append-only receipt structure requires a second receipt, stop and
   request a successor steer rather than inventing Receipt 132. Record final
   limb states without rewriting the verbatim owner act or N0 facts.
7. Run `git diff --check` and every applicable Root G0-G4/governance validator.
8. Push ordinary commits to the same branch and open one unlabeled PR targeting
   `main`. Confirm hosted governance CI. Do not merge.

A spike stop is a compliant outcome. Preserve the pushed N0 commit, append the
stop evidence within the authorized write set, clean every disposable byte,
push the resulting ordinary commit, and return the PR for owner disposition.

## RETAINED NEGATIVE GRANTS

This steer authorizes no:

- `G-HELPER`, `launchctl`, plist, installer, LaunchAgent, host launchd, Finder,
  signed-bundle, notarization, or Developer ID mutation/proof;
- live-authenticated `G-SENT`, network-enabled `G-APPR`, login, device-code
  flow, Keychain access, credential/token/account movement, or account change;
- completed vendor-process external connection or network approval;
- production implementation, runtime/tool/App byte change, pin change,
  configuration adoption, App adoption, workplan activation, cutover, release,
  publication, redistribution, or reliance;
- mutation of accepted evidence or an existing immutable record;
- foreign-loop write, decision, dependency, or work; or
- disposition, commissioning, closure, or lift of `TM-ROOT-106` or
  `TM-ROOT-122`.

The Tier-0 relationship disposition is the only substantive held-binding
disposition. The other nine bindings remain held. G0.5 remains incomplete
because `source_identity` and `implementation_act` remain unavailable.

## STOP CONDITIONS

Stop the affected node, preserve N0, clean disposable state, and report without
scope expansion if any basis or digest differs; exact 0.149.0 is unavailable;
an artifact identity differs; containment cannot be established; a credential,
login, Keychain, live approval, host mutation, or unauthorized connection is
required; a write outside the exact set is needed; an existing immutable byte
would change; OUT-002 would require inference; a gate-pass claim would exceed
the evidence; either TM blocker changed; a validator fails; or main moved.

## RETURN

Return:

- branch, every commit, N0 commit, PR, labels, target, and merge state;
- exact changed-path list by commit and final tree;
- actual R16 ruling and steer SHA-256 values;
- every recomputed predecessor, artifact, payload, and evidence identity;
- N0 ten-row routing and Tier-0 relationship disposition evidence;
- OUT-002 row-by-row status;
- each N3 limb verdict and exact evidence/limitation;
- quarantine/disposable-state deletion proof;
- local validation and hosted-CI results; and
- confirmation that the PR is unmerged, the workplan remains idle, the other
  nine bindings remain held, G0.5 remains incomplete, `TM-ROOT-106/122` remain
  open and unruled, and every retained negative grant remains intact.
