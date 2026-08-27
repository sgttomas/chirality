# N3.2 G-PROT Return

- **State:** `COMPLETE`
- **Calibrated feasibility verdict:** `REJECTED`
- **Gate claim:** none; `G-PROT` and `G4` are not passed by this result.
- **Primary evidence:**
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/_run_records/R16-G05-NONHOST-FEASIBILITY-2026-08-27/G_PROT_FEASIBILITY.md`
- **Primary evidence SHA-256:**
  `b3ab9e3feaa93162b53eaa41fa1295e62f0c9bbc392adf5ff14ce4359b185c77`

## Exact result

The deterministic fixture exercised the SHA-pinned repo-native path and shell
policy evaluators for five representative protected rules and one safe
control under three actor postures: primary, descendant with full-root
read/write scopes, and descendant narrowed to a `notes/` prefix.

For the contract-relevant primary and full-root descendant postures, the
fixture produced ten protected rows. Full read + file-change + shell-write
denial occurred in `0/10`; enforcement mismatches occurred in `10/10`.

- Prefix `private/**`: all three surfaces allowed for primary and full-root
  descendant.
- Mid-path `projects/*/execution/**/accepted/**`: all three surfaces allowed
  for primary and full-root descendant.
- Suffix `**/*.secret`: all three surfaces allowed for primary and full-root
  descendant.
- Exact `.env`: all three surfaces allowed for primary and full-root
  descendant.
- `.codex/instructions/**`: file change and shell write denied with exact
  class `instruction-root`, but read allowed.
- Safe `notes/ok.md`: all three surfaces allowed for primary and full-root
  descendant.

Narrowing a descendant to the `notes/` prefix was not equivalent to compiling
the rules. It admitted `notes/seed.secret` for read and file change while
denying shell wholesale, including for the safe `notes/ok.md` target.

## Basis identities

- R16 ruling:
  `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef`
- R16 steer:
  `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba`
- accepted DEL-02-07 Scope of Work:
  `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5`
- accepted DEL-02-10 Scope of Work:
  `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29`
- current path evaluator:
  `fe707666d7fb528519b9ce358987e198082ad1e6f11132b97eadc435d20e5eaf`
- current shell evaluator:
  `ce2ebf15b73942180e17619ef9d4f220968cbd1af6ef22fb08bf0a6a0d1ce3d1`
- current instruction-root helper:
  `3ab8b1e585e7c4797f8c5606715ab0d6778c9267799cc91b222a07779f5cbaef`
- N0 commit:
  `9164d95456bd67576a1b1164fd08e52516edb368`

## Limitations

- No App Server, packaged App, real `turn/start`, model, or native descendant
  executed.
- Exact 0.149.0 generated schema/types remain unavailable, so no exact
  file-change approval wire claim is made.
- The exercised App-loop modules were read-only inputs, not Root authority;
  no cross-loop surface was written or adopted.
- No production compiler or glob matcher was implemented.

## Implementation implication

The available representations are insufficient for the strict G-PROT
contract. Workspace-write must remain blocked for profiles carrying protected
rules until a separately authorized implementation defines one canonical
rule grammar and proves the same compiled deny semantics across reads, file
changes, and shell writes for primary and descendant actions. Prefix
over-denial and expressible subsets cannot be accepted as substitutes.

## Containment and cleanup

- Network: not used.
- Vendor binary: not used.
- Credentials/accounts/Keychain: not accessed.
- Host state: not mutated.
- Disposable fixture: created only under
  `/private/tmp/chirality-r16-gprot.XXXXXX`, deleted by exit trap.
- Cleanup check:
  `find /private/tmp -maxdepth 1 -name 'chirality-r16-gprot.*'` returned no
  paths.
- Product/runtime/tool/App/Piping/Tier-0/configuration writes: none.
- Git commit: none.
- Repair cycles: none; the first deterministic run completed successfully.

## Paths written by this instance

1. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/_run_records/R16-G05-NONHOST-FEASIBILITY-2026-08-27/G_PROT_FEASIBILITY.md`
2. `execution/_Coordination/AgentRuns/ROOT_V3_R16_G05_SPIKES_2026-08-27/instances/N3_2_G_PROT/RETURN.md`
