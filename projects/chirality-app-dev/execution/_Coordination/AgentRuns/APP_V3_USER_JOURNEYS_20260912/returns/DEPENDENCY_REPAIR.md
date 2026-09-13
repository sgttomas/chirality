# Dependency repair — frozen author return

TASK Type 2, gpt-6-astra medium per dispatch; no delegation. Source basis:
9eaddb5965642a783ad700743eecdf876e9e0104 on
codex/user-journey-build-evidence-20260913. Scoped repair complete; independent
review, CI and final production HTTP check remain parent-owned.

## Final changes and installed verification

- Next pinned exactly to 15.5.25; existing sharp override changed to 0.35.4.
- Shipped nanoid resolves to 3.3.18 under PostCSS's unchanged `^3.3.16` range.
  No new direct nanoid dependency or override; no major forced on other consumers.
- `images.unoptimized: true` disables the unused Next optimizer endpoint.
- No new maintained regression test. Parent rejected the initially authored VM
  test because it extracted an upstream private handler using exact source
  delimiters, making coverage depend on incidental compiled text. That still-
  untracked test was removed from the candidate. Parent owns the real production
  HTTP probe after build and before signing: normal page/static-asset positive
  controls, empty optimizer request and existing-source optimizer request,
  expecting optimizer 404 before validation/decoding.

Installed and lock versions both equal Next 15.5.25, sharp 0.35.4, nanoid 3.3.18.
`npm ls next sharp nanoid --omit=dev --json` exits 0 and resolves nanoid through
Next → PostCSS. Loading sharp succeeds and reports sharp 0.35.4, libvips 8.18.6,
libheif 1.23.2. No malformed image or exploit input was processed.

Lock review: 40 changed package records including the root record, zero added or
removed records. Changes are only Next/env/SWC, sharp/native/libvips platform
packages, nanoid, and sharp's required emnapi runtime 1.11.2 → 1.11.3 (new range
requires at least 1.11.3). npm's unrelated Runtime manifest metadata refresh and
three removed Pi integrity fields were restored exactly from the source basis.
No Runtime file or unrelated dependency version changed.

## Commands and results

All npm commands ran from projects/chirality-app-dev/frontend. npm output lines
containing the at-sign were filtered; audit JSON was parsed in memory and only
safe summaries emitted. The JSON-escaped exact-version selector below decodes to
the actual install argument.

1. Edited package/config pins; `npm install --ignore-scripts --no-audit --no-fund`
   — exit 0; changed 11 installed packages.
2. `npm update nanoid --ignore-scripts --no-audit --no-fund` — exit 0, but registry
   selected 3.3.19. Corrected to the explicitly requested 3.3.18 using argv
   `['npm','install','nanoid\u00403.3.18','--save-exact','--ignore-scripts','--no-audit','--no-fund']`
   (exit 0), then removed its temporary direct package/root-lock declaration.
   The transitive exact lock entry remains compatible with unchanged PostCSS range.
3. Parsed lock comparison against source basis — zero unrelated changed records;
   installed/lock/version-tree checks above — pass.
4. `npm test -- src/__tests__/lib/next-image-optimizer-disabled.test.ts src/__tests__/electron/renderer-server-port.test.ts`
   — **2 files, 7 tests passed at the earlier candidate**, retained only as a
   historical observation. The VM handler test was subsequently removed by
   parent direction; this result is not maintained optimizer coverage. The
   existing renderer-server-port test file remains unchanged.
5. `npm run typecheck` — **pass**, renderer and Electron. First attempt identified
   an optional-config access in the new test; corrected that access and reran
   focused tests/typecheck successfully. Those typechecks remain applicable to
   the final three-source-file candidate after removing only the added test;
   no dependency/config change or repeated check followed its removal.
6. `npm audit --omit=dev --json` — exit 1, **2 moderate, 0 high, 0 critical**.
7. `npm audit --json` — exit 1, **19 package rows: 9 high, 9 moderate, 1 low,
   0 critical**. Audit exit 1 accurately indicates outstanding advisories.

## Remaining warnings and boundary

Production audit's two moderate rows are PostCSS 8.5.22 and its propagated Next
row: [GHSA-fxqj-rqcc-2cmp](https://github.com/advisories/GHSA-fxqj-rqcc-2cmp), concerning
attacker-controlled sourceMappingURL processing when `from` is unset. npm offers
a Next major-version change; that is outside this narrow approved patch. No
runtime reachability claim for this advisory is made here. The targeted Next
critical and sharp/nanoid high advisories are absent from the updated audit.

All remaining high rows in the full frontend audit have only development-marked
lock nodes: Pi coding agent, xmldom, ajv, brace-expansion, fast-uri, ip-address,
js-yaml, minimatch and undici. Other non-production moderate/low rows belong to
development tooling. These remain warnings for their tooling/legacy contexts;
production omission is not a claim that those packages are safe. Earlier artifact
exclusion evidence is recorded in DEPENDENCY_WARNING_TRIAGE.md; this author did
not rebuild or inspect a new artifact. Runtime dependencies/audit were untouched.

The existing signed artifact still contains its old dependency bytes. This return
claims repaired checkout/installed dependency state, not a repaired shipped
artifact, universal vulnerability absence or public release readiness.

## Frozen file hashes

Final source scope is exactly three files below. Paths are relative to
projects/chirality-app-dev/frontend. The removed VM test is not part of the
candidate; this return is coordination evidence.

| File | SHA-256 |
|---|---|
| `package.json` | `f759f09de43fc1d34223858c222082645efeb2a8ee3cb48bc3ab1c3947c69ecc` |
| `package-lock.json` | `a20175b1ed798443c7293d2ce63a57c323a9e5e42aa104600b8d63ae99b1efbb` |
| `next.config.mjs` | `64a9b5efc2e772c9cf6822d8cfc224c1e2db92516faec7fb3619e65cdcdf04f9` |

Preflight: DEL-09-06 reliance at
APP_V3_USER_JOURNEYS_20260912:DEPENDENCY_REPAIR — ALLOW/CLEAR/NOT_HELD;
register d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c,
scan 928812620766e95e172395751d2e3fb23733e232b691e6782ab631583f28a4c8.
No full App/Runtime suite, Runtime changes, authentication/profile/credential
access, App launch, signing, packaging or Git mutation. Parent owns final review,
CI/full coverage, artifact rebuild and the independently reviewed production
HTTP page/static-positive and optimizer-404 checks before signing. This is a
derivative repair/evidence return; no governed acceptance or release act.
