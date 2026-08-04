# E3 independent-refuter return

Status: `COMPLETE / BLOCK`

The exact-bound packet was refuted. `REFUTATION.md` records two blockers and
three review findings:

1. G1/G3 conflict with the supposedly fixed 2,500 ms termination consequence.
2. Restart recovery after an interruption failure with otherwise successful
   cleanup has no defined state transition or retry operation.
3. The exact 500 ms force-settle cap lacks explicit policy/evidence calibration.
4. The start-during-start normative rule is missing from the implementation/test
   map despite a current source race.
5. The pre-identity interruption latch lacks a post-force/generation terminal
   rule and matching tests.

All twelve dispatch hashes matched. The recommended close/C1/F1 implementation
shape, evidence distinctions, bounded source/test authorization, implementation
hold, and conditional App-notice hold otherwise survived attempted refutation.

Required disposition: `RETURN FOR REVISION / DO NOT IMPLEMENT`. Repair the two
BLOCK findings, address the REVIEW findings, regenerate affected drafts, and
redispatch E3 against new hashes.

Writes were confined to this instance's `REFUTATION.md` and `RETURN.md`. No
manager draft, source, test, contract, register, App content, lifecycle, or Git
state was modified.
