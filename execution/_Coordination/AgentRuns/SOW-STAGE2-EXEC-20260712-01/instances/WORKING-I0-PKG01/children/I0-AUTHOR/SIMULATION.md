# Apply / target / rollback simulation

Verdict: `PASS`.

- Target preimage reproduced exact legacy-only `LEGACY_FOUR_DOC` and all five frozen hashes.
- Applying the exact five replacement rows produced single-format `SOW_V1`; validator returned valid with no issues; `_STATUS.md` remained exact ISSUED bytes.
- The applied `ScopeOfWork.md` hash was exactly `23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21`.
- Applying the exact inverse rows restored single-format `LEGACY_FOUR_DOC`; all four source files and `_STATUS.md` were byte-identical to the frozen preimage.
- This disposable simulation is evidence only. No live target or Git state was changed.
