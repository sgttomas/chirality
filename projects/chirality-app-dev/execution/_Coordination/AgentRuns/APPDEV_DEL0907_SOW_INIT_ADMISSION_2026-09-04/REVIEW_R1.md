# DEL-09-07 initialization admission — independent review R1

Verdict: PASS. Zero BLOCKER or MAJOR findings; no required remediation.

Reviewed basis `95b5687a7c9a4c6fe6e655f628495dec08ce04d8` through frozen head
`e079cbc397e4208c4c82d6a55a6dffacf67165e4`, all eleven changed files and
all added/deleted lines. Review used the detached worktree
`/private/tmp/chirality-del0907-init-admission-jcyUcf/review`.

Read context: root and App AGENTS, the workflow-component standard's human
authority and routine execution constraints, immutable D-APP-104 ruling,
scope-of-work SKILL/BRIEF_SCHEMA/TOOL_POLICY/QA_CHECKS, full frozen diff,
and surrounding scanner/register/admission logic.

The new admission is restricted to the exact DEL-09-07 package, path,
dispatch operation and declared INIT token. Its source and scaffold hashes
are pinned, including the post-SCA pointer. Missing or altered inputs,
symlinks, extra entries and special files block. Directory traversal errors
are accumulated as blocking errors. Nonblocking file opens prevent FIFO
source inspection from hanging. The admission is stateless eligibility,
not role authentication or a persistent reservation, as its docs disclose.

When the exact contract appears, ordinary scanner/register checks govern.
The initialization row cannot suppress malformed input, a held basis or
identity mismatch. Ordinary CLEAR remains a basis check rather than contract
acceptance. This supports the existing INIT skill's direct production
authoring and subsequent verifier without granting lifecycle or product acts.
D-APP-104 bytes remain unchanged; its old behavior is retained and tested
against the immutable proposal row. New transition fixtures source the
pre-initialization commit, avoiding an inherent failure when the later SOW
is created. Decision provenance distinguishes the owner's bounded repair
direction from approval of unseen implementation bytes.

## Independently executed checks

Working directory was the detached review worktree above.

`/private/tmp/chirality-piping-dec093-venv/bin/python -m pytest -q -p no:cacheprovider projects/chirality-app-dev/execution/_Scripts/tests/test_app_hold.py -k SowInitializationTests`

PASS: 11 passed, 28 deselected, 19 subtests passed in 2.37 seconds.
These exercise successful INIT/evidence, source drift, operation/token
restriction, missing/extra paths, symlink ancestors and evidence, FIFO input,
valid consumption, held/malformed/symlink/FIFO contracts, package/path
mismatch and row tampering.

`git diff --check 95b5687a7c9a4c6fe6e655f628495dec08ce04d8..e079cbc397e4208c4c82d6a55a6dffacf67165e4`

PASS: no output. Full unaffected suites were intentionally not repeated
under the owner's direction. Writer-reported wider checks are not claimed
as independent reviewer executions. Final receipt and narrative closeout
were pending at this freeze and remain the manager's closeout responsibility.

## Execution attribution

Fresh ephemeral Agent 2 reviewer, delegated-harness-native; role not
mechanically enforced; instruction-asserted. Non-delegation is instruction
and config asserted, not mechanism-proven. Codex/OpenAI/GPT-6 per session
instructions; exact backend identifier is not exposed. No substitution was
requested or observed. No child was dispatched. This report is original
review evidence, not a verbatim native event transcript. Repository content
was not edited; only this permitted scratch report was authored.
