# A1 Reconciliation R2 Amendment 001

Status: `ACTIVE — FULL FAN-IN RERUN AFTER PKG01 PORTABILITY REPAIR`

`RECON-A1-F` discovered and correctly held on two unclassified generated
`workspace_root` values in accepted PKG01 check evidence. The owning manager
repaired and revalidated them under
`A1-PKG01-CHECK-EVIDENCE-PORT-R2-001`; HELP_HUMAN independently reproduced
the terminal result.

The PKG01 package manifest changed from 37 bindings at SHA-256
`77ea1855811612ae3f19226e6fd5b1d80cd737d91b1ee519f80d3dd49068b1b3`
to 40 bindings at SHA-256
`4924de97675bf8f0ad8bba606d3d5fc171d03445259a5e96eb72c5e002871f62`.
All 40 current bindings reproduce. Member/candidate/count/verdict,
replacement/rollback, child, project, and lifecycle bytes remain unchanged.
The two JSON postimages are portable, parse, retain all six PASS results, and
reverse exactly to their preimages. The historical R1 normalization proof is
retained as an intermediate chain.

This amendment supersedes only the package-binding cardinality and PKG01
portability basis in `A1-RECONCILIATION-ACTIVATION-001`: the exact current
aggregate is now 189 bindings (`23 + 40 + 64 + 62`), not 186.
`RECON-A1-F` must preserve the sealed 186-binding audit as explicitly
historical pre-repair evidence, independently reproduce all 189 current
bindings, validate the complete PKG01 R1→R2 chain and zero generated-prefix
claim, and rerun every affected package fan-in/portability/claim check before
terminalizing. All other activation objectives, metrics, write boundaries,
simulations, App checks, snapshot outputs, and prohibitions remain unchanged.
