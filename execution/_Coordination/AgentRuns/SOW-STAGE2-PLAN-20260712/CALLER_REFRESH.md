# D-GOV-16 Active Caller Refresh

Status: `PASS — ALL OBSERVED ACTIVE CALLERS CLASSIFIED`
Basis: `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`

## Result

No unclassified active caller was found. The current active surfaces are
already candidate-aware but remain Stage-1-gated; Stage 2 must replace that
pilot posture with the ruled `SOW_V1`/`LEGACY_FOUR_DOC` transition contract
before any deliverable conversion.

The original inventory vocabulary reproduced 5,365 tracked matching paths on
the current basis, versus 5,307 at its older observation. Its current sorted
path-list SHA-256 is:

```text
cec0137408ec558adf84f698e8937af922efe13cb05243bdeb850defa924a155
```

The 58-path increase is classified as the ruled Stage-1/D-GOV-16 governance,
run evidence, and candidate machinery added since the older observation. It
does not add a migration member or an unclassified executable caller.

| Top-level family | Current matching paths | Disposition |
|---|---:|---|
| `_DomainEngines/` | 1 | historical loop evidence; preserve |
| `agents/` | 6 | active instruction consumers; activation tranche |
| `docs/` | 24 | canon, current explanation, proposal, and historical governance; split below |
| `domains/` | 2,494 | independent DOMAIN/KTY schemas and generated evidence; out of scope |
| `execution/` | 41 | immutable Stage-1 and other run evidence; preserve |
| `exports/` | 1 | derivative; regenerate from accepted canon when applicable |
| `plans/` | 1 | historical planning evidence; preserve |
| `projects/` | 2,755 | 616 source documents, project history/evidence, and App runtime consumers; do not bulk-rewrite |
| `skills/` | 23 | active, compatibility, and independent-schema skills; split below |
| `tools/` | 19 | active, compatibility, and independent-schema tools; split below |

The count above deliberately retains the original inventory vocabulary. A
second targeted search for `ScopeOfWork.md`, `SOW_V1`, `LEGACY_FOUR_DOC`,
`PILOT_DUAL`, and `MIGRATION_DUAL` was used to locate the new transition
consumers.

## A. Exact canon activation

These are authoritative or current explanatory surfaces, not historical
evidence:

| Surface | Current state | Required Stage-2 disposition |
|---|---|---|
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | Stage-1 candidate; SHA-256 `8409bf3cebb3af947f54cca9d2e1c0b62445041bf72b81bd8aef912ce9fc0013` | Replace byte-for-byte with ruled standard SHA-256 `7f742901...85a6f` |
| `docs/TYPES.md` | pre-successor SHA-256 `6b17e67e...1d45` | Apply only ruled `TYPES.proposed.patch` |
| `docs/SPEC.md` | pre-successor SHA-256 `4cb7e341...d6a8b` | Apply only ruled `SPEC.proposed.patch` |
| `docs/DIRECTIVE.md`, current architecture/design explanations | speak in four-document terms | Update only live explanatory claims after exact canon activation; do not rewrite historical evidence |
| proposal and D-GOV files | immutable ruling/evidence | retain byte-for-byte |

The canon activation must be an exact-copy/exact-patch operation with hashes
checked before and after. It must not combine interpretation edits with the
ruled bytes.

## B. Active agents and manager contracts

The activation tranche must remove Stage-1-only variance semantics and make
format resolution explicit in:

- `agents/AGENT_ORCHESTRATOR.md` — new PROJECT/SOFTWARE initialization uses
  `scope-of-work`; existing `LEGACY_FOUR_DOC` remains transitional; migration
  is lifecycle-neutral;
- `agents/AGENT_REVIEW.md` — `SOW_V1` consumes deterministic checklist output
  without duplicate extraction; legacy review remains supported; an actual
  human-gated review, not compilation, owns semantic disposition;
- `agents/AGENT_AUDIT_EPISTEMIC.md`, `AGENT_AUDIT_DECOMP.md`, and
  `AGENT_EVALUATION_STRUCTURE_AUDIT.md` — resolve canonical, legacy,
  migration-dual, ambiguous, and invalid states under D-GOV-16;
- `agents/AGENT_WORKING_ITEMS.md` and `AGENT_RECONCILIATION.md` — replace
  pilot-only authority with conversion receipts, atomic replacement, wave
  fan-in, rollback, and single-format closure;
- `agents/AGENT_PREPARATION.md` and `AGENT_PROJECT_DECOMP.md` — preserve the
  DOMAIN boundary and direct new PROJECT/SOFTWARE production initialization to
  `SOW_V1`.

The instruction activation is root-owned by HELPS_HUMANS. It is not a license
for these agents to edit lifecycle state during migration.

## C. Active skills and deterministic tools

### Migrate now

- `skills/scope-of-work/` must support explicit `INIT`, `CONVERT`, and
  `VERIFY` modes under D-GOV-16. `CONVERT` remains deterministic and
  lossless; `INIT` is source/decomposition-grounded; all modes fail closed.
- `skills/content-digest/`, `deliverable-consistency/`, `proposal-format/`,
  `semantic-matrix-build/`, `lens-register/`, and `semantic-lensing/` must
  replace `SOW_V1_CANDIDATE`/Stage-1 variance inputs with resolver-selected
  `SOW_V1`, while retaining `LEGACY_FOUR_DOC` compatibility.
- `tools/scope_of_work/` must replace `PILOT_DUAL` and D-GOV-15-only checks
  with the D-GOV-16 `MIGRATION_DUAL` authority contract, retain fail-closed
  ambiguous/partial behavior, support ISSUED refusal unless the exact
  administrative authority is supplied, and preserve deterministic map,
  parity, checklist, and HTML behavior.
- `tools/validation/scan_deliverable_consistency.py`, semantic-pipeline
  validators, `tools/reporting/generate_coverage_csv.py`, and
  `tools/evaluation/count_deliverable_files.sh` must resolve both accepted
  formats without silently changing existing report columns.
- `tools/REGISTRY.md`, `tools/EXTERNAL_TOOLS.md`, and `skills/README.md` must
  describe the active contract. Applicable exports are regenerated from these
  accepted sources.

### Retain through rollback

`skills/four-documents/`, legacy readers, legacy-only checks, and
`tools/validation/check_four_documents.sh` remain supported compatibility
surfaces. They must reject new PROJECT/SOFTWARE initialization after
activation but continue validating existing `LEGACY_FOUR_DOC` members. They
are not retirement targets in this plan.

### Independent schemas

`skills/domain-documents/`, scope-change packets, SCC-resolution cases,
drawing extraction, DOMAIN/KTY identifiers, packet/case schemas, fixtures,
templates, and archives retain their independent grammars. Similar ordinary
words and short IDs do not make them deliverable-format callers.

## D. App Dev runtime consumers

The active runtime seam is:

- `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts`;
- `projects/chirality-app-dev/frontend/src/components/shell/document-view.tsx`;
- associated workspace, scanner, document-contract, API, MCP, dependency, and
  UI tests under `frontend/src/__tests__/`.

The current UI makes `ScopeOfWork.md` feature-flagged and the scanner
recognizes a Stage-1 `PILOT_DUAL` variance. Activation must instead:

1. show the selected canonical production contract;
2. allow existing legacy-only folders during transition;
3. make `ScopeOfWork.md` normal for `SOW_V1`;
4. fail partial and unauthorized dual formats closed;
5. keep control-plane and DOMAIN/KTY documents unaffected; and
6. pass the full applicable App typecheck, build, unit/integration, scanner,
   API/MCP, and rendered-view checks.

This App-runtime work has disjoint writes from root agent/skill/tool activation
and may be prepared concurrently, but both lanes must fan in before conversion.

## E. Historical, source-content, explanatory, and derivative material

- The 616 legacy production documents are migration sources, not callers to
  bulk-rewrite in the activation tranche.
- `_STATUS.md` histories, receipts, plans, reviews, concordance ledgers,
  Stage-1 evidence, and old decision packets remain byte-identical.
- Current explanatory canon may be updated after the exact standard lands;
  thesis snapshots and historical design analysis remain historical unless an
  owning publication workflow expressly regenerates them.
- Exports are derivative and must be regenerated from accepted source rather
  than hand-edited as authority.

## Gate and rerun rule

HELPS_HUMANS must emit a refreshed machine-readable caller manifest after the
activation changes. EVALUATION and RECONCILIATION must confirm that every
active caller is migrated or expressly retained before the census/manifest
freeze releases conversion. Any new active caller, unclear classification, or
scope overlap stops the dependent graph and returns a decision request.
