# QA report — DEL-00-01 RV1 SELF_CHECK

| Check | Result |
|---|---|
| Reliance-hold preflight (manager's run, cited) | PASS — `candidate-validation=ALLOW` (×8 total) |
| ADR identity | PASS — `ad6bab7ee007…` |
| SOW identity | PASS — `3757632b507d…` |
| `D-PEC-105` ledger rendering (independent) | PASS — ADR 6 hunks, SOW 3 hunks |
| SOW format | PASS — `SOW_V1` |
| Checklist identity and reproduction | PASS — 7 rows, `6e99f93c37c7…`, byte-identical twice |
| Prior-checklist diff | PASS — source hash only (`bb815439…` to `6e99f93c…`) |
| Strict registers | BASELINE — 68 registers / 285 rows / 0 errors / 26 `XRG-013` warnings, exit 1 |
| Identity check (audit-decomp substitute) | PASS — 12/12 |
| Matrix closure | PASS — OUT 2, REQ 10, AC 7 (each once), VER 4 |
| AC-001, AC-003..AC-006 | PASS |
| AC-002 | PARTIAL — RF-001 |
| AC-007 | READY FOR OWNER DECISION |
| OC-001 / DS-001 / TB-001 | Y / SATISFIED / 2 registered, 0 unregistered |
| Findings | 5 open (MAJOR 1, MINOR 3, OBSERVATION 1); 0 deferred |
| Lifecycle / acceptance | CHECKING unchanged / NOT PERFORMED |
