# D-GOV-36 — Managed authentication custody, bootstrap and logout

Status: RULED — APPLIED_UNPUBLISHED. Owner-selected boundaries recorded; no main-observable effect claimed.
Owner: Ryan Tufts
Owner decision date: 2026-09-06 (local MDT)
Accepted source basis: main@2c75eb4bf03436eb305310996044eca0b67d3116
CandidateSHA: TBD
PublicationSHA: TBD
EffectiveSHA: TBD
ID allocation: D-GOV-36 verified next free on application basis main@2c75eb4.

## Recorded owner act and exact referent

> I approve these three recommended dispositions.

The owner act is transcribed in
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-126_RULING_CREDENTIAL_CUSTODY_BOOTSTRAP_AND_LOGOUT_2026-09-06.md`,
SHA256 `4480ad2e70bfcac6487980d9a310ae52720cb472c10467897d97aaf184e55a73`.
The exact selected slate is
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_RUNTIME_CONTRACT_REVIEW_2026-09-06/control/CUSTODY_DECISION_SLATE_v1.md`,
SHA256 `429b2e8305d2e79b1a55f539174cc133e413bbf6c79eb951df77cb0c222b5cc2`.
This records settled choices. Root recording is applied under the explicit owner M2 grant below; publication and effective identities remain pending. No main-observable effect is claimed.

## Narrow later disposition

Owner selected all three dispositions in the pinned App slate, as recorded by D-APP-126. For managed Codex authentication, permit the daemon-owned exact trusted supplier authentication process to persist credentials using explicitly configured built-in OS keyring as a narrow exception to D-GOV-20 ruled architecture items 2–3's exclusive daemon/Electron safeStorage custody formulation. The packaged daemon remains the sole lifecycle and access controller. Authentication for each canonical root is independently acquired in root-private app-owned contexts. No cross-root credential copying, shared authenticated home, ambient credentials, client/tool-worker credential access or plaintext fallback is permitted. Qualification of the exact supplier, backend and process/storage boundaries is required before operational reliance. A custom adapter is justified only by a demonstrated remaining gap.

Permit an account-only nonexecuting bootstrap auth namespace for sign-in before folder selection. It grants neither project/no-folder execution nor folder consent. Bootstrap credentials are not copied to root contexts. Preserve authenticated project-scoped Unix control, no TCP control listener, operational/non-authoritative credential state, local-model residency and every unaffected D-GOV-20 exclusion. Local profile/settings do not constitute client authority or an additional cloud account.

Global account switch/sign-out durably fences every hosted context in the active account generation. Local-model contexts are unaffected and folder disconnect is local to that folder. Retire tool/turn execution first; retain only necessary purpose-limited context for a separately authorized bounded remote-revoke attempt; then retire auth processes and clear local credentials, verifying cleanup. Ungranted, offline or impossible revoke proceeds to local cleanup with remote state unknown. Do not retain credentials indefinitely or claim browser-wide/provider-global revocation. Human-approval assurance remains separate.

This records selected boundaries, not source implementation, live login/provider/credential operations, protected-fixture retries, supplier acceptance, publication, merge, cutover or release authorization. Exact source/configuration/status and bootstrap+A/B briefs follow through Runtime and App scopes.


## Supersession and effect

This later instrument supplies only the stated exception to D-GOV-20 Ruled architecture items 2–3 and the stated bootstrap/logout boundaries. The original D-GOV-20 decision remains immutable. Its retained transcription in PRD_ROOT remains read with actual later amendments, as that section already requires. Runtime ownership migration remains accepted; no Root product activation is restored.

The App and Runtime loops apply affected contract and derivative changes through their owning instruments. Release of dependent work requires this owner act and applicable notices on fetched origin/main, accepted owning contracts and separately authorized execution scope. Root M2 application authorization is recorded below. Validation is recorded in the application run; publication and effective main observability remain pending.

## Exact Root application authorization

Owner Ryan Tufts, 2026-09-06 America/Edmonton, verbatim:

> Yes apply and validate this bounded Root governance change, including its required M2/G4 manifest, coordination records, and App/Runtime notices

This applies the previously reviewed candidate patch SHA256 `a536943ebc8e646094f025e7f13b74413a6ae959abbc010149f11921ff05dcf9` with truthful application metadata, plus the expressly named manifest and coordination records. Application evidence and byte-identical copies of the otherwise unpublished App ruling/slate are in `execution/_Coordination/AgentRuns/ROOT_D126_CUSTODY_APPLICATION_2026-09-06/`. Those copied sources retain their original hashes and authority class; they do not apply App owning instruments. No commit, push, publication, merge or operational reliance is authorized by this grant.
