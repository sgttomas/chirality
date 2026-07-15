# VERIFY-B1 Frozen Basis Reproduction

Verdict: `PASS`

- Checkout and `origin/main`: `4d153302c3c4cd42578936db160c2bac1270225a`.
- Accepted W-P3 manifest: `P3_MANIFEST.tsv` SHA-256 `ffaa85110f530cedac5e3dd8866354be9a7d89079dc3cf758c715d275839f5f4`.
- Expected live bindings: `EXPECTED_LIVE_BINDINGS.tsv` SHA-256 `82cb784e9e676a3f4ece2e68341e8217fcf2e33160ba1b61559f395d4d6411b1`.
- Population: exactly `DEL-10-01..05` in numeric order; 5 members; 1,594 physical legacy-source lines.
- Live state: 5/5 `IN_PROGRESS`; 5/5 exact `LEGACY_FOUR_DOC`; 5/5 live `ScopeOfWork.md` absent; 45/45 live file hashes reproduce the accepted rows.
- Candidate state: 15/15 hashes reproduce the parent-accepted candidate family; no candidate write occurred.
- Accepted predecessor state, W-P3 release, references, and `main` ancestry were reread and remain PASS.
- PKG-00 direction: `PKG-10` has 28 active upstream-only rows covering five members and seven PKG-00 targets; frozen verdict remains PASS. No PKG-00 surface was written or treated as downstream authority.
- Active method/check bindings reproduce the W-P3 frozen hashes, including the SOW standard, seven deterministic SOW tools, four skill-contract files, Piping instructions, workflow profile, and project check profile.
- Tool-migration authority is exactly `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.

No blocker, waiver, unknown, authority expansion, or basis drift was found.
