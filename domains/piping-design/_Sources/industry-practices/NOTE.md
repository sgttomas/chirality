# Note on the Use of These Materials

## What this collection is

This folder is a private knowledge base of piping-design industry practices, gathered from a deliberate cross-section of operators, refiners, midstream and offshore companies, and consensus-standards bodies. Its purpose is to provide *design-judgment context* to a piping-design assistant — the kind of judgment that experienced piping engineers bring above and beyond what the governing codes prescribe.

The collection intentionally does **not** include the underlying codes themselves (ASME B31.x, API 5L/6D/570/520/521, ASTM material specs, NACE corrosion standards, etc.). Code compliance is a separate, downstream concern, validated by industry-accepted piping stress analysis software (CAESAR II, AutoPIPE, ROHR2, START-PROF, etc.) that the user supplies independently. This knowledge base feeds only the *design* stage — helping produce plausible piping designs that the validator can then check for compliance.

## Why this use is justified

This material is **not used for any commercial purpose**. It is a development-time reference base for **open-source software** whose architecture is explicit on this point: the software interfaces with each user's own private knowledge repositories at runtime, and does not redistribute the contents of this folder. The collection here serves only as the corpus against which the design-assistant's reasoning is developed and calibrated, much as an experienced engineer reads many companies' standards over the course of a career to form judgment.

The technical content in every one of these documents is itself a distillation of decades of *open* technical literature — ASME PVP papers, NACE technical committee work, Welding Research Council bulletins, API task-group findings, OMAE and OTC conference proceedings, university research, and countless engineer-to-engineer knowledge sharing at conferences, in plant walkdowns, and across project handovers. The companies that nominally "own" these standards have largely *codified* community knowledge they themselves received freely through that open literature. Continuing that pattern of free knowledge propagation — in a new format, for a new generation of engineers and the tools they will use — is more in keeping with how this knowledge actually got built than locking it up would be.

## How these sources were chosen

Where there were choices, three properties were preferred:

**Age.** Older revisions were favored over newer ones. The 1989 Shell Canada piping classes, the 1993 Shell Pipeline Engineering DEP, the Chevron Gray Manual era, the earlier PIP revisions — these are when the industry's piping judgments crystallized. Most subsequent revisions add incident-driven amendments, vendor-specific notes, or compliance boilerplate; the foundational technical content is essentially unchanged. Older is closer to the durable consensus.

**Breadth of source organizations.** Twelve distinct issuing organizations are represented: Shell (DEPs), Shell Canada, Chevron (Piping Manual / Gray Book), BP (Cherry Point Refinery STPs), Phillips 66 (Refining Engineering Practices), Suncor Energy, Syncrude Canada, Plains Midstream Canada, Oil Search Alaska (Nanushuk Project), WorleyParsons, and the Construction Industry Institute (Process Industry Practices). This cross-organization redundancy lets a reasoning agent triangulate consensus practice rather than echo any single company's house style.

**Authority and recognition.** Within each topic, the most widely cited and most often referenced sources were preferred over project-specific or vendor-promotional documents.

## Acknowledgments

Sincere thanks to the engineering communities at Shell, Chevron, BP, Phillips 66, Suncor, Syncrude, Plains Midstream Canada, Oil Search Alaska, WorleyParsons, and Shell Canada — and to the Construction Industry Institute's Process Industry Practices program — and above all to the many individual engineers whose careers produced the practices captured in these documents. The intent here is to honor and extend that lineage, not to obscure it. Source-organization attribution is preserved in the master index (`00-MASTER-INDEX.xlsx` / `.csv`) precisely so that every contribution remains visible and traceable.

## Pre-processing notes

The PDFs in this folder have been stripped of non-technical front- and back-matter (cover pages, document-control tables, copyright preambles, signature/approval pages, distribution lists, and standalone series-preface boilerplate) so that downstream chunking and embedding sees pure technical content. This was done on a per-document basis with a conservative bias: scope, definitions, abstracts, table-of-contents, references, and any numbered body sections were always retained, as were all technical tables and figures. The boilerplate was removed because in a retrieval system its near-identical recurrence across many documents from the same organization would otherwise pull retrieval toward source identity rather than topical relevance. Source identity is not lost — it lives in the structured metadata of the master index alongside each document, where it can inform retrieval and attribution without polluting the chunk bodies the model reasons over.

---

*Ryan — Chirality (`ryan@chirality.ai`)*
*Note last revised: 2026-05-17*
