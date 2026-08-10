# Work-graph amendment v1.5 — R4 exhaustive branch/evidence repair

Parent: `WORKING_ITEMS`

Authority: `R4_PACKET_REPAIR_AUTHORITY_ADOPTION.md`

Execution form: bounded direct-manager mechanical audit and documentation
repair. No Agent 2 author is used.

Allowed prepared writes are limited to affected bytes in:

- `prepared/COMMAND_AUTHORITY_LEDGER.md`;
- `prepared/OWNER_OPERATED_RUNBOOK.md`;
- `prepared/EVIDENCE_RETURN_PACKET.md`;
- `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md`;
- `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md`; and
- `prepared/PREPARED_PACKET_INDEX.md`.

Allowed control writes are limited to this amendment, the authority adoption,
an exhaustive branch/evidence audit matrix, mechanical backcheck, R4 freeze,
one sealed fresh-verifier brief and return, closeout records, and Receipt 138.

Required sequence:

1. prove unchanged R3 identities;
2. enumerate every runbook branch, invoked command, and precondition;
3. enumerate every required evidence object and its literal capture/return
   action;
4. repair all discovered instances of the two authorized defect classes;
5. prove command uniqueness, range/reference/order/precondition/evidence
   closure and unaffected-byte equality;
6. freeze R4; and
7. dispatch exactly one genuinely fresh read-only verifier.

No repair or second verifier is authorized after the verifier verdict or
no-return. No runtime, debugger, package, helper/GUI, signal, credential,
product, release, reliance, Git, Task Management, or foreign-loop action is
permitted.
