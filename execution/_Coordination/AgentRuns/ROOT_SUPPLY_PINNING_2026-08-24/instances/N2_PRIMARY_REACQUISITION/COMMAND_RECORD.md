# Command Record — N2 Primary Reacquisition and Inventory

All commands were run from the Root repository unless an absolute path is
shown. No command executed the vendor binary.

1. Read the sealed brief, `AGENTS.md`, all six cumulative supply instruments,
   and N1 `RETURN.md`; verified the N1 return SHA-256
   `3b37a25b50254ecedce1871e59515ce53c8de7e42f24cc9dca97e71853cfae20`.
2. Created a unique external quarantine with
   `mktemp -d /private/tmp/chirality-root-supply-r14-primary.XXXXXX`, producing
   `/private/tmp/chirality-root-supply-r14-primary.lTtHP2`.
3. Downloaded the exact primary canonical URL once with `curl --fail
   --location --proto '=https' --tlsv1.2` into the quarantine. Curl exited
   zero. No ephemeral signed redirect URL is persisted.
4. Immediately ran `stat -f '%z %N'`, `shasum -a 256`, `file`, `tar -tzvf`,
   and `git ls-files --error-unmatch` on the archive. Required the ruled
   `71843308`-byte and `35892a…2032` identities before extraction. The archive
   was external and untracked.
5. After the archive gate passed, extracted its sole member into an isolated
   quarantine subdirectory with `tar -xzf`. Ran `stat`, `shasum`, `file`,
   `lipo -archs`, `otool -hv`, and `otool -l`; required the ruled contained
   SHA-256 `b1d1a8…de2` and arm64 platform identity.
6. Performed static signature inspection only with `codesign -d --verbose=4`,
   `codesign --verify --deep --strict --verbose=4`, `codesign -d
   --entitlements :-`, `spctl --assess --type execute --verbose=4`, and
   `otool -l`. Compared every relevant field to R13's admitted defect class.
7. Retrieved the exact-tag `LICENSE`, `NOTICE`, and repository-root metadata
   from official `openai/codex` URLs into quarantine. Verified their byte
   sizes, SHA-256 identities, and Git blob identities. These supporting texts
   are not substitute artifacts. No equivalence asset was downloaded by N2.
8. Confirmed the primary archive has no `LICENSE`, `NOTICE`, or `COPYING`
   member and recorded the applicable Apache-2.0 Section 4 packaging duties.
9. Wrote repository evidence only through `apply_patch`; retained the external
   quarantine intact for N2b/N3.

The primary vendor executable was not run. No live `CODEX_HOME`, PATH,
launchd, daemon, pin, manifest, or runtime configuration was touched.
