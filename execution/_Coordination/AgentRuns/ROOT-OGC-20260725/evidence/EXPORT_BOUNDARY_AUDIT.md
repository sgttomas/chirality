# Export-Boundary Audit — evidence for the standing regeneration deferral

Run: `ROOT-OGC-20260725`, stage S3. Executor: ephemeral bounded Agent 2
generalist (`opus-5`) under the sealed brief
`execution/_Coordination/AgentRuns/ROOT-OGC-20260725/briefs/EXPORT-AUDIT-BRIEF.md`.
Authorization: owner ruling 2026-07-25, recorded in
`docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md` item 4.

**Mode: READ-ONLY.** No export was run. No file outside this audit and the
stage return was written. The two writes made by the exporter to tracked
files (`export-manifest.csv`, `export-report.md`) were **not** performed; all
comparison against current tree state was done by an independent
read-only re-implementation of the profile's own traversal and scan rules.

**Audit basis.**

| Field | Value |
|---|---|
| Audited tree | worktree on branch `claude/root-owner-gated-closeout-20260725`, HEAD `4aaa66483` (merge of PR #350) |
| Last commit that refreshed the export artifacts | `5af6c4a49` (2026-07-24, "Make exported validation tests fixture-aware") — verified ancestor of HEAD |
| Profile audited | `exports/chirality-app/export_public.py` (401 lines), plus `exports/chirality-app/README.md` (profile doctrine) and `exports/chirality-app/PUBLIC_README.md` (the staged public landing page) |
| Uncommitted state in the audited worktree | sibling edits to `docs/CONTRACT.md`, `docs/governance_harness/_DECISIONS/_REGISTER.md`; new untracked `docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`; this run's own `execution/_Coordination/AgentRuns/ROOT-OGC-20260725/` |

---

## 1. Allowlist summary (the boundary contract, PRD D-10)

The profile is a **pure allowlist copier with a fail-closed post-scan**. It
consumes no external config file; the allowlist is the module's own constants.
Nothing is read from the tree to decide membership.

### 1.1 Membership

**Root files copied verbatim (`ROOT_FILES`, 6):** `.gitignore`, `AGENTS.md`,
`CLAUDE.md`, `CHIRALITY_FRAMEWORK.md`, `PROFESSIONAL_ENGINEERING.md`,
`LICENSE.md`.

**Root file substituted (`PUBLIC_ROOT_FILES`, 1):** staged `README.md` is
copied from `exports/chirality-app/PUBLIC_README.md`. The canonical root
`README.md` is deliberately **not** copied.

**Root directories copied recursively (`ROOT_DIRS`, 7):** `.github`, `agents`,
`skills`, `tools`, `docs`, `init`, `runtime`.

**Generated in-stage (1):** `init/init-prompt.md` is overwritten with a
framework-only public launcher, replacing the private loop entrypoint.

Everything else at the repository root is outside the allowlist by
non-membership — the copier never visits it. At the audited basis that means
`execution/`, `projects/`, `domains/`, `plans/`, `_DomainEngines/`,
`exports/`, and root `README.md`.

### 1.2 Subtractions applied inside allowlisted roots

- `EXCLUDED_PUBLIC_PATHS` (exact, 2): `.github/workflows/harness-premerge.yml`,
  `tools/practitioner_harness/BACKLOG.md`.
- `EXCLUDED_PUBLIC_PREFIXES` (1): `docs/governance_harness/briefs/`.
- `SKIP_DIRS` (any path component, 26): `.git`, `.Archive`, `.archive`,
  `.claude`, `.chirality`, `.checkpoints`, `.pytest_cache`, `__pycache__`,
  `.mypy_cache`, `.ruff_cache`, `node_modules`, `.next`, `dist`,
  `dist-electron`, `build`, `target`, `out`, `artifacts`, `_Sources`,
  `_LocalIndexes`, `migration`, `projects`, `domains`, `plans`, `exports`.
  Note this list also blocks those names **nested** anywhere inside an
  allowlisted root, which is what keeps `runtime/node_modules`,
  `tools/**/__pycache__`, and any nested `_Sources` corpus out.
- `SKIP_FILE_NAMES`: `.DS_Store`. `SKIP_SUFFIXES`: `.pyc`, `.pyo`, `.zip`,
  `.pdf`, `.PDF`, `.tsbuildinfo`. Any file whose name starts with `.env`.

### 1.3 Sanitization

`sanitize_text_files()` rewrites 17 text suffixes, applying 6 ordered literal
replacements that map the **legacy** `/Users/ryan/ai-env/projects/...` roots to
placeholders (`<chirality-root>`, `<chirality-app-root>`,
`<legacy-chirality-*>`, `examples/`). Sanitization is a convenience layer, not
the guarantee — see §1.4.

### 1.4 Failure conditions (what makes the export refuse)

1. **Missing allowlist entry** — `build_stage()` raises `SystemExit` listing
   any `ROOT_FILES`/`ROOT_DIRS`/`PUBLIC_ROOT_FILES` entry absent from the
   tree, rather than silently skipping (owner ruling 2026-07-01, recorded in
   the profile README).
2. **`CLAUDE.md` drift** — must contain exactly `@AGENTS.md\n`, else
   `SystemExit`.
3. **Boundary scan findings** — `boundary_findings()` walks the *staged* tree
   and returns exit code **2** (no apply, report written) on any of:
   - public README missing any of 3 required markers, or containing any of 5
     forbidden private-canonical markers;
   - a top-level path in `{projects, domains, migration, plans, exports}`;
   - a directory whose name is in `SKIP_DIRS`;
   - a `.DS_Store`, `.env*`, `.pyc`, `.zip`, `.pdf`, `.tsbuildinfo` file;
   - **any residual `/Users/…/`, `/home/…/`, or `C:\Users\…\` path** in a text
     file (excluding `<placeholder>`, `example`, `fixture` forms).
4. `apply_target()` refuses a target without a `.git` directory, and only runs
   when `--apply-target` is passed explicitly.

**The load-bearing safety property is (3)'s private-home regex, not the
replacement list.** The replacement list is stale with respect to the current
checkout location, but a stale replacement list cannot leak: an unmatched
private absolute path is not rewritten and is therefore *caught by the scan*,
failing the export. The profile fails closed on the one leak class it most
plausibly encounters.

### 1.5 Dry-run equivalence check (read-only re-implementation)

Re-applying the profile's traversal, exclusion, sanitization, and scan rules
to the current tree without writing anything:

| Check | Result |
|---|---|
| All 13 `ROOT_FILES` + `ROOT_DIRS` entries present | PASS (13/13) |
| `CLAUDE.md == "@AGENTS.md\n"` | PASS |
| Public README required markers (3) | PASS — none missing |
| Public README forbidden markers (5) | PASS — none present |
| Residual private-home paths after sanitization, across all staged text files | **0 findings** |
| Files that would stage | **738** (vs. 711 in the tracked manifest) |
| Ignored-but-present files inside allowlisted roots that could sweep in | only `tools/*/__pycache__/` — all covered by `SKIP_DIRS` |
| Credential-pattern scan (`sk-ant-`, `ghp_`, `AKIA…`, PEM private keys) across allowlisted roots | 0 hits |

A regeneration run at this basis would therefore be expected to **succeed with
zero boundary findings**. The deferral is not masking a failing export.

---

## 2. IN/OUT determination for repository state added since the profile was last exercised

Changes between `5af6c4a49` and HEAD `4aaa66483`: 305 files added under
`execution/`, 440 added + 106 modified + 4 renamed + 1 deleted under
`projects/`, 6 under `_DomainEngines/`, 4 under `domains/`, and **58 files
inside allowlisted roots** (30 added, 28 modified).

| Repository state | IN / OUT | Governing rule |
|---|---|---|
| Root `execution/PKG-01…PKG-06` trees | **OUT** | `execution` is not in `ROOT_DIRS` — never traversed. Concurred by `docs/PRD_ROOT.md` §9.4 (RD-4) and D-GOV-21 packet §4 ("Root `execution/` remains outside the export allowlist"). |
| Root `execution/_harness/` guard state (`adapter.yaml`, `root_guards.yaml`, `surface_ownership.yaml`, `work_graph.yaml`) | **OUT** | Same non-membership rule. Explicitly relied on in `tools/validation/validate_root_harness_adapter.py` module docstring: "Root `execution/` is outside the public-export boundary (packet §4)". |
| `execution/_Decomposition/` | **OUT** | Non-membership. |
| `execution/_Coordination/AgentRuns/` (incl. this run) | **OUT** | Non-membership. |
| `execution/_Reconciliation/`, `_Evaluation/` | **OUT** | Non-membership. |
| `projects/*`, `domains/*`, `plans/*`, `migration/*` | **OUT ×2 (defence in depth)** | Non-membership **and** listed in both `SKIP_DIRS` and the scan's `forbidden_top`. |
| `_DomainEngines/` (6 files changed since basis) | **OUT** | Non-membership only — **not** in `SKIP_DIRS`, **not** in `forbidden_top`. Currently harmless because it is a root sibling the copier never visits; see caveat C3. |
| Root `README.md` (modified since basis) | **OUT** | Deliberately replaced by `PUBLIC_README.md` via `PUBLIC_ROOT_FILES`. |
| `exports/**` (this profile, its manifest, report, PUBLIC_README) | **OUT** | Non-membership + `SKIP_DIRS` + `forbidden_top`. This is what keeps the `--apply-target` machine path in `exports/chirality-app/README.md` out of the public tree. |
| **Decision records** `docs/governance_harness/_DECISIONS/D-GOV-21…26` (6 new) | **IN** | `docs` is allowlisted; `_DECISIONS/` is not excluded. Deliberate: the profile README states "Public governance decisions, their handoff, and `human_actors.md` remain in scope because authority verification depends on them". |
| Proposal packets `docs/governance_harness/_PROPOSALS/D-GOV-21…24/PACKET.md` (4 new) | **IN** | Same rule. Only `docs/governance_harness/briefs/` is prefix-excluded. |
| `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` | **IN** | Same rule. |
| **Tranche manifests** `docs/governance_harness/tranche_manifests/*.yaml` (4 new — the directory did not exist at the last export; 0 rows in the tracked manifest) | **IN** | `docs` allowlisted, no exclusion covers the directory. See §3.2 — this is the one materially new consequence. |
| `docs/PRD_ROOT.md` (adopted root PRD) | **IN** | `docs` allowlisted. **Deliberate and owner-ruled**: RD-4 (`docs/PRD_ROOT.md` §9.4, RULED 2026-07-25, Receipt 38) selected option D — adopted bytes in root `docs/` "publishing through the **existing** export allowlist … so **no boundary change occurs**", candidates and revision evidence remaining in root `execution/`. |
| `tools/validation/validate_root_*.py` + `validate_instruction_tranche_manifest.py` and their 5 test files (11 new) | **IN** | `tools` allowlisted. Functional consequence assessed in §3.2. |
| `tools/practitioner_harness/test_root_adoption.py` and 7 modified harness files | **IN** | `tools` allowlisted; only `BACKLOG.md` is path-excluded. |
| `.github/workflows/governance-harness.yml` (modified: adds G0–G4 steps) | **IN** | `.github` allowlisted; only `harness-premerge.yml` is path-excluded. |
| `docs/SPEC.md`, `docs/CONTRACT.md`, `docs/DIRECTIVE.md`, `docs/TYPES.md`, `docs/DBM_Agent_Instruction_Architecture.md`, 9 `docs/thesis/*` | **IN** | `docs` allowlisted. All stale in the staged manifest. |
| `runtime/**` (5 modified: `package.json`, lockfile, CLI sources/tests) | **IN** | `runtime` allowlisted per D-GOV-20. `runtime/node_modules` excluded by `SKIP_DIRS`; no credential, user-data, machine-registration, or model artifact found in the staged subset (packages: cli, client, contracts, core, daemon, engine-claude, engine-pi-omlx — sources, tests, tsconfigs, package manifests only). |
| `agents/AGENT_CHANGE.md`, `skills/pandid-valve-tile/SKILL.md` | **IN** | Allowlisted roots. |

**No state added since the last export crosses from OUT to IN.** Every new
private-evidence surface produced by the root loop (PKG trees, guard state,
decomposition, run records) lands under `execution/`, which is outside the
allowlist by construction and additionally cited as outside it by the guards
themselves. The additions that are IN are governance documents, validators,
and CI config — all of them classes the profile already exported before this
period.

---

## 3. Staleness of existing staged content

### 3.1 What is actually committed under `exports/`

Only four tracked files: `export_public.py`, `README.md` (profile doctrine),
`PUBLIC_README.md` (the authored public landing page), `export-manifest.csv`
(711 rows), `export-report.md`. **No staging tree is committed** —
`.gitignore` lines 115–118 exclude `exports/*/staging/`, `staging-*/`,
`latest/`, and no `exports/chirality-app/staging/` directory exists. There is
therefore no stale *tree* on disk that could be applied by accident; an apply
requires a fresh `build_stage()` first, because `--apply-target` copies from
the stage the same run just built.

That is the single strongest fact for the deferral: **the deferral cannot
leave a stale artifact where a fresh one is expected, because the artifact
that gets published does not persist.**

### 3.2 What a regeneration would materially change (headline)

| Surface | Change |
|---|---|
| Manifest row count | 711 → **738** (+27) |
| `docs/` | 72 → **88** files (+16): the adopted root PRD, 6 D-GOV decision records, 4 proposal packets, the D-GOV-21 handoff, and the 4 tranche manifests — plus content-hash churn on `SPEC`, `CONTRACT`, `DIRECTIVE`, `TYPES`, the decision register, and 9 thesis chapters |
| `tools/` | 334 → **345** files (+11): the 5 root guards + 5 test files + `test_root_adoption.py`, plus hash churn on 8 practitioner-harness files |
| `.github/`, `agents/`, `skills/`, `runtime/`, `init/` | file counts unchanged; content hashes change for `governance-harness.yml`, `AGENT_CHANGE.md`, `pandid-valve-tile/SKILL.md`, and 5 runtime files |
| `export-report.md` | staging path, counts, and per-top-level table update; boundary findings expected to remain **0** |

### 3.3 Stale claims in staged content that could mislead

Three findings, all in the *narrative* surfaces rather than the mechanism:

**S1 — `PUBLIC_README.md` carries pre-D-GOV-23 genus framing.** It opens
"Chirality is a governed **macOS application environment** for agent-assisted,
deliverable-heavy professional work." D-GOV-23 (RULED 2026-07-25) superseded
the genus in `docs/DIRECTIVE.md` §1 toward "canonical human-governed
application environment **and generative operating form** for governed
professional knowledge work", and D-GOV-22 adopted the root PRD whose RD-1
fixes a two-level genus. Regeneration does **not** fix this: `PUBLIC_README.md`
is an authored file the exporter copies verbatim, so it only changes when
someone edits it. This is a propagation gap, not an export-mechanism gap.

**S2 — `PUBLIC_README.md`'s Repository Contents table omits `.github/`,** which
the profile does export (2 files). Cosmetic; the analogous defect in the
private root `README.md` (omitting `runtime/`) is already recorded as
concordance finding **C-4** in `docs/PRD_ROOT.md` §10.2 with `HumanRuling = TBD`.

**S3 — the tracked `export-manifest.csv` and `export-report.md` understate the
tree by 27 files and are hash-stale across ~28 more.** They are derivative
records of a run at `5af6c4a49`; under the AGENTS.md derivative-package rule
they must cite their basis, and at present they carry no basis annotation
inside the artifacts themselves (the basis is recoverable only from git
history). They do not gate anything and are not consumed by any validator.

None of S1–S3 is a disclosure risk. S1 is the only one that would mislead a
reader, and it misleads about *product framing*, not about what is or is not
published.

### 3.4 Functional consequence in the public repository (new since the basis)

The exported `.github/workflows/governance-harness.yml` now runs G0–G4. Four
of the five are explicitly designed to **PASS-idle when their state surface is
absent**, which is exactly the public tree's condition (no `execution/`):

- **G0** materialization fence — no `PKG-*`/`DEL-*` children ⇒ PASS idle;
  `execution/` not a directory is handled.
- **G1** harness adapter — manifest absent and nothing materialized ⇒ PASS idle.
- **G2** surface-ownership register — no packages and no register ⇒ PASS idle.
- **G3** work-graph — surface absent ⇒ PASS idle (CI mode).
- **G4** instruction-surface tranche manifest — **does not depend on
  `execution/`**; it reads `docs/governance_harness/tranche_manifests/`, which
  **is** exported.

G4 is therefore the exception, and it produces a concrete finding:
`docs/governance_harness/tranche_manifests/ROOT-CLOSEOUT-20260725.yaml`
declares `m6_notice.disposition: routed` with
`routed_to: [domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md]`,
and the validator asserts `(root / notice).exists()`, emitting
`"routed notice … does not exist"` as a BLOCK failure otherwise. `domains/` is
in `SKIP_DIRS` **and** `forbidden_top` — it can never be exported. **A public
export taken at this basis would ship a CI workflow that fails on its own
tree.** The other three manifests use `disposition: none-required` with empty
`routed_to` and are unaffected.

This is a *pre-publication defect surfaced by the deferral*, not caused by it —
and it argues for the deferral, since the next actual export need is the right
moment to resolve it (options include a fixture-aware exception in the
validator, mirroring the earlier "Make exported validation tests fixture-aware"
fix at `5af6c4a49`; excluding `tranche_manifests/` from the export; or excluding
G4 from the public workflow). **This audit decides none of them.**

---

## 4. Ambiguity flagged under the D-GOV-20 export boundary (owner's to settle)

D-GOV-20 permits generic runtime/CLI/contracts/safe adapters and excludes
credentials, machine state, downloaded models, and private project
adapters/evidence. Two items sit at the edge; neither is decided here.

**A1 — Governance records that *name* private-tree paths.** Exported
governance documents contain repo-relative references into `projects/*` and
`domains/*` — e.g. `ROOT-CLOSEOUT-20260725.yaml` cites
`domains/chirality/_Sources/Source_Manifest.csv` "row 37" and a sha256 pin;
`D-GOV-21_IMPLEMENTATION_HANDOFF.md` names two private coordination notice
paths; `D-GOV-23`/`D-GOV-24` name `projects/chirality-app-dev` pinning
behaviour; `docs/PRD_ROOT.md` names `projects/*`/`domains/*` as consuming
contexts. These are *references and structural facts*, not private evidence
content, and the profile permits them (they are not machine-absolute, so the
scan does not fire). Whether disclosing the existence, names, and pin
structure of private project and domain workspaces is intended publication is
a **publication judgement**, and RD-4 shows the owner treats such questions as
his. Volume is low (16 such references in the D-GOV-21 packet, 1–3 in each
other file).

**A2 — Proposal packets as a class.** `_PROPOSALS/*/PACKET.md` are exported
because only `docs/governance_harness/briefs/` is prefix-excluded. Packets
record declined options, adversarial-review history, and internal deliberation
(the D-GOV-21 packet even carries a deliberately dangling
`projects/chirality-root/` reference recorded as an accepted WARN). Decisions
are clearly intended to publish — authority verification depends on them.
Whether *candidate deliberation* is equally intended is not stated anywhere in
the profile doctrine, and this class predates the audited period, so it is
raised as a standing question rather than a change.

---

## 5. Verdict

> **SAFE — WITH CAVEATS.** The standing deferral of export-staging
> regeneration accumulates **no leak risk** and **no silent staleness
> hazard**.

Grounds:

1. **Leak risk is structurally zero for everything the deferral defers.** All
   state added since the last export lands under `execution/`, `projects/`,
   `domains/`, or `_DomainEngines/`, none of which the allowlist copier ever
   visits. The three private trees are additionally blocked twice more
   (`SKIP_DIRS`, `forbidden_top`). Deferral cannot expand an allowlist that is
   a source constant.
2. **The mechanism fails closed, and the fail-closed path is the one that
   matters.** The residual `/Users|/home|C:\Users` scan makes the stale
   replacement list a *failure* mode, not a *leak* mode. A dry-run over the
   current tree produces 0 findings and 738 staged files.
3. **No stale artifact can be published.** The staging tree is gitignored and
   absent; `--apply-target` copies only from a stage built in the same run, so
   there is no path by which "deferred" becomes "published something old".
   The pre-existing handoff instruction — "do not apply an export from a
   pre-D-GOV-21 staging" — is enforced by construction as well as by
   instruction.
4. **Regeneration remains deterministic and currently green.** All 13
   allowlist entries exist, `CLAUDE.md` is byte-exact, both README marker sets
   pass, no credential patterns appear in allowlisted roots, and no ignored
   file inside an allowlisted root escapes `SKIP_DIRS`.
5. **The deferral is authorized in form.** D-GOV-21 packet §4 permitted
   "Regenerate the export staging in the implementation tranche, **or defer
   explicitly in the handoff state with source SHA named**"; the handoff does
   exactly that.

Caveats attaching to the disposition:

- **C1 — G4 will fail in the public tree at the next export.** The routed
  notice in `ROOT-CLOSEOUT-20260725.yaml` points into `domains/`, which is
  unexportable, and the exported `governance-harness.yml` runs G4. This must
  be resolved **before** the next apply, not before the next commit. It is a
  correctness defect in the published CI, not a disclosure defect.
- **C2 — `PUBLIC_README.md` will not self-heal.** Regeneration copies it
  verbatim; the pre-D-GOV-23 genus framing (S1) and the missing `.github/` row
  (S2) require an authored edit. Whoever triggers the next export should treat
  the landing page as an authoring task, not a regeneration output. S2 is the
  sibling of the already-open C-4 finding in `docs/PRD_ROOT.md` §10.2.
- **C3 — the allowlist has no negative-space alarm.** A future root-level
  directory becomes OUT silently, by nobody adding it. This is correct-by-
  default and is why leak risk is zero, but it also means `_DomainEngines/`
  (added since the basis) is OUT with no record that anyone considered it. The
  profile alarms loudly on a *removed* allowlist entry and says nothing about
  an *added* root sibling. Not a defect at this basis; a monitoring gap if the
  deferral runs long.
- **C4 — RD-4's amendment obligation sits alongside the deferral.**
  `docs/PRD_ROOT.md` §9.4 states that, the adopted PRD having joined the
  instruction surface, "every amendment is an M2 instruction-surface tranche
  requiring independent owner authorization, a tranche manifest, routed
  notices, **and export-manifest regeneration** (D-GOV-21 M2/G4/M6)". A
  standing deferral does not contradict that for tranches already closed under
  the explicit-deferral clause, but the owner may wish to state which of the
  two governs a **future** PRD amendment tranche. Flagged, not resolved.
- **C5 — the derivative artifacts carry no basis annotation.** `export-manifest.csv`
  and `export-report.md` do not name the commit they were generated from; the
  basis (`5af6c4a49`) is recoverable only from git history. Under the AGENTS.md
  derivative-package rule a citation would be preferable. Non-blocking.
- **C6 — two publication questions are open** (§4 A1/A2): governance records
  that name private-tree paths and pin structure, and proposal packets as an
  exported class. Both predate the audited period; both are owner judgement.

Nothing found in this audit argues for regenerating now rather than at the
next actual export need — and C1 argues affirmatively that regenerating now
would produce a public tree with red CI, so the next *need* is the correct
trigger and the correct occasion to fix C1 and C2 together.
