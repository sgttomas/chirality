# TRANCHE — D-PEC-08 O-A: embedded upload-agent v1 (import proposals)

> **Epistemic status: tranche packet, executed under the D-PEC-08 O-A ruling
> (2026-07-05).** This packet names the exact file fence, tests, deferred
> D-PEC-07 obligation handling (RV-13..21), and the rollback/verification plan
> the ruling requires. The adopted design brief
> `_DomainEngines/proposals/pec/BRIEF_2026-07-05_embedded_upload_agent_design.md`
> is the design authority; on any disagreement between this packet and the
> ruled decisions (D-PEC-07/08, D-T0-13/14), the ruled decisions govern.
>
> Structure precedent: this packet follows the TOOLMAKER brief pattern of
> `_DomainEngines/pec/PEC_2026-07-04_tier0-prep/TOOLMAKER_BRIEF-harness_pec_registration.md`
> and the coordination-surface conventions of
> `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` (RV-20).

## Authorization chain

1. D-PEC-07 O-C (RULED, SHA `1a9e4071c`) — zero-code pathway formalized; design
   brief produced.
2. S-3 ruling (Receipt 22) — brief ADOPTED; RV-12 rider (no instance content to
   external models under CLOSED D-T0-14); RV-13..21 deferred to this packet.
3. D-PEC-08 O-A (RULED 2026-07-05, in-session steer; verbatim in
   `_DECISIONS/D-PEC-08_upload_agent_source_tranche_authorization.md`) —
   authorizes preparation/execution of this bounded tranche.

## What v1 implements (scope)

The in-app **import proposal** pathway from the adopted brief, deterministic
and CSV-only:

1. **Propose** — an RBAC'd route accepts a CSV text body (contract declared by
   the caller), hashes it (SHA-256), stores it, and computes a **dry-run**
   `ImportReport` against a savepoint that is rolled back. Proposal lands
   `ready_for_review` (or stays `draft` with the error recorded if the CSV is
   not contract-shaped).
2. **Review** — proposals are first-class records (`import_proposal`, ref
   prefix `IPR-`) with full report detail; a `refresh` act re-runs the dry-run.
3. **Accept** — a human act, hash-bound: the accepter must echo the proposal
   `version` and the source CSV's SHA-256. Stale proposals refuse acceptance.
4. **Apply** — a human act on an `accepted` proposal; executes the real
   `importContract` in the same transaction as the lifecycle change (atomic:
   mid-apply throw rolls back everything). `force` remains a separate explicit
   control, default off, human-only.
5. **Audit** — history entries on every lifecycle step; `audit_event` rows on
   accept and apply.
6. **Prerequisite repair** (brief §"Prerequisite repairs"): RAIL unanchored
   intake idempotency — re-importing a RAIL row that previously landed as an
   unanchored intake item updates it (matched by its `[item_id]` verbatim
   prefix) instead of duplicating it.

The **agent seam** in v1 is deterministic only: the agent (or user) maps files
to §16 contract shape outside the app (FILE_DROP_RUNBOOK v1.1) and the
proposal pathway replaces the direct import for the propose→approve→apply
loop. **No LLM call exists in this tranche**; the RV-12 rider (no instance
content to an external model under CLOSED D-T0-14) is honored trivially.

Out of scope, unchanged from the brief: auto-apply, agent-initiated imports,
`force=true` defaults, non-import write actions, SSO, xlsx parsing, multipart
upload, any new runtime dependency (ADR-002).

## Exact file fence (the only writable paths for this tranche)

| Path | Change |
|---|---|
| `projects/pec/core/src/types.ts` | add `import_proposal` to `RECORD_TYPES` |
| `projects/pec/core/src/permissions.ts` | add `import.propose` / `import.accept` actions + rules |
| `projects/pec/core/test/permissions.test.ts` | pin the new permission rules |
| `projects/pec/server/src/db.ts` | `import_proposal` table + index; add to `CONTROLLED_TABLES` |
| `projects/pec/server/src/repo.ts` | `TABLE`, `REF_PREFIX` (`IPR`), `JSON_COLS` entries |
| `projects/pec/server/src/services/proposals.ts` | NEW — proposal lifecycle service |
| `projects/pec/server/src/import/index.ts` | RAIL unanchored-intake idempotency repair only |
| `projects/pec/server/src/api.ts` | proposal routes + same-origin guard on proposal mutations |
| `projects/pec/server/test/import-proposal.test.ts` | NEW — end-to-end proposal tests |
| `projects/pec/web/src/pages/Admin.tsx` | "Proposed imports" section (upload → review → accept → apply) |

Everything else — including `pec.db`/`-wal`/`-shm`, `backups/**`,
`fixtures/**`, `tools/**`, root manifests, and all other `server/src/**` and
`core/src/**` files — stays closed (F-PEC-1 remains the outer fence; this
packet opens exactly the rows above and nothing else).

## Deferred D-PEC-07 obligations — discharge or carry

- **RV-13 (K-AUTH-2/hash binding, version binding, stale refusal) — discharged.**
  Acceptance requires echoing the proposal `version` (optimistic concurrency)
  and `sha256` equal to the stored source hash; mismatch → 400. v1 has no
  separate mapped CSV (mapping is outside the app; the uploaded CSV IS the
  mapped CSV), so source hash = mapped hash; a future in-app mapper must bind
  the mapped hash separately. Staleness: the dry-run records a project history
  watermark (`MAX(history_entry.id)` excluding `import_proposal` rows); accept
  and apply refuse with 409 `STALE_PROPOSAL` if the project changed since, and
  `refresh` re-runs the dry-run (demoting an accepted proposal back to
  `ready_for_review`, voiding the acceptance). The coordination-level K-AUTH-2
  git-SHA binding is carried by the D-PEC-08 ruling record + PR + receipt.
- **RV-14 (CSV-only v1) — discharged.** Upload is a UTF-8 CSV text body
  (existing `readBody` path, no multipart, no xlsx, no new dependency),
  size-capped at 5 MiB (under the global 25 MiB body cap). Conversion stays
  agent/client-side per FILE_DROP_RUNBOOK v1.1.
- **RV-15 (history vs audit) — discharged.** Chosen: `history_entry` rows
  (record_type `import_proposal`) for every lifecycle step — kinds `created`,
  `proposal_dry_run`, `proposal_accepted`, `proposal_rejected`,
  `proposal_applied` — plus `audit_event` rows for accept
  (`import_proposal_accept`) and apply (`import_proposal_apply`), mirroring the
  config-change audit precedent. Records created by apply get the standard
  `kind='import'` history, unchanged.
- **RV-16 (permission naming) — discharged.** `import.propose` (upload,
  refresh, read proposals, reject-own): `admin`, `pm`, `coordinator`,
  `document_controller`. `import.accept` (accept, reject-any, apply, `force`):
  project `admin` only — parity with the existing `config.manage` direct-import
  gate; acceptance is register-administration work, not an engineering
  judgment, so it is deliberately NOT in the `PERSONAL_JUDGMENTS` set
  (instance-admin break-glass applies, I-6 untouched). Read access to stored
  raw CSVs/previews rides `import.propose` — narrower than membership, so
  viewers and contributors never see raw uploads (RV-19 read-side concern).
- **RV-17 (deterministic contract, preview stability, stale dry-run,
  apply-failure lifecycle) — discharged.** The dry-run report is the full
  `ImportReport` (same shape as direct import; the deterministic result schema
  the profile marks TBD remains TBD at profile level — this packet does not
  publish a schema, it reuses the live shape). Preview stability: the dry-run
  savepoint rollback restores `seq`, so refs assigned at apply match the
  preview unless the project changed in between — exactly the case the
  staleness watermark refuses. Apply failure: lifecycle change and import run
  in ONE transaction; a mid-apply throw rolls back both (no half-applied state,
  no lifecycle corruption); the proposal simply remains `accepted` and the
  error returns to the caller.
- **RV-18 (schedule wording, report completeness) — discharged.** No schedule
  code change is needed (evidence-04 proved the seam as-is); the brief's
  "multi-file schedule support" is satisfied by the documented extractor
  mapping in `IMPORT_TEMPLATES/IMPORT_MAPPING.md`. The proposal UI renders the
  full report including `intakeCreated`.
- **RV-19 (upload store lifecycle) — discharged by design choice.** v1 stores
  the uploaded CSV **in the database** (`import_proposal.source_csv`, capped at
  5 MiB), deliberately deviating from the brief's "outside the DB" sketch: the
  proven backup/restore path is single-file (`VACUUM INTO` + `copyFileSync`),
  and an external store would silently fall outside it — the exact loss mode
  RV-19 flags. Retention/deletion: proposals are controlled records
  (append-only lifecycle, no delete path). MIME/extension policy: text CSV
  only. Project scoping: `project_id` column + project-scoped routes.
  Read-side RBAC: `import.propose`. An external content-addressed store
  remains a future tranche if upload sizes demand it.
- **RV-20 (coordination precedent) — discharged.** Named in this packet's
  header.
- **RV-21 (CSRF posture) — discharged for the new surface.** Proposal
  mutation routes require same-origin when a browser context is detectable:
  if an `Origin` header is present, its host must match the request `Host`,
  else 403 `CROSS_ORIGIN`. (Cookie-less API clients and same-origin fetches
  are unaffected.) Extending this guard to the pre-existing mutation routes is
  a candidate follow-up outside this fence — recorded here, not smuggled in.

## Tests (ride the same PR)

- `core/test/permissions.test.ts`: propose/accept role matrices, viewer
  refusal, instance-admin break-glass.
- `server/test/import-proposal.test.ts`: propose→dry-run leaves data untouched;
  malformed CSV stays `draft` with error recorded; hash/version binding on
  accept (wrong hash 400, wrong version 409); staleness refusal + refresh
  re-arm; accept/apply RBAC (proposer without `import.accept` gets 403); apply
  atomicity and report; RAIL intake re-import idempotency; cross-origin
  refusal; full lifecycle history/audit trail.

## Rollback plan

- The tranche rides one PR on branch `codex/pec-dpec08-upload-agent-tranche`;
  rollback before merge = close the PR; rollback after merge = `git revert` of
  the merge commit (owner act). No data migration is destructive: the new
  table is additive (`CREATE TABLE IF NOT EXISTS`); reverting the code leaves
  any `import_proposal` rows inert in scratch/demo DBs (they gate nothing and
  no other table references them). No existing route, schema column, or
  behavior is modified except the RAIL unanchored-intake duplicate repair,
  whose pre-repair behavior (duplicate intake rows) is strictly worse and is
  itself pinned by a test.
- The live scratch/demo DBs are untouched by this PR (code-only tranche; the
  standing checks run on temp DBs and the committed fixtures).

## Verification plan (workplan step-4 checks)

Profile validator green; repo-wide harness `self-check` exit 0; FULL
practitioner-harness pytest at the final commit SHA; pec belt-and-braces
`npm run typecheck && npm test && npm run build && npm run drill` green;
`coord-check --diff origin/main..HEAD` pass; `git diff --check` pass;
adversarial scope check: `git diff --name-only` ⊆ the fence table above plus
this packet, the D-PEC-08 packet/register ruling records, and the loop
receipt. CI green; owner merges (never self-merge).
