# Fresh reviewer return — R1

- RunStatus: `SUCCESS`
- Verdict: `FAIL`
- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-REVIEW-01`
- TaskSkill: `software-code-review` v1
- WriteAuthorization: read-only; no file, index, or external state write.
- Frozen identity: `PASS`; 47/47 file hashes and aggregate `eeabad67107add91cea891b03c63d89c940244155d1d240082223119de80983c` match.
- Coverage: 9/9 product paths and 38/38 evidence/control paths, 100%.
- Parseability: all 15 JSON and 3 NDJSON subjects parse.
- Scope validation: `PASS`, zero violations.

## Actionable findings

1. `BLOCKING` — `frontend/scripts/run-network-policy-proof.mjs` captures only
   Next/Electron parent PIDs, not Electron descendants/network-service PIDs,
   and treats `lsofExitCode: 1` plus zero endpoints as proof of zero egress.
   Final evidence had four unusable/empty snapshots while an allowed
   Anthropic renderer fetch occurred. Enumerate the descendant tree, fail
   closed on unusable capture, test observed child traffic, rerun, and
   recalibrate the claim.
2. `BLOCKING` — `frontend/scripts/run-packaged-security-proof.mjs` evaluates
   `daemon.captured()` before credential store/status/remove, so operation-time
   fixture leakage is absent from the scan; it also does not recheck oMLX
   isolation after Anthropic mutation. Scan complete closed streams/artifacts
   after operations and recheck oMLX after store/remove, with negative tests.
3. `BLOCKING` — packaged GUI/daemon cleanup errors are swallowed. Propagate
   cleanup failure, record confirmed shutdown, and require it in the PASS
   predicate.
4. `ACTIONABLE SECURITY FENCE` — source proof inherits a live
   `ANTHROPIC_API_KEY` when present. Scrub all provider credentials and use
   only explicit non-secret fixtures where needed.
5. `ACTIONABLE EVIDENCE CONSISTENCY` — first source attempt used owner Electron
   user data while the implementer return globally claimed no owner-user-data
   mutation. Preserve the failed attempt and issue a calibrated correction or
   supported audit; all reruns must isolate user data from process start.

## Accepted blocker and disposition

The reversed production API-key environment precedence is correctly separate,
executable as a self-expiring `it.fails` case, and held outside this node under
DEL-02-05 R03 / DEL-04-05 RQ-001. Both deliverables and Remaining items remain
open. This accepted blocker does not excuse the five candidate findings.

Manager recommendation: do not land the frozen candidate. Serialize bounded
proof-glue/evidence remediation, rerun affected/full/host gates, freeze a new
complete identity, and dispatch a new fresh 100% read-only review.
