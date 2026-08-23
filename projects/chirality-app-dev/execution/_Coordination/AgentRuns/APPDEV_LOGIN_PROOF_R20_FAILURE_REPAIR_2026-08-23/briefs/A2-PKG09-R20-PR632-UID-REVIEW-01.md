# Sealed brief — fresh PR #632 UID-portability source review

- RequestedBy: `WORKING_ITEMS` instance `/root/node3_pkg09` under HELP_HUMAN.
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-UID-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-UID-REVIEW-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 review mode; role/non-delegation instruction-asserted. Do not delegate.
- Objective: independently review the complete diagnosis and frozen test-only UID/host-identity portability candidate. Do not repair or rerun substantive commands.
- AcceptedBasis: exact branch/HEAD `codex/app-login-proof-r20-repair` / `4a48aeaede2d050631006f8ff23fb11736752bef`; Amendment 11; plan/graph v12; accepted diagnosis/disposition; implementation brief; frozen implementation/repair-cycle evidence.
- ReviewWriteScope: only `instances/A2-PKG09-R20-PR632-UID-REVIEW-01/`.
- Matrix: independently re-trace UID-to-real-metadata dataflow; inspect every whole-file inventory row; prove the single `REAL_UID` covers every coherent baseline route/text/assertion; prove deliberate non-root mismatches use `REAL_UID + 1`, root `0` and non-UID session/parser values are retained, and the remaining literal `501` is only inert captured-fixture service text. Check explicit unavailable-`getuid` failure. Confirm no GID/real-path/symlink/homedir finding was omitted and no product weakening/change exists.
- Immutable controls: focused candidate 59,162 bytes / `77ff11055fa5c110001d37784e0a344a7f7874fcc3c69a2b62b5b7722c5e5bd7`; R19 fixture 3,049 / `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`; product proof script 56,144 / `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`.
- Evidence matrix: ordinary focused and single `umask 0002` focused each PASS; sole local-socket/network-forbidden full suite PASS; APP-HOLD/typecheck/syntax/static inventory/diff/containment/index PASS; CI-only UID proof calibration accurate; four-record EOF repair is exactly one LF each with correct reconstruction; terminal whitespace PASS.
- Permitted checks: read source/evidence; compute hashes/counts; inspect Git diff/status/index; recover gzip logs read-only; run static syntax/JSON/whitespace checks that do not rerun product/test gates. Do not run focused/full tests, umask, typecheck, syntax, APP-HOLD, supply/build/package/preflight/proof/network/operator/private-root/Desktop actions.
- Verdict: PASS only with no actionable finding. Otherwise return exact finding severity/path/line/evidence and stop; do not repair.
- Outputs: `ACTIVATION.md`, `REVIEW.md`, and `RETURN.md` with exact hashes and verdict.
- Git fence: no stage, commit, fetch, push, PR mutation, rebase, force-push, or merge.
