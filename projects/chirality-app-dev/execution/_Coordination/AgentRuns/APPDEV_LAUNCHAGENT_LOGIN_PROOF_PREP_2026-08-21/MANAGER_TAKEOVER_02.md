# WORKING_ITEMS manager takeover 02

- ReplacementManagerInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- Replaces: `WI-PKG09-LOGIN-PROOF-PREP-01`, whose implementation recovery did
  not reach a validated Agent 2 return.
- Package boundary: exactly `PKG-09`, narrowed to `DEL-09-04`.
- Authority/objective/write fences: unchanged from `ACTIVATION.md`; the owner
  `PREPARE-THEN-OWNER` ruling authorizes harness preparation only.
- Live preflight: APP-HOLD `dispatch` is `ALLOW` for `DEL-09-04` at
  `b1876a5e0f0083e10c0c18255cd92ed0079b63a2`.
- Provenance: attempt 1 is preserved as `INTERRUPTED` with no frontend bytes.
  Attempt 2 was stopped before a return to prevent overlapping package writes.
  The unvalidated recovery script/test pair remains only starting input; it is
  not accepted or attributed to either interrupted child.
- Sole current package writer: fresh Agent 2 node
  `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-03`. No other PKG-09 child may write
  while it is active.
