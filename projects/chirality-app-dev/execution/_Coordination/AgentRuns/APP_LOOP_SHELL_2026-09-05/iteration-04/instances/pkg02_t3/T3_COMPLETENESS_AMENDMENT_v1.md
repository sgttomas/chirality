# T3 completeness matrix and bounded amendment v1

OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: finish the feasible Files/Document type and menu behaviors in target §§5.2–5.5 within the existing seventeen source/test paths, retaining explicit PDF/CSP and independently owned later-tranche boundaries.
JudgedBy: WORKING_ITEMS /root/pkg02
OwnerCaseSelection: NONE
RejectedAlternatives: treating all images or JSON as an unsupported handoff silently omits accepted rendering; editing shared ChatMarkdown/globals/state broadens the fence; raw SVG/HTML insertion or CSP relaxation is unsafe and unauthorized; applying the D108 text cap to all resources misstates authority; a folder chooser cannot grant no-folder session or cross-root runtime capability; hiding incomplete accepted features behind an unqualified completion claim is false.
RationaleArtifact: execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t3/T3_COMPLETENESS_AMENDMENT_v1.md
IndependentVerifier: initial /root/pkg02/t3_review CHANGES_REQUESTED at reviewer/REVIEW_RETURN.md; its scope and source findings remain historical. Fresh entire-revised-diff software review and parent governed refutation required; no future verdict inferred.
EffectStatus: HELD
PreservedGates: D64 §5.1 classes1–10; original17-file fence, no global/helper/state/policy/Root/contract writes or new dependencies; current CSP/IPC sender/root containment; original Remaining/lifecycle/Checking SHA and D108 in-panel PDF requirement; no owner/release/acceptance/merge act; APP-HOLD; complete focused/global/browser/native proof, A1 re-stage, existing primary/session guards and truthful partial closeout.

Actual effect: parent explicitly approved this bounded completeness work as agent implementation choices. Current author revision3 repair is in progress under REVIEW_REPAIR_AMENDMENT_v1.md. This new immutable amendment precedes the additional type/menu effects below; no prior frozen evidence is rewritten. Governed landing remains HELD.

## Source and ownership matrix

Accepted meaning is current DEL-02-03-V3-01 Remaining and its cited target/plan; neither target nor this matrix is a new work queue. D108 Q4a/Q4b supersedes old PDF/Office/text-size choices. Existing SOW and dependency/guard meaning remains unchanged.

| Source | Requirement and current disposition | Bounded completion or explicit residual |
|---|---|---|
| §5.2 | Default tree, directory toggle, keyboard arrows/Enter/Space, file buttons | Preserve bounded actual tree API and legacy consumers; verify actual keyboard/action effects. |
| §5.2 | Selected file highlight while open | Preserve selected path representation consistently; verify selection hint, breadcrumb and actual opened target. No claim invisible underlying tree is visible. |
| §5.2 / §4.1 | Choose folder/root basename footer, no-folder Files copy | Add through existing WorkspaceProvider chooser/validation; use exact friendly no-folder message. Preserve active-session/primary semantics and existing limitations. No hidden root, new no-folder session or runtime rebinding. |
| §5.3 | Markdown headings/lists/tables/code/links; title first h1 or filename; name/mtime | New file viewer may consume installed ReactMarkdown/GFM locally, leaving shared ChatMarkdown and legacy viewer untouched. Render safe markup; local working-root links open via existing panel callback and bounded endpoint; external HTTP(S) links retain outside-app behavior. Reject unsafe schemes and traversal. |
| §5.3 | Expanded readable measure/type | Scope component style to expanded file document, retaining center visibility and actual responsive scroll proof. |
| §5.3 | Ask/Attach/quote selection tools | T4-owned DEL-02-03-V3-02; not selected here. No fake action or claim. |
| §5.4 | Text/log/YAML/TOML/code with wrapping and hover line numbers | Implement in DocumentView with bounded rendering, accessible text and real line association. D108 text cap is10MiB; no old force/Load-anyway bypass. |
| §5.4 | CSV first500 logical rows | Preserve actual CSV parser behavior and table with safe bounded columns, disclose truncation. |
| §5.4 | JSON folded tree | Implement safe recursive/iterative folded presentation within bounded depth/item budget; malformed JSON displays truthful error/raw text fallback. Preserve opaque keys, no prototype mutation or execution. Explain rendering truncation; no invented runtime schema. |
| §5.4 | PNG/JPEG/GIF/SVG/WebP image fit, natural size click | Add bounded descriptor image path/MIME handling and img-only rendering. SVG never enters raw DOM. Direct response must have safe download disposition; verify scripts/external fetch cannot run. No CSP loosen/override, no object/embed/webview. Large resources receive size+handoff rather than unbounded decoding. |
| §5.4 + D108 | PDF built-in viewer | Current Electron iframe unavailable due unchanged CSP; usable default-app handoff remains partial. D121 proposal is undecided; standalone browser preview is not native PDF proof. |
| §5.4 + D108 | Office QuickLook + Open default; other formats handoff | Actual native fixture evidence required. Add Reveal action below; errors must be truthful and accessible. PDF/QuickLook uncapped. |
| §5.5 | Files Refresh/Reveal root/Copy root | Refresh/copy exist; add validated directory Reveal through bounded new action. Clipboard success/failure accessible. |
| §5.5 | Document Reveal/Copy/Open/Reload/TOC | Complete within existing component/main/preload/endpoint-local policy/tests. Attach deferred only under T4 ownership. TOC must navigate rendered headings, handle duplicates and ignore code fences. |
| §5.5 | Session parent/summary/id | Already activated in REVIEW_REPAIR_AMENDMENT_v1.md; exact recorded parentage and guard only, deterministic disclosed metadata summary. |
| §5.5 | Who-is-working Refresh | Existing recorded agents/session refresh, preserve real content and selection guards. |
| §5.5 | Activity/Settings menus | T5/T6 owned elsewhere, no placeholders or fake completion. |
| §5.1 / D108Q5 | Pop-out | Explicitly deferred by owner; no window policy expansion. |

## Exact action and resource design choices

Keep the existing document bridge and same sender policy. Extend its discriminated action contract with `reveal` for `{projectRoot,target}` and `reveal-root` for `{projectRoot}` (target must be absent for root action). Main calls only Electron `shell.showItemInFolder` on the validated canonical target. File reveal uses existing regular-file/descriptor/containment validation; root reveal uses a separate validated existing-directory branch with absolute/canonical/instruction-root separation and access checks. It must not change file-only GET/open/QuickLook guards to accept directories. Unknown actions and malformed payloads fail without native effects. No arbitrary path/URL or shell command execution bridge. Surface thrown native errors; actual Finder UI proof is separate from unit callbacks.

For images select a 2MiB decoded-input byte guard as an explicit bounded engineering default, informed by the target's old generic size guard but not asserted as a new owner criterion or the D108 text cap. Report actual size and a native handoff above the guard. PDF and QuickLook remain uncapped, text stays10MiB. Stream permitted binary responses from validated descriptors, cap observed image reads and handle changes/mismatch/error without buffering arbitrary files. No claim that byte limits alone prevent decoder risk; actual SVG/invalid/mislabeled-image tests and browser behavior are required. If the existing policy cannot safely support a listed image format within this fence, return a concrete blocker before weakening it.

TOC/local Markdown rendering may import installed ReactMarkdown and remarkGfm in DocumentView; no dependency or shared helper mutation. The new file-only renderer must preserve safe external links, bounded same-root navigation, heading anchors and legacy document behavior. Do not infer a local path from arbitrary external URLs or decode traversal into a permitted file. Display errors for unavailable targets. JSON rendering must be bounded for adversarial nesting/width without changing raw file truth.

## Evidence and review

Author records exact implemented coverage against this matrix and all residuals, runs meaningful current endpoint/component/native-handler tests, preserves failures and all older freezes, then returns a new whole-source manifest/diff. Fresh reviewer assesses all changed bytes and native sender/path/image/direct-response/JSON/local-link/clipboard/TOC/resize behavior. Manager fixtures must include normal and hostile SVG, raster image, JSON/malformed/deep JSON, local Markdown link and duplicate/code-fenced headings; browser proof includes900px/960px/1440px, expanded view, themes and primary continuity. Real Electron proof uses actual UI actions through main for Office/Reveal/default-app; no mocked native-display claim.

Ontology: these are file-presentation conveniences and explicit native handoffs; runtime/session truth and owner-selected PDF semantics remain unchanged. Epistemology: exact target type/menu table and D108 ground owed behaviors; implementation safety and rendering limits remain disclosed engineering judgments, tested rather than claimed authoritative. Praxeology: one source author inside17 paths, independent full review, then serialized global/render/native evidence; separate D121 packet and parent routing. Axiology: accessible usable files, bounded resource use, truthful errors and preserved primary dialogue, without evading security or acceptance gates.
