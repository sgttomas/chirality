# R16 G0.5 N3.5 — Deterministic G-APPR Feasibility

- **Verdict:** `SUPPORTED_FOR_DESIGN`
- **Calibration:** deterministic fixture feasibility only; this is not a
  G-APPR gate-pass claim and creates no implementation or network authority.
- **Execution date:** 2026-08-27
- **Exact-pin basis:** OpenAI App Server `rust-v0.149.0`, accepted payload
  SHA-256
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`.
  No App Server binary was required or executed for this synthetic limb.
- **Containment result:** command network was not enabled; no live request was
  emitted; no approval was granted or applied; no production configuration or
  implementation byte changed.

## Recomputed input identities

| Input | SHA-256 |
| --- | --- |
| `plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md` | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| `plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md` | `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba` |
| `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` | `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b` |
| DEL-02-08 `ScopeOfWork.md` | `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430` |
| DEL-02-10 `ScopeOfWork.md` | `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29` |
| N2 `OUT002_ENDPOINT_POLICY_CANDIDATE.md` | `f8626f88c7bf4e733da858e55ef304307d72c61e293c26355ecd072a1bf96a54` |

N0 was already preserved in commit
`9164d95456bd67576a1b1164fd08e52516edb368` before this limb began.

## Deterministic fixture method

The synthetic fixture and evaluator were created only under
`/private/tmp/chirality-r16-g-appr-n3-5-20260827/`. The fixture SHA-256 was
`3e3db63b58a6ee69e64960d77d850955c0eeeaca2f30e165273f86db7b8054a5`;
the evaluator SHA-256 was
`6c5772e9179ba49a0e4219fcf841edbbcfca113a64a06d7ee52902581c40db6f`.
The evaluator was run twice using:

```text
jq -cS -f evaluate.jq fixtures.json
```

Both canonical results had SHA-256
`4a8a25f9c0e8282f3b291bfcc4cd034149d44b882b9dd170bd73eac27a84270c`.
The result was 12 cases, 12 passed, 0 failed. Fixture host
`fixture.invalid` is reserved synthetic data; it was never resolved or
contacted.

## Exact posture cases

| Case | Exact fixture vector | Expected and observed result |
| --- | --- | --- |
| `P1_DEFAULT_NO_COMMAND_NETWORK` | `posture=no_command_network`; `is_default=true`; `network_access=false`; attributed request; `networkApprovalContext=null` | `PASS` — `DENY_WITHOUT_PROMPT` |
| `P2_ASK_PER_DESTINATION` | `posture=ask_per_destination`; `network_access=false`; attributed request; `networkApprovalContext.host=fixture.invalid`; `protocol=https`; exact caveat “A grant may unblock queued requests to the same destination; grouping requires empirical exact-pin observation.”; `acceptForSession=false`; `explicitUserAct=false` | `PASS` — fixture routes to `ROOT_API_V2_MANAGED_PROMPT`; no prompt was delivered |
| `P3_LABELLED_COMMAND_NETWORK_ON` | `posture=command_network_on`; `network_access=true`; label=`Command network on`; `synthetic_request=null` | `PASS` — `REPRESENTATION_ONLY__LIVE_EXECUTION_NOT_PERFORMED` |

Each request attribution vector contained `canonical_root_id`,
`initiating_role`, and `initiating_instance_id`. The ask vector demonstrates
that host and protocol can be carried through attributed
`networkApprovalContext` routing without making a request.

## Exact attributed-decision cases

| Case | Exact fixture vector | Expected and observed result |
| --- | --- | --- |
| `D1_ATTRIBUTED_DENIAL` | attributed synthetic human actor; `decision=deny`; `acceptForSession=false`; `explicitUserAct=true`; `decisionApplied=false` | `PASS` — attributed denial fixture accepted structurally; nothing applied |
| `D2_UNATTRIBUTED_DECISION` | `attribution=null`; `decision=deny`; `decisionApplied=false` | `PASS` — `REJECT_UNATTRIBUTED` |
| `D3_SESSION_ACCEPT_WITHOUT_EXPLICIT_USER_ACT` | attributed actor; `decision=not_evaluated`; `acceptForSession=true`; `explicitUserAct=false`; `decisionApplied=false` | `PASS` — `REJECT_SESSION_ACCEPT_WITHOUT_EXPLICIT_USER_ACT` |
| `D4_SESSION_ACCEPT_EXPLICIT_USER_ACT_SHAPE_ONLY` | attributed actor; `decision=not_evaluated`; `acceptForSession=true`; `explicitUserAct=true`; `decisionApplied=false` | `PASS` — `SCHEMA_ELIGIBLE__NOT_GRANTED_OR_APPLIED` |

These decision cases prove only deterministic shape and refusal rules.
`D4` does not contain an allow decision and did not grant or apply anything.

## Exact refusal cases

| Case | Exact defect | Expected and observed result |
| --- | --- | --- |
| `R1_ASK_MISSING_HOST` | ask posture with `host=null` | `PASS` — `REJECT_MISSING_HOST` |
| `R2_ASK_MISSING_PROTOCOL` | ask posture with `protocol=null` | `PASS` — `REJECT_MISSING_PROTOCOL` |
| `R3_ASK_UNATTRIBUTED_REQUEST` | ask request with attribution absent | `PASS` — `REJECT_UNATTRIBUTED` |
| `R4_COMMAND_NETWORK_ON_UNLABELLED` | `network_access=true` with empty label | `PASS` — `REJECT_UNLABELLED_ON_POSTURE` |
| `R5_DEFAULT_WITH_NETWORK_ACCESS_TRUE` | default no-network posture with `network_access=true` | `PASS` — `REJECT_DEFAULT_NETWORK_ACCESS_TRUE` |

## Claim, limitation, and implementation implication

The fixtures support a design in which one root-scoped posture discriminator
enforces the three accepted G0 A7 states, approval requests and decisions are
attributed, ask-per-destination requests carry visible host/protocol through
`networkApprovalContext`, the grouping caveat is preserved, and
`acceptForSession` is structurally unavailable without an explicit user act.

This evidence does **not** establish:

- empirical managed-prompt delivery at exact pin 0.149.0;
- empirical grouping of queued requests by destination;
- any live network behavior, completed connection, or approval effect;
- generated or implemented Root API v2 schema/types; or
- complete DEL-02-08 OUT-003 or DEL-02-10 OUT-005 acceptance.

Prompt delivery and destination grouping therefore remain
`UNAVAILABLE_UNDER_BOUNDS` within this deterministic limb. Their proof needs
the separately authorized network-enabled exact-pin G-APPR work that R16
explicitly withholds.

Implementation should encode the three postures as a closed root-scoped
policy state; require request and decision attribution; require host and
protocol for ask routing; reject unattributed records and unlabelled on-state;
enforce `acceptForSession => explicitUserAct`; and retain a non-executing
fixture suite equivalent to these cases. A later separately authorized
exact-pin integration suite must prove actual prompt delivery and observe
same-destination grouping before G-APPR can pass.

## Cleanup

After durable evidence capture,
`/private/tmp/chirality-r16-g-appr-n3-5-20260827` was deleted. Both a direct
absence test and a `/private/tmp` name scan returned no path. No transient
fixture, evaluator, App Server artifact, credential, token, account state, or
production configuration is part of this evidence packet.
