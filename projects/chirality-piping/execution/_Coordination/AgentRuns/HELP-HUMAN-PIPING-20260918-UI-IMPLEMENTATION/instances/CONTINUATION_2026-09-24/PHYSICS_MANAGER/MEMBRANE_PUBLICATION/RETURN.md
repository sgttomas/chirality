# PHYS-R4 publication repair

Both actual public solver modes now reproduce the independent Fraction expression case with an admitted length of 1m. The interrupted predecessor attempt used L=1e-77m and stopped at PIPE_ELEMENT_INPUT_INVALID, so it remains failed admission evidence rather than a public stress proof. red-02.log reports solved mechanics, wall=4.94065645841246544e-324N and old membrane/headline=5.24219931650160766e-171Pa against the frozen independent reference 3.13333333333333371e-171Pa.

The facade publishes the already computed membrane and passes retained mechanical/thermal actions into the exact maximum. Each axial constant is recovered through the same SourceAnnulus constitutive helper before wall-force projection; constant pressure leaves the distributed axial slope and nonaxial statics unchanged. Pressure-free exact members keep their prior branch. Shared annulus/helper and scalar arithmetic bytes are unchanged. green-01.log passes both modes with membrane/headline=3.13333333333333325e-171Pa at unchanged relative1e-9.

PHYS_R4.delta.patch and REPAIR_BINDING.json bind the two changed source/test paths against F03 without copying the source forest. Independent review, affected public tests, pending regression disposition integration/full suite, consumer/native joins and ROOT merge gates remain open. These arithmetic-range inputs do not claim material fitness or engineering validity.

## Affected public check

After independent source backcheck reported PHYS-R4 closure, ROOT released the bounded test lane. Actual affected-public-01 execution passes36/36: pressure14, source geometry/near9, membrane2, elastic2, coverage/ties4, signed reactions/springs4 and grouping guard1. Exact command, compiler versions, before/after source hashes and raw log are retained. No test criterion changed. Lane returned to NUM. Full product library has not been rerun or cleared by this check.
