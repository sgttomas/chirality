# HELPS_HUMANS return — H2 PIA-U10 identity proposal

Status: **COMPLETE — READY FOR HUMAN G1 SELECTION — NO IDENTITY SELECTED**

## Result

PIA-U10 now has the exact seven-artifact proposal package required by plan v5.
It presents four non-inferred choices:

1. `G1-A` — Root wrapper canonical;
2. `G1-B` — App-host implementation explicitly registered;
3. `G1-C` — converged Root concrete adapter; and
4. `G1-D` — continue hold.

For every implementation target the options identify compatibility,
ownership, migration, evidence, rollback, tradeoffs, and later owning
instruments. H2 recommends no option and selects none.

The versioned schema separates the upstream Pi package/version/integrity from
the Chirality implementation family. One stable identity object binds exact
source/build, capability profile, registration, policy, client composition,
packaging, and rollback facts. Its proposed registry key is a schema-namespaced
SHA-256 over RFC 8785 canonical stable identity. Runtime fingerprint, evidence
bundle, observation time, residency epoch, live model, and verdict are grouped
under `mutable_evidence` and explicitly excluded from the key.

The options specify collision cases for the current Root/App same-descriptor
implementations, changed source/build, changed capability/policy, changed
client/packaging, evidence-only reruns, rollback changes, and changed build or
lock evidence. JSON Schema validates shape; later PIA-U30 must recompute the
digest and prove declared key equality and non-collision.

## Required artifacts

- `identity_proposal/BASIS.json`
- `identity_proposal/ROOT_PI082_IDENTITY_OPTIONS.md`
- `identity_proposal/CANDIDATE_IDENTITY.schema.json`
- `identity_proposal/IDENTITY_FIELD_MATRIX.csv`
- `identity_proposal/ARTIFACT_MANIFEST.csv`
- `instances/H2-PI-IDENTITY/RETURN.md`
- `instances/H2-PI-IDENTITY/STATUS.json`

`ARTIFACT_MANIFEST.csv` hash-binds the six other required artifacts and excludes
itself to avoid a recursive hash.

## Validation

- JSON parse: `BASIS.json`, schema, and `STATUS.json` PASS.
- Draft 2020-12 schema: local Ajv 2020 compile PASS; complete positive candidate
  instance PASS; missing `implementation.family_id` negative instance rejected.
- CSV: field matrix parses with the exact seven-column header and 58 unique
  field rows; artifact manifest parses with the exact six-column header and six
  unique paths.
- Hash manifest: every listed byte count and SHA-256 reproduces.
- Candidate whitespace over the two allowed H2 scopes: PASS.
- `git diff --check` over the two allowed H2 scopes: PASS.
- Scope audit: no H2 write exists outside the two declared directories; no Git
  action or future-work dispatch occurred.

## Interruption and write-race record

Two earlier H2 attempts were reported rejected/interrupted with no accepted
output; no return or content from them was used. In this H2 turn, `BASIS.json`
and `CANDIDATE_IDENTITY.schema.json` were written immediately before an
intentional turn interruption. The parent initially observed no terminal
return, then detected those two files after the interruption and issued a race
correction. This resumption inspected and validated those exact partial files,
completed only the five missing required artifacts, and did not rely on any
prior H2 return. Agent 0 owns correction of its provisional dispatch log.

## Preserved boundaries

- Pi `0.82.0` remains a preferred evidence candidate only.
- D-GOV-20 remains version-neutral; D-APP-72/SCA-APP-002 Pi `0.80.10` remains
  operative.
- No identity, implementation family, package ownership, migration, policy,
  capability, or rollback target is accepted.
- No project, runtime, source, dependency, lock, decision, decomposition,
  register, lifecycle, release, reliance, or Git surface was written.
- No future work unit was dispatched.

## Decision request

DecisionID: `PIA-U10-G1`

The human Root owner may select `G1-A`, `G1-B`, or `G1-C` as one target for
validation; amend the proposal; or select `G1-D` to continue the hold. Any G1
choice remains validation-target selection only. It is not Pi approval, App
supersession, App work authorization, implementation activation, release,
reliance, or Task Management closure.
