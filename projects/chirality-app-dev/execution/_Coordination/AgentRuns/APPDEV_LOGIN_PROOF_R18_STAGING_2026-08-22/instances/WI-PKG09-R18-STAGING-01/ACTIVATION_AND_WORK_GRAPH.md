# Activation and work graph

- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- InstanceID: `WI-PKG09-R18-STAGING-01`
- PackageID / selected deliverable: `PKG-09` / `DEL-09-04`
- AcceptedBasis: `166efa82748133e90674be62304b81f8a0a8c1b4`
- Objective: exact-merge offline unsigned rebuild and documentation-only R18
  staging, retaining `IN_PROGRESS`/unproved state.
- Pattern: `TERMINAL_FAN_OUT_IN`, selected by explicit owner direction.
- Dependency edge: executor return and manager freeze precede fresh review.
- Integration owner: `A2-PKG09-R18-EXECUTE-01` for R18/status/package/evidence.
- Review owner: `A2-PKG09-R18-REVIEW-01` for its unique review record only.
- Escalation: cache miss/network attempt, basis drift, existing root/plist/job,
  package or check failure, write-boundary breach, procedure ambiguity, proof
  mutation, or any hard-fence contact.
- Return: exact package identities and hashes, selected label, check matrix,
  changed paths, blockers/reruns, derivative status, and fresh-review verdict.

The graph is frozen before dispatch. Agent 2 children may not delegate.
