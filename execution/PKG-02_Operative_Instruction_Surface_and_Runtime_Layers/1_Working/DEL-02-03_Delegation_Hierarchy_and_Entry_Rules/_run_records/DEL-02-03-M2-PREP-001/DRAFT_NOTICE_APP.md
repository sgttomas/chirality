# DRAFT — Root D-GOV-35 Delegation-Class Notice to Chirality App

Status: `DRAFT — NOT ROUTED — BLOCKED ON D-GOV-35 RULING`

Intended route after ruling:
`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-22_ROOT_DGOV35_DELEGATION_CLASS.md`

This draft is coordination, not authority. It remains inside the Root
DEL-02-03 preparation record. It does not amend the App loop, adopt D-GOV-35,
authorize App WP-06, lift a held binding, or permit a foreign write.

## Prospective Root change

If D-GOV-35 is ruled and the separate M2 application tranche is authorized,
Root `AGENTS.md` would change from SHA-256
`268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`
by the exact N1 patch at SHA-256
`4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`.
The change would recognize `Chirality-managed` and
`delegated-harness-native` execution while preserving managed children as the
sole Chirality-managed path. It would permit untyped, Agent 0, and Agent 1
primary native delegation, make native descent insufficient to assign an
Agent 0/1/2 role, always offer Codex Agent 0/1/2 role entry, and preserve
explicit Agent 2/TASK entry when `G-ROLE` cannot prove non-delegation with the
label `role not mechanically enforced`. Governed-workflow evidence from that
posture is `instruction-asserted`; for the native class K-SUBAGENT
non-delegation is instruction+config asserted, not mechanism-proven. Hard
filesystem, network, process, canonical-root, account-identity, and policy
containment remains required.

## App surfaces and follow-on

The App loop owns whether and how to adopt the notice through SCA-APP-008 and
App WP-06. Its assessment must cover:

- App `docs/CONTRACT.md` K-SUBAGENT-1/2/3;
- immutable D-APP-68 disposition 4 and prospective supersession through the
  App loop's own instrument;
- DEL-08-04's SOW and DEL-08-05's record boundary;
- `frontend/src/lib/harness/subagent-governance.ts:205-213`, whose accepted
  file SHA-256 is
  `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c`;
- the G0 A3 parity/evidence amendments and the App-owned runtime/test changes;
  and
- rebuilding and verifying the generated packaged instruction-root mirror
  through `frontend/package.json` and
  `frontend/scripts/verify-instruction-root-integrity.mjs`, never by manually
  rewriting generated evidence.

The App authority corpus is currently v18 and does not pin Root `AGENTS.md`;
the App loop decides whether to expand it. Existing packaged-security,
parity-run, D-APP-88, login-proof, and reconciliation evidence identified in
the D-GOV-35 `IMPACT.md` is historical/immutable and must not be rewritten.
The Root-owned public-export projection under `exports/chirality-app/` is a
Root follow-on, not an App write.

The receiving loop may adopt, amend, decline, or defer this coordination under
its own instruments and cadence. It should return its disposition and any new
candidate/evidence identities to the Root coordination surface.
