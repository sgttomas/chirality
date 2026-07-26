# Orchestration Plan — ROOT-OGC-20260725 (owner-gated closeout)

Agent 0: `HELP_HUMAN` posture · Date: 2026-07-25 · Basis: `4aaa66483`
(post-PR-#350 `main`) · Branch: `claude/root-owner-gated-closeout-20260725`

## Authorization

Owner ruling, in-session, 2026-07-25, verbatim: "Delegate to `opus-5`
subagents the closeout of those four owner-gated issues by following your
recommendations in each case." The four issues and the adopted
recommendations are recorded verbatim in
`docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`
(authored in this tranche). The ruling adopts the recommendations as
dispositions and delegates exact prose to the dispatched agents; approval
binds at the human-gated PR merge (K-AUTH-2 vehicle, stated in the record).

## Work graph

| Node | Actor | Work | Write targets | Status |
|---|---|---|---|---|
| S1 | Agent 2 — ephemeral (`opus-5`), sealed brief `briefs/SPEC-GUARDED-SET-BRIEF.md` | R1: SPEC §1.1 `_Archive/` note; R2: `.github/workflows/` into SPEC §0.2.2 + `CLAUDE.md` into the guards' instruction-surface set (+ tests) | `docs/SPEC.md`, `tools/validation/**`, `returns/S1_RETURN_RAW.md` | DISPATCHED |
| S2 | Agent 2 — ephemeral (`opus-5`), sealed brief `briefs/KWRITE2-GLOSS-BRIEF.md` | R3: K-WRITE-2 gloss amendment | `docs/CONTRACT.md`, `returns/S2_RETURN_RAW.md` | DISPATCHED |
| S3 | Agent 2 — ephemeral (`opus-5`), sealed brief `briefs/EXPORT-AUDIT-BRIEF.md` | R4: read-only export-boundary audit grounding the standing deferral disposition | `evidence/EXPORT_BOUNDARY_AUDIT.md`, `returns/S3_RETURN_RAW.md` | DISPATCHED |
| A0 | Agent 0 | D-GOV-26 + register row; fan-in verification; M6 notice to app-dev (SPEC + CONTRACT pinned in its authority corpus); tranche manifest; Receipt 50; PR | `docs/governance_harness/**`, `projects/chirality-app-dev/execution/_Coordination/`, run record, `LOOP_RECEIPTS.md` | IN PROGRESS |
| GATE | Owner | Human-gated PR merge | — | STOP STATE |

Write-target disjointness: S1 owns `docs/SPEC.md` + `tools/validation/`;
S2 owns `docs/CONTRACT.md`; S3 is read-only outside the run record; Agent 0
touches none of those. Pin survey at this basis: app-dev authority corpus
pins SPEC and CONTRACT (routed notice required); the chirality domain pack
pins neither.
