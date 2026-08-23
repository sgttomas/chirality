# WORKING_ITEMS manager return — PR #632 UID package/restage content candidate

- Run: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- Basis: branch `codex/app-login-proof-r20-repair`; exact source/build HEAD `2ee96958daf997b7a156f020739bde43ca78ebf9`; parent `4a48aeaede2d050631006f8ff23fb11736752bef`; frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- Verdict: `UID_PACKAGE_RESTAGE_VALIDATED_PASS`; ready for CHANGE to create the immutable Receipt-excluded Phase D/E content commit after the terminal candidate-whitespace PASS.

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

## Build, restage, and review

- Frozen-supply verification and offline `desktop:pack` each ran exactly once and exited zero, without download, network escalation, or retry. Native main SHA-256 is `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; runtime CLI SHA-256 is `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.
- Instruction-root evidence is `pass` for the exact 2ee revision and 43 checked files. The packaged R17 guard is intact. Generated packaged-main identity `64b99b9a0c661dc53fe71aa6fed184a52220d8c61b4cc41989149c8a672b2947` is recorded as a fresh, causally unexplained observation.
- R20 is rebound to exact revision `2ee96958daf997b7a156f020739bde43ca78ebf9`; root, label, destinations, and seven procedure blocks remain semantically unchanged. Read-only Step 0 passed with no mutation or proof act.
- Shared hashes: R20 `f3cd377d980606fd71af259d4d24f4cbc52601418a009b8b4d6aa382ba6b5341`; DEL status `b5691adf37e156f6eb487d36d1f3a50cc40733ae4ad3150ae784871d655abacd`; TM candidate `3f5a2ef33053f66031150b41b0f3c9b39b1157a9076442b6a22e8983f3d80734`.
- Fresh build/restage review passed without finding: REVIEW `2077d32fb1a44e82b19f013a8e8961762f40502dd1a90ffb366a08705d8c02ec`; RETURN `bb0055654c205717467cd0d9ab6292c76c1c956023b4bb74d33ff2671e98a415`.
- Unreached governance/control-plane gates passed, including routed affected checks, practitioner self-check, G0–G4, receipt-prior, corpus, APP-HOLD, scope, diff, instruction-root evidence, frontend identity, and empty index.

## Handoff

After the terminal candidate-whitespace gate passes, CHANGE must preserve the exact App-only Receipt-excluded bytes, create one content/evidence commit, and return its 40-character commit. Receipt 193 is authored only after that commit. No proof, publication, push, merge, signing, notarization, deployment, or release claim belongs in this handoff.
