# RECON-A1-F Terminal Return

Terminal verdict: `PASS`.

W-A1 preintegration reconciliation independently reproduced the exact 15
ordinary App members across APP-PKG-00..03, all 30 terminal author/verifier
children, 456 claim mappings, 4,817 source lines, 15 candidate identities,
and separate schema/content-authority/preservation/execution-substrate
verdicts.

Current package fan-in is 189/189 bindings after the versioned PKG01 R2
portability repair. The earlier 186/186 audit is retained as explicitly
historical pre-repair evidence. The complete PKG01 R1-to-R2 chain passes:
exact two-field repair, JSON parse, six registered PASS results, exact reverse
preimages, and zero unclassified generated prefixes.

All 15 members independently pass schema, claim map, parity, complete
source-line disposition, checklist identity/linkage, render identity/safety,
partial fail-closed, and unauthorized-dual fail-closed checks. The normalized
replacement manifest contains exactly 75 rows and rollback is its exact
75-row inverse, excluding status/control paths. Isolated apply/rollback
simulations pass 15/15: apply resolves exact SOW_V1 with status/control
preserved; rollback restores the exact legacy tree and removes the candidate.

The full App check set passes: harness self-check; 264 harness pytest tests;
typecheck; 713 frontend tests with four skipped; build; and live-stub premerge
with Section 8 at 8/8 and report-only Section 9 at 16/16. Project tracked and
untracked dirty paths are zero; diff hygiene and reconciliation-evidence
portability pass.

Immutable derivative:
`snapshots/W_A1/preintegration/**`. Its MANIFEST has 23/23 reproduced bindings
and SHA-256
`c8ae005ca8d1007ccf7f7ee12dc81f441ad65ae3fa094d7314249e747831a5eb`.

Blockers, conflicts, waivers, missing outputs, stale bindings, human rulings,
and rerun requirements at the recorded identities: none.

Requested parent action: HELP_HUMAN independently reproduce and accept or
reject this derivative. This return is a recommendation only. It performs and
authorizes no Git change, integration, lifecycle acceptance, H1/H2, ISSUED,
release, or retirement action.
