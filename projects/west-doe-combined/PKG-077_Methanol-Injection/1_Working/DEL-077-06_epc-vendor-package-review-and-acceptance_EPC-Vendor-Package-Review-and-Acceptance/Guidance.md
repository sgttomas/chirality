# Guidance: DEL-077-06 — EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists to give the EPC Integrator an auditable basis on which to accept the Package Vendor's Methanol Injection package (`PKG-077`) into the larger facility. It separates *vendor-owned* engineering/design/equipment/documentation work from the *integrator-owned* judgement that the package, as delivered, can be integrated, constructed, tied-in, and turned over within the project's interface, constructability, and operability envelope. [Source: `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` PKG-077 responsibility split.]

## Principles

1. **Acceptance is integrator judgement, not vendor self-certification.** The Package Vendor's deliverables (`DEL-077-04`, `DEL-077-05`) are inputs; the acceptance decision belongs to the EPC Integrator. [Source: `DELIVERABLE_REGISTER.csv` rows; `PACKAGE_REGISTER.csv` responsibility split.]
2. **Reference set is fixed and named.** Acceptance is measured against three named EPC-authored deliverables (`DEL-077-01`, `DEL-077-02`, `DEL-077-03`), not against generic convention. [Source: `_CONTEXT.md` Scope.]
3. **Interfaces are the integration surface.** The package's applicable interface types listed in `PACKAGE_REGISTER.csv` are the dimensions along which integration acceptance is evaluated. [Source: `PACKAGE_REGISTER.csv`.]
4. **No silent disposition.** Every review comment, checklist item, and test/inspection record gets an explicit status, owner, and evidence pointer. [ASSUMPTION: standard EPC review-log convention; source slice not located.]
5. **TBD beats invention.** When source material does not establish a criterion (e.g., specific test pass/fail thresholds, code clauses, traceability scheme), record `TBD` rather than fabricating a number. [Skill `four-documents` constraint.]

## Considerations

- **Scope overlap with Cryogenic Unit.** `PACKAGE_REGISTER.csv` records the Gate 6 disposition that "Methanol Injection scope is included with the Cryogenic Unit package scope" while retaining PKG-077 as a distinct workbook-defined package row. Acceptance reviewers should confirm there is no double-acceptance or gapped acceptance with the Cryogenic Unit package. [Source: `PACKAGE_REGISTER.csv`.]
- **No declared dependencies yet.** `_DEPENDENCIES.md` records no declared upstream/downstream. Until declared, acceptance work should treat DEL-077-01 / -02 / -03 / -04 / -05 as functional upstream inputs even though they are not formally declared. [Source: `_DEPENDENCIES.md`; `DELIVERABLE_REGISTER.csv`.]
- **No deliverable-specific source slices copied.** `_REFERENCES.md` notes that no deliverable-specific source slices were copied during PREPARATION; the workbook row 72 and `DBM-Deepcut/4-25_Deepcut_DBM.md` are cited but not locally sliced. Detailed acceptance criteria that depend on those source texts remain `TBD` until sliced. [Source: `_REFERENCES.md`; `PACKAGE_REGISTER.csv`.]
- **Vendor documentation gap.** `DEL-077-05` carries `ART-CF38039426` "TBD vendor document register" because detailed vendor-document requirements are not present in current source material. Acceptance criteria for vendor documents will inherit this gap until source slices land. [Source: `ARTIFACT_REGISTER.csv` row ART-CF38039426.]

## Trade-offs

- **Breadth vs. defensibility of the acceptance log.** A wide-coverage review log catches more integration gaps but increases cycle time; a narrow log closes faster but risks accepting integration defects. The PKG-077 interface list defines a defensible minimum breadth. [Source: `PACKAGE_REGISTER.csv` interface list.]
- **Accept-with-exceptions vs. block on every open item.** Some open items (e.g., minor documentation cleanup) do not impair integration; others (e.g., missing interface evidence) do. The acceptance gate decision record should distinguish these. [ASSUMPTION: industry-standard "accept with exceptions" pattern; specific policy TBD.]
- **Integrator-redo vs. vendor-redo.** When source material shows a vendor deliverable does not meet datasheet (DEL-077-02), the trade is between integrator-side workaround and forcing vendor rework. The responsibility split in `PACKAGE_REGISTER.csv` favors vendor rework for engineering/design/equipment defects. [Source: `PACKAGE_REGISTER.csv`.]

## Examples

No source-grounded worked example is available in the currently accessible reference set. Examples will be added when source slices for vendor review logs or acceptance checklists are sliced into `_REFERENCES.md`. [TBD — pending source slice availability.]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-077-06-01 | PKG-077 retained as a distinct package row while Gate 6 disposition states "Methanol Injection scope is included with the Cryogenic Unit package scope." Acceptance boundary between PKG-077 and the Cryogenic Unit package is unresolved. | `PACKAGE_REGISTER.csv` row PKG-077 (Note column) | `PACKAGE_REGISTER.csv` row PKG-077 (workbook row 72 retains separate package) | Datasheet Conditions; Specification Scope (REQ-077-06-004); Procedure Steps | Treat PKG-077 acceptance as scoped to the package boundary defined by workbook row 72 only; cross-reference Cryogenic Unit acceptance in the gate decision record. | TBD |
| C-077-06-02 | `_REFERENCES.md` lists `DBM-Deepcut/4-25_Deepcut_DBM.md` as cited source material but no source slice has been copied; acceptance criteria depending on that source remain unresolvable. | `_REFERENCES.md` Missing/Deferred References | `PACKAGE_REGISTER.csv` PKG-077 source citation | Specification REQ-077-06-008; Standards row for `DBM-Deepcut`; Procedure Steps | Slice the DBM-Deepcut sections relevant to vendor package review into `_REFERENCES.md` before Pass 3 / before acceptance execution. | TBD |
