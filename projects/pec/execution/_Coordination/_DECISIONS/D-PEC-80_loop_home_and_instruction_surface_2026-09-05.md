# D-PEC-80 — PEC canonical loop home, generic init, and run-based PR boundary

Status: `PROPOSAL — AWAITING_RULING`

DecisionID: `D-PEC-80`

Date: `2026-09-05`

Owner: Ryan Tufts

Prepared by Codex acting as HELP_HUMAN; role not mechanically enforced.
The analysis, classification, and candidate choices are the agent's. No owner
acceptance of these candidate bytes is asserted. D-PEC-79 is reserved by the
already-adopted, unapplied PRD candidate; this packet does not reuse that ID.

## Basis and three separately rulable items

Branch `codex/pec-loop-home-consolidation-20260905` starts at fetched
`origin/main` `7458e9c1eb9399ed259da464207d9a507acdea2e`.
The proposal has three independently reviewable decisions:

- **A — Migration.** Re-home the loop, its Task Management directory, and its
  evidence; update live locators and validation coverage. Every moved file is
  byte-identical in the migration commit. Preserve archived plans and all
  historical observations. Remove the old directory entirely: no stub and no
  parallel pointer surface. The relocation map and Git history are the record.
- **B — Generic instruction surface.** Replace the moved init's plan-first
  protocol with the PEC loop's generic instruction surface, following the
  app-dev D-APP-105/112 shape and incorporating D-APP-113's two corrections.
  Preserve fence wording; move the model convention to project AGENTS.
- **C — Run-based PR boundary.** Adopt the run/iteration and gate-class split
  below, replacing the receipt archive's per-iteration READY PR practice.

The app-dev precedents govern the method being adapted, not PEC authority:
`projects/chirality-app-dev/loop/LOOP_INIT.md` and the D-APP-105, D-APP-112,
and D-APP-113 records beside its decision register were read on the basis
above. PEC D-PEC-57/58 establish the product/frozen-corpus boundary;
D-PEC-78 retains the PEC-local registry home and typed schema. Its single
PEC locator changes only to follow the loop; no loop is added or removed.

## Owner directions and exact write scope

The task, pre-application report, and grant are preserved in
`D-PEC-80_LOOP_HOME_2026-09-05/OWNER_DIRECTIONS.md`.
The latest owner grant, verbatim:

> I grant the exact additional paths above, the locator-only source exception, and the proposed receipt/migration treatment.

This is execution permission to prepare the reviewable branch, not a ruling
accepting A, B, or C. Owner merge is the acceptance act. The candidate receipt
and register must remain awaiting owner until a real owner direction occurs.

Beyond `projects/pec/**` and deletion of `_DomainEngines/pec/**`, the grant is
exactly:

```text
init/dev-loop-init-prompt.md
_DomainEngines/profiles/pec.yaml
tools/validation/validate_instruction_entrypoints.py
tools/validation/test_validate_instruction_entrypoints.py
tools/validation/validate_pec_loop_receipts.py
tools/validation/test_validate_pec_loop_receipts.py
tools/practitioner_harness/cmd_bridge_status.py
tools/practitioner_harness/test_bridge_status.py
tools/practitioner_harness/BACKLOG.md
tools/taskmgmt/test_taskmgmt.py
projects/chirality-app-dev/frontend/scripts/run-pec-bridge-rehearsal.ts
```

The explicit locator-only exception covers that app-dev script plus PEC's
`v2/config/loops.json`, `v2/tests/config/fixtures/duplicate_loop_id.json`,
`v2/tests/config/fixtures/missing_loop_id.json`,
`v2/tests/config/test_json_loop_registry.py`, and
`v2/tests/config/test_loop_registry_contract.py`. It permits no feature,
schema, runtime behavior, loop membership, data, or lifecycle change.
No `agents/**` file changes, so no agent-index coordination notice is required.

## A — Relocation and reference disposition

The complete machine-readable maps are in
`D-PEC-80_LOOP_HOME_2026-09-05/RELOCATION_MAP.csv` and
`D-PEC-80_LOOP_HOME_2026-09-05/REFERENCE_INVENTORY.csv`.
The relocation map records all 337 files, byte lengths, and before/after
SHA-256 hashes. The inventory records each matching line, its source basis,
classification, and disposition, including preserved historical references.

| Old population | Canonical home | Treatment |
|---|---|---|
| Init, receipt ledger, three top-level workplans, currency note | `projects/pec/loop/` | Byte-identical move first; init rewritten and receipt appended only in B/C closeout |
| Two hidden archived workplans | `projects/pec/loop/.archive/` | Byte-identical and immutable |
| Entire `_TaskManagement/` directory, including register/archive and reports | `projects/pec/execution/_Coordination/_TaskManagement/` | Byte-identical; no row disposition or archive act |
| Every `PEC_*` evidence folder, same folder name | `projects/pec/execution/_Coordination/AgentRuns/` | Byte-identical, including evidence-local attributes and binary artifacts |

Initial literal search: 723 matching lines across 342 tracked files. Final
classification after independent review: tool/configuration/test 8 files /
10 lines; launcher/catalog 3 / 8; live documents/pointers 6 / 10; immutable
records/historical observations 325 / 695. The initial owner return listed
8 live and 323 historical files; the refinement preserves the two parser
SOWs' dated observations rather than rewriting their recorded evidence.
Constructed paths are additionally recorded in `CONSTRUCTED_PATHS.md`.

Historical references embedded in the Root TM-ROOT-118 concern, parser
CLM-017/CLM-015/CON-005, retired runbooks, and packet-local validation code
are preserved. The migration does not close any Task Management concern.
The independent inventory review found no newly broken parent-relative link;
a pre-existing malformed relative citation remains historical evidence.

The profile's output/write locator changes to PEC's project-local AgentRuns
home under this explicit grant. All other profile semantics remain unchanged;
D-T0-27's old exact hash remains historical lineage, not the new byte identity.
The obsolete, absent draft-profile fallback in bridge-status is removed.
Task Management production discovery already supports the canonical home;
its tests retain generic DomainEngine coverage and add PEC identity coverage.

## Receipt migration contract

The ledger's 426714-byte preimage through Receipt 166 is frozen at SHA-256
`153732e389a1dd948805dd71150f63d865ef3c70cb8b8f8230a36b836dda0dd7`.
The new wrapper accepts exactly that unchanged legacy-only state so A can be
validated independently. Any continuation requires the shared v2 marker and
`loop_receipt_contract.py` rules; no old receipt is normalized or rewritten.
The marker and one Receipt 167 are appended in final closeout. This prospective
format is part of A's owner-granted treatment, subject to merge acceptance.
It preserves the existing ledger's pointer-only, attribution, cap, and
non-authority rules while adding deterministic cursor and prefix validation.

## B — Consolidation and ordering

The standing plan is the source for the protocol and pointer index. The old
init and plan receive exhaustive clause dispositions in `CLAUSE_TRIAGE.csv`
and its readable table `CLAUSE_TRIAGE.md`: POINT (discoverable source), MECH
(command/check replaces prose), KEEP (necessary rule, compressed), OWNER
(verbatim owner/fence text), DROP (explanation or provenance without behavior).
Owner intent and target sequence remain in the immutable plan as overlay
content. On merge of B, the plan only narrows and orders; its protocol and
plan-precedence clauses are superseded by the init without editing the plan.

Order: header naming the full deliverable/Remaining work surface; bootstrap;
pointer index; verbatim fences; optional committed-HEAD overlay; Steps 0–5;
first return; posture; work-type checks; evidence contract; per-run steer and
historical path/section mapping. The model convention moves verbatim from the
old init to the project's Agent Posture, not to a root agent package.

D-APP-113 corrections are incorporated at authoring: state-column register
grep and exact prerequisite/SatisfactionStatus semantics. PEC's separate
active reliance-hold preflight remains independently blocking. No DepClosure
snapshot is invented when absent.

## C — Run-based PR boundary

- **Step 1:** Owner acts, rulings, routed notices, and reliance-hold releases
  are observable only on `origin/main` after `git fetch`. A predecessor item
  is observable once its commit, checks, and run record are on the run's
  branch. This distinction never overrides an explicit owner/acceptance gate.
- **Step 4:** One branch per run cut from `origin/main`; one commit and one
  receipt per ordinary iteration, pushed after each closeout. Independent
  nodes run concurrently under one recorded work graph with disjoint write
  loci; dependent nodes run in later iterations on the same branch. Open one
  PR at terminus or when the next step requires a merged act. Never self-merge;
  the owner merges or rejects by commit.
- **Step 5:** First receipt names the base commit; later receipts chain to
  the previous. Commit, push, return to Step 0 on the same branch. Rejected
  work returns to Step 0 on the next run.
- **Posture:** Persist until only human decisions remain, then present the
  slate. Do not manufacture extra work to prolong a run.

This amends the historical `READY PR IS OWNER MERGE GATE` per-iteration
practice. It changes the PR boundary, not source authority, owner-only acts,
acceptance gates, or independent verification. A predecessor commit proves
its recorded work, not a human act. The current migration is the expressly
approved exception: A is independently committed and checked before B/C,
while the entire run produces one receipt and one PR.

## Validation and dry-run evidence

Baseline command outputs and exit codes are in `BASELINE_CHECKS.json`;
`BASELINE_POINTERS.json` records pointer existence. The original standing
plan has no literal executable Step 0 block, no Task Management validator
command, and no receipt validator command. Those omissions are repaired with
explicit read-only commands; no invented command is called a verbatim plan
command. Historical source/demo checks are classified by work type, not run
against the frozen product for this control-plane migration.

Migration-only and final check ledgers, dry-run tables, final old-reference
scan, and commit identities are indexed in `VALIDATION.md` in the evidence
directory. Acceptance checks are execution evidence, not owner rulings.

## On-ruling mechanics, rollback, and handoff

The owner may accept, amend, or decline A, B, and C separately. The PR diff is
the candidate. A partial disposition is implemented as an amended candidate
on this same PR, retaining dependency truth (B uses A's paths; C's textual
changes are identified above). No unsupported partial combination is silently
merged. On explicit owner merge direction, add a one-line ruling record,
flip only the corresponding register disposition to RULED, and re-author the
new receipt's gate outcome on the same PR. Merge only on explicit owner
instruction; no past PEC self-merge permission applies.

Rollback is by reverting the scoped commits, with paths moved back according
to the relocation map. No product data rollback exists. Historical receipts,
plans, evidence, notices, and ruling bytes remain recoverable unchanged.

This package is derivative coordination evidence over the cited Git basis,
not decomposition truth or phase acceptance. A/B/C await the owner; no
product, lifecycle, release, or reliance gate is advanced. Checks must rerun
on any changed candidate, and a fresh origin comparison is required before
owner merge. Subsequent operators use the new init only as a candidate until
its merge is observable. Post-merge instruction defects take their own
residual ruling row, following D-APP-113.
