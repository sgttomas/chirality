# Chat transcription — owner ruling on HGD-1, HGD-3 and FC-1 to FC-3, 2026-09-27

**Epistemic status: CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING.** This file
transcribes an owner act given in chat, as relayed verbatim by the
coordinating session. Its authority comes from the owner's words, not from this
file.

## The owner's words (verbatim)

Typed by the owner in chat on 2026-09-27, in answer to the package in
`RECOMMENDATION.md` (this run folder), whose proposed reply it adopts word for
word:

> HGD-1: invert DEP-02-01-006 to UPSTREAM INTERFACE; HGD-3: close without emitting; FC-1: resolve DEP-02-01-012 to DEL-05-03; FC-2 and FC-3: close without emitting.

## What it decides

- **HGD-1.** DEP-02-01-006 (DEL-02-01 and DEL-08-02) becomes `Direction=UPSTREAM`,
  `DependencyType=INTERFACE`. HGD-1 is closed.
- **HGD-3.** The DEL-02-01-V3-01 prerequisite on DEL-02-02-V3-03 is closed
  without a register row. HGD-3 is closed.
- **FC-1.** DEP-02-01-012 (the redaction helper) is resolved to the deliverable
  target DEL-05-03, with the field values of `RECOMMENDATION.md` § FC-1
  (`Explicitness=IMPLICIT`, `Confidence=MEDIUM`).
- **FC-2 and FC-3.** Both fenced candidates are closed without a register row.

Each ruled row keeps its ID; no row is added, retired or deleted.

## Boundary

The ruling decides these five items in the DEL-02-01 register only. It changes
no other register, no scope, no lifecycle state and no pointer.
