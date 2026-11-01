# Consumer use and publication inputs

Maturity: obtaining/use and change-inspection candidate with bounded named-reader
evidence and independent examination. The owner approved the six-file content
proposal at `4d33dfed9e2388efad504d7736275e8d55d41722` with “approved.”
Integration is recorded in PR #1784; product acceptance and release remain separate. Initial assessment
used `fd847ac9ac68250b2f35d2e9c0087c16e86b510a`. The current undertaking uses the
integrated F-02 result at `1357d706ea77497903976bf159f3880bea4d1360` as its real
source candidate, compared with `257ab4c18014bf872a1c72eeb7593a7ad3d135c0`.
No library release or consumer adoption is performed.

## Current undertaking and outputs

Give an independent consumer a usable way to select material, obtain its actual
bytes/resources/notices, examine changes and decide adoption. The proposed README
route and workflow-package guidance are the maintained outputs. This locality
holds their source basis, actual examination and limits. The existing F-02
change account supplies the reason and meaning of that candidate's changes;
it is not reproduced as a new version/history register.

## Reusable sources

`README.md`, the selected tool/workflow guides and `LICENSE.md` provide pieces
of an obtaining/use route. Select the actual surface and its required resources
and component-specific notices before evaluating a use claim. Ordinary reading
can use files without Git; executable operations retain their declared dependencies.
Root-specific execution and grants do not automatically become consumer instructions.

`docs/alignment-manual/README.md` distinguishes stable discovery from reliance
on an exact edition/source and gives the maintained rendering route.
`projects/FROZEN.md` preserves the completed archive transition and frozen-product
recovery references. Use those existing homes; do not create a second edition
history or re-run the completed removal.

## Selected consumer and publication bases

For Q-04, App Agent 0 identified the actual package reader at App revision
`366e7a6656d807142e7bdeda0ccf99c37d7227b1`:
`app/src-tauri/src/workflow_workspace.rs::Snapshot` and
`workflow_declaration.rs`, governed by
`execution/PKG-02/DEL-02-01/Work/WORKFLOW_DECLARATION.md` §§6.1 and 7 and
`execution/PKG-02/DEL-02-02/Work/WORKSPACE_AND_REGISTRATION.md` §4.5.
Capture is read-only; registration and execution are separate acts. The selected
claim is limited to capturing the current Root coordinated-knowledge-work package,
preserving its two files/content identity and parsing its declaration standing.

The maintained App fixture
`workflow_catalog_tests::actual_embedded_package_preserves_full_tuple_and_both_files`
examines App's existing embedded package. Its admitted revision is
`1b1733864cd89fd6d8ca74bf3e2084ff1105c1fc7d76537eefb42e2ae9a41e83`.
The current Root package's two source files differ from those embedded bytes,
so that fixture's result cannot qualify the newer input by itself. App has no
maintained standalone entrypoint accepting an arbitrary external package path.
The [isolated fixture wrapper](fixtures/app_workflow_reader.rs) exercised the exact
App reader source successfully, as described below. No pinned App input or
maintained consumer source was overwritten. This binds the selected reader claim;
it is not qualification of every possible consumer operation or library holding.

## Named-reader examination and reproduction

One filtered test ran against a complete immutable App source export at the
revision above. The only additions were the test wrapper and its `cfg(test)`
attachment in `app/src-tauri/src/lib.rs`; the production reader/parser, embedded
resources and pins were unchanged. Source comparison covered all 3,597 archived
regular files. The fixture binds the two Root source-file SHA-256 values and
checks exact captured bytes, declaration standing, hygiene and identity behavior.

The actual reader captured both files, totaling 22,621 bytes, with no declaration
or hygiene findings. The declaration and all five categories were `Undeclared`:
requirements are undeclared, not established absent. Its package method was
`chirality.app.workflow-package.sha256/v1`, with value
`3730d84debb5d77582a0c26211a5f380cdb1a44c7e26eeb537f334db43fdd881`.
Relocation preserved that value. A controlled resource-byte change in a separate
copy changed it while leaving the original input intact. LICENSE.md was checked
separately and is outside this package identity.

To reproduce, export the exact App revision and selected Root package/license
from their repositories into owned temporary directories. Copy the fixture into
the exported App's `app/src-tauri/src/` and append
`#[cfg(test)] mod app_workflow_reader;` to that export's `src/lib.rs` only. Set
`CHIRALITY_READER_PACKAGE` to the exported package and `CHIRALITY_READER_SCRATCH`
to an owned empty directory. From the exported `app/src-tauri`, run:

```sh
cargo test --offline --locked --jobs 2 --lib \
  app_workflow_reader::root_package_capture -- \
  --exact --nocapture --test-threads=1
```

Use an isolated Cargo home and target directory and follow any local build-resource
policy. This Snapshot path does not require Codex state; the observed run also
isolated a Codex home to comply with its host policy. It used ordinary copied
cached dependencies, no
downloads, original-target writes or writable links back to another checkout.
One test passed with 1,977 other tests filtered out. Existing compilation warnings
were not changed. Reproduction needs that complete source and available offline
dependencies; the fixture is not part of ordinary library use or Root's default CI.
The tested fixture at `5ff58130db0a85916bdc4cccf79da5f2a8e9e471` has SHA-256
`bb7404921047839c463eeac0f71539df8563ddd89dd288192f6aac8ca913ebb2`.
Independent-review clarification subsequently changed only its reproduction
comment; executable test code is identical, so the passing behavior evidence is reused.

This is actual capture/declaration/content-identity evidence at the two named
revisions. It establishes neither registration, workflow execution, supplier
capability, user approval, product adoption nor a release. The original embedded
package remains at its own identity. Later source changes require examining
which parts of this evidence remain applicable.

For Q-05, the candidate is the F-02 source revision named above, including
Consolidated v9 and its maintained HTML, compared with the pre-F-02 source basis.
This is an identified candidate using an existing edition name, not a newly
published library version. PR #1783 supplies the actual consequential change
account and source/render examination. The manual's rendered source identity
remains its recorded commit; the later integration revision does not rewrite it.
The actual delivery candidate is a source archive containing LICENSE.md and the
v9 Markdown/HTML from that revision. Extracted bytes were compared with their
source blobs; the HTML retains renderer source commit
`6472b49b2a6c7ebf4db1356d7bf83fa3af412305` and the matching Markdown hash.
Its source/render and desktop/narrow examination from PR #1783 remain applicable
because those bytes are unchanged. The archive is identified as a source candidate,
not a published edition or a replacement for the complete library.
No library GitHub release was returned by the bounded release-list query during
this undertaking. Discovery of no suitable publication requires an explicit
development-source choice, not silently calling main or an archive tag a release.

## Copy and change-inspection exercise

An isolated Git archive of LICENSE.md and the complete selected workflow package
at Root `1357d706ea77497903976bf159f3880bea4d1360` was extracted without Git metadata.
The copied bytes matched their source blobs. Reading the method and contained
REVIEW-NOTES resource needs no Git installation or invocation. This exercise
covers the selected copy, not every file in a full-repository download.

The source comparison from `257ab4c18014bf872a1c72eeb7593a7ad3d135c0` to
`1357d706ea77497903976bf159f3880bea4d1360` identified the six selected maintained
documentation outputs changed by F-02: three shared references, the corrected
PRD, and v9 Markdown/HTML. The full revision comparison also changes two
DEL-02-02 locality records (ScopeOfWork.md and Work/Applicability.md); those were
excluded from this consumer-output comparison, not represented as unchanged.
The selected outputs' meaning/use account is in PR #1783. A deliberately
unavailable comparison revision was rejected; it was not reported as no change.
Inspection leaves the consumer's selected basis unchanged.

## Remaining use and decisions

Q-04 is now bound for the selected App reader claim. Q-05 has the identified
source/edition candidate and prior comparison basis; no owner publication is
claimed. Other interfaces and uses still need their own bindings and evidence.
Independent review found no blockers; its clarity corrections are incorporated.
The owner approved this content for integration. Bind only the resources and conditions
needed by a selected use.
Coordinate shared README edits with DEL-01-01, which owns navigation; this
locality owns obtaining/version/compatibility meaning. DEL-02-02 may need a
named adopter's basis before changing a disputed clause; DEL-03-01 owns any
separately justified executable repair. Existing maintenance and reconciliation
methods remain usable without whole-deliverable completion gates.

Verify historical bytes actually relied upon, preserving original pins and
editions; do not extend that into a global history audit. Consumer adoption,
private operational data and product releases stay with their owners. Initial
native needs preserve these conditional uses and unresolved source bindings.

Neighboring DEL-02-02, DEL-03-01 and DEL-04-01 needs were deliberately left
unchanged: their unresolved adopted-clause or exported-interface conditions are
different claims from this bounded package-reader and source-candidate case.

## Complete library source candidate after the 60% decision

The broader delivery subject is the complete tracked library repository at
`7c334bf5cb529a814e0f96f68bc8d9500b15cdd5`, described as **Chirality library source
candidate at that revision**. This is a proposed source-delivery basis, not an
owner release or semantic-version decision. Its preceding comparison basis is
`547e7d7f833f9bec351f7a034bddd7c1a37db15a`. The source candidate adds the structured
brief's PyYAML dependency explanation and the corresponding toolkit examination;
no executable capability changed. The current PR's subsequent evidence updates
are not silently included in that identified archive.

The complete archive was produced with `git archive --format=tar` at the exact
revision. Its SHA-256 is
`b442c2476ae532ca2223731e6697eae050d11f2f0edb37bac3a87218043a49cd`.
`git get-tar-commit-id` identifies that revision. All 1,052 files, totaling
13,514,094 bytes, matched the selected Git blobs and modes before and after the
selected operations; no extra source files appeared. No tracked links or gitlinks
were present. Extraction was outside every Git repository, with no `.git` metadata.
The archive preserves LICENSE.md and other tracked notices. Selected surfaces had
no separate component notice; this is not a universal licensing/support assessment.

The actual extracted form supplied these bounded operations:

- Source-qualified preparation, current-project and ScopeOfWork resource loading
  succeeded under their compatible roles. Requested resources retained matching
  hashes; incompatible TASK/project-setup selection and a missing resource were
  rejected. No write targets or write capability were inferred from selection.
- Archived DEL-05-01 validated as SOW_V1, derived eight checklist criteria and
  passed its boundary-owner check without site packages. Format validity is not
  substantive acceptance.
- Current scaffolding created a disposable accepted-identity locality outside the
  source tree. Repeating it preserved declaration bytes and existing Work content.
  The prepared check passed without a blank ScopeOfWork or lifecycle files.
- The same read-only JSON brief failed before normalization without PyYAML and
  succeeded using an existing suitable interpreter, returning no writable targets.
  The updated guide accurately describes this dependency and its fallback limits.
- Native dependency querying refused the non-Git source directory. Direct reading
  of its existing declaration exposed conditions and evidence pointers without
  deriving reverse links, Git observations or input suitability.

The first project-setup probe selected TASK and was refused; that was corrected
to the method's declared WORKING_ITEMS role for context selection. The first
missing-resource probe was also masked by that role mismatch. Only the subsequent
compatible-role refusal establishes the missing-resource observation. No role
execution, delegation or host permission was inferred from either selection.

Reproduction uses the full `git archive` at the named revision, safe extraction
outside a checkout and the maintained commands in the selected guides. Keep
Python bytecode disabled to observe source preservation. Use Python/PyYAML and
zsh where required, and the documented PYTHON override for shell helpers; no
install or network access was needed. ScopeOfWork tools retain common.py and
id_catalog.json; resolution retains roles, registry, catalog, selected package
resources and applicable legacy maps. Query Git/HEAD prerequisites remain in force.

Full-tree correspondence establishes source-delivery identity; behavioral evidence
is limited to the operations above on the observed platform/filesystem. Historical
and Root-only holdings keep their declared standing. No frozen product was run,
no broader App qualification is inferred, and owner content/delivery approval
remains pending. The earlier named App-reader and manual-edition cases retain
their own exact bases and limits.
