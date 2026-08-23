# Source, copy, and semantic checks

## Source safety gate

- Exact source directory: Directory, non-symlink, mode `0700`, UID `501`, GID `20`, size `160`, inode `51867392`.
- `prepared.json`: regular, non-symlink, mode `0600`, UID `501`, GID `20`, 1,248 bytes, inode `51867393`, SHA-256 `5961b2060b554dc12989947a45335422f48f9e953d5af60c2ece88f7fdcf0a88`.
- `summary.json`: regular, non-symlink, mode `0600`, UID `501`, GID `20`, 2,018 bytes, inode `51867394`, SHA-256 `38a603c470a51209b463a4657448794f8500cb32bfd5f83c2e6c611fb0aa06b1`.
- `evidence-package.json`: regular, non-symlink, mode `0600`, UID `501`, GID `20`, 398 bytes, inode `51867395`, SHA-256 `aa84cdf66753d229dc9b2d27d147bc892107f054266d62f1f4bdf261280a6405`.
- No Desktop enumeration or other Desktop path read occurred.

## Destination and byte identity

- Exact DEL destination: Directory, non-symlink, mode `0700`, UID `501`, GID `20`, size `160`, inode `51911009`.
- Copied files are regular, non-symlink, mode `0600`, UID `501`, GID `20`; destination inodes respectively `51911010`, `51911011`, `51911012`.
- All three source/destination pairs passed byte-for-byte `cmp` and retained the exact source sizes and SHA-256 values.

## Copied-public-JSON semantic gate

Deterministic `jq -e` checks passed the complete sealed matrix: schemas and statuses; exact source revision; direct package-executable binding; non-claiming preparation; all launch-agent/login-session/process assertions; complete non-refused cleanup with `passOnlyFailureLogCleanup=REMOVED`; all default-protection assertions; owner/harness proof boundary; exact evidence-package cross-hashes and two-file manifest.

Result: `PASS`, with no schema or semantic mismatch.

## Fence evidence

This executor did not read, stat, list, traverse, or otherwise query the private proof root. It did not query or touch `com.chirality.runtime`. It performed no proof, launchctl, GUI, operator, network, release, Git, frontend, package, procedure, receipt, or Task Management act.
