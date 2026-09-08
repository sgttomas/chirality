# Runtime publication whitespace method assessment

Status: `PASS_ACTIONABLE_METHOD__NO_EXECUTION`

Frozen at `2026-09-07T23:03:34Z`. This is a record-only assessment. It changes no selected Runtime byte, validator, attribute, Git, source, canonical, process, or evidence state.

## Observed blocker

CHANGE's accepted Runtime publication selection contains 170 paths and 574611 bytes. The mandatory candidate-whitespace check exits `2` with 42 diagnostics across 28 files. The raw failure is SHA-256 `f5c1f4d5a775c3da96c866af168785ea2f3ca6818e58628505f90a0056e72afd`; classification SHA-256 `17c5c27a2b7ee8c881c4ed8891507a96c5d85059f064de2b64b0b94a8c6bebf3` divides them into:

- 23 immutable text evidence files with one or more accepted terminal blank lines;
- two historical `CANDIDATE.patch` files whose `+ ` lines are literal unified-diff payload;
- three accepted snapshot CSVs with CRLF terminators.

The three canonical postimages and seven Gate 5 acceptance files are clean. All diagnosed bytes are hash-bound selection members; normalizing them in place would break the accepted manifests and evidence chain.

The validator delegates tracked candidates to `git diff --check` and the PR workflow invokes it over the committed base range. Repository `.gitattributes` already uses `whitespace=cr-at-eol` for exact-byte CSV registers and `-whitespace` for unified-diff or sealed raw evidence. Git supports path-specific comma-separated whitespace rules, including disabling only `blank-at-eof`; therefore a narrowly scoped attribute repair can retain all other whitespace checks for the 23 cosmetic cases.

## Recommended minimal method

Apply the adjacent `PROPOSED_GITATTRIBUTES.patch` to the current `.gitattributes` preimage SHA-256 `021e250c8f66ea1e9ea5af85575f17626e8cb93121a6f49fa321bcb35c7afb79`. It adds only:

1. `whitespace=-blank-at-eof` on each of the 23 exact diagnosed paths. Trailing spaces/tabs and the other configured checks remain active.
2. `-whitespace` on the two exact historical unified-diff payloads, matching the existing repository treatment for `.diff` artifacts. Their literal `+ ` bytes remain unchanged.
3. `whitespace=cr-at-eol` on the three exact Runtime snapshot CSVs, matching the existing rule for root scope-change CSVs. Actual spaces/tabs before CR remain detectable.

Do not edit the 28 accepted files, rewrite manifests, weaken `validate_candidate_whitespace.py`, skip the mandatory PR check, use local-only `$GIT_DIR/info/attributes`, or make a directory-wide evidence exception. The proposed rules are versioned, exact-path, independently inspectable, and limited to the diagnosed representation feature.

After authorization and application, CHANGE should:

1. Verify `.gitattributes` still matches the reviewed postimage and all 170 original selection members still match their approved SHA-256 and byte counts.
2. Expand the tranche selection by exactly `.gitattributes` plus the method record selected by the owning handoff; regenerate the selection count/tree digest without altering any original member.
3. Stage the exact selection and run the same `validate_candidate_whitespace.py --base-ref <base>` command used by CI. Require exit `0`, retain the original raw failure and classification, and record a before/after diagnostic map proving that only the classified 42 diagnostics disappeared.
4. Run `git diff --cached --check`, manifest/tree verification, required governance checks, and fixed-head PR checks. Fail closed on any new diagnostic, unexpected attribute match, byte drift, or path drift.

## Why normalization is not preferred here

The prior D121 method of preserving an external pre-normalization bundle and publishing reviewed derivative copies is sound when a publication representation can become a new derivative identity before acceptance. Here the affected files already form accepted canonical snapshots and sealed, mutually hash-linked evidence. Producing 28 normalized derivatives would require new paths, updated references, successor manifests, fresh review, and a changed 170-member publication contract. It adds a second representation of the same record and creates more opportunity for lineage mistakes. Path-specific format declarations preserve the authoritative bytes and keep the check meaningful.

If Git on the actual publication lane does not honor any proposed narrow rule exactly, stop and use the D121-style successor derivative for that category only. Do not fall back to `-whitespace` for a broader directory.

## Authority and impact

The accepted CHANGE handoff says to publish only the exact 170-path selection and to fail on unexpected paths. Adding `.gitattributes` therefore requires an explicit amended owning-workflow handoff before staging. Because this change declares the representation of already accepted immutable bytes, changes no semantic or canonical content, and retains rather than bypasses the mandatory check, consolidated Agent 0 may authorize it as a low-risk mechanical publication adjustment under the existing standing Git grant. A new human semantic acceptance vote is unnecessary unless the exact review finds a rule matching beyond these 28 paths or changing a selected byte.

The amended handoff must bind the `.gitattributes` preimage/postimage, the exact patch, the unchanged 170-member digest, the expanded selection, and a separate review. CHANGE then performs ordinary validated closeout. Any proposal to weaken the validator, waive CI, alter canonical/evidence bytes, or broaden the exception requires a new disposition and is outside this method.

Impact is limited to Git whitespace classification for the 28 named paths. It does not alter checkout normalization, file contents, manifests, authority, Runtime behavior, source, SOW, supplier state, Gate 5 acceptance, or release state.

## Inputs

- `change-runtime-publication/WHITESPACE_CLASSIFICATION.json` — `17c5c27a2b7ee8c881c4ed8891507a96c5d85059f064de2b64b0b94a8c6bebf3`
- `change-runtime-publication/STAGED_WHITESPACE_FAILURE.txt` — `f5c1f4d5a775c3da96c866af168785ea2f3ca6818e58628505f90a0056e72afd`
- `tools/validation/validate_candidate_whitespace.py` — `dcdf39a0003f82ba9689aa52f07915086802664f652c2a15e433f3663c347dae`
- `.github/workflows/governance-harness.yml` — `9e6a9ef814c79f1c35a00d154986bf3ba7174c49450d0e9cc36bca1de8f73079`
- `agents/AGENT_CHANGE.md` — `bb2922c5761395687caf120097276806769ec38f4fee8935d9e6c7bbb8506a06`
- Official Git `gitattributes` and `core.whitespace` documentation, inspected 2026-09-07.
