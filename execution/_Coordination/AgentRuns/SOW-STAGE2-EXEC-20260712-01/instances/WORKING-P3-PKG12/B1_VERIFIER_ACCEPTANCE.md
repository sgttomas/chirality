# PKG-12 B1 Replacement Verifier Acceptance

Status: `ACCEPTED PASS_UNCHANGED`

The authorized fresh replacement `VERIFY-B1-R1` independently returned
`PASS_UNCHANGED` for all five members: 171/171 mappings, 1,737/1,737 physical
source lines, 25 replacement rows, 25 inverse rows, five simulations, 35/35
negative probes, and 7/7 registered checks.

Frozen bindings:

- `STATUS.json`: `f5191b4406a6971319029797d4746b98d8fadd0c13442ba34525a4bfbb861cb3`
- `RETURN.md`: `88e628ff06509477f830e68bc2b8aeb539ec9ab94e920120dc8840a55dee8001`
- self-excluding `MANIFEST.tsv` (244 valid entries):
  `fadfb2f1f91fdcedd208d285cd90ec7eaa154c3bf1b83ed6229bca04086d26bc`

Parent validation reproduced all manifest entries and confirmed the 112-command
ledger contains zero target beneath prohibited author or failed-verifier trees.
Candidate bytes and 45/45 live bindings remain unchanged; candidate/project
writes, blockers, unknowns, waivers, and repairs are zero. The initial blocked
verifier remains excluded from accepted fan-in.
