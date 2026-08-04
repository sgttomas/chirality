# Validation report — TM-ROOT-105 generic contract candidate

Status: `PASS_WITH_NONBLOCKING_NOTE — STRUCTURAL/CANDIDATE VALIDATION ONLY`

RunID: `ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03`

## Outcome

The candidate carrier is complete, internally consistent, hash-bound to its
declared evidence, contained to its authorized path, and independently
refuted. The terminal fresh Agent 2 verdict is
`PASS_WITH_NONBLOCKING_FINDINGS`; every blocking finding from the two earlier
failed reviews is closed.

This PASS does not accept a semantic clause, resolve a TBD, authorize
implementation, or create App/Piping reliance.

## Deterministic checks

| Check | Result | Evidence |
|---|---|---|
| signed ruling SHA-256 | `PASS` | recomputed `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06` |
| evidence-manifest shape and source hashes | `PASS` | 24 TSV rows; 24/24 paths present; 24/24 SHA-256 values match |
| structured matrices | `PASS` | `CONTRACT_MATRICES.json` parses; identity, capability, audit, interruption, budget, and fail-closed matrices present |
| TBD inventory | `PASS` | contiguous `TBD-105-01` through `TBD-105-21` present in both candidate and decision form; none selected |
| required output inventory | `PASS` | candidate, six matrix classes, consumer boundary, compatibility map, decision form, plan, three sealed reviews, validation, return, and handoff present |
| candidate/authority calibration | `PASS` | all substantive outputs state candidate/non-authority posture; activation gates distinguish semantics from implementation |
| consumer-local boundary | `PASS` | domain, operation, unit/tolerance/mapping, privacy, professional, human-acceptance, and compatibility meanings remain local/opaque |
| one implementation family / no fallback | `PASS` | exact candidate clauses and fail-closed matrix prohibit active switching and silent runtime/fixture substitution |
| capability exactness | `PASS` | exact affirmative grant/capability/resource/brief/policy conjunction plus non-allow denial; TBD-105-20 owns unresolved semantics |
| whitespace | `PASS` | `validate_candidate_whitespace.py --paths <this run>` returned clean |
| symlink/containment scan | `PASS` | no symlink exists in the run carrier; every output resolves below the authorized run root |
| Git preservation | `PASS` | branch HEAD remained `88e7590d3664d4f1daf91bed2a8899bda0748b92`; this run staged or committed nothing |

## Independent review fan-in

| Instance | Verdict | SHA-256 | Disposition |
|---|---|---|---|
| `A2-READONLY-REFUTATION` | `FAIL` | `1b11a2642527a41a54be7eae95aa05a7e39759836a00d4e0c9fd56faf7338b7f` | found stale Root doctrine claim, incomplete ALLOW conjunction, and missing grant TBD; repaired |
| `A2-READONLY-BACKCHECK` | `FAIL` | `bbc45ec6aeff42dc7a9e91e508f60970789951a572c4e3e6d8a0338fe815150b` | closed three findings; found residual exact-policy-ALLOW and grant/policy ownership gaps; repaired |
| `A2-FINAL-READONLY-REFUTATION` | `PASS_WITH_NONBLOCKING_FINDINGS` | `4a6c6bf92a6c3e5897131eb5103f4429848f6fcb3af5578acab171d3e30ba67d` | every blocking finding closed; no new package defect |

## Nonblocking fan-in note

The first review requested a separate Receipt 81 evidence-manifest row. The
repair instead uses E-023, the tranche manifest whose `m2_gate.authorization`
contains the signed owner amendment, exact Receipt 81 allocation, and no-
replacement restriction, together with E-024's routed correction and E-022's
current instruction bytes. The terminal refuter found this a substantively
sufficient signed-authority/currentness substitute. This substitution is
explicit here; no evidence or candidate repair remains.

## Commands / methods

- SHA-256 recomputation over the ruling, evidence manifest, frozen review
  artifacts, and review returns.
- TSV parsing and path/hash comparison.
- JSON parse plus required-key/matrix-count checks.
- regex set comparison over the exact TBD sequence.
- repository candidate-whitespace validator scoped to this run.
- filesystem real-path and symlink scan scoped to this run.
- `git rev-parse HEAD`, status, and staged-delta inspection.

## Rerun requirements

Rerun all deterministic checks and a fresh independent refutation if any
candidate artifact, evidence source, or hash changes. Before presenting
`TM105-SEM-A`, materialize a new no-TBD exact candidate, hash it, refresh the
compatibility map, and independently refute those exact bytes. Any
implementation requires a separate sealed implementation/check tranche after
semantic and applicable scope/affected-client gates.
