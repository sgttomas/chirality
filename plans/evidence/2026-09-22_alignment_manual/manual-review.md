# Manual review integration record

Date: 2026-09-22. Basis: `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`.

The human-readable assessment is [MANUAL_REVIEW_v1.md](../../../docs/alignment-manual/MANUAL_REVIEW_v1.md); the full revised text is [Consolidated v2](../../../docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.md). This integration record preserves the review assignment, complete coverage, actual child execution, and treatment of every returned recommendation. Exact applied original/replacement text is in [v2-edit-manifest.json](v2-edit-manifest.json).

## Role, mechanism, and write boundary

The manager acted as HELPS_HUMANS, Type 1, native child `/root/manual_review_manager`, under HELP_HUMAN `/root`. Root `AGENTS.md` and `agents/AGENT_HELPS_HUMANS.md` were loaded. The manager also read `agents/AGENT_TASK.md` deliberately to form bounded child assignments; that was a comparison/dispatch consultation, not a role switch. Workflow bodies were inspected as documentary evidence; no reusable workflow was authored, registered, revised, or executed.

Three actual Type 2 children were launched with `collaboration.spawn_agent`, `fork_turns="none"`, explicit TASK role loading, disjoint continuous manuscript ranges, source verification, and two-file evidence-only write boundaries. Each executed and returned an assessment; these were delegated-harness-native descendants, not Chirality-managed `delegate_agent` sessions. No model override was requested. The actual backend model/effort is not inferred from historical project records. All children were forbidden to delegate and report no descendants.

| Actual child ID | Supplied assignment | Return |
|---|---|---|
| `/root/manual_review_manager/manual_ch1_ch2` | Root entry, TASK role, undertaking brief, complete lines 1–1212, bounded current-source checks; write only its report/manifest | [Review](review-ch1-ch2.md), [source/coverage manifest](review-ch1-ch2-sources.json) |
| `/root/manual_review_manager/manual_ch3_ch4` | Same supplied instruction requirements; complete lines 1213–2625 and relevant current-source checks; two-file scope | [Review](review-ch3-ch4.md), [source/coverage manifest](review-ch3-ch4-sources.json) |
| `/root/manual_review_manager/manual_ch5_ch7` | Same supplied instruction requirements; complete lines 2626–3731 including vocabulary and source notes; two-file scope | [Review](review-ch5-ch7.md), [source/coverage manifest](review-ch5-ch7-sources.json) |

The host exposes unrestricted filesystem access, enabled network and approval policy `never`. Read-only and write-path restrictions were instruction boundaries, not separately enforced OS sandboxes. The initial manager brief permitted evidence files only. The parent then explicitly authorized writing the complete incremented v2 and public assessment, followed by byte-exact extraction of `assets/Figure_1_1.png`; those amendments were received before those writes. The guide/README/HTML and Git closeout remain owned by other participants. No original manuscript, project record, live pointer, accepted doctrine, workflow, branch, commit, push, or merge was changed by this manager.

## Continuous coverage

The ranges 1–1212, 1213–2625 and 2626–3731 partition all 3,731 original lines with no gap or overlap. Each reader attests complete continuous reading including source notes, figures, captions, tables and blank lines. Initially truncated displays were explicitly excluded or repaired by untruncated rereads. The manager read every final assessment, inspected material source counterparts independently, and evaluated all proposed modifications before generating v2.

| Portion | Heading/body/source-note allocation | Reader |
|---|---:|---|
| Title, contents, Preface | 1–44 | `manual_ch1_ch2` |
| Chapter 1 | 45–544 | `manual_ch1_ch2` |
| Chapter 2 | 545–1212 | `manual_ch1_ch2` |
| Chapter 3 | 1213–1856 | `manual_ch3_ch4` |
| Chapter 4 | 1857–2625 | `manual_ch3_ch4` |
| Chapter 5 | 2626–3478 | `manual_ch5_ch7` |
| Chapter 6 | 3479–3559 | `manual_ch5_ch7` |
| Chapter 7 | 3560–3676 | `manual_ch5_ch7` |
| Working vocabulary | 3677–3731 | `manual_ch5_ch7` |

Original manuscript SHA-256: `2af9b747a60a0cdf13660c6c8a38dd4d927ff24f28312cd7096ad629e3db34d9`. The preserved originals were not rewritten. Figure 1.1 was extracted exactly from the supplied DOCX, visually compared and checked against its XML placement/caption; [extraction evidence](figure-extraction.json) records the asset SHA and source member. The temporary duplicate used for viewing was removed after canonical placement.

## Disposition of all returned recommendations

IDs are the reviewers' own labels; M IDs identify edit-manifest groups. “Guide” means the observation was delivered to Root for the companion operational guide, not that this manager claims to have edited that guide.

| Reader finding | Treatment | Reason or applied group |
|---|---|---|
| R1 | Applied, combined | Current adoption, preserved pins, project-specific entry, sources: M02/M06/M11. |
| R2 | Applied | Draft/unregistered `software-prd` at first body mention and source availability: M07. |
| R3 | Applied | Dated application/provenance note and actual review links: M01/M02/M06. |
| R4 | Applied in part; guide detail | Type terminology and actual role/enforcement added: M04. Full role/method/skill/tool taxonomy belongs in the operational guide; existing body already distinguishes their main purposes. |
| R5 | Applied | Initial development versus continuation of accepted work: M03. |
| R6 | Applied | Supported inference and material-gap clarification: M03. |
| R7 | Retained existing text; guide | Original §4.10 already states standing Git authority and rejects invented per-merge gates. No duplicate repository paragraph added to §1.7. |
| R8 | Applied | Source/decision network and attention views: M05. |
| R9 | Applied | Current preparation skill and legacy compatibility: M08/M09. |
| R10 | Applied | Exact asset restoration A01; no image reconstruction or prose change. |
| R optional PRD repetition trim | Deferred | The repetition supports different teaching contexts; no clear correction required. Recorded as an optional future editing pass. |
| C34-01 | Applied | Loop standing, current checks and source counterparts: M02/M06. |
| C34-02 | Applied | Phase cursor/pin preservation, actual AgentRuns examples, pointer maintenance and source-qualified methods: M02/M06. |
| C34-03 | Applied | Bound no-receipt/no-handoff statements: M11. |
| C34-04 | Applied | Active legacy comparison and published D-GOV-16 decision: M09. |
| C34-05 | Applied | Default granularity repair and in-flight adoption: M10. |
| C34-06 | Applied | Short actual mechanism/role/enforcement addition at §4.5: M04. The existing declared HELP_HUMAN read-only ceiling remains unchanged. |
| C34-07 | Applied | Actual source evidence and current skill kinds: M06/M08. |
| C34-08 | Applied through common note | Author's phase model and no implied current stage are explicit in M02. Existing §1.7 already denies numerical percentage measurement; no repeated Chapter 3 warning added. |
| E1 | Applied through common note | Four-project applicability and selected-run continuity: M02. |
| E2 | Applied | Chapter 5 and glossary continuation qualifiers: M11. |
| E3 | Applied | Chapter 5/7 source standing: M06. |
| E4 | Applied | Shared Revision 2/D-GOV-44 versus prospective run rider: M10. |
| E5 | Applied | SOW artifact scope and active legacy forms: M09. |
| E6 | Applied | Authorized edits/no-change/proposal completion meaning: M13, cross-referencing existing §4.11. |
| E7 | Applied in part; guide detail | Type glossary and §4.5 actual-role delivery: M04. Avoid adding two operational paragraphs to the reflective conclusion; guide receives full entry/dispatch account. |
| E8 | Retained existing text; guide | Existing §4.10 already distinguishes standing Git from acceptance/release. No duplication in the intentionally brief delivery chapter. |
| E9 | Guide and provenance note | The manuscript is broader than the App MVP; its external capability reference remains attributed historical input. Current Codex-only qualification and actual-host verification belong in the guide. No vendor page was newly verified. |
| E10 | Applied | Removed “accepted Chapter 5”; also removed “accepted manual chapters” in Chapter 3 sources: M12. |
| E11 | Applied with author meaning retained | Preserved last-resort Task Management wording and added no redefinition of governed `DEFERRED`, no automatic promotion, no loss of owning obligation: M14. |

## Source standing and synthesis

The public assessment identifies six distinct classes: current repository conduct; adopted App/Piping entry; shared standards with project/run adoption limits; prospective runtime interface; original proposals/historical archives; constructed/domain examples and claims whose underlying evidence was not revalidated. The latest loop development is explained using the merged implementation record, current project instructions and notices rather than obsolete template priority.

The result preserves the manual's useful argument while making present use less ambiguous. The most consequential editorial choice is to keep operating procedures in the companion guide and keep the book's explanatory voice. The graph is not promoted to authority, the newer bounded method does not replace active corpus reconciliation, and source existence is not represented as execution, acceptance or qualification.

No external fact-check was necessary for these repository corrections. The original author directions, source ZIPs, external consultation dates and retrospective case evidence were not independently reconstructed. No empirical productivity or current project-completion claim is added. [Manager source evidence](manual-review-sources.json) preserves loaded paths/hashes; the child manifests preserve fuller source-read boundaries.

The larger undertaking retains final review of the combined guide/manual/HTML candidate, rendered inspection, required repository checks and Git closeout. This manager's mechanical checks concern manuscript identity, complete reading coverage, edit replay, original anchor retention, source links and the restored figure; they are not a replacement for independent candidate review or human acceptance.
