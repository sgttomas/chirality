# WORKING_ITEMS Run — D-APP-50 Headless Preview Live Transport

**Date:** 2026-07-20

**Package:** PKG-10 — Domain Engine Future Boundary

**Deliverable:** DEL-10-01 — DomainEngineProfile Contract Draft

**Authority:** D-APP-50 Option A, riders 1–6, limited to the already-ruled read-side `domain_headless_preview_run` exposure for `open_pipe_stress`

**Implementation commit:** `f67d44706f4b2b5495833f809cb0bc714d2bbc18` (single parent `bc35e3b0049d990f494dd3610603be285c7aa9ed`)

## Staged closeout rationale

The runtime implementation was validated before its governed pull-contract pin could be
updated. D-APP-48 binds exported package bytes to a reachable commit, while the W1
implementation owner had no Git authority. G0 therefore created the exact 14-path
implementation commit, and this serialized W2 closeout repins D-APP-48 to that reachable
commit before removing the corresponding DEL-10-01 residual. No implementation bytes were
changed during W2.

## Implemented boundary

`mcp__chirality__domain_headless_preview_run` is live only for the registered
`open_pipe_stress` profile and only as a read-side, input-dependent, exclusive tool. It
invokes one caller-configured local `openpipestress-runner solve` process. The harness
remains the permission, path-containment, event, redaction, result-budget, and artifact
layer; it does not reproduce piping mechanics.

The MCP input is `runnerInputRef`, a regular-file reference contained by the project root.
The referenced file carries the complete schema-first DEC-065 solve request, and its exact
bytes are sent to stdin. This preserves an auditable input reference, byte identity, and the
full request envelope. The prior `modelInputPath` concept represented only a preview-model
fragment and could not truthfully carry the complete DEC-065 request, so it was rejected and
removed rather than adapted into a partial transport.

## Configured executable and process controls

- Configuration requires `CHIRALITY_OPEN_PIPE_STRESS_RUNNER_PATH` and
  `CHIRALITY_OPEN_PIPE_STRESS_RUNNER_SHA256`.
- Before every invocation, the path must be absolute; its realpath must resolve to a regular,
  executable file; and the executable bytes must match the configured lowercase SHA-256.
  There is no `PATH` lookup or fallback executable.
- The harness directly spawns the verified executable with exact argv `solve`, `shell: false`,
  one foreground process, and the minimal environment `NODE_ENV=production`, `LANG=C`, and
  `LC_ALL=C`. Ambient secrets are not inherited.
- The exact validated `runnerInputRef` bytes are written once to stdin. Structured JSON on
  stdout is the only accepted result channel. Stderr is separately bounded and is never
  returned to the model.
- The default timeout is 30 seconds. Stdout and stderr each have independent 2 MiB caps;
  timeout or overflow terminates and reaps the child. Signals, unsupported exits, malformed
  JSON, schema mismatches, and exit/result contradictions fail closed.
- DEC-065 exit `0` requires a structured result with no blocking diagnostic and is returned
  as completed. Exit `1` requires a structured blocking diagnostic and is preserved as a
  non-successful MCP result. Exit `2` is an input/usage refusal. Other exits are unsupported.
- The transport has no network, daemon, telemetry, shell, output-path, hidden filesystem
  mutation, proposal, acceptance, or apply behavior.

## D-APP-48 repin

The private intra-repo pull contract is repinned to source commit
`f67d44706f4b2b5495833f809cb0bc714d2bbc18` and registry version
`harness-tools.v14.headless-preview-live`. The deterministic validator required these
byte-current export hashes:

| Export | SHA-256 |
|---|---|
| `./event-schema` | `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` |
| `./mcp/tool-names` | `92912cd43633aadb28f5e3155e815abba8a6a51f74a3e77132097e9b0d883f85` |
| `./tool-catalog` | `27504b2a5a487116a6c7a886d56efdc5f3cf4426779f2a3dca665e184977f83e` |
| `./tool-descriptor` | `a121391ec71851e7280db4ebf2731b53db6829cb42d1bf07604cb8a4f76dc6d4` |
| `./types` | `5c789e28915f96913910cb820db8ff8a58dc72ea085541f0977d08a4bc58ff9f` |

All other export hashes, package identity, constants, export order/targets, validation
commands, and D-APP-48 boundary flags remain unchanged. The repin records current bytes; it
does not reinterpret or widen D-APP-48.

## Validation evidence

- The frozen 14 implementation files reproduce the W1/G0 SHA-256 map exactly.
- The D-APP-48 pull-contract validator and the recorded harness-contract dependency lint
  pass against the reachable implementation commit.
- Strict duplicate-key JSON parsing, the focused headless transport suite, generated catalog
  test, frontend typecheck, receipt validation, authority-corpus v9 status, repository
  self-check, validation pytest baseline, practitioner-harness pytest baseline, and
  tracked/untracked/cached whitespace and containment checks are the W2 closeout gates.
- W1 separately recorded the full implementation validation, including adjacent and full
  frontend tests, build/premerge, secret scan, and generated documentation evidence. W2 is a
  repin-and-record closeout and does not alter those implementation bytes.

## Exact governed/product changed paths

The final tranche has exactly 18 governed/product paths: the 14 implementation paths in the
G0 commit plus four W2 closeout paths. Run-control records under the named coordination run
are separate orchestration evidence.

1. `projects/chirality-app-dev/frontend/docs/harness/adding_a_tool.md`
2. `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md`
3. `projects/chirality-app-dev/frontend/docs/harness/tool_catalog.md`
4. `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-catalog.ts`
5. `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts`
6. `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-profile-registry.test.ts`
7. `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-options-builder.test.ts`
8. `projects/chirality-app-dev/frontend/src/__tests__/lib/tool-descriptor.test.ts`
9. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-profile-registry.ts`
10. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/read-tools.ts`
11. `projects/chirality-app-dev/frontend/src/lib/harness/tool-evidence.ts`
12. `projects/chirality-app-dev/frontend/src/lib/harness/tool-path-policy.ts`
13. `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`
14. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`
15. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`
16. `projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_STATUS.md`
17. `projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_run_records/WORKING_ITEMS_RUN_2026-07-20_DAPP50_HEADLESS_PREVIEW_LIVE.md`
18. `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`

## Rejected alternatives and exclusions

Rejected alternatives were a shell or `PATH`-resolved process, an unpinned executable,
partial `modelInputPath` input, importing or reimplementing piping source, a sidecar/network
transport, hidden output files, or widening this read-side tool into proposal/apply behavior.
Those choices would weaken provenance, process isolation, or the ruled per-operation boundary.

No piping, tier-0, pec, apply-class, proposal-transport, provider/network, packaging,
publication, distribution, lifecycle-transition, professional-approval, certification,
sealing, authentication, code-compliance, or solver-truth claim or effect is included.

## Surviving Remaining item

The deliverable remains `IN_PROGRESS`, its Checking Approval SHA is unchanged, and this
separate item remains byte-for-byte:

> Advance the domain engine beyond the currently authorized staged, read-only boundary only through a new owner ruling that names the next tier-0 capability and its verification evidence. Preserve the F-APP-3 stepwise lane, keep apply-class exposure excluded unless separately ruled, and coordinate the bounded contracts in DEL-10-02..DEL-10-05 (governed by D-APP-50 and D-APP-53; gated: new owner ruling).
