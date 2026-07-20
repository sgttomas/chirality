# Retained D-APP-70 Boundaries

The following boundaries are current applied constraints, not proposal-only
alternatives. A physical or primary mapping never transfers a retained
semantic, consumer, security, evidence, or integration boundary.

1. **Shell integration and shared presentation.** DEL-02-01 is the physical
   integration lead for `globals.css`, with DEL-02-02 Pipeline/Workbench,
   DEL-02-03 Working Root, DEL-02-04 pane/toolkit, DEL-02-05 API-key/runtime
   feedback, DEL-05-04 projection, DEL-06-01 mode/permission, DEL-08-02
   persona routing, DEL-08-05 child-run, DEL-09-06 renderer-security, and the
   DEL-02-02/DEL-08-03 Pipeline-selector boundary retained. DEL-02-03 remains
   the ChatMarkdown/ANSI consumer; DEL-08-02 retains navigation persona/guard.
2. **Working-root document UX.** DEL-02-01 remains shell host; DEL-03-03
   remains DocumentView route dependency; DEL-09-04 remains renderer-typing
   verification consumer. FilePicker retains DEL-02-04 attachment UI state,
   DEL-09-06/server attachment security, and DEL-02-01 hosting. DEL-06-04
   write/edit enforcement is not a substitute.
3. **Replay and projection.** DEL-05-01 storage, DEL-02-01 hosting/composition,
   DEL-08-05 child-run semantics, DEL-05-05 artifact/tool-result semantics,
   PKG-06 execution policy, DEL-05-02 vocabulary/persistence, and DEL-06-01
   permission semantics remain distinct as specified row by row.
4. **Working-root route.** DEL-07-01 containment and DEL-02-03 consumption
   remain distinct from DEL-07-03's physical route-contract ownership.
5. **Catalog generation.** DEL-06-02 owns only the deterministic generator and
   check mechanism; generated semantics stay with their ruled owners.
6. **Electron preload.** The shared boundary across DEL-02-03
   `selectDirectory`, DEL-02-05 `apiKey`, and DEL-09-06
   `safeStorage`/security is applied. No physical lead or path-level owner is
   selected. D-APP-71 separately offers those three leads or deferral.
7. **Network-policy fixture.** DEL-04-01 retains its evidence edge; the fixture
   remains development/test-only and is not packaged proof.
8. **Contract lint.** DEL-09-05 remains the release-quality consumer.
9. **PEC evidence.** DEL-10-03 retains proposal-tool verification interest and
   F-APP-3 remains binding; no apply surface or hard-fence crossing is implied.
