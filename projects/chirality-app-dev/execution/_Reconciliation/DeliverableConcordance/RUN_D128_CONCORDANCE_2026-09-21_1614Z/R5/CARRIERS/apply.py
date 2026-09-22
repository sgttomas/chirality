#!/usr/bin/env python3
"""Bounded D-APP-131 carrier repairs; preserve exact before/after text and row mapping."""
import csv, hashlib, json, re, subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
PROJECT = ROOT / 'projects/chirality-app-dev'
RUN = PROJECT / 'execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z'
OUT = RUN / 'R5/CARRIERS'
BASE = '379df923927d157be3ebb51d8a1dcf783d970112'
rows = list(csv.DictReader((RUN / 'R3/CLAIM_CONCORDANCE.csv').open()))
manifest = []

def sha(s): return hashlib.sha256(s.encode()).hexdigest()

def replace(delid, start, end, body, units, reason):
    path = next((PROJECT / 'execution').glob(f'PKG-*/1_Working/{delid}*/ScopeOfWork.md'))
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text()
    begin = text.index(start)
    finish = text.index(end, begin + len(start)) if end else len(text)
    old = text[begin:finish]
    original = subprocess.check_output(['git', 'show', BASE + ':' + rel], text=True)
    ob = original.index(start)
    oe = original.index(end, ob + len(start)) if end else len(original)
    assert old == original[ob:oe], 'Refusing to overwrite an already repaired or independently changed block'
    new = body.strip() + '\n\n'
    before = OUT / f'{delid}_{len(manifest)+1:03d}_before.md'
    after = OUT / f'{delid}_{len(manifest)+1:03d}_after.md'
    before.write_text(old); after.write_text(new)
    matched = [r for r in rows if r['DeliverableID']==delid and any(r['ClaimID']==u or r['ClaimID'].startswith(u+'.') for u in units)]
    assert matched, (delid, units)
    for row in matched:
        manifest.append(dict(ClaimKey=row['ClaimKey'],DeliverableID=delid,Path=rel,Start=start,End=end or 'EOF',Execution='b',BeforeSHA256=sha(old),AfterSHA256=sha(new),Before=before.relative_to(ROOT).as_posix(),After=after.relative_to(ROOT).as_posix(),Authority='D-APP-131; D-APP-127; D-GOV-43',Reason=reason,PriorDisposition=row['Disposition'],ImplementationEvidence=row['ImplementationEvidence'],VerificationEvidence=row['VerificationEvidence']))
    path.write_text(text[:begin]+new+text[finish:])

link = 'execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z'
note = 'Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.'

replace('DEL-03-01','### CLM-005 — Construction','### CLM-006',f'''### CLM-005 — Engine boundary and conformance

The App must consume the Runtime-owned engine boundary for the sole qualified MVP engine, Codex. Turn inputs preserve the active session, registered project root, selected role, permission policy, resolved runtime options, content and attachment references, and cancellation semantics required by the accepted contract. Contract-module filenames, interface signatures and former shim paths are implementation evidence, rather than an additional App implementation mandate.

The surviving request/session correctness obligations must be mapped to current verification, including D-GOV-43 S-1–S-8 where applicable. D-GOV-43 retires vanished-purpose gates and avoids duplicate checks for the same condition; the legacy suite as a whole is not a new blanket admission gate. Deterministic stub and retained SDK tests establish only their own subjects. P-08 remains a bounded coverage-mapping residual: identify genuinely uncovered live-Codex obligations for accepted turns, terminal outcomes, capabilities, applicable tool handling and secret protection; do not declare equivalence without that mapping.

Verification hooks: `projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/lib/engine-conformance.test.ts`. The last is retained compatibility/test evidence and is not a live-Codex qualification witness.

{note}''',['CLM-005'],'Lift source paths and TypeScript shapes into evidence; retain input and conformance requirements and the missing Codex witness.')

replace('DEL-03-02','### CLM-005 — Construction','### CLM-006',f'''### CLM-005 — Runtime lifecycle and App transport boundary

The App delegates execution to its application-owned Runtime service. Runtime owns turn admission and the one-active-turn-per-session invariant, releases active-turn ownership after a terminal outcome, and preserves accepted input and terminal evidence. HTTP and Desktop surfaces validate and transport requests and stream results; they do not create an independent runtime or acquire an App-local substitute lock.

Requests bind registered project identity/root, role, permission and delegation policy, runtime options, content and attachment references. Interrupt and cancellation handling remains coordinated with DEL-03-04. A renderer disconnect unsubscribes from the stream and must not interrupt the running turn. Public event handling preserves Codex notifications under the accepted protocol rather than promising the former closed SDK event vocabulary.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. Remaining binding and delegation-policy findings retain their own gates in `_STATUS.md`; the wording does not certify them complete.

{note}''',['CLM-005'],'Lift proposed filenames, in-module Set and TBD API snapshots; retain lifecycle, binding, and transport guarantees.')

replace('DEL-03-03','### CLM-005 — Construction','### CLM-006',f'''### CLM-005 — Route and stream compatibility

Harness routes must remain thin, validated clients of the App-owned Runtime service. Their compatibility obligation concerns the supported App operations and inspectable outcomes, with live Codex notifications preserved through the full protocol. Compatibility does not require manufacturing every legacy SDK event name or translating away an unknown Codex notification.

The stream must preserve ordering and replay identity, expose failures, and permit detach/reattach without turning a renderer disconnect into a turn interrupt. Runtime owns turn coordination. Route presence alone does not establish operation completeness: the live scaffold route's missing composition remains a P-15 residual, and fake-port tests do not establish a live fixture capture.

Verification hooks: `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`, `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`, and `projects/chirality-runtime/tests/daemon.test.ts`. `RouteAdapterTestIndex.md` and the R3 rows preserve missing-fixture evidence separately.

{note}''',['CLM-005'],'Replace SDK mapper and fixture-TBD mechanism assertions with stable compatibility and stream guarantees; preserve scaffold and fixture residuals.')

replace('DEL-03-04','### CLM-005 — Construction','### CLM-006',f'''### CLM-005 — Interrupt and durable terminal evidence

Explicit user interruption must reach the active Runtime turn, release turn ownership on termination, and preserve a truthful terminal outcome. Accepted input and attachment references must remain recoverable after failure. A disconnected renderer stops receiving frames; disconnection by itself must not cancel the turn or release active-turn ownership. Reattachment must expose the continuing or completed turn consistently.

Malformed-tail tolerance, unique event identity, append-only records, and the surviving secret-protection requirement remain verification obligations. No compatibility mapper or legacy SDK test substitutes for evidence on the live Codex path; the redaction gap is retained under P-12.

Verification hooks: `projects/chirality-runtime/tests/app-owned-composition.test.ts`, `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/daemon.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`.

{note}''',['CLM-005'],'Lift former mapper paths and test-TBD list; apply D127 disconnect supersession while retaining termination, persistence, and redaction duties.')

replace('DEL-03-02','### Current responsibility','### Current acceptance obligations',f'''### Current responsibility

App HTTP and Desktop surfaces are clients of the application-owned Runtime service. They bind registered project identity/root, role, permission and delegation policy, and runtime options; Runtime owns the session lifecycle and the one-active-turn invariant. The App must not construct a second runtime.

The delegation-policy purpose survives, while the retired Root DEL-02-11 storage owner does not. D-APP-127 retires the former Root owner; it does not settle the replacement storage or interface allocation for the surviving policy. Binding/default behavior and that ownership follow-through remain open rather than being inferred from the existence of an App thread index or upstream agent configuration.

Verification hooks: `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts` and `projects/chirality-runtime/tests/turn-hardening.test.ts`.

{note}''',['SEC-1'],'Apply accepted A2 ownership without asserting all binding behavior is implemented.')

replace('DEL-03-02','### Current acceptance obligations','### Seating and rulings',f'''### Current acceptance obligations

1. App HTTP and Desktop surfaces remain clients of the application-owned Runtime service; Runtime owns session execution state and the active-turn invariant.
2. Boot and session-creation requests bind registered project identity/root, role, mode, delegation policy and options; the boot fingerprint reflects the real inputs.
3. The accepted delegation policy defaults to `none`, narrows managed delegation only, and adds no delegation class. The retired Root DEL-02-11 is no longer an acceptance dependency. Replacement storage/interface ownership and verification of the surviving policy obligation remain explicit residuals; this clause assigns no new storage field.

{note}''',['SEC-2'],'Apply A2 and retired Root owner; retain binding and delegation obligations and residuals.')

replace('DEL-05-02','### Current responsibility','### Current acceptance obligations',f'''### Current responsibility

Consume Runtime-owned event records for App audit and replay without owning the generic writer. Preserve accepted-turn and terminal evidence and keep Codex notifications inspectable as received, including unfamiliar methods. The event vocabulary is open under D-GOV-43 and D-APP-127; the retired Root DEL-02-10 and closed schema are not current admission gates.

The App remains responsible for the accepted proposal interaction and its audit/replay meaning (SOW-082). Retiring the old schema gate does not certify proposal-event implementation or remove any unfulfilled user-facing guarantee.

Verification hooks: `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `projects/chirality-runtime/tests/turn-hardening.test.ts`, and `projects/chirality-runtime/tests/app-owned-composition.test.ts`.

{note}''',['SEC-1'],'Apply Runtime ownership and full event preservation; retain proposal audit purpose.')

replace('DEL-05-02','### Current acceptance obligations','### Seating and rulings',f'''### Current acceptance obligations

1. Runtime event records are consumed for App audit and replay without creating a second generic schema or writer.
2. The App preserves the accepted offer/accept/adjust/decline proposal audit meaning where that interaction is supported. Former `proposal.*` candidates and Root DEL-02-10 approval are historical implementation and ownership evidence; they do not restrict the open Codex event stream. Unfulfilled proposal behavior stays in Remaining.
3. Accepted-turn and terminal-event persistence conformance is verified with malformed-tail tolerance preserved; unknown Codex notifications remain inspectable and the surviving secret-protection obligation remains visible.

{note}''',['SEC-2'],'Lift closed event enumerations and retired owner gate; preserve proposal meaning and durability.')

replace('DEL-02-05','### Current responsibility','### Current acceptance obligations',f'''### Current responsibility

Provide the App account and runtime-feedback experience, selected-project attachment controls, typed errors, and retry-preserving failure state. Codex owns credentials and the account login/logout methods. Chirality presents its own sign-in state without reading, copying, or relaying credentials; its sign-out must leave other Codex clients unchanged.

The effective Codex home shares the user configuration and resources by reference while keeping authentication and model-cache state private to Chirality. The user selects approval and sandbox policy for each project/turn. Retired hosted admission, root-private account consent, brokerage generations, model residency, and external local-model-server status are not current live-login prerequisites.

The account row and right-panel Settings retain their accepted presentation ownership. Labels and current state must be truthful, with unavailable or fixture state distinguished from verified live login. DEL-09-06 retains attachment, credential-IPC, renderer, and other surviving security verification. Broader role and exact account-indicator conflicts are accounted separately; this repair does not silently decide those rows.

Verification hooks: the production S-8 account check in `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md` and `projects/chirality-runtime/tests/app-owned-composition.test.ts`. Native outcomes require their actual recorded evidence.

{note}''',['SEC-1'],'Apply accepted credential custody, A2, and surviving UX purpose; preserve unresolved presentation and native-evidence matters.')

for delid, heading in [('DEL-09-04','Codex MVP packaging basis'),('DEL-09-05','Current Codex MVP conformity'),('DEL-09-06','Current Codex MVP conformity')]:
    extra = ('Artifact identity must bind the selected candidate package version, App Info.plist and actual `Chirality-<candidate-version>-arm64.dmg`. Packaged executable behavior and instruction-root integrity require actual package evidence. Signing, notarization, minimum-OS and architecture inspection results must be recorded against that candidate; no result is inferred from a missing record.' if delid != 'DEL-09-06' else 'The accepted S0/default-app PDF fallback remains the current MVP basis; S1 built-in multi-page PDF criteria remain inapplicable to this release. Applicable attachment budgets, containment, nonce/window/IPC, renderer-egress and packaged default-app observations remain required. No native PASS is inferred from source tests.')
    replace(delid, f'## {heading}', '## Purpose and Objective Traceability',f'''## {heading}

Codex is the sole MVP engine. Under D-GOV-43 topology A2 and D-APP-127, the App owns its Runtime service child and Runtime owns the stock Codex App Server child. Hosted supplier admission, per-root account consent, the LaunchAgent, packaged-basis hashing and supplier-containment evidence are retired subjects; they are not present-day qualification gates.

The App must preserve Codex-held credential custody and separation from other Codex clients, user-selected approval and sandbox policy, truthful event/approval presentation, and applicable renderer, attachment, secret-protection and package-executability controls. Historical Anthropic/Claude/Pi descriptions remain compatibility evidence and do not qualify the live Codex path.

{extra}

Verification hooks: `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md` and `NATIVE_CHECKLIST.md` in the same folder, plus `frontend/package.json` registered packaging/security commands. These procedures supersede the retired Stage 9–13 spine; repeat affected checks when source, configuration or packaging changes invalidate earlier evidence. No publication or product acceptance follows from this text repair.

{note}''',['SEC-1'],'Apply D127 explicit retirement and replacement of packaging/security subjects; retain candidate-bound evidence and surviving controls.')

with (OUT/'REPAIR_MANIFEST.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(manifest[0]));w.writeheader();w.writerows(manifest)
print(json.dumps({'source_rows':len(manifest),'deliverables':len({x['DeliverableID'] for x in manifest}),'blocks':len({x['Before'] for x in manifest})}))
