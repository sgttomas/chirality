# DRAFT / NOT DISPATCHED — Root PIA-U30 G1-B identity validation brief

Status: `DRAFT ROOT BRIEF — REQUIRES SEPARATE AUTHORITY — NOT DISPATCHED`

## Runtime envelope

- Work unit: `PIA-U30`
- Owning loop: `Root`
- Candidate role: bounded validation executor selected by the future Root
  owning instrument; `TBD_BY_SEPARATE_ROOT_AUTHORITY`
- Parent: `HELP_HUMAN` or the Root manager named by that separate authority
- Agent type: Agent 2 only if dispatched; no delegation
- Proposed run ID and immutable evidence path: `TBD_BY_SEPARATE_ROOT_AUTHORITY`

This brief is a Root-local derivative proposal. H4 does not dispatch it and
does not grant a write target.

## Objective

Prove that one complete PIA-U10 identity for validation-target family
`chirality.app.pi-agent-engine-adapter`:

1. validates against the exact accepted PIA-U10 schema;
2. has a reproducible RFC 8785/JCS stable-identity digest and matching registry
   key;
3. cannot collide with Root's same-descriptor
   `createPiOmlxEngineAdapter` family;
4. is carried through proposed Root registry, fingerprint, event, session,
   package-evidence, and client-composition contracts without losing App
   affected-client ownership; and
5. preserves D-APP-72/SCA-APP-002 `0.80.10`, `durableResume: false`, and all
   release/reliance holds.

The work produces factual validation evidence only. It does not approve Pi
`0.82.0`, activate a registry, modify runtime contracts, supersede App, or
authorize release or reliance.

## Hard prerequisites

Stop before execution unless all are true and SHA-bound in the future launch
record:

1. owner ruling
   `OWNER_RULING_2026-08-03_S2_APPLY_PI_G1B.md` remains SHA-256
   `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`;
2. `G1B_VALIDATION_TARGET.json` remains SHA-256
   `c5b2087e070cc92cc3daecd35460497be47b6f9dff3155bde5b1cbd0aef2db01`;
3. accepted schema remains SHA-256
   `ecb9f93908d7948c7d0b4ec284745a471ff4c4a096d9cb76e4fc46c396154a5c`;
4. App has independently accepted the exact work necessary to produce the
   candidate evidence; Root's draft handoff is insufficient;
5. immutable, independently accepted PIA-U22 and PIA-U23 returns and artifact
   manifests exist at exact hashes;
6. all schema-required stable identity records listed as `TBD` in the target
   envelope have exact accepted values and provenance; and
7. a separate Root authority names the executor, runtime/tool policy, exact
   allowed write path, read set, and launch hash.

## Declared reads

The future sealed launch may permit read-only access to:

- this G1-B continuation package;
- exact accepted PIA-U20–U25 returns selected as inputs;
- exact accepted Root identity-contract candidate/validation surfaces;
- the PIA-U10 schema and field matrix;
- Root runtime contracts, registry, fingerprint, events, session, and test
  sources named by the separate authority; and
- exact App return artifacts and source hashes, without writing App.

No mutable latest pointer or branch name may substitute for an accepted input
hash.

## Proposed write boundary

One new immutable Root evaluation/test evidence directory only, with exact path
`TBD_BY_SEPARATE_ROOT_AUTHORITY`. The future launch must reject paths outside
the active checkout and must exclude `projects/*`, `runtime/*`, `docs/*`,
dependency/lock/authority/register/lifecycle/release/reliance/Task-Management,
and Git surfaces.

## Required immutable outputs

1. `BASIS.json` — launch/input hashes, dirty-state declaration, schema and
   selected family, exact accepted predecessor inventory, and tool versions;
2. `COMMANDS.jsonl` — ordered commands, cwd, redacted environment, timestamps,
   exit status, and artifact references;
3. `RESULTS.json` — schema-versioned assertions with PASS/FAIL/UNKNOWN;
4. `ADAPTER_IDENTITY.json` — complete schema-valid G1-B identity plus declared
   digest/key;
5. `STABLE_IDENTITY.jcs.json` — exact RFC 8785 canonical bytes used for digest;
6. `IDENTITY_COLLISION_TESTS.json` — positive, Root-wrapper collision,
   stable-field drift, mutable-evidence invariance, partial/unknown-field, and
   declared-digest mismatch cases;
7. `ROOT_APP_CONFORMANCE.json` — attribution across proposed registry,
   fingerprint, event, session, package evidence, and App composition fields;
8. `ARTIFACT_MANIFEST.csv` — relative path, bytes, SHA-256, provenance,
   derivative status, and evidence role;
9. `RETURN.md` — findings, limitations, blockers, reruns, and no-authority
   statement; and
10. `STATUS.json` — terminal status and criterion verdicts.

## Execution and validation contract

1. Verify every prerequisite hash before semantic work.
2. Reproduce frozen/current App hashes; stop `TARGET_DRIFT` on mismatch.
3. Validate the complete identity with Draft 2020-12 and asserted formats.
4. Execute the exact canonicalization/recomputation procedure in
   `SCHEMA_VALIDATION_CANONICAL_DIGEST_PLAN.md`.
5. Run all positive and negative collision cases in that plan.
6. Demonstrate that changing mutable evidence alone preserves the digest/key.
7. Demonstrate that the alternative Root wrapper cannot register or resolve
   under the G1-B key.
8. Verify generic proposed Root attribution surfaces carry the selected family,
   digest/key, client composition, package identity, and evidence references.
9. Verify `durableResume: false` and no broader native/sandbox/tool authority.
10. Parse all JSON/CSV, reproduce every manifest hash, scan for secrets and
    forbidden absolute paths, run candidate-whitespace and scoped
    `git diff --check`, and audit writes against the exact future path.

## Acceptance and stop rules

PASS requires every mandatory G1B-AC12/13 and Root/App conformance assertion to
pass with no UNKNOWN value, exact predecessor hashes, and no write-scope or
secret violation. Any missing input, mismatch, collision, canonicalizer
disagreement, undeclared source, or App/Root drift returns `BLOCKED` or `FAIL`.
The executor does not repair source or request a mid-run human decision.

Return to the Root manager for independent acceptance of the evidence bundle.
Even a complete PASS is not Pi approval or App supersession. Independent
EVALUATION and later human gates remain required.
