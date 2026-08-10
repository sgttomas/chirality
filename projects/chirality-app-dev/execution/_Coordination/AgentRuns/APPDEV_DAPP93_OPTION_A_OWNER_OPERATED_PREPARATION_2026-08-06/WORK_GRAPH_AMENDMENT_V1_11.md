# Work-graph amendment v1.11 — R4.4.1 manifest-only repair

Authority: `R4_4_1_MANIFEST_REPAIR_AUTHORITY_ADOPTION.md`

Posture: `SINGLE_MANAGER_MANIFEST_REPAIR — VERIFIER HELD`

Status: `ACTIVE`

## Nodes and ordering

1. `R441-BASIS`: reproduce Receipt 139 freeze, verifier BLOCK, handoff, and
   every frozen prepared identity.
2. `R441-MANIFEST`: amend only the manifest terminal-cleanup clauses so exact
   temp-root removal depends on the already-enumerated route prerequisites and
   named retention routes remain mandatory.
3. `R441-INDEX`: refresh only the manifest identity in the prepared index.
4. `R441-BACKCHECK`: prove every unaffected prepared byte and every command
   byte unchanged; prove route consistency, whitespace/diff/frontend/App-only
   containment, and fixed-root/returned absence.
5. `R441-FREEZE`: issue one immutable successor and report identities to
   HELP_HUMAN.
6. `R441-VERIFY`: held until HELP_HUMAN explicitly accepts the successor.

No verifier, packet, runtime, debugger, package, helper/GUI, signal,
credential, product, release, reliance, Git mutation, Task Management,
foreign-loop, or other action is authorized in this tranche.
