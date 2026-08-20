# CHANGE handoff — API-key environment-precedence repair

Terminal state: **PR-CI green; owner merge pending**.

- Branch: `codex/app-api-key-precedence-20260820`.
- Stacked PR: `#589`, base
  `codex/app-packaged-security-proof-20260820` at
  `6710ee6354debc201f6a454e2802897026cd4b38`.
- Dependency / merge order: merge PR `#586`, then PR `#589`; this tranche did
  not modify the predecessor branch.
- N1 PKG-04: `45336238247f304bcdd3c718be2b1f8dcff6c387`.
- N2 PKG-02, including reviewed closeout whitespace remediation:
  `4d1d927fa4a8df2672534dfd1206716c1e6cd7d4`.
- N3 PKG-09: `675b87a56c4f2fbdd9aef332600b3088dd543738`.
- Shared fan-in: `432577fcde3796933f30d9d10df86094d5282f7b`.
- Fresh integrated Review 03: PASS, zero actionable findings; frozen reviewed
  subject 98 paths at
  `7ea308cf90bac02a7c439c71d0f01d2024ecee2a90c1fc16cfd1f4fd95bc1959`.
- Complete landed candidate: 112 paths after the N2 closeout remediation;
  candidate-wide whitespace, JSON parse, containment, product identities, and
  APP-HOLD reliance pass.
- Packaged proof: PASS, subject `1623b297…b4ce2`; secret scan 5,868/0.
- Initial PR CI at the shared fan-in commit: governance Harness
  `32398779013 / 96521728803`, Harness pre-merge
  `32398778692 / 96521729491`, and unsigned macOS artifact
  `32398778725 / 96521727665` — PASS. See `CI_ATTEMPT_01.md`.

The selected API-key precedence and packaged-security/network residuals are
closed. DEL-02-05, DEL-04-05, DEL-09-06, and DEL-09-04 remain `IN_PROGRESS`;
lifecycle, Checking Approval SHA, dependencies, F-APP-2, owner-machine,
signing, notarization, distribution, publication, and release fences remain
unchanged. No merge occurred. Next owner action is the declared stacked merge
order.
