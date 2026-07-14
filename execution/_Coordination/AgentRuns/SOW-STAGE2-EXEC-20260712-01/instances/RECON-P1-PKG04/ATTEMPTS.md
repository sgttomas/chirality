# RECON-P1-PKG04 Attempts

## Attempt 1 — retained mechanical adapter stop

The frozen PKG-03 full-reproduction template was bound at SHA-256
`787114fc44eecd3953d23cda8605963932657ca7e461c2e5e99c861191df5e05` and
adapted only through exact constant substitutions. It created
`snapshots/W_P1/PKG04-preintegration/`, completed the five-manifest audit, and
then stopped before member reproduction because PKG-04 `CHILD_INDEX.tsv` uses
the header `terminal_status` while the template expected `terminal_verdict`.

Classification: `SAFE_MECHANICAL_ADAPTER_DEFECT`. The retained partial
snapshot is an unaccepted attempt. It contains no member acceptance and is not
an immutable phase-boundary snapshot. No upstream, candidate, project,
lifecycle, control, dependency, Git, H1/H2, release, or retirement byte was
changed. The corrected run writes a distinct `PKG04-preintegration-r1`
snapshot and repeats the complete audit from the beginning.
