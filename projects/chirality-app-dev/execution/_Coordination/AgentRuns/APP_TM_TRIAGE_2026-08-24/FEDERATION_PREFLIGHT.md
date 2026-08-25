# Mandatory federation preflight

Date: `2026-08-24`

Command:

`python3 tools/taskmgmt/taskmgmt.py federation --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`

Result: `COMPLETE`; four canonical live registers discovered, read, and
validated; 55 typed-field findings computed and 30 App-relevant/program-level
findings presented; register writes `0`.

| Register | OPEN | DEFERRED | ELEVATED | CLOSED | Archived |
| --- | ---: | ---: | ---: | ---: | ---: |
| PEC | 16 | 1 | 0 | 1 | 7 |
| Root | 11 | 8 | 0 | 0 | 108 |
| App | 9 | 3 | 0 | 1 | 31 |
| Piping | 11 | 23 | 0 | 0 | 8 |

Presented typed relationships/findings:

- `FOREIGN_LINK_TO_LOCAL=1`
- `LOCAL_LINK_TO_FOREIGN=26`
- `REMOTE_CLOSED_LOCAL_OPEN=1`
- `LOCAL_CLOSED_REMOTE_OPEN=23`
- `MISSING_NOTICE=4`

The helper wrote only its gitignored rebuildable projection at
`execution/_Coordination/_TaskManagement/.candidates/federation.json`; this is
not authority and is outside the tracked candidate write set. It may be
deleted without effect.

Limits: `COMPLETE` means complete canonical-register discovery/read/schema
validation, not semantic completeness, adoption, inferred promotion,
priority, closure, or disposition. Relationships were formed only from
schema-governed fields. No global-absence claim relies on free-form Notes.
