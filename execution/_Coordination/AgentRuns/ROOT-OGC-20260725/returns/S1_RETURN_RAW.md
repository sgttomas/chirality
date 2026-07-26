# S1 Terminal Return — SPEC notes + guarded-set enumeration (ROOT-OGC-20260725)

Executor: ephemeral bounded Agent 2 generalist (`opus-5`), sealed brief
`execution/_Coordination/AgentRuns/ROOT-OGC-20260725/briefs/SPEC-GUARDED-SET-BRIEF.md`.
Branch `claude/root-owner-gated-closeout-20260725` (worktree). No commits.
Status: **COMPLETE with two REPORTED findings requiring Agent 0 disposition.**

---

## 0. Headline findings (read first)

**F-1 — Section-number discrepancy in the ruling, the brief, and the guards.**
The instruction-surface *enumeration* does not live in `docs/SPEC.md` §0.2.2.
It lives in **§0.2.1** (`REPO_ROOT` — the active checkout), at the sentence
`docs/SPEC.md:44`. §0.2.2 (`WORKING_ROOT`) contains no enumeration — it carries
a narrower *write-prohibition* list at `:52` (`agents/`, `skills/`, `tools/`,
root `docs/`), which already omits `AGENTS.md` and `init/` by design. The
"§0.2.2" label is carried by D-GOV-26 item 2, this brief, and all three guard
docstrings/comments; `docs/PRD_ROOT.md` O-1 and the PRD concordance annex cite
§0.2.1 **correctly**. I executed the substance (extended the enumeration at
`:44`, §0.2.1) and corrected the citation inside my write scope (the three
validators). I did **not** touch D-GOV-26 or the brief. Agent 0 should decide
whether the ruling record's "§0.2.2" needs an errata note.

**F-2 — Four ratified/adopted verbatim restatements now diverge.** The
enumeration is restated word-for-word in four live governance surfaces outside
`docs/SPEC.md`. All four are now **incomplete relative to the amended SPEC**
(they omit `CLAUDE.md` and `.github/workflows/`). Per brief §4 these are
REPORTED, not fixed. Detail in §3 below. Notably `docs/PRD_ROOT.md` O-1 is a
verbatim restatement, so the brief's stated risk condition ("a verbatim
restatement would be [contradicted]") **has materialized**.

---

## 1. Edits made — exact sentences, before/after

### Edit 1 — `docs/SPEC.md` §0.2.1 line 44 (R2: enumeration extension)

BEFORE
```
`REPO_ROOT` is the home of the **shared instruction surface** (`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`) — the release-managed agent operating system (the **instruction root**; see `DIRECTIVE.md` §2.6). The instruction surface is read-mostly: changing it is a repo-wide governance action, not ordinary working-root execution.
```

AFTER
```
`REPO_ROOT` is the home of the **shared instruction surface** (`AGENTS.md`, `CLAUDE.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) — the release-managed agent operating system (the **instruction root**; see `DIRECTIVE.md` §2.6). `CLAUDE.md` is the session-initialization instruction pointer: it imports `AGENTS.md` and adds no instruction layer of its own, so editing it changes what every session loads. `.github/workflows/` holds the CI workflow definitions that gate merges, so editing them changes how governance is enforced rather than what it says. The instruction surface is read-mostly: changing it is a repo-wide governance action, not ordinary working-root execution.
```

Two members added to the list; two new sentences state the WHY per brief §2.
The read-mostly sentence is byte-identical. No normative requirement changed.

**Placement note (F-1):** the brief said "§0.2.2". I edited §0.2.1 because that
is where the sentence actually is — the brief's own instruction ("Read the
section first and place them so *the sentence* stays precise about WHY",
singular) identifies this sentence uniquely, and the string quoted in the guard
comments as "§0.2.2's enumeration" is a literal match for `:44`. Editing
§0.2.2's `:52` prohibition list instead would have expanded a MUST NOT, which
the brief forbids.

### Edit 2 — `docs/SPEC.md` §1.1, after the required-subfolders table (R1)

BEFORE — the table ended at `| `3_Issued/_Archive/` | Archived issued versions |`
and was followed directly by `### 1.2 Tool Roots`.

AFTER — one sentence inserted between them:
```
The `_Archive/` subfolders above are **local working state, not tracked repo content**: the repository ignore policy excludes every `_Archive/` path ("Archives are historical/local, not canonical repo content"), so these folders exist in a working checkout but are not under version control, and nothing canonical may live only in an `_Archive/`.
```

The parenthetical quotes the live `.gitignore:12` comment verbatim; the ignore
rule itself is `.gitignore:22` (`**/_Archive/`). No table row changed, no
required subfolder removed, no normative requirement altered — the sentence
only records the tracking status the ignore policy already imposes.

## 2. Validator and test changes

### 2.1 Guarded set (all three definitions found and changed)

`grep -rn "INSTRUCTION_SURFACE_FILES" --include="*.py" .` returned exactly three
definition sites, all now identical:

| Guard | File | Change |
|---|---|---|
| G2 | `tools/validation/validate_root_surface_ownership.py:100` | `("AGENTS.md",)` → `("AGENTS.md", "CLAUDE.md")` |
| G3 | `tools/validation/validate_root_work_graph_dispatch.py:108` | same |
| G4 | `tools/validation/validate_instruction_tranche_manifest.py:124` | same |

`INSTRUCTION_SURFACE_DIRS` was **not** changed — `.github/workflows/` was
already present in all three (that was the pre-existing guard behavior D-GOV-26
item 2 ratifies into doctrine). Post-change, all three sets are byte-identical:
files `("AGENTS.md", "CLAUDE.md")`, dirs `("agents/", "skills/", "tools/",
"docs/", "init/", ".github/workflows/")` — matching the amended SPEC §0.2.1
enumeration exactly.

### 2.2 Comments/docstrings that enumerate the set

All three enumerating comments were rewritten to (a) include `CLAUDE.md`,
(b) name D-GOV-26 as the basis, (c) preserve the Lane B workplan citation as
the prior basis for `.github/workflows/`, and (d) correct the section citation
from §0.2.2 to §0.2.1 (F-1). G2's stale line `` `CLAUDE.md` is a recorded open
item, not silently included`` was removed — that open item is now closed.

### 2.3 Regression tests added (7 new tests, mirroring the Lane B pattern)

| Suite | Tests added |
|---|---|
| `test_validate_root_surface_ownership.py` | `test_claude_md_is_instruction_surface`; `test_block_on_unmarked_claude_md_write_target` (register entry with `CLAUDE.md` write target and `instruction_surface: false` → BLOCK); `test_pass_on_marked_claude_md_write_target` (same marked `true` → PASS) |
| `test_validate_root_work_graph_dispatch.py` | `test_claude_md_is_instruction_surface`; `test_block_on_claude_md_target_without_marker` (node write target `CLAUDE.md`, no `M2:` marker → BLOCK); `test_pass_on_claude_md_target_with_valid_m2_marker` (→ PASS) |
| `test_validate_instruction_tranche_manifest.py` | `test_claude_md_is_instruction_surface`; `test_diff_mode_blocks_uncovered_claude_md_change` (committed `CLAUDE.md` change not covered by a manifest path → BLOCK); `test_diff_mode_pass_when_claude_md_change_is_covered` (manifest declares `CLAUDE.md` → PASS) |

Each unit-level test pins both the positive (`CLAUDE.md`, `./CLAUDE.md`) and the
negative (`projects/demo/CLAUDE.md` — a *project* pointer file is not root
instruction surface, since matching is exact against the FILES tuple, not
suffix-based).

## 3. Concordance survey — every enumeration restatement found

Method: `grep -rn "0\.2\.2"` and `grep -rn "instruction surface"` across
`*.md`/`*.py` repo-wide, then inspection of every hit carrying a member list.

### 3.1 Live ratified/adopted surfaces — DIVERGENCE (report only, not fixed)

| # | Site | Form | Verdict |
|---|---|---|---|
| R-1 | `docs/DIRECTIVE.md:13` (§1 genus paragraph) | Verbatim: "(`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`)" | **DIVERGES** — now incomplete. Ratified 2026-07-11; amended by D-GOV-23/D-GOV-24. |
| R-2 | `docs/DIRECTIVE.md:201` (§2.6 Instruction root bullet) | Verbatim: "— `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and `init/`." | **DIVERGES** — now incomplete. Also carries the desktop-bundle packaging list (`agents/`, `skills/`, `tools/`, `docs/`, `init/` → `instruction-root/`), which raises a real question: is `.github/workflows/` packaged into a desktop `instruction-root/`? Almost certainly not — CI wiring is monorepo-only. Amending R-2 naively would assert something false about desktop builds. |
| R-3 | `docs/TYPES.md:50` ("Instruction Root" row) | Verbatim: "— `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`." | **DIVERGES** — now incomplete. |
| R-4 | `docs/PRD_ROOT.md:442` (**O-1**) | Verbatim: "The shared instruction surface is `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and `init/`." Provenance cites `docs/SPEC.md` §0.2.1 (correctly). | **DIVERGES** — this is the case the brief flagged. O-1 is a TRANSCRIBED obligation in the *adopted* PRD; its transcription source (SPEC §0.2.1) has changed under it, so O-1 is now an incomplete transcription. |

### 3.2 Live surfaces citing by reference — NO divergence

| Site | Form | Verdict |
|---|---|---|
| `docs/PRD_ROOT.md:242` (§ human capacities, Product maintenance) | Cites "`docs/SPEC.md` §0.2.1–§0.2.2" — reference only, no member list | **UNAFFECTED** (incorporation by reference) |
| `docs/PRD_ROOT.md:450` (**O-9**) | Cites "`docs/SPEC.md` §0.2.2, §1" — reference only | **UNAFFECTED**; note the §0.2.2 pointer here targets the `:52` prohibition, which I did not touch |
| `docs/TYPES.md:49` (Repo Root row) | "Home of the shared instruction surface" — no list | **UNAFFECTED** |
| `docs/DIRECTIVE.md:7` (Authority chain) | "`AGENTS.md` and `agents/` are the live instruction surface" — deliberately partial, about the *live agent* surface | **UNAFFECTED** (not an enumeration of the instruction root) |
| `docs/DIRECTIVE.md:3` (provenance note) | "(`AGENTS.md`, `agents/`)" — partial, historical | **UNAFFECTED** |
| `docs/WORKFLOW_COMPONENT_STANDARD.md:33` | "applies to the shared instruction surface and to working-root…" — no list | **UNAFFECTED** |
| **root `AGENTS.md`** | **carries no enumeration at all** — grep for the member list and for "instruction surface" returned zero hits in `AGENTS.md` | **UNAFFECTED** (brief §4's `AGENTS.md` check: negative, nothing to diverge) |
| `docs/SPEC.md:52` (§0.2.2), `docs/SPEC.md:78` (§0.3 `{INSTRUCTION_ROOT}` row), `docs/SPEC.md:65` (§0.2.4) | Partial lists serving other purposes (write prohibition; token anchor; path-reference discipline). §0.2.4 already omitted `init/` before this tranche, so it was never a verbatim restatement. | **UNAFFECTED — deliberately not edited** (minimal diff; editing `:52` would expand a MUST NOT) |

### 3.3 Immutable records / candidates / derivative packages — informational only

Not live doctrine; listed for completeness, no action implied.

- `docs/governance_harness/_PROPOSALS/D-GOV-22_root_prd_adoption/PACKET.md:201` — verbatim enumeration inside the adoption packet's coverage table (immutable record of what was adopted).
- `docs/governance_harness/_PROPOSALS/D-GOV-23_directive_genus_supersession/PACKET.md:127` — quotes the DIRECTIVE §1 sentence (immutable).
- `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md:186` — M2's own partial list (`AGENTS.md`, `agents/`, …); `:96` and `:504` reference SPEC `:48-52` for the S6 supersession (immutable).
- `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md:434` and `..._concordance_annex.md:121,124,178` — candidate/derivative copies of the PRD material; the annex at `:178` cites "§0.2.1 (line 44), §0.2.2 (line 52)" and is the one surface that already distinguished the two sections correctly.
- Prior AgentRun returns (`ROOT-LANE-B-20260725/returns/N1_RETURN*.md`) recommended exactly this change; historical evidence.

### 3.4 Corroborating (not divergent) evidence for `CLAUDE.md` membership

- `tools/validation/validate_instruction_entrypoints.py` (registered in
  `tools/REGISTRY.md:54`) **already** validates that tracked `CLAUDE.md` is
  exactly the one-line `@AGENTS.md` import contract. It runs PASS. So a
  deterministic root validator already treated `CLAUDE.md` as governed
  entrypoint state before this tranche; D-GOV-26 item 2 aligns the guarded set
  with that pre-existing posture rather than inventing a new claim.
- `.github/workflows/harness-premerge.yml` copies `CLAUDE.md` alongside
  `AGENTS.md` into its staging step (`:97`) — i.e. CI already ships it as
  instruction content.

## 4. Verification transcript (verbatim, every exit code)

```
$ python3 -m pytest tools/validation -q
242 passed in 2.75s
exit=0
```
(235 before this tranche + 7 new; zero failures, zero pre-existing tests changed.)

Five registered root guards (names resolved from
`execution/_harness/root_guards.yaml` — note G0's validator is
`validate_root_materialization_fence.py`, not `validate_root_guard_registration.py`):

```
$ python3 tools/validation/validate_root_materialization_fence.py      # G0
G0: materialized root packages/deliverables found: PKG-01_…, …, PKG-06_…
G0 PASS: G1-G4 registered and passing per execution/_harness/root_guards.yaml; materialization gate satisfied.
exit=0

$ python3 tools/validation/validate_root_harness_adapter.py            # G1
G1 PASS: root harness adapter execution/_harness/adapter.yaml is schema-valid (root-harness-adapter/v1); declared pointers exist and pinned baselines match the observed tree (status_files=45, pinned_at=653fabc9b3e8abf369f5e776a7d3ee24bf235e7a).
exit=0

$ python3 tools/validation/validate_root_surface_ownership.py          # G2
G2 PASS: surface-ownership register execution/_harness/surface_ownership.yaml is schema-valid (root-surface-ownership/v1); 6 entr(ies) declare write targets; 6 materialized PKG-*/DEL-* child(ren) all registered; decomposition='execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md'.
exit=0

$ python3 tools/validation/validate_root_work_graph_dispatch.py        # G3
G3 PASS (CI mode): work graph work_graph.yaml is schema-valid (root-work-graph/v1); 6 node(s), active: none; declared write targets, disjointness/serialization, and M2 markers check out.
exit=0

$ python3 tools/validation/validate_instruction_tranche_manifest.py    # G4 CI mode
G4 PASS (CI mode): 4 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['ROOT-CLOSEOUT-20260725', 'ROOT-LANE-B-20260725', 'ROOT-STEP8-ACCEPT-20260725', 'ROOT-STEP9-MAT-20260725'].
exit=0
```

```
$ python3 tools/validation/validate_path_anchors.py
PASS: no literal home-dir absolute paths found in 996 live path-anchor surfaces
exit=0

$ python3 tools/validation/validate_instruction_entrypoints.py    (extra, see §3.4)
PASS: root instruction entrypoints are canonical
exit=0

$ git diff --check
exit=0
```

**No retro-invalidation of committed manifests — confirmed two ways.** (a) G4 CI
mode PASSes: all four committed manifests remain schema-valid. (b) Diff-mode
proof of non-causation, below.

```
$ python3 tools/validation/validate_instruction_tranche_manifest.py --base main --head HEAD
G4 BLOCK (diff mode):
  - instruction-surface path 'docs/CONTRACT.md' changed in main..HEAD but is not covered by any declared tranche manifest path
  - instruction-surface path 'docs/DIRECTIVE.md' …
  - instruction-surface path 'docs/PRD_ROOT.md' …
  - instruction-surface path 'docs/SPEC.md' …
  - instruction-surface path 'docs/TYPES.md' …
  - (10 further docs/governance_harness/** paths)
  - instruction-surface path 'tools/validation/validate_root_materialization_fence.py' …
  INFO: diff main..HEAD: 756 changed path(s), 40 on the instruction surface, checked against 4 manifest(s)
exit=1

$ git diff --name-only main..HEAD | grep -c '^CLAUDE.md$'
0
```

This BLOCK is **pre-existing and provably not caused by this tranche**:
`CLAUDE.md` does not appear anywhere in the `main..HEAD` diff, so widening
`INSTRUCTION_SURFACE_FILES` cannot have contributed a single reported path.
Every reported path is a `docs/**` or `tools/validation/**` file changed by
*earlier* commits on this branch. See open item OI-1.

```
$ git status --porcelain
 M docs/CONTRACT.md                                                  # sibling S2
 M docs/SPEC.md                                                      # MINE
 M docs/governance_harness/_DECISIONS/_REGISTER.md                   # sibling
 M tools/validation/test_validate_instruction_tranche_manifest.py    # MINE
 M tools/validation/test_validate_root_surface_ownership.py          # MINE
 M tools/validation/test_validate_root_work_graph_dispatch.py        # MINE
 M tools/validation/validate_instruction_tranche_manifest.py         # MINE
 M tools/validation/validate_root_surface_ownership.py               # MINE
 M tools/validation/validate_root_work_graph_dispatch.py             # MINE
?? docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md   # sibling
?? execution/_Coordination/AgentRuns/ROOT-OGC-20260725/                  # this run
```

Exactly 7 files in my declared write scope, plus this return. In scope.

## 5. Constraint confirmations

- **Write scope honored.** Touched only `docs/SPEC.md`, three validators, three
  test suites, and this return. `docs/CONTRACT.md` (sibling S2), `_REGISTER.md`,
  and `D-GOV-26_owner_gated_closeout.md` were **read only, never written**.
- **Not touched** (explicitly forbidden): `CLAUDE.md`, `.gitignore`, `AGENTS.md`,
  `docs/PRD_ROOT.md`, any `.github/workflows/*` file, any other `docs/*.md`.
- **No commits, no branching, no push.** Working tree left dirty for Agent 0.
- **Minimal-diff discipline.** Two prose insertions in SPEC (one sentence for
  R1, two sentences + two list members for R2); no other SPEC prose altered.
  In the validators, only the guarded-set tuple and the enumerating comments.
  No existing test was modified or deleted; all 7 test changes are additions.
- **Divergences reported, never silently fixed.** Four ratified/adopted
  restatements (R-1…R-4) left byte-identical.
- **No delegation.** Single agent, no subagents dispatched.

## 6. Open items for Agent 0

- **OI-1 — this tranche needs an M2 manifest.** No `ROOT-OGC-20260725.yaml`
  exists under `docs/governance_harness/tranche_manifests/`. My edits are on the
  instruction surface: `tools/validation/**` is already covered by
  `ROOT-LANE-B-20260725.yaml` (it declares all six validator/test files I
  touched), but **`docs/SPEC.md` is covered by no manifest**, nor is the
  sibling's `docs/CONTRACT.md`. G4 diff mode at the PR gate will BLOCK until a
  manifest covers them. Writing it is outside my scope
  (`docs/governance_harness/**`). Recommend one ROOT-OGC-20260725 manifest
  covering `docs/SPEC.md`, `docs/CONTRACT.md`, the six `tools/validation/**`
  files, the D-GOV-26 record, `_REGISTER.md`, and itself. Note the diff-mode
  BLOCK is currently *broader* than this tranche — the 10 `docs/governance_harness/**`
  paths and `docs/{DIRECTIVE,PRD_ROOT,TYPES}.md` from earlier branch commits are
  also uncovered, which is a branch-level manifest-coverage question, not an S1
  finding.
- **OI-2 — disposition F-2 (four diverging restatements).** R-1/R-2/R-3 are
  ratified root governance; R-4 is the adopted PRD's O-1. Each is now an
  incomplete transcription of an amended source. Options: (a) accept as
  incomplete-but-not-contradictory and note it, (b) an M2 correction tranche
  amending all four, (c) amend R-4 only (closest to the changed source). Flagging
  a trap in option (b): DIRECTIVE §2.6 (R-2) pairs its list with the desktop
  `instruction-root/` packaging list, and `.github/workflows/` is almost
  certainly *not* packaged into a desktop bundle — a mechanical find-and-replace
  there would assert something false. `docs/PRD_ROOT.md:948` C-2 shows the
  established handling for exactly this class ("Not amended here — ratified
  instruction surface. Recommend an M2 correction tranche.").
- **OI-3 — disposition F-1 (§0.2.2 vs §0.2.1).** The ruling record D-GOV-26
  item 2 and the S1 brief both say "§0.2.2"; the amendment landed at §0.2.1
  because that is where the enumeration is. Substance matches the ruling exactly;
  only the section label differs. Agent 0 to decide whether the record needs an
  errata note at the human gate.
- **OI-4 — `.github/workflows/harness-premerge.yml` path triggers.** That
  workflow triggers on `AGENTS.md` but **not** on `CLAUDE.md`, even though it
  stages `CLAUDE.md` as instruction content (`:97`). Now that `CLAUDE.md` is
  doctrinally instruction surface, the trigger list arguably should include it.
  Out of my write scope (no CI workflow files); reported, not acted on.
