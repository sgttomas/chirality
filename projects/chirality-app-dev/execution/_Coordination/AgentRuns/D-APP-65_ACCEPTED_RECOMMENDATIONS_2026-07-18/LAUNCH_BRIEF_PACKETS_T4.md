# Sealed Launch Brief — N8 Packet Author (T4, D-APP-66 + D-APP-67)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Authority:** D-APP-65 disposition 5 (owner authorized these two decision packets, to be ruled in-session). The packets go to the owner for ruling — author them AWAITING_RULING; do NOT record any ruling, and do not write any code.
- **Posture:** fresh context; bounded file tools; read the live code before designing options; no delegation; no Bash except read-only inspection (`grep`, `ls`) if file tools are insufficient.

## Write scope (exactly these)

1. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-66_PACKET_CONTENT_SHA_REVALIDATION_2026-07-18.md` (new)
2. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-67_PACKET_SECRET_REGISTRY_REDACTION_TAXONOMY_2026-07-18.md` (new)
3. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` (append exactly two rows, State `AWAITING_RULING`, Ruling record cell `—` pending)
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_N8_PACKETS.md` (your return)

## Packet shape (both)

D-APP-63 compact shape: H1 with ID + one-line scope; metadata block (**Status:** AWAITING_RULING — authored under D-APP-65 disposition 5, owner ruling to be transcribed on receipt; **Date prepared:** 2026-07-18; **Prepared by:** N8 packet-author child under this sealed brief; prep is agent work, the ruling is the owner's — K-AUTH-1); sections `## Context`, `## Options`, `## Recommended option and rationale`, `## Human Ruling and Disposition` (placeholder: "AWAITING RULING — to be transcribed verbatim on receipt"), `## On-ruling mechanics (planned)`.

Ground every code claim in the live tree — read the files first; cite paths + line numbers. Name concrete test additions. State explicitly in each packet: no code lands unless and until the owner rules for it; a declined or deferred ruling leaves the packet AWAITING_RULING with the deliverable's gate intact.

## D-APP-66 — Content-change SHA revalidation (DEL-07-04)

Context to bind: DEL-07-04 `_STATUS.md` line 10 deferred item ("needs its own decision packet before code"; D-APP-53 Option C; D-APP-56 R4-P46 reaffirmed); assessment anchor `Assessment_INSP-03_DEL-07-04.md` ~line 47 ("Approval SHA binding is persisted but not automatically revalidated against content changes", anchored at `frontend/src/lib/lifecycle/status-writer.ts:125-160`). Read `frontend/src/lib/lifecycle/transition.ts` (approval-SHA parsing/validation — presence + format `/^[0-9a-f]{7,64}$/i` only; error codes `APPROVAL_SHA_REQUIRED`, `INVALID_APPROVAL_SHA`) and `status-writer.ts` before writing options. Determine from the code and kit docs what the approval SHA actually references (e.g. a git commit SHA of the approved state) and design revalidation semantics that are honest about what can be checked deterministically at transition time.

Options to present (refine against the code; keep three):
- **A (draft-recommended):** transition-time revalidation — when a human-gated transition supplies an approval SHA, deterministically verify it against the current governed content state before the status write; new typed error code (e.g. `APPROVAL_SHA_STALE`); enforcement wired in `transition.ts` before `writeStatusDocument`; tests in `frontend/src/__tests__/lib/lifecycle-status.test.ts` covering match, stale, and malformed cases. Spell out precisely what "verify against current content state" means given what the SHA references — if full deterministic verification is not possible from inside the runtime (e.g. requires git), present the honest bounded variant (e.g. verify the referenced object exists and the governed file's current content hash matches a recorded binding) and say what remains unverifiable.
- **B:** consumption-time warning only (no transition blocking).
- **C:** keep as governance checklist; no code (status quo).

## D-APP-67 — Arbitrary-secret-registry redaction taxonomy (DEL-05-03)

Context to bind: DEL-05-03 `_STATUS.md` line 10 deferred item; assessment rows DEL-05-03-R12 PARTIAL and "Arbitrary configured secret taxonomy is not accepted" (anchors `frontend/src/lib/harness/run-logger.ts:64-77`/`64-109`); ORN-11 evidence explicitly excludes the broader registry; scanner prior art `frontend/scripts/scan-secret-evidence.mjs` (DEL-05-03 UNMAPPED-2 — scans broader shapes than the runtime contract); the 2026-07-18 operational evidence: secret-hygiene gates tripped four consecutive verifier returns over the fixture-marker/real-credential boundary. Read `run-logger.ts` (value-based variant expansion: raw, URL-encoded x2, lowercase percent, `+`-encoding; longest-first; `[REDACTED_API_KEY]` token) and the scanner's marker list before writing options.

Options to present (three):
- **A (draft-recommended):** adopt a configured-secret registry taxonomy — (i) runtime: broaden the run-logger helper to accept registered named secrets beyond the three API-key sources, same variant-expansion and longest-first discipline, replacement tokens `[REDACTED_API_KEY]` (key-class) / `[REDACTED_SECRET]` (other registered classes); registry fed only from explicit configuration (no pattern-guessing of arbitrary values); (ii) committed-file surface: ratify the scanner's fixture-marker convention as the governed taxonomy for synthetic tokens in committed text (a secret-shaped string is allowed only if fixture-marked; verifier returns quote tokens only in fixture-marked form); (iii) tests extending `run-logger.test.ts` + `redaction-path-matrix.test.ts`. Name the exact registry mechanism you propose after reading the code (e.g. env-var list / settings surface) and its schema.
- **B:** ratify the taxonomy document (committed-file rules + verifier-quoting rule) without broadening the runtime helper (helper stays API-key-specific).
- **C:** defer again (status quo).

## Register rows

Append two 6-column rows after D-APP-65: ID; Decision one-liner; Blocks (the respective deliverable's gated item); State `AWAITING_RULING`; Packet path; Ruling record `— (awaiting owner ruling)`.

## Return format

`RETURN_N8_PACKETS.md`: for each packet — the options as one-paragraph summaries suitable for presenting to the owner verbatim, your draft-recommended option, and the key design facts you pinned from code reading (with citations). Deviations (none expected).
