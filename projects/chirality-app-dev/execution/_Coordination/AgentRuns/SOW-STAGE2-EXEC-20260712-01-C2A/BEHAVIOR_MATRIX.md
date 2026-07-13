# C2A Production-Format Behavior Matrix

| Observed/requested state | Resolution | Valid | Selected production documents | Evidence |
|---|---|---:|---|---|
| Complete legacy four-document kit only | `LEGACY_FOUR_DOC` | yes | all four legacy production documents | scanner test; full suite |
| Structurally valid `ScopeOfWork.md` only | `SOW_V1` | yes | `ScopeOfWork.md` | scanner test; full suite |
| Complete dual, exact isolated path, exact `D-GOV-16@<sha>`, matching body marker | `MIGRATION_DUAL` | yes | `ScopeOfWork.md` only | scanner test |
| Complete dual in normal project/API scan | `AMBIGUOUS` | no | none | route test; scanner test |
| Complete dual with authority/body-marker mismatch | `AMBIGUOUS` | no | none | scanner mismatch test |
| Partial legacy, with or without Scope of Work | `INVALID` | no | none | scanner partial test; route incomplete-kit test |
| Invalid or unreadable Scope of Work | `INVALID` | no | none | scanner structural-invalid test |
| No production contract at or beyond `INITIALIZED` | `INVALID` + error | no | none | scanner initialized-missing test |
| No production contract at `OPEN` | `INVALID`, warnings allowed | no | none | review-found regression test after repair |
| Requested format disagrees with resolution | resolved state + `requested_format_mismatch` | no | none for invalid/ambiguous state | scanner mismatch test |

`DocumentView` consumes `selectedProductionDocuments`, always retains the
control-plane choices, keeps `_STATUS.md` as its default, resets that default
when the deliverable selection changes, and contains no Stage-1 feature flag.
DOMAIN/KTY discovery remains on its independent scan path; it is not passed
through the PROJECT/SOFTWARE production-format resolver.
