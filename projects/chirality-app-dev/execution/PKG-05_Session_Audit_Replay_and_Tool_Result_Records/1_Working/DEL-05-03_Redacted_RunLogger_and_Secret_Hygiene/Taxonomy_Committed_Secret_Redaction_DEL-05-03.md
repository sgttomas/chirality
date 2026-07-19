# Taxonomy: Committed-Secret Redaction — DEL-05-03

**Purpose:** the governed taxonomy for secret-shaped strings in committed and
generated text within this project, ratifying the live scanner's previously
unwritten fixture-marker convention and the verifier-quoting practice as
deterministic rules. This is the deliverable ruled by D-APP-67 Option B.

**Authority:** D-APP-67 Option B, owner ruling 2026-07-19, transcribed
verbatim with canonical SHA-256
`766058c8a5831859df867519ed3a19c3a5d91f00b16318401150322a4d134955` in
`execution/_Coordination/_DECISIONS/D-APP-67_PACKET_SECRET_REGISTRY_REDACTION_TAXONOMY_2026-07-18.md`
§Human Ruling. Taxonomy authorship is agent work under that ruling; the
ruling is the owner's act (K-AUTH-1).

**Date:** 2026-07-19

**Standing of this document:** agent-produced findings ratified by owner
ruling; no issuance, release-readiness, or professional claim is made or
implied. Lifecycle state of DEL-05-03 is unchanged by this artifact. The
grounding line numbers below cite `frontend/scripts/scan-secret-evidence.mjs`
as read in the live tree on 2026-07-19; if the scanner changes, the rules
stand and the citations are refreshed by a dated addendum, never by editing
this ratified text.

---

## Rule 1 — Shape rule

A **secret-shaped string** may appear in committed or generated text **only
in fixture-marked form**. Secret shapes are the scanner's detection classes:

- an `sk-ant-` continuation — pattern `sk-ant-[A-Za-z0-9._=/-]{8,}`
  (`frontend/scripts/scan-secret-evidence.mjs:50`, scanned at lines 320-334);
- a URL-embedded credential — `https?://user:pass@host` shape
  (`scan-secret-evidence.mjs:51`, scanned at lines 336-350);
- a ≥8-character high-entropy token appearing in a secret-named context
  (key/token/password/credential naming), the class the scanner's
  environment-value checks instantiate for configured secrets
  (`scan-secret-evidence.mjs:180-204`; usability floor `value.length >= 8`
  at line 187).

**Fixture-marked form** means the token itself contains one of the scanner's
sanctioned markers — the 12-marker list `ambient`, `alias`, `alt-key`,
`bridge`, `dummy`, `example`, `fake`, `fixture`, `placeholder`, `redaction`,
`test`, `ui-key` (`scan-secret-evidence.mjs:52-65`) — or the file lives
under a sanctioned test path (`__tests__`, `/test/`, `/tests/`;
`isFixtureToken`, `scan-secret-evidence.mjs:141-148`). Marker-in-token is
the preferred form: it keeps the string self-evidently synthetic wherever it
is later quoted, independent of file location.

The marker list is **governed**: additions or removals are recorded changes
to the scanner's `FIXTURE_MARKERS` list (`scan-secret-evidence.mjs:52-65`)
with a dated note in this deliverable, never ad-hoc judgment applied at
review time.

## Rule 2 — Value rule

**Exact live environment secret values are blocked unconditionally; markers
sanctify shapes, never values.** The scanner scans every candidate file for
the exact values of the configured environment secrets in raw and
URL-encoded variants (`collectEnvironmentSecrets`,
`scan-secret-evidence.mjs:180-204`; variant expansion at lines 194-200) and
records every occurrence with disposition `blocked`, reason
`actual_environment_secret_value`, with **no fixture-marker escape**
(`scan-secret-evidence.mjs:296-318`). A real value containing the substring
`test` is still a real value. Any `blocked` finding fails the scan
(`scan-secret-evidence.mjs:401-403`, exit at lines 431-433).

Findings themselves persist **hash-only**: the scanner records
`valueSha256` and `valueLength`, never the raw matched value
(`redactedFinding`, `scan-secret-evidence.mjs:166-178`).

## Rule 3 — Verifier-quoting rule

Verification and review artifacts (verifier returns, run records, evidence
notes, decision packets) quote secret-shaped tokens **only in fixture-marked
form**. When a verifier must quote a non-marked secret-shaped token found in
evidence, the quote is **defused in place** — a sanctioned marker (Rule 1
list) is inserted into the quoted token — with a disclosed editorial note
stating that the quote was defused; the verdict text itself is untouched.

This codifies the 2026-07-18 practice: four consecutive verifier returns
tripped the secret-hygiene gate that day entirely over this
fixture-marker/real-credential boundary because it was unwritten convention
(recorded in the D-APP-65 accepted basis, §2 recommendation 4, and the
D-APP-67 packet §Context). Under this rule the boundary is deterministic
for every future verifier: quote marked tokens freely; defuse-and-disclose
anything else.

## Rule 4 — Runtime boundary

The runtime redaction contract **remains configured-API-key-specific per
this ruling**: `readConfiguredApiKeyVariants`
(`frontend/src/lib/harness/run-logger.ts:64-77`) continues to draw from its
three API-key sources only, replacing with the single token
`[REDACTED_API_KEY]`; no `[REDACTED_SECRET]` class token is introduced. The
pec agent password (`CHIRALITY_PEC_AGENT_PASSWORD`,
`frontend/src/lib/harness/mcp/pec-bridge-client.ts`) remains protected by
envelope construction (the allowlisted envelope surface), not by the
redaction registry. The Option A configured-secret registry design is **not
adopted**; it is preserved as reference in the D-APP-67 packet for any
future owner ruling.

## Rule 5 — Enforcement surfaces

- **Committed and generated text:** `npm run proof:secret-scan`
  (`frontend/package.json:30`) runs
  `frontend/scripts/scan-secret-evidence.mjs` over git-tracked files plus
  generated harness artifacts (`candidateFiles`,
  `scan-secret-evidence.mjs:242-273`), writing the hash-only summary to
  `frontend/artifacts/harness/security/latest/secret-scan-summary.json`
  and failing on any `blocked` finding. This is the deterministic gate for
  Rules 1-3 on everything the repository carries.
- **Runtime:** the run-logger value-redaction tests
  (`frontend/src/__tests__/lib/run-logger.test.ts`) and the redaction path
  matrix tests (`frontend/src/__tests__/lib/redaction-path-matrix.test.ts`)
  pin the Rule 4 boundary: configured API-key values never appear raw in
  persisted events, replay, or bridge output, in raw or URL-encoded
  variants.
