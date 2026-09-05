# AUDIT_DECOMP Return

**Status:** `POST_ALIGNMENT_AUDIT_COMPLETE`
**Overall:** `WARNINGS`
**Closure readiness:** `FAIL`
**New blocker/major versus SCA-APP-010 Gate-5 post-change:** `NO`
**Basis:** `d66395d101143df68d956984f7ab93f5027418ec` plus the working tree (thirteen refreshed registers)
**Object:** live applied SCA-APP-010 decomposition and companion against the live filesystem (SCA-APP-010 active)
**Snapshot path:** `projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518/`

Fresh full-scope SOFTWARE audit is complete with no repository writes outside
the ten snapshot files and the two instance files. Topology 10 / 52 / 84
(79 / 4 / 1), 10 objectives, 8 open issues, S9 / M41 / L2 / XL0; forward
52/52 and 10/10; reverse 52/54 (PKG-00, DEL-00-01/02 carried); reverse-view
parity 0 / 0; no duplicate or dangling ID; OI-008 AffectedScope 4 equal to
telemetry; companion 83 rows / 50 families / 18 columns with 83/83 pins to
the live hash; 54/54 SOW_V1; 52 statuses; 51 MEMORY reads; thirteen refreshed
registers hash-exact, v3.1 VALID, anchored to the applied rows; corpus v20,
no drift.

Occurrence-weighted totals are 0 blockers / 72 warnings / 10 info
against Gate 5's 0 / 74 / 8. No new BLOCKER and no new MAJOR condition
exists; zero new warning occurrences. G5-010-COV-005 is resolved at the
context (DEL-02-02 DeliverableName equals the applied name; folder label
retained by design, INFO PA-010-COV-005). G5-010-COV-004 is partially
resolved: identity, DeliverableName, Package Scope, and Deliverable Scope are
aligned on all thirteen carriers, but Traceability `CoversScopeItems` (nine
carriers) and the Anticipated Artifacts paragraph (ten carriers) still lag the
applied rows and DEL-08-03's ownership-boundary section still names the
retired DEL-02-02 consumer, so PA-010-COV-004 remains a 13-occurrence
WARNING outside the executed WI permitted effect. G5-010-COV-013 is
reclassified to INFO because SCA-APP-009 is no longer active. The 68 other
warning occurrences (reverse-only folders, four carried PARTIAL contexts, 50
artifact-incomplete IN_PROGRESS rows, stale 81/48 and 10/51 prose, SCA-APP-008
residue) are carried unchanged.

Top issues: PA-010-COV-004 thirteen amended-carrier Traceability and
artifact lags; PA-010-COV-003 four carried PARTIAL contexts;
PA-010-COV-011 stale 81/48 and 10/51 prose; PA-010-COV-012 SCA-APP-008
residue; PA-010-COV-001/002 undeclared control-plane folders;
PA-010-COV-007 artifact presence 12/202; PA-010-COV-015 SCA-APP-010
pre-pointer wording and trailing derivative fields; PA-010-COV-016
DecompCoverage pointer not moved.

Recommended next action: HELP_HUMAN validates fan-in with N4 and N5 and
presents to the owner (a) the residual thirteen-carrier context lag as a
further WORKING_ITEMS authorization or a `FUTURE_WRITE_SET.csv` amendment,
(b) acceptance of this snapshot as the DecompCoverage pointer target, and
(c) the SCA-APP-010 `Handoff_State.md` derivative-field update on
disposition. Do not infer closure, seating, pointer authority, or any
downstream act from this derivative audit.
