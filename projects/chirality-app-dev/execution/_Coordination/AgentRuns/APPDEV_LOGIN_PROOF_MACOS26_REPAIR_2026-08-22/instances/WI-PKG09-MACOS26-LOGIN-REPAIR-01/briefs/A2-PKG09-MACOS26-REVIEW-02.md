# Sealed brief — A2-PKG09-MACOS26-REVIEW-02

- RequestedBy: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- ChildInstanceID: `A2-PKG09-MACOS26-REVIEW-02`
- AgentType: fresh ephemeral generalist Agent 2; no delegation
- Mode: evidence-only full review after repair cycle 1; no repair
- Basis: current frozen candidate, first review
  `adc3de73ed0ab46043ad599c9dbac34078c2982a7db9b9c8a7a42ce5a30b64d8`,
  and remediation return
  `c0d35ab67934859fd542eac421d84f9a111876de6f3253f47d859be100dbe3c6`

Read and apply the complete 14-item matrix and all boundaries from
`A2-PKG09-MACOS26-REVIEW-01.md`. Re-review 100% of source, tests, status,
R14, R15, implementation/remediation evidence, and current Git state.

Additionally verify F-01 is fully closed by direct cases for all 12 added
classes: non-Darwin; root UID; process/account UID mismatch; invalid `root`,
`loginwindow`, and `_mbsetupuser` current accounts; setup console identity;
signaled stat; signaled top-level launchctl; trailing domain output; incomplete
top-level braces; and incomplete security-context braces. Confirm each case
rejects without product/install execution, service/mutating launchctl, or
session-root creation.

Independently run syntax, focused Vitest, typecheck, optionless live preflight
with proposed-root absence checks, APP-HOLD, self-check, hashes, forbidden scan,
diff/whitespace/containment, and index checks. Full-suite rerun is optional
unless evidence is inconsistent; validate the retained 1,245-pass/4-skip
record and lack of source change between diagnostic and unrestricted rerun.

Write only `review-cycle-1/REVIEW.md` in this instance. Do not repair or mutate
source/product/proof/operator/Git/shared paths. Return `PASS` or actionable
findings with file/line evidence.
