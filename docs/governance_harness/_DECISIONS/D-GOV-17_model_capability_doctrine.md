# D-GOV-17 — Canonical model-capability doctrine and related dispositions

Status:       PROPOSED — AWAITING OWNER RULING
HumanRuling:  TBD
Ruling SHA:   TBD (conditional per the D-GOV-02 caveat: this record self-declares bind-at-publish; the SHA is recorded at ruling publication)
Date:         2026-07-18 (proposed)
FramedBy:     Owner-directed architecture-evaluation remediation program (2026-07-18); D-APP-61 M3-C precedent (project-local re-home of the runtime capability convention)

## Decision to make

Four separable matters arising from the 2026-07-18 four-lens architecture
evaluation and its owner-directed remediation. Each matter is ruled
independently; unselected matters produce no change. No matter has operative
effect before its ruling.

## M1 — Canonical home for the model-capability doctrine

The only current home of model/capability doctrine is the app-dev project
agent index (`projects/chirality-app-dev/AGENTS.md`, section "Runtime
capability convention", owner-revised 2026-07-12, re-homed under D-APP-61
M3-C). The proposed canonical text is
`docs/governance_harness/_PROPOSALS/D-GOV-17/MODEL_CAPABILITY_DOCTRINE.proposed.md`
(exact bytes, SHA-pinned in the package README). It is a generic redraft: the
substance of the app-dev convention plus the capability-invariance principle,
with no project-local references.

- **M1-A (recommended): canonical section in root `AGENTS.md`.** Place the
  proposed text verbatim as a new root `AGENTS.md` section. Root `AGENTS.md`
  is the runtime doctrine home; this is runtime doctrine. The app-dev section
  is then converted, in a project-fenced follow-up, to a local binding that
  cites the canonical section and retains only its historical rescission
  note.
- **M1-B: standalone `docs/MODEL_CAPABILITY_DOCTRINE.md`** carrying the
  proposed text verbatim, referenced from root `AGENTS.md` by one citation
  line. Same app-dev follow-up as M1-A.
- **M1-C: decline.** The doctrine stays project-local; the app-dev section
  remains its sole home; this proposal package remains a non-authoritative
  record.

Risk/tradeoff: M1-A/B make the doctrine available to every project (piping
currently has no equivalent section) and give the capability-invariance
principle a citable canonical statement; M1-C avoids adding root doctrine but
leaves each future project to re-derive its own convention. Adoption by any
project other than app-dev remains that project's own act through its own
instruments; this ruling compels no project to bind.

## M2 — Instruction-surface validator boundary (codification of the F3 residual)

D-GOV-02 and `docs/CONTRACT.md` already bound machine BLOCKs to "objective
preconditions and hygiene only." The residual gap: no repo-wide rule governs
validators that check instruction, launcher, or loop surfaces, where the
PR #268 near-miss showed a hygiene check can silently become a judgment gate
that rejects owner-adopted text. D-APP-61 Appendix V corrected this for
app-dev only.

- **M2-A (recommended): adopt the following codifying paragraph** as a ruled
  caveat of this record, with a one-line pointer added beside the existing
  D-GOV-02 note in `docs/CONTRACT.md`:

  > Instruction-surface validators — validators that check instruction,
  > launcher, or loop surfaces rather than run artifacts — enforce
  > structural properties and byte parity only (tagged-block equivalence,
  > required-file presence, structural duplication of canonical mechanics),
  > never vocabulary occurrence alone. No validator finding may be
  > constructed such that content the owner has adopted or ruled is
  > mechanically rejected; where ruled text trips such a validator, the
  > validator is presumed defective and is corrected under review — never
  > the ruled text. This generalizes D-APP-61 Appendix V and extends the
  > D-GOV-02 caveat that BLOCKs apply to objective preconditions and
  > hygiene only.

- **M2-B: decline** as sufficiently covered by D-GOV-02 and project-level
  precedent.

## M3 — Scope-of-Work conversion provenance disposition (F4)

The four-document → SOW conversions carry no deliverable-local conversion
records. Central provenance exists:
`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/CONVERSION_CLOSURE/repair_integration/.../PROJECT_MANIFEST.tsv`
binds each production `ScopeOfWork.md` SHA-256 to its integration merge
commit (`74b9804cf…`), with instance evidence under the same run.

- **M3-A (recommended): rule the centralized closure record canonical.**
  The central manifest is the canonical conversion provenance; deliverable-
  local conversion records are not required; forward traceability resolves
  through the central manifest. Recorded in this decision record only — no
  file backfill.
- **M3-B: backfill** one dated conversion-pointer record per converted
  deliverable (53 files) citing the central manifest.

## M4 — MEMORY template disposition (F7a)

`docs/templates/MEMORY_TEMPLATE.md` requires title `# Memory — {{DEL-ID}}`
and five minimum sections. Actual practice is universal and identical:
53/53 deliverable `MEMORY.md` files use `# MEMORY - DEL-XX-YY` with a
`## Decisions And Evidence` section; 0/53 conform to the template. The
divergence is uniform, which makes practice the de facto convention and the
template the outlier.

- **M4-A (recommended): revise the template to codify practice** — title
  `# MEMORY - DEL-XX-YY`; required section `## Decisions And Evidence`;
  optional sections (e.g. `## Open Items`, `## Dependency Note`) permitted
  by topic-then-chronology guidance. No deliverable file changes.
- **M4-B: mass-conform** the 53 `MEMORY.md` files to the current template.
- **M4-C: defer.**

## Caveats to adopt with any ruling

- No matter has operative effect before its ruling; implementations apply
  only the ruled matters' exact staged bytes or enumerated edits.
- M1-A/M1-B implementation places the proposed doctrine bytes verbatim
  (conditional status line replaced as the ruled implementation directs) and
  is verified byte-against the SHA pinned in the package README.
- Project adoption beyond app-dev is offer-only through each project's own
  instruments; nothing here writes any project surface other than the named
  app-dev follow-up.
- A machine PASS from any validator referenced here remains structural
  evidence only, never approval (K-DOMAIN-4 analogue; D-GOV-02).

## Ruling format

Reply with a separable selection, for example: `M1-A; M2-A; M3-A; M4-A`.

<!-- BEGIN OWNER RULING VERBATIM -->
AWAITING_RULING
<!-- END OWNER RULING VERBATIM -->

Canonical ruling-text SHA-256: `TBD_AFTER_OWNER_ACT`
