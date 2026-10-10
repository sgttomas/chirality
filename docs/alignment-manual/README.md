# Manuals for human agent work

These documents explain the management method and its repository application.
Current development follows Root `AGENTS.md`, the active project entry, owner
steering and applicable product commitments. A manual does not create authority
merely because it is the latest edition.

## Project Management Manual

**Current edition: Consolidated v9.** [Read HTML](Project_Management_for_Human_Agent_Teams_Consolidated_v9.html) · [Markdown source](Project_Management_for_Human_Agent_Teams_Consolidated_v9.md)

The general management reference explains purpose, accountable reliance,
production contracts, dependencies, coordinated work, evidence and delivery.
It does not impose Chirality repository paths or a fixed staffing arrangement.

Stable discovery link: `docs/alignment-manual/README.md#project-management-manual`.

## Field Book

**Current edition: v2.** [Read HTML](Project_Management_for_Human_Agent_Teams_Field_Book_v2.html) · [Markdown source](Project_Management_for_Human_Agent_Teams_Field_Book_v2.md)

A short decision and navigation aid for the person directing work. It preserves
the method's distinctions without requiring a universal sequence of records.

Stable discovery link: `docs/alignment-manual/README.md#field-book`.

## Agent User Manual

**Current edition: v4.** [Read HTML](CHIRALITY_AGENT_USER_MANUAL_v4.html) · [Markdown source](CHIRALITY_AGENT_USER_MANUAL_v4.md)

Operational guidance for people and agents working in the current Chirality
repository: Root, App v4 and SWBPIPE. This is not the App product's user guide.

Stable discovery link: `docs/alignment-manual/README.md#agent-user-manual`.

## Discovery and reliance

The anchors above are versionless pointers. They reduce stale entry links and
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
  --source docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v4.md \
  --output docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v4.html \
  --basis-date 2026-10-10 --basis-revision <source-commit>
```

Use the corresponding management or Field Book filenames for the other editions.
Add `--check` to verify without writing. The displayed revision identifies the
source used for rendering, not human acceptance. Check links and inspect the
result at desktop and narrow widths. Review content before preparing revised
Word/PDF publication layouts; retained earlier print editions remain historical.

## Earlier editions

Earlier editions retain their identities for historical consumers. Their old
procedures do not override current instructions. In particular, App v4's original
project-definition basis named Consolidated v7, Field Book v1 and User Manual v3.
The current App v4 basis states its forward selection separately.

- [Consolidated v8 Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v8.md), [Word](Project_Management_for_Human_Agent_Teams_Consolidated_v8.docx), [PDF](Project_Management_for_Human_Agent_Teams_Consolidated_v8.pdf).
- [Consolidated v7 Markdown](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md).
- [Field Book v1](Project_Management_for_Human_Agent_Teams_Field_Book_v1.html).
- [Agent User Manual v3](CHIRALITY_AGENT_USER_MANUAL_v3.html).

Still earlier files and review evidence are recoverable from
`archive/pre-manuals-2026-10-09` and `archive/pre-efficiency-cleanup-2026-10-09`.
No old edition is removed or rewritten by the current revision.
