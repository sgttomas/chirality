# N2 federation evidence — Objective V1

RunID: `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21`

InstanceID: `N2-TASK-MANAGEMENT`

Invoking loop: Root

## Mandatory preflight

Command:

```text
python3 tools/taskmgmt/taskmgmt.py federation --register execution/_Coordination/_TaskManagement/REGISTER.csv --out execution/_Coordination/_TaskManagement/.candidates/federation-n2-v1-pre-2026-08-21.json
```

Result: `COMPLETE`; four canonical registers discovered, read, and validated;
79 typed findings presented; zero operational errors; zero unresolved
ambiguities; zero register writes. The projection is rebuildable, gitignored,
and non-authoritative.

Preflight Root state: 22 live rows (`OPEN=12`, `DEFERRED=10`) and 105 archived
rows (`CLOSED=105`).

## Final federation

Command:

```text
python3 tools/taskmgmt/taskmgmt.py federation --register execution/_Coordination/_TaskManagement/REGISTER.csv --out execution/_Coordination/_TaskManagement/.candidates/federation-n2-v1-final-2026-08-21.json
```

Result: `COMPLETE`; four canonical registers discovered, read, and validated;
79 typed findings presented; zero operational errors; zero unresolved
ambiguities; zero register writes. Final Root state is 22 live rows
(`OPEN=14`, `DEFERRED=8`) and 105 archived rows (`CLOSED=105`).

Finding counts were identical before and after: 49 `FOREIGN_LINK_TO_LOCAL`,
2 `LOCAL_LINK_TO_FOREIGN`, 2 `REMOTE_CLOSED_LOCAL_OPEN`, 22
`LOCAL_CLOSED_REMOTE_OPEN`, and 4 `MISSING_NOTICE`. These are observations,
not dispositions; none was selected for work in V1.

## Register identity proof

| Loop | Live SHA-256 pre | Live SHA-256 final | Archive SHA-256 pre/final |
|---|---|---|---|
| Root | `19227d842a7c21043c20b684ec3a25ef133def2aea6c3ce12450d52a227fe3de` | `db13beefb51bef20321565faffe5f6557e9d26f76144ea871486b3d1498a8830` | `7185b82085f60ed8af669f3d6cdccb724b6d52624aa5585a171b6656d924c61b` |
| App | `ff84a9ace7722532374aa73d474ac99d34a605c30e951468076904e474a0497f` | unchanged | `8e75d44ab11b20877f86a3b57e7d27a47f60f0188d71181db120144cab51d1e6` |
| Piping | `5bad460d18782fbf7f3b370e2eca2d3518a178dfb485aa1d9386b2e9d85a064c` | unchanged | `c110c052fa2735b31c6889b8fdd7f2898d7a0194fc5bf5fbf703bc9024472192` |
| PEC | `6f7eb2a528a8a38ee01b94f5a028632d95297c82f4fa197f4c62f7102fef9264` | unchanged | `bf0d5537686d3dba23ad2e3c1b91d989850cda04e98e92dc545516829c9242b6` |

No foreign register or archive changed.
