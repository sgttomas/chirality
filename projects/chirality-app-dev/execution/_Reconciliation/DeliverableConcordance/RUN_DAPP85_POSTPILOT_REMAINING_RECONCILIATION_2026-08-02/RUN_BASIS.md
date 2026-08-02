# Run Basis — D-APP-85 Post-Pilot Remaining Reconciliation

Status: `GATE_1_COMPLETE / STOPPED_AT_GATE_2`

This is a derivative, read-only reconciliation package. It changes no
deliverable truth and carries no authority to apply its recommendations.

## Frozen source state

- activation merge / `main` / `origin/main`: `556ae59a34ac2f06ef924d367843a72ea00d1f37`
- D-APP-85 ruling SHA-256: `b7ed59d65fe56acfc0b57ae8843161349548e663894f689f07ec7382eba44e63`
- D-APP-85 packet SHA-256: `56fedf46e067d2bd2edf25eabf259bf2edf4c7d8f69df640775145c41ad7f4d4`
- activation packet basis: `e5fe7e66cca66836f49980f50ad32816c8b96861`
- source-state check: all 18 canonical claim-block hashes equal their packet-preparation hashes; no row is `STALE_INPUT`
- overlap check: no other active reconciliation run or worktree had a declared write target in the C01-C18 `_STATUS.md` population

## Accepted bases and pointers

- decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, SHA-256 `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`
- dependency pointer: `execution/_Reconciliation/DepClosure/_LATEST.md`, SHA-256 `d3c19bfa29bef2294e2f4b69170f09c3cd6b051a6ddaae2faac9db4cbdd03d5f`, resolving to `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`
- scope-change pointer: `execution/_ScopeChange/_LATEST.md`, SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`, resolving to closed-for-scope-change-only SCA-APP-007
- decision register SHA-256: `175d8f8e96c5cf9f67ddfe022bac8184deafe330f985bd8f762e0861af2ab550`
- authority corpus: `docs/DIRECTIVE.md` `e1a3d00b18fa728f0886f036774c4825ad8f65f3245b56b4545da2714a903031`; `docs/CONTRACT.md` `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`; `docs/SPEC.md` `eee520f783ce0161c84bb8c2bd570b7521b3f6926bceea8cde7d387bbc3df990`; `docs/TYPES.md` `998785af3a0f14a87424339ccb6b242b8932f7a572c4336ac47538c64f3e3169`; `docs/PRD.md` `3c357da78277f4c15ecee7cbba6c0a198bc1568b612229eeba63cb1d5972ea7b`; `execution/_Reconciliation/References/AUTHORITY_CORPUS.json` `9aa9dec22dc416d04e385247acbce2dfeb40478f06c54629360497fad6258203`
- D-APP-81 six-relation historical snapshot SHA-256: `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`; not interpreted or changed

## Method pins

- `docs/DELIVERABLE_CONCORDANCE_METHOD.md`: `abf3e78fce606c4557d61cdbfbdb7292a3d858838f6526da6b433d1bcd0ef627`
- `agents/AGENT_RECONCILIATION.md`: `46bca06f907c4da765b1b1177ecd51c6858fdf45bf7620341175c3b847a3e4f7`
- `loop/WORKPLAN_2026-07-18b_app_dev_loop.md`: `d94a01911365773c6d2423880d949738e96f9afd31373bd24c57f1960ebf8ee8`

## Validation basis

Validation ran from an isolated copy under `/private/tmp`; it did not install
dependencies or write generated files in this checkout.

- runtime build and full runtime test suite: `PASS`, 8 files / 64 tests;
- frontend full test suite: `PASS`, 140 files and 1092 tests passed, 1 file and 6 tests skipped;
- Section-9 validator: `PASS`, 16 named checks;
- public-export boundary scan: `PASS`, 814 staged files, no boundary finding;
- PEC opt-in bridge integration: `PASS`, 1 file / 3 tests.

These results prove only covered behavior. In particular, they do not provide
a direct current Desktop/CLI concurrency test, a direct exactly-one-terminal
model-drain recovery proof, or a fresh packaged executable run for C07.
