# APP-DEV LOOP STEER — v3 Gate 5: SCA-APP-008 application — 2026-08-23

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing transcription source. Owner: Ryan Tufts. Target workspace: App-dev loop (`projects/chirality-app-dev/`). The loop's instruments govern; this steer is the "new exact owner act" that Gate-4 section 0 requires, and it directs one bounded application tranche under the approved Gate-4 plan. Companion instruments: ruling record A8 (SHA-256 recorded in the PR that published this steer — the files merged together), and records A3 (SHA-256 `91d6867286de465f56bb41a6de9e9d8657e6b63ddb009f294d81b3e6dcccded9`), A5 (SHA-256 `1896d89200c4cd390b4606aed0229fe03bf7c5070f454e1dca5d6c6acde2bb9b`), A6 (SHA-256 `66bd22a1b439979f74bbaedf2c182d222a6ba38952ec046f78fc2091885e4e63`), and A7 (SHA-256 `56b9dc8ed8835a3220ccab10416cd9457d2a1d58b62c92582d84c773430e22d2`).

**This is the first tranche in this pathway that writes to live authoritative
truth.** Everything before it produced candidates. Read the whole steer and
the whole approved Gate-4 plan before any write.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge `c2864d63b0effd3e3685a8724d82a72f9fa8f4e1`
  (PR #660, ruling record A7) and therefore also `8a022e448…` (PR #659,
  Phase 2b / Receipt 198), `a252502af…` (PR #657, the Root K-CONTROL-1
  ratification), and `699b3eae0…` (PR #656, Phase 2 / Receipt 197).
- Approved plan artifacts: Gate-3 `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`;
  Gate-4 `47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6`.
- Approved Phase-2b transaction artifacts: K-CONTROL-1
  `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`;
  K-EVENT-4
  `c6b6d31497f0399c319b9b1772964b5c003ca1b520289cd7238d14efd84ba463`;
  reconstruction record
  `920a5f4091270d42048ab44161726ca87687624d97351d5a02840bf17617e2dd`;
  register transaction record
  `db1941c1c87ae7cd849dac3b32968a6911e74eaee8c56239725682e44b93603d`;
  superseded register candidate
  `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0`
  (see N0).
- Live target pre-images, by content SHA-256 and Git blob OID:

  | Target | SHA-256 | Blob OID |
  | --- | --- | --- |
  | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `48ae8edf982f3ce92e7a686993f3832501e42576` |
  | `docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` |
  | `execution/_Decomposition/contract_invariant_coverage_register.csv` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `ab2e13344d1ce071d2c1167320b7c875c373eaaf` |
  | `execution/_ScopeChange/_LATEST.md` | `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794` | `c6ce8b2a92c67506887d95c88790a445dbc5668d` |

  (Paths are relative to `projects/chirality-app-dev/`.)
- Must remain byte-identical throughout: App Task Management register
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`;
  frontend tree object `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`; the
  eleven frozen A2 assessment identities; every accepted Gate-1/2/3/4 and
  Phase-1/2/2b file in the snapshot; ratified Root `docs/CONTRACT.md`
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`
  and the four other A4-A Root source blobs.

## Authority context

A7-A approved the exact Phase-2b candidates and, with the Root K-CONTROL-1
amendment ratified (A5-B), satisfied the contract group's Gate-5 eligibility
prerequisites. A3-C and A5-C keep **one** Gate-5 act covering the
decomposition and contract groups together. A8-A (companion record)
authorizes this application act, resolves the register-anchor defect in N0,
and states the pointer disposition. A7-B governs the notice.

This act applies exactly the approved transactions to exactly the named
targets. It confers no carrier activation, SOW change, lifecycle
transition, dependency hand-edit, implementation dispatch, release,
publication, readiness, or reliance authority. It lifts no blocker:
TM-ROOT-106/122, C1, TM-APP-030, D-APP-97/F-APP-2, G6a, G1, the ten held
DEL-02-06 bindings, and every later gate remain exactly as they are.

## N0 — corrected companion-register candidate (do this first)

HELP_HUMAN's pre-Gate-5 verification found a defect in the A7-A-approved
register candidate `69abc8859cc…`: all 83 rows of its
`AppDecompositionBasis` column cite the decomposition candidate identity as
`932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`, which
matches no artifact that has ever existed. The true decomposition
post-image — independently reconstructed from the approved Gate-3 D-01
through D-05 transactions, 112419 bytes, and cited correctly by Gate-3,
Gate-4, ruling record A3, and all Phase-1 evidence — is
`932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`. The
defect was introduced in the Phase-2 register rebuild and carried forward
verbatim into Phase 2b. It never reached live truth: the live register
cites neither value.

Regenerate the register candidate as a **pure, deterministic anchor
correction**: replace every occurrence of the incorrect value with the true
value in the `AppDecompositionBasis` column, and change nothing else. The
corrected candidate must hash to exactly

```text
62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3
```

at 98230 bytes, 83 rows, 50 families, with the `AppDecompositionBasis`
column the only column that differs from `69abc885…`, zero occurrences of
the incorrect value, and 83 of the true value. A8-A approves that exact
identity; it supersedes `69abc885…` for application. If regeneration
produces any other identity, or if house convention would require
re-labelling the anchor (for example `candidate-sha256` to an applied-state
form), **stop and report** rather than deviate — a different label is a
different owner decision.

Independently review the corrected candidate before it is used, and record
the exact pre→post lineage (`69abc885…` → `62c9a318…`, cause, and the
one-column scope) in the run evidence and receipt. Also record that the
superseded Phase-2 and Phase-2b register candidates and their transaction
records retain the incorrect value as immutable historical artifacts and
are not to be edited.

## N1 — freeze and prove every pre-image before any write

Follow Gate-4 section 1 exactly. In particular: materialize recovery copies
from the exact Git blob OIDs in the basis-gate table into a private
temporary directory and verify their SHA-256 values there; never treat a
mutable worktree copy as rollback truth. Reconstruct every authorized
candidate in a temporary directory from the exact transactions and require
each declared post-image identity **before** replacing any live target:

| Target | Required post-image SHA-256 | Bytes |
| --- | --- | ---: |
| decomposition markdown | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | `112419` |
| `docs/CONTRACT.md` | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | `34877` |
| companion register | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | `98230` |

Also mechanically confirm, before write, that `K-CONSENT-1` and
`K-UNTYPED-1` collide with no existing invariant ID in the App contract, the
companion register, or the ratified Root contract (Gate-4 section 3
precondition; the concordance decision-input package
`4d16cefae5dc672376a62ae00437c27ff857e7d994206549e888da3409f40c2a`
records the earlier census, but re-derive it here rather than citing it).

Any mismatch aborts before write and returns the drift to the owner. Do not
rebase, paraphrase a transaction, refresh a hash opportunistically, or
re-express an application as a patch edit.

## N2 — apply the decomposition group atomically

Apply D-01 through D-05 in Gate-4 section 2 order to one candidate file,
require the full-file identity above, then atomically replace the live
target. Confirm unchanged 10-package/51-deliverable topology, stable IDs,
objectives, Scope Ledger relations, SOW relations, context-envelope
relations, and scope mappings. D-APP-103 continues to **defer**; create no
decision-replay packet in this act.

## N3 — apply the contract group atomically

Apply C-01 through C-11 in Gate-4 section 3 order, substituting the
approved Phase-2b regenerated C-01 row
`add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616` and
resolved C-06 row
`92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`.
Require the full-file identity above before replacing the live contract.
In the same atomic group, apply the N0-corrected companion register.
Never leave a changed contract beside a stale coverage claim, and never
retain a partial C-01 through C-11 state — a failure restores the whole
group including the register.

Consume the A2-B SCC orderings exactly as Gate-4 section 4 records them:
`SCC-DELEGATION-EVIDENCE`, `SCC-ACCOUNT-MIGRATION-UX`, and
`SCC-RUNBOOK-VALIDATION` are decomposed or inverted as accepted, their
non-gating feedback edges (E-020, E-018, E-032) stay non-gating, and every
named downstream gate — accepted Root/App account-consent contract, WP-03
and WP-05 fixtures, the G6a exact-candidate ruling, WP-09/WP-11 separation
— remains in force. Cut, merge, and silent linearization are forbidden.

## N4 — post-write validation, then dependency and closure reruns

Run Gate-4 section 5 direct validation, then section 6: re-extract
dependencies for the amended carriers DEL-02-05, DEL-08-04, DEL-08-05, and
DEL-09-05 through the registered extraction workflow — never hand-edit a
dependency record to mimic extraction — and dispatch the fresh named audit

```text
AUDIT_DEP_CLOSURE — SCA-APP-008-GATE5-POST-APPLICATION
```

consuming post-application decomposition and newly extracted records. A new
SCC must be surfaced, not linearized. A blocking extraction or audit result
keeps the SCA open and is recorded verbatim in the handoff; it is never
manually upgraded. The frozen Phase-0 audit PASS is assessment evidence
only and substitutes for nothing here.

Then run the full Gate-4 section 7 validator set, plus this loop's standard
gates: candidate whitespace against the basis commit **before** generating
any artifact that pins another artifact's hash, agent instructions,
instruction entrypoints, CI-form G4 (expect zero instruction-surface paths
and zero required manifests), taskmgmt validate, the App receipts
validator, the App authority-corpus reconciliation named in Gate-4 section
5.4, frontend tree identity, and `git diff --check`.

## N5 — pointer candidate, notice candidate, review, and return

- **`_LATEST.md` does not move in this tranche.** A8-B withholds pointer
  authorization. Leave the live pointer byte-identical at
  `a0298fdc…` and instead produce an exact pointer candidate — pre-image
  identity, proposed post-image bytes, and post-image SHA-256 — as an
  artifact for a separate owner act, exactly as Gate-4 section 8's fallback
  directs. Do not apply it.
- **Regenerated Root notice.** Per A7-B, produce a regenerated notice to the
  Root loop describing **applied** state (the applied decomposition and
  contract identities, the corrected register, the ratified Root
  K-CONTROL-1 row it aligns to, and what remains gated), superseding the
  frozen draft
  `DRAFT_NOTICE_TO_ROOT.md`
  `8ebc728b6d6c408a3dfeb60ae07887dbe7d5b88ba8fe06c1b954e98e8a380f72`,
  which stays byte-identical and unrouted. Mark the regenerated notice
  `READY_TO_ROUTE` with its exact identity. **Do not route it and do not
  write to any Root-loop path**; routing is carried by HELP_HUMAN to the
  owner and thence to the Root loop, which adopts, amends, or declines
  under its own instruments.
- Fresh independent review of the applied state and every artifact, with
  unlimited repair and fresh re-review; disclose every repair and, if a
  repair changes bytes that another artifact pins, regenerate that pinning
  artifact or record exact pre→post lineage.
- Close with a four-state handoff naming every applied identity, the
  pointer candidate identity, the notice candidate identity, the audit
  verdict, and every remaining blocker.

## Write set, exactly

- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
  (the D-01..D-05 post-image only).
- `projects/chirality-app-dev/docs/CONTRACT.md` (the C-01..C-11 post-image
  only).
- `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv`
  (the N0-corrected post-image only).
- Dependency records for DEL-02-05, DEL-08-04, DEL-08-05, DEL-09-05 as
  produced by the registered extraction workflow, plus the new immutable
  closure-audit package.
- New files strictly inside
  `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/`
  (additions only — every existing snapshot file is immutable), including
  the corrected register candidate, the pointer candidate, and the
  regenerated notice candidate.
- Run/control evidence under
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-<DD>/`.
- One append to `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`
  (Receipt 199; parent Receipt-198; incorporate this steer and record A8 by
  immutable path and SHA-256).

Not selectable: `execution/_ScopeChange/_LATEST.md`; the App Task
Management register; any carrier SOW, `_CONTEXT.md`, `_STATUS.md`, or
lifecycle file; any `_Evaluation` file; anything under
`projects/chirality-app-dev/frontend/` or any other
`projects/chirality-app-dev/docs/` file; every frozen assessment,
Gate-1/2/3/4, and Phase-1/2/2b artifact; any Root-loop path; `agents/**`,
`tools/**`, `AGENTS.md`, root `docs/**`, `exports/**`, `plans/**`; any
other project.

## Rollback and abort

Follow Gate-4's rollback protocol verbatim. Restore bytes from the verified
Git blob copies; never rewrite history, rebase, force-push, or use a broad
destructive checkout or reset. Preserve failure evidence inside this run
root and never claim closure from a rolled-back or partial state. If the
contract group fails, restore the contract and the register together.

## Discipline

- Branch `codex/app-v3-gate5-2026-08-<DD>`. **Do not merge.** HELP_HUMAN
  byte-verifies every applied identity, the write-set boundary, and the
  untouched-surface list before endorsement; the owner's merge is the act
  that lands the application on `main`.
- If `main` advances, a routine non-rewriting sync merge is covered by the
  standing authorization recorded verbatim in Receipt 197; record each sync
  and that citation in Receipt 199. If a sync changes any pre-image,
  post-image, or pinned identity named in this steer, **stop and report**
  instead of proceeding.
- Report a stop rather than improvising whenever an anchor, identity,
  count, or validator disagrees with this steer. A stop is a successful
  outcome of a fail-closed design.
