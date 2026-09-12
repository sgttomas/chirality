# Independent supplier adoption review

Verdict: **PASS**, no actionable finding remains in the five-file adoption v2 candidate. Qualification acceptance and its limits are recorded in `QUALIFICATION_REVIEW.md` beside this file.

Reviewed read-only by `/root/r16_fixture_review` (TASK/Type 2, Astra high, parent HELP_HUMAN) against frozen `/private/tmp/chirality-supplier-adoption-review-mzjdbtsi/adoption-manifest-v2.json`, SHA256 `af5d1e3f20f7cfb55fc7a5d5dc972aa9d3f6aabcf86361ac7ee780518ac94df2`, and the complete adoption diff. No candidate was applied, built, committed or executed by this reviewer.

| File | Accepted candidate SHA256 |
|---|---|
| README.md | `2435da50b93c74c5d7a6357c6eb4c7652540ed30610f2200aafe03aca8566fa3` |
| codex-local-trial.patch | `ce64b7d498dfa7122cffac0df1ad1a96697e64e580c19f97a6fd3ef11b63e20a` |
| source-build.json | `6bef203c1034f50f2be42313a4708a65766100d783f8f47db121bf3d8ccb7cc2` |
| build-invocation.json | `5f7ac9987e58db33ee5454b46dcaa2ee370322bcac7cf51ea8028ede4eb3df8d` |
| build-enclosure.sb | `6f8fada36a25bc332db157f9d31d9afbab4efa11749a83ba57243e206d2a2dfb` |

All five preimages and candidate digests independently match the manifest. The complete maintained patch preserves all prior patch bytes and appends only the five-line literal `/` DIRECTORY read-data addition. All 94 declared build-file identities independently match the actual compiled candidate source. The old 93 `changedFiles` entries remain identical. Parent supplied the successful isolated-index upstream apply check; the reviewer did not mutate that index or rerun application. The patch structure, preserved predecessor bytes, one-file source-snapshot delta and all 94 measured postimages are consistent with that result.

The new source/payload record accurately separates custom-built Codex from the unchanged official rust-v0.149.0 code-mode host and records both raw measured identities. Its 6419 regular-file snapshot, exclusion of 24 Git administrative entries and separately preserved contained `LICENSE -> COPYING` symlink agree with the source inventories. Every referenced evidence digest independently matches. The historical build05 source-build record is recoverable from commit `798507c4712819f77fa868813d11adb799af9726`; a read-only Git object read independently matched its declared SHA256. No historical build03/build04 file is in this diff.

The compiler enclosure is byte-identical to the actual build enclosure. Maintained invocation argv/cwd match the successful build record exactly, including sanitized environment, cloned paths and locked/offline ARM64 dev build. Its v1 stale `PROPOSAL ONLY` status was corrected: v2 records executed success, exact exit/duration and build-result digest while preserving the approved original proposal separately with its exact hash. No retrospective mutation of that proposal is implied.

README and source-build claims agree with the accepted six direct plus six supplier/host shell passes, preserved V6 overall FAIL, separate clean EOF/fresh-worker/exact-thread-resume/README continuation and five filters totaling 14 actual passing Rust tests. The observed shutdown UnknownProcessId diagnostic is explicitly retained. The literal-directory grant is described as permitting root-directory data/enumeration without recursive descendant-file access; no account/protocol behavior change is claimed.

This is a derivative source-adoption readiness review. Parent may apply these exact five candidate bytes under the existing authorization and verify their postimages. Signing, packaging, authenticated Runtime retirement/authority and the next signed-App trial remain separate obligations. No publication approval or bit-for-bit reproducibility is supplied. Reopen only if the candidate bytes or relied-on evidence change.
