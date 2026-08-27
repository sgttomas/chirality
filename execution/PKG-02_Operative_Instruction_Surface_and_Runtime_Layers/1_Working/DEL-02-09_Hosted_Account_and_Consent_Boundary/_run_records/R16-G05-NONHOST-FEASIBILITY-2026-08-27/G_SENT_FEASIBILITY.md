# R16 N3.6 — deterministic G-SENT feasibility

- Date: 2026-08-27
- Node: `N3.6`
- Carrier: `DEL-02-09`
- Result: `SUPPORTED_FOR_DESIGN`
- Gate status: feasibility evidence only; `G-SENT` has not passed
- Account posture: synthetic no-account data only
- Vendor/App Server execution: none
- Authentication, login, device-code flow, Keychain access, credentials,
  tokens, and account mutation: none
- Command network authority or approval: none

## Verified basis and sequencing

| Input | Recomputed SHA-256 |
|---|---|
| `plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md` | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| `plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md` | `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba` |
| accepted DEL-02-09 `ScopeOfWork.md` | `e0cf3285f36c4397840d4875641d48bae53c493cff1bc065c3315e6575478176` |

N0 was complete and pushed before this fixture ran. The branch HEAD and its
remote were both `0246e92b4bfede52c226d58122e8ac4bb980e666`; the immutable N0
transcription commit `9164d9545` is its ancestor. This node did not require N1
or any vendor binary.

## Fixture contract

The disposable fixture modeled a fail-closed coordinator preflight. A turn is
eligible to proceed only when all of these synthetic current values exactly
match the recorded values: canonical root, account identity, account epoch,
consent version, consent root, consent account identity, consent policy
digest, effective policy digest, worker generation, and fixed cwd. Missing or
different values deny the preflight.

The synthetic policy was canonicalized as compact sorted-key JSON and hashed:

```json
{"allow_login_shell":false,"canonical_root":"/Users/ryan/.codex/worktrees/0b6e/chirality","command_network":false,"temporary_write":false,"writable_roots":["/Users/ryan/.codex/worktrees/0b6e/chirality"]}
```

SHA-256: `2141a82c777b9d99cc1814e0a289db324f806734d6934fe1dd4e0ba2d27ecc72`.

The disposable Python fixture source had SHA-256
`3717bd9e1b01e4b701fae34eb0e43827108e5191e38ab02955c6f58cd5be929c`.
It used only synthetic strings and filesystem path literals, ran with
`/usr/bin/python3 -B` in a non-login execution, returned exit `0`, and emitted
`total=21`, `matched=21`, `mismatched=0`.

## Exact deterministic cases and results

| Case | Attempt | Expected | Observed | Decision reason |
|---|---|---:|---:|---|
| `PF-00` | all preflight values match | `ALLOW` | `ALLOW` | `all_match` |
| `PF-01` | canonical root drift | `DENY` | `DENY` | `canonical_root` |
| `PF-02` | account identity drift | `DENY` | `DENY` | `account_identity` |
| `PF-03` | account epoch drift | `DENY` | `DENY` | `account_epoch` |
| `PF-04` | consent version drift | `DENY` | `DENY` | `consent_version` |
| `PF-05` | consent root drift | `DENY` | `DENY` | `consent_root` |
| `PF-06` | consent account identity drift | `DENY` | `DENY` | `consent_account_identity` |
| `PF-07` | consent policy digest drift | `DENY` | `DENY` | `consent_policy_digest` |
| `PF-08` | effective policy digest drift | `DENY` | `DENY` | `effective_policy_digest` |
| `PF-09` | worker generation drift | `DENY` | `DENY` | `worker_generation` |
| `PF-10` | cwd drift | `DENY` | `DENY` | `cwd` |
| `PF-11` | missing account identity | `DENY` | `DENY` | `account_identity` |
| `AC-01` | read canonical-root `AGENTS.md` | `ALLOW` | `ALLOW` | `policy_allows` control |
| `AC-02` | write synthetic canonical-root path | `ALLOW` | `ALLOW` | `policy_allows` control; classifier only, no write performed |
| `AC-03` | read `/etc/hosts` | `DENY` | `DENY` | `outside_root_read` |
| `AC-04` | write `/Users/ryan/synthetic-outside-root` | `DENY` | `DENY` | `outside_root_write` |
| `AC-05` | write `/tmp/synthetic-temp-write` | `DENY` | `DENY` | `temporary_write` |
| `AC-06` | write `/private/tmp/synthetic-temp-write` | `DENY` | `DENY` | `temporary_write` |
| `AC-07` | write under effective `TMPDIR` | `DENY` | `DENY` | `temporary_write` |
| `AC-08` | request login shell | `DENY` | `DENY` | `login_shell` |
| `AC-09` | request command network | `DENY` | `DENY` | `command_network` |

These are deterministic fixture decisions, not observations of a production
adapter, a live account, or App Server `turn/start` enforcement.

## Bounded hard-outer-envelope observations

Two positive attempts were safe to execute because the enclosing environment
kept them denied:

| Probe | Exact target | Exit | Exact observation | Cleanup/connection result |
|---|---|---:|---|---|
| outside-root write | `touch /Users/ryan/.chirality-r16-gsent-outside-write-probe-20260827` | `1` | `Operation not permitted` | follow-up `test ! -e` exited `0`; no file exists |
| command network | `/usr/bin/curl --noproxy '*' --connect-timeout 2 --max-time 3 http://192.0.2.1:9/` | `7` | `Failed to connect to 192.0.2.1 port 9 after 1 ms: Couldn't connect to server` | zero response bytes; no connection completed |

The probes ran through non-login execution. No network request was approved,
and the reserved TEST-NET-1 destination was not granted authority.

No actual outside-root read probe was executed because this evidence worker's
outer filesystem envelope permits broad reads and therefore cannot establish
the intended product denial. No actual temporary-write denial probe was
claimed: the explicitly authorized disposable fixture itself was created
under `/private/tmp`, demonstrating that this worker envelope does not prove
the product's required temporary-root denial. No login shell was launched;
the R16 global containment rule required non-login shells, so the fixture
tested fail-closed request classification only.

## Calibrated verdict

`SUPPORTED_FOR_DESIGN` applies to the deterministic no-account limb only. The
fixture demonstrates that an exact-match preflight can reject each required
identity/continuity drift independently and that a fail-closed action policy
can represent the required outside-root read/write, temporary-write,
login-shell, and command-network denials. The enclosing environment also
directly denied one outside-root write and one command-network connection.

This is not a `G-SENT` gate-pass claim. The following remain
`UNAVAILABLE_UNDER_BOUNDS`:

- a real App Server thread and representative `turn/start` carrying the exact
  candidate sandbox/approval policy;
- a live authenticated account and account epoch/digest observation;
- model/tool sentinel execution for primary and descendant actions;
- production enforcement of outside-root reads, both temporary roots, login
  shells, sticky cwd, and command-network denial at `turn/start`; and
- packaged profile activation and release-gate sentinel behavior.

Those limbs require credentials/live authentication, the production adapter
and exact policy binding, generated or implemented surfaces, or broader
execution authority withheld by R16.

## Implementation implication

A later authorized implementation should make the coordinator preflight a
single fail-closed predicate evaluated before every production turn. It must
require every value rather than default missing data, bind consent to canonical
root plus account plus policy, compare worker generation and fixed cwd, and
refuse `turn/start` when the exact policy cannot be bound. The client boundary
should reject extra-root and login-shell operations before dispatch, while the
actual App Server sandbox must independently enforce read, write, and both
temporary-root denials. Command network must remain explicitly false and
outer-enforced. A later authorized live G-SENT must then exercise these exact
canaries through representative primary and descendant `turn/start` paths.

## Cleanup

The disposable root was
`/private/tmp/chirality-r16-gsent.zPMQbE`. It contained only the synthetic
fixture source. It is not evidence and must be absent at fan-in; the instance
return records the post-deletion verification.
