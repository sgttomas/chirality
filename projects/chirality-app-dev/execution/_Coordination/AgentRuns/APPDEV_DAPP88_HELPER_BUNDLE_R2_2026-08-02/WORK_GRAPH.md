# Work graph — D-APP-88 standalone helper R2

- Version: `v1` (frozen before dispatch)
- Selection authority: App `HELP_HUMAN` retry direction under owner-approved D-APP-88 Option B
- Posture: `TERMINAL_FAN_OUT_IN`, serialized implementation then fresh verification
- Package/deliverable: `PKG-09 / DEL-09-04`

## Nodes

1. `A2-DAPP88-R2-IMPLEMENT-01` — `FAILED / BLOCKED`; the standalone-helper candidate passed structural packaging and fresh-stop gates, failed the required auditable post-GUI first-signal gate, froze evidence, and rolled back all R2 product/config/test bytes.
2. `A2-DAPP88-R2-VERIFY-01` — `FAIL / EVIDENCE COMPLIANCE`; the first fresh verifier accepted the conservative engineering disposition but found a malformed source hash, overbroad two-arm/raw-evidence claims, an undisclosed TASK tool-policy violation, and an unfrozen whole-tree equality claim.
3. `A2-DAPP88-R2-IMPLEMENT-01-C1` — `PASS / EVIDENCE REMEDIATION`; corrected only R2 evidence, narrowed the blocker, disclosed the tool-policy failure, fixed the hash, and froze deterministic whole-tree equality without product writes.
4. `A2-DAPP88-R2-VERIFY-02` — `PASS`; second fresh read-only verification accepted the corrected package for truthful `BLOCKED/PARTIAL` manager fan-in, not implementation acceptance.
5. `WI-PKG09-DAPP88-B-R2-FANIN` — `BLOCKED/PARTIAL`; manager accepts the diagnostic evidence and rollback, routes the Root investigation request upward, and preserves D-APP-88 as open.

## Gates

- Gate 1: standalone helper is a complete electron-builder product with its own `appId`, product/executable name, and builder-generated matching Chromium helper topology. The GUI bundle is not copied or mutated into the helper.
- Gate 2: deterministic packaging embeds exactly one finished top-level runtime helper at `Contents/Library/LoginItems/`; final output is relocatable and hash/plist/executable/symlink bound.
- Gate 3: final-bit drills prove LaunchAgent helper routing, one runtime singleton/store set, CLI/GUI coexistence, first-signal graceful teardown after coexistence, SIGKILL recovery, safeStorage/resource/instruction-root continuity, no TCP/token/global Node, and exact cleanup.
- Gate 4: full software checks and D-APP-89 zero-consumer/rollback guards pass; Root projection is restored exactly.
- Gate 5: fresh verifier returns PASS, or the implementation is rolled back/preserved as a truthful blocker package before manager fan-in.

No copied-main mutation or signal-wrapper fallback is permitted.
