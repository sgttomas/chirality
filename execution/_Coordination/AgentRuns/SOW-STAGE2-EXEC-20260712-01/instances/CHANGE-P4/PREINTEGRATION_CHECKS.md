# CHANGE-P4 Preintegration Checks

Verdict: `PASS`
Basis: `main@e8f59a63372f38d9e788ac39b39995558f5aba73`
Branch: `codex/sow-p4`

The accepted preintegration manifest reproduces at SHA-256
`f2a96e80ac1c9fbc1e799b43fa912d52a606abbc194040585e6454b88ce612be`.
All 110 source/target rows and 198 retained control bindings matched the sealed
basis before mutation.

Twenty-two ordered atomic commits each contain exactly one deliverable's
accepted five-path replacement. The complete project delta is exactly 110
paths: 22 `ScopeOfWork.md` additions and 88 legacy deletions. Every other
project byte is unchanged.

Fresh deterministic reproduction passes 22 clean SOW_V1 format checks, 729
claim maps covering all 6,759 accepted source lines, 22 parity reports, 22
review checklists, and 22 finalizations byte-identical to accepted production.
The 110 replacement and 110 rollback rows are exact inverses; 22
apply/target/rollback simulations pass.

All 22 dependency schemas pass. Practitioner self-check reproduces its
accepted baseline; 264 practitioner tests, 20 public-export/Scope-of-Work
tests, and the agent, skill, path-anchor, and instruction-entrypoint validators
pass. Strict project-commit diff hygiene passes. Required remote checks remain
mandatory on the exact final source head.
