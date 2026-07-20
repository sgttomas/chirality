# Candidate Owner Slate — PROPOSAL ONLY

This is a near-miss owner slate for independent V1 review and later human
ruling. Nothing here creates, transfers, or accepts ownership. The exact
population is all 22 rows of `PROPOSED_MAPPING.csv`.

## Proposed grouped rulings

1. **Shell integration and shared presentation:** map `page.tsx` and
   `navigation-intent.ts` to DEL-02-01; treat `chat-markdown.tsx` and its
   sole-imported `ansi.ts` helper as DEL-02-01 primary with DEL-02-03 as the
   only other current production consumer. Designate DEL-02-01 integration
   lead for `globals.css` without semantic transfer, explicitly retaining
   DEL-02-02 Pipeline/Workbench, DEL-02-03 Working Root, DEL-02-04 pane/toolkit,
   DEL-02-05 API-key/runtime-feedback, DEL-05-04 projection, DEL-06-01
   mode/permission, DEL-08-02 persona-routing, DEL-08-05 child-run, and
   DEL-09-06 renderer-security boundaries plus the recorded
   DEL-02-02/DEL-08-03 Pipeline-selector boundary. The owner must also choose
   among DEL-02-01 integration lead, ownerless/shared physical-file treatment,
   and a capability-level split before assigning a path lead; this slate does
   not adjudicate those physical-owner alternatives.
2. **Working-root document UX:** map `document-view.tsx`, `file-picker.tsx`,
   `document-view-state.ts`, and `chirality-window.d.ts` to DEL-02-03, while
   retaining DEL-02-04 attachment UI state and DEL-09-06/server-route
   enforceable attachment security for FilePicker. DEL-06-04 write/edit
   enforcement is not a substitute and has no separately evidenced current
   FilePicker boundary.
3. **Replay and projection:** map the six session/event projection paths to
   DEL-05-04. DEL-05-02 keeps canonical event schema/persistence, DEL-05-05
   keeps ToolResultStore/artifact semantics, DEL-06-01 keeps permission
   semantics, and DEL-08-05 keeps child-run lifecycle/artifact semantics.
   `ansi.ts` is excluded because no replay/transcript implementation imports
   it or ChatMarkdown. For `harness-events-provider.tsx`, shared application
   infrastructure remains an explicit owner alternative. For
   `harness-event-views.ts`, split-by-capability and ownerless/shared projection
   utility remain explicit physical-owner alternatives.
4. **Working-root content route:** select DEL-07-03 as nearest existing owner
   or explicitly designate another physical route-contract integration owner;
   retain DEL-07-01 containment and DEL-02-03 consumption boundaries.
5. **Catalog generation:** map only the generator/check mechanism to
   DEL-06-02; do not centralize ownership of generated catalog semantics.
6. **Electron preload:** designate a physical-file integration owner, or an
   explicit shared implementation boundary, across DEL-02-03 `selectDirectory`,
   DEL-02-05 `apiKey`, and DEL-09-06 `safeStorage`/security interests.
7. **Network-policy fixture:** map `scripted-agent-sdk-proof.ts` primarily to
   DEL-09-06 with a DEL-04-01 evidence edge; do not treat it as packaged proof.
8. **Contract dependency lint:** map the semantic lint to DEL-03-01 and retain
   DEL-09-05 as its release-quality consumer.
9. **PEC evidence:** map both evidence-driver paths primarily to DEL-10-04,
   retaining DEL-10-03's proposal-tool verification interest and F-APP-3.

## Exact proposed population

| Group | Paths | Proposal state |
|---|---:|---|
| Shell integration and shared presentation | 5 | Owner ruling required |
| Working-root document UX | 4 | Owner ruling required |
| Replay and projection | 6 | Owner ruling required |
| Working-root content route | 1 | Owner and integration-boundary ruling required |
| Catalog generation | 1 | Owner ruling required |
| Electron preload | 1 | Integration-owner ruling required |
| Network-policy fixture | 1 | Owner ruling required |
| Contract dependency lint | 1 | Owner ruling required |
| PEC evidence | 2 | Owner ruling required |
| **Total** | **22** | **All remain proposals** |

## Material cautions for the owner

- The prior Remaining container is never the default owner.
- Code and call graphs support candidate selection but do not authorize it.
- The content route and Electron preload have genuine physical-file
  integration ambiguity; a generic rule should not be inferred from either.
- Acceptance of any group should name its retained semantic boundaries.
- `DEL02_01_CHILD_PACKAGE_FIDELITY.csv` is the exact 14-row child-to-package
  choice inventory for groups 1–3; it is evidence, not authority.
- Mapping acceptance alone would not authorize implementation repair,
  lifecycle transition, release, publication, or Remaining closure.
