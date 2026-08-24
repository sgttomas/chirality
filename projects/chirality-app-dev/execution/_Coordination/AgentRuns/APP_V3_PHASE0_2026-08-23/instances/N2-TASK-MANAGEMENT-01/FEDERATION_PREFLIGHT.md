# Mandatory federation preflight

Date: `2026-08-23`

Invoking loop: App (`projects/chirality-app-dev`)

Coverage: `COMPLETE`

The deterministic federation helper ran before triage or harvest. It
discovered and validated every canonical Git-tracked live register and its
tracked archive. No canonical input was invalid, unreadable, or ambiguous;
the exclusion list was empty. The helper constructed relationships only from
schema-governed fields and reported zero register writes. Its default
`.candidates/federation.json` target was already present as a gitignored,
derivative projection; no projection is an output of this sealed run and no
projection is cited as authority.

## Coverage inventory

| Namespace | Live register | Live SHA-256 (before = after) | Live validation | Live rows | Archive | Archive SHA-256 (before = after) | Archive validation | Archived rows |
|---|---|---|---|---:|---|---|---|---:|
| PEC | `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | `6f7eb2a528a8a38ee01b94f5a028632d95297c82f4fa197f4c62f7102fef9264` | PASS | 18 | `_DomainEngines/pec/_TaskManagement/REGISTER_CLOSED.csv` | `bf0d5537686d3dba23ad2e3c1b91d989850cda04e98e92dc545516829c9242b6` | PASS | 7 |
| ROOT | `execution/_Coordination/_TaskManagement/REGISTER.csv` | `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` | PASS | 19 | `execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv` | `c8a58b08a30dea35fc361d08fec81e405fa08d40f04604709a6dd9b806e45e1c` | PASS | 108 |
| APP | `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` | `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6` | PASS | 13 | `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv` | `8e75d44ab11b20877f86a3b57e7d27a47f60f0188d71181db120144cab51d1e6` | PASS | 31 |
| PIP | `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv` | `5bad460d18782fbf7f3b370e2eca2d3518a178dfb485aa1d9386b2e9d85a064c` | PASS | 34 | `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv` | `c110c052fa2735b31c6889b8fdd7f2898d7a0194fc5bf5fbf703bc9024472192` | PASS | 8 |

Status totals were PEC `OPEN=16, DEFERRED=1, CLOSED=1`; Root `OPEN=11,
DEFERRED=8`; App `OPEN=9, DEFERRED=3, CLOSED=1`; and Piping `OPEN=11,
DEFERRED=23`.

The helper reported 55 typed-field findings and presented 30 for this
non-Root invocation: one `FOREIGN_LINK_TO_LOCAL`, 26
`LOCAL_LINK_TO_FOREIGN`, one `REMOTE_CLOSED_LOCAL_OPEN`, 23
`LOCAL_CLOSED_REMOTE_OPEN`, and four `MISSING_NOTICE` observations. Counts
for `AMBIGUOUS_REFERENCE`, `DUPLICATE_GLOBAL_ID`, `INVALID_REGISTER`,
`UNREADABLE_REGISTER`, `ORPHANED_LINK`, `INBOUND_ELEVATION`, and
`OUTBOUND_AWAITING_ACK` were all zero. None of the reported integrity
findings changes or dispositions a row.

The helper excluded by design untracked register lookalikes, tracked paths
outside sanctioned coordination shapes, archives/exports/fixtures/evaluation
copies and generated projections as live inputs, `Notes` prose and other
untyped text, foreign-register writes and automatic receiving rows, and every
inferred promotion, priority, elevation, closure, or disposition effect.

This is an invocation-local preflight only. It creates no standing sweep,
loop-entry requirement, priority, authority, lifecycle effect, or work duty.
