# Decision log

| Gate | Disposition | Evidence |
| --- | --- | --- |
| Gate 1 | Narrow semantic intent previously approved | owner ruling quoted in `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md` |
| Gate 2 | ACCEPTED | owner response “Approve exact Runtime application”; exact subject `scope/DECISION_SUBJECT.md` SHA256 `3be40d62ada16bb7d2588c948904c0a6ec9fb5f83d64c15e6c40dbdaaeffcaf1` |
| Gate 3 | APPROVED | exact patch SHA256 `4be28f9e5929765c8666908e8895ffa2a8d75d2f0df66c133e1b383ee1e94395`; independent prospective review PASS |
| Gate 4 | APPROVED | propagation draft SHA256 `f81bfeb89c2846b23f5b894969838cd797e27a178d87e286c65d90a32ef8ccfd`; action draft SHA256 `3685b15ccadae3beb2e308e49f3bd637ad7c0a1ee4137c0f735e1b5c3cd93c7a` |
| Gate 5 application | EXECUTED; VALIDATION IN PROGRESS | exact three canonical postimage hashes recorded in `Application_Journal.json` |
| Gate 5 poststate acceptance | PENDING | requires independent actual-poststate audit and owner confirmation |

The exact approved candidate text retains `PROSPECTIVE / NOT EFFECTIVE` and ledger `GATE3_REVIEW_NOT_ACCEPTED`. Those labels described candidate/effect state when authored. Gate 3 approval is now separately and durably recorded above. `PROSPECTIVE / NOT EFFECTIVE` remains materially correct before Runtime publication/main identity and required Root successor adoption. The ledger candidate label is stale current-facing metadata after actual Gate 3 approval; it was preserved to honor the exact approved patch and must not be read to erase the recorded owner act. Whether it requires a separately approved exact metadata postimage before canonical closure is a Gate 5 finding, not silently repaired here.

