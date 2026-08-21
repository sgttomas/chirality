# Work graph amendment 05

- N2-R1 post-remediation review verdict: `FAIL`, one actionable P2.
- Prior P1 fixes are accepted as effective: mandatory source revision and no
  bootout without exact proof-job identity.
- Remaining P2: launchctl parse ambiguity or process-executable inspection
  failure safely avoids bootout but can record `jobMutationRefused: false`
  because that flag depends on an exception-message prefix. Evidence must
  truthfully record refusal whenever identity was not proved and mutation was
  therefore withheld.
- Dispatch fresh exact two-file remediation node
  `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-02`, followed by a fresh full-diff
  read-only review. No concurrent writes; all other authority/fences unchanged.
