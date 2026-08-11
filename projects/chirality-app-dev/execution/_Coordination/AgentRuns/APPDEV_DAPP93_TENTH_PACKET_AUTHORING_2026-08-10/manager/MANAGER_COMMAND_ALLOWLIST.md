# Frozen manager command contract — tenth lineage

Status: `SEALED BEFORE CHILD DISPATCH`

Every manager command is logged in `MANAGER_COMMAND_LOG.csv`. Exact paths may
be substituted only where the form says `{ALLOWLISTED}` or `{TENTH}`; those
placeholders mean one exact path in `MANAGER_READ_ALLOWLIST.txt` or under the
tenth run root. No broad `AgentRuns` operand, glob, `find`, or recursive search
outside the tenth root is valid.

| Form | Exact executable/operation | Frozen use |
|---|---|---|
| BBOOT | read-only bootstrap | exact git status/rev-parse and tool-resolution commands run before sealing, individually logged |
| B01 | `apply_patch` | exact named files under tenth root only |
| B02 | `/opt/homebrew/Cellar/git/2.55.0/bin/git status --short --branch` | branch state |
| B03 | `/opt/homebrew/Cellar/git/2.55.0/bin/git rev-parse HEAD` or `... origin/main` | exact base |
| B04 | `/usr/bin/shasum -a 256 "{ALLOWLISTED_OR_TENTH}"` | one exact file |
| B05 | `/bin/cat "{ALLOWLISTED_OR_TENTH}"` | one exact whole file |
| B06 | `/bin/test -f|-x|-r "{ALLOWLISTED_OR_TENTH_OR_PINNED_BINARY}"` | one exact gate |
| B07 | `/usr/bin/stat -f '%z' "{ALLOWLISTED_OR_TENTH_OR_PINNED_BINARY}"` | BSD byte count |
| B08 | `/usr/bin/wc -c "{TENTH}"` | one exact tenth file |
| B09 | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg -n -e <full-historical-pattern> "{ONE_TENTH_CHILD_FILE}"` | zero-ID scan only |
| B10 | `/bin/zsh -n "{ONE_TENTH_ZSH_STUB}"` | syntax only |
| B11 | `/usr/bin/env -i ... /bin/zsh --no-rcs "{ONE_TENTH_PROBE_SCRIPT}"` | exact restricted probe |
| B12 | `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13 "{TENTH}/manager/MANAGER_VALIDATION.py" <preflight|census|fanin|log-audit>` | deterministic tenth-only validation |
| B13 | `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` | receipt contract |
| B14 | `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13 execution/_Reconciliation/References/reconcile_authority_corpus.py status` from App root | corpus status |
| B15 | `/opt/homebrew/Cellar/git/2.55.0/bin/git diff --check` | diff hygiene |
| B16 | `(cd "{TENTH}" && /usr/bin/shasum -a 256 -c FINAL_INVENTORY.sha256)` | inventory verify |
| B17 | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg -n -F 'Receipt-157' projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` | exact receipt-cursor check only |

Pinned manager chains:

- Python symlink and real binary:
  `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` ->
  `python3.13`, both bytes SHA-256
  `1a2e543a5426f665b9f321d391995b46e985fbea8df2a5bea86d7210c603460a`.
- Git symlink `/opt/homebrew/bin/git` ->
  `/opt/homebrew/Cellar/git/2.55.0/bin/git`, both bytes SHA-256
  `5f0351f649aa1321345229d5256fc8043517778b134a3b4571ecdc3818f124b2`.
- rg real binary SHA-256
  `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423`.
- `shasum -> /usr/bin/perl` pins
  `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` /
  `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd`.
- cat/test/stat/wc/zsh/env/printf retain their catalog pins.
