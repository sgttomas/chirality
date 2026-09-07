# Root D-GOV-36 application checks

Status: `PASS_WITH_BROAD_WORKSPACE_WHITESPACE_FAILURE_RETAINED`

The faithful Root tranche was applied while `HEAD` was `a52e754491041b43ac4bc9414dff9becd52207ff`. CHANGE then fast-forwarded to `9428e4af44c91063f2188e31698e4c84d8549be9`; the two commits have the same tree for this transition, no target path changed, the index remained empty, and every applied postimage hash remained unchanged. The candidate's historical dispatch basis remains `1ffa47863b9a53ab359d84e1c72ca7d93a69b47d` and is not represented as the application or validation HEAD.

## Passing results

- Seven direct canonical postimages are byte-identical to the final author-v1 postimages; Receipt 148 is an exact suffix match.
- Candidate patch SHA-256 `a4e94ea7a506cf71759208a7754fc8e1b218aeb0870952128529d2a1c9cca9ae`; `git apply --reverse --check` passes against the applied tree.
- Root status and G0, G1, G2, G3, and G4 CI-mode checks pass.
- Root self-check exits zero with the retained baseline: 0 BLOCK, 4 REVIEW, 55 WARN, 14 INFO, and 1 NOT_APPLICABLE.
- Instruction entrypoints pass.
- Tranche-scoped candidate whitespace passes for the exact eight canonical effects.
- Affected profiles pass: 836 tests and 45 subtests.
- `git diff --check` passes before and after the fast-forward.

## Retained non-pass and required closeout rerun

The required whole-worktree command `validate_candidate_whitespace.py --base-ref origin/main` exits 1 because the shared checkout contains many pre-existing and concurrently produced untracked evidence artifacts with whitespace findings. It includes patch files whose context preserves historical trailing whitespace. This result is not rewritten as a pass or waived. The exact Root target scope passes with the validator's supported `--paths` mode. CHANGE must run the exact staged/candidate registered-scope whitespace check and the committed-range G4 command before publication, because uncommitted files cannot be evaluated by `--head HEAD --added-manifests-only`.

An initial Step-0 attempt with `/usr/bin/python3` failed operationally because that interpreter lacked PyYAML and exposed an error-path local-variable bug. All authoritative reruns used `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` and passed as stated above.

## Boundaries retained

No project access, consent, execution, private-supervisor access, full wire/source acceptance, supplier qualification, protected-fixture retry, lifecycle promotion, or release is claimed. Receiving notices route coordination only. App and Runtime adoption, their accepted snapshots and derivatives, paired validation, and owning receipts remain downstream gates.
