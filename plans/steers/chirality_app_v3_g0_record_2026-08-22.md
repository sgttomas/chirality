# G0 RECORD — Chirality App v3.0.0-rc.1 — owner rulings of 2026-08-22

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: Chirality App v3.0.0-rc.1 G0 decisions. Target workspaces: Root governance loop and App-dev loop (transcribed into their receipts). Supersedes nothing; the loops' instruments govern.


Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-22, against Revision 3.1
(`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`,
SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`,
main `13201dfe7dc3b97c9aa36f6305cae604b48ef80f`). Where the owner typed text it
is quoted verbatim; "[click]" marks a selected slate option. Items marked
AMENDS PLAN supersede the plan's text for the loops; the SCAs carry the change.

A1 — Native Codex delegation: [click] "Required, no Chirality cap" — enabled for
  untyped / Agent 0 / Agent 1 primaries; no child allowlist, fan-out cap, model
  allocation or scheduling by Chirality; upstream/account limits apply.

A2 — Native-descendant classification: [click] "Not automatically Agent 2".

A3 — Explicit Codex Agent 2/TASK entry when G-ROLE cannot mechanically prove
  non-delegation: [click] "Offer, labelled". Owner text: "I understand the
  predicament, but I can also enforce within my local config file what the max
  number of agents can be in Codex. I understand I'm losing some control and
  potentially contradicting claims the project makes about itself, but that's a
  price I can pay because Codex is both very reliable and the external config is
  something reasonable to ask of a user (at this point in the product's
  development). But it's very important that I be able to perform the full
  Agent 0/1/2 functionality through the Codex App Session so that it can be
  close to parity with native Chirality agents. So my choice would be something
  like outcome 2."
  Recorded form (AMENDS PLAN §5.3 "G0 failure pre-decision"): Agent 0/1/2 role
  entry is always offered for Codex sessions (parity requirement). If G-ROLE
  fails, the Agent 2/TASK mode is still offered, labelled "role not
  mechanically enforced"; evidence from such sessions is marked
  instruction-asserted for governed workflows (plan §5.3 "conformance
  consequence"); D-GOV-35 states that for the delegated-harness-native class
  K-SUBAGENT non-delegation is instruction+config asserted, not
  mechanism-proven; hard filesystem/network/process containment is unchanged.
  Note: the owner's user-level `~/.codex` config does not reach root-private
  homes (A9); the equivalent controls live in Chirality's per-worker overlay.

A4 — Restart semantics: owner text: "It seems that restart or re-attach is
  something the Codex App Server offers? If so, let's incorporate it. If not,
  then I agree with your recommendation here." Fact recorded: App Server offers
  `thread/resume` / `thread/fork` over persisted JSONL rollouts; no in-flight
  turn re-attach is documented. [click] confirmed final form (AMENDS PLAN §4.2
  "Fresh recovery", AT-036, F-14): active turns terminalize on retirement or
  crash; after restart the next action resumes the stored thread via
  `thread/resume` when canonical root, account identity, and policy digest match
  (cwd fixed to the canonical root); otherwise a fresh thread. No in-flight
  re-attach claim.

A5 — App Sandbox: [click] "Decline App Sandbox" — hardened runtime + Developer
  ID + notarization only.

A6 — G-SBX workspace-write failure: owner text: "Proceed as recommended now.
  This sandboxing has been vexing in the past for other matters. Let's try to
  work through it adhering as closely as possible to the intent of what I was
  trying to achieve." Recorded form (AMENDS PLAN §6.2 third paragraph): repair
  first under the unlimited-repair rule; if the exact pin is proven incapable of
  expressing the envelope, return to the owner with the evidence for a decision
  then. No pre-authorized read-only fallback.

A7 — Command-network posture: [click] "Per-root consent, 3 postures" (AMENDS
  PLAN §5.4 last paragraph, §6.2, G-APPR, AT-020, V3-05, K-NET-1 amendment
  text): each canonical root chooses under consent (1) no command network
  [default]; (2) ask per destination — managed-network prompts
  (`networkApprovalContext`) routed through Root API v2 showing host/protocol
  with the stated caveat that a grant may unblock queued requests to the same
  destination, `acceptForSession` allowed only as an explicit user act; (3)
  command network on (`network_access = true`), labelled. G-APPR must prove
  prompt delivery and observe grouping empirically at the exact pin.

A8 — Posture label: [click] "Opt-in Preview".

A9 — Codex operational home: [click] "Root-private app-owned home" — per-root
  `CODEX_HOME`; login per root unless G3 proves safe keyring reuse; ambient
  `~/.codex` not read.

B1 — TM-APP-025: [click] "macOS arm64 only; 2nd target deferred" — second
  deployment target carried to a post-rc.1 scope change; row closes
  RESOLVED_BY_DECISION when SCA-APP-008 applies.

B2 — TM-APP-030 (bundle identity): owner text: "Let it resolve at G-HELPER."

B3 — TM-APP-027/028/032: owner text: "Okay." — retain DEFERRED; not fired;
  expected to fire at G6a–G7 when `release_act` completes the binding manifest.

B4 — Pin drift (TM-ROOT-106 Pi 0.82.0; TM-ROOT-122 Electron 43.2.0): [click]
  "Defer; resolve at G1 separately" — routine Task Management; the plan's
  "resolve before G1 / AT-039" stays a named blocker; SCA-004 / SCA-APP-008 do
  NOT carry pin amendments.

B5 — Root rows: owner text: "I agree with your proposal." — D-GOV-35 resolves
  TM-ROOT-126; the DEL-02-03 M2 draft manifest honours TM-ROOT-127; SCA-004
  dispositions TM-ROOT-035, 042, 107, 108 (and names 106/122 as G1 blockers
  per B4). TM-ROOT-037/039/040/041/104/111/113/114/115/118/119/120/123 are
  untouched.

C1 — App Server 0.149.0 artifact download: not yet authorized (requested with
  the second Root steer).

C2 — WP-00 / DEL-09-04 proof: owner text: "Agreed, I'll execute that sequence
  first before any of this planned work impedes." No frontend writes until the
  capture or an explicit deferral is transcribed.

D1 — D-APP-74: owner text: "No I think I may have made a mistake with D-APP-74
  excluding multi-child execution. The Agent 0/1/2 posture described in the
  root AGENTS.md is what I want and requires that multi-child execution be
  possible." then "I agree with your proposal." Recorded form: the D-APP-74
  exclusion is tranche-scoped to SCA-APP-004; SCA-APP-008 authorizes
  multi-child managed execution and the root AGENTS.md Agent 0/1/2 graph as App
  capabilities for the v3 carriers (DEL-08-04 / DEL-08-05 amendments),
  prospectively superseding that exclusion for those carriers; no retroactive
  edit of D-APP-74.

D2 — F-APP-2 / D-APP-97: owner text: "Yes, keep F-APP-2 active through
  preparation and only list at G6a with exact candidate."

D3 — D-APP-103: owner text: "I agree with your proposal." — SCA-APP-008 records
  "defers": the per-attempt decision-replay packet is prepared after
  SCA-APP-008 is applied so it covers both descendant classes once; one
  sentence in the assessment, no new instrument.
