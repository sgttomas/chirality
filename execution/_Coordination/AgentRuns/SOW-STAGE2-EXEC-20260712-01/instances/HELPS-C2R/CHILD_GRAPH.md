# HELPS-C2R Child Graph

Status: `ACTIVE`
Selection authority: `HELPS_HUMANS` under sealed C2R brief
Posture: `SEQUENTIAL`

```text
C1G_ACCEPTED -> TOOL-CORE -> HELPS-C2R manager implementation/fan-in -> C2R return
```

| Child | Form | Dependency | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|---|
| `TOOL-CORE` | bounded ephemeral Agent 2 generalist | `C1G_ACCEPTED` | live canon and exact P0 tool caller rows | only exact `tools/**` paths enumerated in its brief plus its own return/status | `children/TOOL-CORE/RETURN.md`, `STATUS.json` | all assigned callers dispositioned; resolver/checklist/conversion tests green; no path outside exact scope; no delegation |

The child does not own C2R integration, caller completeness, exports, agent/skill/docs changes, semantic acceptance, Git, project paths, lifecycle, conversion, H1, H2, or legacy retirement. HELPS_HUMANS validates its terminal return before using it.
