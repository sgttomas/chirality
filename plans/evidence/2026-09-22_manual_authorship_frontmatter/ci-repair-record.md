# CI repair record

The first required harness run for PR #857 failed in the existing `test_public_export_profile.py::test_public_export_excludes_private_runtime_surfaces` check. Its curated export includes the tranche manifest under `docs/`, and the boundary scan correctly rejected an absolute local Downloads path in that manifest.

The manifest now names the supplied authorship source by its filename and points to the internal `BRIEF.md` and `INPUTS.json` for its actual local origin and hash. Those internal run records are under `plans/`, which the export excludes. No rule, exclusion list, or check was weakened; the book, Word/PDF, companion instructions, and renderer are unchanged.

The affected test module passes locally using the configured Python 3.13 environment: **5 passed**. The next commit contains the manifest and evidence-record repair. The required GitHub CI rerun on that commit remains the merge gate.
