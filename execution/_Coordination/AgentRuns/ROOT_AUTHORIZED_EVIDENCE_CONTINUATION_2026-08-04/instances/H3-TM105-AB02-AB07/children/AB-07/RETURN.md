# AB-07 — store/privacy evidence inventory

- Child: `H3-TM105-AB02-AB07/AB-07`
- Posture: evidence only; sealed evidence set only
- Terminal result: `COMPLETED_WITH_UNRESOLVED_POLICY_FACTS`
- Completeness claim: none beyond the 14 declared evidence inputs and the sealed brief

## 1. Input verification

Every declared input matched the SHA-256 fixed in the launch brief. No input
drift was observed.

| Evidence path | Verified SHA-256 | Result |
|---|---|---|
| `execution/_Coordination/AgentRuns/ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04/instances/H2-TM105-AB01-AB09/RETURN.md` | `380e0c22ca554a604c10d30a3ed49c3fdc79e4806910b80369c8eb88ba0e19a1` | MATCH |
| `execution/_Coordination/AgentRuns/ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04/instances/H2-TM105-AB01-AB09/children/AB-09/RETURN.md` | `f43b4dd8c1165a8318d4c4287036cb3faf2d879e0c9cb540329641e9acbe021b` | MATCH |
| `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/OWNER_VENDOR_PLATFORM_FACTS.md` | `fc0dc536f01c39345e6ee195e789fb07ce28f7fd593f9e83dccdcae3ec7c78aa` | MATCH |
| `runtime/packages/contracts/src/events.ts` | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | MATCH |
| `runtime/packages/contracts/src/harness/event-schema.ts` | `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` | MATCH |
| `runtime/packages/contracts/src/harness/transcript-replay.ts` | `05cd1eae2a8c911775b00e8957ff9b4141f2072e6f063eaadec9b3bc62b1b99a` | MATCH |
| `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | MATCH |
| `runtime/packages/core/src/auth-registry.ts` | `28f8bade3372a6b0f1797a0c9623f0ad68f54f4ef2a6dee6638aeaeef20a29fa` | MATCH |
| `runtime/packages/core/src/fs.ts` | `21ed1bb39afa1a0c773f45f547892182af3c18f7a52c4505895e52924ac513b5` | MATCH |
| `runtime/packages/engine-claude/src/index.ts` | `f397ac1a54b4af77d5d131b8fed27308b5d24852d5e856c36136c8d3bdb5d592` | MATCH |
| `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts` | `531f69c42c87d799b2b9aecec4bbfb96e2a1210dcd17135542c3483b48a9c208` | MATCH |
| `runtime/packages/engine-pi-omlx/src/omlx-client.ts` | `2025db32a48dc261bb6d0b753cfa99b99a4ad97a85f795a8930cac8af6b3f306` | MATCH |
| `runtime/tests/session-and-residency.test.ts` | `5d9c1cda16267557ea8ca599109568718fcb7a22b3dcb8f58a67f760fa596b02` | MATCH |
| `runtime/tests/turn-hardening.test.ts` | `e5880870ef7ee94b90ebef4baf72335bf24073ca35b1d829ead05c3be9ee7b2b` | MATCH |

Drift verdict: `NO_DRIFT`.

## 2. Store, delete, and migration path inventory

These are current implementation observations, not approved-store or policy
decisions.

| ID | Path or surface | Current observed operation | Provenance and boundary |
|---|---|---|---|
| ST-01 | `<runtimeDirectory>/projects/<projectId>/sessions/<sessionId>/session.json` | Session creation and update use atomic JSON writes. Creation records session/project identity, project root, timestamps, role/persona/mode, engine selection, status, and optional parent/approval/write-target fields. | `session-store.ts` lines 28-59, 105-115, 390-404; `fs.ts` lines 10-21. `runtimeDirectory` selection, backups, and production deployment topology are outside the sealed set. |
| ST-02 | `<runtimeDirectory>/projects/<projectId>/sessions/<sessionId>/events.jsonl` | Harness events are JSON-serialized and append-written; each append is handle-synced. `appendEvent` generates UUID and timestamp. `persistEvent` skips an event if replay finds the same `eventId`. | `session-store.ts` lines 127-150, 156-207, 406-408; `fs.ts` lines 24-33. No approval of JSONL as a store is implied. |
| ST-03 | `<runtimeDirectory>/projects/<projectId>/sessions/.deleted/<sessionId>.json` | `delete` first resolves the session, recursively removes the central session directory, then atomically writes a deletion marker containing schema, session ID, and deletion timestamp. `list` and `get` consult the marker. | `session-store.ts` lines 62-103, 117-125, 410-413. The marker itself retains identity/time metadata. Crash behavior between removal and marker write is not tested or guaranteed in the sealed set. |
| ST-04 | Project-relative configured legacy session roots: `<legacyRoot>/<sessionId>/session.json` or `<legacyRoot>/<sessionId>.json`, plus optional `<legacyRoot>/<sessionId>/events.jsonl` | `list` reads and normalizes legacy records without migration. `get`, when no central record exists, lazily creates a private temporary central directory, writes normalized v2 session JSON with legacy source path/migration time, byte-copies legacy `events.jsonl` if present, and renames the temporary directory into place. The source is not removed. Root and symlink containment checks are applied. | `session-store.ts` lines 62-103, 223-270, 345-388. H2/AB-09 independently characterizes this as storage migration, not compatibility migration. |
| ST-05 | Legacy source after session deletion | A legacy lookup may migrate first because `delete` calls `get`; deletion then removes the central copy and adds the marker. The declared test asserts the original legacy session file remains byte-identical after migration and after deletion. | `session-store.ts` lines 82-125; `session-and-residency.test.ts` lines 39-75. This is residual-source evidence, not a conclusion about compliant deletion or erasure. |
| ST-06 | `<runtimeDirectory>/auth/clients.json` | Registry records include client ID, SHA-256 token hash, optional project ID, scopes, creation time, and optional revocation time. Issue replaces any prior same-ID registry record; revoke operations timestamp records. Registry writes are atomic JSON writes. | `auth-registry.ts` lines 17-29, 52-68, 136-158, 160-162; `fs.ts` lines 10-21. No retention/removal of old registry versions, backups, or filesystem snapshots is established. |
| ST-07 | `<runtimeDirectory>/auth/tokens/<clientId>.token` | Issuance writes the plaintext bearer token plus newline at mode `0600`. `ensureClient` reads and may reuse this file when it hashes to the active registry record; otherwise it rotates by issuing. Revocation changes the registry but no token-file removal appears in the sealed implementation. | `auth-registry.ts` lines 52-97, 136-158. Secure erasure, backup treatment, and token-file cleanup are `UNKNOWN`. |
| ST-08 | Pi transcript root supplied by `transcriptRootFor(sessionId)` | Pi start passes a session-specific transcript root into an external runtime while disabling built-ins and ambient resources. | `pi-omlx-engine.ts` lines 25-35, 45-51, 80-88. The path construction, transcript bytes, lifecycle, permissions, deletion, encryption, and provider behavior are absent from the sealed set. |
| ST-09 | SDK linkage fields surfaced from a session record | Transcript view may expose engine/Claude/SDK session IDs, SDK transcript path, SDK store key, SDK config directory, setting sources, package versions, and model. | `transcript-replay.ts` lines 46-65, 199-217, 230-353. This proves field handling, not that every field is persisted or that any referenced SDK store meets a policy. |
| ST-10 | Artifact links referenced by tool events | Transcript view may expose absolute/relative artifact path, SHA-256, tool/turn IDs, a retention-policy string, redacted/truncated booleans, and byte length from event metadata. | `transcript-replay.ts` lines 18-28, 136-153, 296-316. The actual artifact writer/store/delete path is not in the sealed set. |
| ST-11 | oMLX loopback control endpoint | Model status/load/unload calls go only to literal loopback HTTP, use a bearer credential, reject redirects, and enforce a timeout. This is a control surface, not evidence of model/transcript persistence or deletion. | `omlx-client.ts` lines 8-30, 45-120. Vendor retention, logs, credential handling, and model-data lifecycle are `UNKNOWN`. |
| ST-12 | Generic `removeIfExists` helper | A force-removal helper exists. | `fs.ts` lines 91-93. No sealed caller links it to a TM105 evidence/content store, so it proves no store deletion behavior. |

There is no sealed evidence of database, cloud-object, backup, telemetry,
crash-dump, swap, cache, log-aggregation, or remote-provider evidence-store
paths. Absence from this sealed set is not proof those paths do not exist.

## 3. Content and metadata class inventory

The classes below describe fields the sealed code can carry. They are not a
protected-data taxonomy, sensitivity classification, or permission ruling.

### 3.1 Content-bearing classes

| Class | Current carrier/evidence | Qualification |
|---|---|---|
| Free-form event payload | `HarnessEvent.data` is `Record<string, unknown>`; `RuntimeEvent.data` is generic. | `event-schema.ts` lines 52-61; `events.ts` lines 17-37. Content is structurally unbounded by these types. |
| Conversation text | Replay reads message `text` or `message`, concatenates assistant `message.delta` text when no completed assistant message exists, and returns it as transcript items. | `transcript-replay.ts` lines 239-294. No minimization or redaction transform is evidenced. |
| Tool result and artifact description | Replay reads tool names, summaries, result content counts/types/byte length/output-persisted indication, and artifact metadata. | `transcript-replay.ts` lines 136-180, 296-316. Actual tool output bytes may be referenced rather than present; exact behavior depends on event data not bounded here. |
| Error/terminal narrative | Replay reads `error`, arrays of errors, stop reason, terminal reason, or subtype. | `transcript-replay.ts` lines 182-197, 318-333. These strings could contain user/provider content; no classification is established. |
| Legacy record content | Normalization spreads the raw legacy record and then overwrites/adds normalized v2 fields. Legacy event bytes are copied as a whole. | `session-store.ts` lines 255-264, 272-343. Unknown legacy fields can therefore be retained in the normalized record unless overwritten. |
| Credentials | Auth token plaintext is written to a token file; provider credentials are fetched through a `ProviderCredentialPort` and passed to the Claude/Pi runtime or oMLX Authorization header. | `auth-registry.ts` lines 52-74; `engine-claude/index.ts` lines 37-55; `pi-omlx-engine.ts` lines 53-88; `omlx-client.ts` lines 72-92. Provider credential storage behind the port is absent. |

### 3.2 Metadata-bearing classes

| Class | Examples established by sealed code |
|---|---|
| Identity and linkage | Project, session, turn, event, parent event/session, client, engine session, Claude session, SDK session, tool, adapter, provider, and model identifiers. |
| Time/order | Session creation/update, event timestamp, client creation/revocation, deletion/migration time; runtime event `sequence`; JSONL physical line order. |
| Runtime/configuration | Project root, persona, mode, agent type/role, engine selection, allowed write targets, approval reference, scopes/project binding, SDK config path and setting sources, package names/versions, residency epoch. |
| Lifecycle/status | Session status; event type; transcript item status; terminal status; legacy migration marker; deletion marker; token revocation marker. |
| Artifact/store locator | Artifact absolute/relative paths, SDK transcript path/store key, legacy source path, transcript root supplied to Pi. |
| Integrity/size indicators | Artifact SHA-256 and byte length; result byte length/content counts; malformed-line count and per-event-type counts. |
| Policy-shaped labels without demonstrated enforcement | `retentionPolicy`, `redacted`, and `truncated` artifact metadata fields. |

Protected-data classes, data subjects, data controller/processor roles,
sensitivity tiers, purpose limitation, access populations, and legally
regulated categories are all `UNKNOWN`.

## 4. Evidence/unknown matrix

| Topic | Engineering evidence in the sealed set | Result / unknown boundary |
|---|---|---|
| Persistent tamper detection | Session JSON uses atomic write/rename; event appends are synced. Artifact metadata can carry SHA-256. Auth tokens are compared by SHA-256 hash. | These are write-durability, referential-integrity, or authentication mechanics, not an independently anchored evidence-store tamper detector. No MAC/signature, authenticated event chain, trusted timestamp, append-only enforcement, external anchor, or verification of artifact bytes is evidenced. Persistent-tamper detection: `UNKNOWN`/not demonstrated. |
| Malformed/truncated JSONL | Replay splits by newline; parse failure or wrong schema/session increments `malformedLineCount` and omits the line from returned events. | Detection/counting of malformed units is implemented. Byte-preserving quarantine, distinction between truncation and other malformation, recovery, and alert/escalation are not implemented in this surface. AB-09 records a conflict with accepted DEL byte-preserving quarantine semantics; no resolution is made here. |
| Semantic truncation | Artifact metadata may state `truncated` and byte length. | The flag is merely read from event data. No truncation algorithm, cap, provenance, original-byte retention, loss measurement, or enforcement is evidenced. Product acceptance of truncation/data loss is expressly absent in `OWNER_VENDOR_PLATFORM_FACTS.md`. |
| Reorder | Runtime events have a numeric `sequence`; stored harness events do not. Replay returns valid harness events in JSONL line order and derives the last recognized terminal encountered. `persistEvent` de-duplicates only by existing event ID. | No monotonic sequence check, timestamp-order check, parent-order validation, duplicate-ID payload conflict check, reorder detection, or canonical ordering is evidenced for the stored harness stream. Reorder behavior under tampering/concurrency is untested. |
| Cross-session/turn event injection | Declared turn-hardening tests assert coordinator rejection of an engine event for another session and no persistence into that other session; boot validation similarly rejects a foreign-session event before persisting boot events/identity. | Tested at the coordinator/service paths represented by those tests, not as a complete direct-store or all-route authorization proof. SessionStore `persistEvent` itself checks schema and resolves `event.sessionId`, but its signature separately receives `projectId`; it does not compare against an independently supplied active turn in the sealed source. |
| Filesystem access control | Store directories are chmod `0700`; atomic JSON, JSONL, legacy copied events, and token files are chmod/mode `0600`. Safe identifiers and legacy-root canonical containment checks are present. | Owner/process identity, ACLs, group policy, sandbox reachability, backup-reader population, and enforcement on all referenced artifact/SDK/provider paths are `UNKNOWN`. Mode bits do not establish approved access roles. |
| Runtime API access control | Bearer tokens, timing-safe hash comparison, required scopes, optional project binding, and revocation timestamps are implemented. Project/session paths also call `requireAuthorized`, whose implementation is outside this sealed set. | Exact grant issuer/policy/evaluator/trust anchors, role-to-scope mapping, intended principals, audit, expiry, audience/nonce, and route completeness are `UNKNOWN`. H2 additionally records that `ensureClient` can reuse an existing token without comparing newly requested scopes/project to the stored record. |
| Token/credential custody | Runtime client token plaintext is stored in a `0600` file; registry holds its SHA-256 hash. Provider credentials are abstracted behind a port. | Hashing is not encryption. Keychain/HSM/secret-store choice, encryption at rest, rotation/expiry, backup treatment, memory lifetime, deletion, and responsible custodian are `UNKNOWN`. Revocation does not remove the plaintext token file in the sealed source. |
| Encryption in transit | oMLX endpoint is syntactically restricted to literal loopback HTTP and redirects are rejected; bearer auth is sent. | No TLS is used on this loopback control path. OS/process isolation of loopback traffic and all other provider channel guarantees are `UNKNOWN`; no acceptability conclusion follows. |
| Encryption at rest | No sealed session/event/auth/artifact/SDK source demonstrates encryption at rest or an encryption key. | Encryption-at-rest guarantee and key custody: `UNKNOWN`. File permissions are not encryption. |
| Redaction reversibility | Artifact metadata can carry `redacted: boolean`; transcript replay returns that flag. | No redaction transform, target fields, replacement method, source retention, irreversible destruction, test vector, or re-identification analysis is present. Whether redaction occurs, is correct, or is reversible is `UNKNOWN`. |
| Deletion residuals | Central session directory removal plus tombstone is implemented; declared legacy test establishes the original legacy session source remains after deletion. Auth revocation leaves token-file deletion unaddressed. | Complete erasure is not established. Backups, artifacts, SDK transcripts, provider copies, logs, caches, tombstones, token files, and legacy bytes are unenumerated or retained. No policy conclusion is authorized. |
| Migration integrity | Migration uses a private temporary directory, atomic JSON, byte-copy of legacy events, then rename; source is preserved. A declared test checks legacy session source byte identity. | No hash comparison of copied event bytes, collision/conflict policy, crash/fault matrix, malformed legacy handling test, complete content census, or privacy reclassification is evidenced. `get` mutates by migration, conflicting with the AB-09-described DEL recovery-mode non-mutating diagnostic requirement. |

## 5. Testable observed behaviors versus absent tests

No product tests were run in this child. The following are assertions present
in the two sealed test files; they are test-source evidence, not a fresh test
receipt.

### 5.1 Behaviors asserted by sealed tests

1. A legacy session is lazily copied to the central store, migration metadata
   points to the canonical legacy source, and the legacy session source remains
   byte-identical after migration.
2. Deleting that migrated session makes subsequent `get` return
   `SESSION_NOT_FOUND`, while the legacy session source remains byte-identical.
3. An adapter event for another session is rejected by the turn coordinator
   and does not appear in the other session's replay.
4. A nonzero engine exit without terminal success becomes failed evidence and
   a failed session, never a completed one.
5. An event emitted after process exit is rejected and the specific late event
   is not persisted; a failed terminal is present.
6. Engine-stream termination without `process:exit` fails closed.
7. Adapter-forged tool completion does not satisfy the required in-process
   tool receipt; the session fails.
8. Boot-stream validation rejects a foreign-session event before persisting
   engine events or engine identity; boot events after process exit are also
   rejected.

### 5.2 Material behaviors with no sealed test coverage

- deliberate byte tamper, single-line edit, valid-but-forged JSON, partial
  final write, arbitrary truncation, reorder, duplicate event ID with changed
  payload, timestamp rollback, parent-link inconsistency, concurrent append,
  and crash/fault behavior at each write/delete/migration boundary;
- validation of artifact SHA-256 against artifact bytes, preservation of
  malformed raw bytes, quarantine, reconciliation, external anchoring, and
  tamper alerting;
- filesystem ownership/ACL behavior, cross-user/process access, symlink/hardlink
  attacks outside the tested legacy-root containment path, backup/snapshot
  readers, and permission inheritance on referenced artifact/SDK paths;
- bearer scope/project enforcement tests, revoke/rotation/token-file cleanup,
  the `ensureClient` scope/project reuse seam, authorization auditability, and
  direct-entry/route completeness;
- encryption at rest/in transit, key generation/rotation/custody/destruction,
  credential-store behavior, secure deletion, and post-delete forensic residue;
- artifact retention/truncation/redaction enforcement, redaction correctness or
  reversibility, subject/tenant segregation, and provider/SDK transcript
  lifecycle;
- legacy event-byte equality after copying, migration collision/conflict,
  malformed legacy inputs, rollback, cleanup after failure, and deletion across
  central/legacy/artifact/SDK/provider replicas.

## 6. Policy, legal, product, and privacy facts

The only sealed owner-fact carrier is explicitly a request inventory, not a
decision form. Therefore the following remain `UNKNOWN`:

| Fact domain | Status | Reason / owning evidence needed |
|---|---|---|
| Approved stores and prohibited stores | `UNKNOWN` | Accountable owner/product ruling plus complete deployment/store topology. |
| Protected-data classes and sensitivity | `UNKNOWN` | Accountable owner and attributable privacy/legal classification. Code field shapes cannot supply it. |
| Authorized access roles/populations | `UNKNOWN` | Owner policy, issuer/evaluator/trust-anchor facts, route census, and deployment identity evidence. |
| Purpose, minimization, and product acceptability | `UNKNOWN` | Product/privacy owner facts; no inference from existing persistence. |
| Retention duration or trigger | `UNKNOWN` | Accountable owner plus applicable legal/privacy obligations and store-specific implementation evidence. The `retentionPolicy` string field is not policy authority. |
| Deletion deadline, scope, or erasure standard | `UNKNOWN` | Owner/legal/privacy facts and replica/residual/backup/provider evidence. Current `delete` behavior is not an accepted deletion policy. |
| Legal hold | `UNKNOWN` | Attributable legal rule, hold issuer/workflow, precedence over ordinary deletion, affected-store census, and release/audit evidence. |
| Privacy rights/requests | `UNKNOWN` | Applicable jurisdiction/role/data-subject facts and approved access/correction/export/deletion workflow. |
| Incident response/breach obligations | `UNKNOWN` | Applicable legal/contract facts and owner-approved detection, evidence preservation, notification, and response workflow. |
| E-discovery | `UNKNOWN` | Legal owner requirements for preservation, collection, authenticity, chain of custody, review, export, and disposition. |
| Cross-border/provider processing | `UNKNOWN` | Deployment/provider topology and attributable vendor/legal facts. |
| Encryption and key-custody requirement | `UNKNOWN` | Owner security policy, platform/vendor guarantees, exact key/store topology, rotation and recovery requirements. |
| Accepted truncation/data-loss posture | `UNKNOWN` | Expressly listed as an absent owner fact; optional metadata cannot decide it. |

No privacy, security, contractual, regulatory, records-management, litigation,
or product-acceptability conclusion is made.

## 7. Conflicts, non-coverage, and separately owned evidence actions

| ID | Conflict or non-coverage | Treatment / separately owned evidence action |
|---|---|---|
| CN-07-01 | Session deletion removes the central session directory but preserves a tombstone; the declared legacy case also preserves original source bytes. | Root storage owner must produce a complete replica/residual census and fault-tested delete behavior. Accountable product/legal/privacy owners must separately define any deletion obligation. |
| CN-07-02 | The delete sequence removes central bytes before writing the tombstone, while `get` can migrate an unmarked legacy source. No crash-between-steps test is present. | Root engineering must test the interruption window and establish the resulting state machine; no behavior is inferred beyond code order. |
| CN-07-03 | `get` performs lazy migration, whereas AB-09 records accepted DEL recovery semantics requiring retained diagnostics not to mutate while recovery is required. | Root recovery/storage owners must reconcile direct-entry gating and migration sequencing. This child selects no implementation. |
| CN-07-04 | Malformed JSONL units are counted and omitted from replay, whereas AB-09 records accepted DEL requirements for byte-preserving quarantine and readiness hold. | Root storage/recovery tranche and adversarial evidence are required. No malformed byte is repaired or assigned a winner here. |
| CN-07-05 | Runtime event contracts have `sequence`; persisted harness event contracts do not, and current replay uses file order. | Root event/storage owner must define and test ordering, duplicate, parentage, and tamper semantics. Vendor ordering/authenticity facts are separately required if relied upon. |
| CN-07-06 | `events.ts` omits `turn.cancelled`, while harness schema/replay recognizes it; AB-09 already identifies this terminal-contract conflict. | Root contracts owner must reconcile the event surfaces. No union is selected as authoritative for TM105. |
| CN-07-07 | Artifact fields named `retentionPolicy`, `redacted`, and `truncated` are accepted as metadata without evidenced enforcement. | Product/privacy/legal owners supply policy facts; Root/artifact owners supply exact transformations, lifecycle paths, validation, and adversarial tests. Field names must not be treated as fulfilled policy. |
| CN-07-08 | File modes and runtime scopes are concrete controls, but approved access roles, issuer/policy trust, expiry/audience/nonce, route completeness, and deployment identities are absent. | Security/product owner facts plus Root end-to-end authorization census/tests are required. Preserve H2's `ensureClient` scope/project reuse finding. |
| CN-07-09 | Plaintext runtime token material is stored at `0600`; provider credential custody is abstract; no at-rest encryption/key evidence appears. | Security/platform owners must supply encryption/key-custody requirements and implementation evidence. Vendor/provider guarantees require attributable primary evidence. |
| CN-07-10 | Revocation timestamps the auth registry but no token-file deletion occurs in the sealed implementation. | Root auth owner must establish residual token behavior, cleanup/rotation semantics, and tests; security/product owners separately decide requirements. |
| CN-07-11 | Pi receives a transcript root and transcript view can expose SDK/artifact paths, but their writers, bytes, access controls, retention, deletion, encryption, and provider copies are not in scope. | Root/engine/artifact owners must enumerate these paths; vendor owners must obtain attributable SDK/provider facts; legal/privacy/product owners rule only after that evidence. |
| CN-07-12 | Current tests cover selected coordinator validation and one legacy migration/deletion case, not adversarial store/privacy behavior. | Root QA/security owners must execute a bounded matrix for tamper, truncation, reorder, concurrency, fault injection, access, encryption, redaction, deletion, migration, backup, and provider residuals after authorization. |
| CN-07-13 | The sealed set contains no complete deployment topology or all-store census. | Accountable owner/platform evidence must define intended contexts; Root engineering must perform a declared exhaustive route/store/direct-entry census. Absence here is not nonexistence. |
| CN-07-14 | Legal hold, privacy rights, incident, and e-discovery facts are wholly absent. | Accountable legal/privacy/records/security owners must provide attributable requirements and approved workflows. Engineering cannot infer them. |

## 8. Authority and holds

This return is derivative preparation-only evidence. It chooses no approved
store, retention/deletion duration, access role, redaction policy, encryption
scheme, key custodian, protected-data class, privacy/legal interpretation,
backend, migration design, or contract candidate. Every unsupported policy
fact remains `UNKNOWN`.

All semantic, implementation, client-acceptance, lifecycle, release, reliance,
publication, Git, PR, register, receipt, notice, no-TBD-successor, and byte-gate
holds remain intact. No evidence store, credential, remote provider, product
test, source, contract, client, register, receipt, notice, Git state, or PR was
mutated by this child. No lifecycle, release, publication, reliance, foreign-
loop, or authority effect is created.
