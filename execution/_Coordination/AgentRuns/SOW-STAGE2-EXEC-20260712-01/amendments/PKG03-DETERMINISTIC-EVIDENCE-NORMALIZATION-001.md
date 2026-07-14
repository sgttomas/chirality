# PKG-03 Deterministic Evidence Normalization 001

Recorded: `2026-07-14`
Authority: explicit human direction in the active root loop
Status: `ACTIVE`

## Human direction

Obvious deterministic fixes must not stop the loop; fix this class every time.
For the exact PKG-03 blocked evidence state, preserve the pre-normalization
bytes in branch history, then deterministically normalize the exact 56
EOF-warning files, regenerate and rebind every directly or transitively
affected manifest/snapshot/return hash and byte count, prove that no semantic,
project, or candidate content changed, rerun every required check, and continue
through PR, required CI, merge, and postmerge binding.

## Authorized repair

The preserved pre-normalization commit is
`ce4ea40f2c290eb41b6f9cd29f49d0f54d74a5ca`. Its warning inventory is
`instances/CHANGE-P1-PKG03/IMMUTABLE_WHITESPACE_WARNINGS.txt` and names exactly
56 files, each with exactly one `new blank line at EOF` finding.

For each named file, remove exactly one terminal LF only after proving its
pre-normalization bytes end in two LFs. Preserve every other byte. Rebuild the
four child manifests, the package manifest, the RECON manifest, prior
reconciliation manifest and copied prior manifest, upstream audit tables,
source bindings, accepted snapshot manifest, and all direct narrative/hash
consumers. Retain before/after hashes and the proof that every normalized file
equals its historical bytes minus exactly one final LF.

## Unchanged fences

This is a deterministic evidence-format repair. It does not authorize any
candidate, project, lifecycle, dependency, control, PKG-00, `DEL-01-01`, H1,
H2, release, retirement, or semantic change. The eight atomic project commits
remain unchanged. Merge remains conditional on every required check passing
on the exact final remote head.
