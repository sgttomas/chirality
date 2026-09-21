# V-SHARD-DEL-02-01-1: verifier notes

- **Run and package:** RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 PKG-02.
- **Unit:** DEL-02-01, the merged ledger of record. The two halves come from the split plan.
- **Shard:** 41 items.
- **Basis:** evidence only, read from the frozen tree at `00115c719`.
- **Status:** these are verdicts, not rulings.

## (i) Counts

| Class | CONFIRMED | REFUTED | CONTESTED | Total |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / REMAINING_WORK) | 6 | 1 | 2 | 9 |
| a30 (sample of other non-ALIGNED) | 18 | 2 | 0 | 20 |
| b (ALIGNED sample) | 1 | 0 | 0 | 1 |
| c (reverse responses) | 11 | 0 | 0 | 11 |
| **Total** | **36** | **3** | **2** | **41** |

**Verdict-field refutations (Addendum 3): 2 of 30 distinct ledger rows (6.7%).**

- `DEL-02-01#CLM-017`: Disposition `ACCEPTED_DIVERGENCE` should be `IMPLEMENTED_DIFFERENTLY` with R4-Q4. The CauseTag primary and CAUSE2 are also inverted.
- `DEL-02-01#CLM-023.2`: Disposition `DOCUMENTED_UNIMPLEMENTED` should be `ALIGNED`. The VER-001 claim map, parity report (PASS) and checklist exist in the Root execution tree under `execution/_Coordination/AgentRuns/SOW-PACKAGE-BATCH-ADOPTION-20260714-01/.../members/DEL-02-01/`.
  - Caveat: CONVENTIONS §7 does not say whether Root `execution/` is in bounds. If the manager rules it out, downgrade this item to CONTESTED.

**Field-only refutation (1):** `DEL-02-01#CLM-030.2`, field Notes. The `SEE:DEL-02-01#REGISTER-3` pointer is missing; Addendum 5 rule 3 requires it.

**CONTESTED (2), both on Disposition:**

- `REGISTER-4`: the MR-5 verdict pair does not fit a duplicate-RefID collision.
- `REM-5`: two elements of the V3-02 Return are not evidenced:
  - redaction proven on path-like fixtures;
  - review PASS for the item.

**Class c:** all 11 responses are CONFIRMED.

- CAP-WOVEN-021: "continue a recorded conversation" sits in tension with SEC-1's "replay … does not resume". The PARTIAL link stands, and R3 may want to note the tension on SEC-1.

## (ii) Systematic patterns

### 1. Half A versus half B: the evidence supports half A

This concerns the matrix/PORTAL reading (CLM-010.1, CLM-010.5, CLM-010.10, CLM-017 and CLM-020.1 in this shard).

**The governing texts keep the old UI:**

- D-APP-74 (`D-APP-74_RULING_2026-07-23.md` L96-108) keeps "current UI" as compatibility surfaces "until separately retired". It also requires separate owner acceptance for old-UI retirement.
- PRD FR-001 (L591) keeps the loop-first UI.
- PRD FR-007 (L602) keeps the "Legacy 3x4 matrix … compatible".
- App DIRECTIVE L234 preserves matrix behaviour through the compatibility period.
- Amended TYPES §4 drops only the *required visual matrix in the target shell*.

**What was retired, and by what:**

- The only governing retirement is D-APP-108 Q3, which unmounts Workbench and Pipeline with their URLs kept.
- The PORTAL loop-first shell and the matrix disappeared through commit `9b005c23a` (v3 four-role adoption). That commit voids the legacy element (`woven-dialogue-route.tsx:18`) and rewrites `agent-matrix.tsx` as a role directory.
- No App ruling retires them.

**Consequences for grading:**

- ACCEPTED_DIVERGENCE fails MR-8 wherever the difference includes the loop-first/matrix UI. So half B's CLM-020.3/.4/.5/.8 and CLM-017 readings are not supported. Of these, only CLM-017 was in this shard, and it is REFUTED.
- IMPLEMENTED_DIFFERENTLY or DOCUMENTED_UNIMPLEMENTED with R4-Q4 is the supported reading.
- CLM-020.1 is correctly ACCEPTED_DIVERGENCE on its own evidence. Its claim covers only route reachability and the Workbench/Pipeline tertiary forms, which Q3 governs.
- CLM-010.1 (REQ-001) differs from CLM-020.1 because it also requires PORTAL reachability.

### 2. `OTHER:V3_ROLE_ADOPTION` (10 checked ledger rows, plus the SEC-1, SEC-2 and SEC-4 rows named by class-c items)

- No vocabulary tag fits exactly:
  - `SHELL_REDESIGN` names SCA-APP-010, and its ob.5 *keeps* the loop-first UI.
  - `V3_RELEASE_SCOPE` needs explicit CONTEXT scope direction, which the adoption run folder does not give. The cited `UI_SOURCE_FREEZE_v7.md` is only a hash list.
- The nearest tag is `V3_RELEASE_SCOPE`. `OTHER` is justified, and no row was refuted on this ground.
- Both halves proposed adding `V3_ROLE_ADOPTION` to the vocabulary.
- The CTX citation to `UI_SOURCE_FREEZE_v7.md` explains little. The mechanism evidence is the commit itself.

### 3. Cross-row CauseTag inconsistency on the stale PRD `MATCH` fact

- CLM-001 and REGISTER-3 use `DOC_HYGIENE`.
- CLM-030.2 uses `CARRIER_PROPAGATION`.
- Both are defensible. R3 should pick one.

### 4. Other points

- **DirectionEvidence:** several R4-Q4 rows omit `GOV:D-APP-108 Q3` even where Q3 explains the Pipeline part (CLM-010.9, CLM-010.10). This is a field-level observation only, and nothing was refuted on it.
- **Reach tags:** all match `REACHABILITY.csv`. SYMBOL-UNREACHED notes were used correctly on statically LIVE but unrendered modules: PortalLoopShell, AgentMatrix, PipelineSurface, WorkbenchSurface and ActivityShelf.
- **PostReleaseBasis:** `TOUCHED_PATHS.csv` contains no App paths, so NO holds everywhere.
- **Line anchors:** all within drift. Examples: chat-panel 2126 vs 2127; woven-dialogue-shell 855 vs 854.

## (iii) Effort

- **Files read:**
  - about 25 frozen-tree files, all by line range: SoW, `_STATUS`, `_REFERENCES`, `Dependencies.csv`, TYPES/PRD/DIRECTIVE excerpts, the D-APP-74/108/127 rulings, and about 15 frontend modules;
  - the evidence pack;
  - three SURFACES capability files, filtered.
- **Git:** read-only only: `git show` on 9b005c23a, b2b32669c, 8362783a2 and 07e1a4f0b; `git blame -L` on PRD L603.
- **Out of bounds:** `projects/chirality-runtime/execution/**` was not read.
- **Context budget:** moderate, not tight.
