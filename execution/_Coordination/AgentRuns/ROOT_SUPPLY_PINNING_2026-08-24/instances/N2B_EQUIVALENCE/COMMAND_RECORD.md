# Command Record — N2b Exact Packaging Equivalence

All repository-relative commands were run from the Root checkout. No
downloaded or extracted vendor binary was executed.

1. Read the sealed brief, `AGENTS.md`, all R12–R14 instruments, and the N1/N2
   returns; independently reverified the retained primary quarantine.
2. Created external quarantine
   `/private/tmp/chirality-root-supply-r14-equivalence.BmK7x0` and downloaded
   only the R13-named zstd and package assets from the exact official
   `openai/codex@rust-v0.149.0` URLs using `curl --fail --location --proto
   '=https' --tlsv1.2`.
3. Immediately required exact `stat -f '%z'` byte sizes and `shasum -a 256`
   identities before extraction.
4. Decompressed the zstd asset with the workspace-bundled system utility
   `/Users/ryan/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/zstd`
   and extracted the package with `tar -xzf`. Neither operation invokes
   vendor code from the pinned assets.
5. Used `file`, `lipo -archs`, `stat`, `shasum -a 256`, and `cmp -s` to
   compare both alternate app servers to the N2 primary. Required identity
   and all three comparisons passed.
6. Used `tar -tzvf`, `find`, `stat`, `shasum`, `file`, and `lipo` to inventory
   every package member and freeze all executable SHA-256 identities for N3.
7. Performed static `codesign --verify --deep --strict`, signature display,
   entitlements inspection, and `spctl --assess` on the alternate app servers
   and ancillary Mach-O members. No member was invoked.
8. Wrote only the N2b instance and candidate `02B_EQUIVALENCE/` evidence via
   `apply_patch`. Both external quarantines remain intact for N3.

Ephemeral signed redirect URLs were not copied into governed evidence.
