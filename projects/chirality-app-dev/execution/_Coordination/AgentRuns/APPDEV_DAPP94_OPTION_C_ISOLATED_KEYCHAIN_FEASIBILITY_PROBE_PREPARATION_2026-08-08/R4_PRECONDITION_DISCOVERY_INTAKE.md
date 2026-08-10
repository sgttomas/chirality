# R4 precondition-discovery intake manifest and terminal verdict

Status: `VALIDATED_PRECONDITION_DISCOVERY — STOP_BEFORE_SECURITY_MUTATION`

Source root, preserved in place:
`/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/evidence/`.

Derivative intake root:
`intake/r4_precondition_discovery/`.

Copy method: byte-for-byte `cp -p` into a previously absent derivative intake
directory. Every retained derivative object reproduced byte-identically by
`cmp` against its source. No source object was moved, deleted, overwritten,
or altered.

Object count: 22. Aggregate byte count: 486.

| File | Bytes | SHA-256 |
|---|---:|---|
| `host-arch.exit-status.txt` | 2 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `host-arch.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `host-arch.stdout.txt` | 6 | `c1669e1d8edca98769c37d494b76442a1d6e5ffffd7b4da1fb63aef8ebaf6f01` |
| `host-sw-vers.exit-status.txt` | 2 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `host-sw-vers.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `host-sw-vers.stdout.txt` | 63 | `46c87c2b8fd5d25040390e531128cd533d199bde1b50a51790375ab5984c99bb` |
| `host-uname.exit-status.txt` | 2 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `host-uname.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `host-uname.stdout.txt` | 148 | `990293563fff283b44d779e3b5722800dd9a27bf09db4d3e1b46a8f4c729582c` |
| `isolated-home-default.exit-status.txt` | 2 | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |
| `isolated-home-default.stderr.txt` | 84 | `c4cd2b8b78b5dde28b680c841bb0fcc418d84450cdd6c0bcab15f94a83e6ab56` |
| `isolated-home-default.stdout.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `isolated-home-search.exit-status.txt` | 2 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `isolated-home-search.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `isolated-home-search.stdout.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `pre-default.exit-status.txt` | 2 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `pre-default.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `pre-default.stdout.txt` | 54 | `99563436b11d637838e83d3750afbe806eeab9c8c29dc7d860704e2f1da43953` |
| `pre-search.exit-status.txt` | 2 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `pre-search.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `pre-search.stdout.txt` | 54 | `99563436b11d637838e83d3750afbe806eeab9c8c29dc7d860704e2f1da43953` |
| `terminal-status.txt` | 63 | `e8922561b820c66b94e435a6179c42e4d23c15a564821e6a9f7f4820ddc3555a` |

## Validated findings

- owner-domain pre-default and pre-search observations each exited zero and
  exactly match the accepted one-element baseline
  `/Users/ryan/Library/Keychains/login.keychain-db`;
- under the R4 isolated HOME, default observation exited `1`, emitted empty
  stdout, and emitted exactly
  `security: SecKeychainCopyDomainDefault user: A default keychain could not be found.\n`
  on stderr;
- under the same isolated HOME, search-list observation exited `0` with empty
  stdout and stderr;
- terminal status is exactly
  `FAILED_BEFORE_SECURITY_MUTATION:home-does-not-preserve-default\n`;
- frozen R4 command order places that terminal route before
  `MUTATED=1` and before every create/unlock/bind/probe/delete command;
- filesystem classification found the retained
  `home/Library/Keychains/` directory empty and the current `returned/`
  directory present and empty.

## Calibrated conclusion

On this exact host/session and captured R4 route, changing filesystem `HOME`
changed the user-domain default/search observations: the isolated HOME had no
default and an empty search list. This is precondition-discovery evidence for
the R5 design only; it is not a universal macOS claim.

## Terminal verdict

`VALIDATED_STOP_BEFORE_SECURITY_MUTATION`: the retained bytes support exit
`23`, `MUTATED=0`, no R4 keychain file, no owner-domain default/search
change, no Electron probe, and no cleanup. The retained R4 temp root and current
`returned/` are predecessor evidence and must remain untouched.
