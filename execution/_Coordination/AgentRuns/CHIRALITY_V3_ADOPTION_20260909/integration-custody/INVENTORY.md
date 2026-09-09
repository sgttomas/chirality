# Chirality v3 integration custody inventory

Date: 2026-09-09
Integration checkout: `/private/tmp/chirality-v3-adoption-20260909`
Branch: `codex/chirality-v3-adoption-20260909`
Base: `c16812685831a1cae3d44bf478d08b033c605c3a`

## Custody posture

This record inventories the reviewed lane subjects before final integration freeze. It does not accept governed content, qualify a supplier or native adapter, authorize publication or release, or authorize a merge. Source files were not edited, staged, committed, or pushed while preparing this inventory. Existing worktrees remain preserved.

The user's approved Chirality v3 implementation plan authorizes preparation and integration of the named candidate. Exact governed acceptance remains distinct from the standing ordinary Git grant and from any later merge, publication, release, supplier, credential, account, binary, or native qualification decision.

## Effective overlay status

Only subjects marked effective below may contribute to final staging readiness. Historical PASS evidence proves its exact predecessor only and is not a claim about later source bytes.

| Lane | Effective subject or state | Review state | Final-freeze status |
|---|---|---|---|
| Root | `ROOT_SCOPE_FREEZE_V7.json` overlaid by `ROOT_SEMANTIC_SUCCESSOR_V1.json` SHA-256 `8669df0d1b2ab639e0e3d1352843130aabf8d88ab8050ed9f5169b022d9afad5` | Astra Section 2 PASS; exact evidence below | Effective and source-stable |
| App authority corpus | `CORPUS_V21_FREEZE_v2.md` SHA-256 `31d9269c57a6722ab5615883f373bfa0d1bda72732acf2b149d2def53271670c` | Independent PASS; exact evidence below | Effective and source-stable |
| Runtime | V5 is superseded. Effective `projects/chirality-runtime/execution/_Coordination/AgentRuns/CHIRALITY_V3_ADOPTION_20260909/MANAGER/SOURCE_FREEZE_V6.json`, SHA-256 `559b0166c5488e8309481ac1f2f46c7270ae7b4415aede9748859ae66a68cc8e`; 48 members plus two exact Root fixtures | V4 Astra review plus the engine supplement remain applicable; R2-8 successor review `APP_ADAPTER_TESTS_SUPPLEMENT_V2.md` SHA-256 `fa067c79d2bd9f4066ddcd32d2e7fdaca88abc4cefe2c51d9faac272d2208a11`, manifest `0260ae74e83c95d3f555af6d6318c3aa605fc3f0d22f9e29d9369aa30c2b004c`, PASS. Manager V6 validation `98875fedd87ab1edede800e9a81fae63864d7c964b643ce1bd0626e28c32e944`; handoff `c6895aca133748d8930fc590cce45abbb15f73c2d513d11f93eefeadc49bfec0`; App full 1,996 PASS/4 expected skips plus typecheck; Runtime 772 PASS/14 expected skips remains applicable | Effective and source-stable |
| App product | V6 is superseded. Effective `projects/chirality-app-dev/execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/UI_SOURCE_FREEZE_v7.md`, SHA-256 `240a974e9e6a0c9317ea77b9588997adf2d03b613bfd78595ee1a8c3c5405a80`; 48 postimages | Custody rehash 48/48 exact; Astra Section 4 PASS at `review-v7/RETURN.md` SHA-256 `0bbe887d2d6a9fe4c3324a1083a99f206daebf544b80ab367e71519dd8250c94`, manifest `483f6abaaa0cf5151e4e4e185ffe7b87d4538c6ac8ee36bc0d5a47b9baa38997`; manager validation `UI_VALIDATION_v7.md` `3d5ec4d51138111f67a8e8cf5bf07680a0511b1d14acc54c4dd67578997b549e`, return `45bb160dc11fbfea84be9b03eea240317d3464e1de2069c439c48474109fed89`, handoff `ac4c280882e74071fc588caef7d137b959e3492083190e75a48d09f03532f289` | Effective and source-stable |
| Distribution | V10 distribution bytes remain unchanged; effective reliance anchor is `distribution/subject-v12.json`, SHA-256 `3d494992fbb033f68b623a2124ea681dd12673e83fc3b5eedf83ae264f1e9c8d`; 19 members and 1,104 export rows | V12 independent PASS: return `d3e853c8c188490a27c6305029358018018aec95c981468cc7b8af84d0fc1719`, checks `2a87a4332d2d0e7203ed5d3a5a47de4708f50c478936fae89e496b8e55452bb0`, manifest `9e6bdec73d5d932845c9fa3f1111fa58d10df77c18dd4e307f98e9c79a31f5a1`; 19/19 exact and all V6/manager/review anchors verified | Effective and source-stable |

## Preserved reviewed predecessors

| Lane | Exact historical subject | Subject SHA-256 | Independent evidence | Disposition |
|---|---|---:|---|---|
| Root V7 | `ROOT_SCOPE_FREEZE_V7.json` | `7f5ef062acd1e3ea63bc4fa3c5e61ad534cd24823c4b18ee28b9cfe1ff1c4ff8` | `review-v2/RETURN.md` `2fdf2594ea9953371cd6fa2ec25557074f7cde2c4fbeadc13e2fbf3bdfbb69be` | Preserved; superseded only for the 30 semantic-overlay paths |
| Runtime source | `projects/chirality-runtime/.../MANAGER/SOURCE_FREEZE.json` | `b4a1ecd017321111c3a24a550d438f2429827d66f217439a17e02f87ce125af0` | `runtime-context-review-v2/RETURN.md` `c7766b2d0c9e94ca68c3c3068e535666d21c80843870404430284924a25fcbf1` plus supplement below | Preserved; predecessor-only reviewed members remain in the effective union |
| App backend | `runtime-context-review-v2/APP_SUBJECT.sha256` | `657190f5299c39ee90e576251a5cff570be4fb1f8a1740322bd7e927d0299670` | `APP_RETURN.md` `4e6e1531c9fa33a88c07fbde5814973a9de323af4b5a1accee7f843554b8c47e` | Preserved; predecessor-only reviewed members remain in the effective union |
| App UI V4 | `UI_SOURCE_FREEZE_v4.md` | `a74885a9b11870d1b22a1107f229c9904ce20942663cfea60dfd16500330bdb9` | `review-ui-v4/RETURN.md` `18ed4fbdba8554dee5a5ac9575611b2a9c633b053ad3d22fab1b48323ca881aa` | Preserved; predecessor-only reviewed members remain in the effective union |
| Distribution V9 | `distribution/subject-v9.json` | `4fb22e1a2925b82b2705e3bb9370639b669cfb7599e97c2475906f88ea60e1ee` | `distribution/review-v9/RETURN.md` `f158e09a47fa4f3ecfb786f577c75aaf949c4c67eba9c09cd9f082f27e77d5ec` | Preserved; V10 is the effective export rebind |

## Closed predecessor attribution gaps

### Runtime and App supplement

The Runtime manager freeze contains six relevant changed files that are not members of the declared Runtime independent-review subject:

- `projects/chirality-runtime/package-lock.json`
- `projects/chirality-runtime/packages/contracts/package.json`
- `projects/chirality-runtime/packages/contracts/src/index.ts`
- `projects/chirality-runtime/packages/core/package.json`
- `projects/chirality-runtime/packages/core/src/index.ts`
- `projects/chirality-runtime/tests/runtime-daemon-signal.test.ts`

These are dependency, public-export, catalog-export, and daemon-test glue for the predecessor implementation.

The exact seven-path supplement covering these six files and the App integration test below passed independent review:

- subject SHA-256 `fe91df552fb8f5bf36facf5186b9085203d0eb6e3bfa28322f596f8799494802`
- `runtime-context-review-v2/supplement-v1/RETURN.md` SHA-256 `47e481e9f90973cd9f0ef0faaae6027116e0128676a2c123d475af3c85dafd4d`

The reviewer found the dependency pins, public exports, daemon test adapter wiring, and assertions consistent and unweakened. This review-attribution gap is closed for the hashed supplement subject.

### App integration test supplement

`projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` was absent from the earlier App backend, App UI, Distribution, Runtime, and Root reviewed subjects. It is now covered by the exact independent seven-path supplement recorded above; this attribution gap is closed for that hashed postimage.

### App authority corpus successor

The App authority corpus successor is frozen at:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_FREEZE_v1.md`
- SHA-256 `c26ce2f53b19f80a2bf097388e71f8917eab0fcb07f919899718c986263ffa6d`

Its bound author artifacts are:

- `CORPUS_V21_CANDIDATE.md` SHA-256 `f8a21ca9ac5b3fa96edaf38e870bad0754d34dea33e73b4abf0a3ca322e3e080`
- `CORPUS_V21_REFERENCE_MANIFEST.sha256` SHA-256 `e537d15e84e6c61f91704d1cab5055804cae2fec0d2abfda631f5a20a08910f4`

The freeze records the expanded workflow authority pins, including substantive resource bytes. `projects/chirality-app-dev/AGENTS.md`, the reconciliation corpus files, project coordination record, and deliverable reference files remain in this corpus lane.

Independent review of this preserved v1 freeze returned a blocking verdict:

- 50 of 52 frozen deliverable `_REFERENCES.md` postimages contain nine relevant v21 members, while DEL-10-01 and DEL-10-03 contain all 12. Review confirmed this preserves the accepted relevance model: D-APP-45 adds domain-engine only to those two deliverables, while D-APP-38 and ISSUE_READINESS require reconciliation of each deliverable's actual authority rows. The defect is `_README.md`'s overbroad claim that every deliverable records both workflow closures. It must describe the six common documents, complete software closure, and domain-engine closure where that method is an authority reference, with a deterministic conditional-closure audit/test.
- malformed-current rejection is incomplete: `status`, `apply`, and `audit` fail without mutation when a current v21 member is absent, but `bump` succeeds and appends v22 because its path omits current-snapshot validation.

The v1 corpus subject is therefore retained as a failed reviewed predecessor. The corrected successor is `CORPUS_V21_FREEZE_v2.md`, SHA-256 `31d9269c57a6722ab5615883f373bfa0d1bda72732acf2b149d2def53271670c`. It preserves conditional relevance, narrows the README claim, clarifies the overlapping alias/row accounting, and adds malformed-current `bump` rejection.

Independent v2 review returns PASS with no open findings: `review-corpus-v2/RETURN.md` SHA-256 `c31e02f5a595e96b207d0749ffac7d2109248cf19299331fa23ed9792b27e958`, `CHECKS.json` SHA-256 `df8cacd67263c40e7b1a7d9ce8fd7bac8309d4df05c4eee0f76ecdfcbd372d48`, and `MANIFEST.json` SHA-256 `16df98af28d9a152ea0a0d4d231311e51a3dd6d6d69b2d8ddb0009c657b67865`. The corpus review hold is closed for the exact v2 subject.

The 30-file Root semantic successor intersects none of the 12 v21 authority-corpus member paths. A direct post-review hash check confirms all 12 live v21 members still match their recorded hashes, so the semantic successor does not reopen the corpus v2 review.

## Independent semantic-quality successor

The added independent semantic review required bounded corrections to scope-change candidate activation, reusable skill eligibility, current change routing, canonical skill callsites, legacy normalization, catalog containment/parsing, DOMAIN HTML authority wording, and candidate-pointer validation. Root V7 remains preserved as a reviewed historical subject.

The corrected 30-file Root successor is frozen at `execution/_Coordination/AgentRuns/CHIRALITY_V3_ADOPTION_20260909/ROOT_SEMANTIC_SUCCESSOR_V1.json`, SHA-256 `8669df0d1b2ab639e0e3d1352843130aabf8d88ab8050ed9f5169b022d9afad5`; 30/30 postimages match. Manager validation passed 59 focused tests, 514 Root-owned tests plus 48 subtests, 71 workflow packages, eight canonical skills, a fresh 79-method index, three unmodified skill quick-validations, and `git diff --check`.

Terminal independent Section 2 review returns PASS: `astra-second-pass/root/REVIEW_V2.md` SHA-256 `bdd213c929e5214f8b80d94143499d728ee85b99abc011339e0438b9d3db7f09` and `EVIDENCE_MANIFEST_V2.json` SHA-256 `984039e2bff6ad8bdac095f82cb0cf7897f09f24104abc95613974085451dcd7`. The reviewer closed SEM-1 through SEM-5 and ROOT-2P-1 through ROOT-2P-6, ran 513 tests plus 48 subtests and 28 deterministic probes, and verified 370 source hashes and 107 freeze/reference bindings. Runtime semantic agreement and the distribution rebind remain separately owned.

## Supplemental App governance custody

The App project `AGENTS.md` and `_Coordination.md` postimages are independently reviewed and exact. Review return SHA-256 `26ea0c30c7355d4a1d22d3c41c4e7385a21f39fb4af50689e21881ea99481ba2`, manifest `a6bec2d2556f0ead2c1629ec7dd7af2cf202810a1bf916beb75d824d1767d284`, and manager custody `c7c940a5a0bcfce62802619afb52214041f4e49f33a885010890bb5665d58c4d`. The inherited `_COORDINATION.md` wording that treats a newest workplan as operative remains a nonblocking observation because `loop/LOOP_INIT.md` has higher entry precedence; optional cleanup remains outside this adoption tranche.

## Exclusions and preservation

No `pnpm-lock.yaml` or pnpm workspace artifact is present in the current changed-file inventory. Any unrelated Runtime pnpm lock/workspace artifacts that appear later remain excluded and preserved. Runtime's changed `package-lock.json` is not excluded: it is an explicit member of the Runtime source freeze and records the production YAML parser dependency.

Evidence packets, superseded freeze records, and historical instructions remain preserved. Final staging must be driven by a successor exact integration manifest after all gaps above close; it must not infer source membership from `git status` alone.

## Final custody state

All Root, Runtime, App product, App corpus, distribution, and supplemental source lanes have terminal manager and independent-review evidence. The exact integration union is recorded in `integration-custody/STAGING_MANIFEST_V1.json`: every changed source path has a subject owner, while duplicate captures, generated fixtures, build output, and superseded nonterminal packets remain preserved outside the selected evidence set.

No source file is unattributed. Staging, commit, push, and PR creation remain pending parent inspection of the machine manifest. Governed adoption acceptance, merge, publishing, release, supplier, credential, account, binary, packaging, and native qualification remain separate.
