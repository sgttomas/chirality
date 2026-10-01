# Additive availability observation for unselected A1 options

This note uses only the already sealed clean B01 output. No new case, arithmetic
experiment, solver run or repair was performed for it. It supplements the
unselected closure draft in DESIGN/continuation_05 without rewriting that seal.

Source: `Run/instances/A1-DIAGNOSIS/continuation_03/cases/B01/guard-workload.log`,
lines 47 and 127–141, where Run is the current audit-response run folder.
The existing exact comparator found every B01 force truth to be zero and every
published row honest.

The recorded pair is p128/P256. Its publication has

    S_pub(force) = 0                (bits 0000000000000000)
    E_force      = h = 2^-1074      (bits 0000000000000001).

The unchanged verification rule has
`e_hat_force = max(E_force, RN64(E_moment/L)) >= h`, so its force-row
resolution allowance `V_force=2^(8-256) e_hat_force` is strictly positive in
retained/exact-sum arithmetic. It must not be rounded to a binary64 zero in
this reasoning. The recorded force stop-rule summary is likewise nonzero.

Therefore applying draft P or C's covered-row `X<=S_pub` cap to this preserved
candidate/verification pair would require a positive numerator to be <=0.
It would reject the pair even though its published force zeros are honest.
This is a direct consequence of the proposed rule and observed E/S bits, not
an observed execution of a repair.

The draft's zero-scale proof remains a sufficient honesty argument; this
observation makes one availability cost concrete. It does not establish the
later selected precision or whether the case would select at all. The existing
p512 Phi floor may supply a nonzero scale then, but that state's complete
checks have not been exercised under P/C. No alternate error split, structural-
zero exemption or constant change is selected to preserve p128.

Carry this pair into the eventual comparison of P/C/U, work/precision/cache
effects and protected availability commitments. A changed honest case is not
automatically a human checkpoint, but its actual contract/retirement effects
must be assessed under the decision boundary. U's changed published scale is
still an explicit contract alternative, not a selected workaround.
