# V3-DAPP70-FORMAT-BINDING-BACKCHECK Launch Brief

- **Role:** EVALUATION (Agent 1; load and obey `agents/AGENT_EVALUATION.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Instance:** `V3-DAPP70-FORMAT-BINDING-BACKCHECK`
- **Basis commit:** `36a422ac5568a02ecf120c214f8e1fc96fd6ab45`
- **Release amendment:** `../../amendments/V3/v1.md`
- **Release-amendment SHA-256:**
  `6c290cacff3a208707034ae70fc28f8f0ded8c0b8e330b2989161cd145a55152`
- **R4 RETURN SHA-256:**
  `3f466b9d95a9967dc8e1eac81defb884c4d6ee6821f74dd1df7c1099d759bf84`
- **R4 STATUS SHA-256:**
  `568f71392021ed1353b4bcff5c17a29763f75b0430230a5ea2d8362ba1c6fba6`
- **Evaluation output:**
  `projects/chirality-app-dev/execution/_Evaluation/CQF1_DAPP70_FORMAT_BINDING_BACKCHECK_36A422AC_2026-07-20/`
- **Delegation:** prohibited
- **Repair/downstream/Git authority:** none

## Objective and independence

Independently attempt to refute R4's exact nonsemantic format-and-binding
repair. Reconstruct the ten direct and seven transitive preimages; verify all
17 old-to-new hash transitions and every changed byte; revalidate current
W1/V2/applied/D-APP-71/Receipt-80 anchors, semantic and state neutrality,
complete dirty-population containment, hygiene, repository controls, and
origin disjointness. Treat R4's terminal claims as assertions, not proof.

Return exactly `ACCEPT | BLOCK`. Do not repair any finding.

## Mandatory preflight

Before writing the additive evaluation package:

1. require branch `codex/app-dev-dapp70-mapping-application-20260720` and
   `HEAD == 36a422ac5568a02ecf120c214f8e1fc96fd6ab45`; use the locally available
   `origin/main` read-only and perform no fetch or Git-state mutation;
2. bind amendment v1, R4 graph/launch/handoff/return/status to their current
   hashes, including R4 handoff
   `f520e4fe67dcab28561ee2c22c23204adfc2aeae9fdd1ace5c05d9b608ba12e1`;
3. strict-parse R4 STATUS with recursive duplicate-key rejection and require
   terminal `FORMAT_BINDING_REPAIR_COMPLETE_AWAITING_V3`, exact diagnostic
   accounting `13 / 10 / 9 / 4`, prior CHANGE count 14 preserved unresolved,
   exactly ten direct and seven transitive transitions, no blocker or waiver;
4. reproduce the 42-path pre-v17 tranche with canonical sorted path-list hash
   `d2365880b7639a9c6465b38468d4787c3c1b33bc416705b96913fbb174d27438`,
   the six v17/R4 repair controls, and the exact 48-path pre-v18 basis with
   hash `2b735dadd409ff52ed45ef1b211fc1e59c6a32447c8ba6e58440853901b0c10f`;
5. account separately for the four v18 release controls and the append to the
   already-counted root HANDOFF_STATE, then record the complete launch
   population before V3 outputs;
6. require current anchors: W1 RETURN/STATUS
   `4228184e5eadcced8de6d261f87c42918c72c075002728fba2565366c803ed38` /
   `fdf1e9a2052fed915607696706eb24aeced275cf8cd9885e17322929463eb655`,
   V2 RETURN/STATUS
   `8bd93871ef167c283204e135b5a88e7106de279f498a11c4138406eecd043874` /
   `d1c54e2276129cc4930dd6433b556a26ed7041147294ed92662701a85d92a5c3`,
   applied manifest/handoff
   `40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e` /
   `388effec0ce63d606d2707dc59ba4a52d68efcff18553bc7043fcd2787c01c94`,
   D-APP-71 packet
   `711cd2e238362819f601c838c807f729e873c4a05ce478a3de4615ce6985f18c`,
   decision register
   `3eb0a430bc98c43b4b7f2b6603d1f186ec679bc44685cb80ea1350aed96828c5`,
   and Receipt-80 ledger
   `7e5b6baa046fac24bebbf3990378bd596647410b2c974eab7cd91166392eebc4`;
7. freeze a complete before-write status/inventory/content hash manifest; and
8. fail closed without partial outputs on any input, population, hash, schema,
   state, authority, or containment mismatch.

## Exact 17-transition and byte-reconstruction audit

Independently recompute every pre/post pair in R4 STATUS. For each direct path,
reverse only the declared repair and authorized hash substitutions and require
the exact graph-bound pre-repair SHA. For each transitive path, reverse only
the declared old/new hash tokens and require the exact pre-repair SHA.

Prove the complete repair delta contains exactly:

- nine single terminal-LF deletions, leaving exactly one final LF;
- four deletions of exactly two trailing U+0020 bytes on D-APP-71 packet lines
  3, 4, 5, and 6; and
- exact old-to-new 64-hex hash-token substitutions required by the 17-path
  dependency chain.

No other byte, prose, CSV field, JSON value, order, option, count, verdict, or
state may differ. Search all current W1/V2/applied/Receipt-80 surfaces for each
superseded hash. Any occurrence outside explicitly historical v16,
amendment-V2, V2-launch, v17, R4 graph/brief/return/status/handoff, or V3's own
audit evidence is a blocker.

## Current anchors and neutrality

Independently verify applied-manifest closure; W1
`APPLICATION_COMPLETE_AWAITING_V2`; V2 `ACCEPT`; 22 exact mapping rows in
original order; nine groups `5+4+6+1+1+1+1+1+2`; the 21 physical/primary plus
one shared-only split; four closures plus one narrowed residual; and all five
local records.

Require D-APP-71 exactly `AWAITING_RULING`, selection null, no ruling file, and
unchanged neutral options DEL-02-03, DEL-02-05, DEL-09-06, and DEFER. Require
Receipt-80 unique/latest, parent Receipt-79, unchanged prose and accounting,
with only its two authorized pointer hashes transitioned.

Prove R4 changed no semantic claim, deliverable lifecycle/status content,
frontend/runtime source, ScopeOfWork, dependency view/register, decomposition,
authority, local R5 record, release/publication state, hard-fence state, or Git
state. Byte-bind the 22 sources, five SOWs, ten dependency files, five status
files, five local records, upstream 14-file derivative, R3, and accepted V1
surfaces against the preserved W1/V2 evidence.

## Hygiene, controls, origin, and containment

- Run individual `git diff --no-index --check /dev/null <path>` for every
  untracked/new file in the 42-path tranche, all v17/R4/v18 controls, and every
  V3 output; separately run it for all 17 repaired/transitive text paths.
- Run actual `git diff --check` and `git diff --cached --check` after V3 output
  creation; both must exit zero. Also construct a staged-equivalent patch of
  every untracked/new file and require its check to exit zero without mutating
  the index.
- Strict-parse every bound/new JSON with recursive duplicate-key rejection;
  validate CSV schemas and the applied/W1/V2/R4/V3 hash closures.
- Run the receipt validator, authority-corpus v9 status, repository self-check,
  and exact final path/content containment inventory.
- Compare `36a422ac..origin/main` read-only. Require every origin-advance path to
  remain disjoint from app-dev, the instruction stack, all 42 tranche paths,
  repair/release controls, and V3 outputs; record exact count and path-list
  hash. Any overlap or unavailable evidence is a blocker.

## Outputs and terminal contract

Write only:

1. `EVALUATION_PROTOCOL.md`, `EVALUATION_REPORT.md`, `FINDINGS.csv`, and
   `HANDOFF.md` under the exact additive evaluation output root; and
2. `RETURN.md` and terminal `STATUS.json` in this instance directory.

The terminal return must include exact 17-transition reproduction, byte-delta
classes, all anchor hashes, 42/repair/v18/V3 population accounting, individual
and aggregate hygiene, JSON/receipt/corpus/self-check/origin/containment
results, semantic/state/source/SOW/dependency neutrality, findings, unknowns,
conflicts, blockers, waivers, and rerun triggers.

Return only `ACCEPT | BLOCK`. No repair, modification of any subject/control,
new receipt, D-APP-71 ruling/selection, lifecycle/status/source/SOW/dependency
action, downstream release, publication, hard-fence effect, waiver, or Git
action. Do not delegate.
