# Manifest regeneration attempt 2 failure

The first remediation command used `path` as its loop variable under `zsh`,
shadowing the shell's special command-search path. Hash and byte-count
utilities consequently resolved as unavailable, and the produced manifest was
invalid. Reason code: `MANIFEST_REGEN_PATH_SHADOW`.

No candidate or live/project file was touched. The invalid manifest was not
accepted. The next attempt uses a non-special loop variable, explicit utility
paths, regenerates the manifest from finalized evidence, and verifies every
row before return.
