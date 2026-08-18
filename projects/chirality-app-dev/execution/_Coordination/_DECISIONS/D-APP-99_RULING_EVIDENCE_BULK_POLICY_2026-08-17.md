# D-APP-99 — Evidence-bulk policy

Status: `RULED — C3`

DecisionID: `D-APP-99`

Date: `2026-08-17`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Exact owner ruling

```
**C3 — Evidence-bulk policy for packaged captures and release artifacts, TM-APP-035.**

Committed evidence for packaged UI captures, parity reruns, DMG/dist packaging, and CI artifact verification is compact and commit-bound: a JSON summary carrying the commit hash, artifact names, sizes, SHA-256s, the assertions checked and their results, and — for CI-produced artifacts — the workflow run id. Full accessibility-tree dumps, screenshots beyond a small representative set, DMGs, `.app` bundles, and other bulk outputs are not committed; they are CI artifacts or local outputs referenced by hash. Guideline: a committed evidence file over ~2,000 lines needs a stated reason in the run record. Existing landed captures (PR #492 and earlier) remain immutable history. Piping's DEC-025 sweep summary is the reference shape. TM-APP-035 is resolved by this ruling. Apply prospectively; no rewriting of landed evidence.
```

## Effect

`TM-APP-035` is resolved by this ruling and awaits the next TASK_MANAGEMENT
maintenance pass. The policy applies prospectively; existing evidence is not
rewritten.
