# Manager Attempts and Remediations

## MGR-ATTEMPT-001 — runtime telemetry enum

The first manager telemetry invocation used unsupported outcome `ACTIVE` and
wrote no event. It was immediately rerun with supported outcome `STARTED`.
Classification: safe invocation correction; reason code
`TELEMETRY_OUTCOME_ENUM`; no governed input or project/candidate byte changed.

## MGR-ATTEMPT-002 — author manifest terminal blank line

After terminal author return, manager fan-in found the self-excluding
`I0-AUTHOR/MANIFEST.tsv` ended with one blank line. Exact preimage SHA-256:
`57690a7a27597fdc8fef1156ee185a7c4c0d75ce7b75544a43e1f20e30df68be`;
the only repair removed that empty terminal record. The 44
data bindings, their order, paths, hashes, byte counts, author return/status,
candidate family, and all substantive evidence remained unchanged. The
manifest is self-excluding, so no transitive child binding required refresh.
The postimage is 8,783 bytes at SHA-256
`201bfb0a2ca0d6c449b2fbf92e6cc17f193f1b1ef7f30d96a360471a8a071315`.
Its row reproduction is recorded in
`I0_AUTHOR_ACCEPTANCE.md`.

## MGR-ATTEMPT-003 — manager test path correction

The first manager root-test command named nonexistent historical path
`tools/export/test_generate_agent_docs.py`. Pytest failed before collecting a
test and the failure output remains `ROOT_TESTS_ATTEMPT_1.txt`. The manager
immediately reran the accepted current pair
`tools/validation/test_public_export_profile.py` plus
`tools/scope_of_work/test_scope_of_work_tools.py`: 20 passed. No project,
candidate, authority, status, lifecycle, or test source changed.

## MGR-ATTEMPT-004 — manager closure EOF normalization

Before final manifest freeze, the manager found its generated Markdown/TSV/
JSON closure surfaces created through patch application had one empty terminal
record each. It removed exactly one final LF from each affected generated file,
excluding all sealed `LAUNCH_BRIEF.md` files and all child-frozen evidence,
then rebuilt the complete manager manifest. No substantive byte, candidate,
project input, result, count, or verdict changed.

## MGR-ATTEMPT-005 — manifest root-depth correction

The first manager-manifest run used the `execution/` directory as its root,
so it bound 185 instance files under paths missing the `execution/` prefix and
omitted the candidate family. Validation rejected all 185 path bindings. The
script root was corrected to the repository root, the invalid manifest was
replaced, and the complete instance plus candidate manifest was regenerated
and independently reproduced. No bound artifact changed.