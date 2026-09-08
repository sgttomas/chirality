# Manager return — Agents projection presentation simplification

Verdict: **PASS / PUBLICATION_READY_SELECTION**.

The owner-directed two-locus change replaces the Agents-card metadata dump with the minimum recorded relationship view. Cards show a known agent type (`Agent 0`, `Agent 1`, or `Agent 2`), the recorded persona when present, and plain parent/tree relationship copy. Unknown type/persona values are omitted without inference. Raw session or parent identifiers, engine/model/provider attribution, currency, provenance, timestamps, runtime status, artifact/approval references, and technical diagnostics are absent from the rendered projection.

Hierarchy placement, refresh/error/loading access, selected state, disabled-selection behavior, and internal session identity remain intact. No CSS, Runtime, contracts, hierarchy builder, permissions, or unrelated product source changed.

Frozen source:
- exact patch: `23462b0f2020c5dbaf9ab19d95d8a276bbe2c59d51df6688c499d33d35f252a8`
- component postimage: `99f516d8e16a79d5082c2892e41b4d86582d492692ce05d32415bab99547adb4`
- focused-test postimage: `1da832039a57f3ba036728380df8adfb787161511c77c4f89e9a9f0033407338`
- author manifest: `44a0908e83464783531257bb6866de7ce49cbfd50f9f0866f90f8b546c06f4b1`

Validation:
- focused Vitest: 1 file, 6 tests PASS
- registered frontend typecheck PASS
- exact two-path scope, whitespace, patch equality, and reverse application PASS
- fresh independent full-diff review: PASS with zero findings; manifest `c76e430d3ee34edfa9071f4991e43e50e617ac5a2abfb1314f9c14a1d9264820`
- narrow actual Chrome and Safari visual/accessibility qualification: PASS; manifest `5636d4adeb51778519e134b2c52cfd1e54a469ef23b5eca41e42a953a7f59ded`

Manager recomputed the author 4/4, review 3/3, and browser 43/43 manifests; independently reran the focused six tests; verified both live postimages; and visually inspected all twelve browser captures. At 390 CSS pixels, light and dark trees remain readable in Chrome and Safari. Refresh, selected, and disabled states render correctly. No required content is clipped or obscured, and accessibility records carry meaningful tree relationships without removed metadata or raw IDs.

The visual packet uses a narrow synthetic fixture with the byte-exact production component, hierarchy builder, and full production CSS. It does not claim full-shell or native Electron behavior. CUA returned JPEG capture bytes; extensions were corrected. Safari captures were cropped by exactly 70 pixels to remove native browser chrome and unrelated tab titles while retaining the complete page viewport. The owned tabs and server were closed, PID absent, and port 64503 listener-free.

APP-HOLD-1 dispatch preflight for DEL-02-02 returned ALLOW/CLEAR at HEAD `4f98be53e7359b72521f20181537f67fd63ad69b`, scan fingerprint `ff6ce063eaf9c7611ce5be39133c032e7f06abf1612da03e45e61168c4b4b399`, register `c08a2948201cfcc09a661750f45148f9555d1ce38b925eeacf987de89ac5cafc`.

No Git, receipt, Runtime, account/provider, user data, user daemon/oMLX, protected fixture, or D121 isolation was changed.
