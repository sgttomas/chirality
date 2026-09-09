# Chirality v3 Runtime adoption candidate — adapter-successor custody

This append-only handoff supersedes `HANDOFF_V3.md` for exact source custody. All accepted Runtime behavior, R2-1 through R2-7 review evidence, and qualification limits remain unchanged.

Final custody review of two previously omitted App adapter tests exposed R2-8: the production Claude SDK, Anthropic direct, and Pi preparers returned adapter-local successor references, while Runtime correctly requires the frozen target `${basisId}:${basisSha256}`. Direct adapter tests did not cross Runtime validation, so they missed the mismatch. The pre-repair independent FAIL is preserved at `APP_ADAPTER_TESTS_SUPPLEMENT_V1.md` SHA-256 `2795df36a4db1d6bd2b04730fec7a9066949942a219f60b7b4b579cf89403ba6` and manifest SHA-256 `0f2b11182d646f6d2e88c7f8475cab9a3f6f3404344b94491b92cf7d6eb842ee`.

`/root/app_redesign_plan` authored the bounded repair. All three preparers now return the canonical frozen-basis reference. A new controlled integration test crosses `RuntimeService` and `RuntimeMethodService` validation into the actual Claude manager and Legacy-to-Anthropic preparation wrappers. Pi truthfully advertises `durableResume: false`, so Runtime leaves its transition unchanged and does not claim a provider successor; the test separately confirms its callable preparation seam uses the canonical reference.

The corrected source is `SOURCE_FREEZE_V6.json`, SHA-256 `559b0166c5488e8309481ac1f2f46c7270ae7b4415aede9748859ae66a68cc8e`, with 48 source members plus two shared fixtures. It includes the previously omitted Claude and Anthropic test postimages, the Anthropic manager, all three corrected preparers, and the new integration test. All 50 bindings reverified unchanged.

Author and manager focused validation each passed App typecheck and 4 files / 118 tests. Final manager App validation on the exact V6 bytes passed typecheck and the full suite: 189 files passed with one expected skip; 1,996 tests passed with four expected skips; exit 0. Runtime core remained unchanged from its successful build and 772-test final run.

Independent `/root/astra_runtime_second_pass` (gpt-6-astra high, read-only) returned successor PASS with no open findings. It ran the exact 118 tests with Runtime core explicitly aliased to source plus two tampered-preparer negative tests, both rejected by real Runtime replacement validation. `APP_ADAPTER_TESTS_SUPPLEMENT_V2.md` SHA-256 `fa067c79d2bd9f4066ddcd32d2e7fdaca88abc4cefe2c51d9faac272d2208a11`; manifest SHA-256 `0260ae74e83c95d3f555af6d6318c3aa605fc3f0d22f9e29d9369aa30c2b004c`.

Manager validation is `VALIDATION_V6.json`, SHA-256 `98875fedd87ab1edede800e9a81fae63864d7c964b643ce1bd0626e28c32e944`. This remains a reviewed adoption candidate. No staging, commit, project-pin change, execution cutover, release, provider execution, supplier execution, credential access, packaging qualification, network qualification, or native qualification occurred.
