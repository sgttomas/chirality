# N3.6 G-SENT return

- Instance: `N3_6_G_SENT`
- Role: bounded ephemeral Agent 2; no delegation performed
- Result: `SUPPORTED_FOR_DESIGN`
- Gate status: deterministic no-account feasibility only; `G-SENT` has not
  passed
- Git action: none; this instance did not commit, push, amend, or rewrite

## Primary evidence

`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/_run_records/R16-G05-NONHOST-FEASIBILITY-2026-08-27/G_SENT_FEASIBILITY.md`

SHA-256:
`0cde9c24c0c60723f222e88a0b62fc596a422bf606dd2b184bf7e9038f247ff6`.

## Exact results

- N0 sequencing prerequisite: satisfied and pushed. Branch and remote were at
  `0246e92b4bfede52c226d58122e8ac4bb980e666`; N0 transcription commit
  `9164d9545` is an ancestor.
- Required input identities recomputed and matched: R16 ruling
  `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef`,
  R16 steer
  `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba`,
  DEL-02-09 accepted SOW
  `e0cf3285f36c4397840d4875641d48bae53c493cff1bc065c3315e6575478176`.
- Deterministic fixture: `21/21` expected decisions matched; zero mismatches;
  process exit `0`.
- Preflight match control allowed. Independent root, account identity, account
  epoch, consent version/root/account/policy, effective-policy, generation,
  cwd, and missing-account cases all denied as expected.
- Action controls allowed synthetic in-root read/write classification.
  Outside-root read/write, `/tmp`, `/private/tmp`, effective `TMPDIR`, login
  shell, and command-network fixture attempts all denied as expected.
- Hard-envelope outside-write probe: exit `1`, `Operation not permitted`, and
  target absence verified.
- Hard-envelope command-network probe to TEST-NET-1: curl exit `7`, zero
  response bytes, and no completed connection.

## Limitations

Actual production `turn/start`, live-account continuity, primary/descendant
model/tool canaries, production outside-root read enforcement, both temporary
root denials, production login-shell denial, sticky cwd, and packaged
activation/release sentinel behavior are `UNAVAILABLE_UNDER_BOUNDS`. No
authentication, credential access, account mutation, vendor execution,
network approval, host mutation, or production/configuration edit was
performed.

The current worker envelope permits broad reads and authorized temporary
fixture writes, so those envelope capabilities were not misstated as product
denial proof. The fixture supports the fail-closed design but does not replace
later exact-policy App Server enforcement evidence.

## Implementation implication

Require a complete exact-match identity/consent/policy/generation/cwd
preflight before every turn, deny missing values, bind consent to root plus
account plus policy, and refuse `turn/start` unless the exact policy is bound.
Use client-side rejection plus independent App Server sandbox enforcement for
extra-root, temporary-root, login-shell, and command-network canaries. The
later live G-SENT must run representative primary and descendant
`turn/start` paths.

## Cleanup and write set

- Deleted disposable root:
  `/private/tmp/chirality-r16-gsent.zPMQbE`; post-delete `test ! -e` passed.
- Outside-write probe target
  `/Users/ryan/.chirality-r16-gsent-outside-write-probe-20260827` is absent;
  `test ! -e` passed.
- No artifact, credential, account state, vendor binary, or disposable byte
  remains.
- This instance wrote only the primary evidence file and this `RETURN.md`.
