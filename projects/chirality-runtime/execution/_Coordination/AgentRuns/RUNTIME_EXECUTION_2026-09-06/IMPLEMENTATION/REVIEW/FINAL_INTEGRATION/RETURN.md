# Final integrated runtime review

Verdict: PASS for the reviewed implementation and explicitly stated validation limits. All six initial actionable findings repaired. This verdict does not accept live hosted login/model execution or resolve the known command-containment problem.

Reviewer: OpenAI GPT-6, exact serving model ID unavailable; ephemeral Agent 2, role not mechanically enforced. No delegation. All source read-only; authored output only REVIEW/FINAL_INTEGRATION. Prior review packages and their seals remain unchanged.

## Repaired findings

1. Persistent threads: thread/start now requests ephemeral:false. A controlled JSONL fixture writes a thread to disk, its first process is retired, and a distinct successor process resumes the saved thread and produces the second turn. This validates adapter process continuity without claiming the pinned vendor completed it.
2. Role continuity: immutable prepared journals now record rolePolicyDigest separately from standing root/account policy. Broker restart passes the executed role/settings digest; absent or changed recorded digest chooses a new thread. Existing consent identity is preserved. Agent2→Agent0 and changed-policy tests fence reuse.
3. Malformed control shapes: interrupt turnId and approval requestId are scalar-validated before interpolation, returning typed invalid requests without raw coercion errors.
4. Login shutdown: generation-scoped login operations are tracked; shutdown cancels promptly and again after pending starts drain. Cancellation has a bounded grace and reports degraded failure rather than successful closure when the port does not drain. Restart is denied while the stop promise remains active. Tests cover startup race, current login, and blocked cancellation.
5. Safety interruption: exact live-turn interrupt preflight checks project/generation liveness and retains compatibility admission without requalifying launch/account supply. A hosted-boundary failure during live work no longer prevents stopping that work. This exception does not admit another operation.
6. Journal race: immutable terminal metadata decides whether a thread association is authoritative. A late unbound association cannot invalidate the committed terminal or grant resume. Bound associations remain strictly checked. Original actual built-code reproduction produced unreadable committed records in 30/30 races; identical reproduction after repair produced 0/30 unreadable records. Both outputs retained.

## Independent checks

- Initial integrated fixture/socket suite: 109/109 tests, 9 files, passed before repairs.
- Post-repair suite: 134 passed and 1 failed of 135 across 10 files. The failure was a source/dist mismatch: the new test expected the new shutdown-start guard message while package imports still used older compiled daemon code. Original output retained; not suppressed.
- After manager rebuilt current source: all 28 delegated broker tests passed independently. The other 107 cases had passed in the preceding run. No claim of an independently rerun full 135-test pass is made.
- Actual concurrent journal race: 30/30 unreadable before repair, 0/30 after repair. Disposable journals were removed; script and JSON observations remain.

Parent owns final full-suite/typecheck and repository fan-in. FINAL_SOURCE_HASHES.json pins this reviewed source/test snapshot; later source changes require bounded backcheck.

## Accepted implementation behavior and limits

Actual controlled tests exercise client→authenticated broker→private supervisor RPC→worker, distinct standalone service processes, rotating configuration-bound supervisor credentials, generation fences, retirement, role/event metadata and decisions. Hosted standalone validation checks keep the worker-private home/binary disjoint from broker configuration, credentials, journals and registries, and keep the project disjoint from broker storage. The exact supply and fixture issuance paths remain distinct. No fixture is evidence of real provider authentication or completion.

Dedicated Codex login actor permits only account/login operations and allowlisted HTTPS URLs; it cannot initiate a model turn. Real account files remain private and bound by digest. Drift fails launch qualification. No live login, account use, model request, or launchd installation was executed by this reviewer.

Approval decisions are durable runtime evidence with applied:false; no provider network request is automatically authorized by these records. Role evidence is instruction-asserted and the digest binds declared settings, not a mechanical delegation/sandbox proof. The v2 contract is closed and unknown provider authority requests fail; optional diagnostics are bounded/quarantined. Actual model attribution is separate from policy identity.

Parent reports exact accepted-binary offline initialization/config/account-read evidence. This reviewer does not turn that report into hosted turn conformance. The required outer sandbox remains in place. Distinct generated inner command profiles currently fail while identical-profile controls pass; the source-grounded compatible topology is unresolved and may require another implementation iteration. This is not a blanket macOS prohibition and does not justify raw-spawn fallback. Provider-enabled workers do not yet have a proved command-network-off firewall. Text-only hosted validation is also unperformed.

The raw controlled-worker mode remains an explicitly trusted embedding/test seam without filesystem/network containment. Job rendering is still render-only, while standalone service composition now has genuine two-process controlled tests. Scope/product acceptance, compatibility-hold release and App adoption remain outside review authority.
