# R4.4.6 attempt-2 intake freeze

Status: `IMMUTABLE DERIVATIVE INTAKE — SOLE FRESH VERIFIER GATE`

This freeze binds derivative validation of immutable `returned_r4_4_6/` only.
It does not alter, replace, or extend any prepared packet, execution authority,
or returned evidence byte.

Returned snapshot:

- exactly 20 primary files and 20 `.sha256.txt` sidecars;
- every sidecar-recorded SHA-256 reproduces its paired primary;
- ordered aggregate SHA-256 over all 40 basenames in JavaScript
  `Array.prototype.sort()` code-unit order, emitting exact
  `name|byte_count|sha256\n` rows:
  `480f1817774d2c2a8bc74e7e584674341f9699a2f9e2a9f5132f75050a790cfb`.

| Frozen derivative | SHA-256 |
|---|---|
| `R4_4_6_ATTEMPT2_RETURNED_MANIFEST.md` | `524003693164b372daf1ed017bb56277e202c220168b3eebd3c3a329459fba5a` |
| `R4_4_6_ATTEMPT2_CONTROL_RANGE_INDEX.md` | `a7f5d9d00aa1fbe954e0604494acdbdaa0312984fd553d8c8aef153e600b8f54` |
| `R4_4_6_ATTEMPT2_DISPOSITIONS_AND_CAUSAL_MATRIX.md` | `e5c9a2e30c23add8d0047062bc267e26fce32696e54af96fc0e99c7525504bde` |
| `R4_4_6_ATTEMPT2_INTAKE_VALIDATION.md` | `cbfd133a0b1f54c210009eb6e3504778e7054fe871b1adb0064a0057cc61535c` |

Bound accepted packet/addendum anchors:

- R4.4.6 packet freeze:
  `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89`;
- R4.4.6 packet verifier PASS:
  `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748`;
- cleanup-observation addendum freeze:
  `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf`;
- cleanup-observation addendum verifier PASS:
  `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f`.

Frozen derivative verdict:
`STOP_INCOMPLETE — ENVIRONMENT DEPENDENCY AT C1118`.
Eight D-APP-88 signal-path cells remain `UNKNOWN`. Package and direct-child
identity are supported at launch only; C1119 pre-attach revalidation was not
run. The step-14 stop-condition violation and stale predecessor runbook identity
in the frozen form are explicitly retained. The matching contact-signature
records in GUI stdout and stderr are supporting only. No product or reliance
claim is available. Any byte change to a returned object or listed derivative
invalidates this freeze.
