# Git whitespace-attribute closeout backcheck

Date: `2026-08-09`

Scope:
`APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06/**`

The repository candidate-whitespace validator identified horizontal
whitespace and terminal blank lines in accepted raw transcripts/output
captures and in earlier frozen control objects. Those bytes are bound by
adjacent SHA-256 sidecars, intake manifests, freeze records, and accepted
verifier returns. Normalizing them during Git closeout would corrupt the
accepted evidence identities.

Closeout therefore adds one path-contained `.gitattributes` rule setting
`-whitespace` for this closed AgentRun. The rule changes Git validation
semantics only for this immutable exact-byte package. It does not change any
accepted package, transcript, output, sidecar, manifest, freeze, ruling,
decision, receipt, runtime, product, or credential byte.

The candidate-whitespace validator remains authoritative for all other
paths. The closeout branch must demonstrate:

1. no D-APP-93 accepted evidence byte differs from the pre-closeout worktree;
2. `git diff --check` passes with the exact-byte attribute active;
3. the repository candidate-whitespace validator passes after the retained
   package is staged; and
4. receipt and governed-register validators remain passing.
