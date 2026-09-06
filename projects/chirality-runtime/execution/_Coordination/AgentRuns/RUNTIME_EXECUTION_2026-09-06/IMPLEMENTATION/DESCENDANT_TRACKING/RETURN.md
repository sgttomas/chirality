# Descendant tracking integration return — AMENDMENT8

Executor: OpenAI GPT-6, exact serving model ID unavailable; bounded Agent 2, role instruction-asserted and not mechanically enforced. Writes only assigned supervisor/test files and this evidence. No vendor executable, account or provider network used.

## Result

Production CodexSupervisor starts DescendantTracker after spawn and before actor initialize/turn acceptance. It observes while the process runs, samples before existing owned-process-group cleanup, reconciles after that cleanup, then stops observation. A census failure, observed detached survivor, changed process identity or remaining observed owned-group process prevents a successful terminal/clean retirement. The bounded ENGINE_UNAVAILABLE diagnostic carries reason DESCENDANT_RECONCILIATION_REQUIRED, observation/scans/counts, at most 32 detached PIDs, coarse/polling limitations and signalAuthority NONE. No arbitrary detached PID is signalled.

Actor.close deliberately absorbs transport-close errors; supervisor now explicitly awaits its idempotent transport cleanup after actor close, both in the result's finally path and retirement. This ensures a genuine provider terminal cannot hide failed descendant reconciliation and become successful completion. A failed initial census closes the launched child before acquisition returns. Existing account/root/epoch/native-policy and fixture-production boundaries remain intact.

Success still returns the ordinary WorkerResult; it is not a claim that polling observed every descendant. Unobserved detach between polls and coarse ps start identities remain explicit limitations, not PID-safe kill authority. The tracker supplies observation, not a complete process containment proof.

## Validation

`npm run build`: PASS. `npx vitest run tests/codex-supervisor.test.ts`: PASS, 22 tests. New cases use actual JSONL child processes with explicit controlled census seams: a terminal followed by an observed detached survivor fails wait/retire/close; the owned child is verified gone; a clean observed closure succeeds; and a census failure blocks acquisition. No actual detached foreign process is created or signalled in these integration tests. Utility-owned tracker tests remain sibling evidence. Prior named-policy/readback, role, recovery, timeout, crash and cleanup cases remain passing.

Controlled config/read fixtures now include remote_plugin:false, matching the actor's updated exact observed readback requirement. Native compiler direct invocation is honored verbatim. The prior NATIVE_POLICY evidence's app-server-subcommand description is superseded by the exact dedicated-binary finding recorded in this brief; historical sealed bytes remain unchanged.

## Handoff

Pre/post source snapshots and output hashes preserve this integration. Sibling basis hashes identify the tracker, compiler and actor at closeout. Parent owns private-wire delivery of the sanitized reconciliation diagnostic, ProcessSupervisor fan-in, full validation, independent review, actual probes and any further reconciliation. No provider or hard-containment acceptance, lifecycle advancement or hold release is claimed.
