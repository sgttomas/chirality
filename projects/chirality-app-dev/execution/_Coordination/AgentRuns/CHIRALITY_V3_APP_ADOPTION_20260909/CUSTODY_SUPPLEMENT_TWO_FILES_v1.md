# Custody Supplement — Two App Adoption Test Files v1

Manager verdict: PASS; both previously unattributed test postimages are now
bound to independent review and may enter final integration custody.

## Subjects and provenance

- `execution/_Reconciliation/References/test_reconcile_authority_corpus.py`
  — SHA-256 `d554422d5a221964e3279073aae6fef301516e1ebac360329415bcea3cda5ab1`,
  1,964 bytes, new relative to base. This is the focused regression for the
  corpus-v21 reconciler repair: each of status, apply, audit, and bump must fail
  without mutation when the current corpus snapshot is incomplete. It closes
  the independently reported `cmd_bump` fail-closed gap.
- `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`
  — SHA-256 `ac8f3938a45995c6a647bc16af28ab799b08f20b36607acbe1a3cbd3937021d0`,
  37,678 bytes, modified relative to base. Its v3 additions cover role-route
  handoff into the still-mounted primary dialogue, same-session continuation,
  project and replay guards, and retained shell composition. Earlier suites
  executed it, but no prior source freeze bound its exact postimage.

## Independent supplemental review

Reviewer `/root/astra_app_second_pass` inspected 100% of both postimages and
base/new-file diffs and returned PASS with no actionable findings. The Python
test passed one test with four command subcases. The exact shell Vitest file
passed 18/18. The review calibrates the shell test's mocked routing separately
from real continuation evidence and the Python test's single malformed-member
fixture; it found no removed or masking assertions.

- review return SHA-256: `e9126045f644d1c9a042bec82939540a0e7d75e2ffeeb95807d3d8cee4fac6cd`
- review manifest SHA-256: `fe528e0e2775cbd15143277c1ee90df69958cacc0ecfbe5ae69d86d0b8550fb3`

Manager backcheck reconfirmed both subject hashes, both review artifact hashes,
the manifest's exact subject identities, reviewer identity, PASS verdict, and
clean diff formatting. No subject or product file changed during review.
