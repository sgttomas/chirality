# DRAFT — App Notice to Root — SCA-APP-010 Root-Owned Dependencies

**Status:** `DRAFT_UNROUTED — retained inside the SCA-APP-010 snapshot`
**Notice class:** cross-loop coordination, not authority
**Routing state:** `NOT_ROUTED`
**Authority effect:** none. This draft leaves the snapshot only after the owner applies SCA-APP-010 at Gate 5 and separately authorizes routing to `execution/_Coordination/`.

## Proposed notice

The App-dev loop's owner-approved SCA-APP-010 amends the App decomposition so
that the centre dialogue is the invariant primary surface, Workbench and
Pipeline presentation are retired from the active shell (code retained), and
the prompted specification ladder (folder, agent, permissions, delegation,
optional governed workflow) is seated on existing App carriers. Applied
identities will be recorded here at routing time: decomposition post-image
`c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`,
companion register post-image
`63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`, Scope
Ledger 80 → 84 rows, topology unchanged.

Three App presentations depend on Root-owned semantics the App does not
define. The App records them as `OI-008` and asks Root only to note them as
cross-loop coordination; acceptance, amendment, or decline is a Root-loop act:

1. **App-wide account presentation over a root-private login home.** App
   `DEL-02-05` presents one OpenAI account for the app and consent, network
   posture, and role per folder. `K-CONSENT-1` semantics are unchanged. The
   root-private login home (`K-KEY-1`) and any shared-login contract remain
   Root `DEL-02-09`'s; App `DEL-02-05-V3-03` stays gated on that contract.
2. **Additive `proposal.*` event types.** App `SOW-082` consumes
   `proposal.offered`, `proposal.accepted`, `proposal.adjusted`, and
   `proposal.declined` in the session record. These are candidates against
   the closed `HarnessEvent` schema v2 (`K-EVENT-3`) owned by Root
   `DEL-02-10`; the App consumes them only after Root acceptance is routed
   back. Until then the App's `DEL-05-02` item remains gated.
3. **Per-chat delegation policy on the session record.** App `SOW-083`
   binds a delegation policy (`none` by default) in the boot request and
   honours it in the App-managed delegation bridge. The stored field on the
   daemon-owned session record is Root `DEL-02-11`'s.

No Root action is requested beyond recording these dependencies. The App
adds no delegation class, no tool outside its in-process deterministic
boundary, no provider or network change, and no release act.

## Exclusions

This draft is not App or Root authority; it does not activate implementation,
alter either loop's contract or scope ledger, move any pointer, or claim
release readiness.
