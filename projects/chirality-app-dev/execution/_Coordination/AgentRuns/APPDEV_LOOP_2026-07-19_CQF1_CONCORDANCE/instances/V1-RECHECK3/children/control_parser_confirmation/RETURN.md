# Corrected-Control Parser/Provenance Confirmation Return

- **Verdict:** `ACCEPT`
- **Role:** fresh bounded read-only Agent 2
- **Parent:** EVALUATION / V1-RECHECK3
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Subject:** `instances/R1-CONTROL-REISSUE/` plus immutable bound predecessors
- **Delegation:** none
- **Waivers:** none

## Conclusion

The corrected terminal control record withstands refutation. Its exact status
and return hashes match the sealed V1-RECHECK3 bindings. The raw status has
exactly one top-level `control_label_erratum` member, no duplicate member at
any object depth, and the required structured value and path order. A
duplicate-rejecting parser, ordinary Python, Node `JSON.parse`, and jq agree
exactly.

The immutable R1-REPAIR2 predecessor still reproduces the original duplicate
defect from its bound raw bytes: two unequal members, ordinary-parser
last-member path loss, and strict duplicate rejection. The additive record
therefore repairs V1R2-001 without rewriting or concealing it.

Independent source and control evidence establishes the corrected paths. The
control reissue did not change the 14-file derivative, proposal or source
state. Owner routing and W1 remain blocked; the separately authorized
V1-RECHECK3 is the current verifier gate. No blocking finding was found.

## Exact bindings

Recomputed with `sha256sum`:

| Artifact | SHA-256 | Result |
|---|---|---|
| R1-CONTROL-REISSUE `STATUS.json` | `0a6e4d600d26d1c71c1cb1c7f442c767f00f6ff4be854ce519fdb374800f17c0` | exact |
| R1-CONTROL-REISSUE `RETURN.md` | `f94081cf3848b387deb6e9edf74f6c104c706f014697ff14b67f2f440c6d76b6` | exact |
| R1-REPAIR2 raw `STATUS.json` | `a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44` | exact |
| R1-REPAIR2 `RETURN.md` | `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a` | exact |
| Sealed R1-REPAIR child brief | `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa` | exact |
| Sealed R1-REPAIR child return | `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0` | exact |
| V1-RECHECK2 return | `cfb858139539f038629d06279f2c259c6948dff7ede772dad48ea1b12515820e` | exact |
| V1-RECHECK2 status | `af250ce853165152321c993fe3065f2df2b36ab774c1f67e8057e493875c0fe4` | exact |
| V1-RECHECK2 protocol | `4e835f298071d92b7e18a449538143256174622ffe0903963c5197e5ddbbd50f` | exact |
| V1-RECHECK2 report | `81cf1298e32e7a263fd6f01136fe29857102ac5a21d26fb25efa622a0855a0ea` | exact |
| V1-RECHECK2 findings | `43ba5e391b2a867cda1d2cea098859b757c140ff125762ef4210dd4932025f05` | exact |
| V1-RECHECK2 handoff | `428afe00ead5b6130f18f9c5bea9c9986270c8203323ba8976c6181d79fbd4a0` | exact |
| V1-RECHECK2 technical child launch/return | `ab2cd7ebbeffc0b9d17e5e06fb0ac644d16d7d3cd9dd2ff628af62291d35d278` / `32474f641ac1de6ba55ad521466bad375ff3280c0951bc1d4e636927c655682d` | exact |
| V1-RECHECK2 governance child launch/return | `f234f799f8797b23f1f68275d79874e25f22d9f6ca8116da9b824b6f38e220fb` / `f67c7707e7e705717339374d36c4469fce7aae2f37e8845d6f24088dae2aedb3` | exact |

`git rev-parse HEAD` and `git rev-parse origin/main` both returned the exact
basis. The ordered 22-row manifest independently reproduced 22 rows, 22
unique paths, and SHA-256
`2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.

## Corrected parser evidence

Tool versions were Python 3.13.7, Node v24.5.0, and jq-1.7.1-apple.

Methods and results:

1. A Python `object_pairs_hook` accumulated member names per parsed object
   and raised on every repeated member. Parsing the corrected raw bytes
   passed with zero duplicate members at every object depth and exactly one
   encountered `control_label_erratum`.
2. An anchored raw scan for
   `^  "control_label_erratum"\\s*:` found exactly one top-level occurrence.
3. Ordinary Python `json.loads`, Node `JSON.parse`, and
   `jq -c '.control_label_erratum'` each returned the same object:

```json
{
  "classification": "NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED",
  "correct_paths": [
    "projects/chirality-app-dev/frontend/src/app/globals.css",
    "projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts"
  ]
}
```

The classification, array cardinality, both strings, and path order are
exact. There is no scalar substitute and no parser divergence.

## Immutable predecessor reproduction

The same raw scan over bound R1-REPAIR2 `STATUS.json` found exactly two
top-level occurrences. An ordered-pair parse retained these two values, in
order:

1. the structured object above; and
2. the scalar `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`.

They are unequal JSON values. The duplicate-rejecting parser rejected the
predecessor at `duplicate:control_label_erratum`. Ordinary Python, Node, and
jq all exposed only the later scalar, thereby losing both corrected paths.
The predecessor raw hash remains exactly
`a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
The new additive instance does not alter or erase that evidence.

## Corrected-path provenance

The independent path chain passes:

- `CQF1_SCOPE.csv` contains the exact corrected paths at manifest rows 1 and
  11 (CSV lines 2 and 12), both in `DEL-02-01` and both `UNASSERTED`.
- At the exact basis, `globals.css` resolves to Git blob
  `6eb6d932410368d2163208fa40ec08061a4c9bb8` and live SHA-256
  `1218ddd28db9a5a3b88d552b2e3172198937fc4968d7ce1c84a6ac16a61efd5d`.
- At the exact basis, `ansi.ts` resolves to Git blob
  `53500f33e066567f39f03978fd7f59f6b8ade9e0` and live SHA-256
  `777a846021e6c075c75d0a89a233ff86c0669bc202f7b18aa7d9eaf1ec6e2dd9`.
- Live `git hash-object` values equal both basis blobs, and both corrected
  files exist.
- The sealed child brief and return use both exact corrected paths and their
  exact source bindings. The ledger, mapping, fidelity matrix, run basis,
  updates v8/v9, R1 amendment v5, and V1 amendment v4 independently retain
  the corrected labels.
- Legacy wrong labels `frontend/src/styles/globals.css` and
  `frontend/src/lib/ansi.ts` exist neither live nor at the basis.

This supports the sustained nonconsequential classification: the corrected
control record restores machine-readable path provenance without changing a
source, package row, owner proposal, acceptance criterion, or gate.

## Unchanged derivative and gates

The activated derivative still contains exactly 14 files. Recomputed hashes
match every binding in the corrected status:

| File | SHA-256 |
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

The corrected status remains terminal and unaccepted. It records false for
owner acceptance, owner-slate release, W1 release, lifecycle transition,
publication/issuance, and Git action. R1 amendment v5 authorized no fresh V1;
V1 amendment v4 separately releases only V1-RECHECK3. That amendment still
blocks owner-slate routing and W1 until HELP_HUMAN accepts a terminal
`ACCEPT`. No ownership, authority, lifecycle, publication, or release state
is smuggled by the control reissue.

## Findings, unknowns, containment, and rerun

- **Blocking findings:** none.
- **Nonblocking findings:** none.
- **Unknowns within the sealed objective:** none.
- **Waivers:** none.
- **Subject/control/package repairs:** none.
- **Git or lifecycle actions:** none.
- **Writes:** only this `RETURN.md`; the launch brief and all subject,
  control, package, predecessor, authority, and evaluation inputs were read
  only. No delegation occurred.

Rerun or return `BLOCK` if the corrected status/return hash changes, a member
duplicates at any object depth, any parser diverges or loses either path, the
predecessor hash/defect ceases to reproduce, corrected source provenance or
package bindings drift, write containment fails, or owner/W1/lifecycle/Git
gates change without separately accepted authority.
