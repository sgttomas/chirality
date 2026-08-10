# Unresolved consequential choices

Status: `NON_AUTHORITATIVE_INCOMPLETE_CANDIDATE`

Selection authority remains `HUMAN` under orchestration plan v3. The specific
accountable product, security, platform, privacy/legal, runtime, App, PEC, or
other owner is `UNKNOWN` unless the cited accepted evidence assigns a bounded
ownership partition. This package chooses no alternative.

| Choice | Alternatives preserved | Missing evidence | Lawful decision owner / gate |
|---|---|---|---|
| Identity schema family/version/encoding | JSON family; typed binary family; another explicitly proposed family; no selection | Exact field meanings, requiredness, nullability, namespaces, validators, cross-language corpus, current migration | Accountable human semantic gate after Root design evidence (`TBD-105-03`) |
| Run/session identity lifetime | Run-scoped; session-scoped; split identities; another evidenced design | Workload/isolation/cost study and client impact | Accountable product/runtime owner then human gate (`TBD-105-01`) |
| Rollover boundary | New run; new session; new daemon generation; combination; explicit rejection | Field-by-field trigger matrix, invalidity/migration corpus, DEL adjacency | Accountable human semantic gate (`TBD-105-04`) |
| Backend/profile identity and topology | OS sandbox; brokered tools; hybrid; unsupported | Qualified platform cells, package/API/version, adversarial corpus, credential/process/network topology | Platform/security/product owners `UNKNOWN`; all AB-02 candidates `NOT_QUALIFIED` (`TBD-105-02/05/18/19`) |
| Rights grammar | Current `ToolPermission`; current descriptor vocabulary; richer typed grammar; other | Executable/process/env/path/inode/network/IPC/device/credential/channel semantics plus mapper/backend proof | Accountable runtime/security owner `UNKNOWN`, then human gate (`TBD-105-17`) |
| Grant/capability/policy model | Single grant; composed grants; policy-only; another model; no selection | Issuer/evaluator/policy authority, authentication, replay, applicability, precedence, conflict, expiry, revocation, exact decision corpus | Accountable security/product owners `UNKNOWN`, then human gate (`TBD-105-20`) |
| Receipt authenticity/store | Unkeyed evidence; keyed/authenticated evidence; external anchor; other | Threat/trust model, keys/trust anchors, ordering/tamper tests, retention and privacy rules | Security/privacy/legal/product owners `UNKNOWN` (`TBD-105-06/09`) |
| Interruption state vocabulary | Current turn/harness tokens; proposed requested/ack/cleanup/terminal lifecycle; family-specific models | AB-04 timing and AB-08 per-family evidence; current-union reconciliation | Accountable runtime/product owner then human gate (`TBD-105-10/11`) |
| Generic terminal model | Expanded terminal enum; base terminal plus orthogonal facts; hybrid | Full event/error/tool crosswalk, mixed-fact and unknown-code corpus, consumer review | Accountable human semantic gate (`TBD-105-16`) |
| Partial/truncation representation | Terminal states; orthogonal flags; quarantined evidence; no accepted use | Workload/atomicity/loss/privacy evidence and consumer policy | Product/privacy/client owners `UNKNOWN` (`TBD-105-12/14/16`) |
| Continuation existence and semantics | No continuation; opaque token; explicit cursor record; other | Owner posture, binding/expiry/replay/stale corpus, DEL consistency, clients | Accountable human semantic gate plus affected clients (`TBD-105-15`) |
| Budget dimensions and overflow | Current descriptor bytes; candidate multi-dimension budget; deny/truncate/artifact/continuation/fail combinations | Representative workloads, maxima, costs, product loss posture | Product/client owners `UNKNOWN` (`TBD-105-13/14`) |
| Serialization/canonicalization | Opaque original bytes; UTF-8 JSON with later profile; typed binary with later profile | Exact byte rules, validators, language/library corpus, migration | Accountable compatibility/crypto owner `UNKNOWN`, then human gate (`TBD-105-21`) |
| Digest/crypto profile | Current SHA-256 practices; algorithm agility; other cryptographic/non-cryptographic profiles | Algorithm/purpose distinction, payload scopes, domain separation, threat model, agility/migration policy | Accountable security/compatibility owner `UNKNOWN`, then human gate (`TBD-105-21`) |
| Unknown schema versions | Reject; quarantine; preserve-and-defer; negotiated reader; other | Compatibility posture, old/new clients, support window, security analysis | Accountable human plus affected-client gates (`TBD-105-03/04/21`) |
| DEL compatibility epoch/binding | Future positive decimal epoch and complete manifest only; no value selected here | Owner-supplied epoch, complete accepted manifest, exact sources/clients/evidence | Accountable human and DEL-owned Root gates; no TM105 widening |
| Root generic client/CLI migration | Hard cutover; staged window; another accepted plan | Exact versions, declaration locus, mismatch/status mapping, no-resend evidence | Root client/CLI owner plus human lifecycle/release gates |
| App migration/resume/profile | D-APP-84 proposal alternatives; no selection | App ruling, Pi version conflict resolution, SCOPE_CHANGE, implementation/conformance | App-owned gate after Root semantics |
| PEC v2 effect | Affected; not affected; exact bounded operation; another ruling | PEC-owned authoritative evidence | PEC owner; currently `UNRESOLVED` with no dependency/veto |
| Piping effect | Current DEL `NOT_AFFECTED`; later reopen only on Piping-owned exact obligation | Any later accepted Piping instrument | Piping-owned gate; no current Root obligation |
| Retention/redaction/privacy/legal | Multiple possible policy regimes; no selection | Protected data, stores, roles, durations, deletion/legal hold, incident/e-discovery, jurisdiction | Attributable product/privacy/legal/security owners `UNKNOWN` |
| Implementation family and fallback | One family per tool; exact families all unselected | Registry, package/version, backend/profile, full no-fallback suite, independent review | Root/App/other owning implementation and affected-client gates (`TBD-105-07/08`) |

Every choice remains consequential. Schema compilation, vector validation,
hashing, or package completion is not a choice resolution and supplies no
semantic, implementation, client, lifecycle, release, reliance, publication,
Git, or byte-gate effect.
