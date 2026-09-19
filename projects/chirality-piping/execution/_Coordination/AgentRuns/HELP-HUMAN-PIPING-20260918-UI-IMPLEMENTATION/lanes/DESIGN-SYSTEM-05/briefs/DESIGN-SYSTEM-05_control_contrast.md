# Sealed brief — DESIGN-SYSTEM-05: control-boundary contrast and the disabled ink (design system V1.4)

Sealed by ROOT (HELP_HUMAN, Agent 0) on 2026-09-19T00:06Z before launch. Role: HELPS_HUMANS design manager, working alone; you do not delegate. Model requested: Claude Fable 5.1. Mechanism: Claude Code `Agent` tool, general-purpose type, background.

Path placeholders: resolve `{REPO_ROOT}` with `git rev-parse --show-toplevel` in the worktree you are started in; `{WORKING_ROOT}` is `{REPO_ROOT}/projects/chirality-piping`; `{DESIGN}` is `{WORKING_ROOT}/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260916-UI-DESIGN-PROGRAM`; `{RUN}` is `{WORKING_ROOT}/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`. Write no absolute machine path in anything you produce.

## Why this pass exists

The first implementation slice put the tokens into the product (`{RUN}/instances/B1-TOKENS/RETURN.md`; read "Where the design could not be followed" and the semantic-changes table). It found two things the design system must settle before the shell is built from it:

1. **Control boundaries.** `border.strong`, which §2.9 says "frames inputs and the table", measures 1.75:1 to 2.36:1 on the surfaces §2.9 lists. The owner adopted WCAG 2.2 AA for touched controls (`{WORKING_ROOT}/execution/_Coordination/_DECISIONS/D-68_RULING_2026-09-15.md`). Success criterion 1.4.11 asks 3:1 for the visual information needed to identify a user-interface component. The product already tests it: `expectResolvedStyleAndTargets` in `{WORKING_ROOT}/apps/desktop/e2e/ui-foundation-workflows.ts` asserts 3:1 or better on a control's border. The slice kept the product's present border values rather than move that check. The system needs a boundary token that meets the criterion.
2. **The disabled ink.** `text.disabled` measures 2.0:1 to 2.8:1 on the surfaces §2.9 lists, and 1.94:1 (light) and 2.28:1 (dark) on `disabled.fill`, a pairing §2.9 does not list. The product today draws disabled labels at 3.74:1. WCAG exempts inactive components, so this is a design decision and not a conformance one. It matters now because the implementation's rule for a control whose gap is outside a tranche is "absent, or disabled with its reason": disabled controls will be common, and their labels have to be findable. §2.9 already calls `text.disabled` "the one token to lift", and §8 item 6 leaves the contrast target open. The slice kept the product's present disabled ink meanwhile.

## The work

Amend `{DESIGN}/instances/DESIGN-SYSTEM/` from V1.3 to V1.4 with the smallest change that settles both. `tokens.json` goes to 1.3.

1. **A control-boundary token** (working name `border.control`; choose the name by the file's conventions) with light and dark values at 3:1 or better against every surface a control sits on (`surface.panel`, `surface.base`, `surface.sunken`, `surface.header`, `surface.raised`, and the control's own fill where it differs). `border.strong` stays for framing that identifies no component (the table frame, the expansion edge). Go through §5 component by component and move every boundary that identifies a control to the new token; list each move.
2. **A sweep of the same criterion across the system.** For every component in §5: what identifies it and what shows its state (checkbox and radio outlines, switch tracks, the pressed state, the selection bar, icon-only buttons' glyphs, a chip that is a control, the drag handle, the splitter), the token that draws it, the measured ratio in both themes, pass or fail against 3:1. Fix failures with the fewest token changes; where a failure is deliberate (a recessive hairline that identifies nothing), say why it is outside the criterion.
3. **`text.disabled`.** Measure it on every surface and fill it is drawn on, `disabled.fill` included, and add those pairs to §2.9. Recommend one of: keep; lift to a stated ratio. A lifted value must stay visibly apart from `text.muted` and must not read as enabled; say how the disabled state is carried besides ink (fill, no hover, cursor, the reason tooltip). Give your recommendation with its measurements; ROOT decides and records the decision as ROOT's, open to the owner.
4. **Records.** §2.2 tables, §2.9 table and findings, §8 (close or restate item 6 accordingly), §9 change-log rows continuing the numbering, the specimen, and the generated tables, all through the tools in `tools/` (`contrast.mjs` and its pair list, `gen.mjs`, `splice.mjs`, `agree.mjs`, `render.mjs`), used as V1.3's `RETURN.md` describes; nothing generated is edited by hand. Add an addendum to `RETURN.md`. Nothing the owner ruled changes: names, labels, copy rules, the six functions, the tooltip form.
5. **Not in this pass:** the specification, the frames, the product. The product holds its own copy of `tokens.json` 1.2 with a recorded hash and adopts 1.3 later in a slice of its own; do not touch `apps/desktop/**`. List the frames that draw a control boundary with `border.strong`, so a later frames pass can follow.

## Write scope and git

`{DESIGN}/instances/DESIGN-SYSTEM/**` and your own folder `{RUN}/instances/DESIGN-SYSTEM-05/**` (screenshots under `shots/`, scratch output, nothing else). Nothing else in the repository. Run no state-changing git command; ROOT commits. ROOT's launch message names your worktree; work only there. The specimen is rendered from its file with every network request blocked, so no server and no port is used; if you start any server for any reason, run it through `sh {RUN}/tools/with_e2e_lock.sh <command>` and stop it.

## Checks

`node tools/contrast.mjs` and `node tools/agree.mjs` (or however V1.3's tools are run; say exactly what you ran) clean; every colour value of 1.2 unchanged except those this pass changes, shown by a diff of `tokens.json`; the specimen renders in light and dark (Chromium), screenshots under your instance folder.

## Return

Your final message is your return; ROOT retains it. Include the model you are, every file changed, the token diff, the component sweep table, the disabled-ink recommendation with measurements, what you ran, and what you did not do. End with: Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
