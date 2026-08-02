# Fresh Adversarial Agent-2 Return

Execution contract: sealed evidence only; no tools, Bash, filesystem access,
write, edit, network, native Pi tools, or delegation.

Verdict: `PASS`.

1. C01-C18 exactly once: `PASS`.
2. Allowed dispositions/counts: `PASS` — 13 remove, 3 restate, 2 no change.
3. Every non-no-change row supported: `PASS` — all 16 are covered by the
   107-row conjunct ledger and current validation evidence.
4. Unknowns preserved: `PASS` — all six D-APP-81 UNKNOWN relations remain
   untouched.
5. Replacement exactness: `PASS` — C04, C06, and C16 exact bytes and hashes
   are specified; all three are no broader than their original claims.
6. Excluded/out-of-scope preservation: `PASS` — all 30 noncandidate blocks and
   named siblings match their recorded hashes.
7. Gate-2 stop/no target writes: `PASS` — only derivative run-root artifacts
   are new.

No overclaim was found. Unsupported packaged-executable, concurrency,
model-drain recovery, and PEC-registration limitations remain explicit. The
package is fit to stop at Gate 2.
