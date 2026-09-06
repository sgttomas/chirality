# AC-002 bounded semantic finding

Disposition: PARTIALLY_IMPLEMENTED, documentary criterion only. Prior human AC-007 acceptance is ALIGNED, exact artifact bytes unchanged. This is not an engineering-fit rejection or lifecycle reversal. Residual is a held owner-disposition proposal, not executable Remaining.

The criterion expressly requires the decision record context to reproduce CLM-006's recorded Gate-4 basis elements. That basis includes a specific reason for isolation: nearly all §16 open decisions concern adapters, so isolation preserves those decisions cheaply. Full current ADR inspection finds related but distinct assertions: package grain is hexagonal; external implementation adapters are replaceable; contract home remains unresolved; OI001–009 and OI013 are not decided; functional core is lighter. None explicitly or equivalently classifies the open-decision population as largely adapter-level or states the economic rationale for preserving those choices. Replaceability concerns implementation interchange; a list of non-decisions records scope exclusion. Neither alone communicates the omitted rationale about the population of pending decisions. This is a narrow omission of a requested context element, not a requirement to repeat particular words.

REQ-002 remains ALIGNED because it asks context to derive from the recorded basis and introduce no new scope, which the current artifact does. AC-002 is stronger: it calls for reproduction of basis elements. VER-001 remains an ALIGNED executed inspection method, and its current outcome includes this AC-002 finding. It is not rolled into repair as a falsely failed finite suite. Historical candidate validation asserted that the adapter-level rationale was carried; that assertion is preserved but does not establish its textual presence. Final SELF_CHECK says corroborated mapping, and exact owner fitness acceptance supplies the human act, not an independent textual occurrence proof.

Owner may accept the semantic interpretation that the existing distributed statements are sufficient; alternatively the owner may authorize a bounded clarification through the frozen CHECKING change path. No prior ruling is reversed, and no new artifact acceptance is inferred.

Exact line evidence (UTF-8 line bytes without newline):

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md:82` — SHA256 of exact line `9a9525bca56e15befd31040133b8e596781532a7ba2f2daf14427ff9a2981a1a`

  - **CLM-006** — The recorded basis for the core-isolation decision is the Gate 4 exchange captured in `SOFTWARE_DECOMP.md` §Open Issues, row OI-012: the PRD invariants force the isolation properties under either candidate style (PEC-K-07 makes bridges disposable inputs; PEC-K-02 makes the store a throwaway projection; PEC-SVC-001 is the dependency-free-core rule); the package partition is congruent with a hexagonal grain (core: PKG-03/04/05 plus PKG-01 entities; driven edges: PKG-02/06 plus store; driving edges: PKG-07/08/09); nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply; the lighter functional-core/imperative-shell variant fits a deterministic-derivation service with less ceremony; the one seam to keep crisp is entity schema (core) versus store persistence (adapter) inside PKG-01.

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md:97` — SHA256 of exact line `d85afbbcd31a784208f98d909565164555b82cb282c27d461de11ecf5f2e2a00`

  - **REQ-002** — The core-isolation decision record shall state its context from the recorded Gate 4 basis (CLM-006) and shall not introduce product invariants, service rules, or scope items that are absent from the accepted PRD and decomposition.

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md:102` — SHA256 of exact line `bacc4d443e5dde3815979735e8b38b0e1bbf9844fd7c6d55082661b1478a6ea7`

  - **REQ-007** — The ADR set shall leave the §16 owner decisions OI-001 through OI-009 and the tooling follow-on OI-013 undecided; deciding any of them is out of this deliverable's scope. The recorded basis characterizes those §16 decisions as "nearly all ... adapter-level" (CLM-006), not uniformly so, and this requirement binds all nine regardless of that characterization.

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md:108` — SHA256 of exact line `8726c5b7c3d40dd3d830bd81e45da22772b484f16f6d01a5a836deb76a640587`

  - **AC-002** — That decision record's context section reproduces the recorded Gate 4 basis elements of CLM-006 and adds no invariant or service rule absent from the accepted PRD and decomposition.

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md:147` — SHA256 of exact line `5a9a2121d4b16bb5d505de6b0d37383549d48e2dcc034364438df1c93124c22b`

  | OUT-001 | SOW-088 OBJ-005 | REQ-001 REQ-002 REQ-006 CLM-006 CON-001 | AC-001 AC-002 AC-005 | VER-001 | Published core-isolation ADR |

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md:30` — SHA256 of exact line `10859ce664c6c5ca2d2cb6f0d6b7d28d2f79b62736910d4b0eadb6a1850b8706`

  The accepted Gate-4 basis records two conforming isolation styles. It also

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md:67` — SHA256 of exact line `c536145d072ee1c332a96c4765c5238b9eb17315747a5c2ad21e130b0b98399c`

  5. Functional-core / imperative-shell remains the preferred internal

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md:94` — SHA256 of exact line `c07cc314e00aa938407c02ae5ca15862e8a37cb99ac8ef83fd1b558559e44087`

  - No universal shared-types package is selected. Contract ownership and home

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md:109` — SHA256 of exact line `7188b60119153ff1cb3f924077047710a7968439728243f2f52708ccb1e9d253`

  This ADR decides none of OI-001 through OI-009 or OI-013. It creates no

- `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_run_records/D-PEC-72_CANDIDATE_VALIDATION.md:33` — SHA256 of exact line `1d3432ddb251891b9fdf1916133abd4e00e6a0a3a1c0f8ca2c6b197a58f24b90`

  | AC-002 | PASS | Context carries PEC-K-07, PEC-K-02, PEC-SVC-001, the accepted package grain, adapter-level open-decision posture, functional-core alternative, and the PKG-01 seam; no new product invariant/service rule is asserted. |
