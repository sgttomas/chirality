# Independent Review R1 Disposition

Review: `/private/tmp/chirality-app-v3-app-hold-bootstrap-20260904/reviews/REVIEW_R1.md`

Immutable review SHA-256:
`6242246a747b0001b4ae11f90edf75c0f59151d7c349bce2e6b644d269503120`

Verdict received: `FAIL` — zero BLOCKER, two MAJOR, one MINOR, three NOTE.

## Findings

| Finding | R4 disposition |
| --- | --- |
| M1 — decision-basis digest omitted the conditional ruling and did not bind every later authoritative effect | Remediated. `APPROVAL_EFFECT_MANIFEST.sha256` is now an acyclic owner-approval root over every authoritative leaf, including the packet/register, exact templates and deterministic transform, literal file-set/live-surface contracts, integration contract, and application/rollback instructions. The rendered question states exactly what that root does and does not identify. Only exact owner answer `Yes` can deterministically render the conditional ruling. |
| M2 — proposal tree was collapsed to one row and lacked exact file-set equality | Remediated. `LIVE_SURFACE_MANIFEST.csv` now has one literal row for every proposal file. `PROPOSAL_FILESET.txt` is the exact sorted file set, and `tools/render_approval.py verify` enforces equality among the observed files, file-set contract, and proposal manifest rows. It also enforces that `ARTIFACT_HASHES.sha256` hashes every proposal file except itself. |
| MINOR — complete patch had an EOF whitespace error while evidence claimed strict applicability | Remediated. The stale preservation file was replaced with a newline-terminated current-main record. R4 is checked forward from a clean detached basis with `git apply --check --whitespace=error-all`; CHECKS and return evidence use that exact result. |
| NOTE — runtime semantics were otherwise strong | Accepted and preserved. The core guard semantics were not weakened; all targeted and adversarial regressions are rerun on R4. |
| NOTE — refresh onto current main | Completed at exact basis `77ea8aa68affdb0485134b23d55303c362a312ac` (PR #699 merge); current-main overlap is recorded separately. |
| NOTE — filesystem assurance is point-in-time | Accepted. Candidate and application instructions explicitly require clean isolated checkouts, exact preimages, regular/non-symlink file checks, fresh validation, and remint/review if current state moves. No claim of continuous filesystem integrity is made. |

No finding was waived or silently deferred.
