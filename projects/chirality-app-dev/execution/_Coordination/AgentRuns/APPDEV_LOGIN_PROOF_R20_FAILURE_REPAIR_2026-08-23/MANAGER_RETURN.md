# WORKING_ITEMS manager return — PR #632 UID source candidate PASS

- Run: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- Basis: branch `codex/app-login-proof-r20-repair`; HEAD `4a48aeaede2d050631006f8ff23fb11736752bef`; parent `74525fb6b34f614c114e59a1bf09d20102fc6aac`; frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`.
- Verdict: `UID_SOURCE_CANDIDATE_VALIDATED_PASS`; ready for CHANGE to create the immutable final frontend-touching source/evidence commit. No build has run in this tranche.

## Diagnosis and implementation

- Read-only diagnosis confirmed the CI-only failure: the coherent mocked UID reached `expectedUid`, while real fixture metadata carried the runner identity. The product ownership guard is correct and unchanged.
- The whole focused test was swept once for UID/GID, launchctl domain, real-path, temporary-directory/symlink, homedir, process, and platform entanglement. No GID or additional real-state path defect exists.
- The sole frontend change is `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`, 59,162 bytes / `77ff11055fa5c110001d37784e0a344a7f7874fcc3c69a2b62b5b7722c5e5bd7`, with 44 insertions and 35 deletions.
- One explicit `process.getuid` availability guard and one `REAL_UID` supply every coherent baseline identity. Four deliberate non-root mismatches use `REAL_UID + 1`; root `0`, non-UID session/parser cases, and the sole inert captured-fixture `501` remain intentional. No `502` or GID constant remains.
- R19 fixture remains 3,049 bytes / `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`. Product proof script remains 56,144 bytes / `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`.

## Validation and review

- APP-HOLD returned ALLOW. Ordinary focused and the single `umask 0002` focused run each passed 72/72. The sole local-test-socket-permitted, external-network-forbidden full suite passed 1,282 with 4 skipped. Typecheck, syntax, static inventory, diff, containment, and index passed.
- Local tests establish no regression but do not prove the UID class on the UID-501 host; Linux CI with a different UID remains the host-identity arbiter.
- Record-hygiene repair cycle 1 removed exactly one surplus terminal LF from four implementation-instance records, recorded complete pre/post lineage, and reran no substantive gate. Candidate whitespace then passed with zero skipped paths.
- Fresh evidence-only review PASS, no finding: activation `bb151ee8e17330c5c38beb8d315a8dbe6ab98d4ad27978f79f27a63d35bc5cf2`; review `6dd494e99d531444322270544272c7d4af414c6debc4afd5ea2486e284f2403b`; return `2cc269da0e475a119610723c3fd2b28d00d46200a117fd129b9478d0c138628c`.

## Handoff

CHANGE must preserve exact App-only bytes, create one final frontend-touching source/evidence commit, and return its 40-character commit and frontend tree. Only then may WORKING_ITEMS run the single frozen-supply verifier/offline pack and R20 revision/package restage. No package, R20/status, TM, receipt, proof, publication, or merge action belongs in this source commit.
