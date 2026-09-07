# Gate 5 ledger-repair handoff — successor v2

State: `WAITING_EXACT_LEDGER_REPAIR_V6_APPROVAL`.

Completed: exact original SCA-002 application; immutable SCA-002 application snapshot; first independent poststate audit; append-only ledger-repair authoring; correction of historical SCA-001 state; correction of contract-choice status; removal of self-staling repair language; fresh independent v6 PASS; manager hash, CSV-field, evidence, and strict patch-applicability validation.

V5→v6 cause: v5 correctly addressed both substantive concerns, but its future canonical row called itself a `proposed exact postimage`. V6 replaces only that self-reference with durable ledger-state wording and makes the accepted-contract evidence paths unambiguous. No generic metadata expansion or new authority was introduced.

Next owner decision: approve the exact v6 one-file repair and limited snapshot/pointer/audit-rerun plan in `GATE5_REPAIR_DECISION_SUBJECT_v2.md`.

After approval: reverify the unchanged ledger preimage; apply the exact patch; create a new immutable repair snapshot and permitted pointer update; rerun independent `AUDIT_DECOMP`; then present the corrected poststate for separate Gate 5 owner confirmation under `agents/AGENT_SCOPE_CHANGE.md` lines 590–597.

No v6 correction has been applied. Canonical remains the exact SCA-002 application poststate. No SOW, source, Root, Git, process, credential, supplier, oMLX, lifecycle, hold, release, or protected-fixture action occurred.
