# CHANGE-P1-PKG03 Preintegration Checks

Verdict: `PASS`
Basis: `main@5f124ad80fe84357f6dc33072dc4fbdbeb05d545`
Branch: `codex/sow-p1-pkg03`

## Exact basis and mutation

- Local `main`, local `origin/main`, and remote `refs/heads/main` were equal to
  the sealed basis before branch creation.
- Accepted snapshot `MANIFEST.tsv` reproduces rebound SHA-256
  `9d96e649cd45dc75bbb67abd390271875f3112c060afdc2fafa12efd90fc6f3a`;
  the pre-normalization identity is retained in branch history.
- All 32 legacy source hashes, eight absent live `ScopeOfWork.md` states,
  eight clean-production hashes, and 40 status/control/dependency hashes
  reproduced before mutation.
- Eight ordered commits each contain exactly one deliverable's five manifest
  paths:
  - `3707ca488af3601179318995fd39c9f5c7d3bdce` — `DEL-03-01`;
  - `032e790db00c6d2ebfa3b7b388666fb505466f90` — `DEL-03-02`;
  - `bd90ea581e5ad08d5406d6c20f3989044a2e3cde` — `DEL-03-03`;
  - `8fafbbe3fc900a5bb8aa5d7fee61a8474d6755d0` — `DEL-03-04`;
  - `ac38bd95ebc55ab0ff9350089ece6d6394e07f27` — `DEL-03-05`;
  - `e6526f77396ee05f0e2747c98b07e6a736579a35` — `DEL-03-06`;
  - `95dec4f5aaf11d24e5280ad4123b6c8a9125f7da` — `DEL-03-07`;
  - `17461e2915710b9f146df6cb39df330fa3eb0d69` — `DEL-03-08`.
- Project delta is exactly the accepted 40-row replacement manifest: eight
  clean `ScopeOfWork.md` additions and 32 legacy-file deletions. No status,
  lifecycle, context, dependency, reference, PKG-00, `DEL-01-01`, or other
  project path changed.

## Deterministic and preservation gates

- Eight live targets validate as clean `SOW_V1`; their hashes equal the
  accepted production hashes and all four legacy files are absent.
- Fresh map and parity reproduction passes 234 mappings and 1,966/1,966
  source lines; eight checklist derivations pass.
- All eight finalization reports bind the exact evidence and production
  hashes and mapping counts.
- Replacement and rollback manifests are exact 40-row inverses.
- Fresh scratch apply, target, and inverse-rollback simulation passes 8/8;
  status/control/dependency hashes are unchanged.
- Separate outcomes: schema `PASS`; content/authority `PASS`;
  preservation/containment `PASS`; execution substrate `PASS`.

## Registered checks

- `python3 tools/practitioner_harness/harness.py self-check`: `PASS`.
- `python3 -m pytest -q -p no:cacheprovider tools/practitioner_harness`:
  `264 passed`.
- Agent instructions: 33 files, zero errors and warnings.
- Skill metadata: 44 valid, zero invalid.
- Path anchors: 449 live surfaces, no literal home-directory path.
- Instruction entrypoints: canonical.
- Public-export and Scope-of-Work tool tests: 20 passed.
- Per-commit and live-project `git diff --check`: `PASS`.
- Whole working diff `git diff --check`: `PASS` after the human-directed exact
  56-file EOF normalization and complete transitive manifest rebinding.

No semantic, preservation, schema, substrate, containment, project-check, or
diff-hygiene blocker remains. The pre-normalization blocked state and warning
inventory are preserved at `ce4ea40f2c290eb41b6f9cd29f49d0f54d74a5ca`.
All required remote checks must pass on the exact remote head before merge.
