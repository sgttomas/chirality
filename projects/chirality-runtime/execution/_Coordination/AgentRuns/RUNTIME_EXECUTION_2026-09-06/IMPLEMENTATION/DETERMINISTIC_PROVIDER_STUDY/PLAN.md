# Exact App Server deterministic-provider test

Author: OpenAI GPT-6; exact model ID unavailable. Ephemeral Agent 2, role not mechanically enforced. No descendants dispatched. AMENDMENT7 release permits exactly tests/exact-codex-conformance.test.ts and tests/fixtures/response-provider.mjs plus this evidence directory. No vendor execution performed by this author.

## Method

The real accepted 0.149.0 App Server runs against a local deterministic Responses HTTP/SSE peer. The peer replaces the model only; it does not simulate App Server JSONL, tool execution, native descendants, permission enforcement, or terminal events. Native policy comes from prepareCodexNativePolicy, with the synthetic project writable and synthetic broker/foreign canaries outside it. The copied exact binary and empty home are beneath worker-private storage. No account is imported, and the actual account/read result must show no account.

The peer binds only 127.0.0.1 on an ephemeral port, rejects Authorization headers and any endpoint other than POST /v1/responses, caps requests/body/output, and retains only advertised tool schemas, issued-call results, hashes and structural summaries. It never stores full prompts or request headers.

1. Parent first runs discovery-only. Actual thread/turn reaches the deterministic model; the peer returns a terminal message and records the precise tool schemas advertised by that binary. Verify provider configuration and native profile readback using the parent probe before interpreting an action result.
2. Exercise uses only actual advertised function schemas. It requires exec_command or shell_command, then spawn_agent and wait. Required unmapped parameters, another tool dialect, unsupported encoding or missing features fail explicitly. The shell command writes a project canary and tests read denial of two synthetic out-of-root files. Returned outputs must report both denials.
3. The real primary worker calls the real native descendant tool; the child receives a unique user marker. The same deterministic peer directs its real shell tool to perform independent canaries, then completes the child. Primary waits for actual child completion before its final message. Tests require both files and real issued spawn/wait results.
4. All App Server children are process-group terminated and all operational scratch removed. Parent-selected evidence directory receives bounded schemas/results and verdict. A failed scenario is evidence, not grounds to bypass containment or fabricate success.

## Current configuration hypothesis

Custom provider runtime_deterministic: base_url http://127.0.0.1:<port>/v1, wire_api responses, requires_openai_auth false, supports_websockets false; retry counts zero. No key or bearer-token field is configured. An intentionally synthetic model name prevents a claim of using a real model. features.multi_agent=true is a candidate switch which must be verified against exact binary behavior; no current documentation field is treated as accepted 0.149 support without observation.

Official configuration documentation establishes current custom-provider fields, not version-specific conformance: https://learn.chatgpt.com/docs/config-file/config-reference . Official Responses function streaming describes output_item added/done and function_call_arguments delta/done: https://developers.openai.com/api/docs/guides/function-calling . Event framing is implemented as SSE data records around those typed events and completed response metadata. Sources fetched during this study; latest documentation is subordinate to actual exact-payload observations.

## Run contract

Ordinary npm test: one loopback-only fixture check; exact vendor scenario skips by default.

Parent opt-in variables: CHIRALITY_RUN_EXACT_CODEX_CONFORMANCE=1, CHIRALITY_EXACT_CODEX_PATH=<verified accepted binary>, CHIRALITY_EXACT_EVIDENCE_DIR=<fresh evidence directory>. Add CHIRALITY_EXACT_DISCOVERY_ONLY=1 for schema discovery. Run only tests/exact-codex-conformance.test.ts. Parent owns vendor execution release and environment; this author ran fixture-only with the opt-in variable explicitly removed.

Expected evidence class: exact-app-server-deterministic-model, never actual hosted model or account proof. Local provider routing and action-network policy do not themselves prove that the App Server host attempted no other egress. The test records externalEgressEnforcement=NOT_ESTABLISHED_BY_THIS_TEST. Parent must retain the actual execution-envelope/egress evidence and must not label mere configured loopback as a host firewall. No :minimal, broad read grant, raw unrestricted tool fallback or guessed provider approval response is included.
