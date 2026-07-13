# C1 Exact Canon Candidate Receipt

Status: `PASS`
Basis: `main@c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`; accepted `P0_BASIS` / `B0_PASS`; D-GOV-16 ruling `7584718aa32b112e415331736d1a8e68c12ac176`.

The ruled successor-standard bytes were copied exactly. Candidate `TYPES.md` and `SPEC.md` are the live-basis bytes with only the ruled zero-context patches applied. Live patch preflight passed for both patches, the standard compares byte-identical to its ruled source, and both patched candidates compare byte-identical to independently reproduced patch output.

An intermediate edit-adapter placement discrepancy in the two pure-insertion hunks was detected by independent comparison inside the isolated candidate, corrected to the ruled hunk positions using the ruled text, and all checks were rerun successfully. No ruled byte was altered and no live file was touched.

Exact C1 writes are the three candidate docs, this receipt, `MANIFEST.tsv`, `HANDOFF_STATE.md`, and `instances/HELPS-C1/{RETURN.md,STATUS.json}`. There were no interpretation edits, extra candidate paths, live canon edits, project edits, Git-ref actions, commits, remotes, or receipts outside the declared targets.

Live before/after SHA-256 values remain: standard `8409bf3cebb3af947f54cca9d2e1c0b62445041bf72b81bd8aef912ce9fc0013`; TYPES `6b17e67e42116abe9753391f54d39565c94ab90395f91d537f41ee21a1241d45`; SPEC `4cb7e341dcfd1d8f963a743989a2ae9371faa3a8cd9e04cad66e3cb10c9d6a8b`.
