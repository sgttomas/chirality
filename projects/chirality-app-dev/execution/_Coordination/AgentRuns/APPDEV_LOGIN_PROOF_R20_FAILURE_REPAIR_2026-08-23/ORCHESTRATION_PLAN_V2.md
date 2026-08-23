# Phase-A orchestration plan v2 — repair cycle 1

Supersedes v1 only for the post-review path; the original plan and review remain immutable evidence.

1. Fresh review 01 is `BLOCKED`, SHA-256 `0134c2db5a9255236171880b95f66a5d93292cd41f71be458dc853dc5636ef76`, on exact findings F-01 through F-05.
2. The original implementation child resumes as the sole overlapping source write owner for repair cycle 1. It changes only the existing three frontend targets and writes only its unique repair evidence.
3. It repairs exactly the five findings, reruns syntax, exact focused Vitest, typecheck, fixture fidelity, whitespace, containment, and index checks, then freezes new hashes.
4. A genuinely fresh reviewer session reviews 100% of the repaired candidate and the five-finding closure matrix. PASS with no actionable finding is required.
5. A second repair/fresh-review cycle is available only if cycle 1 review finds an actionable defect. No Phase B, Git integration, build, package, or full suite is released here.
