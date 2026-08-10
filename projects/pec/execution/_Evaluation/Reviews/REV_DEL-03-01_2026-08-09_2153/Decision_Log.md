# Decision log — DEL-03-01 exact-byte acceptance

1. Confirmed the serialized predecessor pointer was
   `REV_DEL-02-07_2026-08-09_2151`.
2. Reproduced exact DEL-03-01 SOW SHA-256 `564955235aeab…` before any review
   write.
3. Ran the PEC `promote` reliance-hold preflight; result `ALLOW`.
4. Applied the owner's `ACCEPT_EXACT_BYTES` ruling to this exact SOW only.
5. Recorded the SOW as the accepted current production contract and preserved
   RF-001/RF-002 `REVISE / RESOLVED`.
6. Preserved Gate 5 unentered and lifecycle `INITIALIZED`; changed no product,
   status, dependency, source, unrelated review, release, reliance, or Git
   state.
