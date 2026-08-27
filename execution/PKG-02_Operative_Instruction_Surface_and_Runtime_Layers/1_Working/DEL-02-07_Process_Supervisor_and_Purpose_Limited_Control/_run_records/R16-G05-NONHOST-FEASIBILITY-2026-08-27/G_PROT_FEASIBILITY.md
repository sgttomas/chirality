# R16 G-PROT Deterministic Feasibility Evidence

- **Node:** `N3.2 — G-PROT feasibility`
- **Date:** 2026-08-27
- **Calibrated state:** `REJECTED`
- **Gate status:** this is a bounded feasibility result; it does not state that
  `G-PROT`, `G4`, or any release gate passed.
- **Execution posture:** deterministic, no network, no vendor binary, no
  credential or account access, no host mutation, no production
  implementation, and no write to an App, runtime, tool, Piping, Tier-0,
  workplan, pin, or production-configuration surface.

## Governing basis and actual identities

| Input | SHA-256 recomputed from actual bytes |
| --- | --- |
| R16 ruling record | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| R16 companion steer | `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba` |
| release execution plan | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |
| accepted DEL-02-07 `ScopeOfWork.md` | `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5` |
| accepted DEL-02-10 `ScopeOfWork.md` | `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29` |
| N3.2 sealed launch brief | `5b2241d11cfaafec51e31ae540c6a19565cf07de8a2a5e3c536ed37609ae8fe4` |
| current repo-native `tool-path-policy.ts` inspected and exercised read-only | `fe707666d7fb528519b9ce358987e198082ad1e6f11132b97eadc435d20e5eaf` |
| current repo-native `tool-shell-policy.ts` inspected and exercised read-only | `ce2ebf15b73942180e17619ef9d4f220968cbd1af6ef22fb08bf0a6a0d1ce3d1` |
| current repo-native `instruction-root.ts` inspected and exercised read-only | `3ab8b1e585e7c4797f8c5606715ab0d6778c9267799cc91b222a07779f5cbaef` |

N0 is the pushed immutable commit
`9164d95456bd67576a1b1164fd08e52516edb368`; its parent is the exact R16
merge `b0d975a9139eddebf5c1e728cf724b55c8a97cad`. The N0 return preserves the
other nine held bindings and records G0.5 incomplete. N2 returned
`UNAVAILABLE_UNDER_BOUNDS` for exhaustive account/model/turn endpoint
enumeration; that result does not affect this independent deterministic limb.

The release-plan contract is strict: every protected-path rule, including a
mid-path glob, must deny read, file change, and shell write for primary and
descendant actions. One inexpressible rule or enforcement mismatch is
blocking; an expressible subset is not success.

## Method

A fresh directory matching
`/private/tmp/chirality-r16-gprot.XXXXXX` held one fixture root and temporary
copies of the three SHA-pinned policy modules above. The copies received only
Node 24 TypeScript-loader adaptations:

1. extensionless relative TypeScript imports received an explicit `.ts`
   suffix;
2. type-only `HarnessToolDescriptor` imports were removed; and
3. the unused runtime `HarnessError` import was removed from the copied
   instruction-root module.

No policy branch, matcher, decision, or return value was changed. Node
`v24.18.0` loaded the temporary copies with
`--experimental-strip-types`. The fixture called the actual exported
`evaluateToolPathPolicy` and `evaluateShellCommandPolicy` functions. It then
deleted the entire disposable directory through an exit trap. A subsequent
`find /private/tmp -maxdepth 1 -name 'chirality-r16-gprot.*'` returned no
path.

The primary posture omitted managed child scopes. The full-root descendant
posture supplied the fixture root as both `allowedReadScopes` and
`allowedWriteTargets`. A third descendant posture supplied only the
`notes/` prefix, to test whether prefix narrowing is equivalent to protected
glob compilation. The file-change representation used a
`project-root-write` descriptor; the shell-write representation used the
actual shell evaluator with a one-second timeout and an absolute
redirection target.

## Exact fixture results

`ALLOW` means the available representation admitted the operation. `DENY:X`
is the exact returned `denyClass`. For every protected row, the required
result is denial in all three surface columns.

| Actor posture | Case | Declared rule | Probe target | Read | File change | Shell write |
| --- | --- | --- | --- | --- | --- | --- |
| primary | R1_PREFIX | `private/**` | `private/token.txt` | `ALLOW` | `ALLOW` | `ALLOW` |
| primary | R2_MIDPATH | `projects/*/execution/**/accepted/**` | `projects/acme/execution/run-01/accepted/state.json` | `ALLOW` | `ALLOW` | `ALLOW` |
| primary | R3_SUFFIX | `**/*.secret` | `notes/seed.secret` | `ALLOW` | `ALLOW` | `ALLOW` |
| primary | R4_EXACT | `.env` | `.env` | `ALLOW` | `ALLOW` | `ALLOW` |
| primary | R5_INSTRUCTION_ROOT | `.codex/instructions/**` | `.codex/instructions/AGENTS.md` | `ALLOW` | `DENY:instruction-root` | `DENY:instruction-root` |
| primary | SAFE | none | `notes/ok.md` | `ALLOW` | `ALLOW` | `ALLOW` |
| descendant_full_root | R1_PREFIX | `private/**` | `private/token.txt` | `ALLOW` | `ALLOW` | `ALLOW` |
| descendant_full_root | R2_MIDPATH | `projects/*/execution/**/accepted/**` | `projects/acme/execution/run-01/accepted/state.json` | `ALLOW` | `ALLOW` | `ALLOW` |
| descendant_full_root | R3_SUFFIX | `**/*.secret` | `notes/seed.secret` | `ALLOW` | `ALLOW` | `ALLOW` |
| descendant_full_root | R4_EXACT | `.env` | `.env` | `ALLOW` | `ALLOW` | `ALLOW` |
| descendant_full_root | R5_INSTRUCTION_ROOT | `.codex/instructions/**` | `.codex/instructions/AGENTS.md` | `ALLOW` | `DENY:instruction-root` | `DENY:instruction-root` |
| descendant_full_root | SAFE | none | `notes/ok.md` | `ALLOW` | `ALLOW` | `ALLOW` |
| descendant_narrow_notes_prefix | R1_PREFIX | `private/**` | `private/token.txt` | `DENY:managed-read-scope` | `DENY:managed-write-scope` | `DENY:managed-shell-scope` |
| descendant_narrow_notes_prefix | R2_MIDPATH | `projects/*/execution/**/accepted/**` | `projects/acme/execution/run-01/accepted/state.json` | `DENY:managed-read-scope` | `DENY:managed-write-scope` | `DENY:managed-shell-scope` |
| descendant_narrow_notes_prefix | R3_SUFFIX | `**/*.secret` | `notes/seed.secret` | `ALLOW` | `ALLOW` | `DENY:managed-shell-scope` |
| descendant_narrow_notes_prefix | R4_EXACT | `.env` | `.env` | `DENY:managed-read-scope` | `DENY:managed-write-scope` | `DENY:managed-shell-scope` |
| descendant_narrow_notes_prefix | R5_INSTRUCTION_ROOT | `.codex/instructions/**` | `.codex/instructions/AGENTS.md` | `DENY:managed-read-scope` | `DENY:managed-write-scope` | `DENY:managed-shell-scope` |
| descendant_narrow_notes_prefix | SAFE | none | `notes/ok.md` | `ALLOW` | `ALLOW` | `DENY:managed-shell-scope` |

For primary and full-root descendant postures there were ten protected rows:
five rules times two actors. Exactly zero of ten denied all three surfaces;
all ten were enforcement mismatches. The instruction-root special case
denied file and shell writes but still admitted reads. Prefix narrowing did
not repair the representation: it admitted the suffix-glob target under the
allowed `notes/` prefix and denied shell for the unprotected safe target as
well. That is over-denial plus a protected-path miss, not a round trip of the
declared rules.

## Verdict

`REJECTED`

The available repo-native representations do not accept a declared
protected-rule set and cannot express the required mid-path or suffix glob
deny while retaining ordinary workspace access. Root-prefix scopes can
either admit a protected descendant or deny a larger subtree. The current
instruction-root special case is write-only and does not satisfy the required
read denial. The shell surface requires a descendant's managed scopes to
cover the whole project root or denies shell wholesale, so it cannot preserve
safe shell writes while denying a protected subset. Because the R16 and
G-PROT contract makes any inexpressible rule blocking, the evidence rejects
the proposition that the available representations are sufficient for the
design.

## Limitations and unavailable proof

- This result does not execute the App Server, a packaged App, a real
  `turn/start`, a model, or a native descendant. It makes no Seatbelt,
  packaged-bundle, or actual-turn enforcement claim.
- Exact 0.149.0 generated schema/types remain unavailable under the accepted
  G2/N2 record. Therefore this packet does not claim exact wire-field
  conformance for file-change approval messages.
- The exercised modules are existing App-loop implementation bytes read as
  available representations. They are not adopted as Root authority, were
  not modified, and do not create cross-loop work or truth.
- No production protected-path compiler exists or was implemented here. No
  glob matcher was inserted into the exercised modules; doing so would have
  changed the question from feasibility of available representations to
  unauthorized product implementation.
- The narrowed descendant posture proves only prefix-scope behavior. It does
  not establish that a native App Server descendant consumes these App-loop
  modules.

These limitations do not weaken the `REJECTED` feasibility verdict: the
actual available representations already produce blocking mismatches. They
do reserve all exact-pin, packaged, actual-turn, and native-descendant proof
for a separately authorized implementation and conformance tranche.

## Implementation implication

Workspace-write must remain blocked for a profile carrying any protected rule
until a separately authorized design provides one closed, canonical
protected-rule grammar and one shared compile result that is enforced before
read, file-change, and shell-write execution for both primary and descendant
actions. The future design must either:

1. provide exact deny semantics at every three-surface enforcement boundary,
   including mid-path globs, symlink/canonicalization handling, subprocess
   writes, and descendant inheritance; or
2. withhold the affected capability, including shell or all workspace-write,
   rather than treating prefix over-denial or an expressible subset as
   success.

The exact-pin generated types, packaged App Server behavior, and real
primary/descendant canaries must then be proved in the separately gated
conformance work. This result grants no WP-03/WP-05 implementation authority
and does not lift any R16 hold.
