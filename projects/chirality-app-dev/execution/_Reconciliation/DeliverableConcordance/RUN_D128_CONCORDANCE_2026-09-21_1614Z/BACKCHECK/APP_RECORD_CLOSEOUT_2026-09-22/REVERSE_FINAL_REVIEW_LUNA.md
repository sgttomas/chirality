# Final reverse-map comparison

Reviewer: `/root/reverse_final_comparison_luna`, read-only Type 2 comparison, `gpt-6-luna` / xhigh. Scope: the 107-row App reverse-ownership map and the named checks below. No source, map, or Git edits were made; this report is the sole write.

## Result

**Semantic comparison: PASS at the reviewed map bytes. Final source binding: PASS at the current snapshot, with a known administrative dependency.** The map SHA-256 is `2224ca155853003c57e6ac36b6c330201549afaa3a964fd8e7670dffe1be898b`, matching the assigned candidate.

The frozen R3 source contains 107 non-sentinel capabilities. The map contains the same 107 IDs exactly once. Independent recomputation found all 107 `OriginalRowSHA256` values and the four copied source fields (`OriginalCapability`, `OriginalReach`, `OriginalState`, `EvidencePaths`) exact. The 102 row-to-claim-key associations resolve to 22 distinct keys in frozen R2; no key is missing. The six dispositions total 40 existing App obligation, 28 mechanism evidence, 23 external Runtime-owned, 9 legacy/retired/non-MVP, 4 Root-instruction-owned, and 3 accepted App requirement carrier-repair rows.

`refresh_reverse_bindings.py --check` passed: 107 rows, 102 current claim citations, zero stale source hashes, and the expected map SHA. An independent recomputation found all 185 distinct paths named in `SourceHashes` present and matching their recorded bytes. Current claim citations point to the expected current claim heading or responsibility/acceptance section; the citations preserve frozen discovery keys and do not claim that historical suffix keys are current headings.

## Focused semantic comparison

The three update capabilities—CAP-ELECTRON-030, CAP-SHELL-014 and CAP-SHELL-015—are consistently assigned to DEL-09-05 CLM-005 (release-check maintenance) and DEL-02-01 CLM-009 (shell presentation). The current DEL-09-05 block names manual, startup and six-hour metadata checks, fixed endpoints, refusal of credentials and redirects, truthful state and explicit browser handoff. DEL-02-01 CLM-009 carries the account-row presentation and the same bounded behavior; CONTRACT K-NET-1 supplies the governing network rule. The map preserves named tests and candidate-bound native evidence as remaining verification. It does not report fresh runtime/native results or authorize install, restart or publication.

CAP-SETTINGS-041 remains `MECHANISM_EVIDENCE`: its preload type declaration is evidence of represented IPC shape, while the rationale assigns each feature to its own accepted owner. The correction removes the false implication that update authority or carrier propagation is unresolved. Its remaining task retains sender/shape isolation and feature conformance and does not create updater scope.

These focused rows agree with the earlier preliminary semantic review and affected claim-citation backcheck in `REVERSE_REVIEW.md`. No new owner decision, unsupported feature, retirement, or product-completion assertion was found.

## Binding dependency and limits

The map binds `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` in the three updater rows at SHA-256 `c0096fffd2c38488d2e58ce6125609ab483566869f9b9424d805556678fb3ab8`. The bytes match now, but the parent has identified a pending final administrative D-APP-128 status update to that register. After that update, refresh this map's affected register binding, rerun `refresh_reverse_bindings.py --check`, and record the successor map SHA before calling source bindings immutable. This is a hash-only dependency unless that administrative edit changes the governing decision or mapped obligations.

This review does not certify implementation behavior, native update scheduling, signing, packaging, a product release, or lifecycle acceptance. The review covers the assigned map and bindings only; it does not close the delivery and verification tasks retained in the App records.

## Affected final hash-only recheck

Parent updated the App D-APP-128 run-visibility entry in `_REGISTER.md`. Its current SHA-256 is `648117032619476bc6a98506b16225c0922e311a5867a862c96072ac0bca3f79`. The three and only three reverse-map rows binding that register are CAP-ELECTRON-030, CAP-SHELL-014 and CAP-SHELL-015; each now binds that exact current SHA. Their prior register binding was `c0096fffd2c38488d2e58ce6125609ab483566869f9b9424d805556678fb3ab8`.

**Affected final binding: PASS.** `refresh_reverse_bindings.py --check` passes on map SHA-256 `b1a4837d1d255c14eb2c0e55c14c55ce426c7d18236e2b27283c1b594d5455a0`, with 107 rows, 102 current claim citations, zero hash drift, and unchanged disposition totals (40 existing App obligations, 28 mechanism evidence, 23 external Runtime-owned, 9 legacy/retired/non-MVP, 4 Root-instruction-owned, 3 accepted App carrier repairs). Independently, I replaced only the three register-hash values in an in-memory copy with the prior value and serialized it; the reconstructed bytes hash to the previously reviewed map SHA `2224ca155853003c57e6ac36b6c330201549afaa3a964fd8e7670dffe1be898b`. This confirms all 107 IDs, classifications, the 102 claim-key associations, their citations, and all other map content are unchanged from the reviewed bytes. No source or map edit was made in this recheck.
