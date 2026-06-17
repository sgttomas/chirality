# D-APP-12 Ruling - Default Provider Cutover After STAB-02(d) No-Live Proof

**Status:** RULED-HOLD
**Date:** 2026-06-17
**Decision:** Default-provider cutover to `agentSdk`
**Ruling authority:** Human project authority in chat
**Packet:** `execution/_Coordination/_DECISIONS/D-APP-12_PACKET_STAB02D_PROOF_2026-06-17.md`

## Ruling

Option B is approved.

STAB-02(d) readiness evidence is accepted for the Runtime Stabilization program:
package layout, mounted-DMG SDK presence, and the no-live packaged resolver/HOME proof
are sufficient to close the non-live readiness tranche.

Default-provider cutover is **not** approved now. `agentSdk` remains opt-in.

Before any later D-APP-12 cutover packet may recommend making `agentSdk` the default,
WORKING_ITEMS should first request or prepare one bounded live packaged read-tool proof
path, unless the human explicitly waives that proof in a later ruling.

Governance documents must not declare the SDK-backed Anthropic path the active default
runtime until a later ruling explicitly approves that cutover.

## Boundaries

This ruling does not approve:

- changing the default provider to `agentSdk`;
- declaring SDK-backed Anthropic execution the active default in governance text;
- live-provider API use;
- release-readiness claims based on the SDK path;
- concrete non-Anthropic provider implementation or provider routing;
- provider-network expansion;
- Pi runtime paths;
- lifecycle issuance;
- professional approval;
- certification, sealing, authentication, or code-compliance acceptance;
- professional-boundary claim changes.

## Required Next Action

WORKING_ITEMS may complete STAB-06 governance refresh by documenting the accepted
stabilization outcomes and the continuing opt-in provider posture. If no replacement
active queue is selected by the human, coordination should stop at no unblocked
stabilization tranche rather than selecting unapproved live-provider work.

## Validation Requirements

STAB-06 is governance/control-plane work. Runtime commands are not required unless the
refresh changes executable behavior. Minimum expected evidence:

- `git diff --check`;
- targeted stale-reference searches for `D-APP-12`, STAB-02 readiness, default-provider
  wording, and retired active-queue pointers;
- link/path existence checks for newly referenced ruling and packet files.
