# W6 manager receipt — N3

- Runtime child: `/root/w1_del0206/n3_w6`
- Runtime parent: `/root/w1_del0206`
- Launch brief SHA-256: `ea8c8a3a283fa4d5ea4f28bd91180fa8c61fb785451fc49b70fe9d0a453266a7`
- Governing brief SHA-256: `c4d97e2ad8998c67efd407aad2e2a470997159dc538ee0f46f48cf1055a21b7e`
- Verdict: `ACCEPT_FOR_N4`; result `DESIGN_COMPLETE_NOT_EXECUTED`.
- Evidence design SHA-256: `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0`
- Child return SHA-256: `1c1746a05f1afee4886f6057544bf7093fc89d182420da718ead9a9c0a4f2fd2`
- Coverage: 16 requirement rows, 18 restart/replay scenarios, 6 drain cases, 8 terminal shapes, 7 cutover/rollback stages, 8 retained-function classes, and decisions D1-D9.
- Findings: `N3-F01` through `N3-F07`; no repair or semantic adoption.
- Manager validation: hashes reproduce; matrices have required columns; D1-D9 remain explicit human decisions; `DESIGNED_NOT_EXECUTED` is not presented as evidence; tool statement and exact two-file write containment are present. Accepted for N4 fan-in.
- Forbidden effects: none.
