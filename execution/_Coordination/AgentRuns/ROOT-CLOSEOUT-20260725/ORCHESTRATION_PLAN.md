# Orchestration Plan — ROOT-CLOSEOUT-20260725

Agent 0: `HELP_HUMAN` posture · Date: 2026-07-25 · Basis: `9d0cbc536`
(post-PR-#349 `main`) · Branch: `claude/root-closeout-20260725`

## Authorization

Owner direction, in-session, 2026-07-25: "let's close out what we can now
before proceeding to the per-deliverable initialization and creation of
scopes of work." Releases the agent-closeable dormant items; owner-gated
items are staged as recommendations only.

## Work graph

| Node | Actor | Work | Write targets | Status |
|---|---|---|---|---|
| H1 | Agent 2 — ephemeral generalist (`opus-5`), sealed brief `briefs/HARNESS-ADOPTION-BRIEF.md` | Practitioner-harness adoption of the root adapter (aliases, loader normalization, status/drift, tests, live baseline pin) | `tools/practitioner_harness/**`, `returns/H1_RETURN_RAW.md` | DISPATCHED |
| A0 | Agent 0 | 45 `_SEMANTIC.md` placeholder stubs (SPEC §2.1 fileset closure); D-GOV-19/20 historical reconciliation receipts; Lane B + gated-downstream closure banners in the 2026-07-25 workplan; CHANGE merge-verdict standing rule (`agents/AGENT_CHANGE.md`); tranche manifest; Receipt 49 | `execution/PKG-*/1_Working/*/_SEMANTIC.md`, `execution/_Coordination/**`, `agents/AGENT_CHANGE.md`, `docs/governance_harness/tranche_manifests/` | IN PROGRESS |
| FAN-IN | Agent 0 | Battery, G4 diff mode, commit, human-gated PR | — | PENDING |
| GATE | Owner | PR merge + rulings on the staged owner-item menu | — | STOP STATE |

Write-target disjointness: H1 owns `tools/practitioner_harness/**`
exclusively; Agent 0 touches nothing under `tools/`. Serialized fan-in.

## Owner-gated items staged (recommendations only, applied only on ruling)

1. `_Archive/` tracking tension (SPEC §1.1 vs `.gitignore` `**/_Archive/`).
2. Instruction-surface enumeration: add `.github/workflows/` to SPEC
   §0.2.2; decide `CLAUDE.md` membership in the guarded set.
3. K-WRITE-2 gloss debt (CONTRACT.md exact-prose amendment).
4. Export-staging regeneration (currently DEFERRED).
