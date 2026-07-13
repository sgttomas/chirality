# W-A2 Ordinary App Preflight Basis

Status: `CANDIDATE — AWAITING HELP_HUMAN A2-B0 FAN-IN`

This is a derivative read-only preflight package. It cites accepted upstream
truth and does not replace decomposition truth, P3 membership truth, accepted
pilot or W-A1 integration truth, deliverable truth, or Git history. It releases
no manager and authorizes no candidate generation, conversion, repair,
integration, lifecycle act, H1/H2 act, release, or retirement.

## Ref and accepted-snapshot basis

- Dispatch and synchronized main: local `HEAD`, local `main`, local
  `origin/main`, and remote `refs/heads/main` all equal
  `b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4`.
- Parent acceptance binding: the dispatch commit contains the A2 activation;
  its parent `71a5511a7785a4157f3b614e75634ace024caef3` binds the accepted W-A1
  integration evidence.
- Accepted W-A1 integration-evidence main:
  `e64ce353597fa9a5ca39dcb4d0a24e0d0cb70d7a`; both accepted commits and
  `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` are ancestors of dispatch.
- Accepted membership: `snapshots/P3_MANIFEST/EXECUTION_MANIFEST.tsv` in this
  run. The exact ordinary App subset is the 16 rows frozen in
  `A2_MANIFEST.tsv`: PKG-04=5, PKG-05=5, PKG-06=6.
- Accepted predecessors: P0/P2/P3, P4 pilots, and W-A1 acceptance packages in
  this run, plus the accepted Stage-2 workplan and active work graph.

## Decomposition and control basis

- App decomposition:
  `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4`,
  SHA-256 `a907cda33835ebf06187331c1c5937a9ae9949923c5465b17519cbd8fcaba6d4`.
- Each A2 manifest row freezes `_CONTEXT.md`, `_REFERENCES.md`,
  `_DEPENDENCIES.md`, `Dependencies.csv`, its dependency-row count, all four
  legacy source hashes, and the exact `_STATUS.md` hash.
- All paths in this derivative are repository-relative. Machine-specific
  strings inside accepted live control files are not reproduced as authority.

## Active method and consumer basis

| Surface | SHA-256 |
|---|---|
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| `tools/scope_of_work/common.py` | `c996955374833be390d8a9c0fdbb8ed0acef629204b38de8e312a963d6ea3214` |
| `tools/scope_of_work/validate_scope_of_work.py` | `f0f10590538b5aab788c120a0993a66addba6e106b352959fe11ee97511fecfe` |
| `tools/scope_of_work/convert_four_documents_to_scope_of_work.py` | `8ddef1b65f337f7091156c579558bbe8adb245a8afa43295f9d041724f203ec9` |
| `tools/scope_of_work/map_scope_of_work_claims.py` | `59f539cbf70c8428998d2a6f285c7ea30846da9163e0e0b691dcd13797b9b25f` |
| `tools/scope_of_work/report_scope_of_work_parity.py` | `a1ee956422b59013ccb02af777d70f7762e715aee850ba551f2584e6333a7576` |
| `tools/scope_of_work/derive_review_checklist.py` | `0ce012e63d873919c7ca589ce05cf1f2775259eee8312e2148677c17ab224438` |
| `tools/scope_of_work/render_scope_of_work.py` | `e0c84805ba83f55dc4ee90eead194b295bf9de3edce903e1ed419c48c19e9023` |
| `skills/scope-of-work/SKILL.md` | `4cf912e9bd164e3b52184a798265e2334ea019a651b00cb22c2582f177cc2911` |
| `skills/scope-of-work/BRIEF_SCHEMA.md` | `8ab32a83e10306c4e041337fa314c841e2d155b6b27d8f71b262426092ea7cb7` |
| `skills/scope-of-work/QA_CHECKS.md` | `b9b0d73f0d2b730b3b4b2aa3a9bf95427c06147b513f02d3865e33a2a62ccc18` |
| `skills/scope-of-work/TOOL_POLICY.md` | `f8810aa3de02d8ccbb7ba297e954f3a194d5ef04697f93de80c613a08774058e` |
| `projects/chirality-app-dev/software-workflow.json` | `21344b177d8e489f0b85a840baef8fd85a3f280f7a9d6d77e5e8e885e12549ac` |
| App deliverable scanner `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts` | `3f3a45c6dd09c35e51f22f651399f70fbae33a17021ebdf531e192ee11b2dc3f` |

Accepted P2 caller prerequisites remain bound by root caller-manifest SHA-256
`6fb003fb5ae265bae3df1a197c4718b448e912879c74abaa9d6c778b8604ae85`
and App caller-manifest SHA-256
`b2511fd3caa365c4a561e90dee49b737933e292321637fb44c2c69425bbf9771`.
The accepted closure proves 64/64 root and 9/9 App callers classified, legacy
and SOW supported, and missing, partial, invalid, or unauthorized dual states
fail closed.

## Frozen execution contract

If HELP_HUMAN accepts this preflight, it may separately release the three
PARKED managers in `PACKAGE_PLAN.tsv`. Each deliverable uses a sealed
`TASK + scope-of-work`, `MODE=CONVERT` author followed by a separate verifier.
The author may write only the listed candidate and author evidence. The
verifier may write only verifier evidence and may not repair the candidate.
Both bind exact row hashes and the exact migration authority. Package-manager
candidate/evidence scopes are pairwise disjoint; all project deliverable paths
remain read-only until a later accepted RECONCILIATION manifest is serially
integrated by CHANGE.

The future atomic live-tree delta per accepted member is exactly:

```text
A  ScopeOfWork.md
D  Datasheet.md
D  Specification.md
D  Guidance.md
D  Procedure.md
```

`_STATUS.md` and every other control file must remain byte-identical. The
inverse five-row rollback must be frozen before integration. A PASS here is a
recommendation for HELP_HUMAN fan-in only, not a release or integration act.
