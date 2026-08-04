# Launch brief — Root Task Management ruling application

RunID: `ROOT_TM_RULING_APPLICATION_2026-08-03`

Parent: `HELP_HUMAN`

Manager: `TASK_MANAGEMENT` (Agent 1)

Invoking loop: Root

## Objective

Apply the accountable-human rulings of 2026-08-03 to Root rows
`TM-ROOT-105`, `TM-ROOT-109`, and `TM-ROOT-121`; preserve
`TM-ROOT-112` unchanged; archive the three owner-closed rows mechanically;
and prepare the ordinary Root-to-Piping post-ruling notice without writing a
foreign register.

## Authority and accepted evidence

- Authoritative verbatim ruling:
  `execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`,
  SHA-256
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- Derivative application map:
  `execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/RULING_APPLICATION_MAP.md`,
  SHA-256
  `87ccfdbe4cf2fb89adc275b330c958c0810973096c8a6749448f3bb8bbef12a5`.

## Write scope

- `execution/_Coordination/_TaskManagement/REGISTER.csv` and its canonical
  sibling archive;
- Root Task Management session/report surfaces;
- Root ordinary notice and receipt surfaces;
- this RunID.

No source/runtime/package/App/Piping content, foreign register,
`HANDOFF_STATE.md`, lifecycle/release/reliance, or Git action is authorized.

## Acceptance checks

1. Mandatory federation preflight is `COMPLETE` before register writes.
2. Only `TM-ROOT-105`, `TM-ROOT-109`, and `TM-ROOT-121` change, each exactly
   to `CLOSED / RESOLVED_BY_DECISION` on the signed ruling.
3. Closure notes preserve the preparation-only/no-contract-byte boundaries,
   the App trigger distinction, and the separately active carrier IDs.
4. `TM-ROOT-112` is byte-identical as a row.
5. Deterministic archive dry-run and application pass; live/archive
   validation, staleness/closure echo, final federation, counts, hashes,
   containment, and whitespace checks pass.
6. The outgoing Root-to-Piping notice states exactly what is and is not
   ruled and requests no Piping-register write.

