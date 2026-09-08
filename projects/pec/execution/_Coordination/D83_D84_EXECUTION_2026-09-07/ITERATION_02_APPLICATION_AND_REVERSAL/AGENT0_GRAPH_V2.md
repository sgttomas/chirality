# HELP_HUMAN execution graph v2

| Node | Role | State | Responsibility and gate |
|---|---|---|---|
| `/root` | HELP_HUMAN Agent 0 | active, read-only supervisor | Observe both managers, validate fan-in, release later scanner work, and route CHANGE. |
| `/root/pec_session_authority` | RECONCILIATION Agent 1 | active common recorder | Maintain this additive graph/basis, validate relayed returns, append Receipt 174, seal and hand off; no production writes. |
| `/root/pec_d83_application` | RECONCILIATION Agent 1 | terminal validated fan-in accepted; writers stopped | Applied exact 57 ordinary entries / 89 items and completed R5 evidence/backcheck; frozen DEL-01-05 excluded. Actual `/root/pec_d83_application/d83_author` and `/root/pec_d83_application/d83_verifier` details and seals are bound in `ACTUAL_RETURNS/D83_APPLICATION.md`. |
| `/root/pec_d84_reversal` | REVIEW Agent 1 | terminal validated fan-in accepted; writers stopped | Recorded exact one-status D84 L administrative reversal and independent verification; no promotion or acceptance. Actual `/root/pec_d84_reversal/d84_l_verifier` PASS and manager seals are bound in `ACTUAL_RETURNS/D84_L_REVERSAL.md`. |
| `/root/pec_d84_repair` | WORKING_ITEMS Agent 1 | prepared, source held through Iteration 02 closeout | Read-only preparation complete; both prerequisites now validate, but source production remains a later iteration after parent release. |
| `/root/pec_change_sol` | CHANGE Agent 1 | released after common seal | Verify and commit/push this one iteration under standing authority; no repeat approval needed. |

All listed Agent 1 managers were parent-configured as `gpt-5.6-sol` with
`medium` reasoning. This is requested/configured allocation evidence, not a
claim about an unexposed serving identity. No production Agent 2 was launched
by common integration. The D83 and D84 managers' actual specialists are
recorded in their own sealed dispatch records. Manager-owned validation remains with each manager;
common integration performs only exact fan-in and containment checks.

Dependencies: D83 ordinary application and D84 reversal share only the merged
authority basis and have disjoint write scopes, so they execute concurrently.
D84 scanner source repair depends on the validated reversal and on clean fan-in
with the D83 iteration; it remains held for the next iteration on this branch.
