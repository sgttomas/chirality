# Exact offline probe adapter return

API: `probeExactCodexWorker({executablePath, privateDirectory})`. Calls exact verifier, constructs a fresh private child scratch under the existing canonical owned0700 directory, installs observed PROBE_CONFIG.toml bytes and a sandbox-exec network/write/home-read/securityd-deny envelope, revalidates supply immediately before launch, and invokes only the observed initialize/initialized/config-read/config-requirements/feature-list/account-read(refreshToken:false) sequence. No thread, turn, login, network or signature operations. The already recorded signature finding remains attached to the sanitized supply descriptor.

Every JSONL response must match the outstanding fixed request ID and response shape; server requests are never executed. Unknown notifications cannot authorize anything and are discarded. Process output, per-response time and whole process lifetime are bounded. Teardown kills the process group and removes scratch after process close. Returned evidence consists only of method statuses, auth-required boolean, exit/signal, stderr digest and exact supply identity; no account/config contents, token or home contents are serialized. `hostedTurnAvailable` is unconditionally false: an offline readiness probe cannot authorize hosted execution.

`runControlledCodexProbeForTests` is explicitly named and returns controlled-fixture evidence, without a production supply field or offline containment claim. It cannot influence exact verifier issuance or production executable identity.

Validation: whole workspace typecheck PASS. Five focused tests PASS (4.136 seconds): actual fixture process exchange and cleanup, exact-supply rejection of fixture executable, protocol rejection without readiness inference, malformed/unsolicited/flood rejection, alias refusal and actual silent-process timeout/cleanup. No exact vendor invocation performed by this child; parent was notified of callable API for coordinated positive execution.

Limits: macOS arm64 only for exact probe; path-based launch retains verifier-documented post-revalidation race. Renderer/daemon broker wiring is manager-owned. This probe does not establish production two-job launch, hosted-turn conformance, authentication acceptance, compatibility-hold release or deliverable acceptance. Group teardown does not claim OS-wide containment of a deliberately escaping process.

Author: OpenAI GPT-6, exact serving model ID unavailable; bounded Agent2 role not mechanically enforced, instruction-asserted, no descendants.
