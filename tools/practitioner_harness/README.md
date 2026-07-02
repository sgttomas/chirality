# tools/practitioner_harness — Charter

A practitioner bench tool over the Chirality governance corpus: it reads
authored files and git history, reports facts with sources, and refuses
objectively broken lifecycle writes. It is not a control plane, not a task
database, and none of its output is authority.

**Basis:** `plans/governance_harness_proposal-B_2026-07-01/governance_harness_plan_v3_2026-07-01.html`
(plan of record; terminal planning artifact) under decisions **D-GOV-01..07**
(`docs/governance_harness/_DECISIONS/`, ruled by the owner 2026-07-01, SHA-bound
at publication commit `82a35c545`). Design changes from here supersede a
D-GOV-* record or arrive as PR review — never a new plan document.

**Pilot scope (D-GOV-03):** `projects/chirality-app-dev`,
`projects/chirality-piping`, and the `_DomainEngines/` control area
(read + report only). `domains/*` deferred; `projects/chirality-governance/`
out of scope by construction; `.archive/` trees excluded from every walk.

## Commands

```sh
python3 tools/practitioner_harness/harness.py status --project app-dev
python3 tools/practitioner_harness/harness.py status --project piping
python3 tools/practitioner_harness/harness.py status --domain-engines
python3 tools/practitioner_harness/harness.py drift --all            # status-vs-history vs the 92/154 baseline
python3 tools/practitioner_harness/harness.py self-check             # restated-state surface audit
python3 tools/practitioner_harness/harness.py brief --project piping --deliverable DEL-02-04
```

Markdown report to stdout; machine-readable JSON via `--json-report` (must
resolve under the declared generated root). `--strict` makes REVIEW findings
exit nonzero.

## Authority classes (plan v3 §Authority Classes)

| Artifact | Class |
|---|---|
| `_STATUS.md`, `_CONTEXT.md`, decision records, dependency registers, DAG approvals, domain profiles | **Authority**, subject to each artifact's own ratification/ruling status, which reports label |
| Engine-owned domain stores (OpenPipeStress persistence) | **Authoritative domain truth** under K-DOMAIN-1 and the adopted profile; outside this tool's cache rule |
| `_harness/adapter.yaml` | **Harness configuration authority only** — governed, committed, human-reviewed; never lifecycle or project truth |
| Tranche brief (CANDIDATE) | **Generated projection** — source-cited, rebuildable, non-authority footer |
| Tranche brief (HUMAN_ADOPTED) | **Committed governed fence** (D-GOV-04); an adoption existing only in a scratch directory does not exist |
| Validation records (`run-validations`, later phase) | **Factual evidence artifact** — never approval, never lifecycle state |
| Status / drift / self-check reports | **Generated view** — never authority, never read back as input |
| Local index cache (none yet) | **Rebuildable projection** — gitignored, one-command regeneration, never cited (D-GOV-01) |
| `write_status.sh` guard | **Refusal mechanism** — blocks objectively broken transitions; never approval, never authorship |

## Write posture — three categories, no unqualified "read-only"

1. **Read-only inspection** — `status`, `drift`, `self-check`: byte-identical
   guarantee over governed files (tested).
2. **Generated-artifact output** — `brief`, report emission: writes land only
   under the declared generated root `{REPO_ROOT}/_harness_generated/`
   (gitignored; safe to delete; rebuildable). Path containment is enforced
   (symlinks, `..`, absolute paths resolved before the check; violations
   refuse, exit 2).
3. **Write-path guard** — `tools/scaffolding/write_status.sh` preconditions:
   ships with the harness, lives outside it. Refuses; never authors.

## Self-exclusion — two classes

Narrative projections (status/drift/self-check reports) are never read back by
any harness component as input. Evidence records (later `run-validations`
phase) may be read as facts for the tranche that produced them and never
promote to lifecycle, approval, plan, or project status.

## Cache contract

For Chirality governance state and harness projections, the only permitted
database pattern is a rebuildable, gitignored cache regenerated from files by
one command, safe to delete, never cited as authority (D-GOV-01). This rule
does not reach developer tooling caches, and it does not reach engine-owned
domain stores (K-DOMAIN-1; D-GOV-01 scope note). No cache is implemented in
this phase.

## Claim language

No harness output says approved, issued, professionally accepted, certified,
sealed, safe, ready for construction, or closed — unless quoting a labeled
human-authored governed artifact. It says narrower things: the artifact is
present or absent; the approval SHA is missing, TBD-pending-publish, reachable,
or unreachable; two current-truth sources conflict; human review required.
Lifecycle state names (`CHECKING`, `ISSUED`) appearing as parsed data values
are quotations of governed sources, not claims. Enforced by
`test_claim_language.py`.

## Severities and exit codes (D-GOV-02)

| Severity | Meaning | Exit behavior |
|---|---|---|
| BLOCK | Objective violation within the declared observation boundary | exit 1 (override: human only, recorded) |
| REVIEW | Material issue requiring human judgment | exit 0 (`--strict`: exit 1) |
| WARN / INFO / NOT_APPLICABLE | Hygiene / context / preconditions absent | exit 0 |

Exit 2 = operational error or refusal (missing identity allowlist per
D-GOV-04, unparseable manifest, output-path containment violation). The
harness adopts 0/1/2 aligned with the newest validator class
(`tools/validation/validate_domain_engine_profile.py`); older tools vary.
`Ruling SHA: TBD` is conditional per D-GOV-02: REVIEW when the artifact
self-declares bind-at-publish; BLOCK only when relied on as bound authority.
No BLOCK ever attaches to the CHECKING→ISSUED judgment itself (K-GATE-1).
Findings against a brief that is not committed + HUMAN_ADOPTED cap at REVIEW
(D-GOV-04).

## Ratification labeling (D-GOV-05 / K-CLAIM-1)

Every report labels the ratification status of each invariant it checks.
Ratified minimal harness basis (D-GOV-05, ruled 2026-07-01): source-of-truth
rule (DIRECTIVE §2.1/§2.3), K-AUTH-1, K-AUTH-2, generated-output rule
(D-GOV-01), K-WRITE-2 (SPEC §0.2.3), K-PROV-1, K-STATUS-1, and the D-GOV-02
severity taxonomy (TYPES §11). All other invariants remain DRAFT on the full
root-ratification track; findings on DRAFT invariants are advisory (never
BLOCK), except purely local technical checks — path containment, source-file
existence, generated-output labeling — which may BLOCK regardless.

## Identity (D-GOV-04)

`docs/governance_harness/human_actors.md` is the identity source for
RuledBy/AdoptedBy/HumanRuling attribution matching. Identity-dependent checks
refuse (exit 2) when it is absent or an attributed actor does not match —
refuse rather than guess.

## Drift baseline

Measured and verified 2026-07-01: **92 of 154** `_STATUS.md` files under the
two pilot `execution/` trees disagree with their own last parsed history
assertion — all 92 in chirality-piping (101 files), app-dev 0/53 clean. The
shared signature: history records an approved advance to CHECKING while the
frontmatter `Current State:` line still reads IN_PROGRESS. `drift` reports
run-over-run counts against this baseline, split by project and caveat class
(`PARSED` / `PARSED_WITH_ASSUMPTIONS` / `UNPARSEABLE`; unparseable histories
are labeled, never guessed). Success is this number trending down; failure is
this tool becoming a cleaner-looking second source of truth.

## Parser: prose-bullet-v1

Versioned parser plugin agreeing with the TypeScript prior art
(`projects/chirality-app-dev/frontend/src/lib/lifecycle/status-parser.ts`) on
the strict grammar, plus eight prose rules for the piping dialect (each hit
labeled `PARSED_WITH_ASSUMPTIONS`). Deliberate v1 limits (documented in the
module): "preserved/retained/kept/verified as X" prose and evidence-lifecycle
bullets ("promoted to COMMITTED") do not yield deliverable states — they are
UNPARSEABLE by design until the History trailer grammar rides D-GOV-05.
Configuration first, parser code only for a genuinely new dialect.

## Guard reconciliation (write_status.sh vs transition.ts)

`tools/scaffolding/write_status.sh` now enforces preconditions reconciled with
chirality-app-dev's `frontend/src/lib/lifecycle/transition.ts` (DEL-07-04):
same six-state order with backward-transition blocking; same allowed from→to
pairs; HUMAN-only CHECKING/ISSUED; same approval-SHA format rule
(`^[0-9a-f]{7,64}$`). Adapter-declared per root (D-GOV-03): app-dev declares
approval-SHA fields, so the git-verifiable SHA precondition blocks there;
piping's status schema carries no SHA fields, so an absent SHA surfaces as
REVIEW and proceeds (schema alignment is a separately-ruled parked item).
Recorded divergences from transition.ts:

1. **Laxer pre-human actor vocabulary.** `transition.ts` binds each transition
   to a fixed actor list (e.g. OPEN→INITIALIZED only `4_DOCUMENTS`); the guard
   accepts any non-empty actor for pre-CHECKING transitions because the live
   corpus contains more spellings (`PREPARATION`, `TASK+*`, `ORCHESTRATOR*`,
   `CHIRALITY_FRAMEWORK`, `WORKING_ITEMS`) and hard enforcement would
   false-block lawful scaffold flows. CHECKING/ISSUED remain HUMAN-only, with
   the same actor normalization (uppercase, whitespace→`_`,
   USER/OPERATOR/HUMAN*→HUMAN).
2. **Same-state re-assert allowed with WARN** (`transition.ts` refuses it as
   TRANSITION_NOT_ALLOWED); the corpus contains lawful re-assert history lines.
3. **New-file creation permitted at OPEN** (`transition.ts` only transitions
   existing documents); creation at any other state is refused.
4. **`--force-human-override <reason>` exists** (HUMAN-only; reason recorded in
   the history line as `[override: ...]`; never overrides usage errors) —
   BLOCK override is human-only and recorded, per D-GOV-02. `transition.ts`
   has no override path.
5. **Approval-SHA requirement is adapter-conditional**
   (`guard_requires_approval_sha` in `_harness/adapter.yaml`), not
   unconditional as in `transition.ts`; no-schema roots get REVIEW-and-proceed.
   The SHA is additionally checked for git reachability
   (`git cat-file -e <sha>^{commit}`), which `transition.ts` does not do.
   Format matched case-insensitively, mirroring `transition.ts`.
6. **Invalid state is exit 2 (usage)** rather than the pre-guard script's
   exit 1, aligning with the adopted operational-error convention.

Stated honestly: tool usage is guided operationally, not enforced — hand edits
bypass any guard. The guard hardens the sanctioned path; drift detection
exists precisely because hand edits happen.

## Generated-view header

Every generated report and brief carries:

> **Generated view — not authority.** Produced by tools/practitioner_harness.
> Sources cited per finding; on any disagreement the cited source files govern.
> Regenerate from project files; safe to delete. Structural checks are not
> approval, issue, authentication, or acceptance of residual risk (K-AUTH-1;
> D-GOV-01).

Missing this header on a file under the generated root is a BLOCK
(`generated_disclaimer_missing`).

## Tests

Co-located pytest (`python3 -m pytest tools/practitioner_harness -q`):
read-only guarantee (byte-identical governed files), drift fixtures modeled on
the `_DomainEngines/` contradictions, path containment (absolute, `..`,
symlink, case), exit-code contract, parser grammar + caveat classes, claim
language, guard behavior matrix, the stale-open-issue (`STALE_OPEN_ISSUE`,
K-STALE-2) and draft-basis-used-as-binding (`DRAFT_BASIS_AS_BINDING` /
`DRAFT_BASIS_RULED_CLOSED`, K-CLAIM-1) checks with their archive fixture
corpus (`test_archive_fixture_corpus.py`), and a live-tree baseline test
(92/154; the three owner-retained stale surfaces must be detected by
`self-check`; `STALE_OPEN_ISSUE`/`DRAFT_BASIS_AS_BINDING` pinned at zero and
`DRAFT_BASIS_RULED_CLOSED` at seven on the live tree).

**Fixture corpus.** The adversarial fixtures in
`test_archive_fixture_corpus.py` are verbatim pre-images from
`git show 15c958e06^` (the state before the D-GOV-06 cleanup slice), with
machine-absolute paths re-anchored to a synthetic `fixture` home-directory
prefix. They live as string constants inside `test_`-prefixed modules on
purpose: loose fixture data files under `tools/` carrying home-dir-absolute
content would fail `tools/validation/validate_path_anchors.py`, and `tools/`
ships verbatim into the public export.
