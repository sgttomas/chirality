# Manager preflight — evidence boundaries

## Basis

- Branch / HEAD: `codex/app-login-proof-r17-repair` /
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Initial porcelain and index: empty.
- Receipt validator: PASS before activation.
- Proposed future R18 root:
  `/private/tmp/ch-r18-91499728-51dd`, exact root length 33 UTF-8 bytes,
  independently absent and not a symlink; exact future control-socket path
  length 67 UTF-8 bytes with a 36-byte margin below the 103-byte maximum.

## Independent read-only observations

The manager inspected only the owner-preserved public failed-evidence
directory, exact proof-plist existence, exact proof-service absence, and the
private proof-root's existence bit. It did not print or copy file bodies and
did not enumerate or inspect the private root.

- Preserved directory: mode `0700`, six regular files, each mode `0600`.
- `prepared.json`: SHA-256
  `1416d6d162df551163dcc3f90c88d4519b2662d2ba903883e60ece0715fe1476`.
- `summary.json`: SHA-256
  `f2f912bc35652e1b877a1eefdf511f9658a88e7ab69051ec637deb260bcfd230`.
- `evidence-package.json`: SHA-256
  `d3bf7c4c261916e6de4507f5be1728839ba7676bb9494d31433d00945ff358a4`.
- `daemon.stdout.log`: SHA-256
  `cb8f06c1bc2fa8e696fd45c1ca9fe7462373b92177393f0e8560fe15d70ae83c`.
- `daemon.stderr.log`: SHA-256
  `6fa805d99101b2f8074600289050b960042892d6312ebda559f2163f199147bb`.
- `desktop-daemon.log`: SHA-256
  `1bab152fccad435db691bec70dc159521e1c6d94b5435b0cfdeb2fc1e98196a6`.
- Bounded filename/content scans reported zero forbidden private filenames and
  zero files matching capture-state schema, credential/token-name, private-key,
  or login-session digest-salt categories; no matching body was printed.
- Exact proof plist: absent.
- Exact proof service: `launchctl print` exit `113` with the exact expected
  two-line not-found result.
- Private proof root: present; no traversal, content read, write, or cleanup.
- R16 full control-socket path: 119 UTF-8 bytes.
- R13 hypothetical full control-socket path: 111 UTF-8 bytes.

Owner statements about capture exit, run count, cleanup residuals, and manual
bootout remain owner-attributed until independently supported by the preserved
public artifacts. No independent observation upgrades the failed proof.
