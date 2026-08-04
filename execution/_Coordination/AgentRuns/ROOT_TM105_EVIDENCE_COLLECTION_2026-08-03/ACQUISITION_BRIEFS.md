# Bounded evidence-acquisition briefs

Status: `PREPARATION ONLY — THESE BRIEFS SELECT NO SEMANTICS`

Each brief produces evidence and bounded alternatives. None may draft a no-TBD
successor, present a byte gate, modify product source, or infer an owner/vendor
fact. Any experiments require a clean declared environment and immutable raw
evidence.

## AB-01 — authorization and execution threat model

- **TBDs:** 05, 06, 08, 17, 19, 20.
- **Inputs:** current client auth, tool descriptors/bridges, App/Piping needs,
  deployment diagrams if supplied.
- **Acquire:** asset/principal/trust-boundary inventory; attacker capabilities;
  confused-deputy, replay, stale grant, policy mismatch, credential leakage,
  child-widening, native-tool bypass, and evidence-tamper cases.
- **Owner/vendor facts required:** trusted principals, grant issuer and policy
  authority, acceptable trust anchors, deployment topology, regulated data.
- **Output/acceptance:** threat matrix with severity, required mechanical
  controls, unmitigated risks, and evidence needed to falsify each control.
  Every unsupported assumption remains marked `UNKNOWN`.

## AB-02 — backend, rights grammar, and topology proof

- **TBDs:** 02, 05, 17, 19.
- **Prerequisite:** AB-01.
- **Acquire:** bounded candidates for OS sandbox versus brokered tools; exact
  version/API/package identity; rights-grammar expressibility; process tree,
  path canonicalization, symlink/race, network/provider-channel, IPC/device,
  credential, orphan, and bypass probes.
- **Owner/vendor/platform facts required:** backend support commitment,
  redistribution/licensing, signed/entitled context, security update policy,
  deployment restrictions.
- **Output/acceptance:** per-backend immutable test report with raw commands,
  environment identity, expected/actual denial matrix, escape/adversarial
  corpus, known gaps, and explicit `NOT_QUALIFIED` unless every gate passes.

## AB-03 — platform and packaging matrix

- **TBDs:** 02, 18, 19.
- **Prerequisite:** AB-02 candidate backends.
- **Acquire:** exact OS version/architecture/backend pairs, clean CI or physical
  witnesses, packaged/signed/notarized/install-context runs, and unsupported
  pair behavior. Cross-platform dependency entries are not support evidence.
- **Owner/vendor facts required:** release targets, minimum OS versions,
  architectures, packaging channels, signing/entitlement policy, support
  lifetime.
- **Output/acceptance:** allowlisted matrix with evidence hashes per cell;
  absent or untested cells remain unsupported and fail closed.

## AB-04 — interruption and cleanup timing study

- **TBDs:** 01, 10, 11.
- **Prerequisites:** AB-02, AB-03, AB-08 family inventory.
- **Acquire:** repeated cold/warm and fault-injected measurements per tool/effect
  class and supported platform/backend: request-to-ack, graceful completion,
  forced termination, child/resource cleanup, evidence durability, tail
  percentiles, hangs, and orphan scans.
- **Non-transfer rule:** accepted TM112 daemon-stop values are exact evidence
  for daemon transport shutdown, not generic tool deadlines.
- **Owner/vendor facts required:** maximum acceptable latency and provider/tool
  interruption guarantees.
- **Output/acceptance:** raw timestamped trials and reproducible harness, with
  empirical ranges separated from later human policy caps.

## AB-05 — workload, result-budget, overflow, and partial-output study

- **TBDs:** 12, 13, 14, 15, 16.
- **Prerequisites:** AB-02, AB-03, representative tool-family inventory.
- **Acquire:** privacy-safe workload corpus and distributions for all proposed
  dimensions; atomicity and data-loss effects of deny/truncate/artifact/
  continuation/fail; partial-output classes; storage/network/process costs;
  deterministic repeatability.
- **Owner/consumer facts required:** acceptable maxima, latency/storage cost,
  loss/truncation policy, privacy classifications, continuation posture.
- **Output/acceptance:** evidence tables by tool/effect class; no default or
  maximum is proposed without workload and product-policy provenance.

## AB-06 — schema, state, grant, and digest design evidence

- **TBDs:** 03, 04, 10, 15, 16, 17, 20, 21.
- **Prerequisites:** AB-01, AB-02, AB-07, AB-09.
- **Acquire:** complete field/type census; current-schema crosswalk; required
  versus optional fields; canonical serialization candidates; digest-bearing
  type inventory; state-transition tables; migration/unknown-version vectors;
  grant/policy and continuation-token structural requirements.
- **Owner facts required:** compatibility and crypto-agility posture; exact
  accepted schema family only at a later semantic gate.
- **Output/acceptance:** versioned candidate schemas plus cross-language golden
  vectors and negative corpora. This brief returns designs for later review,
  not accepted bytes.

## AB-07 — evidence store, retention, redaction, and privacy basis

- **TBDs:** 06, 09, 12, 14, 20.
- **Prerequisite:** AB-01.
- **Acquire:** current store/delete/migration inventory; content-class and
  metadata-class inventory; tamper/truncation/reorder behavior; access control;
  encryption/key custody if applicable; redaction reversibility; retention and
  deletion obligations; incident/e-discovery needs.
- **Owner/legal/privacy facts required:** retention durations, protected data,
  approved store, access roles, deletion/legal-hold rules.
- **Output/acceptance:** provenance-marked policy requirements and testable
  store behaviors with legal/product facts distinguished from engineering
  observations.

## AB-08 — implementation-family conformance and no-fallback evidence

- **TBDs:** 07, 08, 10, 11, 14, 16, 18, 19.
- **Prerequisites:** AB-02 and AB-03 for backend/platform-specific cases.
- **Acquire:** public-tool-to-family inventory; adapter/version/schema bindings;
  fixture/stub/synthetic/preview path census; permission-before-start,
  terminal/evidence, cancellation, result budget, cleanup, unavailable and
  unknown-state tests; deliberate family-change protocol.
- **Owner/consumer facts required:** family membership, affected-client suite
  and acceptance owners.
- **Output/acceptance:** exact suite manifest, independently reproducible raw
  evidence, zero silent-fallback paths, and explicit non-conformance for gaps.

## AB-09 — compatibility, lifecycle, and DEL-02-06 alignment

- **TBDs:** 01, 04, 07, 12, 15, 18, 21.
- **Inputs:** accepted DEL-02-06 V2 semantic bytes in their exact scope,
  current session/event/client surfaces, affected-client inventories.
- **Acquire:** field-by-field identity/lifetime/rollover matrix; compatibility
  identity and migration impact; old/new client behavior; interrupted/partial
  work treatment; digest/profile version migration; affected-client census.
- **Boundary:** do not widen DEL semantics into TM105. Record exact consistency,
  conflict, or non-coverage for each link.
- **Owner/client facts required:** supported migration window, client versions,
  lifecycle commitments, and each affected client's acceptance.
- **Output/acceptance:** compatibility delta and conflict register with exact
  evidence hashes and separately owned follow-ons.
