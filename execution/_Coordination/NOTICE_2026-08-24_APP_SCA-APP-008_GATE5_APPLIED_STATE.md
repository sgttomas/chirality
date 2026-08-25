# NOTICE TO ROOT — SCA-APP-008 Gate-5 Applied State

**Status:** `READY_TO_ROUTE`
**Notice class:** cross-loop coordination, not authority
**Routing state:** `NOT_ROUTED`
**Supersedes for routing:** `DRAFT_NOTICE_TO_ROOT.md`, SHA-256 `8ebc728b6d6c408a3dfeb60ae07887dbe7d5b88ba8fe06c1b954e98e8a380f72`

## Coordination notice

The App-dev loop's owner-authorized SCA-APP-008 Gate-5 candidate branch has
applied and validated these exact App authoritative identities:

- SOFTWARE_DECOMP post-image: `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`
  (`112419` bytes; topology remains 10 packages and 51 deliverables);
- App contract post-image: `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`
  (`34877` bytes);
- corrected App invariant-coverage companion register:
  `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`
  (`98230` bytes, 83 invariant IDs, 50 families); and
- App authority corpus v19:
  `eaec3c0a3a1b7bf76a9a3ec922bf826772e9097441d5631126cb7a5e025e10ef`,
  current with no drift after exactly 51 governed `REF-002` updates.

The App K-CONTROL-1 row is aligned to the ratified Root contract at
`docs/CONTRACT.md`, SHA-256
`ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`.
Both surfaces state that exactly one runtime control socket is live today,
that the Root daemon exclusively owns `{userData}/runtime` under Root
K-RUNTIME-1, and that the private daemon-to-Process-Supervisor socket becomes
live only through the separately gated DEL-02-07/WP-03 implementation
pathway. The App register records K-CONTROL-1 as Root-owned external authority,
`MAPPED_WITH_OPEN_ISSUE`, with
`RUNTIME-OPEN-005;DEL-02-07;WP-03`; no implementation-coverage claim is made.

The registered workflow refreshed dependency records for DEL-02-05,
DEL-08-04, DEL-08-05, and DEL-09-05. The fresh named audit
`AUDIT_DEP_CLOSURE — SCA-APP-008-GATE5-POST-APPLICATION` returned
`WARNINGS`, non-blocking: 51/51 registers are schema-valid, 564/564 evidence
rows are populated, and 112/112 active endpoints resolve. It surfaces one
nine-node live-register SCC with ten representative cycles, five isolated
deliverables, and one informational bidirectional pair. It does not cut,
merge, invert, or linearize the new SCC. The accepted A2-B
`DECOMPOSE` / `DECOMPOSE` / `INVERT` orderings remain intact, and E-018,
E-020, and E-032 remain objective-relative and non-gating.

## Remaining gates and blockers

This notice lifts none of the following:

- `_LATEST.md` pointer movement remains a separate owner act; the live pointer
  remains byte-identical to SHA-256
  `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`;
- the owner merge that would land this candidate branch on `main` remains a
  separate act;
- WP-03 and WP-05 fixtures and a later explicit implementation act remain
  required for the delegation and supervisor-socket carriers;
- the accepted Root/App account-consent contract remains a downstream gate;
- TM-ROOT-106 and TM-ROOT-122 remain G1 blockers, and G1 remains unruled;
- C1 App Server artifact download remains unauthorized;
- TM-APP-030 remains assigned to G-HELPER;
- D-APP-97 and F-APP-2 remain active through preparation and lift only at G6a
  against the exact candidate; G6a is unruled;
- all ten DEL-02-06 binding-manifest entries remain `HELD_UNAVAILABLE`;
- D-APP-103 continues to `defers`; no decision-replay packet was created;
- WP-09 runbook authoring/review and WP-11 release execution remain separate,
  with the G6a exact-candidate ruling still required;
- the second deployment target remains deferred to a post-rc.1 scope change;
- the warning-bearing live-register SCC and five isolated deliverables remain
  unresolved derivative findings without repair or scheduling authority; and
- every later owner gate, carrier activation, SOW/lifecycle transition,
  implementation dispatch, signing, notarization, deployment, distribution,
  publication, release-readiness, and reliance decision remains separately
  governed.

## Requested Root handling after routing

When the owner routes these exact notice bytes, the Root loop may record the
App identities as cross-loop coordination and surface any exact Root/App
contract drift. The Root loop adopts, amends, or declines under its own
instruments and cadence. This notice is not Root authority and does not request
a Root contract, schedule-basis, lifecycle, implementation, or release change.

The frozen draft remains immutable historical assessment evidence and must not
be routed. This regenerated notice is ready to route but has not been routed,
and no Root-loop path has been written by the App loop.
