# W6 manager capture — N5-R2 fresh read-only return

- Runtime child: `/root/w1_del0206/n5_r2_w6`
- Runtime parent: `/root/w1_del0206`
- Launch brief SHA-256: `bdaf11fdec33efe8c87536431fbc1fc9775c79f98e568d0061a6ae3d976e7669`
- Governing brief SHA-256: `632d2cbefac9003f36d9d722374b22fdeca5d0da45e637acf7335c8a7d872121`
- Verdict: `RETURN`
- Coverage: `18/18` full and hash-exact; adversarial matrix `15 PASS / 1 FAIL`; writes/repair: none.
- Prior `N5-F01`: `PASS` — base hash, ten unique rows, nine columns, unresolved fields, positive/negative evidence, and preservation honesty all pass.

## Finding

- `N5-R2-F01` — `MATERIAL_SEMANTIC_REFERENCE_DEFECT`.
- Artifact: `integration/DEGRADED_MODE_DELTA_CANDIDATE.md`, line containing `remain D1/D6/D16 owner decisions.`
- Evidence: the accepted decision ledger defines only D1-D9; `D16` is nonexistent. The surrounding boundary and condition row 10 correctly identify D1-D9 and `TBD-016`.
- Impact: the candidate invents a decision identifier and is internally contradictory. N5-R2 may not infer or repair the intended exact reference.
- Disposition: exact correction by N4, updated self-check/return, then another genuinely fresh read-only N5 recheck.

All other adversarial dimensions pass. No write, repair, shell, network, executable check, runtime execution, delegation, Git, adoption, lifecycle, release, reliance, or foreign effect occurred.
