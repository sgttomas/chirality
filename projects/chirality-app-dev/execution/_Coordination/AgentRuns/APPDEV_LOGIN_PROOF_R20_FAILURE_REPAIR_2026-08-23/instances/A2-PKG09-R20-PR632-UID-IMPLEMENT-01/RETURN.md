# Return — PR #632 UID portability implementation

- Status: `PASS_IMPLEMENTATION_PENDING_TERMINAL_READ_ONLY_GATES`.
- Basis: `4a48aeaede2d050631006f8ff23fb11736752bef`; frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`.
- Sole frontend source change: `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`; `44` insertions / `35` deletions.
- Candidate test: `59,162` bytes; SHA-256 `77ff11055fa5c110001d37784e0a344a7f7874fcc3c69a2b62b5b7722c5e5bd7`.
- Implementation: module-load availability guard plus one `REAL_UID`; all inventoried coherent host-identity values derive from it; exactly four deliberate non-root mismatches use `REAL_UID + 1`; root `0`, session/asid/parser/path/platform/mode semantics, and the sole inert R19 `501` string are retained.
- Local checks: APP-HOLD PASS; ordinary focused `72/72` PASS; `umask 0002` focused `72/72` PASS; exact socket-permitted full suite `1,282` passed / `4` skipped PASS; typecheck PASS; proof-script syntax PASS; static whole-file inventory PASS.
- Immutable controls: R19 fixture exact at `3,049` bytes / `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`; product proof script exact at `56,144` bytes / `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`.
- Calibration: this host runs UID `501`; local passes establish no regression but do not prove the cross-UID class. Linux CI with a different UID is the host-identity arbiter.
- Fences: no delegation, ordinary-sandbox full-suite diagnostic, product/build/package/proof/operator/network/Git action, retry, or out-of-scope write occurred.
- Terminal handling: diff whitespace, containment/index, and candidate-whitespace are deliberately executed after this record freeze and returned out of band without a later evidence edit.

Fresh review must inspect the exact source diff and these immutable instance records. It must retain the CI limitation rather than treating the UID-501 local host as proof of portability.
