# Schema, Types, and Method Evidence Index

**State:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

| Required evidence | Result | Durable evidence |
| --- | --- | --- |
| generated JSON schema | `UNAVAILABLE_UNDER_BOUNDS` | dedicated app-server rejects `generate-json-schema`; code-mode host exposes only `--listen`; no output directory created |
| generated TypeScript types | `UNAVAILABLE_UNDER_BOUNDS` | dedicated app-server rejects `generate-ts`; code-mode host exposes only `--listen`; no output directory created |
| schema-derived exhaustive stable method inventory | `UNAVAILABLE_UNDER_BOUNDS` | cannot derive exhaustively without generated schema/types |
| schema-derived exhaustive experimental method inventory | `UNAVAILABLE_UNDER_BOUNDS` | cannot derive exhaustively without generated schema/types |
| observed bounded method/config inventory | `AVAILABLE` | `03_EMPIRICAL_EVIDENCE/METHOD_CONFIG_FEATURE_MATRIX.md` |
| exhaustive feature inventory | `AVAILABLE_118_OF_118` | `03_EMPIRICAL_EVIDENCE/FEATURE_INVENTORY.json` |

Current official App Server documentation describes wrapper invocations
`codex app-server generate-json-schema` and `codex app-server generate-ts`.
None of the three pinned assets contains that `codex` wrapper executable.
R14-B permits executing only files contained within those assets. The bounded
run therefore stopped discovery at the authorized package boundary and did
not download, install, or execute another program.

These are candidate gaps, not inferred absences from the protocol itself. An
owner accepting this candidate at G2 would do so with all four unavailable
schema/type/method outputs explicitly in view; this file makes no such
acceptance.
