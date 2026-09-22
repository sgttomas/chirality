<!-- PACKET
id: P-13
cluster: CL-13
title: Protected paths, instruction root and hooks on Codex
question: On the live Codex path, which surface carries the protected-path, instruction-root and hook guarantees: the Codex sandbox (documented), new code, or none (retired)?
recommended: B: document sandbox; keep domain rows accepted
depends_on: P-09, P-04
decision_type: owner (incl. App governance amendment); engineering; external authority (Root K-DOMAIN-2)
tier: GOVERNING
-->
# P-13 — Protected paths, instruction root and hooks on Codex

Cluster CL-13 · live-path finding XPF-042 · draft by TASK D3 for HELP_HUMAN review; not a ruling.

**Question.** On the legacy harness, Chirality's own hooks blocked three kinds of write:
- writes outside the project;
- writes to the instruction root;
- writes to protected domain paths.

On the live Codex path, only the user's chosen Codex sandbox limits writes. Which surface should carry each guarantee now?

Addendum 9 keeps this finding separate from R4-Q6 (whether D-GOV-43 superseded the App DIRECTIVE and K-PERM texts, P-04). The "Full access" part still depends on P-04.

## What we found
- The guarantees are unamended:
  - K-PATH-2: writes stay inside the project root;
  - K-ROOT-2: ordinary execution does not change the instruction root;
  - K-HOOK-1: hooks fail closed;
  - SPEC §15.2: required hooks.

  Each names Chirality hooks as its enforcement (`docs/CONTRACT.md:52,99,100`; `docs/SPEC.md:847-860`). [GOVERNING]
- K-DOMAIN-2 (protected domain paths) sits under CONTRACT §1.10 "Domain Engine Future Scope". It specializes a Root framework clause and "MUST NOT weaken" it (`docs/CONTRACT.md:142,150`). [GOVERNING]
- D-GOV-43 item 4 makes sandbox and approval the user's choice per project and per turn, Full access included. [GOVERNING]
- On the live path, "workspace-write" maps to a Codex sandbox whose only writable root is the project folder (`projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts:107`). That keeps the instruction root and other folders unwritten. "Full access" maps to `danger-full-access`, which lifts that limit (`projects/chirality-runtime/packages/contracts/src/delegated.ts:318-330`). [code]
- No live code guards a domain profile's protected paths *inside* the project, and none rejects symlink writes. The Runtime registers no Chirality tools or hooks: the Codex adapter starts each turn with an empty tool list (`projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts:231`; R3 cross-package finding XPF-042). [code]
- 9 of the 25 PRIMARY rows are PKG-10 domain-path rows. Workers read them as "Difference already permitted" under D-APP-37 (doc-only acceptance of the future domain scope) and D-APP-49. [run finding]
- The PKG-07 rows turn on containment and instruction-root checks in scaffolding and scanning. The live scaffold returns 501 (see P-15), and the scanner is only as contained as the root its caller supplies. [run finding]

## Affected rows
<!-- COUNTS -->
**25 rows are decided in this packet** (PRIMARY); 51 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-13`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Total |
|---|---:|---:|---:|---:|---:|
| PKG-06 |  |  | 1 |  | 1 |
| PKG-07 | 2 | 4 | 4 |  | 10 |
| PKG-10 |  |  | 5 | 9 | 14 |
| **Total** | **2** | **4** | **10** | **9** | **25** |

ALSO/CONTEXT members by Disposition: Governing texts disagree 31, Partly built 14, Text out of date 3, Built differently 2, Difference already permitted 1.

<!-- /COUNTS -->
The 25 PRIMARY rows carry "no owner decision needed" as sealed. Grouped:
- PKG-10 protected and proposal paths (14): 9 already permitted, 5 text out of date;
- PKG-07 containment rows (10);
- one PKG-06 stale considerations row.

The 51 ALSO rows, mostly PKG-06 hooks and DEL-07-01 instruction root, are decided in P-09.b. They must agree with this packet.

## Options
**A. Change the code.** Add live enforcement:
- a Runtime-side check on Codex file-change approvals for the instruction root and protected domain paths;
- refusing or warning on Full access for governed projects.

*R5 would:* hold the guarantee rows until a separate implementation brief, issued in the Runtime project loop (this is Runtime code), lands. The stale rows are repaired now.

**B. Change the deliverable text (and the governing text).** Record that the Codex sandbox carries containment and instruction-root protection when "workspace-write" is chosen, and that Full access lifts it by the user's explicit choice (D-GOV-43 item 4). Retire the Chirality-hook wording through a governance amendment. *R5 would:* edit the listed rows. The PKG-10 domain rows stay "Difference already permitted", as future scope.

**C. Accept the divergence** for all three guarantees without amending the governing texts. *R5 would:* record the acceptance. K-ROOT-2 and K-HOOK-1 stay unamended, so the conflict remains.

**D. Defer** until a domain engine is actually integrated.

## HELP_HUMAN recommendation (draft)
Option B.
- The live sandbox does protect the project boundary and the instruction root under the default policy.
- Lifting that under Full access is what D-GOV-43 item 4 chose.
- The domain-path rows are future scope that D-APP-37 already accepted as doc-only.
- Symlink rejection and fail-closed hooks have no Codex counterpart. The amendment should say plainly whether they are retired or kept.
- If the owner keeps any of them, that part becomes option A.

K-DOMAIN-2 must not be weakened without Root authority.

## Who decides
- The owner decides which guarantees remain.
- The App governing-text changes (CONTRACT K-PATH-2, K-ROOT-2, K-HOOK-1; SPEC §15.2) go through an App governance amendment.
- Any code is an engineering matter, through an implementation brief.
- Changing or weakening K-DOMAIN-2 is outside the owner's App authority. It routes to Root / HELPS_HUMANS.

## On ruling
1. HELP_HUMAN records the ruling in the consolidated R4 ruling record: the next free D-APP ID, with its register row.
2. The R5 tranche managers for PKG-10, PKG-07 and PKG-06 edit the P-13 PRIMARY key set in `PACKET_INDEX.csv`.
3. A separate App governance-amendment tranche handles the CONTRACT and SPEC clauses by the corpus-bump procedure (D-APP-38 under D-APP-56).
4. Any code guard goes to a `software-bounded-implementation` brief.
5. R6 backchecks every listed row. There is no lifecycle transition.

## Risks, contested rows and dependencies
- ALSO rows:
  - `DEL-07-01#CLM-011.4` (S2-013): the spot check proposes adding R4-Q6. It diverges only through Full access, so it depends on P-04.
  - `DEL-10-02#CLM-024` (S2-059): undecided whether "Governing texts disagree" or a future trade-off. Decided in P-09.
- PKG-10 graded the same point three ways across rows: "Governing texts disagree", "Partly built", "Difference already permitted" (XPF-042). R5 should make them consistent under the ruling.
- Dependencies:
  - **P-09.b:** hook and instruction-root rows;
  - **P-04:** Full access;
  - **P-15:** scaffold containment.
