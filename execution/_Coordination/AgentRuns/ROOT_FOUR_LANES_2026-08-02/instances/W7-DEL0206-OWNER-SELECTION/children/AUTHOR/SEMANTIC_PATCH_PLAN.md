# DEL-02-06 future semantic patch plan

- Status: `DERIVATIVE_MAPPING_NOT_AN_EDIT_INSTRUCTION_FOR_CURRENT_BYTES`
- Coverage: every option for D1-D9, TBD-001..TBD-016, CENSUS, and
  COMPAT-DELTA.

## Future-version rule

`V{NN}` means a new, owner-named two-digit semantic-candidate sequence. The
selected sequence is used consistently across the package. A future authorized
writer must create new files at the paths below, bind their exact hashes in a
new immutable manifest, and leave all current `accepted_inputs/`, `integration/`,
`handoff/`, W6, W6-R1, and W7 author bytes unchanged. No path in this plan is a
current write authorization.

Path keys resolve exactly under:

`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/future_semantic_candidates/V{NN}/`

| Key | Exact future versioned-candidate file |
|---|---|
| `DEC` | `OWNER_DECISIONS_CANDIDATE_V{NN}.md` |
| `REC` | `RECOVERY_SPEC_CANDIDATE_V{NN}.md` |
| `EVD` | `RECOVERY_EVIDENCE_SCHEMA_CANDIDATE_V{NN}.md` |
| `STO` | `RECOVERY_STORAGE_CONTRACT_CANDIDATE_V{NN}.md` |
| `DEG` | `DEGRADED_MODE_CONTRACT_CANDIDATE_V{NN}.md` |
| `CUT` | `CUTOVER_ROLLBACK_CANDIDATE_V{NN}.md` |
| `COM` | `ROOT_COMPATIBILITY_POLICY_CANDIDATE_V{NN}.md` |
| `BND` | `COMPATIBILITY_BINDING_CANDIDATE_V{NN}.md` |
| `CEN` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V{NN}.md` |
| `EVP` | `RECOVERY_EVIDENCE_PLAN_CANDIDATE_V{NN}.md` |
| `CDL` | `COMPATIBILITY_DISPOSITION_CANDIDATE_V{NN}.md` |

Every created file must cite accepted Scope-of-Work SHA-256
`dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`,
the accepted packet-manifest SHA-256
`360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f`,
and handoff SHA-256
`bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`.

## Required rerun sets

- `VR-ROOT`: regenerate the complete V{NN} package and manifest; rerun
  applicable basis, integration, 27-row completeness, internal-reference,
  dependency, and no-effect checks; then run a genuinely fresh read-only
  semantic refutation. Any material finding returns to the authoring/human
  gate; the refuter does not repair.
- `VR-COMPAT`: `VR-ROOT` plus identity-grammar, exact-equality, mismatch,
  binding, epoch, and conditional-delta consistency checks across `COM`, `BND`,
  `CDL`, `CEN`, and `REC`.
- `VR-CENSUS`: rerun affected-client determination against the adopted exact
  Root contract; verify accepted-obligation sources and all five
  classifications; route client-owned evidence without writing client bytes;
  then perform `VR-ROOT`.
- `VR-FOREIGN`: verify Root text only retains, routes, or states no current
  Root effect. Any App, PEC, Piping, or Tier-0 semantic outcome requires its
  owning instrument and a later Root census rerun; then perform `VR-CENSUS`.
- `VR-EVIDENCE`: statically validate complete N3-R01..N3-R16 and RR-01..RR-18
  coverage and exact contract/fixture/result binding; results remain
  `DESIGNED_NOT_EXECUTED`; then perform `VR-ROOT`.
- `VR-DEFER`: verify no selected semantic value is inserted, retain the row as
  unresolved/deferred, and rerun the 27-row completeness/no-effect review.

## No-effect fences

- `F-ROOT`: no edit to current accepted/candidate/handoff bytes; no semantic
  adoption, implementation, executable check, runtime/client/project write,
  profile/check adoption, dependency, SCA/decomposition/PRD, Task Management,
  lifecycle, release, publication, issuance, reliance, Git, PR, or merge effect.
- `F-FOREIGN`: `F-ROOT` plus no App, PEC, Piping, or Tier-0 selection, work,
  dependency, veto, byte, or foreign-loop effect.
- `F-DEFER`: `F-ROOT` plus no narrowing by implication and no silence-as-choice.

## Complete option-to-patch mapping

The locator after `#` is the mandatory future heading or placeholder ID.

| Row | Option | Future path and locator | Dependencies | Validation/refutation reruns | Fence |
|---|---|---|---|---|---|
| D1 | `D1-A_INTERRUPTED_WITH_RECOVERY_PAYLOAD` | `REC#D1-OWNER-SELECTED-RECOVERY-TERMINAL-POLICY-A` | D4, D7, TBD-006, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D1 | `D1-B_NEW_RECOVERY_TERMINAL` | `REC#D1-OWNER-SELECTED-RECOVERY-TERMINAL-POLICY-B`; new vocabulary also enumerated at `EVD#D1-NEW-TERMINAL-SCHEMA` | D3, D4, D7, TBD-006, TBD-016 | VR-ROOT, VR-EVIDENCE, VR-COMPAT | F-ROOT |
| D2 | `D2-A_NEW_TURN_EXPLICIT_RETRY` | `REC#D2-OWNER-SELECTED-RETRY-POLICY-A` | D1, D4, D7, TBD-006, TBD-008 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D2 | `D2-B_NO_RETRY_FOR_INDETERMINATE` | `REC#D2-OWNER-SELECTED-RETRY-POLICY-B` | D1, D7, TBD-006, TBD-008 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D3 | `D3-A_CANONICAL_HASHED_AUDIT` | `EVD#D3-AUDIT-SCHEMA-A`; cross-reference at `REC#D3-AUDIT-BINDING` | D4, D7, D8, TBD-008, TBD-014 | VR-EVIDENCE | F-ROOT |
| D3 | `D3-B_MINIMAL_EVENT_LINKED_AUDIT` | `EVD#D3-AUDIT-SCHEMA-B`; evidence limitation at `DEC#D3-OWNER-ACKNOWLEDGED-LIMITATION` | D4, D7, D8, TBD-008, TBD-014 | VR-EVIDENCE | F-ROOT |
| D4 | `D4-A_PER_TURN_ATOMIC_RECONCILIATION` | `STO#D4-TRANSACTION-BOUNDARY-A`; referenced by `REC#D4-PER-TURN-DURABILITY` | D1, D3, D7, D9, TBD-006 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D4 | `D4-B_WHOLE_CORPUS_ATOMIC_RECONCILIATION` | `STO#D4-TRANSACTION-BOUNDARY-B`; referenced by `REC#D4-CORPUS-DURABILITY` | D1, D3, D7, D9, TBD-006 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D5 | `D5-A_COUNT_UNTIL_DURABLE_DISPOSITION` | `REC#D5-DRAIN-ACCOUNTING-A` | D4, D6, D8, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D5 | `D5-B_QUARANTINE_UNKNOWN_WITH_GLOBAL_LATCH` | `REC#D5-DRAIN-ACCOUNTING-B`; latch cross-reference at `DEG#D5-UNKNOWN-ATTRIBUTION-HOLD` | D4, D6, D8, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D6 | `D6-A_STRICT_LATCH_WITH_READ_ONLY_INSPECTION` | `DEG#D6-READINESS-AND-RETAINED-FUNCTIONS-A`; Root-only matrix at `REC#D6-ROOT-RETAINED-FUNCTIONS` | D3, D5, D7, D8, TBD-009 | VR-ROOT, VR-CENSUS | F-FOREIGN |
| D6 | `D6-B_STRICT_LATCH_NO_RUNTIME_ENDPOINTS` | `DEG#D6-READINESS-AND-RETAINED-FUNCTIONS-B` | D5, D7, D8, TBD-009 | VR-ROOT, VR-CENSUS | F-FOREIGN |
| D7 | `D7-A_SESSION_QUARANTINE_GLOBAL_READINESS_HOLD` | `REC#D7-MALFORMED-EVIDENCE-A`; evidence rules at `EVD#D7-PRESERVATION-AND-REPAIR-AUTHORITY` | D3, D4, D6, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D7 | `D7-B_WHOLE_CORPUS_QUARANTINE` | `REC#D7-MALFORMED-EVIDENCE-B`; evidence rules at `EVD#D7-CORPUS-QUARANTINE` | D3, D4, D6, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D8 | `D8-A_EVENT_BOUND_ATTRIBUTION_TUPLE` | `EVD#D8-ATTRIBUTION-SCHEMA-A`; referenced by `REC#D8-TURN-ATTRIBUTION` | D3, D5, D7, TBD-016 | VR-EVIDENCE | F-ROOT |
| D8 | `D8-B_BATCH_BOUND_ATTRIBUTION_WITH_UNKNOWN` | `EVD#D8-ATTRIBUTION-SCHEMA-B`; limitation at `DEC#D8-UNKNOWN-PER-TURN-DIMENSIONS` | D3, D5, D7, TBD-016 | VR-EVIDENCE | F-ROOT |
| D9 | `D9-A_STAGED_SCAN_CUTOVER_RESTORE` | `CUT#D9-CUTOVER-ROLLBACK-A` | D1, D2, D3, D4, TBD-006, TBD-014 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| D9 | `D9-B_DEFER_CUTOVER` | `DEC#D9-CUTOVER-DEFERRED` | none; later exact plan required | VR-DEFER | F-DEFER |
| TBD-001 | `TBD001-A_ROOT_OPAQUE_EPOCH_GRAMMAR` | `COM#TBD-001-COMPATIBILITY-IDENTITY-A` | COMPAT-DELTA, TBD-004, TBD-015 | VR-COMPAT | F-ROOT |
| TBD-001 | `TBD001-B_ROOT_SEMVER_GRAMMAR` | `COM#TBD-001-COMPATIBILITY-IDENTITY-B` | COMPAT-DELTA, TBD-004, TBD-015 | VR-COMPAT | F-ROOT |
| TBD-002 | `TBD002-A_AUTHENTICATED_PREFLIGHT_EQUALITY` | `COM#TBD-002-DECLARATION-AND-COMPARISON-A` | TBD-001, TBD-003 | VR-COMPAT | F-ROOT |
| TBD-002 | `TBD002-B_PER_REQUEST_DECLARATION_EQUALITY` | `COM#TBD-002-DECLARATION-AND-COMPARISON-B` | TBD-001, TBD-003 | VR-COMPAT | F-ROOT |
| TBD-003 | `TBD003-A_TYPED_COMPATIBILITY_MISMATCH` | `COM#TBD-003-MISMATCH-ENVELOPE-A`; Root presentation only at `REC#TBD-003-ROOT-PRESENTATION` | TBD-001, TBD-002, TBD-007, TBD-008 | VR-COMPAT, VR-CENSUS | F-FOREIGN |
| TBD-003 | `TBD003-B_GENERIC_PROTOCOL_MISMATCH` | `COM#TBD-003-MISMATCH-ENVELOPE-B`; limitation at `DEC#TBD-003-GENERIC-CLASS-LIMITATION` | TBD-001, TBD-002, TBD-007, TBD-008 | VR-COMPAT, VR-CENSUS | F-FOREIGN |
| TBD-004 | `TBD004-A_IMMUTABLE_BINDING_MANIFEST` | `BND#TBD-004-BINDING-RECORD-A` | TBD-001, CENSUS, TBD-014, COMPAT-DELTA | VR-COMPAT, VR-CENSUS, VR-EVIDENCE | F-ROOT |
| TBD-004 | `TBD004-B_DEFER_BINDING` | `DEC#TBD-004-BINDING-DEFERRED` | later exact binding design | VR-DEFER, VR-COMPAT | F-DEFER |
| TBD-005 | `TBD005-A_ACCEPT_CURRENT_CENSUS_BOUNDARIES` | `CEN#TBD-005-CENSUS-DISPOSITION-A` | CENSUS, TBD-009, TBD-011, TBD-013 | VR-CENSUS, VR-FOREIGN | F-FOREIGN |
| TBD-005 | `TBD005-B_RETURN_CENSUS_FOR_NEW_EVIDENCE` | `CEN#TBD-005-CENSUS-DISPOSITION-B` | new accepted-obligation evidence | VR-DEFER, VR-CENSUS | F-FOREIGN |
| TBD-006 | `TBD006-A_STAGED_FAIL_CLOSED_MIGRATION` | `CUT#TBD-006-MIGRATION-AND-INDETERMINATE-BEHAVIOR-A` | D1, D2, D4, D9 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| TBD-006 | `TBD006-B_DEFER_MIGRATION_SEMANTICS` | `DEC#TBD-006-MIGRATION-SEMANTICS-DEFERRED` | later D1/D2/D4/D9 package | VR-DEFER | F-DEFER |
| TBD-007 | `TBD007-A_DISTINCT_TEN_CONDITION_CLASSES` | `DEG#TBD-007-TYPED-FAILURE-CLASSES-A` | D1, TBD-003, TBD-008, TBD-016 | VR-ROOT, VR-COMPAT, VR-EVIDENCE | F-ROOT |
| TBD-007 | `TBD007-B_BOUNDARY_GROUPED_CLASSES` | `DEG#TBD-007-TYPED-FAILURE-CLASSES-B`; non-collapse proof at `EVP#TBD-007-GROUPING-PROOF` | D1, TBD-003, TBD-008, TBD-016 | VR-ROOT, VR-COMPAT, VR-EVIDENCE | F-ROOT |
| TBD-008 | `TBD008-A_TOTAL_PRECEDENCE_DENY_DEFAULT_RETRY` | `DEG#TBD-008-PRECEDENCE-RETRY-AND-EVIDENCE-A` | D2, D3, TBD-007, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| TBD-008 | `TBD008-B_PARTIAL_PRECEDENCE_TABLE` | `DEG#TBD-008-PRECEDENCE-RETRY-AND-EVIDENCE-B`; unresolved pairs at `DEC#TBD-008-UNORDERED-PAIRS` | D2, D3, TBD-007, TBD-016 | VR-ROOT, VR-EVIDENCE | F-ROOT |
| TBD-009 | `TBD009-A_ROUTE_SEPARATE_CLIENT_MATRICES` | `CEN#TBD-009-CLIENT-MATRIX-ROUTES-A` | D6, CENSUS, TBD-011, TBD-014 | VR-FOREIGN, VR-CENSUS | F-FOREIGN |
| TBD-009 | `TBD009-B_RETAIN_ALL_CLIENT_MATRICES_UNRESOLVED` | `CEN#TBD-009-CLIENT-MATRIX-ROUTES-B` | later client-owned rulings | VR-DEFER, VR-FOREIGN | F-FOREIGN |
| TBD-010 | `TBD010-A_ROUTE_TIER0_RELATIONSHIP_ACT` | `DEC#TBD-010-TIER0-ROUTE-A` | TBD-001, TBD-004 | VR-FOREIGN | F-FOREIGN |
| TBD-010 | `TBD010-B_RETAIN_WITHOUT_TIER0_ACT` | `DEC#TBD-010-TIER0-ROUTE-B` | none | VR-DEFER, VR-FOREIGN | F-FOREIGN |
| TBD-011 | `TBD011-A_RETAIN_PEC_UNRESOLVED_AND_ROUTE` | `CEN#TBD-011-PEC-UNRESOLVED-ROUTE-A` | CENSUS, TBD-009 | VR-FOREIGN, VR-CENSUS | F-FOREIGN |
| TBD-011 | `TBD011-B_STATE_NO_CURRENT_ROOT_EFFECT_WITHOUT_ROUTE` | `CEN#TBD-011-PEC-UNRESOLVED-ROUTE-B` | later PEC-owned evidence may reopen census | VR-FOREIGN, VR-CENSUS | F-FOREIGN |
| TBD-012 | `TBD012-A_NO_SEAM_PROVEN_ROUTE_IF_EVIDENCED` | `DEC#TBD-012-OWNERSHIP-SEAMS-A` | CENSUS | VR-ROOT, VR-CENSUS | F-FOREIGN |
| TBD-012 | `TBD012-B_RETURN_FOR_SEAM_DISCOVERY` | `DEC#TBD-012-OWNERSHIP-SEAMS-B` | new source-cited evidence | VR-DEFER | F-DEFER |
| TBD-013 | `TBD013-A_STATE_NO_CURRENT_ROOT_EFFECT` | `CEN#TBD-013-PIPING-STATUS-A` | CENSUS | VR-FOREIGN, VR-CENSUS | F-FOREIGN |
| TBD-013 | `TBD013-B_ROUTE_FOR_PIPING_REVIEW` | `CEN#TBD-013-PIPING-STATUS-B` | later Piping-owned accepted obligation | VR-FOREIGN, VR-CENSUS | F-FOREIGN |
| TBD-014 | `TBD014-A_N3_MATRIX_AS_MINIMUM_OBLIGATION` | `EVP#TBD-014-CONFORMANCE-AND-REGRESSION-A` | D1-D9, CENSUS | VR-EVIDENCE, VR-CENSUS | F-ROOT |
| TBD-014 | `TBD014-B_REDESIGN_MATRIX_BEFORE_SEMANTICS` | `DEC#TBD-014-EVIDENCE-MATRIX-RETURNED` | new evidence design and fresh refutation | VR-DEFER, VR-EVIDENCE | F-DEFER |
| TBD-015 | `TBD015-A_ADOPTION_CAUSES_NEW_EPOCH` | `COM#TBD-015-EPOCH-CRITERIA-A`; conditional disposition at `CDL#TBD-015-DELTA-LINK` | TBD-001, TBD-004, COMPAT-DELTA | VR-COMPAT, VR-CENSUS | F-ROOT |
| TBD-015 | `TBD015-B_DEFER_EPOCH_CRITERION` | `DEC#TBD-015-EPOCH-CRITERION-DEFERRED` | later compatibility decision | VR-DEFER, VR-COMPAT | F-DEFER |
| TBD-016 | `TBD016-A_EXPLICIT_RECOVERY_STATE_MACHINE` | `DEG#TBD-016-DAEMON-RECOVERY-STATE-A` | D1-D8, TBD-007, TBD-008 | VR-ROOT, VR-EVIDENCE, VR-COMPAT | F-ROOT |
| TBD-016 | `TBD016-B_RETAIN_STATE_CLASSES_UNRESOLVED` | `DEC#TBD-016-STATE-CLASSES-DEFERRED` | later D1-D8 decision package | VR-DEFER | F-DEFER |
| CENSUS | `CENSUS-A_ACCEPT_CURRENT_CLASSIFICATIONS` | `CEN#CENSUS-OWNER-DISPOSITION-A` | TBD-005, TBD-009, TBD-011, TBD-013 | VR-CENSUS, VR-FOREIGN | F-FOREIGN |
| CENSUS | `CENSUS-B_RETURN_FOR_NEW_EVIDENCE` | `CEN#CENSUS-OWNER-DISPOSITION-B` | new accepted-obligation evidence | VR-DEFER, VR-CENSUS | F-FOREIGN |
| COMPAT-DELTA | `COMPATDELTA-A_DELTA_IF_RECOVERY_ADOPTED` | `CDL#COMPATIBILITY-DELTA-DISPOSITION-A` | TBD-001, TBD-004, TBD-005, TBD-015, CENSUS | VR-COMPAT, VR-CENSUS | F-ROOT |
| COMPAT-DELTA | `COMPATDELTA-B_DEFER_DISPOSITION` | `CDL#COMPATIBILITY-DELTA-DISPOSITION-B` | later recovery-adoption and epoch decisions | VR-DEFER, VR-COMPAT | F-DEFER |

## Sequence after a valid owner choice

1. A separately authorized future writer instantiates `V{NN}` and only the
   option locators selected by the owner, while preserving every dependency and
   unresolved foreign gate.
2. The writer creates a complete immutable package and hash manifest; current
   bytes remain untouched.
3. The applicable rerun sets above execute. The fresh refuter is read-only and
   cannot repair.
4. Only exact accepted future semantic bytes can become semantic truth. A
   selection response, this mapping, a successful static check, or silence is
   not adoption.
5. Implementation remains held for a separate sealed activation binding exact
   source, contract, fixtures, reads, writes, checks, rollback, and return
   identities. App, PEC, Piping, and Tier-0 continue under their own owners.
