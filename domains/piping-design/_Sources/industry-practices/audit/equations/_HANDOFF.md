# Industry Practices Equation Audit Handoff

T21 decision: EQUATION_AUDIT is required before downstream canonical use.

## Scope

- Source Markdown: `/Users/ryan/ai-env/projects/chirality/domains/piping-design/_Sources/industry-practices/industry-practices.md`
- Audit root: `/Users/ryan/ai-env/projects/chirality/domains/piping-design/_Sources/industry-practices/audit/equations`
- Source documents with display equations: 20
- Display equations: 94
- Pages with display equations: 54
- Crops: not generated in this initialization pass
- Review allowance at closure: `ALLOW_UNREVIEWED=0`

## Current State

| Source | Equations | Pages | Verified | Flagged | Backcheck | Unreviewed | Review HTML |
|---|---:|---:|---:|---:|---:|---:|---|
| `01-overall-piping-design-standards-07` | 3 | 1 | 0 | 0 | 0 | 3 | [01-overall-piping-design-standards-07](audit/equations/01-overall-piping-design-standards-07/working/equations.html) |
| `01-overall-piping-design-standards-08` | 6 | 2 | 0 | 0 | 0 | 6 | [01-overall-piping-design-standards-08](audit/equations/01-overall-piping-design-standards-08/working/equations.html) |
| `01-overall-piping-design-standards-10` | 20 | 10 | 0 | 0 | 0 | 20 | [01-overall-piping-design-standards-10](audit/equations/01-overall-piping-design-standards-10/working/equations.html) |
| `03-piping-materials-and-line-classes-08` | 1 | 1 | 0 | 0 | 0 | 1 | [03-piping-materials-and-line-classes-08](audit/equations/03-piping-materials-and-line-classes-08/working/equations.html) |
| `03-piping-materials-and-line-classes-09` | 1 | 1 | 0 | 0 | 0 | 1 | [03-piping-materials-and-line-classes-09](audit/equations/03-piping-materials-and-line-classes-09/working/equations.html) |
| `03-piping-materials-and-line-classes-15` | 11 | 6 | 0 | 0 | 0 | 11 | [03-piping-materials-and-line-classes-15](audit/equations/03-piping-materials-and-line-classes-15/working/equations.html) |
| `03-piping-materials-and-line-classes-17` | 1 | 1 | 0 | 0 | 0 | 1 | [03-piping-materials-and-line-classes-17](audit/equations/03-piping-materials-and-line-classes-17/working/equations.html) |
| `07-stress-flexibility-and-mechanical-analysis-03` | 5 | 2 | 0 | 0 | 0 | 5 | [07-stress-flexibility-and-mechanical-analysis-03](audit/equations/07-stress-flexibility-and-mechanical-analysis-03/working/equations.html) |
| `10-shop-and-field-fabrication-06` | 1 | 1 | 0 | 0 | 0 | 1 | [10-shop-and-field-fabrication-06](audit/equations/10-shop-and-field-fabrication-06/working/equations.html) |
| `12-thermal-insulation-and-heat-tracing-05` | 1 | 1 | 0 | 0 | 0 | 1 | [12-thermal-insulation-and-heat-tracing-05](audit/equations/12-thermal-insulation-and-heat-tracing-05/working/equations.html) |
| `13-painting-coatings-and-corrosion-protection-05` | 3 | 2 | 0 | 0 | 0 | 3 | [13-painting-coatings-and-corrosion-protection-05](audit/equations/13-painting-coatings-and-corrosion-protection-05/working/equations.html) |
| `13-painting-coatings-and-corrosion-protection-06` | 2 | 2 | 0 | 0 | 0 | 2 | [13-painting-coatings-and-corrosion-protection-06](audit/equations/13-painting-coatings-and-corrosion-protection-06/working/equations.html) |
| `14-non-metallic-and-specialty-piping-05` | 11 | 8 | 0 | 0 | 0 | 11 | [14-non-metallic-and-specialty-piping-05](audit/equations/14-non-metallic-and-specialty-piping-05/working/equations.html) |
| `14-non-metallic-and-specialty-piping-06` | 2 | 1 | 0 | 0 | 0 | 2 | [14-non-metallic-and-specialty-piping-06](audit/equations/14-non-metallic-and-specialty-piping-06/working/equations.html) |
| `15-hot-tapping-and-leak-repair-02` | 1 | 1 | 0 | 0 | 0 | 1 | [15-hot-tapping-and-leak-repair-02](audit/equations/15-hot-tapping-and-leak-repair-02/working/equations.html) |
| `15-hot-tapping-and-leak-repair-03` | 7 | 5 | 0 | 0 | 0 | 7 | [15-hot-tapping-and-leak-repair-03](audit/equations/15-hot-tapping-and-leak-repair-03/working/equations.html) |
| `16-cross-country-pipelines-and-offshore-01` | 6 | 3 | 0 | 0 | 0 | 6 | [16-cross-country-pipelines-and-offshore-01](audit/equations/16-cross-country-pipelines-and-offshore-01/working/equations.html) |
| `16-cross-country-pipelines-and-offshore-03` | 9 | 3 | 0 | 0 | 0 | 9 | [16-cross-country-pipelines-and-offshore-03](audit/equations/16-cross-country-pipelines-and-offshore-03/working/equations.html) |
| `16-cross-country-pipelines-and-offshore-04` | 2 | 2 | 0 | 0 | 0 | 2 | [16-cross-country-pipelines-and-offshore-04](audit/equations/16-cross-country-pipelines-and-offshore-04/working/equations.html) |
| `17-specific-service-utility-systems-01` | 1 | 1 | 0 | 0 | 0 | 1 | [17-specific-service-utility-systems-01](audit/equations/17-specific-service-utility-systems-01/working/equations.html) |

## Gate 2 Review Instructions

Open each `equations.html`, compare every extracted display equation against the page image, then export verified/flagged sidecars from the browser UI into that source document's `working/` folder. After exports are present, run EQUATION_AUDIT Phase 3 for any flagged equations, then backcheck and close to immutable snapshots.

## Notes

- The 88 source PDFs without `$$...$$` display equations are out of scope for EQUATION_AUDIT.
- Inline math occurrences were not counted as display equations by the current EQUATION_AUDIT extractor.
- The audit HTML folders include a `pages` symlink to the corresponding PDF2MD work directory so page PNGs render in the review UI.
