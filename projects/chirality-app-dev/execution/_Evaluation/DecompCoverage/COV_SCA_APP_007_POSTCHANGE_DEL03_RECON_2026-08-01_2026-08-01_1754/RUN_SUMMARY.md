# SCA-APP-007 Post-change Decomposition Coverage Summary

**RUN_STATUS:** `WARNINGS`

**Scope:** `PKG-03,PKG-09`

**Authoritative input:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (`sha256:dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`)

**Expected source snapshot:** current accepted decomposition plus SCA-APP-007 Gate-5 migrated filesystem

**Expected handoff phase:** `SCA-APP-007 Gate 5 post-change`

The decomposition declares two in-scope packages and ten in-scope deliverables. Exactly one physical root now resolves to each package, and all ten declared deliverables resolve to folders with matching IDs and context. All ten are `IN_PROGRESS`.

The two topology warnings identified pre-change are resolved: `PKG-03_Harness_Runtime_Core` no longer exists, and no reverse-only `DEL-03-06` folder remains. Its 38 historical proof files are preserved byte-for-byte under accepted `DEL-09-06`; the migration manifest reports 38/38 SHA-256 matches and 97,817 bytes on each side. No blocker or new warning was found.

Ten pre-existing anticipated-artifact filename warnings remain. They are unrelated to SCA-APP-007: each scoped SOW_V1 document contract validates, but the named implementation artifacts do not have conservative folder-local filename matches while the deliverables remain `IN_PROGRESS`.

**Closure verdict:** `WARN`. SCA-APP-007's topology objective passes and is suitable for Gate-5 fan-in, while ordinary production artifact warnings remain for their owning deliverables.

Per the sealed brief, `_Evaluation/DecompCoverage/_LATEST.md` was not updated.
