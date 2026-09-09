# G4 manifest declaration correction

Status: **READY FOR REVIEW**

The current Chirality v3 adoption tranche manifest now declares `.github/workflows/harness-premerge.yml`, the sole instruction-surface path omitted from the full PR range. Existing M2 authorization, merge gate, M6 routing, and all other declared paths are unchanged.

The exact CI-form command over `c16812685831a1cae3d44bf478d08b033c605c3a..HEAD` passes with 421 changed paths, 74 instruction-surface paths, and one added manifest. The G4 validator suite passes 48/48; whitespace validation and `git diff --check` pass. Export-manifest row rebinding is separately owned.
