# Affected-surface and compatibility map

Status: `CANDIDATE IMPACT MAP — READ-ONLY ANALYSIS — NO CHANGE AUTHORIZED`

| Surface | Current evidence | Candidate delta if later accepted | Compatibility / gate |
|---|---|---|---|
| Root governance and agent doctrine | E-007, E-022, E-023, E-024; current role hierarchy and child scoping | no current Root managed-Bash restriction exists to amend; E-003/E-004 are stale only on that Root-doctrine assertion; product-runtime sandbox semantics may still require explicit governed contracts | do not revive deleted instruction; any new developer-agent doctrine needs a separate owner ruling |
| `agents/AGENT_WORKING_ITEMS.md` write-overlap posture | E-022; disjoint concurrent writes, serialize or integration-own actual overlap | candidate does not change the general overlap rule or impose a full-root/exclusive Bash rule | preserve current instruction unless a separately ruled scope changes it |
| runtime session contracts | E-012, E-015 | add profile/backend/policy/registry/implementation binding and immutable rollover | versioned schema and migration plan `TBD-105-03/04` |
| runtime tool contracts | E-011, E-016 | replace/coexist with coarse permissions using exact grants, receipts, capabilities, and family binding | affected-client/tool registry census; no silent aliases |
| runtime auth registry | E-017 | client scopes are insufficient for authenticated, replay-safe, applicable/precedence-resolved run/tool/resource grants, exact capability matching, and bound deterministic policy decisions | grant/capability/policy model and migration `TBD-105-20`; receipt-only schema/authentication/replay `TBD-105-06` |
| runtime events and errors | E-013, E-014, E-018 | add authorization, budget, cleanup, evidence and generic state vocabulary | event/error version mapping `TBD-105-09/10/16` |
| engine adapters | E-020, E-021 | adapter identity/capabilities do not select a sandbox or authorize native tools | per-adapter conformance and no-fallback proof |
| Pi/oMLX pilot | E-021 | current Agent-2 exactly-one-read-only-tool pilot is narrower than candidate future profile | preserve pilot until separate accepted activation; no implied Bash/native grants |
| App-owned harness tool descriptors | E-016 | current per-tool permissions, path scope, bytes, provenance and interrupt flags may become inputs to an exact profile/grant | App-owned affected-client migration and validator changes; current values are not Root doctrine or generic defaults |
| App affected client | E-003 through E-005 | future affected-client work could bind P1/X1/H1 only after accepted Root bytes | App SCOPE_CHANGE and conformance; no Root candidate reliance |
| Piping affected consumer | E-006 | reusable generic carrier may bind local operations without interpreting them | Piping-owned adoption/routing; preserve fixture-preview and domain boundaries |
| TM-ROOT-121 / DEL-02-06 | owner ruling E-001 separately authorizes TM121 candidate carrier | identity/compatibility/resume may depend on sandbox identity | coordinate identifiers; do not merge carriers or claim resume semantics here |
| validators/tests | E-004 §5 suggests escape/adversarial classes | implementation would require contract, schema, platform, escape, budget, interruption, cleanup and fallback tests | exact suite `TBD-105-07/18`; implementation gate required |

No live caller, alias, registry, schema, validator, or runtime byte is changed by
this map. Historical runs remain governed by their recorded surfaces. A future
migration must name coexistence, refusal, conversion, and removal conditions
before any current contract is retired.
