# Bounded v2 implementation clarification

Parent proposes an isolated v2 implementation tranche: all new v2 consequential entry points enforce accepted guards; legacy v1 cannot reach the new delegated service through an unchecked bypass. Existing v1 regression behavior is preserved, but v1 is expressly NOT claimed root-runtime-1-conformant. Its admission/client adoption/conformance obligations remain named incomplete work before full contract or release acceptance.

N4's statement that additive isolation does not excuse missing shared entry-point guards prohibits an implicit semantic exception or false full-conformance claim. It does not prohibit a bounded implementation that truthfully records unimplemented legacy obligations. This clarification selects no new semantic contract and retires no hold; fresh N5 reviews the distinction before manager fan-in acceptance.
