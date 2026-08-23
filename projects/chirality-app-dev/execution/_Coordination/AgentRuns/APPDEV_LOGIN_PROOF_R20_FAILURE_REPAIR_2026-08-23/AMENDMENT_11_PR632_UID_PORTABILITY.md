# Amendment 11 — PR #632 UID and host-identity portability repair

- Accepted basis: clean branch `codex/app-login-proof-r20-repair`, HEAD `4a48aeaede2d050631006f8ff23fb11736752bef`, parent `74525fb6b34f614c114e59a1bf09d20102fc6aac`, frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`.
- Owner authority is the verbatim second CI-portability direction in `CHAT_TRANSCRIPTION.md`.
- Phase A is read-only: one Agent 2 freezes the exact UID dataflow and a complete one-pass host-entanglement inventory before any frontend write. It must not rerun the known failing CI or claim a local UID reproduction.
- Phase B is test-only: a serialized implementation Agent 2 derives semantically compared UID values from the real process, preserves deliberate mismatch cases, addresses every accepted inventory finding, and leaves product scripts and the R19 fixture byte-identical.
- The frontend candidate receives fresh source/evidence review before CHANGE creates the final frontend-touching commit. Build/restage is commit-gated.
- Later build/restage, suite, TM, review, governance, receipt, and publication phases remain serialized and subject to the owner's exact one-shot and hard-fence constraints.
