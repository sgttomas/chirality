# AB-06 return — schema/state/grant/digest candidate-design evidence

ChildID: `H4-TM105-AB06-SCHEMA-EVIDENCE/AB-06`

Terminal status:
`COMPLETED_WITH_UNRESOLVED_FACTS_AND_MECHANICAL_SCHEMA_COMPILATION_UNAVAILABLE`

Posture: `NON_AUTHORITATIVE_INCOMPLETE_CANDIDATE`; preparation only.

## Outcome

The bounded AB-06 evidence package is structurally produced. It includes a
141-row current field/type census (header plus 140 evidence rows), current
crosswalk and field classifications, six versioned Draft 2020-12 candidate
schemas, 29 transition evidence rows, grant/policy and continuation structural
requirements, three unselected canonicalization/digest alternatives, eight
positive and ten negative vectors, migration/affected-client gaps, and exact
unresolved-choice/TBD registers.

No schema, field, state, transition, issuer, evaluator, policy, right,
continuation, algorithm, canonicalization, backend, topology, migration,
compatibility, privacy, client, or value is selected. All 21 TM105 TBDs remain
open and the policy/vendor/platform/privacy/client facts remain `UNKNOWN`.

## Evidence binding

`git rev-parse --show-toplevel` resolved the active checkout; for this Root
run, `WORKING_ROOT = REPO_ROOT`.

All **41/41** evidence rows declared in `LAUNCH_BRIEF.md` were hashed before
use and matched their sealed expected SHA-256 values. Input drift is `NONE`;
no input was missing or substituted. The sealed child brief separately hashes
to `d57e4f43bd8388bee975a56ce774780d1bba1f7770446e6ce85e206d88de696c`
and was not edited.

H2/H3 returns were used only as derivative prerequisites. Current code,
schemas, tests described by the returns, and package bytes were treated as
implementation evidence, not semantic authority. TM109 was used only for its
accepted identity/provenance envelope boundary; DEL bytes only for accepted
stewardship/recovery/compatibility/degraded/affected-client/evidence scope;
TM112 only to preserve its daemon-specific non-transfer boundary.

## Package inventory

- `FIELD_TYPE_CENSUS.csv`: declared current structural types/fields,
  requiredness/types, provenance and evidence limits across all 17 declared
  current TypeScript sources.
- `CURRENT_SCHEMA_CROSSWALK.csv`: current-to-candidate concept mappings,
  TM109/DEL adjacency/non-coverage, conflicts and open disposition.
- `FIELD_CLASSIFICATION.csv`: every candidate field classified only as
  `REQUIRED_BY_CURRENT_EVIDENCE`, `OPTIONAL_BY_CURRENT_EVIDENCE`, or
  `UNKNOWN_PENDING_SEMANTIC_SELECTION`.
- `schemas/*.json`: identity, grant/policy, continuation, event/outcome,
  state/transition and digest-reference structural candidates.
- `STATE_TRANSITIONS.csv`: current, proposed-unselected, conflicting, TBD and
  DEL-scoped transitions with forbidden inference and later gates.
- `STRUCTURAL_REQUIREMENTS.md`: grant/policy and continuation requirements.
- `CANONICALIZATION_DIGEST_CANDIDATES.md`: opaque original bytes, UTF-8 JSON
  with a later profile, and typed binary with a later profile; no preference.
- `vectors/*.json`: eight positive and ten negative/unknown-version instances.
- `MIGRATION_AFFECTED_CLIENT_GAPS.csv`: Root, App, PEC, Piping, Tier-0 and
  unknown-client gaps with support/migration holds.
- `UNRESOLVED_CHOICES.md` and `IMPLEMENTATION_CRITICAL_TBDS.md`: exact choices,
  all TBDs, UNKNOWN facts, lawful gates and blockers.
- `STATUS.json` and sorted `PACKAGE_MANIFEST.sha256`: terminal machine status
  and member integrity.

## Structural design findings

1. Current identity fields are distributed across session, harness session,
   engine, project, Agent-1 run and auth records with conflicting optionality,
   namespaces and encodings. None is a complete TM105 identity.
2. Current rights vocabularies are non-identical and no declared evidence
   joins either to a qualified backend. Every AB-02 candidate remains
   `NOT_QUALIFIED`.
3. Current event/status surfaces conflict: `RuntimeEvent` and `HarnessEvent`
   differ on sequence, project attribution and cancellation; session,
   transcript, agent-run, error and DEL recovery vocabularies do not form one
   accepted terminal model.
4. No current generic continuation token exists. The candidate records only
   `existenceStatus: "TBD"`; accepted DEL no-replay/new-independent-turn rules
   remain bounded to DEL recovery scope.
5. Current SHA-256 uses bind varying implicit byte inputs. Pretty JSON, JSONL,
   token text, manifest source and other hashes are not one canonical profile.
   TM109 four-part hash carriage and DEL binding-manifest rules are bounded
   adjacency, not generic selection.
6. Root CLI/generic client and App remain affected under accepted DEL scope;
   PEC is `UNRESOLVED`; Piping and Tier-0 remain `NOT_AFFECTED` as current
   runtime-client obligations. Other clients are `UNKNOWN`; inventory absence
   is not proof of nonexistence.
7. Retention, redaction, deletion, protected-data, legal, privacy, vendor,
   platform, support and cryptographic-agility facts remain `UNKNOWN`.

## Validation performed

- Six schema JSON files and both vector JSON files parsed successfully.
- Python `jsonschema` was unavailable exactly as
  `ModuleNotFoundError: No module named 'jsonschema'`.
- Node Ajv Draft 2020-12 was unavailable exactly as
  `AJV_2020_UNAVAILABLE ERR_MODULE_NOT_FOUND`.
- Therefore Draft 2020-12 mechanical schema compilation is explicitly
  `UNTESTED_MISSING_VALIDATOR`, not passed or inferred.
- A bounded deterministic local evaluator exercised only the keywords used by
  these candidate files (`$ref`, type, required, properties,
  additionalProperties, const, enum, minLength/minimum/minItems, items,
  allOf/anyOf/not/if/then). All eight golden vectors passed and all ten
  negatives failed for their declared structural class. This is candidate
  vector evidence, not a substitute for an independent Draft validator.
- All five CSVs parsed with uniform column counts: census 141 rows/7 columns;
  crosswalk 38/8; classification 66/5; migration 16/10; transitions 30/8.
- No child-local symlink was found. Output paths remain beneath the child root.

## Blockers and reruns

Before any no-TBD successor or byte gate, every item in
`IMPLEMENTATION_CRITICAL_TBDS.md` must be resolved through attributable
evidence and the lawful human/owner gates. At minimum this includes the exact
AB-06 set `TBD-105-03/04/10/15/16/17/20/21`, all prerequisites, every
`UNKNOWN`, a qualified backend/platform/family, representative workload and
timing evidence, accepted policy/privacy/legal/vendor facts, client/version/
support-window acceptance, and the DEL epoch/binding/N3/cutover conditions in
their own scope.

Re-run schema compilation and all vectors with an installed independent Draft
2020-12 validator. Re-run cross-language byte/digest vectors only after a
human selects exact schema, canonicalization, payload-scope, algorithm and
domain-separation profiles. Re-run migration/affected-client analysis when
Root/App/PEC/other owner facts or accepted bytes change. Any input hash drift
requires a new sealed brief or explicit parent disposition; silent rebasing is
forbidden.

## Effect boundary

Terminal completion means only that this bounded evidence package was
produced. It is not semantic acceptance, schema selection, contract bytes,
backend qualification, compatibility, privacy sufficiency, implementation
readiness, conformance, safety, affected-client acceptance, lifecycle,
release, reliance, publication, Git, PR, merge, register, receipt, notice,
foreign-loop action, no-TBD successor, or byte gate. No source, test, contract,
client, store, daemon, service, credential, register, receipt, notice, Git or
PR state was changed.
