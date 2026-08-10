# Validation R4.4.2 — sole-verifier BLOCK fan-in

Verdict: `BLOCK_PACKET_ROUTE_CONTRADICTION — TOKEN WITHHELD`

Accepted verifier-gate freeze SHA-256:
`d3366ab939bc3b28ecb5fb2d70f01776ffe8e8ac7c10730ecb70f3e8a5480152`.
Sealed sole-verifier brief SHA-256:
`272325bbf49599652c1fe0192269469d61390dcbf7c5895a47e495018314c760`.
Sole fresh-verifier return SHA-256:
`e6953bc6ebf33c3630ca3dd087066f6a2863c20610b17f7302bb5e166b499863`.

The manifest-only repair removed Receipt 139's universal-removal
contradiction. The verifier nevertheless found a dispositive pre-existing
route cycle: C1142 requires an explicit C1152 no-write/partial-root
disposition, while C1152 is post-cut after C1142-C1143 and C1146.30. Partial
C1070 and Incomplete baseline therefore remain unsatisfiable.

No repair or second verifier is authorized. The execution token is withheld.

