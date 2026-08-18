# D-APP-100 — Packaged daemon instruction-root resolution

Status: `RULED — B1`

DecisionID: `D-APP-100`

Date: `2026-08-17`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Exact owner ruling

```
**B1 — Packaged daemon instruction-root resolution, DEL-09-04.**

The packaged daemon resolves its instruction root from the manifest-resolved root — the same resolution the app and CLI use — not per-process from the packaged resources path. Implement as one bounded engineering node: resolution change in the daemon entry/host code, a regression test proving app, CLI, and packaged daemon agree on the resolved root, and a packaged-under-isolation proof. Independent-review path applies (product source). Fallback to the packaged resources path is permitted only when no manifest root resolves, and must be logged. Remove the DEL-09-04 Remaining item on landing.
```

## Effect

The existing DEL-09-04 decision residual is now an authorized, bounded
engineering node. It remains in `Remaining` until implementation lands. No B1
engineering occurs in this recording tranche.
