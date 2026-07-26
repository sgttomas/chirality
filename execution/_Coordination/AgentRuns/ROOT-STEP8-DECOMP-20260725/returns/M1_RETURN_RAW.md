# M1 Terminal Return — Step-9 materialization

Run: `ROOT-STEP8-DECOMP-20260725` · Node: M1 · Date: 2026-07-25
Executor: the N2 PROJECT_SETUP Agent 1 instance (continuation), `opus-5`. No delegation.
Brief: `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/briefs/MATERIALIZATION-BRIEF.md`
Branch: `claude/root-step9-materialization-20260725` @ `653fabc9b3e8abf369f5e776a7d3ee24bf235e7a` (no commit, no branch, no push).

**Verdict: COMPLETE, with three findings that need Agent 0 disposition (none blocking).**
6 packages / 45 deliverables materialized at state `OPEN`. Adapter baselines
repinned. G0's fence exercised its **second branch** for the first time and
PASSed on a registration it actually read. Full battery green: 233 + 311 tests,
all guards PASS, path anchors PASS.

The three findings, up front:

| # | Finding | Action taken |
|---|---|---|
| F-1 | The brief's `.gitkeep` premise is counterfactual — there are **zero** tracked `.gitkeep` files anywhere under `projects/*/execution/`. The real convention is a substantive `README.md` placeholder. | Matched the **real** convention (README.md), per the brief's operative instruction ("inspect … and match that convention exactly"), and report the wrong example rather than follow it. |
| F-2 | `.gitignore:22` `**/_Archive/` makes every `_Archive/` folder untracked repo-wide by deliberate policy ("Archives are historical/local, not canonical repo content"). The 18 `_Archive/` dirs SPEC §1.1 requires exist on disk but **will not survive a fresh clone**. | Created them as instructed; did **not** touch `.gitignore` (out of scope, and it would contradict a stated repo policy). Reported for disposition. |
| F-3 | `test_live_repo_state_is_clean` **PASSED** — but through G0's *second* branch, not the first. Its name and docstring ("nothing materializes at ruling time (packet §10)") now describe a world that no longer exists. | Did **not** modify the test. This is docstring/name drift, not a failure; Agent 0 dispositions. |

---

## 1. Tree summary

```
execution/
├── PKG-01_Product_Definition_Normative_Basis_and_Authority/     8 deliverables
├── PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/     5 deliverables
├── PKG-03_Governed_Execution_Structure_and_Root_Containment/    6 deliverables
├── PKG-04_Developmental_Machinery_and_Change_Control/          10 deliverables
├── PKG-05_Evidence_Provenance_and_Audit/                        8 deliverables
└── PKG-06_Self_Application_Variants_and_Release/                8 deliverables
                                                          total 45 deliverables
```

Per-package DEL counts **8 / 5 / 6 / 10 / 8 / 8** — matches the brief's expected
figures exactly.

Per-package subfolder set (identical for all six, SPEC §1.1):

```
execution/<PKG-ID>/
├── 0_References/          README.md          (tracked)
│   └── _Archive/          README.md          (git-ignored — see F-2)
├── 1_Working/             <45 DEL folders distributed here>
│   └── _Archive/          README.md          (git-ignored — see F-2)
├── 2_Checking/
│   ├── From/              README.md          (tracked)
│   └── To/                README.md          (tracked)
└── 3_Issued/              README.md          (tracked)
    └── _Archive/          README.md          (git-ignored — see F-2)
```

Per-deliverable file set — **exactly four files, no more, no less**, verified
programmatically across all 45 (`missing-required: 0 | with-extra-files: 0`):

```
1_Working/<DEL-ID>/
├── _STATUS.md         state OPEN
├── _CONTEXT.md
├── _DEPENDENCIES.md
└── _REFERENCES.md
```

**File tally.** 222 files written: 45 × 4 = 180 deliverable files + 6 × 7 = 42
package placeholders. Git sees 204 of them; the 18-file gap is exactly the
`_Archive/` placeholders (F-2).

**Identity check (byte-identical, verified programmatically).** The set of
`PKG-*` IDs in the decomposition §8 table, the set of `DEL-*` IDs in the §9
tables, the set of `DeliverableID` values in
`chirality_root_deliverable_register_v1_0.csv`, and the set of directory names
on disk are all **equal** — symmetric difference empty in both comparisons. No
renames, no additions, no omissions.

---

## 2. Templates instantiated

### 2.1 `_STATUS.md` (example: `DEL-02-05`, verbatim)

```markdown
# Status: DEL-02-05

**Current State:** OPEN
**Last Updated:** 2026-07-25
**Authorization Basis:** D-GOV-25 (root decomposition acceptance, 2026-07-25); owner step-9 direction 2026-07-25 ("Merge PR #348 then proceed with Step 9"); D-GOV-21 §6 step 9
**Accepted Basis SHA:** 653fabc9b3e8abf369f5e776a7d3ee24bf235e7a

## Remaining

## History
- 2026-07-25 - State set to OPEN (PROJECT_SETUP, step-9 materialization, D-GOV-25)
```

**Parser conformance was verified, not assumed.** I ran all 45 files through
`tools/practitioner_harness/prose_bullet_v1.py` directly:

```
status files parsed: 45
non-conforming: 0
sample: PARSED OPEN 2026-07-25 | history entry: OPEN strict PROJECT_SETUP, step-9 materialization, D-GOV-25 PARSED
```

Every file yields `doc_caveat_class = PARSED` (not `PARSED_WITH_ASSUMPTIONS`),
`current_state = OPEN`, and a history bullet matching `RULE_1_STRICT` — the
strict TS-parser-equivalent rule, rule 1, the only rule that yields `PARSED`.
Zero trailing `UNPARSEABLE` bullets. The parenthetical actor string contains no
`)`, so the rule's `([^)]*)` group closes correctly.

### 2.2 `_CONTEXT.md` (example: `DEL-02-05`, verbatim)

```markdown
# Context: DEL-02-05

**Name:** Live Registry Discipline for Skills and Tools
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Discipline:** TBD
**Type:** REGISTER
**Responsible:** TBD

## Description

Keep method packs and deterministic operations maintained as live registries that govern their own membership, with the live registry authoritative over any narrative list and discrepancies surfaced.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Registry drift check
- narrative-vs-registry discrepancy report

## Scope Traceability

- Scope items: SOW-013, SOW-030
- Objectives: OBJ-001
- ContextEnvelope: S
- ContextEnvelopeNotes: Two registries and a comparison rule.
- AnticipatedWriteLocus: instruction-surface (M2); execution-tree for drift reports

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-02-05_Live_Registry_Discipline_for_Skills_and_Tools
- **Package ID:** PKG-02_Operative_Instruction_Surface_and_Runtime_Layers

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
```

Field shape is `docs/SPEC.md` §4.1 verbatim (`Name` / `Package` / `Discipline` /
`Type` / `Responsible`, then Description, Acceptance Criteria, Anticipated
Artifacts, Scope Traceability, Decomposition Reference), which is also
`agents/AGENT_PREPARATION.md`'s schema plus §4.1's two extra sections. Values are
transcribed from the CSV register (`Name`, `Type`, `Description`,
`AnticipatedArtifacts`, `CoversScopeItems`, `SupportsObjectives`,
`ContextEnvelope`, `ContextEnvelopeNotes`, `AnticipatedWriteLocus`,
`ResponsibleParty`) and the §8 package-name column.

**Two fields are `TBD` because the decomposition genuinely does not state them**
(SPEC §4.1 asks for them; the accepted decomposition carries neither):

- `Discipline` — no discipline column exists anywhere in the decomposition or
  its companion registers.
- `Acceptance Criteria` — no per-deliverable acceptance criteria are stated.

Both are marked `TBD` with the reason recorded inline. Neither was invented
(K-INVENT-1), per the brief's "mark anything the decomposition leaves TBD as TBD
— never invent". `ResponsibleParty: TBD` is carried through from the register per
OI-011.

### 2.3 `_DEPENDENCIES.md` (schema-in-place, declared-empty)

Shape follows `AGENT_PREPARATION.md`'s hybrid-container schema and SPEC §5's
ownership zones. It opens with the K-DEP-1 statement, declares
`Mode: DECLARED`, and records **no edges** in either direction:

```markdown
## Upstream (I need these before I can proceed) — human-owned declarations

- None declared. The accepted decomposition declares no inter-package or
  inter-deliverable ordering, and none is inferred here (K-INVENT-1).
```

The Coordination note points at `execution/_harness/work_graph.yaml` and cites
the two places the accepted decomposition says there is no ordering (§8's "No
nesting, no phases, no overlap, no gaps"; §14's Downstream Execution Notes). The
agent-owned sections (`Extracted Dependency Register` = `NOT_RUN_YET`, Run
Notes, Lifecycle Summary, Consumer Handoff Notes) are present as placeholders
for `TASK + dependency-extract`. No `Dependencies.csv` was created —
dependency-tracked status is a later, separate act (SPEC §12.3).

### 2.4 `_REFERENCES.md` (skeleton, decomposition-pointed)

Points at the accepted decomposition **by path and by working-surface section**
(`§9 — <PKG-ID>`), plus the three companion registers (deliverable, scope
ledger, objective register). Source hashes are deliberately **not** pinned —
recorded inline as belonging to the deliverable's own initialization, not to
scaffolding. Shape follows `AGENT_PREPARATION.md`'s `_REFERENCES.md` schema
(Applicable References / Notes) with a `Decomposition Entry` block matching the
app-dev precedent.

### 2.5 Package placeholder `README.md` (example, verbatim)

```markdown
# PKG-02 Issued

Reserved for released deliverables of this package. Nothing is issued at materialization; every deliverable is at lifecycle state `OPEN`.
```

Seven per package, one per otherwise-empty folder. See F-1 below for why
`README.md` and not `.gitkeep`.

---

## 3. Finding F-1 — the `.gitkeep` premise is counterfactual

The brief says: "Inspect how the existing project working roots keep empty
folders tracked (e.g. `.gitkeep` under `projects/chirality-app-dev/execution/`)
and match that convention exactly."

Inspection contradicts the example:

```
tracked .gitkeep under projects/*/execution/: 0
tracked README.md placeholders under projects/chirality-app-dev/execution/PKG-*/: 7
```

Repo-wide there are 21 tracked `.gitkeep` files, but **every one** of them is
under `_DomainEngines/proposals/` or `domains/*/` — none under any project
working root's `execution/`. The actual convention in the working roots is a
short, substantive `README.md`, exemplified by
`projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/`:

```
# PKG-00 Checking

Reserved for review artifacts produced by DAG closure or project-level reconciliation.
```

I followed the brief's **operative instruction** (inspect, then match the
convention found) over its **incorrect example**, and matched PKG-00's shape:
`# <PKG-short-ID> <Folder purpose>` + one "Reserved for …" line.

Worth recording alongside this: PKG-00 is the *only* package in any working root
that has the full subfolder set at all. The other 11 app-dev packages and all 18
piping packages contain **only** `1_Working/`. So the "full SPEC §1.1 subfolder
set" this brief required is stricter than live practice anywhere else in the
repo. That is consistent with SPEC §12.2 (`1_Working/` MUST; the other three
SHOULD), and I built the full set as instructed — but the root is now the most
structurally complete working root in the repo, which is a deliberate outcome
worth knowing rather than a silent one.

---

## 4. Finding F-2 — `_Archive/` folders cannot be tracked

```
$ git check-ignore -v execution/PKG-01_.../0_References/_Archive/README.md
.gitignore:22   **/_Archive/    execution/PKG-01_.../0_References/_Archive/README.md
```

`.gitignore` lines 12–22, under the comment **"Archives are historical/local,
not canonical repo content"**, ignore `Archive/`, `.Archive/`, `**/Archive/`,
`**/.Archive/`, and `**/_Archive/`.

Consequence: the 18 `_Archive/` directories SPEC §1.1 lists as required
subfolders (3 per package × 6) exist on disk and satisfy the brief locally, but
git tracks neither them nor their placeholders. **On a fresh clone they will not
exist.** This is why no working root in the repo has a tracked `_Archive/`
anywhere — it is policy, not oversight.

I did **not** add a `!` negation to `.gitignore`. That file is configuration
outside this brief's write scope, and the change would contradict a stated repo
policy. The tension between "SPEC §1.1 requires `_Archive/` subfolders" and
"`.gitignore` policy says archives are not canonical repo content" is a real
governance question, not mine to settle. Dispositions available to Agent 0:
accept local-only `_Archive/` (status quo, costs nothing), narrow the ignore
rule for `execution/PKG-*`, or amend SPEC §1.1 to stop listing `_Archive/` as
required. I recommend none — it is an owner/Agent 0 call.

The 18 ignored `README.md` placeholders were left in place: removing them would
leave the local tree less conformant with the SPEC §1.1 set the brief demanded,
and they cost nothing.

---

## 5. Finding F-3 — `test_live_repo_state_is_clean` passes on a stale premise

The brief anticipated this test failing. **It did not fail.** Source:

```python
def test_live_repo_state_is_clean():
    """The fence must PASS on the actual checkout at the D-GOV-21 EffectiveSHA:
    nothing materializes at ruling time (packet §10)."""
    code, _ = g0.check(g0.repo_root())
    assert code == 0
```

The assertion is `code == 0`, and G0 still returns 0 — but by a different route.
Before step 9 it returned 0 from the *first* branch (no children → fence idle).
Now it returns 0 from the *second* branch (children exist → registration read →
all four guards registered and passing). The assertion is premise-independent;
the docstring is not. "Nothing materializes at ruling time" is now a description
of a superseded world, and the test **name** — `..._state_is_clean` — reads as
asserting the absence of materialized structure, which it no longer does.

Per the brief I did not modify the test. Flagging it as name/docstring drift
that a governed update in this tranche should probably correct (the assertion
itself is still correct and still valuable — arguably *more* valuable now, since
it exercises the load-bearing path).

---

## 6. Verification transcript (verbatim, every exit code)

### V1 — G0, the fence's first load-bearing run

```
$ python3 tools/validation/validate_root_materialization_fence.py
G0: materialized root packages/deliverables found: PKG-01_Product_Definition_Normative_Basis_and_Authority, PKG-02_Operative_Instruction_Surface_and_Runtime_Layers, PKG-03_Governed_Execution_Structure_and_Root_Containment, PKG-04_Developmental_Machinery_and_Change_Control, PKG-05_Evidence_Provenance_and_Audit, PKG-06_Self_Application_Variants_and_Release
G0 PASS: G1-G4 registered and passing per execution/_harness/root_guards.yaml; materialization gate satisfied.
exit=0
```

**Second-branch evidence.** The output alone is strong (the string "G1-G4
registered and passing per execution/_harness/root_guards.yaml" is emitted only
after `load_registration()` returns a mapping and all four entries validate),
but I confirmed it directly by read-only introspection of the module — no
mutation of any state file, no negative-control tampering:

```
$ python3 -c "<import g0 by path; call its functions>"
materialized_children() -> 6 entries (non-empty => first branch skipped)
load_registration() -> parsed mapping with keys ['G1', 'G2', 'G3', 'G4']
REQUIRED_GUARDS: ('G1', 'G2', 'G3', 'G4')
  G1: registered=True status='passing'
  G2: registered=True status='passing'
  G3: registered=True status='passing'
  G4: registered=True status='passing'
check() exit: 0
exit=0
```

Reading `check()`'s source confirms the control flow: `if not children:` returns
the idle PASS at line 94; with `children` non-empty that branch is skipped, the
"materialized … found" line is appended, `load_registration(root)` is called,
and each of `REQUIRED_GUARDS` is checked for `registered is True` and
`status == "passing"`. **The registration surface written at step 8 was actually
read and actually satisfied.** The N2 return recorded `root_guards.yaml` as
"written but not yet exercised"; that item is now closed.

### V2 — G1–G4

```
$ python3 tools/validation/validate_root_harness_adapter.py
G1 PASS: root harness adapter execution/_harness/adapter.yaml is schema-valid (root-harness-adapter/v1); declared pointers exist and pinned baselines match the observed tree (status_files=45, pinned_at=653fabc9b3e8abf369f5e776a7d3ee24bf235e7a).
G1: materialized root packages/deliverables observed: PKG-01_Product_Definition_Normative_Basis_and_Authority, PKG-02_Operative_Instruction_Surface_and_Runtime_Layers, PKG-03_Governed_Execution_Structure_and_Root_Containment, PKG-04_Developmental_Machinery_and_Change_Control, PKG-05_Evidence_Provenance_and_Audit, PKG-06_Self_Application_Variants_and_Release
exit=0

$ python3 tools/validation/validate_root_surface_ownership.py
G2 PASS: surface-ownership register execution/_harness/surface_ownership.yaml is schema-valid (root-surface-ownership/v1); 6 entr(ies) declare write targets; 6 materialized PKG-*/DEL-* child(ren) all registered; decomposition='execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md'.
exit=0

$ python3 tools/validation/validate_root_work_graph_dispatch.py
G3 PASS (CI mode): work graph work_graph.yaml is schema-valid (root-work-graph/v1); 6 node(s), active: none; declared write targets, disjointness/serialization, and M2 markers check out.
exit=0

$ python3 tools/validation/validate_instruction_tranche_manifest.py
G4 PASS (CI mode): 3 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['ROOT-LANE-B-20260725', 'ROOT-STEP8-ACCEPT-20260725', 'ROOT-STEP9-MAT-20260725'].
exit=0
```

G1 recounted the glob independently and matched the declared 45. G2 now reports
"6 materialized PKG-*/DEL-* child(ren) all registered" — the unregistered-package
check fired for the first time and cleared.

**G2 DEL-level question, confirmed against the validator rather than assumed.**
`materialized_children()` enumerates only *direct* children of `execution/`
matching `PKG-*`/`DEL-*`; the 45 deliverables live at
`execution/<PKG>/1_Working/<DEL>` and are never enumerated. The
unregistered-package check therefore ranges over 6 names, all registered. The
brief's instruction to report-rather-than-modify if I found otherwise did not
trigger: **the register needs no DEL-level entries and I added none.**

### V3 — test suites

```
$ python3 -m pytest tools/validation -q
........................................................................ [ 30%]
........................................................................ [ 61%]
........................................................................ [ 92%]
.................                                                        [100%]
233 passed in 1.64s
exit=0

$ python3 -m pytest tools/validation/test_validate_root_materialization_fence.py -q -k live
.                                                                        [100%]
1 passed, 8 deselected in 0.02s

$ python3 -m pytest tools/practitioner_harness -q
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 69%]
........................................................................ [ 92%]
.......................                                                  [100%]
311 passed in 37.00s
exit=0
```

`test_live_repo_state_is_clean` passed — see F-3. No test was modified. The
practitioner-harness live-baseline suite (which pins app-dev 0/53 and piping
0/101 drift) is unaffected: `cmd_drift` is invoked over the two pilot project
roots only, and the root working root is not among them.

### V4 — path anchors

```
$ python3 tools/validation/validate_path_anchors.py
PASS: no literal home-dir absolute paths found in 996 live path-anchor surfaces
exit=0
```

Note the surface count is **unchanged at 996** — identical to the pre-step-9 run
in the N2 return. The 222 new files were not added to the scanned set, because
`validate_path_anchors.py` is deliberately narrow ("checks instruction and
executable handoff surfaces … ignores historical evidence, generated outputs,
archives, and plans"). So this PASS is not evidence about the new files. I
therefore ran a direct scan over everything I wrote:

```
$ grep -rlE "(^|[^A-Za-z0-9_{])(/Users/|/home/|[A-Za-z]:\\Users\\)" execution/PKG-*
(no output — no machine-absolute paths)
```

### V5 — count checks

```
$ ls -d execution/PKG-*/ | wc -l
6

$ python3 -c "from pathlib import Path; print(len(list(Path('.').glob('execution/PKG-*/1_Working/DEL-*/_STATUS.md'))))"
45

$ per-package DEL counts
PKG-01_Product_Definition_Normative_Basis_and_Authority      8
PKG-02_Operative_Instruction_Surface_and_Runtime_Layers      5
PKG-03_Governed_Execution_Structure_and_Root_Containment     6
PKG-04_Developmental_Machinery_and_Change_Control            10
PKG-05_Evidence_Provenance_and_Audit                         8
PKG-06_Self_Application_Variants_and_Release                 8

$ four required files present in every DEL
deliverable dirs: 45 | missing-required: 0 | with-extra-files: 0

$ ID equality (working surface §9 vs CSV register vs on-disk)
working-surface §9 IDs: 45 | CSV IDs: 45 | on-disk dirs: 45
WS == CSV: True
CSV == DISK: True
pkg WS==DISK: True
```

Expected 8/5/6/10/8/8 — matched. Expected 45 `_STATUS.md` matching the adapter
glob — matched, and the glob used is the adapter's own `status_glob`.

### V6 — `git status --porcelain`

```
$ git status --porcelain
 M docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md
 M execution/_harness/adapter.yaml
?? docs/governance_harness/tranche_manifests/ROOT-STEP9-MAT-20260725.yaml
?? execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/
?? execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/
?? execution/PKG-03_Governed_Execution_Structure_and_Root_Containment/
?? execution/PKG-04_Developmental_Machinery_and_Change_Control/
?? execution/PKG-05_Evidence_Provenance_and_Audit/
?? execution/PKG-06_Self_Application_Variants_and_Release/
?? execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/briefs/MATERIALIZATION-BRIEF.md
```

Mine: the six `execution/PKG-*` trees (204 git-visible files) and the
`execution/_harness/adapter.yaml` modification. Everything else is Agent 0's
concurrent work as the directive said to expect — the D-GOV-25 EffectiveSHA
backfill, the `ROOT-STEP9-MAT-20260725` tranche manifest, and this brief.
Filtering my scope out of the listing leaves exactly those three Agent-0 paths
and nothing unaccounted for.

### Adapter diff (the only modification I made to an existing file)

```diff
 baselines:
-  # Pre-materialization: no PKG-*/DEL-* structure exists under root execution/,
-  # so the observed status_glob count is 0. Verified against the checkout.
-  status_files: 0
+  # Repinned at D-GOV-21 §6 step-9 materialization (2026-07-25): 6 packages and
+  # 45 deliverables materialized from the accepted decomposition (D-GOV-25), all
+  # at lifecycle state OPEN. Count verified against the checkout via status_glob.
+  status_files: 45
   status_mismatch: 0
-  pinned_at: ea0ad7a566ddb51d89297bfcf491636f1fc5dd15
+  pinned_at: 653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
```

Baselines only, as instructed. `schema`, `product`, `working_root`,
`execution_root`, `prd`, `coordination`, `decision_register`, `status_glob`,
`states`, `parser_dialect`, `exclude_globs`, and `status_mismatch` are all
untouched.

---

## 7. Constraint confirmations

| Constraint (brief) | Status |
|---|---|
| Write scope = new `execution/PKG-*` trees + adapter baselines + this return | **Held.** V6 accounts for every path. |
| No instruction-surface writes | **Held.** Nothing under `AGENTS.md`, `agents/`, `skills/`, `tools/`, `docs/`, `init/`, `.github/workflows/`. |
| No `_Decomposition/` edits | **Held.** Read-only (working surface + 2 companion CSVs read). |
| No work-graph changes; nodes stay `pending` | **Held.** `work_graph.yaml` untouched; G3 still reports "active: none". Materialization dispatched no work. |
| No `surface_ownership.yaml` changes | **Held.** Confirmed unnecessary against the validator (§V2), not assumed. |
| No commits, no branches, no push | **Held.** Working tree left dirty. |
| IDs/labels byte-identical to the decomposition | **Held**, verified by set equality across three independent sources (§1). |
| Machine-absolute paths prohibited | **Held**, verified by direct grep over all 222 written files (§V4), not only by the narrow anchor validator. |
| State OPEN only; no SOW_V1, no INITIALIZED claims | **Held.** Four files per deliverable, zero extras — no `ScopeOfWork.md`, no legacy four-doc kit, no `Dependencies.csv`, no `_SEMANTIC.md`. Every `_STATUS.md` reads `OPEN` and its sole history line records the OPEN transition. |
| Fix state, never tests/validators | **Held.** Nothing under `tools/` was modified; F-3 reported rather than edited. |

---

## 8. Open items

1. **F-2 `_Archive/` tracking** (§4) — needs an owner/Agent 0 disposition:
   accept local-only, narrow the ignore rule, or amend SPEC §1.1. Nothing is
   blocked meanwhile.
2. **F-3 stale test name/docstring** (§5) — `test_live_repo_state_is_clean`
   passes but describes a superseded world. A governed update belongs in this
   tranche; it is Agent 0's to stage.
3. **F-1 recorded for the brief-writing loop** (§3) — the `.gitkeep` example was
   wrong; the convention is `README.md`. Worth correcting wherever that
   assumption came from, so it does not propagate to the next materialization.
4. **SPEC §2.1 vs §12.3 minimum-fileset tension.** §2.1 names a five-file
   "minimum viable fileset (PREPARATION)" **including `_SEMANTIC.md`
   (placeholder)**; §12.3's "Valid Deliverable Folder" requires only the four
   this brief specified. `AGENT_PREPARATION.md` also lists five. I followed the
   brief (four files) and did **not** create `_SEMANTIC.md`. If a later
   PREPARATION-style check enforces §2.1, all 45 deliverables will read as
   missing one placeholder. Cheap to fix later; recorded now so it is not a
   surprise. Note also that `tools/validation/check_min_viable_fileset.sh` is a
   shell script and is **not** part of either pytest battery, so nothing in the
   verification I ran probes this.
5. **Practitioner-harness adoption still gated** (carried forward from the N2
   return, now more consequential). The root adapter declares real baselines
   (45 files) but `harness.py`'s alias table still does not contain the root, so
   `harness.py drift` cannot be run against it. The root is the only working root
   with a schema-valid adapter that the harness cannot read. Needs its own
   M2-gated tranche.
6. **Deliverable initialization is per-deliverable gated work.** All 45 sit at
   `OPEN` with `ResponsibleParty: TBD`. `OPEN → INITIALIZED` requires
   `TASK + scope-of-work` producing a valid `SOW_V1` (SPEC §3.3), and assignment
   requires a human. Nothing in this run authorizes either.
7. **`Discipline` and `Acceptance Criteria` are `TBD` for all 45** (§2.2) because
   the accepted decomposition carries neither field. If SPEC §4.1 conformance is
   later audited strictly, these surface as 90 `TBD`s with a single common cause
   — a decomposition-format gap, not 45 independent scaffolding defects.
