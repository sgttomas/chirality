# ROOT RULING RECORD R13 — supply-tranche resumption after the upstream signing defect — owner ruling of 2026-08-24

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: disposition of the fail-closed stop at the supply tranche's N2 signature gate and authorization to resume with an amended signature gate, an equivalence check across exact-version packagings, and a recorded G5 implication. Target workspace: Root loop under its own instruments. Companion instrument: the resume steer (`chirality_app_v3_supply_resume_steer_root_2026-08-24.md`; SHA-256 recorded in the PR that published this record — the files merged together). Prior instruments: R12 (`plans/steers/chirality_app_v3_root_ruling_record_r12_2026-08-24.md`, SHA-256 `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd`) and the supply-pinning steer (`plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md`, SHA-256 `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`), which remains in force except as amended here.

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-24. "[click]" marks the option the owner selected.

## The stop, and its verification

The Root loop stopped fail-closed at N2's signature gate and reported: asset
`codex-app-server-aarch64-apple-darwin.tar.gz` from the official
`openai/codex` `rust-v0.149.0` release, size `71843308` and SHA-256
`35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` both
exact against the channel; extracted arm64 Mach-O SHA-256
`b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`;
embedded signature Team ID `2DC432GLL2` with hardened runtime;
`codesign --verify --deep --strict` failing twice on byte-identical
extractions with `invalid signature (code or signature have been modified)`;
an invalid entitlements blob; `spctl` exit `1`. The binary was never
executed; quarantine was deleted; no receipt, commit, push, or PR was
created. The stop was a compliant execution of the steer.

HELP_HUMAN independently verified: (1) the official release's own asset
metadata publishes exactly that name, size, and digest; (2) upstream issue
`openai/codex#37725` (open since 2026-08-09, spanning release 0.147.0,
unfixed through 0.149.0) documents the identical failure class on
checksum-verified canonical release bytes — same Team ID, same
`codesign --strict` message, same invalid-entitlements warning, same
`spctl` failure — byte-identical across the GitHub release and npm
packagings of the codex CLI, and plausibly attributable to the release
pipeline's notarization change in upstream PR #37154. The defect is a
documented property of the official channel, not evidence of tampering, and
publicly observed execution of these artifacts indicates the kernel-enforced
signature layer still admits them.

R13-A — Resume with equivalence check and amended signature gate: [click]
"Equivalence check, then proceed".
  The owner authorizes resuming the supply tranche as follows.

  1. **Equivalence check (new, before execution).** Under the R12-A download
     terms, additionally download from the same official release, digest-
     pinned by the channel's own metadata:
     - `codex-app-server-aarch64-apple-darwin.zst`, size `50359498`, SHA-256
       `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677`;
     - `codex-app-server-package-aarch64-apple-darwin.tar.gz`, size
       `93775517`, SHA-256
       `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2`.
     Extract each in quarantine and compare the contained arm64 app-server
     Mach-O byte-for-byte against `b1d1a8c3…`, recording equality and each
     packaging's own signature-verification result. If any contained
     app-server binary differs from `b1d1a8c3…`, stop and report — the
     channel-property conclusion would no longer hold.
  2. **Amended signature gate.** A strict-codesign failure on digest-exact
     bytes that matches the documented defect class — Team ID `2DC432GLL2`,
     `invalid signature (code or signature have been modified)`, invalid
     entitlements blob, `spctl` failure — is recorded as supply inventory
     with citation to `openai/codex#37725` and is **not** a stop condition.
     Every other signature, identity, version, or license disagreement
     remains fail-closed exactly as R12 and the supply steer direct.
  3. **Proceed.** N3 bounded empirical execution and N4 candidate assembly
     then proceed under the original steer's containment terms, unchanged.
     If macOS refuses to execute the binary, the loop stops and reports;
     that outcome is compliant.

R13-B — G5 implication recorded in the tranche: [click] "Record in the
resumed tranche".
  The tranche's evidence and the N4 candidate must record, as a named open
  finding for the preparation lane: the release plan fails G5 on "an
  invalid nested signature", and the 0.149.0 app-server vendor signature is
  invalid as published; unless upstream corrects the pipeline, G5 planning
  must either receive a corrected artifact or an owner ruling on how the
  preparation lane treats the documented vendor-signature defect. Citation:
  `openai/codex#37725` and this record.

## Boundary of this authorization

Everything R12 and the supply steer withheld remains withheld: no pin
amendment, no G2 acceptance (the owner rules on the returned candidate with
the signature finding in full view), no implementation, cutover, release,
publication, or reliance authority. The amended gate admits exactly the one
documented defect class and nothing else. TM-ROOT-106/122 and every other
blocker remain as they are.

Not ruled here: G2 supply-unit acceptance; the preparation-lane treatment of
the vendor-signature defect (a later owner ruling at or before G5); any
upstream communication (filing or commenting on OpenAI issues is a separate
owner act); any later gate.
