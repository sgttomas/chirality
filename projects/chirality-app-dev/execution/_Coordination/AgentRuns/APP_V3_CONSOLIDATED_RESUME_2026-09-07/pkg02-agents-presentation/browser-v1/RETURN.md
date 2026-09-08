# Agents projection narrow browser visual qualification

Verdict: **PASS**

The exact reviewed `AgentsProjection` was mounted byte-for-byte with the exact production hierarchy builder, contracts, and full production CSS in a 390 CSS-pixel fixture. Synthetic records cover Agent 0 `HELP_HUMAN`, Agent 1 `WORKING_ITEMS`, Agent 2 `REVIEW` and `TASK`, nested parent relationships, a record with unknown type and no persona, and detached Agent 2 `RESEARCHER`.

Actual Chrome 152.0.7977.83 and Safari 26.6.2 evidence supports the narrow presentation in light and dark themes. Both browsers expose the refresh control and its disabled `Refreshing…` transition, render the completed refresh count, expose Agent 2 REVIEW as selected after activation, and expose the paused notice plus disabled agent controls when selection is disabled. Accessibility names communicate `Top-level`, `Agents reporting to ...`, `Parent: ...`, and `Parent relationship unavailable`. Visual inspection of all retained images found no clipping or overflow that obscures required content at the compact width.

No rendered accessibility record contains raw session/parent IDs, source/provenance, timestamps, runtime state, engine/provider/model, currency, artifact/approval references, or technical diagnostics. The unknown type/persona record renders only its truthful relationship and no inferred label. Product source remained at the accepted hashes.

CUA returned JPEG bytes despite the initial `.png` capture names; evidence uses corrected `.jpg` extensions. Safari captures included native browser chrome and unrelated tabs, so retained Safari images are cropped by exactly 70 top pixels to the complete page viewport and persisted Safari AX records contain only the page subtree. No user data is retained. This evidence does not claim broader full-shell behavior.

The owned Chrome and Safari tabs were closed. The owned server PID 78002 exited cleanly after Ctrl-C, and port 64503 has no listener. Scratch is preserved at `/private/tmp/chirality-app-agents-presentation-20260907` for owner inspection.

Attribution: gpt-5.6-sol, medium reasoning, nondelegating Agent 2; role and nondelegation are instruction-asserted.
