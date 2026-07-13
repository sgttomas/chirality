# C2 Containment and Disjointness Audit

Verdict: `PASS`

## Reproduced sets

- Live tracked source diff: 53 paths.
- C2R source set: 48 paths, exactly the C2R manifest rows with
  `UPDATED` or `REGENERATED` state.
- C2A source set: four paths, exactly `C2A/CHANGED_PATHS.txt`.
- Parent coordination set: one tracked path,
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/WORK_GRAPH.json`.
- C2R/C2A intersection: empty.
- Expected-versus-live set differences: empty for both lanes.

## Denied-surface audit

The tracked source diff contains no deliverable folder, `_STATUS.md`, Remaining,
lifecycle, receipt, release, governed decision/history, or P1 canon write.
Root C2R did not write an App or other project source. App C2A wrote only four
of its nine authorized frontend caller/test paths. Run evidence is confined to
the declared root and App coordination packages plus this C2F derivative
package.

Ignored-state observations are not usable as a clean before/after proof because
the accepted basis records a pre-existing ignored/untracked environment and no
per-path ignored baseline. The current App evidence expressly classifies its
build and harness artifacts as owned ignored check output. No ignored path is
claimed as deliverable or authority state. This limitation does not weaken the
tracked source containment result and must be preserved for C2G review.
