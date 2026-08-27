# N3.7 deterministic G-WIRE feasibility

**Run date:** 2026-08-27

**Primary evidence file:** this file

**Calibrated limb verdict:** `SUPPORTED_FOR_DESIGN`

**Gate status:** no G-WIRE, G0.5, implementation, cutover, or release gate pass is claimed.

## Authority and exact basis

This evidence is the deterministic/no-secret portion authorized by R16 N3.7.
It is evidence about a synthetic design, not an implementation or conformance
result for production Root, an App Server adapter, an event consumer, or a
packaged App.

| Basis | Recomputed SHA-256 |
|---|---|
| `plans/steers/chirality_app_v3_root_ruling_record_r16_2026-08-27.md` | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| `plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md` | `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba` |
| `plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md` | `a8463a7f0392978325e8d25558332e72868271e9c4d99ac26c7425bb3a448301` |
| `plans/steers/chirality_app_v3_g2_acceptance_transcription_steer_root_2026-08-25.md` | `a0d14e05b7749c06605bdfce5d978058b4bea999569f94d0a918a5f2bad6eb76` |
| DEL-02-10 `ScopeOfWork.md` | `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29` |
| DEL-02-12 `ScopeOfWork.md` | `62bcfbdd6a20b647f15594fdd35b312d62942f85cf96aedb4aae5db12ea04663` |
| accepted G2 `03_EMPIRICAL_EVIDENCE/SCHEMA_TYPES_GAPS.md` | `bbcdeaa637f1789d8944ccf58bcf779a25bd60529ebc8fae8fc15ea64e8df053` |

The accepted R15 record expressly carries generated JSON schema, generated
TypeScript types, and the schema-derived exhaustive method inventory as
`UNAVAILABLE_UNDER_BOUNDS`. This run did not attempt to replace or infer any
of them.

N0 sequencing was satisfied before this deterministic execution. Commit
`9164d9545` was an ancestor of execution HEAD `0246e92b4`, and
`origin/codex/root-r16-g05-spikes-2026-08-27` contained `9164d9545` when the
run began.

## Execution boundary

- Runtime: Node `v24.18.0`, invoked through a non-login shell.
- Effective environment keys were exactly `LANG`, `LC_ALL`, `PATH`, `TMPDIR`,
  and macOS-injected `__CF_USER_TEXT_ENCODING`; no home, account, credential,
  token, or proxy variable was present.
- The fixture harness imported no product code and used no generated schema or
  generated type.
- It made no network call, launched no vendor process, accessed no account,
  credential, Keychain, device flow, or production configuration, and changed
  no adapter or event consumer.
- Synthetic fixtures and two result files existed only under
  `/private/tmp/chirality-r16-gwire-n3-7-vOTSmc` with file mode `0600`.
- Synthetic corpus values were deliberately non-secret:
  `SYNTHETIC-NOT-A-REAL-TOKEN-7f93`, `SYNTH-DEVICE-CODE-ABCD`,
  `https://invalid.example/device?user_code=SYNTH-ABCD`, and
  `Bearer SYNTHETIC-NOT-A-REAL-TOKEN-7f93`.

## Synthetic design evaluated

The fixture pipeline was deliberately small and evidence-only:

1. validate protocol version, object shape, event identifier, and turn ID;
2. reject unknown or malformed provider input with a bounded diagnostic code
   and no raw echo;
3. project only type-indexed allowlisted fields;
4. structurally redact the projection before the coordinator;
5. refuse a second terminal for the same turn;
6. structurally redact independently before the synthetic SSE and
   `events.jsonl` sinks; and
7. scan the coordinator projection and both serialized sinks for every
   synthetic corpus value.

The terminal allowlist was exactly, and only:

1. `turn.completed`
2. `turn.failed`
3. `turn.interrupted`
4. `turn.cancelled`

Accepted-case trace `A` was exactly:
`validate -> project -> redact:coordinator -> coordinator -> redact:sse -> sink:sse -> redact:event_log -> sink:event_log`.

Pre-coordinator rejection trace `R(code)` was exactly:
`validate -> reject:code`.

## Exact cases and results

| Case | Input purpose | Result | Coordinator / SSE / log count | Scan result |
|---|---|---|---:|---|
| C01 | accepted `turn.completed` v2 event | accepted; output `turn.completed`; trace A | 1 / 1 / 1 | zero hits in coordinator and both sinks |
| C02 | accepted `turn.failed` v2 event | accepted; output `turn.failed`; trace A | 1 / 1 / 1 | zero hits in coordinator and both sinks |
| C03 | accepted `turn.interrupted` v2 event | accepted; output `turn.interrupted`; trace A | 1 / 1 / 1 | zero hits in coordinator and both sinks |
| C04 | accepted `turn.cancelled` v2 event | accepted; output `turn.cancelled`; trace A | 1 / 1 / 1 | zero hits in coordinator and both sinks |
| C05 | fifth terminal-like identifier `turn.aborted` | rejected `UNSUPPORTED_PROVIDER_EVENT`; trace R | 0 / 0 / 0 | no bytes reached a sink |
| C06 | otherwise known terminal with protocol version 3 | rejected `UNSUPPORTED_PROTOCOL_VERSION`; trace R | 0 / 0 / 0 | no bytes reached a sink |
| C07 | known terminal missing turn identity | rejected `MISSING_TURN_ID`; trace R | 0 / 0 / 0 | no bytes reached a sink |
| C08 | known `turn.failed` carrying all four synthetic markers plus provider-shaped `accessToken`, `deviceCode`, `authUrl`, `providerPayload`, `authorization`, and `raw` fields | accepted after projection/redaction; trace A; all forbidden provider-shaped keys absent before coordinator and from sinks; redaction marker present in both sinks | 1 / 1 / 1 | zero hits in coordinator and both sinks |
| C09 | unknown provider type containing synthetic token and device-code fields | rejected `UNSUPPORTED_PROVIDER_EVENT`; bounded code contained no raw echo; trace R | 0 / 0 / 0 | no bytes reached a sink |
| C10 | positive-control scanner input containing every synthetic corpus value | all four marker IDs detected independently for SSE and event-log scans | 0 / 0 / 0 | four expected hits per scan |
| C11 | two valid terminal events for the same synthetic turn | first accepted; second rejected `DUPLICATE_TERMINAL`; second trace `validate -> project -> redact:coordinator -> coordinator -> reject:DUPLICATE_TERMINAL` | 1 / 1 / 1 total | zero hits in retained coordinator and sink bytes |

The suite executed **62 assertions with 0 failures**. It executed twice from
the same fixture bytes and produced byte-identical result JSON.

| Determinism evidence | SHA-256 / result |
|---|---|
| synthetic fixture bundle | `312b254791703da97d6bde4f4ae54f86dc17e9783e812b54e40b1031a10061a4` |
| first result JSON | `e47f8366414e6280764c23eb5a5c41b043ef22cac6c2119bcf66fe8fe54a74c7` |
| repeated result JSON | `e47f8366414e6280764c23eb5a5c41b043ef22cac6c2119bcf66fe8fe54a74c7` |
| byte comparison | equal |

## Findings and limitations

| Design claim | Evidence result | Calibration |
|---|---|---|
| four-terminal closure can be represented without admitting a fifth terminal | C01-C05 accepted exactly the four ruled identifiers and rejected `turn.aborted` | supports design feasibility only |
| malformed/version-incompatible input can be stopped before the coordinator | C05-C07 and C09 recorded no coordinator or sink event | supports design feasibility only |
| provider-shaped content can be projected and redacted before coordinator use | C08 removed forbidden provider fields and all synthetic corpus values before coordinator capture | supports design feasibility only |
| redaction can precede each sink independently | every accepted trace placed sink-specific redaction before SSE and event-log writes | supports design feasibility only |
| a multi-sink scan can detect leaks without false evidence from a broken scanner | C10 detected every positive-control marker in each sink; all accepted sink outputs had zero hits | supports design feasibility only |
| one terminal per synthetic turn can be enforced | C11 retained one terminal and refused the second | supports design feasibility only |

The full closed HarnessEvent v2 union remains unspecified by generated
exact-pin schema/types in this tranche. Therefore this run does not establish
generated-type conformance, exhaustive provider-event coverage, actual App
Server wire compatibility, real adapter ordering, consumer/replay migration,
logs or support-bundle coverage, actual SSE/`events.jsonl` integration, or
packaged-App behavior. Those are implementation/exact-pin evidence gaps, not
reasons to infer a schema or authorize production work.

## Implementation implication

A future separately authorized implementation can use the tested order as a
minimum invariant: exact-pin validation, bounded reject/project behavior,
allowlist projection, redaction before coordinator visibility, independent
redaction before every sink, and positive-control scans of every serialized
sink. It must bind those invariants to generated exact-pin schema/types and
the complete accepted HarnessEvent v2 contract before any G-WIRE conformance
or gate-pass claim. No runtime, adapter, consumer, App, pin, or production
configuration change is authorized by this feasibility result.

## Cleanup proof

Before cleanup the disposable directory contained only `fixtures.json`,
`run1.json`, and `run2.json`. The harness recursively deleted
`/private/tmp/chirality-r16-gwire-n3-7-vOTSmc`; an independent shell check
returned `cleanup_exact_path=PASS`, and a sorted search for
`/private/tmp/chirality-r16-gwire-n3-7-*` returned no path.
