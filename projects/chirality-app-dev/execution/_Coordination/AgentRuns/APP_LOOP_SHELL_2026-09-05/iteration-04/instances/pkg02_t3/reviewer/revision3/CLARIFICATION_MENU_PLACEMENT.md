# Reveal placement clarification — source revision3

Read-only clarification requested by WORKING_ITEMS after frozen review; original REVIEW_RETURN.md and run record remain immutable. No source/test/native effects.

## Assessment

The implementation provides the required file Reveal capability through the Document Menu, bound to the same current projectRoot/target (right-panel.tsx120–122), including when the content area displays an Office/unsupported/oversize handoff. This remains accessible through the native details/summary control; opening that menu does not navigate away or change target. No unavailable action, wrong target, privilege expansion or functional regression was found. The existing source-correctness PASS remains applicable.

It does **not** reproduce the target's exact card composition: target§5.4 line153 explicitly lists both Open in default app and Reveal in Finder in the handoff card, whereas document-view.tsx435–437 contains QuickLook where relevant and Open-default only. Target§5.5 independently lists Reveal in the menu, so the card omission cannot be described as literal compliance with both placements. The completeness matrix should say “Reveal available in the Document Menu; no duplicate card button.”

Classification: non-blocking presentation-placement deviation with functional capability preserved, not a missing Reveal implementation. Choosing one accessible, current-target menu placement instead of duplicating the same action on the card is an ordinary presentation choice at the source-correctness level. It does not justify an unqualified assertion of exact target/card completion. The parent must record that calibration in its accepted design/evidence narrative or retain the exact-card placement as a minor outstanding target difference; this reviewer does not amend the target, waive an acceptance criterion or declare the whole item complete.

Native verification should operate the actual “Menu” → “Reveal file in Finder” control and label evidence accordingly. An evaluator must not claim that this proves a card-local Reveal button exists. No source change should be made solely to satisfy an invented evaluator locator. If exact two-location conformance is selected by the owning manager, adding the duplicate button is bounded presentation work and requires a new freeze/backcheck, not an owner policy or runtime change.

First-H1 title behavior intentionally also sets the document header h2 label from that H1; two visible copies of the title are consistent with the current source. Locate the document heading by actual level/container when evaluating TOC/title effects, and preserve that attribution.

## D64 attribution

OwnerStandingApproval: D-APP-64 §3, within parent clarification request.
AgentJudgment: CALIBRATE_PRESENTATION_COVERAGE
SelectedOutcome: preserve sourcePASS; explicitly distinguish available menu capability from exact card placement.
JudgedBy: TASK Agent2 /root/pkg02/t3_review.
OwnerCaseSelection: NONE
RejectedAlternatives: invent card control; silently equate both locations; label complete lack of Reveal despite actual usable menu; alter source for evaluator convenience.
RationaleArtifact: reviewer/revision3/CLARIFICATION_MENU_PLACEMENT.md.
IndependentVerifier: actual read-only reviewer clarification; parent governed refutation and actual native verification remain pending.
EffectStatus: clarification record only; no source or accepted target effect.
PreservedGates: D64§5.1 classes1–10, exact write/source bounds, native/browser/global proof, partialPDF/full-item gates, no lifecycle/pointer/owner criterion/Root/provider/release/acceptance/merge act or waiver.

Ontology: action availability and exact placement are separate properties. Epistemology: actual target§§5.4/5.5 and source locations establish both. Praxeology: evaluator exercises current menu and parent records the presentation calibration. Axiology: accessible actions and truthful completeness evidence without counterfeit controls or unnecessary policy escalation.

Provenance: delegated-harness-native TASK Agent2, role instruction-asserted, no delegation; exact runtime model/provider/engine identifiers unavailable/UNKNOWN. This is derivative clarification, not authority truth. Full-item PDF and unexecuted verification residuals remain unchanged.
