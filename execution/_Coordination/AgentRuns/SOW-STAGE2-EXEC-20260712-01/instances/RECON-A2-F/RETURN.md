# RECON-A2-F Terminal Return

Terminal verdict: `PASS`.

W-A2 preintegration reconciliation independently reproduced the exact 16
ordinary App members across APP-PKG-04..06, all 32 terminal author/verifier
status and manifest surfaces, 491 preserved claim mappings, 5,584 source
lines, 144/144 live preflight source/status/control bindings, 16 candidate
identities, and separate schema, authority, preservation, and substrate
verdicts.

Current package fan-in is 208/208 bindings at the exact three graph v18
manifest hashes. All 1,052 child-manifest file/hash/byte bindings reproduce.
The three differing package schemas normalize without information loss, all
ownership is disjoint, and no package evidence was repaired by reconciliation.

Every member independently passes schema, target resolution, claim map,
parity, full source-line disposition, checklist determinism, render
determinism and active-resource safety, partial fail-closed, and unauthorized
dual fail-closed. The combined replacement manifest has exactly 80 rows and
rollback is its exact 80-row action/hash inverse, excluding status/control
paths. Isolated apply/rollback simulations pass 16/16: apply resolves exact
SOW_V1 with status/control preserved, and rollback restores the exact legacy
tree and removes the candidate.

Each package retains five base registered App PASS checks and the initial
no-server frontend-premerge substrate failure. Each server-backed rerun passes
Section 8 at 8/8 and report-only Section 9 at 16/16. Generated evidence has
zero unclassified machine-root or temp-root literals. The 81 remaining
machine-root occurrences are confined to 48 immutable copied source/control
files and are inventoried. Live project paths remain unchanged and clean;
diff hygiene passes.

Immutable derivative: `snapshots/W_A2/preintegration/**`. Its MANIFEST has
16/16 reproduced bindings and SHA-256
`0dbf05dec12668517f3b34097d15afdb5bff3a9bfa9f73569f614883238b000d`.

Blockers, conflicts, waivers, missing outputs, stale bindings, unknowns, human
rulings, and rerun requirements at the recorded identities: none.

Requested parent action: HELP_HUMAN independently reproduce and accept or
reject this derivative. This return is a role-bounded recommendation only. It
performs and authorizes no Git change, integration, lifecycle acceptance,
H1/H2, ISSUED action, release, or legacy retirement.
