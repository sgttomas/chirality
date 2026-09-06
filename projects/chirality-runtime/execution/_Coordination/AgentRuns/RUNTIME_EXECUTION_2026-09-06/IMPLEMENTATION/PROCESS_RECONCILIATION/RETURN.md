# Descendant observation implementation

Parent AMENDMENT8 released packages/core/src/descendant-tracker.ts and tests/descendant-tracker.test.ts. Implemented bounded metadata-only Darwin/Linux ps census, fixed argv/environment, 2MiB/2s process limits, strict numeric/date parsing, bounded records/deadline and one non-overlapping poll timer. No command lines, executable names or environment values are collected.

Tracker retains observed descendants after reparenting/group detachment. Reconciliation classifies matching owned-group members, detached members, gone identities and changed/reused identities. It exposes failure and stale-snapshot conditions. It never sends a signal, and returns signalAuthority NONE. Existing supervisor-owned process-group cleanup remains distinct. Managers should reconcile before and after their own cleanup, then stop; reconciliation after stop is cached evidence.

Three tests passed, including actual detached descendant discovery and continued observation after its controlled leader exited. The fixture descendant self-terminated on a fixed timer. No PID learned from ps was signaled. Deterministic tests reject changed start identity and cap census; core TypeScript build passed. Production consumer integration belongs to the managers.

Limitations are explicit in every result: unobserved detach between polls; ps start timestamps are coarse and are not PID-safe kill tokens. A failure adds a stale-census warning. Successful observation does not prove that no other orphan exists. A detached survivor blocks complete closure; it is not license to kill unrelated or ambiguous processes.

## Immutable read-scope reassessment

The earlier broad /System,/usr,/sbin,/Library/Apple allowlist was provisional, not a minimum proven by exact supply. Current read-only otool metadata for controlled /bin/sh and /bin/cat names /usr/lib/libSystem.B.dylib only (see system_read_dependencies.log). This supports a candidate /bin plus /usr/lib command readset, not a conclusion about every actual Codex action/helper. The exact supply's earlier default-read diagnostic does not prove restricted native read requirements. Conformance owner has adopted that narrower candidate and must record any additional denied dependency before proposing an explicit expansion. No automatic expansion or new vendor execution occurred in this subtask.
