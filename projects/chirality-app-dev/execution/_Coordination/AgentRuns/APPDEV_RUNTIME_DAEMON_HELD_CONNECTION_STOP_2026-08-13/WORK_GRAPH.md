# Frozen work graph v1

Posture: serialized terminal fan-out/fan-in, selected by the owner-directed engineering target.

1. `A2-RUNTIME-STOP-IMPLEMENT-01` — implement and test; owns `runtime/packages/daemon/src/**`, `runtime/tests/**`, and its run record under this run root.
2. `A2-RUNTIME-STOP-REVIEW-01` — fresh read-only code review after node 1 freezes; no writes.
3. Manager fan-in — accept or return remediation; run required checks; write only minimum DEL-09-04 closeout surfaces.

Edge: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. No concurrent writes and no shared writable file.

Fan-in gate: actual child-process `SIGTERM`; complete-headers/incomplete-body Unix-socket holder; bounded clean exit; socket and owner cleanup; source change technically justified; focused test, complete runtime test, typecheck, and independent review pass.
