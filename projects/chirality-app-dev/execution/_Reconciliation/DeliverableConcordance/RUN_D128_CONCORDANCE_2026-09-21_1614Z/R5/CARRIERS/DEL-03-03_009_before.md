### CLM-005 — Construction

> ##### Construction
>
> | Component | Construction Notes | Source |
> |---|---|---|
> | Route adapter layer | Keep `/api/harness/turn` as SSE transport adapter; runtime policy belongs behind `TurnEngine` and engine contract services. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` Section 8.12 FR-071 |
> | SSE encoder/fixture layer | Preserve named SSE events listed in SPEC/TYPES/PRD; additional tool progress events require UI compatibility handling. | `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3 |
> | UI/runtime mapper boundary | Map SDK messages into browser `UIEvent`s and richer persisted `HarnessEvent`s without exposing SDK message names as public UI contract. | `docs/PRD.md` Sections 8.12 FR-116 and 9.3 |
> | Test artifacts | Build route adapter tests, SSE compatibility fixtures, and UI event contract docs. Exact fixture payloads are TBD pending current implementation capture. | `_CONTEXT.md` Anticipated Artifacts; `docs/PRD.md` Section 12.6 |
>

