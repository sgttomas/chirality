# Exact Runtime SCOPE_CHANGE decision subject

The narrow semantic boundary is already owner-approved. The next owner decision is the separate Runtime owning confirmation required by `agents/AGENT_SCOPE_CHANGE.md` Gate 2 (`Impact Assessment`, line 268; human confirmation at line 343), Gate 3 (`Amendment Approval`, line 347; formal confirmation at line 403), and Gate 4 (`Propagation Plan Approval`, line 407; confirmation at line 485).

## Exact subjects

- Gate 2: `IMPACT_AND_ORDERING_REFRESH.md` plus `PREIMAGE_AUDIT.json` and Root publication/sync identities recorded in author-v2/review-v2.
- Gate 3: `author-v2/CANDIDATE.patch`, SHA256 `4be28f9e5929765c8666908e8895ffa2a8d75d2f0df66c133e1b383ee1e94395`; author manifest SHA256 `54a94c193e0064ce2242c58dca2031959b8bca267593de90d2a9eed0574c005a`; final independent review verdict `PASS_DECISION_READY_PROSPECTIVE`, review manifest SHA256 `f56e83895059b7b138a6d3c046430d1a8a95d78e425339ceaae165b0ca641665`.
- Gate 4: `PROPAGATION_PLAN_DRAFT.md` and `AMENDMENT_ACTIONS_DRAFT.csv`. These accept planning and later handoffs only; no future SOW postimage is accepted.
- Application basis: Runtime HEAD and `origin/main` `e8cdc460cffccfe9e58ab4e5b9bbc05350c09327`; candidate targets do not drift from the verified preimages.

## Precise requested disposition

> I accept the Runtime narrow account-authority impact assessment at Gate 2; approve exact candidate patch SHA256 `4be28f9e5929765c8666908e8895ffa2a8d75d2f0df66c133e1b383ee1e94395` at Gate 3; and approve the Gate 4 propagation plan and draft action register, limited to the three canonical Runtime files and the stated later handoffs. Apply and validate this exact Runtime canonical amendment, create its new immutable SCA snapshot and update its active pointer under the SCOPE_CHANGE protocol. This does not approve future DEL-02-06/09 SOW bytes, source implementation, supplier or credential operations, protected fixtures, wire/recovery acceptance, lifecycle promotion, release, or any other held act.

After application and independent poststate audit, Gate 5 owner acceptance remains a new decision. CHANGE publication, exact Runtime commit capture, Root successor adoption and later SOW propagation remain sequential downstream acts.

