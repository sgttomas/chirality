# Agent 0 authorization and amended Runtime publication handoff

Status: `AUTHORIZED_FOR_CHANGE_APPLICATION_AND_ROUTINE_CLOSEOUT`

The consolidated HELP_HUMAN Agent 0 authorizes this exact low-risk mechanical publication adjustment under the existing standing Git grant. This record amends the accepted Runtime publication handoff only as stated below. No further parent confirmation or human semantic vote is required.

## Authorized representation change

CHANGE may apply `PROPOSED_GITATTRIBUTES.patch` SHA-256 `e7414a95778094423910c711c5004523cf40f4a0bdf26759445a50f1dc58da20` to `.gitattributes` preimage SHA-256 `021e250c8f66ea1e9ea5af85575f17626e8cb93121a6f49fa321bcb35c7afb79`. The only authorized postimage is SHA-256 `7d9d8cedce4e8ee24ca95a754ae8f335eb0c2204b628d837ca1e2d3950c13c4f`.

The reviewed patch contains 28 literal paths and no glob metacharacters:

- 23 exact files receive `whitespace=-blank-at-eof`;
- two exact historical `CANDIDATE.patch` payloads receive `-whitespace`;
- three exact CRLF snapshot CSVs receive `whitespace=cr-at-eol`.

Independent review manifest SHA-256 `d22eb2a994509fea7b368664e343c469558b838cca7a19a2234f60f17de26764` is `PASS`. It verified zero unexpected matches across 72,981 candidate paths, unchanged SHA-256 and byte counts for all 170 original selection members, exact reproduction of the frozen 42-diagnostic failure, and exit `0` for the unchanged mandatory validator on both staged and committed base-range candidates. The validator remains `dcdf39a0003f82ba9689aa52f07915086802664f652c2a15e433f3663c347dae`; the workflow remains `9e6a9ef814c79f1c35a00d154986bf3ba7174c49450d0e9cc36bca1de8f73079`.

## Amended selection

Preserve the original 170-member selection, 574611 total bytes, and every member hash exactly as frozen in `change-runtime-publication/SELECTION.json` SHA-256 `25340309aa51d4bdb2601103a8b894dbe536dde5b9b4b49a6e0f5a9bc09ce9bb`. Add only:

1. `.gitattributes` at the exact reviewed postimage;
2. `change-runtime-publication-method/METHOD_ASSESSMENT.md`;
3. `change-runtime-publication-method/PROPOSED_GITATTRIBUTES.patch`;
4. `change-runtime-publication-method/MANIFEST.json`;
5. `change-runtime-publication-method/review-v1/RETURN.md`;
6. `change-runtime-publication-method/review-v1/CHECKS.json`;
7. `change-runtime-publication-method/review-v1/MANIFEST.json`;
8. this `AUTHORIZATION_AND_HANDOFF.md` and its successor `MANIFEST_v2.json`.

The expanded publication selection is therefore 179 paths before CHANGE adds its ordinary tranche-local closeout evidence. CHANGE must regenerate and record the expanded selection digest and byte count from actual staged state. CHANGE's own ordinary closeout records may be added within `change-runtime-publication/` without altering the authorized Runtime or method members.

## Required execution checks

CHANGE is authorized to apply the exact patch, stage the exact amended selection, commit, push, and perform its ordinary PR publication flow under the standing Git grant. It must:

1. fail closed unless the `.gitattributes` preimage and all 170 original selection members match their frozen hashes and byte counts;
2. retain `STAGED_WHITESPACE_FAILURE.txt` SHA-256 `f5c1f4d5a775c3da96c866af168785ea2f3ca6818e58628505f90a0056e72afd` and `WHITESPACE_CLASSIFICATION.json` SHA-256 `17c5c27a2b7ee8c881c4ed8891507a96c5d85059f064de2b64b0b94a8c6bebf3` as the pre-repair failure record;
3. verify the actual attribute postimage and exactly 28 changed matches with the reviewed 23/2/3 split and zero unexpected matches;
4. run the same mandatory candidate-whitespace command used by CI, plus `git diff --cached --check`, selection/manifest verification, governance checks, and fixed-head PR checks;
5. fail closed on any new diagnostic, unexpected match, byte drift, path drift, conflict, or non-fast-forward condition.

No selected Runtime file may be normalized or edited. No `.git/info/attributes`, local configuration override, validator/workflow edit, skip, waiver, directory-wide exception, canonical/source/SOW/supplier/lifecycle/fixture/release change, or broader attribute rule is authorized.
