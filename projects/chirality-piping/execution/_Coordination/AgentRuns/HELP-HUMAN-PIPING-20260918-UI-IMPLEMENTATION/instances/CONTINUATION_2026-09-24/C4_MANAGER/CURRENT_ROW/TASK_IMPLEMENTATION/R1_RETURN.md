# C4-ROW-R1 bounded repair

Read the independent review RETURN.md. Confirmed source cause: pointer-down marks the clicked cell and suppresses focus publication; a remembered same-cell click delegates to startEdit, whose readonly/busy guards return before focusCell publication. This leaves cleared ownership null despite actual activation.

Changed only the same-cell click branch after the existing editRef.current Apply/return guard: publishCurrentRow(address.rowKey) precedes startEdit. The original live-row, generation and surface publication guards remain, and startEdit still enforces readonly/busy editing rules. Other-cell focus/selection and active-editor ownership branches are unchanged.

Added readonly and busy parameterized regressions: primary A, review B activation, currentRowActive loss/clear/reentry, then pointerDown→focus→click on remembered B; require B publication, no editor/draft/selection callback, and A-selected/B-unselected row state. Added rejected Keep-draft active-editor case requiring no clicked-B publication and retention of A editor ownership.

Before/after source hashes: R1_HASHES.json. Historical review/manifests remain unchanged. No child tests/compiler/npm/build/browser/native/CUA/Git mutations executed. Manager sequential focused validation and independent backcheck remain required; these are component publications, not renderer visibility evidence.
