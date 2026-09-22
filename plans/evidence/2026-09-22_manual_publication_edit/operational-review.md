# Independent operational-manual review

**Verdict: PASS.** The two findings on the initial candidate are repaired and independently backchecked. No unresolved blocking operational or navigation finding remains on the Markdown and HTML identified below.

## Assignment and independence

Date: 2026-09-22. Reviewer: fresh TASK Type 2 native descendant `/root/operational_review`, assigned by `/root`. No delegation occurred. The reviewer did not author or repair the publication. The author `/root/operations_transfer` made the two repairs after parent coordination; the HTML publisher regenerated the derivative.

The assignment was to compare the new companion guide with preserved v1 and the current repository basis, verify transferred operating details against primary sources, preserve the distinction between historical v3 inputs and live authority, and examine final HTML parity and navigation. Allowed writes were this report and `operational-review-sources.json` only. Shell/filesystem capabilities are broad in the actual host; the role and file boundary are instruction-asserted, not claimed mechanically enforced. Root `AGENTS.md` and `agents/AGENT_TASK.md` supplied active conduct. The other instructions, workflows, skills, and manuscript text were comparison material, not activated methods.

## Exact reviewed state

| Subject | SHA-256 or Git revision |
|---|---|
| Repository source basis | `0a258f145eac41a62de02b06f032ccbc183838ec` |
| Initial User Manual v2 Markdown | `fac5bfec4fa227864e850123d5ad568b4b00eff94223ae63b1b566b57af7de71` |
| Operational-content backcheck before label cleanup | `8e0782a12c9cd845d46b912c2c0dd34d90ea331b2cebd922add27fa356de86da` |
| Final reviewed User Manual v2 Markdown | `6739f5a559c5bae3efcdd8623457e48677fd92e21106410cba5e8e57310ddb1d` |
| HTML before label cleanup | `861abe7b24ff9a5d80b00ead7cd0a56fdd3e3c1aa80497d17368b474a6943698` |
| Final reviewed User Manual v2 HTML | `00f3024074e8e66a2057961bde114e8a48c28bfb46583382baf6d02b9c2f9b2c` |
| Preserved User Manual v1 Markdown | `2b749f8f12dcd803c6017c93fa6e850257f4aaf88b3d07781842a8a4c0d2ab2b` |
| Supplied v3 transfer input | `c245f0ebdd0e88185a085c47c0bb697a5831a6fba94b3418e355a883b3398cf1` |
| Companion v4 at navigation check only | `3655da7e62577c9da8d866c581039076433d7e10deb6e2e94ac9265e0fac7f44` |
| Unchanged HTML renderer | `4d70e13e78307da22d622f511251530f6cb7a206680f1cb35487ea9a18eacc08` |

The independent [source manifest](operational-review-sources.json) records actual paths, inspection extent, hashes, baseline comparison, and checks. No inspected tracked primary source differed from the named repository basis. The external v3 and preserved v1 hashes match the supplied evidence.

## Findings and repair backcheck

### OPR-01 — P2 — Federation output omitted required gitignored storage — RESOLVED

The initial §13 command guidance offered an arbitrary `--out <derived-federation.json>` beside the register, describing it as authorized and rebuildable without retaining its required gitignored standing. The [Task Management contract](../../../workflows/task-management/resources/contract.md), K-TM-2 and federation preflight, require that standing. The [utility](../../../tools/taskmgmt/taskmgmt.py) writes an explicit output without enforcing Git ignoring; its default is `<register-home>/.candidates/federation.json`. Thus a reader following the original command could produce a trackable projection contrary to the method.

The final paragraph and command omit `--out`, name the actual default, require verifying the authorized destination is gitignored, and state that the directory name alone and the utility do not establish this property. This was checked against the implementation and current ignore rules. No register, tool, policy, or live instruction was changed.

### OPR-02 — P2 — Sweep sequence obscured mode selection — RESOLVED

The initial six numbered activities could be read as the work required on every invocation, although harvesting and deferral review are selected modes. The [method's inputs](../../../workflows/task-management/resources/method.md) specify a narrower default when no mode is named: present open-row state and staleness/closure-echo findings, then await direction. Only the invocation-local federation preflight is mandatory before each requested mode.

The final qualifier states both the selected-mode limit and the exact no-mode default before the numbered activities. It preserves the mandatory preflight and leaves ordinary development free of a Task Management entry requirement. The change is complete on the final Markdown hash above.

## Substantive coverage

The complete substantive v1-to-v2 delta and all fourteen supplied v3 application notes were examined. The author's [transfer map](operations-transfer.md) is supported at the following scope:

| Transfer group | Independent result |
|---|---|
| 1.A, 4.A, Appendix A — entry and continuation | Current App/Piping entries and the local-graph method support recovery through maintained pointers, retention of an existing run's pins, phase cursor, holds and owner directions, `none` versus a missing target, and retention of a completed graph. Runtime and PEC retain their own entry and receipt contracts. Removing dated phase instructions improves recovery without dropping their controlling source route. |
| 2.A — proposed PRD method and publication sources | The current index contains no `software-prd`, contains registered `dbm-publisher`, and distinguishes its accepted DOMAIN publication purpose from generic PRD authoring. Historical `PRD_RECORD.md`, archive identity and proposed-method details remain in evidence, without invented availability or adoption. |
| 2.B, 3.A, 3.B — setup and checkpoint transfers | The preparation skill supports the exact minimum control files, creation-only population, existing-empty-file preservation, optional Memory, new-status-only OPEN, and absence of invented dependencies. Grouped snapshot filenames, manifests and pointers match the decomposition resources; the guide retains their adoption qualification and the standard's prospective status. |
| 3.C — Scope of Work | Exact frontmatter, ordered headings, ID width/catalog, qualified references, matrix columns and output/criterion/method coverage match the standard and workflow. Matrix grouping retains identical method sets; deterministic checklist identity/order/text/hash and regeneration are preserved. INIT remains direct production authoring, conversion remains separate, and status/acceptance authority is not inferred. Tool command interfaces are real. |
| 3.D, 3.E — dependencies and SCCs | ANCHOR/EXECUTION, owner-relative direction, source-presence versus fulfillment fields, declared-row preservation and extracted-row retirement match the current v3.1 method. Closure retains its independent inventory, missing/invalid coverage, active EXECUTION-to-DELIVERABLE defaults and immutable evidence. The SCC method owns bounded case records under existing control structure; cut/merge decisions, unresolved non-gating edges and subsequent DepClosure proof are retained. |
| 4.B — bounded execution | Required brief fields, profile selection, check authorization, host/role/method/brief intersection, native descent versus role, truthful enforcement attribution and candidate-specific integration/review limits agree with their current sources. Source integration does not become scope acceptance or release. |
| 4.C — bounded reconciliation | The guide preserves both-direction comparison, warranted permitted edits, exact proposals when writes are outside scope, candidate currency, concurrent-change preservation, supported no-change completion and incomplete missing-input returns. Owning records, future requirements and separate code-repair/authority paths survive the transfer. |
| 5.A — Task Management | With the two repairs above, invocation, federation, harvesting fences, typed relationships and archive identity, PARTIAL limitations, committed-state trigger classes, human dispositions, parent-only local register writes, ordered routing and method-specific receipts match the contract and utility. No automatic promotion, dispatch, foreign write, priority, scope reduction or lifecycle effect is introduced. |
| 5.B — formal concordance | Activation and frozen discovery remain distinct from bounded upkeep. Calibrated wave checking, independent fan-in, fresh reruns, narrow representation-migration eligibility, complete retained verification and escalation, new source-bound R6 derivatives, exact changed-claim multiset accounting and every-deliverable Remaining census are supported. Numeric profile limits remain in the selected primary resource. |
| 5.C — lifecycle | Warranted-empty Remaining, candidate-specific checking basis and human freeze all remain necessary where adopted. Owner-gated work remains open; deleting entries or passing tests does not advance state. Review preserves frozen claims and changes follow the authorized reversal or issued-baseline route. |

The affected main operational passages in supplied §§1.10, 3.6, 4.11 and 5.6 have corresponding destinations through the same reviewed material. The v3 text was used to check transfer coverage, never to establish a live permission or method.

## Practical use and navigation

The existing 21-section structure, contents, named procedure subsection, examples, and source map remain usable. New detail is placed with the operation it explains. Source links lead directly to the exact methods and schemas; the guide supplies enough information to recognize the correct procedure while leaving full invocation contracts in their owning packages. There is no new universal form, project census, development-entry sweep, graph rebuild, or extra approval ritual. Repeated authority distinctions are brief and relevant to the operation where they occur; no further repetition repair is needed for this focused transfer.

The v4 target exists, and its cited sections 1.5, 1.7, 4.3, 4.6, 4.12, 5.4, 5.6, 5.11 and chapter 6 remain present. Targeted reading confirms the companion's reckoning/judgment and unallocated-obligation descriptions remain consistent with the new book. This is a navigation/relationship check, not an independent review of the whole v4 book.

## Final publication-label cleanup

A later bounded parent instruction removed `, Consolidated v4` from the opening book-link label only. Independent inverse replacement restores the earlier reviewed Markdown hash `8e0782a12c9cd845d46b912c2c0dd34d90ea331b2cebd922add27fa356de86da` exactly. The link target, the companion's Version 2/source basis and all operating text are unchanged. No full operating-source review was repeated.

The regenerated HTML has exactly one corresponding label change and two generated source-hash replacements. Reversing those three substitutions restores prior reviewed HTML `861abe7b24ff9a5d80b00ead7cd0a56fdd3e3c1aa80497d17368b474a6943698` exactly. The renderer/style is unchanged. Its read-only `--check` was rerun successfully, and the publisher's refreshed parity/link evidence names the final Markdown and HTML hashes in the table above. The earlier complete operational and parity findings therefore carry forward to the unchanged content; this bounded final delta passes independently.

## Final derivative checks and limits

The unchanged renderer's read-only `--check` passed on the final Markdown and HTML, identifying 22 sections, 29 headings, eight tables and twelve code blocks. Independent parsing also confirmed complete visible-text parity, exact code-block text, source link order, semantic element counts, unique page IDs, in-page link resolution, source hash embedding, local target existence and absence of external assets. The publisher's final paragraph/table/heading/fragment checks bind the same exact hashes and report no failures.

No browser or alternate transport route was used. The prior file-URL policy block remains respected; structural and content parity do not claim visual browser inspection. No Word/PDF inspection is claimed by this operational reviewer. The parent owns those publication checks and the complete book review.

No broad project census, DAG reconstruction, production suite, Task Management sweep, Scope-of-Work operation, method activation, lifecycle act, consumer adoption, Git mutation or release was performed. Unchanged project product details inherited from v1 retain their cited earlier source audit; this review independently checked the current entry/continuation sources and substantive operating changes rather than repeating all four product audits.

**Final independent result: PASS for the identified companion Markdown/HTML and the stated operational-transfer scope.** Later edits require reassessment of their affected claims and derivative evidence.
