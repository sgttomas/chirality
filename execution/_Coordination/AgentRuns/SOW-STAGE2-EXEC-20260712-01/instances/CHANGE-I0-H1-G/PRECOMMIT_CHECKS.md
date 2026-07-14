# CHANGE-I0-H1-G Precommit Checks

Verdict: `PASS`.

- Basis: local HEAD and `origin/main` both
  `c5abf91b717c0b3901d2a27c578e63976853f8de`; remote main was required to
  match again immediately before commit and push.
- Containment: exactly 245 staged evidence/control-plane paths, all within the
  sealed write scope; zero project paths and zero unrelated paths.
- Manifest chain: seven self-excluding/upstream manifests and 383 bindings
  rehash exactly after normalization. Current principal digests are WORKING
  `096bb62a3e6b02948469479bc761870ee64f6234439aa44d5512af001c349e23`,
  RECON snapshot
  `802656d604adcaed53bdfd6789a79d852da77dc252382387954f369fe603bc74`,
  RECON instance
  `0d88da31ab15f217ddcbad4ef920d1bd629af08767118a8b1c49b7dd102ea77e`,
  and H1 evidence
  `4c9a71df041a37755cd0c291f3013130245b7d44156cc0bb558370c701394df2`.
- JSON: all 51 scoped JSON files parse.
- Live project: the four exact source hashes and `_STATUS.md` hash match the
  accepted W-P1 bindings; `ScopeOfWork.md` is absent; current state is
  `ISSUED`; `git diff HEAD -- projects` is empty.
- Root governance: 33 agent files pass with zero errors/warnings; 44 skills
  pass; 449 path-anchor surfaces pass; root instruction entrypoints pass; the
  20 public-export/Scope-of-Work tests pass.
- Hygiene: all seven initial terminal-blank-line findings were normalized and
  rebound; the final staged diff passes `git diff --cached --check`.

H1 remains unapproved. I1, integration, reissue, reauthentication, lifecycle
action, release, reliance, retirement, and H2 remain prohibited.
