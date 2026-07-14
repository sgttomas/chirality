# RECON-I0-PKG01 Attempts

## RECON-ATTEMPT-001 — canonical production filename

The first full-reproduction invocation finalized clean production bytes to
`prod-a.md` and `prod-b.md`. Finalization succeeded and reproduced the exact
accepted evidence, production, and report hashes, but standalone format
validation correctly rejected the noncanonical filename: a production
contract must be named `ScopeOfWork.md`.

The incomplete RECON-owned snapshot was retained beneath
`instances/RECON-I0-PKG01/attempts/RECON-ATTEMPT-001/`. The harness was
corrected to use verifier-owned `prod-{a,b}/ScopeOfWork.md` paths and is rerun
from scratch. No upstream, candidate, live project, status, lifecycle, Git,
H1/H2, integration, release, reliance, reissue, authentication, or retirement
surface changed.
