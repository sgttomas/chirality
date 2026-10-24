# Manuals for human agent work

These manuals are primarily for a person's own agent to read and use while
working with that person on their problems and projects. They explain how to
carry work through, with the person's purpose, judgment and circumstances at
the centre. People can read them to understand and question the method too.

The [courses](../human-team-courses/README.md) teach project management and
project engineering to people. The manuals give their agents a working method.
The person and agent then learn how to work together through an actual undertaking.

Current development follows Root `AGENTS.md`, the active project entry, owner
steering and applicable product commitments. A manual does not create authority
merely because it is the latest edition.

## Project Management Manual

**Current edition: Consolidated v9.** [Read HTML](Project_Management_for_Human_Agent_Teams_Consolidated_v9.html) · [Markdown source](Project_Management_for_Human_Agent_Teams_Consolidated_v9.md)

Read this manual for the foundation: purpose, accountable reliance, shared
vocabulary, production contracts, dependencies, coordinated work, evidence and
delivery. Its explanations and cases establish the reasoning used by the shorter guides.
It does not impose Chirality repository paths or a fixed staffing arrangement.

Stable discovery link: `docs/alignment-manual/README.md#project-management-manual`.

## Read the collection

Begin with the management manual to understand the method and its shared
[working vocabulary](Project_Management_for_Human_Agent_Teams_Consolidated_v9.md#vocabulary).
A participant already acquainted with the method can return directly to the
relevant chapter. In the Chirality repository, current practice is in Root
`AGENTS.md`, the role files in `agents/`, the selected workflow and the project's
loop entry, not in a manual.

Bring the person's actual problem, context and purposes into that reading.
Discuss consequential interpretations and examine results together. Shared
vocabulary helps participants identify agreement, uncertainty and decision rights;
using the same words does not by itself establish a common understanding.

## Discovery and reliance

The anchor above is a versionless pointer. They reduce stale entry links and
let readers find the current edition without maintaining a second registry.
Their targets can change; that is their purpose and their limitation.

Use the stable link for discovery. Where a decision, requirement or comparison
depends on exact content, identify the resolved edition and source revision in
its existing basis or change record. Git preserves the bytes. Add a content hash
only where a consumer needs one. Changing this index does not silently amend
an accepted requirement or rebind a historical fixture.

The alternatives have different costs. Versionless content would make every
link follow edits but hide edition changes from readers. Fully pinned links
preserve reproducibility but require deliberate updates. This index combines
stable discovery with named editions; current consumers still assess substantive
changes before adopting them. No read receipt or automatic adoption gate is added.

## Read and render

The HTML editions are self-contained, use local fonts and support print and
narrow screens. Edit Markdown and regenerate HTML rather than editing both.
The renderer requires the pinned versions in `requirements.txt`; it fetches no
resources. Use an existing suitable environment or install those dependencies
within the applicable project/host authorization.

For each edition, use its explicit source and output path:

```sh
python3 docs/alignment-manual/render_manual.py \
  --source docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v9.md \
  --output docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v9.html \
  --basis-date <YYYY-MM-DD> --basis-revision <full commit of the source> \
  --edition-label 'Management manual' --metadata-at-end
```

Add `--check` to verify without writing. The displayed revision identifies the
source used for rendering, not human acceptance. Check links and inspect the
result at desktop and narrow widths. Review content before preparing revised
Word/PDF publication layouts; retained earlier print editions remain historical.

## Earlier editions

Earlier editions retain their identities for historical consumers. Their old
procedures do not override current instructions. In particular, App v4's original
project-definition basis named Consolidated v7, Field Book v1 and User Manual v3.
The current App v4 basis states its forward selection separately.

The owner retired the Field Book (v1, v2) and the Chirality Agent User Manual
(v3, v4) on 2026-10-23. The Field Book condensed this manual; the Agent User
Manual restated repository instructions, which are now the only home for current
practice. Recover their text with, for example,
`git show 4ac1315672:docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Field_Book_v2.md`.

- [Consolidated v8 Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v8.md), [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v8.docx), [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v8.pdf).
- [Consolidated v7 Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md).

Still earlier files and review evidence are recoverable from
`archive/pre-manuals-2026-10-09` and `archive/pre-efficiency-cleanup-2026-10-09`.
