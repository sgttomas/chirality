# DEL-09-07: reverse-pass notes

**Result:** all 162 capabilities are `NOT_MINE`. The four surface files are BUILD (41),
ELECTRON (35), ROUTES (44) and SETTINGS (42). There are no errata. The sealed claims SHA-256
is unchanged: `47b23cb1…70c0ff`.

**Why nothing is claimed.** D-APP-127 retired DEL-09-07. The deliverable's scope was a
two-job LaunchAgent installer with its journal, effective-state inspector and
rollback/upgrade/uninstall/cleanup fixtures. None of that exists on any surface. The
capabilities closest to it are the ones that replaced the retired topology:

- CAP-ELECTRON-001 (startup)
- CAP-ELECTRON-003 (App-owned service child)
- CAP-ELECTRON-010 (restart-only runtime-control IPC)
- CAP-SETTINGS-007 (retry in Settings)
- CAP-BUILD-015 (bundle guard against LaunchAgent residue)

The forward rows cite these capabilities only as evidence of retirement. Live deliverables
own them.

**Coverage gaps:** none new. The forward notes already record that SOW-080 is still `IN` in
the decomposition. That gap is routed to EXT `SOW:SOW-080`.
