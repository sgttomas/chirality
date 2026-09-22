# Independent publication review

Status: complete on the exact targets listed below. No unresolved publication finding remains. Suitable for manager fan-in within this bounded review; this is not lifecycle acceptance, a security-sanitizer qualification, or a claim of completed browser/print validation.

Reviewer: `/root/publication_reviewer`, fresh TASK (Type 2), delegated directly by `/root` through native Codex collaboration. No authorship of the publication implementation, no further delegation, no source or Git mutation. The host permits unrestricted access; the write boundary is instruction-based and limited to this review and its source record.

Selected skill: repository `.agents/skills/software-code-review/SKILL.md`. No workflow selected. Scope: `docs/alignment-manual/render_manual.py`, `requirements.txt`, directory `README.md`, the root `README.md` navigation diff, and the finished agent guide Markdown/HTML publication binding. Root owns browser visual inspection. Project-governance editorial accuracy and v2 manuscript content are other reviewers' scopes.

## Findings sent for repair

### P2 — Source HTML can bypass the documented offline-asset validation

Initial location: `docs/alignment-manual/render_manual.py:229–234`, at renderer SHA-256 `b10596a1230fe71604f2192ddc446aab30deae0e49df10982dce25f73a644d22`.

Trigger: retained raw HTML in an otherwise valid Markdown source uses CSS `url()` or `@import`, `<object data="…">`, or `iframe[srcdoc]` containing an externally loaded image. `HTMLAudit` only checks `src`, `srcset`, `poster`, and `link[href]`.

Observed: four independently executed in-memory `render()` cases were accepted and their resource-loading markup survived in the returned HTML. They contradict the asset-rejection claim at directory README line 40 and the emitted self-contained/offline description. The inspected partial guide itself did not contain these forms; this is a renderer contract failure, not an assertion that its current prose loads network assets.

Requested remediation: validate the source fragment before adding trusted page styling/script and conservatively reject unsupported active/resource-bearing HTML while retaining explicit anchors and ordinary semantic markup. Do not silently strip source content.

Disposition: resolved at renderer SHA-256 `caaa10a48f51b79f451b238327cdd57bed9a89de6c97b2c29db3851300dc1e4e`. Read the new `SourceHTMLAudit` and source-token traversal at lines 240–278, its invocation at line 304, and updated README authoring constraints. Independently reran the four reported cases: all reject with specific unsupported-markup errors. Explicit anchors and ordinary Markdown tables/code still render. This is a conservative authoring guard for trusted documentation, not a security-sanitizer qualification.

### P3 — The chapter count also counts the Contents heading

Initial locations: `docs/alignment-manual/render_manual.py:288–289,329`. Every H2 becomes a navigation entry, including the guide's `## Contents`; the mobile label calls the resulting total “chapters.” The final source plan has 21 numbered chapters and one Contents section. Report the count as sections or count chapters separately.

Disposition: resolved in the same repaired renderer. The mobile label (line 371), navigation accessibility labels, and CLI output use “sections.” The independent acceptance fixture with Contents plus Chapter reported two sections.

## Executed checks

- Read all renderer code, pinned requirements, directory README, root README diff, declared tranche, and the publisher's fixture report as evidence leads.
- Ran the repository scope helper against the undertaking's declared write roots. The observed changed and untracked paths stayed within those roots, including the declared root README navigation addition.
- Used existing Python 3.13.14, markdown-it-py 4.2.0, mdurl 0.1.2. No dependency or browser-engine installation and no network access. Local installed distribution metadata confirms markdown-it-py requires Python >=3.10 and has mdurl as its required runtime dependency.
- Ran renderer CLI from `/tmp`: `--help` exited 0; an invalid date, invalid revision, and source/output identity each exited 1 with a specific error. Checks used `-B` and did not write HTML or fixture files.
- Ran four in-memory resource-bypass reproductions by replacing only `Path.read_bytes` during `render()`; no source or temporary fixture file was written. CSS background-image `url`, CSS `@import`, object `data`, and iframe `srcdoc` all passed the initial audit.
- Inspected navigation/responsive/print styles and keyboard affordances statically. This does not establish browser layout, keyboard behavior, or print pagination; those remain root's visual validation.
- Calculated static text/background contrast ratios for body/paper 13.929, muted/paper 6.257, link/paper 7.006, muted/canvas 5.534, table heading 8.930, and code block 10.325. All sampled pairs exceeded 4.5:1. This is not a complete accessibility audit. The fixed page CSS contains no `@import` or `url()` resource mechanism.
- Independently rendered the complete Markdown with the documented CommonMark/table/strikethrough parser configuration, without using the publication renderer for the expected body. After removing only the generated heading IDs and table-scroll wrappers from the published article, its HTML bytes matched the independent parser output exactly. The 343 source link targets also matched in order.
- Audited the full production HTML: 51 unique IDs; 28 headings, each with an ID; seven tables; ten code blocks; both navigation lists contain exactly the 22 H2 targets in source order. No referenced external asset was found. Every generated table-scroll region has its region role, keyboard tabindex, and accessible label.
- Checked all 392 HTML links: 323 local file references resolve to 79 distinct existing targets and 69 in-page links resolve. There are no external links in this edition. The sole cross-file fragment, `../PRD_ROOT.md#531-merge-gate-policy--the-d-8-successor`, matches the heading at `docs/PRD_ROOT.md:484`. The initially absent author source manifest now exists. All eight directory README links and the added root README navigation link also resolve.
- Compared `source-sha256`, `source-basis-date`, and `source-basis-revision` metadata with the source bytes, edition header, and explicit invocation: all match. The content markers each occur exactly once.
- Executed the final CLI `--check` from `/tmp` using `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` and the README's explicit date/revision. It exited 0 and reproduced the published HTML bytes. An initial bare `python3` invocation from `/tmp` selected an interpreter without the pinned dependencies and exited 1 with the documented install message; the existing qualified absolute interpreter resolved that environment difference. No installation was performed.

## Exact reviewed publication targets

Paths are repository-relative. SHA-256 values bind this review to the following working-tree bytes, independently of any later commit identifier:

| Target | SHA-256 |
| --- | --- |
| `docs/alignment-manual/render_manual.py` | `caaa10a48f51b79f451b238327cdd57bed9a89de6c97b2c29db3851300dc1e4e` |
| `docs/alignment-manual/requirements.txt` | `ac981afac84d512ce043af011e6274637949d90e9de4fc114190f55fc322ad10` |
| `docs/alignment-manual/README.md` | `732499bb3548d55d277759c1cb106ddf6230e2c5cf7d48058571be4691fdeee6` |
| `README.md` (navigation addition only) | `c42e7936491f10a462b9db058d22875f7812f95aff87f09e4cf51b9ae9cbeca6` |
| `docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v1.md` (publication source only) | `2b749f8f12dcd803c6017c93fa6e850257f4aaf88b3d07781842a8a4c0d2ab2b` |
| `docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v1.html` | `77bbc449bca0daa3ba4dd3644119a6deaedff3f89f606b26824a0bce504339b5` |

## Limits and return

No browser interaction, responsive viewport rendering, accessibility-tree inspection, screen-reader test, print preview, or printed pagination check was executed by this reviewer. Root owns separate visual validation; this review does not imply that those checks have passed. Static CSS inspection and contrast calculations cannot replace them. No new engine was installed, no network access was used, and no source or Git mutation occurred.

The renderer has been checked as a trusted-document publication tool, not as a hostile-input sanitizer. Repository link checks establish current target existence and the one referenced cross-file anchor, not the target documents' semantic accuracy or future stability. Editorial/project-authority correctness is outside this bounded publication review. Recheck the affected binding and links if any listed publication target changes before integration.
