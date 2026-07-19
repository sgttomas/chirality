# D-APP-67 — Arbitrary-Secret-Registry Redaction Taxonomy (DEL-05-03 runtime helper + committed-file secret taxonomy)

**Status:** RULED — Option B (taxonomy document only), owner ruling
2026-07-19 transcribed in §Human Ruling

**Date prepared:** 2026-07-18

**Prepared by:** N8 packet-author child under sealed brief
`execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/LAUNCH_BRIEF_PACKETS_T4.md`.
Packet preparation is agent work; the ruling is the owner's (K-AUTH-1).

## Context

**The gated item.** DEL-05-03 `_STATUS.md` line 10 carries the deferred item:
"Define and land the arbitrary-secret-registry redaction taxonomy (needs its
own decision packet before code)" — gated since D-APP-53 ruled Option A only
(2026-07-10) and reaffirmed open/unselectable by D-APP-56 R4-P46 (2026-07-12;
`_STATUS.md` line 26). D-APP-65 disposition 5 authorized this packet; it does
not pre-authorize any code.

**The assessed gap.** `Assessment_INSP-03_DEL-05-03.md`: R12 PARTIAL —
"configured-secret schema beyond API-key sources remains TBD" (line 34,
anchored at `frontend/src/lib/harness/run-logger.ts:64-109`); Gap Inventory
Medium — "Arbitrary configured secret taxonomy is not accepted" (line 42,
anchored at `run-logger.ts:64-77`). The ORN-11 evidence matrix explicitly
excludes the broader registry: "An arbitrary configured-secret registry
remains outside ORN-11" and "is not inferred or added by ORN-11"
(`Evidence_ORN-11_Runtime_Redaction_Path_Matrix.md` lines 11, 30).

**What the live runtime helper actually does** (read 2026-07-18, live tree):

- `readConfiguredApiKeyVariants` (`run-logger.ts:64-77`) draws from exactly
  three sources: `getUiApiKey()` (Electron process-global
  `__CHIRALITY_UI_API_KEY__`, `frontend/src/lib/harness/api-key-store.ts:12,
  24-27`), `ANTHROPIC_API_KEY`, and `CHIRALITY_ANTHROPIC_API_KEY`.
- Each value is expanded value-based (no pattern-guessing): raw, plus two
  rounds of URL-encoding with lowercase-percent and `+`-for-`%20` variants
  (`run-logger.ts:19-62`), sorted **longest-first** (`run-logger.ts:76`), and
  replaced with the single token `[REDACTED_API_KEY]` (`run-logger.ts:90`);
  `redactJsonLike` recurses structures (`run-logger.ts:93-109`).
- Live unregistered secret classes exist today: the D-APP-52 transport
  credentials `CHIRALITY_PEC_AGENT_EMAIL` / `CHIRALITY_PEC_AGENT_PASSWORD`
  are read in `frontend/src/lib/harness/mcp/pec-bridge-client.ts:184,296`.
  They are kept out of returned envelopes/events by construction (the
  allowlisted envelope surface; D-55 run row DEL-05-03 UNMAPPED-1), but the
  run-logger registry would not redact them if they ever reached an event or
  error string.

**The committed-file prior art.** The whole-product scanner
`frontend/scripts/scan-secret-evidence.mjs` (D-55 run row DEL-05-03
UNMAPPED-2: implemented, unmapped to any requirement) already scans broader
shapes than the runtime contract: exact environment-secret values with
raw + URL-encoded variants and a ≥8-char usability floor (lines 180-204),
the Anthropic key shape `/sk-ant-[A-Za-z0-9._=/-]{8,}/` (line 50), and
URL-embedded credentials (line 51). Its fixture convention: a shape-match is
`allowed_fixture` iff the token contains one of 12 markers (`ambient`,
`alias`, `alt-key`, `bridge`, `dummy`, `example`, `fake`, `fixture`,
`placeholder`, `redaction`, `test`, `ui-key`; lines 52-65) or lives under a
test path (lines 141-148) — while **exact live environment values are
`blocked` unconditionally, markers never sanctify a real value**
(lines 296-317). Findings persist hash-only, never raw (lines 166-178).

**Operational evidence of cost (2026-07-18).** Secret-hygiene gates tripped
four consecutive verifier returns this session, entirely over the
fixture-marker / real-credential boundary — recorded in the accepted basis of
D-APP-65 (`D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md` §2,
recommendation 4). The boundary works, but it is undocumented convention, not
ratified taxonomy, so every verifier re-derives it.

## Options

### Option A — Adopt the configured-secret registry taxonomy: runtime registry + ratified committed-file rules + tests (draft-recommended)

**(i) Runtime registry.** Broaden the run-logger helper from three hardwired
API-key sources to a **registered named-secret** set, fed only from explicit
configuration — never from pattern-guessing of arbitrary values:

- **Mechanism:** a new env var `CHIRALITY_REDACTION_SECRET_ENV_NAMES` — a
  comma-separated list of entries `ENV_NAME[:class]`, where each named
  environment variable's **value** is registered as a secret; `class` is
  `api-key` or `secret` (default `secret`). Built-in always-on entries: the
  three existing API-key sources (class `api-key`;
  preserving `run-logger.ts:64-77` behavior byte-for-byte) and
  `CHIRALITY_PEC_AGENT_PASSWORD` (class `secret`). Unset/empty named vars are
  skipped; values shorter than 8 chars are refused (mirrors the scanner's
  usability floor, `scan-secret-evidence.mjs:187`), preventing log-shredding
  registrations.
- **Semantics:** identical variant-expansion discipline (raw, two rounds of
  URL-encoding, lowercase-percent, `+`-encoding; `run-logger.ts:19-62`) and
  one longest-first replacement pool across all classes (`run-logger.ts:76`
  discipline) — the matched variant's class selects the token:
  `[REDACTED_API_KEY]` for key-class, **`[REDACTED_SECRET]`** for other
  registered classes. `redactJsonLike` recursion unchanged.
- Registered names and classes may appear in logs; registered **values**
  never do, in any variant.

**(ii) Committed-file surface.** Ratify the scanner's fixture-marker
convention as the governed taxonomy for secret-shaped strings in committed
and generated text:

- A secret-shaped string (key-shape or URL-credential shape) is allowed in
  committed/generated text **only if fixture-marked** (marker substring from
  the 12-marker list, or a test-path location; `scan-secret-evidence.mjs:
  52-65,141-148`).
- Exact configured/environment secret values are blocked regardless of
  markers (`scan-secret-evidence.mjs:296-317`) — **markers sanctify shapes,
  never values**.
- Verifier returns and run records quote secret-shaped tokens only in
  fixture-marked form. This is the rule whose absence tripped four verifier
  returns on 2026-07-18; ratifying it makes the gate deterministic for every
  future verifier.
- The marker list becomes governed: additions/removals are recorded changes
  to the scanner list, not ad-hoc judgment.

**(iii) Tests.** Extend
`frontend/src/__tests__/lib/run-logger.test.ts` (currently three cases,
lines 17-77): registered non-key secret redacts to `[REDACTED_SECRET]`
across raw and encoded variants; class-token selection when key-class and
secret-class values co-occur; longest-first across classes; sub-8-char
registration refused; unset named vars skipped. Extend
`frontend/src/__tests__/lib/redaction-path-matrix.test.ts` (currently two
cases, lines 22-86): a registered fixture-marked pec-password-shaped secret
flowing through hook diagnostics never appears raw in persistence, replay, or
browser-bridge output. All fixture values in tests are themselves
fixture-marked per (ii).

- **Risks:** registry misconfiguration (mitigated by explicit-names-only +
  length floor); token-vocabulary growth (`[REDACTED_SECRET]`) touches
  downstream string assertions.
- **Validation:** frontend typecheck + Vitest + `npm run proof:secret-scan`.
- **Affected files:** `frontend/src/lib/harness/run-logger.ts`,
  `frontend/src/__tests__/lib/run-logger.test.ts`,
  `frontend/src/__tests__/lib/redaction-path-matrix.test.ts`; taxonomy
  ratification text in the deliverable's evidence surface (ORN-11 successor
  note) — scanner code itself needs no change for (ii).

### Option B — Ratify the taxonomy document only; helper stays API-key-specific

Adopt (ii) — the committed-file rules and the verifier-quoting rule — as
governed taxonomy, without broadening the runtime helper
(`run-logger.ts:64-77` unchanged; no `[REDACTED_SECRET]` token). This
resolves the operational friction (the four verifier trips were all
committed-text/quoting boundary cases, not runtime redaction failures) at
zero runtime risk. The R12/Gap "arbitrary configured secret" runtime question
stays open: unregistered live classes like `CHIRALITY_PEC_AGENT_PASSWORD`
remain protected only by construction (envelope allowlists), not by the
redaction registry.

### Option C — Defer again (status quo)

The deferred item stays gated in `_STATUS.md` line 10. The boundary that
tripped four verifier returns remains unwritten convention, re-derived per
verifier; the runtime registry question remains TBD in the assessment record.

## Recommended option and rationale

**Option A.** The taxonomy question and the registry question are one
decision surface: the scanner already enforces a de-facto taxonomy
(UNMAPPED-2 — implemented but unowned), the runtime already has a live
non-key secret class in circulation (`CHIRALITY_PEC_AGENT_PASSWORD`), and the
2026-07-18 session paid a four-trip cost for the taxonomy being unratified.
Option A closes all three with a small code+test surface (the D-APP-65
accepted basis, §2 recommendation 4, graded it exactly that), keeps the
registry explicit-configuration-only (no pattern-guessing of values — the
same discipline that has kept the current helper deterministic), and
preserves `[REDACTED_API_KEY]` behavior for every existing consumer.

**No code lands unless and until the owner rules for it.** A declined or
deferred ruling leaves this packet AWAITING_RULING and DEL-05-03's
`_STATUS.md` line 10 gate intact.

## Human Ruling and Disposition

Transcription note: the owner's ruling below is chat evidence (the session's
structured-question interface), transcribed verbatim; this packet is one of
its two governed homes (the other is the D-APP-66 packet — the two rulings
were delivered as one block and the full block is transcribed in each, with
the same canonical hash). The prompts and option descriptions are
agent-drafted; the selections are the owner's acts (K-AUTH-1).

<!-- BEGIN OWNER RULING VERBATIM -->
On 2026-07-19, the agent presented both AWAITING_RULING packets' options to the owner through the session's structured-question interface; the prompts and option descriptions are agent-drafted, the selections are the owner's acts:

Question 1 (D-APP-66): "D-APP-66 (DEL-07-04 content-change SHA revalidation): how should the approval-SHA surface treat content changes after a human approval? Today validation is presence + hex-format only; nothing detects that governed content changed after the approval was recorded."
Owner selection: "C: Status quo" — keep content-change voiding as a governance checklist item; no code. The gap survives to issuance, where the owner is at every gate anyway (F-APP-4).

Question 2 (D-APP-67): "D-APP-67 (DEL-05-03 secret-registry redaction taxonomy): how far should the redaction contract broaden beyond configured API keys? Context: the pec agent password is currently protected only by envelope construction, and the fixture-marker boundary tripped four verifier returns on 2026-07-18 because it was unwritten convention."
Owner selection: "B: Taxonomy doc only" — ratify the committed-file rules + verifier-quoting rule (which is where all four trips happened) but keep the runtime helper API-key-specific. Zero runtime risk; the pec password stays protected only by envelope construction.
<!-- END OWNER RULING VERBATIM -->

**Canonical ruling-text SHA-256:**
`766058c8a5831859df867519ed3a19c3a5d91f00b16318401150322a4d134955`
(1332 bytes; UTF-8 text between the verbatim markers, excluding the marker
lines and delimiter newlines; computed by the executing instance from this
packet's marker span after writing and recomputed to confirm — same value
recorded in the D-APP-66 packet's identical span)

**Disposition (Option B, this packet's part of the block):** the
committed-file taxonomy and the verifier-quoting rule — Option A part (ii)
— are ratified as governed taxonomy, landed as the dated deliverable
artifact `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md` in the
DEL-05-03 folder. The runtime helper remains API-key-specific by ruling:
`readConfiguredApiKeyVariants` and the `[REDACTED_API_KEY]` contract are
unchanged, no `[REDACTED_SECRET]` token is introduced, and
`CHIRALITY_PEC_AGENT_PASSWORD` stays protected by envelope construction
only. The Option A registry design above is preserved as reference should a
future owner ruling revisit the runtime question; nothing in this ruling
pre-authorizes it. The DEL-05-03 `_STATUS.md` line-10 deferred item is
discharged by this ruling (its required decision packet now exists and is
ruled; the taxonomy lands as a document, not code). ORN-11's original
evidence remains immutable. No lifecycle transition, no `Checking Approval
SHA` change, no fence contact (F-APP-1..5).

## On-ruling mechanics (planned)

1. Transcribe the owner's ruling verbatim into this packet between markers,
   with the canonical ruling-text SHA-256 (D-APP-63 convention); flip the
   `_REGISTER.md` row to RULED (ruled rows above untouched).
2. If ruled Option A: implement exactly the ruled scope in the same program
   under the normal gates (typecheck, Vitest, `proof:secret-scan`); record
   the ratified taxonomy as a dated evidence addendum in the DEL-05-03
   folder; discharge the `_STATUS.md` Remaining item with a dated History
   line citing D-APP-67 (no lifecycle transition; `Checking Approval SHA`
   untouched); dated run record under `_run_records/`.
3. If ruled Option B: land the taxonomy ratification text only (no runtime
   code); discharge or re-scope the Remaining item per the ruling's text
   with a dated History line.
4. If ruled Option C or declined/deferred: no writes beyond the
   transcription; the packet stays AWAITING_RULING (or records the deferral)
   and the deliverable gate stands.
5. No fence contact under any ruling (F-APP-1..5); no release/professional
   claim; ORN-11's original evidence remains immutable — any broadened proof
   lands as new dated evidence, not edits.
