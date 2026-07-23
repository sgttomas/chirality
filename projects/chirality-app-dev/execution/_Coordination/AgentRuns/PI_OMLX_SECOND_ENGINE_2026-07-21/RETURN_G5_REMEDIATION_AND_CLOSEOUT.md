# G5 Remediation and Closeout Return

**Result:** PASS
**Closeout date:** 2026-07-22
**Integration owner:** primary Codex session
**Actual model:** `gpt-5.6-sol`

## Milestone disposition

The D-APP-72/SCA-APP-002 implementation tranche is complete for the offline production milestone. Claude remains the default supervisor. A governed Agent 0/1 or human-authorized policy may launch an explicitly selected Pi/oMLX Agent 2 child with exactly one Chirality-owned `read_file` tool. The adapter is in-process, exact-model, authenticated-loopback-only, fail-closed, provider-neutral at the runtime boundary, isolated from Pi ambient resources and built-ins, and attributed through canonical session/event persistence.

No automatic engine fallback, remote Pi provider, direct Pi supervisor, Pi-native tool/resource/delegation surface, write/shell/network tool, model alias, or graphical selector was added.

## Independent review disposition

- Security/conformance: `PASS_AFTER_REMEDIATION_BACKCHECK`. All original findings covering typed recovery, tool evidence ownership, redaction, malformed-provider diagnostics, wire failures, supply integrity, and packaged execution are closed.
- Claude/stub regression: `PASS`. All original migration, compatibility-field, TurnEngine neutrality, fingerprint, SPEC, scanner, and mixed-engine isolation findings are closed.
- The final concurrent proof uses a scripted Claude Agent SDK parent attributed as `claude-agent-sdk` / `anthropic` and a real Pi SDK child attributed as `pi` / `omlx`; targeted child interruption does not interrupt or contaminate the parent. Managed delegation independently proves creation and persistence of the bounded Pi Agent 2 launch shape.

## Final validation evidence

- Complete Vitest suite: 106 files passed, 1 skipped; 854 tests passed, 4 skipped.
- TypeScript application and Electron typechecks: PASS.
- Registered harness premerge: Section 8, 8/8 PASS; Section 9, 16/16 PASS.
- Electron 43.1.1 / Node 24.18.0 build and `desktop:pack`: PASS.
- Packaged production-route Pi proof: PASS; Pi 0.80.10 resolved from `app.asar`, authenticated fake loopback discovery/completions, governed `read_file`, canonical persistence, model/package attribution, and no raw fixture or credential in evidence.
- Pi supply-chain verifier: PASS; 140 closure artifacts, SHA-512 enforcement, fixed lifecycle-script allowlist, explicit native/WASM policy, and third-party notice.
- Final secret scan: PASS; 2,714 files, including untracked Pi/oMLX sources and generated proof evidence, zero blocked findings.
- Harness contract dependency lint and instruction-root integrity: PASS.
- D-APP-38 authority corpus v12: PASS; all eight registered sources match and no drift is reported after integration on current `origin/main`.
- Stable-source network policy proof: PASS; three fresh launches, 600 seconds idle observation per run, renderer diagnostics and probe payload observed, and zero non-allowlisted endpoints. Evidence: `execution/PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/Evidence/OI-002_PROOF_2026-07-22_060044`.
- `git diff --check`: PASS.

## SCOPE_CHANGE closure backcheck

- All required SCA-APP-002 action, preview, pre/post coverage, supersession, propagation, summary, and handoff artifacts are present and parseable.
- The registered supersession accumulator reproduces the seven-row cumulative map from the accepted SCA-APP-001 map plus the three-row SCA-APP-002 delta.
- All 15 rows in `Execution_Deliverable_Impact.csv` are `COMPLETED_VALIDATED`.
- The 15 affected `_STATUS.md` records preserve `IN_PROGRESS`, preserve their Checking Approval SHAs, retain unrelated Remaining work, and move only implemented D-APP-72 obligations to dated history/evidence.
- `execution/_ScopeChange/_LATEST.md` points to the validated SCA-APP-002 snapshot and claims no lifecycle, release, signing, publication, issuance, or professional-reliance act.
- Independent closeout consistency checks and `git diff --check` pass.

## Recorded residuals and next human gate

- The opt-in live oMLX gate was completed after the offline closeout on 2026-07-22 with owner-selected `Qwen3.6-35B-A3B-8bit` and an Electron-safeStorage credential. Governed read success, hard denial, targeted interruption, offline-provider failure, and bad-authentication failure all passed without automatic fallback. Redacted evidence is recorded in `LIVE_OMLX_PROOF_2026-07-22.json`.
- Pi's upstream optional provider/platform closure remains large; disk presence grants no runtime authority.
- A remote `npm audit` refresh was not run because sending the repository dependency graph to npm was not separately authorized. Local supply integrity and lifecycle behavior were verified.
- Instruction-root source completeness reports `needs_remediation` while this authorized tranche is uncommitted; packaged instruction-root integrity passes.
- The read-only bridge retains the usual local read TOCTOU residual, and the narrow upstream malformed-SSE diagnostic shim is coupled to the pinned Pi/OpenAI parser strings. Both are recorded, non-blocking residuals.
- The network proof retains its pre-existing CONF-002 OCSP/CRL wording note; all explicit non-allowlisted TCP endpoints were absent.

No release, signing, notarization, or lifecycle issuance is claimed by this closeout or its live-proof addendum.
