# DEL-02-08 Agent 2 return

- RunID: `ROOT_V3_PHASE2_2026-08-23`
- InstanceID: `DEL-02-08`
- Role: ephemeral Agent 2 generalist; role not mechanically enforced
- Delegation: none
- Result: `COMPLETE`
- Repair attempt: `2`
- Attempt-2 disposition: `ACTIONABLE_GROUNDING_CITATION_REPAIRED`
- Candidate status: `DRAFT_AWAITING_OWNER_ACCEPTANCE`

## Output and exact identity

- Path: `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/ScopeOfWork.md`
- SHA-256: `fd08461564dda82de2ec62142dedb66b37faed37de70ddcc202043ad0328f6cf`
- Carrier lifecycle remains: `OPEN`

## Exact frontmatter

```yaml
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-08
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@75c4e2ba401a6f5ad0c2f38846c39db6ab157405
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
status: DRAFT_AWAITING_OWNER_ACCEPTANCE
```

The `@75c4e2ba...` suffix is the ruled merge-commit pin required by the Phase 2
steer. The live decomposition file separately verified at SHA-256
`546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986`.

## Grounding citations

| Accepted input | Evidence used |
|---|---|
| `plans/steers/chirality_app_v3_phase2_steer_root_2026-08-23.md` | SHA-256 `bf58c6224e4649038d6faafc4a5125c20042a741f521e992f26b77b00f41d0c3`; exact form, constraints, and failure rule |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | SHA-256 `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`; exact `DEL-02-08_Exact_Supply_and_Protocol_Pinning` row |
| `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_CONTEXT.md` | SHA-256 `052cbb5e5f5fa22b321b3fbf503e82f51219ae414b2bbaa50df07a75a47f589a`; carrier description, artifacts, mappings, boundary, and planning-only locus |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` | SHA-256 `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`; §2 INIT-02 boundary |
| `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` | SHA-256 `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`; direct owner-ruling record, A7 command-network posture |
| House exemplars | DEL-02-06 and DEL-04-09 `ScopeOfWork.md`; required six-section form and output/evaluation pattern |

## Preserved constraints and exclusions

- Preserved verbatim: "exact supply/protocol pinning without any pin amendment (TM-ROOT-106/122 stay G1 blockers), OpenAI service endpoints enumerated separately from command network".
- Carried all three accepted G0 A7 per-root postures, routed
  `networkApprovalContext`, visible host/protocol, the queued-request grouping
  caveat, explicit-user-act-only `acceptForSession`, labelled
  `network_access = true`, separate OpenAI service endpoints, and G-APPR
  exact-pin prompt-delivery/grouping evidence.
- Treated the anticipated write locus as planning only.
- Added no dependency, tool, schedule, implementation selection, dispatch,
  activation, lifecycle transition, pin amendment, hold lift, or acceptance
  act.
- Stated that completion requires this deliverable's own accepted evidence;
  SOW acceptance remains a separate owner act and confers no implementation or
  dispatch authority.

## Validation evidence

- Basis-gate hashes for `AGENTS.md`, applied register, `_LATEST.md`, Task
  Management register, coordination handoff, and Phase 2 steer matched the
  steer exactly.
- `origin/main` and `HEAD` both resolved to accepted basis commit
  `a7bf601cedda23b7fd2c99d4020f4b3c2a32654b`.
- The target carrier's four Phase-1 files were byte-identical to content commit
  `dab470e2f0c7345f10c34bcce9e489eb68bf0541`; no target SOW pre-existed.
- Frontmatter inspection matched the applied register refs and required pin.
- Required body-section count: `6/6`.
- Required verbatim boundary: present.
- Attempt-2 grounding repair: the indirect SCA-004 impact-assessment and
  amendment-preview citation was replaced with direct G0 record ruling A7;
  substantive A7 content and every other SOW semantic were preserved.
- `_STATUS.md`: `OPEN`, unchanged.
- `git diff --check` on the SOW: pass.
- Write containment: only the declared SOW plus this instance's `RETURN.md`
  and `STATUS.json` were written by this instance.

## Remaining gate

The candidate is not accepted. The owner must separately accept, correct, or
decline the exact SOW bytes identified above. No later production act is
authorized by this return.
