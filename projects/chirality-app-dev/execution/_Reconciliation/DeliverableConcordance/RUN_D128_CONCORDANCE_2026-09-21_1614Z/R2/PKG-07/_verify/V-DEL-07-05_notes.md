# V-DEL-07-05 — verifier shard notes (DEL-07-05)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 1 | 1 | 0 | 0 |
| a30 | 12 | 12 | 0 | 0 |
| b | 3 | 3 | 0 | 0 |
| c | 2 | 2 | 0 | 0 |
| **Total** | **18** | **18** | **0** | **0** |

Correction: an earlier version of these notes counted DEL-07-05#CLM-012.15 as a CONTESTED
class a30 item. That was wrong. CLM-012.15 is in SELECTION only as class c, paired with
CAP-WORKSPACE-019, and on that item it is CONFIRMED. The CauseTag point about CLM-012.15 as a
forward row is in pattern 3 below. It is an observation outside the selection and has no CSV
verdict. No item is refuted on a verdict field.

## (ii) Patterns

1. **Mixed live/legacy rows cite R4-Q1 for their legacy-only sub-part.** The keys are CLM-003,
   CLM-004, CLM-011, CLM-017.2 and CLM-012.15. On each row, LIVE code (the dependency route,
   `lib/dependencies/*` and `deliverable-contracts.ts`) meets part of the claim. The MCP-exposure,
   permission, hook or instruction-root part is met only by the LEGACY_ONLY `lib/harness/mcp/read-tools.ts`
   and `lib/harness/tool-path-policy.ts:298`.
   - I graded R4-Q1 as correct. None of these rows is fully "met by LIVE code", and the owner's
     R4-Q1 ruling would decide the legacy-only part.
   - Each of these rows also carries ALSO_MODULE.
   - R3 may want one reading of grading key 5a for this partial-met case.
2. **The dependency route is a served entry that no rendered surface calls.** The API route is
   `REACH=LIVE` as a served handler. That matches the §9 entry-point definition, so I confirmed it.
   - Its only UI callers are `pipeline-surface.tsx:407` and `workbench-surface.tsx:264`, via
     `deliverable-api.ts:242`. Both sit under LoopShell, which `woven-dialogue-route.tsx:18`
     discards (`void legacy`).
   - The worker disclosed this departure from the map. `REACHABILITY.csv` still tags
     `deliverable-api.ts` as LIVE.
   - If R3 ever reads "executed" strictly, these product-behaviour rows would move toward
     `DOCUMENTED_UNIMPLEMENTED` for the API-exposure part.
3. **CauseTag is inconsistent within the unit.** CLM-004 and CLM-017.2 use CODEX_SOLE_ENGINE
   with `GOV:D-GOV-43` and CAUSE2:PRE_V3_DRIFT. CLM-012.15 reverses this: PRE_V3_DRIFT with
   `NONE_FOUND` and CAUSE2:CODEX_SOLE_ENGINE, on the same gap and the same evidence. §4
   precedence admits both. CLM-012.15's forward row is not in this shard's selection, so this
   is recorded here for R3 only; there is no CSV verdict for it.
4. **REF-006 "is MATCH under D-APP-38" rows use STALE_SPECIFICATION with SEE:REGISTER-1.** The
   keys are CLM-001, 008, 009, 010 and 018.
   - Applying tie-break rule 3 this way is correct. The P40 notes call themselves "current-state".
   - The PRD hash recomputes to `17ca3f3c…`, not the recorded `8649ccba…`. The PRD was amended
     under D-GOV-43 on 2026-09-12 (git log `23b3879b3`).
5. **Minor observations (no refutation).**
   - REGISTER-3: the warning's premise ("the enum has no OBJECTIVE") is literally true. The false
     assertion is the `TargetType=UNKNOWN` classification of a resolvable target (TYPES §6.5,
     K-DEP-2). The Disposition holds.
   - CLM-012.14: `runtime-service.ts:580` is a runtime-fingerprint field. It is not an MCP
     configuration, but it is adequate given that no MCP server wiring exists under
     `chirality-runtime/packages`.

## (iii) Effort

- **Read:** about 20 files or ranges. These were the full brief, CONVENTIONS and RUN_BASIS; the
  unit's ScopeOfWork, `_REFERENCES`, `_DEPENDENCIES`, Dependencies.csv and INSP-03; `lib/dependencies/*`,
  `deliverable-contracts.ts`, the route, `read-tools.ts`, `tool-path-policy.ts`, `filesystem.ts`,
  `woven-dialogue-route.tsx` and `runtime-service.ts`; and SPEC §6.1/§13.1, CONTRACT K-MCP-1,
  PRD FR-024 and TYPES §6.5.
- **Git:** read-only `log` and `blame -L` against the frozen tree.
- **Context budget:** not tight.
