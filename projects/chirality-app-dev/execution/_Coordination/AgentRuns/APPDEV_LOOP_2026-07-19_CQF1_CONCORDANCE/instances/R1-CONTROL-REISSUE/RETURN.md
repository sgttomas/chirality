# R1-CONTROL-REISSUE Terminal Return

- **Role:** RECONCILIATION
- **Parent:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Status:** `COMPLETE_UNIQUE_MEMBER_CONTROL_REISSUE`
- **Accepted by parent:** no; fan-in pending
- **Downstream release:** false

## Outcome

R1-CONTROL-REISSUE resolved only V1R2-001/GPE-001 by issuing a new additive
terminal control record with exactly one structured `control_label_erratum`
member. Its value contains the sustained classification and both corrected
paths in required order. R1-REPAIR2, its 14-file derivative, every sealed
child and evaluation input, subject state, authority, and Git state remain
unchanged.

No substantive row, mapping, group, candidate, blocker, or owner choice was
changed or accepted. No waiver was used.

## Mandatory immutable-input preflight

`PASS_EXACT` before status mutation:

- `HEAD` = `origin/main` = exact basis.
- `CQF1_SCOPE.csv`: 22 rows, 22 unique, 22 existing, exact order; ordered
  path-list SHA-256
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- Five Remaining populations remain DEL-02-01 14, DEL-03-03 1, DEL-06-02 1,
  DEL-09-04 4, and DEL-10-04 2. Each owning `_STATUS.md` remains
  `IN_PROGRESS` and basis-identical.
- All 22 source blobs and SHA-256 values reproduce from the exact basis and
  live files. Relied-on subject, status, dependency, decision/authority, and
  decomposition surfaces show no tracked drift from the basis.
- R1-REPAIR2 return/raw status matched
  `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a`
  and
  `a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
- The sealed child launch/return matched
  `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`
  and
  `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
- V1-RECHECK2 return/status, evaluation protocol/report/findings/handoff,
  technical child launch/return, and governance child launch/return matched
  all ten exact launch-brief bindings.
- The instance initially contained only its immutable `LAUNCH_BRIEF.md` and
  released nonterminal `STATUS.json`; this instance was the sole write root.

## Immutable predecessor defect reproduction

V1R2-001 was reproduced against the bound raw R1-REPAIR2 status before the
reissue:

- exactly two top-level members had the name `control_label_erratum`;
- the first value was the structured object and the second was a scalar
  string, and the values were unequal;
- ordinary Python, Node, and jq parsing retained the later scalar and lost
  both corrected paths; and
- a duplicate-rejecting Python `object_pairs_hook` rejected the raw status at
  the repeated member.

The predecessor remains immutable at its exact raw SHA-256. This reissue
records V1R2-001 as `REPAIRED_BY_ADDITIVE_CONTROL_REISSUE`; it does not erase
or recode the verifier finding.

## Unique structured member

The terminal `STATUS.json` contains exactly one top-level
`control_label_erratum` member with this exact structured value:

```json
{
  "classification": "NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED",
  "correct_paths": [
    "projects/chirality-app-dev/frontend/src/app/globals.css",
    "projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts"
  ]
}
```

The classification, two paths, and array order are exact. There is no scalar
substitute and no second member with that name.

## Required parser validation

All checks passed over the final raw `STATUS.json` bytes:

| Check | Deterministic method | Tool/version | Result |
|---|---|---|---|
| Raw top-level occurrence | Anchored member-name scan at object indentation | Python 3.13.7 | exactly 1 |
| Duplicate rejection | `json.loads(raw, object_pairs_hook=reject_duplicates)`; hook rejects repeats for every parsed object | Python 3.13.7 | pass; no duplicate at any depth |
| Ordinary Python | `json.load` plus exact object equality | Python 3.13.7 | pass; exact structured value |
| Ordinary Node | `JSON.parse` plus ordered JSON equality | Node v24.5.0 | pass; exact structured value |
| Ordinary jq | `jq -e` exact object equality | jq-1.7.1-apple | pass; exact structured value |

All four accepted representations expose the same object, classification,
two-path array, and path order. Final terminal status SHA-256:

`0a6e4d600d26d1c71c1cb1c7f442c767f00f6ff4be854ce519fdb374800f17c0`.

## Unchanged derivative bindings

All 14 R1-REPAIR2 package files remain byte-identical:

| Package file | SHA-256 |
|---|---|
| `AFFINITY_AND_MAPPING_ANALYSIS.md` | `1e825d797ddf5c4a9757bb1984ae63be0bf6b053736fe1bd5a8f932d415d4035` |
| `CANDIDATE_OWNER_SLATE.md` | `f6e630e9294c4779f87a0f7734667f565113127769cdaed3ab20b32cd099ce93` |
| `CQF1_PATH_LEDGER.csv` | `b56f87731920765279639d528393bae212403fe49ffb5de6c27065ddd4095288` |
| `DECISION_CLASSIFICATION.md` | `4f7d8d41b344daafd7f4533dcaaec5dc4859fa44561133181ce744006ed285fd` |
| `DEL02_01_CHILD_PACKAGE_FIDELITY.csv` | `100445dd4e2054440776a60e1be36e53d7cdb0bf6cbe94b9e21555f420f1706c` |
| `HANDOFF.md` | `9af95a170fa77149fac4cbe5bae7320e5abe357b39434a5c083a200ba80dbc75` |
| `PACKAGE_NOTES/DEL-02-01.md` | `0045d350a15c5fae07d0a0958096477c8fc057aedb8227cc433947feb3e6dafa` |
| `PACKAGE_NOTES/DEL-03-03.md` | `1ae7d3e728093a853e79240da5eaa91ce6407dc0c67a3b4c10a3cd3c656f6935` |
| `PACKAGE_NOTES/DEL-06-02.md` | `cd0b5b206c3ede37fb1eb3130b5a12cfece15ed1a1b498159ece87aed619f299` |
| `PACKAGE_NOTES/DEL-09-04.md` | `946d03791ae296397b39c8322dd6c48d6daf21bd65489ba07f24558045cb8a48` |
| `PACKAGE_NOTES/DEL-10-04.md` | `9a5e5291e30d3deb9a04992080c406c1499489b1696ee6fd361c4d27385fb59e` |
| `PROPOSED_MAPPING.csv` | `a01651fb49883d2f15971cbc8a85c5cff4c5039eeffb2500be6a78fd62378e86` |
| `QA.md` | `8cf4c42184a1ccd73577e11180562e2b9a576a9063728f4fd3c410227e92dbfd` |
| `RUN_BASIS.md` | `f752abe6d078ec3f485621a9b1f15476db0667642bfb591ed20420d97c2e537d` |

The two proposal CSVs remain valid 22×13 and 22×7 schemas in exact manifest
order with 22 `OWNER_CLASS` rows. The owner slate remains nine groups with
population `5+4+6+1+1+1+1+1+2=22`. The fidelity matrix remains 14×19 with
5 `EXACT`, 5 `FAITHFUL_COMPRESSION`, 4 `REPAIRED_MATERIAL_LOSS`, 0
`EXPLICITLY_REASONED_REJECTION`, and 0 unexplained rows. Package count,
source bindings, final-LF, horizontal-whitespace, and diff hygiene remain
exact.

V1-001 through V1-004 remain sustained; V1R-001 and V1R-002 remain repaired
and sustained; V1R2-002 retains the earlier wrong-label erratum; V1-005
remains a nonblocking unrepaired observation.

## Changed-path accounting and containment

This attempt wrote only:

1. `instances/R1-CONTROL-REISSUE/STATUS.json`; and
2. `instances/R1-CONTROL-REISSUE/RETURN.md`.

The launch brief is unchanged. There were zero derivative-package, subject,
Remaining, SOW/dependency, authority, lifecycle, decision/register/receipt,
plan/graph, evaluation, predecessor, child, or Git writes. No delegation was
used. Containment and per-file diff hygiene passed.

## Blockers, waivers, and next gate

- Requested next gate: HELP_HUMAN accepts this terminal control reissue, then
  separately releases exactly one fresh independent V1 bound to the corrected
  status hash.
- Fresh V1: not released or run by this attempt.
- Owner-slate routing and W1: blocked and unreleased.
- Owner acceptance: absent.
- Lifecycle transition, issuance, publication, and Git action: none.
- Waivers: none.
- Rerun on duplicate member, parser divergence, path loss, input drift,
  package-hash change, write escape, or unauthorized downstream release.
