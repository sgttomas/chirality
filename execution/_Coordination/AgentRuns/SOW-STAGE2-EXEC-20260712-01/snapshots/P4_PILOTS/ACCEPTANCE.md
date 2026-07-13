# P4 Pilots Postintegration Acceptance

Status: `IMMUTABLE DERIVATIVE — G4/P-G PASS`
Accepted: `2026-07-13`
Accepted project truth: `main@b4efb8e554354399aadf1f624c107f63ede3230d`

HELP_HUMAN accepts the P4 pilot phase after validated fan-in of the accepted
P-F-R1 preintegration snapshot and terminal CHANGE-P-G integration/postmerge
closure. PR #223 passed both required checks and merged the exact verified
source head through merge commit
`e3c338c5830fa407ed8e2126cc316aba0325cc99`; the postmerge evidence-only
closeout synchronized local main, origin/main, and remote main at the accepted
project-truth commit above with divergence 0/0.

The exact accepted population is six App PKG-07 and four Piping PKG-13
IN_PROGRESS members. Each was integrated through one serial five-path commit:
one exact accepted SOW addition and four exact legacy deletions, with no
control or status path. Live fan-in independently reproduces 10/10 exact
candidate hashes, 10/10 exact `_STATUS.md` hashes, 10/10 `SOW_V1`, 40/40
legacy files absent, and 10/10 lifecycle states still `IN_PROGRESS`.

The remote PR carried the exact 12-commit architecture, exact path inventory,
and two successful required checks. All recorded App, Piping, SOW tool,
governance, resolver, containment, portability, and diff-classification gates
pass. Blockers, material unknowns, and waivers are none. The 50-row rollback
manifest remains an instruction for a later explicitly authorized forward
act; no automatic reset, revert, cleanup, or history rewrite is authorized.

Exact accepted postmerge and terminal manager hashes are recorded in
`ACCEPTANCE_MANIFEST.tsv`. This acceptance closes G4/P-G and releases only the
read-only A1 ordinary-wave preflight. It does not yet release an A1 package
conversion, alter lifecycle, approve H1 or H2, act on ISSUED Piping DEL-01-01,
release a product, authorize reliance, or retire legacy support.

Rerun P-G if any accepted preintegration byte, source/candidate/status,
manifest operation, commit/PR/check identity, merge ancestry, post-state,
rollback binding, terminal manager record, or accepted-main identity changes.
