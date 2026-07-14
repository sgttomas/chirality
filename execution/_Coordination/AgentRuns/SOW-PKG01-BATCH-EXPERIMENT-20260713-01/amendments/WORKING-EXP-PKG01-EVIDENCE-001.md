# WORKING-EXP-PKG01 Evidence Amendment 001

Status: `ACTIVE — EVIDENCE-ONLY REPAIR`
Triggered by: `notices/RECON-001.json`

RECONCILIATION correctly found that the package manager's live coordination
message reported a final overbroad parent-manifest assertion, but the terminal
package evidence did not preserve the event in `MANAGER_ATTEMPTS.md` or package
checks.

Re-open `WORKING-EXP-PKG01` only to:

1. record the exact assertion, observed failure, cause, correction, containment,
   rerun, and classification in the durable attempt ledger;
2. update package checks, context/efficiency assessment, RETURN, and STATUS so
   every retained setup/retry event is enumerated consistently;
3. regenerate manager and package snapshot manifests and rehash all bindings;
4. preserve all prior evidence and candidate bytes; and
5. return exact pre/post manifest identities and confirm no substantive gate or
   project/plan/lifecycle state changed.

The correction may write only the existing manager instance and package
snapshot. It may not edit child evidence, candidates, project paths, the
accepted plan/current Stage-2 run, lifecycle, Git, H1/H2, or any excluded path.
If the exact event cannot be reconstructed from retained execution evidence,
return `INSUFFICIENT_EVIDENCE` rather than inventing it.
