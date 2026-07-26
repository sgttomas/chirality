# APP-HOLD-1 Candidate — Unresolvable Decomposition-Basis Reliance Hold

Status: `CANDIDATE_NOT_APPLIED`  
Prepared: 2026-07-26  
Prepared by: HELPS_HUMANS (Agent 1), managed by HELP_HUMAN  
Git basis: `918bb48b8fcee66c031d0d6d4040a46089f96067`  
Owner authority: OD-1 preparation approval, 2026-07-26  
Artifact class: proposal; non-authoritative until exact candidate bytes are accepted and applied through a separately authorized App-loop act

## Objective

Prevent any reliance on an App `ScopeOfWork.md` whose declared
`decomposition_basis` cannot be resolved and verified, without inventing a
replacement provenance claim.

The deterministic execution-time scan is authoritative. The expected set is a
review-derived assertion that the scan must confirm or contradict:

- `DEL-02-01`
- `DEL-02-02`
- `DEL-02-04`
- `DEL-05-04`
- `DEL-08-02`
- `DEL-08-03`

## Proposed hold

If adopted, `APP-HOLD-1` binds every held contract regardless of entry path.
No session, agent, workflow, direct invocation, API path, resumed run, or
dependency consumer may:

1. rely on a held contract as an accepted basis;
2. dispatch work whose authority or scope depends on a held contract;
3. promote a held deliverable into `CHECKING`; or
4. consume a held deliverable or contract as an accepted dependency.

`WORKING_ITEMS` preflight is the primary enforcement mechanism. It is not the
source or limit of the prohibition. Fan-in must reject a return whose work or
dependency basis violates the hold, including work that entered through a path
other than `WORKING_ITEMS`.

No held contract is repinned by this candidate. A future population-wide repin
may occur only after a corrected App decomposition is accepted and provenance
for the resulting target basis is established.

## Scan authority

`tools/app_hold.py scan`:

- discovers every `ScopeOfWork.md` below the live App execution tree;
- parses its front-matter `deliverable_id`, `package_id`, and
  `decomposition_basis`;
- verifies both the Git object and the basis path at that object;
- classifies any unresolvable object or missing path as `HELD`;
- compares the governed result with `APP_HOLD_REGISTER.csv`; and
- fails closed on malformed, duplicate, or missing identifying fields.

The scan result wins over this candidate's expected set. A mismatch blocks
application or dispatch and returns to the owner; it is never silently
absorbed.

## Exact owner exception mechanism

APP-HOLD-1 provides no runtime-consulted exception register and does not parse
owner prose. A held target always returns `BLOCK_APP_HOLD`.

Human override remains possible only through a later, separately proposed,
exactly accepted, and applied App-loop amendment to APP-HOLD-1's live
register, tool, and instruction surfaces. That amendment must identify its
target, operation, entry-path scope, reason, duration, and restoration or
expiry behavior. It must be effective before the prohibited act begins.

An owner statement, decision file, Git commit, workflow brief, manager
decision, test result, or successful tool run cannot release a target through
this candidate's runtime. This deliberately trades convenience for a smaller
and auditable authority surface.

## Candidate application surfaces

Only a later, separately authorized application may create or change live
surfaces:

| Candidate source | Proposed live surface | Purpose |
|---|---|---|
| `APP_HOLD_REGISTER.csv` | `execution/_Coordination/APP_HOLD_REGISTER.csv` | Machine-readable active hold |
| `tools/app_hold.py` | `execution/_Scripts/app_hold.py` | Deterministic scan and operation gate |
| `tests/test_app_hold.py` and fixtures | `execution/_Scripts/tests/` | Positive and negative regression checks |
| `INTEGRATION_CONTRACT.md` | App `AGENTS.md`, `software-workflow.json`, and applicable run briefs/fan-ins | Exact preflight and fan-in obligations |
| exact tool catalog rows in `INTEGRATION_CONTRACT.md` | root `tools/REGISTRY.md` and App `execution/_Scripts/README.md` | Required deterministic-tool registration |
| `D-APP-75_RULING_TEMPLATE.md` | App `execution/_Coordination/_DECISIONS/D-APP-75_RULING_2026-07-26.md` plus `_DECISIONS/_REGISTER.md` | Durable App-loop authority for exact application |

This proposal does not modify any of those live surfaces.

`D-APP-75` is the next free App decision ID at the candidate basis. Application
must recheck that it remains free. A collision returns for deterministic
reminting and a refreshed owner candidate; it is not silently renumbered.

## Enforcement boundary

The prohibition is universal, but the candidate does not claim universal
product-code interception. WORKING_ITEMS receives the primary pre-act
target-specific gate. Direct/API/resumed/other-workflow entry remains bound by
the App instruction and is checked at fan-in when it enters governed work.
The registered workflow check verifies corpus/register integrity only. A
future proposal may add product-route interception, but APP-HOLD-1 does not
create that product scope.

## Validation and decision posture

The live-basis scan and candidate tests are recorded in `SCAN_RESULT.json` and
`TEST_RESULT.txt`. `ARTIFACT_HASHES.sha256` binds the complete candidate
packet.

Owner acceptance of this candidate would authorize only the exact application
surfaces and semantics presented here. It would not authorize repinning,
architecture scope change, Root PRD amendment, App SCOPE_CHANGE, lifecycle
acceptance, or Git integration.
