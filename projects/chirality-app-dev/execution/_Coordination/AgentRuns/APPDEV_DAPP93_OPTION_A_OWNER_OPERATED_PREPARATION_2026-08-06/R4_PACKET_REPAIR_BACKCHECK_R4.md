# R4 control-successor exhaustive backcheck R4

Status: `PASS — IDENTICAL PREPARED BYTES; ORDINARY RETURN WIRING PROVED`

This control successor supersedes R3 only for current fitness. Freezes
`b741231bd7a5c7d589f5217c7f01b2a8a56843928b7bf8cbe3b6cb57c8a72bce`,
`5a23e4152cf53bf5d90b1e84eca2ab8200314b6d17344278c7f02da0d25daac9`,
and `ea2dd68f9e0aa16f0b2c536652f8259c0286c0b1597644c9c45bd2539a85da6b`
remain immutable rejected history and are not current freezes.

Accepted EVALUATION report/handoff:
`9b4992a285e18040e2ef9ae2d6af4d34fabdb392277d606a587f82efe8d4f2a5` /
`0b5607afa53151a1f730a3c53a899fa85d321270e820bf97d81435656c2849ff`.

## Rejection reconciliation

HELP_HUMAN's final reported defect was checked against the exact frozen
C1130 row. C1130 already copies
`/private/tmp/chirality-dapp93-owner-operated-20260807/evidence/SOURCE_SCREEN_RESULTS.txt`
as its fifteenth source into the occupied-checked `returned/` directory. It
does so after C1148 creates that file and within the preserved ordinary order
C1145→C1144→C1130. No prepared byte was changed.

The exact ordinary-path producer/copy trace is frozen separately at
`C1155_ORDINARY_PATH_PRODUCER_TRACE.md`. Its verdict is
`PASS_ORDINARY_PATH_REQUIRED_FILES_21_OF_21`: each member of C1155's required
array has a producer and exactly one ordinary-path return/copy operation.
`COMPLETENESS_RESULT.txt` is correctly excluded from that precondition array
because it is C1155's output.

## Exhaustive matrix preservation

Because all nine prepared identities are byte-identical to the R3 backcheck
basis, every prior exhaustive disposition remains unchanged:

| Accepted rows | Rechecked fact | Verdict |
|---|---|---|
| A01-A44 | All branch preconditions, phase-specific early stops, ordinary ordering, terminal failure routes, and preserved C196/C197 rows remain byte-identical. | PASS |
| B01-B40 | All declared required evidence producers, captures, return actions, screens, manifest identities, range hashes, and terminal dispositions remain byte-identical. | PASS |
| C1155 required array | 21/21 ordinary-path objects traced from exact producer through direct return or C1130 copy; no orphan. | PASS |
| `SOURCE_SCREEN_RESULTS.txt` | C1148 producer → C1130 fifteenth source → returned object → C1157/C1154/C1155 consumers. | PASS |

## Mechanical results

- 93 unique command rows: C196, C197, and contiguous C1067-C1157;
- 31 runbook steps and 31 literal evidence-form disposition rows;
- static `zsh -n` PASS for literal changed/new shell bodies; no proposed
  packet, runtime, helper, debugger, mock, or other operation was executed;
- all eight prepared-index object hashes reproduce and the index hash is
  unchanged;
- the three unaffected prepared identities reproduce;
- fixed package root and `returned/` do not exist; frontend Git status is
  empty; trailing-whitespace scan passes;
- the alleged C1130 omission is absent, so no prepared-byte repair was
  necessary or introduced.

Verdict: `PASS_STATIC_R4_CONTROL_SUCCESSOR_RECONCILED`.
