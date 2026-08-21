# Governed execution attribution matrix

## Runtime attribution boundary

Every governed role below ran through the **Codex desktop multi-agent runtime**
with provider **OpenAI** and model **GPT-5 family inherited from the parent**.
The harness did not expose an exact model or build identifier for these
sessions. No greater specificity is inferred. This limitation applies to every
row and is not replaced by role names, task names, or artifact counts.

| Durable / runtime identity | Role | Parent / substitution | Terminal disposition | Engine | Provider | Model |
|---|---|---|---|---|---|---|
| `/root` | HELP_HUMAN Agent 0 supervisor | human entry | supervising | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `WI-PKG09-LOGIN-PROOF-PREP-01` / `/root/pkg09_launchagent_proof_prep` | WORKING_ITEMS manager | Agent 0 initial manager | interrupted / replaced | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `WI-PKG09-LOGIN-PROOF-PREP-02` / `/root/pkg09_launchagent_proof_prep_r2` | WORKING_ITEMS manager | replacement for manager 01 | SUCCESS, terminal fan-in complete | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-01` / `/root/pkg09_launchagent_proof_prep/login_proof_impl` | implementation Agent 2 | manager 01 | interrupted, no product bytes | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-02` / `/root/pkg09_launchagent_proof_prep/login_proof_impl_retry` | implementation Agent 2 retry | replacement for implement 01 | interrupted, no accepted return | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-03` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_impl_r2` | implementation Agent 2 retry | manager 02 replacement attempt | interrupted, analysis only | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-DIRECT-01` / `/root/login_proof_direct_fix` | Agent 0 direct implementation Agent 2 | substituted for implement 03 | success intake, later remediated | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-01` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_review` | read-only reviewer Agent 2 | review of direct intake | FAIL, two P1 findings | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-01` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_remediate` | remediation Agent 2 | fixes review 01 | SUCCESS | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-02` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_rereview` | read-only reviewer Agent 2 | review after remediation 01 | FAIL, one P2 finding | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-02` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_remediate_p2` | remediation Agent 2 | fixes review 02 | SUCCESS | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-03` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_final_review` | read-only reviewer Agent 2 | review after remediation 02 | FAIL, one P1 finding | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-03` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_remediate_cleanup` | remediation Agent 2 | fixes review 03 | SUCCESS | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-PKG09-LOGIN-PROOF-PREP-REVIEW-04` / `/root/pkg09_launchagent_proof_prep_r2/login_proof_review04` | read-only reviewer Agent 2 | review after remediation 03 | PASS, zero findings | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-APPDEV-INTEGRATED-REVIEW-01` / `/root/pkg09_launchagent_proof_prep_r2/integrated_tranche_review` | read-only integrated reviewer Agent 2 | raced with direct reviewer | interrupted immediately, no verdict | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-APPDEV-INTEGRATED-REVIEW-DIRECT-01` / `/root/app_integrated_final_review` | Agent 0 direct read-only integrated reviewer Agent 2 | sole terminal integrated reviewer after duplicate interruption | FAIL, three record-only findings; zero product findings | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |
| `A2-APPDEV-INTEGRATED-REVIEW-DIRECT-02` / `/root/app_integrated_final_review` | Agent 0 direct read-only integrated backcheck Agent 2 | backcheck after amendment 10 remediation | PASS, zero actionable findings; three prior findings closed | Codex desktop multi-agent runtime | OpenAI | GPT-5 family inherited from parent; exact identifier unavailable |

Substitutions and interruptions above are provenance, not evidence of acceptance.
Terminal acceptance follows the work graph, checks, and valid reviewer returns.
