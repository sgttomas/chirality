# Books on Chirality and project management

These publications develop the reasoning and experience behind Chirality's
practice. People and agents can read and question them together, or explore them
independently. The thesis develops the wider argument; the reflective book below
examines its relationship to actual work. Roles and workflows supply selected
working methods, and each project retains its own commitments and authority.

For practical methods, see the [workflow guide](../../workflows/README.md) and
[roles](../../agents/). The [courses](../human-team-courses/README.md) provide
learning material for people. A book can inform or challenge a practice without
silently changing the instructions governing an undertaking.

## Chirality in Practice

**Successor proposal for author content review: First edition.**
[Read HTML](Chirality_in_Practice_Edition_1.html) · [Markdown source and contents](Chirality_in_Practice_Edition_1.md)

*Chirality in Practice: Reflections on Purposeful Work by People and Agents*
is proposed as a reflective successor to Consolidated v9. It develops the
relationship among the thesis, experience across projects and the shared
library's means of working. It is also material that reflection can question
and revise. Reading it is neither an execution prerequisite nor adoption of
new project obligations. The whole draft, title and changed character remain
subject to the author's review; no new edition has been published.

Stable discovery link: `docs/alignment-manual/README.md#chirality-in-practice`.

## Project Management Manual

**Retained agent-addressed work: Consolidated v9.** [Read HTML](Project_Management_for_Human_Agent_Teams_Consolidated_v9.html) · [Markdown source](Project_Management_for_Human_Agent_Teams_Consolidated_v9.md)

This earlier manual combines explanations with guidance addressed to an agent.
It remains available unchanged for readers and projects that select that use.
The successor proposal has a different character; it does not silently replace
an existing selection of v9 or amend a project's adopted instructions. The manual
explains purpose, accountable reliance, production contracts, dependencies,
coordination, evidence and delivery without requiring one repository layout.

Stable discovery link: `docs/alignment-manual/README.md#project-management-manual`.

## Reading and use

The [thesis](../thesis/README.md) develops the argument, the reflective book
examines practice, and v9 preserves the earlier agent-directed account. Their
purposes overlap without making them interchangeable. Their contents allow a
reader to explore relationships beyond the occasion that first prompted reading.

An external project's agent can use a selected role and workflow under the
project's actual instructions. The books offer explanations and examples for
examination; v9 remains an explicit alternative reading selection rather than
an automatically replaced method. The courses retain their identified manual
references. In Root, current execution practice remains in AGENTS.md, the
selected method and project instructions.

## Discovery and reliance

The named anchors above are discovery pointers. The original
`#project-management-manual` anchor still exposes v9 and its different standing;
`#chirality-in-practice` identifies the successor proposal. A change of title and
character is made explicit rather than presented as an interchangeable edition.

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

For the successor, select its own Markdown and HTML paths with the same renderer
and use `--edition-label 'Chirality in Practice · First edition'`. Commit the
reviewed Markdown before rendering and identify that source commit with
`--basis-revision`; its hash records actual source bytes. The source basis and
rendered form do not establish author acceptance or publication.

Add `--check` to verify without writing. The displayed revision identifies the
source used for rendering, not human acceptance. Check links and inspect the
result at desktop and narrow widths. Review content before preparing revised
Word/PDF publication layouts.

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

- [Consolidated v7 Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md). It stays in the working tree because the `software-prd` and `reverse-engineer-software` workflows cite its chapter 2 for the software PRD sequence.

Consolidated v8 (Markdown, Word and PDF) was removed from the working tree on 2026-10-23; recover it with `git show 4ac1315672:docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v8.md`.

Still earlier files and review evidence are recoverable from
`archive/pre-manuals-2026-10-09` and `archive/pre-efficiency-cleanup-2026-10-09`.
