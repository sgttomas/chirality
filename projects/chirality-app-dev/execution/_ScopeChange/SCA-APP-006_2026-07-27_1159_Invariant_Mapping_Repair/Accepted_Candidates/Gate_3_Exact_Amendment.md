# SCA-APP-006 Gate 3 — Exact Amendment Candidate

**Status:** `PREPARED_NOT_ACCEPTED`

**Accepted Gate-2 basis:** `4214915d9fcfecdc2952626421bf50b0e5f7845b`

**Current accepted main checked:** `c487b7dd57a378e2f74417118e78e7f61a161629`

**Currency result:** the App PRD, CONTRACT, decomposition, and prior tracked
SCOPE_CHANGE pointer are byte-identical between those commits. The exact
candidate is therefore anchored to the accepted Gate-2 bytes and validated
from the newer non-drifting Git basis.

## Owner decision requested

Approve, revise, or decline this complete exact amendment candidate. Approval
of Gate 3 would authorize Gate-4 propagation planning only. It would not apply
the decomposition or register, edit any `_CONTEXT.md` or ScopeOfWork contract,
repin a contract, alter APP-HOLD-1, authorize implementation, or authorize a
Git act.

## Exact candidate surfaces

| Candidate surface | Effect if later applied | SHA-256 |
|---|---|---|
| `Candidate_Tree/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Exact amended decomposition working surface. | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` |
| `Candidate_Tree/projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` | New authoritative companion register containing all exact rows. | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` |
| `Gate_3_Exact_Decomposition.patch` | Complete before/after diff for the decomposition surface. | `5aac4f33c62a4cea99ae02cd2cbdbf0bde3e24fc9fd93fa7fbae54c2eda66733` |
| `Register_Enums.json` | Closed candidate vocabularies used by all 81 register rows. | Recorded in `Gate_3_Artifact_Hashes.sha256`. |
| `validate_gate3_candidate.py` | Runnable candidate-integrity, source, owner, topology, and parity validator. | Recorded in `Gate_3_Artifact_Hashes.sha256`. |
| `compare_scope_traceability.py` | Runnable Section 8 / Section 9 comparator. | Recorded in `Gate_3_Artifact_Hashes.sha256`. |

The candidate tree is evidence only until Gate 3, Gate 4, and Gate 5 each
receive their own explicit approval. It is not the authoritative live
decomposition path.

## Exact decomposition amendments

The unified patch is the complete exact before/after record. It makes these
bounded changes:

1. records SCA-APP-006's topology-preserving posture;
2. refreshes `REF-006` to the accepted App PRD SHA-256
   `ef638f43ccae1cd78b26b1ae078a33770cf64cc36c247c5d7da04b35196a4010`;
3. changes the invariant companion register from planned to live and states
   field-level authority precedence;
4. preserves the existing `DEL-02-05` name while expanding its description
   and artifacts to truthfully carry `SOW-023`, retains the `S` envelope, and
   preserves `DEL-09-06` as attachment/security validator;
5. reconciles `SOW-002`, `SOW-023`, `SOW-064`, and `SOW-075`–`SOW-078`
   between Section 8 and Section 9 without deleting any supported relation;
6. partitions `SOW-064` so `DEL-06-02` owns App/project catalog, request
   validation, and collision prevention while `DEL-06-03` owns in-process
   wrappers and extension-boundary documentation;
7. preserves remote MCP, plugins, and marketplace scope as excluded and
   preserves `SOW-076`, `SOW-077`, and `SOW-078` as `OUT`;
8. adds `DEC-022` and one SCA-APP-006 change-log row; and
9. preserves every package, deliverable, scope-item, objective, context
   envelope, lifecycle state, dependency, estimate, schedule, and existing
   stable ID.

### Exact `DEL-02-05` / `SOW-023` partition

- `DEL-02-05` owns selected-working-root attachment selection, multi-select
  preview, remove/clear controls, and retry-preserving draft and attachment UI
  state.
- `DEL-09-06` retains resolver, server-side attachment, network, key, renderer,
  and attachment-security validation.

### Exact `SOW-064` partition

- `DEL-06-02` owns the App/project tool catalog, requested-tool validation,
  unknown-name rejection, and name-collision prevention.
- `DEL-06-03` owns the in-process deterministic MCP wrappers and their
  extension-boundary documentation.
- Neither row activates remote MCP, plugins, or marketplace scope.

## Register population and field precedence

The candidate register has exactly 81 unique invariant IDs in all 48 CONTRACT
families. Its field groups obey the precedence stated in the candidate
decomposition:

- CONTRACT controls invariant identity and normative source text.
- The accepted App decomposition controls App topology.
- The companion register controls cited mapping, coverage, and evidence
  disposition.
- A cited external-owner instrument controls externally owned semantics.
- No register row can transfer, supersede, or silently reinterpret external
  authority.

Closed enums are frozen in `Register_Enums.json`. The candidate reports:

- semantic owners: 45 `APP`, 22 `ROOT`, 14 `UNKNOWN`;
- coverage: 33 `MAPPED`, 34 `MAPPED_WITH_OPEN_ISSUE`, 4 `FUTURE_BOUNDARY`,
  and 10 `UNRESOLVED_SEMANTIC_OWNER`.

The 14 `UNKNOWN` values are explicit non-claims, not omissions:

`K-PERM-1` through `K-PERM-5`, `K-HOOK-1`, `K-BASH-1`,
`K-SUBAGENT-1`, `K-SUBAGENT-2`, `K-KEY-1`, and `K-DOMAIN-1` through
`K-DOMAIN-4`.

Their exact reasons and required dispositions are in
`Agent2_Returns/Register_Mapper/UNRESOLVED_MAPPINGS.csv`. The first ten cross
ruled Root-execution / App-project-authority seams; the four domain rows cross
Root minimums, App specializations, and external domain-truth ownership.
Gate 3 may accept those explicit unknowns or return them for a separately
source-backed partition; it may not invent singular ownership.

## Deterministic results

- integrated candidate validator:
  `PASS_WITH_EXPLICIT_UNKNOWNS`;
- exact invariant population: 81/81, 48/48 families;
- source and basis hashes: PASS;
- all closed enums: PASS;
- all App package, deliverable, validation, and open-issue references: PASS;
- stable topology: 78 scope items, 10 packages, 51 deliverables, 10 objectives;
- accepted-basis Section 8/9 mismatch set: exactly seven scope IDs;
- candidate Section 8/9 mismatch set: zero;
- additions: seven Section-8 relations and one Section-9 relation;
- supported relation deletions: zero;
- `SOW-065`, `SOW-076`, `SOW-077`, `SOW-078`: still `OUT`;
- exact patch reproduction: PASS.

## Explicitly outside this gate

Gate 3 does not approve:

- any live decomposition or register write;
- the seven enumerated candidate `_CONTEXT.md` propagation paths;
- repair of the four carried stale PKG-02 descriptive fields in
  `DEL-02-05/_CONTEXT.md`;
- any ScopeOfWork change or contract-basis repin;
- release or override of APP-HOLD-1;
- dependencies, estimates, schedules, product/runtime code, implementation,
  or lifecycle transitions;
- persistent Root validator/CI changes; or
- Git closeout.

Those boundaries remain exactly as accepted at Gate 2.
