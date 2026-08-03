# HELP_HUMAN orchestration plan — plan version 11

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL`

## Owner authority

Exact packet acceptance:
`OWNER_RULING_2026-08-03_DEL0206_PACKET_ACCEPT.md`, SHA-256
`7ddbef0480700483cb07efe771b64e3f413b489288a02bde987a6a85b9ba70f7`.

Accepted CandidateSetManifestSHA256:
`360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f`.

Earlier continuation ruling SHA-256
`9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`
explicitly directs fresh N0 after exact packet acceptance and the applied
basis reconciliation.

## Node

| Node | Agent 1 | Objective | Stop |
|---|---|---|---|
| W5 | WORKING_ITEMS | Verify and externally record the exact packet acceptance, copy the current six-file candidate byte-identically into RunID-local `accepted_inputs/`, validate the live copy, then dispatch and validate fresh N0 using the existing N0 rerun brief/checklist. | Stop after the N0 gate return. Do not release N1, N2, N3, or any later node; do not implement runtime/client work or change lifecycle/release/reliance, Task Management, Git, or foreign surfaces. |

## Fan-in acceptance

W5 fan-in is acceptable only if the acceptance record contains exactly one
manifest-bound owner token and validates; candidate and accepted-input bytes
are exactly identical; all current-basis checks pass; fresh N0 has a real
bounded child return accepted by WORKING_ITEMS; the manager reports PASS or
precise blockers without releasing N1+; and all excluded surfaces remain
unchanged.
