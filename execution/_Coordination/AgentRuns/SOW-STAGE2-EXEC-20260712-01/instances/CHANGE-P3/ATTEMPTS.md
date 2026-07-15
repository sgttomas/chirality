# CHANGE-P3 Attempts

All attempts were safe, mechanical, and retained. No candidate, project
control, lifecycle, dependency, release, reliance, or authority byte changed.

1. The initial read-only preflight queried `PROJECT_CONTAINMENT.json` for a
   generic `verdict` key. The accepted record instead uses
   `zero_project_writes: true`; the corrected assertion passed.
2. The first repository-check command used two nonexistent convenience script
   paths under `tools/scope_of_work/`. The authoritative commands were resolved
   from `tools/practitioner_harness/README.md` and rerun successfully.
3. The first root Scope-of-Work test invocation used `unittest` discovery on a
   pytest-style module and collected zero tests. The registered pytest command
   was then run with the public-export profile: 20/20 passed.
4. The freshly generated mutable JUnit report lacked a terminal LF. It was
   normalized before evidence freeze from SHA-256
   `23399f4add3904980d180b971098c2f5a0cf2f3d2d630ec4799aa52e653c39a1`
   to `2f4d36badbf48371bf9282a2547886946c444a7b3f1de646d2e15b2a9a526fe4`.
5. The first staged whole-diff probe found one extra blank EOF line in each of
   five new CHANGE-owned text files. Those mutable files were normalized to
   exactly one terminal LF and the full probe was rerun.
6. The first accepted-warning capture retained `git diff --check`'s offending
   content lines as well as its location lines, causing the capture itself to
   reproduce trailing whitespace. The report was mechanically filtered to the
   250 exact diagnostic location lines and the evidence binding was rebuilt.
7. The first isolated-postmerge binding failed because three ignored compiled
   Python residues present in the source worktree had been referenced by the
   PKG-10 author and PKG-12 replacement-verifier manifests but were never
   tracked. The three stale rows were removed, both package manifests were
   rebuilt, all ten package/child manifests revalidated, and the complete
   CHANGE binding was rebuilt. No candidate, project, accepted snapshot, or
   semantic evidence byte changed.
