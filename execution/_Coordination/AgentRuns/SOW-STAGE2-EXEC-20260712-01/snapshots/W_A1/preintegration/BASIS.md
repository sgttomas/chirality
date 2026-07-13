# W-A1 Preintegration Reconciliation Basis

Status: `CANDIDATE DERIVATIVE — RECON-A1-F TERMINAL PASS; PARENT ACCEPTANCE REQUIRED`.

This immutable derivative reconciles the ordinary App W-A1 conversion wave.
It does not replace decomposition truth, deliverable truth, lifecycle
authority, Git history, or the accepted live LEGACY_FOUR_DOC state.

## Frozen authority and source state

- Repository, local main, and origin/main:
  `34b87ec77010035eeaa76f0fa65981ec57e78933`.
- Accepted W-A1 preflight manifest:
  `snapshots/W_A1/preflight/MANIFEST.tsv`, SHA-256
  `2f567949b9632d3ce10435510641ab3ab204b56169295052fc71cd0ef25dbaf4`.
- Accepted preflight decision: `snapshots/W_A1/preflight/ACCEPTANCE.md`,
  SHA-256
  `536a917722618aafd79d0326a682605e2a23e389f929c6a4777f3ddc5a043eda`.
- Migration authority:
  `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.
- Initial reconciliation activation:
  `amendments/A1-RECONCILIATION-ACTIVATION-001.md`, SHA-256
  `a9570f3394bca0556e9f1b6e85830cbd80586a86a55780b5be713867e6787aef`.
- R2 rerun basis:
  `amendments/A1-RECONCILIATION-R2-001.md`, SHA-256
  `94f372c6ad6d21e730f8de5bd7b0c8a6d0cdf2f4cfdcbfc8607acb1e1446ee0c`.

The exact population is 15 IN_PROGRESS, non-pilot, non-ISSUED App members:
PKG-00=2, PKG-01=4, PKG-02=5, PKG-03=4. Every live member remains exact
LEGACY_FOUR_DOC with no live ScopeOfWork.md. Source, status, and control hashes
reproduce from the accepted preflight manifest.

## Accepted package derivatives

| Package | Members | Manifest rows | Manifest SHA-256 |
|---|---:|---:|---|
| APP-PKG-00 | 2 | 23 | `e7e19d4cb25d8ddab52295ccfa06bb7ef7c23b5044a27831196df59a5f8db629` |
| APP-PKG-01 R2 | 4 | 40 | `4924de97675bf8f0ad8bba606d3d5fc171d03445259a5e96eb72c5e002871f62` |
| APP-PKG-02 | 5 | 64 | `72a88b2fb0d3a1882b7e377bb67ba42c34678de1d3864c5e6c6f3013c23ab048` |
| APP-PKG-03 | 4 | 62 | `d335e21b915557e01f3f776d43554a44873d01def8c6c81710aec89dcf09f59b` |

The current aggregate is 189 bindings. The sealed 186-binding package audit
is historical pre-R2 evidence, not current fan-in truth.

## Fences

All project, candidate, package, Git, lifecycle, integration, H1/H2, ISSUED,
release, and retirement surfaces were read-only. This package recommends a
later parent-authorized CHANGE integration only; it performs and authorizes no
integration or lifecycle transition.
