# Brief amendment 02 — post-commit Step 0 portability

- Disposition: `REPAIR BEFORE REVIEW`
- Applies to: `A2-PKG09-R16-EXECUTE-01`, R16 and executor return only
- Detection: manager/parent pre-review correction

R16 Step 0 must not require `git rev-parse HEAD` to equal
`PROOF_REVISION`. That assertion necessarily fails after this documentation
tranche commits or merges even when the built frontend tree is still exactly
identical. Remove it. Retain the repository-toplevel check and make the
authoritative source gate the required empty output from:

```sh
git diff --stat "$PROOF_REVISION"..HEAD -- projects/chirality-app-dev/frontend
```

Use the already defined concrete `PROOF_PLIST` and `PROOF_SERVICE` in safe,
fail-closed uniqueness checks or remove unused variables. The preferred exact
checks are:

- `test ! -e "$PROOF_PLIST"`; and
- query only `/bin/launchctl print "$PROOF_SERVICE"`, capture its output and
  exit without `set -e` terminating the block, require exact not-found
  classification, and fail if the service exists or the result is ambiguous.

Do not query or touch the default operator label/plist/launcher. Retain root
absence before and after optionless preflight. Prove the repaired Step 0 stays
copy-paste executable from a synthetic later docs-only HEAD whose frontend tree
is identical to `PROOF_REVISION`, without executing preflight or any mutation
inside that synthetic proof. A temporary detached/scratch Git view or an
equivalent read-only test is acceptable; do not commit or change the live
branch. Update R16 and executor return hashes/evidence only. Do not rebuild or
change package identities/status.

The fresh reviewer must independently prove the same post-commit portability.
All other requirements and fences remain unchanged.
