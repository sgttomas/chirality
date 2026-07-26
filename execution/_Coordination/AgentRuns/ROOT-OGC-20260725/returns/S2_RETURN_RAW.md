# S2 Terminal Return — K-WRITE-2 gloss amendment (ROOT-OGC-20260725)

Executor: ephemeral bounded Agent 2 generalist (`opus-5`), 2026-07-25.
Brief: `execution/_Coordination/AgentRuns/ROOT-OGC-20260725/briefs/KWRITE2-GLOSS-BRIEF.md`.
Authorization: D-GOV-26 (owner ruling 2026-07-25), item 3 — the K-WRITE-2
gloss debt routed at D-GOV-21 packet §5.1.
Status: COMPLETE. One file changed: `docs/CONTRACT.md` (line 131, K-WRITE-2 row).
No commits.

## Before (entire K-WRITE-2 entry, `docs/CONTRACT.md` §1.10)

```
| **K-WRITE-2** | Agent writes must be **path-contained within the active checkout**. Every `ScopePath` and `AllowedWriteTarget` must normalize to an absolute path that resolves under `git rev-parse --show-toplevel` (`REPO_ROOT`); a target resolving outside it — including via symlink or `..` traversal — is rejected (`SCOPE_OUTSIDE_WORKTREE`) and the task stops. This confines a task's effects to its working root and makes per-working-root and git-worktree isolation safe. | TASK shell (ScopePath normalization, `SPEC.md` §0.2.3); tool path policy; human review of diffs |
```

## After (entire K-WRITE-2 entry)

```
| **K-WRITE-2** | Agent writes must be **path-contained within the active checkout**. Every `ScopePath` and `AllowedWriteTarget` must normalize to an absolute path that resolves under `git rev-parse --show-toplevel` (`REPO_ROOT`); a target resolving outside it — including via symlink or `..` traversal — is rejected (`SCOPE_OUTSIDE_WORKTREE`) and the task stops. This is containment at the checkout boundary: it makes per-checkout and git-worktree isolation safe, but it does not by itself bound a task to a working root inside a monorepo — there a task's effects are bounded by its **declared** write targets (D-GOV-21 M1 fine-grained write ownership), enforced by review, validation, and guard checks against that declaration rather than by the filesystem, and the root product's working root is `REPO_ROOT` itself (D-GOV-21). Gloss amended per D-GOV-26 (docs/governance_harness/_DECISIONS/), ruled 2026-07-25, closing the debt routed at D-GOV-21 packet §5.1; the invariant statement is unchanged. | TASK shell (ScopePath normalization, `SPEC.md` §0.2.3); tool path policy; human review of diffs |
```

Exactly one sentence — the third, explanatory sentence — was replaced. The
normative statement (sentences 1–2), the invariant ID, and the Enforcement
column are byte-identical to HEAD (proved mechanically below).

## Rationale — each changed phrase against the packet §5.1 debt

The routed debt (PACKET.md:164–167): the gloss *"confines a task's effects to
its working root"* **overstates the invariant's mechanical reach in a
monorepo**. Packet §5.1 states the reality: "Within a monorepo checkout,
working-root containment has always depended on narrower accepted scopes —
briefs, declared write targets, agent permissions, and the SPEC §0.2.2
instruction-surface prohibition — not on K-WRITE-2 alone."

| Removed / added | Why |
|---|---|
| Removed: "confines a task's effects to its working root" | The overstated claim named verbatim in §5.1. K-WRITE-2 normalizes against `REPO_ROOT` only; in a monorepo `REPO_ROOT` contains many working roots, so the mechanism cannot discriminate between them. |
| Removed: "per-working-root ... isolation safe" | Same defect, second form: the mechanism makes *checkout* isolation safe, not *working-root* isolation. |
| Added: "This is containment at the checkout boundary" | States the invariant's actual reach — the boundary it does mechanize is `REPO_ROOT`, per the normative sentence that precedes it. |
| Kept (narrowed): "it makes per-checkout and git-worktree isolation safe" | The true residue of the old claim. Git-worktree isolation is genuinely delivered because each worktree has its own `REPO_ROOT`; "per-checkout" replaces "per-working-root" for the same reason. |
| Added: "it does not by itself bound a task to a working root inside a monorepo" | The explicit negation §5.1 requires ("not on K-WRITE-2 alone"), and required by K-CLAIM-1 — the previous gloss asserted a strength the mechanism does not support. |
| Added: "a task's effects are bounded by its **declared** write targets (D-GOV-21 M1 fine-grained write ownership)" | Names what actually does the fine-grained work, per §5.1's list of narrower accepted scopes and D-GOV-21 M1 (PACKET.md:174–179): "Every root package and deliverable declares write targets finer than the checkout, recorded in the static ownership register (G2)." |
| Added: "enforced by review, validation, and guard checks against that declaration rather than by the filesystem" | Distinguishes declaration-plus-enforcement from mechanical filesystem confinement — the precise category error in the old gloss. Matches §5.1's note that these protections were previously prose-enforced and are being mechanized by the D-GOV-21 guards (G1–G4), and CONTRACT's own Enforcement column (TASK shell, tool path policy, human review of diffs). |
| Added: "the root product's working root is `REPO_ROOT` itself (D-GOV-21)" | The ruled root working-root exception. Under it the two boundaries coincide, so the old gloss is not merely imprecise at root — it would read as a containment guarantee that no longer distinguishes anything. Mirrors the citation convention already used at `docs/SPEC.md:48`, `:79`, `:97` ("For the root product only, `WORKING_ROOT` is `REPO_ROOT` (D-GOV-21)"). |
| Added trace: "Gloss amended per D-GOV-26 (docs/governance_harness/_DECISIONS/), ruled 2026-07-25, closing the debt routed at D-GOV-21 packet §5.1; the invariant statement is unchanged." | Supersession trace per the document's own convention (below). |

**Supersession-trace convention followed.** The CONTRACT records amending acts
as an inline citation of the ruling that authorized the change, naming the
decision ID, its `docs/governance_harness/_DECISIONS/` home, and its ruling
date — e.g. `docs/CONTRACT.md:109`: "D-GOV-02
(docs/governance_harness/_DECISIONS/), ruled 2026-07-01 ..." and, appended by
the D-GOV-17 amendment (commit `e7cf58c3a`), "Per D-GOV-17 (ruled
2026-07-18), ...". Header lines 3 and 5 use the same form for the ratification
acts. No separate amendment log or `§3 Retired` mechanism applies (nothing was
retired). The trace deliberately does **not** re-quote the superseded phrase:
the phrase's historical record is preserved in D-GOV-21 PACKET.md:164–167 and
D-GOV-26:42, and re-quoting it in the live catalog would leave the overstating
sentence in the governing surface and falsify the brief's grep check.

## Verification transcript

```
$ python3 -m pytest tools/validation -q
........................................................................ [ 30%]
........................................................................ [ 61%]
........................................................................ [ 92%]
.................                                                        [100%]
233 passed in 2.56s

$ python3 tools/validation/validate_path_anchors.py
PASS: no literal home-dir absolute paths found in 996 live path-anchor surfaces
EXIT=0

$ grep -c "confines a task's effects to its working root" docs/CONTRACT.md
0

$ python3  # byte comparison of the K-WRITE-2 row against HEAD
normative prefix byte-identical: True      # through "... and the task stops."
enforcement column identical: True
OLD GLOSS: This confines a task's effects to its working root and makes per-working-root and git-worktree isolation safe.
NEW GLOSS: This is containment at the checkout boundary: ... the invariant statement is unchanged.

$ git status --porcelain
 M docs/CONTRACT.md                                        # mine
 M docs/governance_harness/_DECISIONS/_REGISTER.md         # not mine (tranche)
?? docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md   # not mine (tranche)
?? execution/_Coordination/AgentRuns/ROOT-OGC-20260725/    # brief + this return

$ git diff --stat
 docs/CONTRACT.md                                | 2 +-
 docs/governance_harness/_DECISIONS/_REGISTER.md | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
```

`docs/SPEC.md` and `tools/validation/` are untouched by this run (absent from
`git diff --stat`); the sibling agent's edits had not landed at the time of
this transcript.

## Constraint confirmations

- Write scope honored: only `docs/CONTRACT.md` (the K-WRITE-2 gloss) and this
  return were written. `docs/SPEC.md` and `tools/validation/` untouched. No
  commit, branch, or push.
- Invariant statement byte-identical (proved above). Invariant ID unchanged.
- Index count line unchanged — "There are **34 stable invariants** across 13
  subsections" is untouched and remains true: no entry added, removed,
  renamed, or moved between subsections. The K-* index row
  `| K-WRITE-2 | 1.10 | Write Scope and Snapshots |` and the §2 Enforcement Map
  rows citing K-WRITE-2 remain accurate — the edit changed no enforcement
  point. No STOP condition arose.
- No other entry was modified (single-line diff).
- Header line 3 ("adding six: **K-WRITE-2** (ScopePath containment) ...") and
  the line 5 ratification-history reference to K-WRITE-2 remain accurate: the
  invariant's substance is unchanged, only its explanatory gloss.
- The §1.13 closing paragraph ("K-WRITE-2 continues to govern agent and tool
  writes to project truth ... they do not grant an agent permission to write
  outside its checkout scope") was checked for consistency and needs no edit —
  it already frames the guarantee as *checkout* scope, matching the corrected
  gloss.

## Residual surfaced (out of my write scope — for Agent 0's disposition)

`docs/thesis/appendix_a_invariant_catalog.md:134` carries a verbatim mirror of
the K-WRITE-2 row, including the now-superseded gloss sentence. That file
declares "The ratified K-* catalog in `docs/CONTRACT.md` governs on
divergence", so the divergence is governed and not a contract defect — but the
thesis appendix now presents the overstating gloss as live text. No validator
enforces CONTRACT/appendix sync (233 validation tests pass with the divergence
present). Recommend a follow-on mirror update under the appropriate
instrument; I did not touch it, as it is outside my sealed write scope.

The other repo-wide occurrences of the superseded phrase are correct
historical/citational records and must not be changed:
`docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md:165`
(the routing itself), `docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md:42`
(the ruling quoting the debt), and
`execution/_Coordination/PRD_CANDIDATE_2026-07-25_concordance_annex.md:301`
(the annex's carried-debt entry — Agent 0 may wish to mark that entry closed
by D-GOV-26 when reconciling the annex).
