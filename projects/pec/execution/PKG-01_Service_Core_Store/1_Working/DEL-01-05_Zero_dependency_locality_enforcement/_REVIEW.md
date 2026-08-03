# Review — DEL-01-05 produced artifacts

**Review stage:** RF-002 INDEPENDENT RERUN COMPLETE / RF-001 FINAL RESEAL CLOSURE  
**Review type:** `INDEPENDENT_VERIFICATION`  
**Reviewer:** `REVIEW-INDEPENDENT-RERUN-20260803`  
**Lifecycle:** `INITIALIZED` (review-from-`INITIALIZED` expressly authorized)  
**Candidate binding:** `D-PEC-77_ACTIVATION.md` SHA-256 `111203c7fb3da9d8efc8d95765e0ecce8cddeafbd59a61f71599ab6d9b26448e`  
**SOW binding:** SHA-256 `53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53`

This independent review evaluates candidate fitness only. It accepts no
artifact or acceptance criterion, changes no lifecycle state, and grants no
release or professional-reliance authority.

## Gate 1 — preconditions

| Precondition | Result | Evidence |
|---|---|---|
| Deliverable and format | PASS | DEL-01-05; valid `SOW_V1`; anticipated CI/lint check plus posture note |
| Lifecycle entry | PASS BY OWNER OVERRIDE | Owner selected independent REVIEW and authorized review from `INITIALIZED` on 2026-08-03 |
| Review independence | PASS | `REVIEW-INDEPENDENT-RERUN-20260803` did not produce the candidate or RF-002 repair |
| Candidate inventory binding | PASS | Activation hash exact; 18/18 inventory paths exist and reproduce their recorded hashes |
| Deterministic checklist | PASS | `chirality-review-checklist/v1`; 11 ordered rows; checklist SHA-256 `6eccfb72ac1d512a6bef287f4a9a828964ba30d46fbb7d3cb69cbbd12f18db2c` |
| Context/decomposition | PASS | DEL-01-05 / PKG-01 / SOW-052;SOW-053 / OBJ-005; three active satisfied ANCHOR dependencies |

## Gate 2 — checklist

Every AC row below is copied in compiler order and byte-for-byte from the
validated checklist source.

| ID | Exact criterion | Verification | Independent result |
|---|---|---|---|
| AC-001 | On a service-core state whose runtime dependency surface is entirely workspace-internal the dependency assertion passes, and on any state that introduces a third-party runtime dependency it fails and names both the offending dependency and the importing module. | VER-001 | PASS on recorded direct/transitive fixtures and inspection |
| AC-002 | The check's admitted set is enumerated in its own configuration, contains only workspace-internal runtime contracts packages, and admits no entry that `PEC-SVC-001` does not permit; adding an entry is a visible configuration change, not an inferred default. | VER-002 | PASS |
| AC-003 | On a service-core state that initiates or configures external network egress the locality assertion fails and names the call site or configuration entry, and on a state using only local transport consistent with `PEC-API-001` it passes; no fixture outcome changes according to whether a loopback listener is later permitted. | VER-003 | PASS — RF-002 resolved on revised exact bytes |
| AC-004 | Both assertions execute on every change to the service core and on every release candidate, each execution bound to the exact state it evaluated, and no earlier passing run is presented as evidence for a later state. | VER-004 | PASS for registration/state binding; no artifact acceptance inferred |
| AC-005 | On a release candidate whose assertions fail, and on one against which either assertion was not executed, the mechanism returns an explicit blocking verdict, demonstrated on a candidate deliberately constructed to violate each rule and on a candidate for which the check was withheld. Whether that verdict binds the release is CON-002 and AC-011, not this criterion. | VER-005 | PASS mechanically; AC-011 owner confirmation remains separate |
| AC-006 | Each assertion, when given an unresolvable manifest, an unreadable surface, or a failing tool invocation, reports failure; no such condition yields a pass, a skip, or an empty successful result. | VER-006 | PASS on recorded fault injection |
| AC-007 | The registration remains armed without further action: disabling, removing, or bypassing either assertion is a visible change to the gate configuration and produces a reported gate failure rather than a silent no-op. | VER-007 | PASS on recorded scratch mutation |
| AC-008 | The enforcement mechanism adds no third-party runtime dependency to the service core, makes no network call, and leaves service-core source and dependency manifests unmodified across a full run. | VER-008 | PASS |
| AC-009 | The posture note contains every element required by REQ-010, states the operative definitions recorded under REQ-009, and asserts no completion of the enforcement obligation. | VER-009 | PASS |
| AC-010 | An accountable owner confirms that neither the posture note nor either assertion resolves, pre-empts, or forecloses `OI-009` / `SOW-083`, and that the enforcement makes no governed act depend on PEC-held state. | HUMAN_REVIEW | PENDING OWNER CONFIRMATION |
| AC-011 | An accountable owner confirms, or declines to confirm, that the enforcement delivered under this contract carries release-gating authority — that its blocking verdict blocks a release candidate — given that `C-08`'s standing-node classification carries "owner confirmation requested" and was accepted at `D-PEC-62` §1.4 as a recorded-but-unresolved, non-gating annotation (CLM-006, CON-002). A decline leaves the mechanism's verdicts advisory and invalidates no other criterion in this contract; the standing framing of the contract stands either way, because it is how the contract is written rather than a claim about the gate's force. | HUMAN_REVIEW | PENDING OWNER CONFIRMATION |

### Common and independent-verification checks

| ID | Check | Result |
|---|---|---|
| AP-001 | Exact 18-row candidate inventory present and hash-reproducible | PASS |
| OC-001 | OBJ-005 trace remains consistent | PASS |
| XD-001 | Candidate/evidence package is internally hash-reproducible | PASS after owner-ordered final manifest reseal — RF-001 resolved |
| DS-001 | Active dependency anchors are satisfied | PASS |
| TB-001 | Open items and owner confirmations remain explicit | PASS |
| IV-001 | Applicable D-PEC-77 and SOW requirements traced | PASS |
| IV-002 | Contractual/evidence traceability is reproducible | PASS after owner-ordered final manifest reseal — RF-001 resolved |
| IV-003 | Analysis method is adequate for the asserted no-egress rule | PASS — import-derived fixed-point AST binding verified with novel probes |
| CU-001 | Integration-owner completion stayed within D-PEC-77 exact path and act fence | PASS |

## Gate 3 — independent mechanical findings

### RF-001 — stale D-PEC-77 manifest (`MAJOR`)

The owner ordered the manifest resealed as the final write after all other
revisions. Agent 0 serialized that closeout after RF-002's independent rerun,
using the final execution-handoff and decision-record hashes together with
activation SHA-256 `111203c7…` and registered-check SHA-256 `074f0a15…`.
The resolution is effective only upon the immediately succeeding read-only
`shasum -a 256 -c MANIFEST.sha256` reproduction of all seven rows; a failed
reproduction voids this closure record and leaves RF-001 open.

**Proposed disposition:** `REVISE` (proposal).  
**HumanDisposition:** `REVISE`; **Status:** `RESOLVED` by the serialized final
reseal and seven-row reproduction condition above.

### RF-002 — locality false negatives (`MAJOR`)

The owner ruled `REVISE`. On checker SHA-256
`3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643`
and locality-test SHA-256
`69051b4c127009c821886c4cc6aea70222f57c3ad51013bdebe53a6211d92d20`,
the three original scratch modules now each return overall/locality `BLOCK`
with a located `EXTERNAL_NETWORK_CALL`:

| Scratch source | Source SHA-256 | Result |
|---|---|---|
| `import socket as s; s.create_connection(("198.51.100.10",443))` | `303b635b082646ef9b62979f779960a5a513ed8d9cafb489a431af9742095eaa` | BLOCK at line 2 |
| `import socket; socket.socket().connect(("198.51.100.10",443))` | `ad74e807c6ffcb555cc84fe342bb131717423ad4bb3ec4f1c510564ae0627d4a` | BLOCK at line 2 |
| `import urllib.request as req; req.urlopen("https://example.invalid")` | `5c765f1daa1b8989dabf39c54658625a0f107aebbc5808847b49ad8f7b68de4a` | BLOCK at line 2 |

Fresh independent probes, absent from producer tests, also pass their expected
classification:

| Novel probe | Source SHA-256 | Result |
|---|---|---|
| imported `socket.create_connection` symbol, assigned callable alias, external tuple | `2f68860aa7c15a6ea2968894c0f0b8a8a8a8688e5a59099d38df2e726d0791a1` | BLOCK, endpoint `203.0.113.41`, line 3 |
| aliased `socket` module, assigned class alias, inline constructor, external tuple | `dd5bc3f280bed933de8bf7cacca59eb9ea403b10b780fada0a54b14a390f41e9` | BLOCK, endpoint `203.0.113.42`, line 3 |
| `from urllib import request` alias plus assigned `urlopen`, keyword URL | `d9b3d396cc102cd697738156de0c5a3be796957820639dc8ce401f107333d583` | BLOCK, located URL, line 3 |
| imported `HTTPConnection`, assigned constructor alias, keyword host | `af89a67224b7720ed5c34acf14950bb0802c48d256d524110053184f7aaf14c9` | BLOCK, located host, line 3 |
| imported socket class plus assigned factory alias, Unix-domain endpoint | `3e4f62c29e1faf10c9ca066c0d35e6fe8d80304c1d96e734204d8a74621d5986` | PASS, zero locality findings |
| aliased socket module plus assigned factory alias, IPv6 loopback | `e19d81462f2d5f4ac30fdc7eae56ed707a9e8555a5e340eae42e8b4f77f70de7` | PASS, zero locality findings |

The full producer suite independently reran 19/19 PASS. The combination of
new spelling/import shapes, fixed-point aliases, inline receivers, keyword
endpoints, and preserved local classifications verifies a general binding
repair rather than a patch limited to the original three spellings.

**Proposed disposition:** `REVISE` (proposal).  
**HumanDisposition:** `REVISE`; **Status:** `RESOLVED` on the revised hashes.

## CU-001 containment verdict

`PASS`. The interrupted implementer returned no accepted result. The shared
integration owner completed only the three missing test modules and the
required verification/fan-in records. The three modules are exact §3.2 paths;
all other candidate inventory paths, the additive workflow postimage, the
activation record, execution handoff, manifest, and later decision/register/
receipt recording are explicitly permitted by packet §3.2. No evidence shows
an integration-owner product, lifecycle, decomposition, Task Management,
foreign-loop, release, acceptance, or professional-reliance act outside the
packet fence. The RF-002 repair itself changed only the packet-authorized
checker and locality-test paths; evidence and handoff updates stayed inside
the same act fence. This verdict does not cure RF-001.

## Findings summary and transition posture

| Severity | Total | Resolved | Open | Human disposition TBD |
|---|---:|---:|---:|---:|
| CRITICAL | 0 | 0 | 0 | 0 |
| MAJOR | 2 | 2 | 0 | 0 |
| MINOR | 0 | 0 | 0 | 0 |
| OBSERVATION | 0 | 0 | 0 | 0 |

RF-002 is resolved on the independently exercised revised checker. RF-001 is
resolved only through the serialized final-reseal condition recorded above.
The evidence-based Gate 5 recommendation remains `RECOMMEND_HOLD` at
`INITIALIZED`; no lifecycle write is authorized or made. No produced artifact
or acceptance criterion is accepted by this review closeout.
