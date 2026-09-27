# Post-D-PEC-101 recheck (HELP_HUMAN, 2026-09-26)

Brief S2A's parallel-act clause: `D-PEC-101` (PR #976, merged as `ce934ac33`) landed before this act's PR. HELP_HUMAN merged `origin/main` `ce934ac33` into the act branch and reran, on that merged tree (`0be210ae3`):

| Check | Command | Result |
|---|---|---|
| 23 pinned files | hash each `PINNED` entry of `apply_s2p.py` against the merged tree | 23/23 unchanged |
| Quotes | `verify_s2p_quotes.py --tree . --gitdir . --prep <run root> --observation aca930622` | exit 0, `RESULT PASS 460/460` (`evidence/post_d101_recheck/q.out`) |
| State claims | `verify_s2p_state_claims.py --gitdir . --prep <run root>` | exit 0, `RESULT PASS 1280/1280` (`c.out`) |
| Sibling IDs | `check_sibling_ids.py <run root>` | exit 0, `RESULT PASS 92/92` (`s.out`) |
| Strict registers | `validate_decomposition_registers.py projects/pec/execution --strict` | exit 1, 0 ERROR, 26 XRG-013, 0 DRB-008 (`strict.out`); the two DRB-008 cleared with `D-PEC-101`'s folders; this act writes no register |

A first quote run passed the full observation SHA to `--observation`, which the script matches as literal text, so the 7 observation-naming checks failed as an invocation error; the rerun with the recorded short form passes. The seven contracts' statements that their `_CONTEXT.md`/`_REFERENCES.md` name revision 1.5 remain true as observations at `aca930622` (they are re-pinned to 1.6 by `D-PEC-101` K4).
