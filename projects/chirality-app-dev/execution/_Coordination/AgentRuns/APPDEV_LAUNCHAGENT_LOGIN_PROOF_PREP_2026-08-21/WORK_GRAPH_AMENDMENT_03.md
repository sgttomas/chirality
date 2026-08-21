# Work graph amendment 03

- Reason: N1-R2 completed defect analysis but did not land its promised patch;
  Agent 0 interrupted it to restore development progress.
- Interrupted node: `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-03`; no accepted
  implementation return and no frontend edits attributed to that child.
- Replacement implementation owner: Agent 0 direct bounded Agent 2
  `/root/login_proof_direct_fix`, durably represented as
  `A2-PKG09-LOGIN-PROOF-PREP-DIRECT-01`, with sole write ownership of exactly:
  - `frontend/scripts/run-packaged-launchagent-login-proof.mjs`
  - `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
- Manager posture: `WI-PKG09-LOGIN-PROOF-PREP-02` performs no writes to those
  files while the replacement is active and will validate the relayed sealed
  return against the unchanged activation authority and acceptance criteria.
- Downstream graph remains serial: replacement implementation return -> fresh
  read-only review over 100% frozen product diff -> manager checks and fan-in.
- WORKING_ITEMS retains acceptance/rejection, independent review, full checks,
  DEL-09-04 evidence/state, and package return ownership. The direct dispatch
  does not widen App, package, host, launcher, proof, or Git authority.
