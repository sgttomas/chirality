# SCA-002 actual-poststate decomposition coverage report

Overall verdict: **BLOCKED** for Gate 5 closure. Mechanical application and structural coverage pass, but the authoritative scope ledger carries current account-control metadata that contradicts the recorded owner approval and completed application. This audit is derivative evidence tied to the accepted upstream snapshot `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_ScopeChange/SCA-002_2026-09-07_ACCOUNT_AUTHORITY/SNAPSHOT_MANIFEST.json`; it does not replace decomposition truth or claim closure, publication or Gate 5 acceptance.

## Exact poststate result

The live canonical hashes are exactly:

- `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md`: `19baaea22ba3a5b2dc465c30f7e8273db7b1833fd4a9bf6c2de0fc6056dcdd9d`
- `Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md`: `413687ca6a857f5464a3205e9f9c4b29ace512c8d2b67dfa095ef3640fab883e`
- `RUNTIME_SCOPE_LEDGER.csv`: `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`

Each is byte-identical to its approved author-v2 postimage. `CANDIDATE.patch` SHA256 is `4be28f9e5929765c8666908e8895ffa2a8d75d2f0df66c133e1b383ee1e94395` and names only these three targets. SCA-002 records Runtime basis `579015fab0c121e702d10c255d2824a86bcad58d`. The published Root D36 file verifies at SHA256 `2697862a31ee856ae923c91af38a5e07f8997115a4bd1baabf083afb069939b1`; Root publication and Runtime sync evidence also match their recorded hashes.

The exact Gate 2–4 grant records owner wording “Approve exact Runtime application,” binds decision subject SHA256 `3be40d62ada16bb7d2588c948904c0a6ec9fb5f83d64c15e6c40dbdaaeffcaf1`, and approves the exact patch. SCA-002 records application executed and Gate 5 pending. It does not claim Gate 5 acceptance.

## Check verdicts

| Check | Verdict | Evidence |
| --- | --- | --- |
| 1 Package forward coverage | PASS | One declared `PKG-02_Runtime_Product`; exact folder exists. |
| 2 Deliverable forward coverage | PASS | Seven declared deliverables; seven exact folders exist. |
| 3 Reverse folder coverage | PASS | No undeclared package or deliverable folder in scope. |
| 4 ID consistency | PASS | Package and all full deliverable slugs match the authoritative register and filesystem. |
| 5 Context fidelity | PASS | Seven contexts match name, package, type, responsible party, description and `ContextEnvelope = M`. |
| 6 Artifact presence | PASS with INFO | All seven live contracts validate as `SOW_V1`; 40 anticipated production outputs remain absent at `INITIALIZED` and are not inferred complete. |
| 7 Objective mapping | PASS | `OBJ-001`, `OBJ-002`, `OBJ-004` and `OBJ-007` each map to all seven existing, non-retired deliverables; no support-count disagreement. |
| 8 Ledger integrity | BLOCKER | Structural mapping passes, but current account-control `DecisionRef` and `Notes` state Runtime acceptance/application are pending after exact approval and application. |
| 9 Derivative package parity | SKIPPED | Variant-owned DOMAIN check; SOFTWARE application/postimage and snapshot checks are covered separately. |
| 9b Package-shape conformance | PASS | Working surface names authoritative registers and labels `TRACE_PREVIEW.csv`/`COVERAGE_PREVIEW.json` as derived; package roles are discoverable. |
| 10 Active snapshot and handoff | PASS | `_LATEST.md` points to exactly SCA-002; all manifest members and pointer hash pass; handoff explicitly surfaces the metadata question and keeps Gate 5/publication/adoption pending. |
| 11 Lifecycle distribution | PASS | Seven `INITIALIZED`; no lifecycle mutation. |

## Conservation

One `SOW-104` IN row, one package, seven qualified deliverables, four objectives, 66 unique qualified inherited requirements, nine held bindings plus the separate R16-B disposition, historical DEL-02-06/09 basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, `root-runtime-1` epoch 1, and all seven full-wire/source gate rows remain. No deliverable `_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv` or `ScopeOfWork.md` differs from basis `579015fab0c121e702d10c255d2824a86bcad58d`.

## Blocking finding

`RUNTIME_SCOPE_LEDGER.csv` is explicitly the authoritative companion register. Its `CandidateState = GATE3_REVIEW_NOT_ACCEPTED` is conserved across the earlier decomposition package and can denote the original SOFTWARE_DECOMP/migration candidate state; this audit does not equate that field automatically with SCA-002 Gate 3. The same row's newly amended `DecisionRef` says “Runtime account-control application pending,” and its `Notes` say synced-basis acceptance, exact applicability rerun and Runtime acceptance/application remain pending. Those statements are current account-control metadata and conflict with `GATE2_4_OWNER_GRANT.md`, SCA-002 `Decision_Log.md` and `Application_Journal.json`.

The active SCA-002 snapshot honestly records and explains the discrepancy, but precedence evidence cannot make contradictory authoritative ledger metadata internally consistent. Gate 5 closure would accept a poststate whose authoritative register misstates the completed act. This is therefore a blocker requiring a separately governed metadata-only amendment; it is not repaired here.

## Required remediation and rerun

Prepare a complete metadata-only `RUNTIME_SCOPE_LEDGER.csv` postimage that preserves the row's scope, package, seven deliverables, four objectives, source lineage and all substantive boundaries while:

1. replacing the account-control `DecisionRef`/`Notes` pending-approval and pending-application claims with exact SCA-002 applied identity and `Gate 5 owner acceptance pending`;
2. explicitly defining `CandidateState` as historical migration/decomposition state, or moving current status to an unambiguous field/value under owner approval;
3. retaining `PROSPECTIVE / NOT EFFECTIVE` until Runtime publication/main identity and Root successor adoption;
4. making no SOW, deliverable, source, lifecycle, wire, supplier, client, release or Git change.

Independently review, separately approve, apply and snapshot that exact postimage, then rerun AUDIT_DECOMP. The resulting concrete Gate 5 subject may include the corrected canonical ledger, exact remediation snapshot and clean poststate audit. Gate 5 acceptance, CHANGE publication, Root successor adoption and later DEL-02-06/09 SOW propagation remain subsequent owner acts.
