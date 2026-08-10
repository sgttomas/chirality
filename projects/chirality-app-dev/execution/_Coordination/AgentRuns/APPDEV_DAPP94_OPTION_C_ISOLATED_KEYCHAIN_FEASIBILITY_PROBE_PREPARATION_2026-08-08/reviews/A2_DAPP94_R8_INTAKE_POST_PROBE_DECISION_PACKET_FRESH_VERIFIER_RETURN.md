# D-APP-94 R8 intake/post-probe decision-packet fresh-verifier return

Verdict: `PASS_DAPP94_R8_INTAKE_POST_PROBE_DECISION_READY`

## Independent verification

- Initial and final read-only hash checks were stable and reproduced the frozen identities exactly:
  - candidate freeze: `3e389f544650b9fc95252b429c3fe87c1294ce71d9fe42cd645c29a74a6cf9d2`
  - intake manifest: `3f8a5aa2accb6179946fb4eee3c4a3ef2a26e05769ee3b271d1c56342bbb2202`
  - feasibility result: `5a2240499c80896f224bce03b6c0b8a7cdd557c6cfea1035f7a8a88b40de50b1`
  - post-probe decision packet: `e610f2c7a79097dc57348bffd17226ce83e316d9f4cac759e0884abe4c4f3c9b`
  - decision register: `fc7e8d812329b4bc9020a7bf2437bc11f6550bde41ba98527ebbb6b61fd3645e`
  - static validation: `5a80f61352bfac46c35e810d3fb9868c5811bcc0329df412b4095566db6666eb`
- `returned_r8/` contains exactly 134 files. The intake contains exactly 134 evidence files after excluding its two derivative Markdown controls. Same-named source and intake evidence are `134/134` byte-identical, with no missing, extra, or mismatched evidence object.
- Independent filename classification produced exactly 67 primaries and 67 true adjacent sidecars. All `67/67` sidecars validate both their adjacent-primary reference and SHA-256. The only primary names ending in `.sha256.txt` are `electron-archive.sha256.txt`, `electron-executable.sha256.txt`, and `probe-script.sha256.txt`; each has and validates its true double-extension `.sha256.txt.sha256.txt` sidecar.
- The manifest contains exactly 134 unique evidence rows. Every declared filename, byte count, and digest matches the intake evidence; no evidence file is unlisted.
- The primary evidence exactly supports the derived facts: prompt `NONE`; one-element synthesized default and search list at the exact R8 login-keychain path; Electron `43.2.0`; Chrome `150.0.7871.129`; `darwin`; encryption available and round trip both true; ciphertext length 51; public-constant hash `a85a62ad9d0e893fa7d85d110384baabdc11f7167dbf605978f498920e6a696f`; owner state `OWNER_STATE_MATCH_NO_BACKSTOP_WRITE`; backstop `NOT_NEEDED`; PASS committed before destructive cleanup; cleanup complete; and recorded R8-root absence status 0. A separate intake-time read-only check also found the fixed R8 temp root absent.
- The post-probe packet is neutral (`NO OPTION SELECTED`), presents exactly Options A/B/C, and supports its recommendation of Option A from the bounded feasibility evidence without converting that evidence into reliance or acceptance. Its three exact owner tokens match their respective options, remain preparation/planning dispositions only, and explicitly grant no attempt-3 authority.
- The decision register contains exactly one D-APP-94 row. It is in `AWAITING_FINAL_POSTURE_RULING`, preserves the historical rejection of unsupported `--password-store=basic` and the historical Option C probe-preparation ruling, and records no final posture selection.
- The packet keeps the product-byte patch route rejected and out of scope. No attempt-3 command, execution token, C1118 authority, reliance, product acceptance, runtime/security/keychain/credential/Electron action, product/package/trace action, Git action, Task Management action, or foreign-loop authority was issued or inferred.

No repair or operational action was performed. This return is verification evidence only and grants no execution or reliance authority.
