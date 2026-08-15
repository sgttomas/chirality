# Frozen work graph v1

Posture: serialized terminal fan-out/fan-in, selected by the owner-directed engineering target.

1. `A2-PKG03-MODEL-DRAIN-IMPLEMENT-01` — `TASK + software-bounded-implementation`; integration owner for `frontend/**`; inspect Root runtime read-only, implement the smallest realistic daemon-restart proof, run focused checks, and return exact evidence.
2. `A2-PKG03-MODEL-DRAIN-REVIEW-01` — fresh `TASK + software-code-review`; read-only after node 1 freezes; review 100% of the diff and evidence.
3. `WI-PKG03-MODEL-DRAIN` fan-in — accept or remediate, run registered full frontend checks, then update only the minimal selected-deliverable and managed return surfaces.

Edge: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. Writes overlap only at manager closeout after both children terminate; the reviewer has no write target.

Fan-in gate: realistic public daemon lifecycle/client/session seams; one armed in-flight drain; daemon stop and restart; durable replay contains exactly one terminal event for the accepted turn; no Root runtime edit; focused test, full frontend Vitest, typecheck, build as applicable; fresh review pass.
