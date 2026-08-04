# TM-ROOT-112 implementation validation

Verdict: `PASS_WITH_NONBLOCKING_FINDINGS / HUMAN REPAIR ACCEPTANCE REQUIRED`

## Identity and containment

- The sealed pre-normalization implementation-brief authoring/execution hash
  `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218`
  and every frozen source hash matched before implementation. The current
  published brief is the semantically identical whitespace-normalized blob
  `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`;
  carrier validation binds both identities without rewriting execution history.
- Final product hashes match `FINAL_PRODUCT_HASHES.sha256`.
- Product changes are exactly `docs/SPEC.md` section 14.1,
  `runtime-daemon.ts`, and bounded `daemon.test.ts` cases.
- `git diff --check` passes. No public timing option, App/R2/process/SIGTERM
  claim, other canonical source, register, receipt, lifecycle, notice, or Git
  mutation occurred in this manager activation.
- `CARRIER_IDENTITY.json` binds the two implementation-brief identities, final
  product hashes, and terminal refutation/remediation/backcheck receipts.

## Fan-in

- Initial final-hash candidate: strict check PASS; daemon 14/14; runtime 73/73;
  evidence build PASS.
- Fresh I2 refutation reproduced two material defects: later pre-force identity
  was not retried after a non-identifying first event, and pre-bind start
  refusal deleted a foreign control path.
- I3 repaired exactly those two defects. Its terminal results: I2 adversarial
  2/2, daemon 15/15, full runtime 74/74, strict checks PASS, build PASS, and
  diff-check PASS.
- Fresh I4 backcheck verdict `PASS_WITH_NONBLOCKING_FINDINGS`; no material
  finding remains. Backcheck SHA-256:
  `eda15a004c4916be3977c938b35a814c42fad1145b59fccd77d08f655c8e15a4`.

Final validated environment: Darwin 25.6.0 arm64; Node 24.18.0; Vitest 3.2.4;
TypeScript 5.9.3. Node 22.19 was unavailable, so its supported-floor execution
remains a disclosed nonblocking compatibility gap. The worktree lacked
`runtime/node_modules`; preserved configs used the installed main-checkout
toolchain against current-worktree source aliases and emitted builds only
inside run evidence directories.

## Closure meaning

The bounded implementation/test tranche is technically complete and
decision-ready. The product bytes are not yet human-accepted. App routing is
still held until the accountable human accepts this exact repair; validation
or publication alone does not satisfy that gate.
