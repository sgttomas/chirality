# Local asset and reference invocation audit

Direct read-only audit completed against the committed local design package. All eleven assets match the README SHA256 inventory, and the HTML matches b2895107614da963b258d005d4fc1642a7dedd687bbae88c26287b04e8d0cea6. INVENTORY_v1.json carries exact inputs, asset identities, PNG dimensions and every embedded-image location. No source, asset or historical evidence bytes were changed.

The eleven assets are the square master, rounded master, four rounded downsamples, ICNS, and light/dark PNG/SVG lockups. Their roles and production method are documented in 05_LOGO_AND_BRAND.md. The parent reports visually inspecting the actual master and both lockup assets in this session; this recorder performed byte/source inspection only. The source-production scratch scripts were not retained, and the random texture quilting does not promise pixel-exact re-derivation. Preserving and checking the committed master/derived bytes is distinct from recreating the original image.

The HTML has six unique embedded PNGs, used in twenty-two img occurrences, all in its Logo panel:

| Decoded size | HTML lines | Use |
|---|---|---|
| 256×256 | 555, 563 | Mark at256/128 and large desktop-icon samples |
| 88×88 | 555 | Mark displayed at64 |
| 44×44 | 555, 566 | Mark displayed at44/32/22/16 and historical header-at22 reference |
| 860×240, light | 559 | Light corporate lockup, displayed height96 |
| 860×240, dark | 559 | Dark corporate lockup, displayed height96 |
| 128×128 | 563 | Dock icon sample |

These are embedded data, not relative file loads. Their decoded-byte hashes are separate from packaged asset hashes; no pixel-equivalence inference is made from a shared brand role. The Shell/Walkthrough are generated from the document's inline HTML/CSS/SVG rather than screenshot images. The sole external markup reference is the Google Fonts stylesheet on line2. There are no external script elements and no missing relative src/href references. No resource was fetched in this audit.

STEPS begins at line936 and contains26 states. renderWalk (994–1000) copies the selected state into frame, updates the caption/current step and stores the index locally. The numbered list uses one-based data-n attributes; prev/next and left/right arrows select states. Independent shell/walk theme buttons use data-theme-of (1043). fit (1018) scales each frame to available width with a logical1180×720 default; tab selection also invokes fit. Account references remain steps13/14/15/26; recorded design decisions supersede examples such as API/provider dots or popout where applicable.

Historical browser-01/reference2.mjs was inspected, not executed. Its recorded invocation is node <browser-01>/reference2.mjs, exit0 after a retained prior reference.mjs evaluator assertion failure. The driver verifies the mock hash, uses Chromium148.0.7778.96 with Node24.18.0, viewport1800×1100, clicks Walkthrough scenes17/18 and both themes, waits on document.fonts.ready, and captures full-page/shell/rail images. It asserts logical1180×720 and records the mock's own fit transform: actual shell830px wide, scale about0.70339. Twelve existing screenshot hashes are recorded in INVENTORY_v1.json. This audit generates no new screenshot and invokes no browser, renderer or alternate route to the blocked HTML opening.

Font evidence is limited. The historical driver installs an HTTPS-abort route, and REFERENCE_PREPARATION.md says fallback rather than pixel-identical typography. However, reference-result.json records requests[] empty and document.fonts entries with both loaded and unloaded Plex faces. Its computed font-family string names a stack, not the actual glyph face. These observations do not establish guaranteed Plex rendering or prove exclusive fallback; the discrepancy remains explicit. The current HTML has no inline @font-face definition. No new rendering inference is added.

Latest owner clarification, verbatim:

> You need to be able to see all the assets used for screenshots and how they are invoked and referred to. Do you have what you need for that? And you aren’t trying to circumvent safeties with external websites, you’re trying to see a report that just happened to be written in HTML.

This request is fulfilled here as asset/reference source inspection. The parent's earlier interactive-browser refusal remains recorded separately; this artifact claims no interactive mock access. Product/runtime authorization, account gates and publication scope remain unchanged.

Method: audit_reference_v1.py, Python standard library only, repository-derived paths, local reads plus writes only in this new audit directory. Exit0; all six deterministic claim flags true. The script and input hashes allow independent recomputation; rerun in a fresh audit-output directory by copying the script there while keeping the repository working directory, preserving this immutable output. No private environment dump or credentials captured. OpenAI GPT-6 family per system, exact serving ID unavailable; native Agent2 role/nondelegation instruction-asserted. This is derivative inspection evidence, not design acceptance or a new standing queue.
