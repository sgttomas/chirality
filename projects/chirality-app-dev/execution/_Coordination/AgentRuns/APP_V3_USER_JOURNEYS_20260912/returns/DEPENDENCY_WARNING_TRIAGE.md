# Dependency warning triage

2026-09-13T03:15:42Z. Read-only TASK follow-up on source `9eaddb5965642a783ad700743eecdf876e9e0104` and its signed local v3.0.0 artifact. `npm audit --json` ran once in each new build workspace, both exit 1 because advisories were found. Raw JSON stayed in process memory; scoped package names below omit the at-sign. No install/fix/upgrade, package, launch, source change or exploit test occurred.

## Critical finding is shipped production code

The frontend's one critical package row is **Next 15.5.21**, containing two critical advisories, not one:

- [GHSA-p293-qw3h-jr36](https://github.com/advisories/GHSA-p293-qw3h-jr36): unauthenticated RCE requires a Windows-hosted filesystem. The checked artifact is macOS arm64; that stated platform precondition is absent. This is a specific exclusion, not a claim that Next is generally safe.
- [GHSA-2xp9-vwfh-vxw4](https://github.com/advisories/GHSA-2xp9-vwfh-vxw4): AVIF optimization through sharp/libheif may lead to RCE. Next versions below 15.5.24 are affected. **Actual ASAR contains Next 15.5.21 and sharp 0.35.3**, so this is not a build-only advisory.

The [sharp advisory GHSA-rgj7-g3m4-5g8c](https://github.com/advisories/GHSA-rgj7-g3m4-5g8c) describes memory-safety issues in libheif, possible RCE on glibc Linux under certain conditions, and affected untrusted-input processing before sharp 0.35.4. That specific demonstrated RCE environment differs from macOS, but the source does not establish macOS immunity to malformed-input memory corruption.

Reachability established from source: `electron/main.ts` constructs a production Next server, passes requests to its normal handler and binds only `127.0.0.1`. `next.config.mjs` does not disable the image optimizer. Installed Next defaults have `unoptimized: false`, empty remote patterns, and unrestricted local patterns; its optimizer route and AVIF decoder path are present. No product `next/image` use was found. Therefore arbitrary remote-image optimization is constrained, but absence of an Image component does not disable the HTTP optimizer endpoint. No active request/exploit or malicious AVIF was attempted. Whether an attacker can supply AVIF bytes to an allowed local URL through this App's routes, and whether native mitigations prevent exploitation on this exact macOS bundle, remain unproven. Loopback-only binding reduces exposure; it does not itself establish safety from local or browser-mediated requests.

## High package rows

| Package row | Actual artifact and relevance |
|---|---|
| sharp 0.35.3 | Shipped production dependency; linked AVIF/libheif risk above. Patched package version is 0.35.4. |
| nanoid 3.3.16 | Shipped production dependency through PostCSS. [GHSA-2v37-7h3g-55p8](https://github.com/advisories/GHSA-2v37-7h3g-55p8) concerns custom generators with size zero; affected below 3.3.18. No product nanoid/custom generator call found. PostCSS uses `nanoid/non-secure` with fixed size 6. Vulnerable custom path reachability is not established; package presence is established. |
| earendil-works/pi-coding-agent; xmldom/xmldom; ajv; brace-expansion; fast-uri; ip-address; js-yaml; minimatch; undici | Frontend lock marks affected entries development dependencies. ASAR has zero package manifest instances for the eight underlying high packages (xmldom, ajv, brace-expansion, fast-uri, ip-address, js-yaml, minimatch, undici); earlier packaged boundary proof excludes Pi/legacy engines. No corresponding package paths occur in Electron/Runtime service/CLI source maps. These reported dependency rows belong to build/test tooling or excluded legacy support, rather than the shipped production npm closure. This does not mean they are safe for tooling that processes untrusted input. |

The Runtime's three high rows are brace-expansion and undici under excluded Pi support, plus development-only nanoid. The first two are not `dev:true` in the Runtime workspace lock because that workspace retains a legacy engine package; they are nevertheless excluded from the Codex-only desktop artifact. Frontend production nanoid is a separate shipped instance as described above. Severity row counts include propagated dependency effects and are not counts of distinct exploitable vulnerabilities.

## Recommendation and limits

Recommend a narrow dependency remediation before public distribution: bring Next to a patched 15.5.x (audit offers 15.5.25), update the explicit sharp override to at least 0.35.4, and resolve shipped nanoid to at least 3.3.18, with normal independent review and affected checks. This is a recommendation to the parent/owner, not authorization for another build or a new governance gate. Keep the signed artifact as an unnotarized local review artifact; do not describe its audit result as clean or dismiss it because dependencies predate this tranche. Address excluded development/legacy highs in a separate dependency-maintenance scope. No remediation or rebuild occurred here.

Evidence basis: both fresh audit responses; source package/lock/config/main; actual ASAR package inventory and extracted package versions; compiled Electron/Runtime source-map inventory; installed Next optimizer defaults and code; installed PostCSS caller; linked GitHub reviewed advisories. Static absence checks cannot prove universal exploit unreachability, and npm audit does not cover all bundled native or supplier vulnerabilities.

## Focused removal alternative requested by parent

Read directly from the actual signed App ASAR `node_modules/next/dist/server/next-server.js`: `handleNextImageRequest` recognizes `/_next/image`, then checks `imagesConfig.loader !== 'default' || imagesConfig.unoptimized`. When true it calls `render404(req, res)` and returns before parameter validation, image fetching or decoding. Therefore `images: { unoptimized: true }` disables optimization at the endpoint itself. It still loads the optimizer module/cache definitions before that guard, but does not invoke image processing. This is stronger than merely changing URL generation by the Image component.

Search of current product `src/**` outside tests, `electron/**`, and Next configuration found no use of `next/image`, `/_next/image`, `imageOptimizer`, or sharp. No configured custom loader or server image-optimization integration exists in those surfaces. This static evidence supports disabling an unused feature without expected product functionality loss; it is not a runtime proof or exhaustive dynamic-input analysis.

A narrower recommendation than the dependency upgrade is consequently to set `images.unoptimized: true`, then independently review and verify that the built endpoint returns 404 without decoding. This removes the observed Next AVIF attack path while retaining packages with outstanding audit advisories; describe it as removal of that reachable path, not a clean audit or repair of sharp itself. A later dependency update remains sensible maintenance, and shipped nanoid's custom-size-zero advisory remains separately tracked. The Windows-specific advisory is still excluded by this artifact's platform. No source change, test request or rebuild has been performed or authorized by this read-only recommendation.

Exact advisory URLs: Next Windows https://github.com/advisories/GHSA-p293-qw3h-jr36 ; Next AVIF https://github.com/advisories/GHSA-2xp9-vwfh-vxw4 ; sharp/libheif https://github.com/advisories/GHSA-rgj7-g3m4-5g8c ; nanoid https://github.com/advisories/GHSA-2v37-7h3g-55p8 . `npm view <package> <version>` equivalent exact-version lookups confirmed published Next 15.5.25, sharp 0.35.4, nanoid 3.3.18 (all exit 0, no acquisition). Next advisories name 15.5.24 as first patched 15.5 release; 15.5.25 is the published same-line version offered by audit.
