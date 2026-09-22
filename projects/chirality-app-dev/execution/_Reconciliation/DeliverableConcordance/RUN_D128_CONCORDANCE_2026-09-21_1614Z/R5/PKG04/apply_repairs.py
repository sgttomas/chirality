#!/usr/bin/env python3
"""Apply the bounded PKG-04 R5 block lifts, preserving the received bytes."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[8]
APP = ROOT / 'projects/chirality-app-dev'
HERE = Path(__file__).resolve().parent
RUN = HERE.parent.parent

REPLACEMENTS = {('DEL-04-01', 'CLM-003'): '### CLM-003 — Attributes\n'
                           '\n'
                           'The current engine is the stock, version-pinned Codex App Server owned '
                           'by the\n'
                           "App's Runtime service (D-GOV-43 A2; D-APP-127; `docs/CONTRACT.md` "
                           'K-ENGINE-3).\n'
                           "D-APP-68's first-adapter `ADOPT_WITH_RESIDUAL_RISK` remains historical "
                           'evidence\n'
                           'within its demonstrator boundary; it does not qualify Codex.\n'
                           '\n'
                           'The probe package must preserve the evaluated version, source state, '
                           'results,\n'
                           'approver, limitations and fallback criteria. Verify these against\n'
                           '`Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` and\n'
                           '`Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`. Mechanism snapshots are '
                           'retained\n'
                           "in this run's R5 PKG04 before-block evidence.\n"
                           '\n'
                           'Applicable runtime-interface, event, session, permission, root, '
                           'instruction,\n'
                           'redaction and provenance guarantees remain current obligations. Their '
                           'live\n'
                           'qualification uses the D-GOV-43 S-1 to S-8 checks, not historical SDK '
                           'results.\n'
                           '\n',
 ('DEL-04-01', 'CLM-009'): '### CLM-009 — Scope\n'
                           '\n'
                           'Preserve the first-adapter probe and adoption evidence for SOW-018, '
                           'SOW-044\n'
                           'and SOW-046 as compatibility history under D-GOV-43 and D-APP-127. '
                           'Readers\n'
                           'must be able to establish the evaluated behavior, demonstrator '
                           'decision\n'
                           'boundary and residual risks through\n'
                           '`Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` and\n'
                           '`Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`.\n'
                           '\n'
                           'This evidence slice excludes downstream runtime implementation and '
                           'activation\n'
                           'of additional tools or providers. SDK transcripts are not '
                           'authoritative\n'
                           'project records. Session/storage evidence gaps remain partial. Newer\n'
                           'App-client/SOW-079 scope and traceability reconciliation remains '
                           'assigned to\n'
                           'the owning loop; the R5 PKG04 return records that residual.\n'
                           '\n',
 ('DEL-04-02', 'CLM-009'): '### CLM-009 — Scope\n'
                           '\n'
                           'The retained Claude options builder is compatibility evidence for '
                           'earlier\n'
                           'options, settings, tool mapping, metadata and max-turn work. Current '
                           'App\n'
                           "integration must honor the user's Codex configuration and selected "
                           'approval /\n'
                           'sandbox policy, preserve safe metadata, and exclude credentials from '
                           'project\n'
                           'records (D-GOV-43 items 3, 4, 8 and 9; D-APP-127; K-ENGINE-3; '
                           'K-KEY-1).\n'
                           'The former empty Claude settings-source mechanism does not restrict '
                           "Codex's\n"
                           'native discovery or shared user configuration.\n'
                           '\n'
                           'Verification hooks: Runtime `tests/codex-effective-home.test.ts` and\n'
                           '`tests/codex-supervisor.test.ts`, plus applicable re-platform native '
                           'checks.\n'
                           'Legacy evidence remains in the R5 PKG04 manifest.\n'
                           '\n'
                           'Instruction composition, App event mapping and credential-boundary '
                           'work\n'
                           'remain in DEL-04-04, DEL-04-03 and DEL-04-05. Generic implementation '
                           'stays\n'
                           'Runtime-owned; PKG-06/PKG-08 control guarantees and event-store '
                           'ownership are\n'
                           'unchanged. Unmet live controls remain open.\n'
                           '\n',
 ('DEL-04-02', 'CLM-023'): '### CLM-023 — Purpose\n'
                           '\n'
                           'Runtime option composition must make the effective configuration and '
                           'chosen\n'
                           'policy inspectable without promoting convenience state into project '
                           'authority.\n'
                           'D-GOV-43 items 3 and 4 and D-APP-127 govern the Codex path. Claude '
                           'fallback\n'
                           'chains and settings isolation are compatibility history.\n'
                           '\n'
                           'Verify current configuration and policy through the hooks in CLM-009.\n'
                           '`frontend/src/__tests__/lib/sdk-options-builder.test.ts` remains '
                           'historical\n'
                           'builder evidence and does not qualify the live path.\n'
                           '\n',
 ('DEL-04-03', 'CLM-003'): '### CLM-003 — Attributes\n'
                           '\n'
                           '| Attribute | Required boundary | Verification / authority |\n'
                           '|---|---|---|\n'
                           '| Scope and objectives | App client event mapping and conformance for '
                           'SOW-040, SOW-044, SOW-051 and OBJ-002, OBJ-004. Generic Runtime event '
                           'semantics remain Root-owned. | SCA-APP-005; `_CONTEXT.md` Deliverable '
                           'Scope. |\n'
                           '| Browser-facing output | Preserve upstream method names, identifiers '
                           'and payloads after required redaction; provide normalized views for '
                           'known events and inspectable unfamiliar notifications. The earlier '
                           'fixed event-name list is compatibility history. | `docs/CONTRACT.md` '
                           'K-EVENT-1 and K-EVENT-6; D-GOV-43 item 2 and A2 supplement; '
                           '`frontend/src/__tests__/lib/harness-event-views-codex.test.ts`. |\n'
                           '| Persisted output | App mapping conforms to the Runtime-owned '
                           'versioned event contract and does not create a second canonical writer '
                           'or silently replace that contract. | `docs/CONTRACT.md` K-EVENT-4; '
                           'App/Runtime conformance fixtures. |\n'
                           '| Source-specific data | Preserve upstream data as required by '
                           'D-GOV-43 while distinguishing operational event data from '
                           'authoritative project evidence; preserve redaction at every sink. | '
                           '`docs/CONTRACT.md` K-EVENT-6; re-platform S-1 and S-7. |\n'
                           '| Historical SDK evidence | The Claude mapper, input categories and '
                           'probe sequence belong to the retained adapter evidence. They do not '
                           'define a notification whitelist or current engine requirement. | '
                           '`sdk-message-mapper.ts` and its tests, and DEL-04-01 '
                           '`Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`; R5 PKG04 evidence '
                           'preserves the earlier attribute text. |\n'
                           '\n'
                           'The listed checks are verification hooks. This text repair does not '
                           'assert a\n'
                           'new test result, native result, or closure of a partial claim.\n'
                           '\n',
 ('DEL-04-03', 'CLM-008'): '### CLM-008 — Scope\n'
                           '\n'
                           'Map Runtime outputs for the App interface and verify conformance to\n'
                           'Root-owned event semantics under SCA-APP-005. D-GOV-43 (A2) requires '
                           'the\n'
                           'complete notification/request stream, redaction, normalized known '
                           'views,\n'
                           'inspectable unfamiliar notifications and explicit unsupported-request\n'
                           'outcomes. A fixed SDK category list must not drop activity or leave '
                           'requests\n'
                           'unanswered. The Claude mapper is compatibility evidence.\n'
                           '\n'
                           'Verification hooks: App '
                           '`frontend/src/__tests__/lib/harness-event-views-codex.test.ts`\n'
                           'and '
                           '`frontend/src/__tests__/components/live-session-requests.test.tsx`, '
                           'Runtime\n'
                           '`tests/codex-app-server-client.test.ts`, and re-platform S-1/S-7 '
                           'native evidence.\n'
                           '\n'
                           'Generic interfaces and event production stay Runtime-owned, with App\n'
                           'conformance in DEL-03-01 and storage under its owning Runtime/PKG-05 '
                           'contract.\n'
                           'Options, probe evidence and credentials stay in DEL-04-02, DEL-04-01 '
                           'and\n'
                           'DEL-04-05. Tool permissions and other package scope are unchanged.\n'
                           '\n',
 ('DEL-04-04', 'CLM-005'): '### CLM-005 — Construction\n'
                           '\n'
                           'The App consumes a source-grounded instruction basis through Runtime, '
                           'retaining\n'
                           'the selected role/method content, origins and hashes for replay. '
                           'Chirality\n'
                           "context is additive and preserves Codex's base instructions and tool "
                           'behavior\n'
                           '(D-GOV-43 item 8).\n'
                           '\n'
                           'Verification hooks: Runtime '
                           '`tests/instruction-basis-and-method-transition.test.ts`\n'
                           '(exact supplied bytes and false-hash rejection) and '
                           '`tests/runtime-v3-api.test.ts`\n'
                           '(exact v3 context supplied at adapter boot). Historical '
                           'composer/fingerprint\n'
                           'mechanics are retained in the R5 PKG04 evidence manifest.\n'
                           '\n'
                           'Instruction-root protection, professional-boundary reminders and '
                           "SCA-APP-010's\n"
                           'organisation-layer, roadmap and fingerprint obligations remain '
                           'current.\n'
                           "D-APP-119's residual and the unknown downstream interface remain "
                           'open.\n'
                           '\n',
 ('DEL-04-04', 'CLM-023'): '### CLM-023 — Purpose\n'
                           '\n'
                           'Traceable instruction composition must let a reader reconstruct the '
                           'active\n'
                           'role and method context against its actual source basis. Runtime '
                           'supplies\n'
                           "supported additive Chirality context while preserving Codex's own "
                           'instructions\n'
                           '(D-GOV-43 item 8); the SDK composer remains compatibility evidence.\n'
                           '\n'
                           "Verify source-grounded composition through CLM-005's named checks. "
                           'Prompt text\n'
                           "does not enforce safety or confer acceptance. SCA-APP-010's "
                           'organisation-layer\n'
                           "and roadmap obligations, including D-APP-119's unresolved ruling, "
                           'remain open.\n'
                           '\n',
 ('DEL-04-05', 'CLM-003'): '### CLM-003 — Attributes\n'
                           '\n'
                           '| Attribute | Required boundary | Verification / authority |\n'
                           '|---|---|---|\n'
                           "| Credential custody | Codex owns credential material in Chirality's "
                           'effective home. The App must not read, copy or relay it, and '
                           "sign-in/out must leave other Codex clients' authentication unchanged. "
                           "| D-GOV-43 items 3 and 6; D-APP-127; the re-platform run's S-8 native "
                           'check. |\n'
                           '| Private state | Credentials and authentication ceremony data are '
                           'non-project state and must not enter durable events, project files, '
                           'logs or tool artifacts. Safe account/status projection exposes no key '
                           'material. | `docs/CONTRACT.md` K-KEY-1 and K-EVENT-6; secret-evidence '
                           'and redaction checks. |\n'
                           '| Network boundary | App transport uses the governed endpoint policy; '
                           "Codex command network follows the user's selected configuration and "
                           'sandbox policy. Neither this attribute nor compatibility code grants '
                           'additional network scope. | D-GOV-43 item 4; `docs/CONTRACT.md` '
                           'K-NET-1; endpoint-policy tests and applicable native evidence. |\n'
                           '| Failure handling | Provider-boundary outcomes must remain truthful, '
                           'typed where required by their contract, and redacted. A historical '
                           'Anthropic failure fixture is not live Codex evidence. | '
                           '`docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; '
                           '`frontend/src/__tests__/lib/redaction-path-matrix.test.ts`; live-path '
                           'evidence remains separately required. |\n'
                           '| Historical provider mechanics | Anthropic key precedence, storage '
                           'path, status vocabulary, base URL and seven-class failure taxonomy '
                           'describe retained compatibility evidence. | Current Codex-only basis '
                           'in `docs/CONTRACT.md`; exact prior attributes and evidence paths '
                           'preserved in R5 PKG04. |\n'
                           '\n'
                           'No native check outcome or residual closure is asserted here. '
                           'Engine-neutral\n'
                           'security requirements elsewhere in this document remain subject to '
                           'their\n'
                           'owning contracts and claim-level verification.\n'
                           '\n',
 ('DEL-04-05', 'CLM-005'): '### CLM-005 — Construction\n'
                           '\n'
                           'Current evidence must establish Codex credential custody, separated\n'
                           'authentication, secret-free App projections and the governing network '
                           'policy.\n'
                           'Verification hooks: Runtime `tests/codex-effective-home.test.ts`, the\n'
                           're-platform `NATIVE_CHECKLIST.md` S-8 native witness, and App '
                           'secret/redaction\n'
                           'checks under K-KEY-1 and K-EVENT-6. Configuration fixtures do not '
                           'establish\n'
                           'native sign-in/sign-out behavior; unknown results remain unknown.\n'
                           '\n'
                           'The R5 PKG04 manifest preserves earlier wrapper/key/base-URL '
                           'mechanisms and\n'
                           'fixtures as compatibility evidence. D-GOV-43 and D-APP-127 do not '
                           'require\n'
                           'recreating Anthropic storage, daemon custody or SDK key handoff. '
                           'Secret\n'
                           'protection, typed failure obligations and network controls remain '
                           'current.\n'
                           '\n',
 ('DEL-04-05', 'CLM-008'): '### CLM-008 — Scope\n'
                           '\n'
                           'This slice participates in the App credential, provider and network '
                           'boundary\n'
                           'under D-GOV-43 (A2), D-APP-127, K-KEY-1, K-EVENT-6 and K-NET-1. It '
                           'must\n'
                           'respect Codex custody, separated authentication, redacted '
                           'status/failure\n'
                           'projection and the applicable App/Codex network policies. Anthropic '
                           'key\n'
                           'precedence and SDK handoff are compatibility evidence. Verify current '
                           'behavior\n'
                           "through CLM-003/CLM-005's named checks; unmet live guarantees remain "
                           'open.\n'
                           '\n'
                           'Options stay in DEL-04-02, App mapping in DEL-04-03, account/Settings\n'
                           'presentation in DEL-02-05 and run logging in DEL-05-03. Runtime '
                           'retains generic\n'
                           'authentication implementation and canonical event storage. This '
                           'application\n'
                           'of accepted direction does not retire the deliverable or allocate new '
                           'scope.\n'
                           '\n',
 ('DEL-04-05', 'CLM-024'): '### CLM-024 — Purpose\n'
                           '\n'
                           'Protect private authentication state and preserve a truthful, redacted '
                           'App\n'
                           'boundary for provider activity. Codex is the sole current MVP engine '
                           'and\n'
                           'credential custodian (D-GOV-43; D-APP-127; current CONTRACT basis); '
                           'the earlier\n'
                           'Claude/Anthropic default is compatibility history.\n'
                           '\n'
                           'No secret exposure or unrecorded policy expansion is permitted. '
                           'CLM-003 and\n'
                           'CLM-005 name verification hooks for current credential/network '
                           'behavior;\n'
                           'historical key-precedence, base-URL and SDK-error fixtures do not '
                           'qualify it.\n'
                           '\n'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def write_csv(path, fields, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def main():
    if (HERE / 'REPAIR_MANIFEST.csv').exists():
        raise SystemExit('Refusing to overwrite preserved repair evidence')
    targets = sorted({did for did, cid in REPLACEMENTS})
    cmd = ['python3', 'execution/_Scripts/app_hold.py', 'check', '--operation',
           'dispatch', '--entry-path', 'workflows/reconciliation']
    for did in targets:
        cmd += ['--target', did]
    result = subprocess.run(cmd, cwd=APP, text=True, capture_output=True)
    (HERE / 'APP_HOLD_PREFLIGHT.json').write_text(result.stdout)
    if result.returncode or json.loads(result.stdout)['verdict'] != 'ALLOW':
        raise SystemExit(result.stderr or 'APP-HOLD-1 did not allow the targets')
    (HERE / 'BEFORE').mkdir()
    (HERE / 'AFTER').mkdir()
    source_rows = list(csv.DictReader((RUN / 'R3/CLAIM_CONCORDANCE.csv').open()))
    package_rows = [r for r in source_rows if r['PackageID'] == 'PKG-04']
    indexed = {r['ClaimKey']: r for r in package_rows}
    manifest, bindings = [], []
    for did in targets:
        path, = APP.glob('execution/PKG-04*/1_Working/' + did + '*/ScopeOfWork.md')
        original = path.read_bytes()
        text = original.decode()
        for (target, cid), replacement in REPLACEMENTS.items():
            if target != did:
                continue
            match = re.search(r'^### ' + cid + r'\b.*?(?=^### |^## |\Z)', text, re.M | re.S)
            if not match:
                raise SystemExit('Missing block ' + did + '#' + cid)
            before = match.group(0)
            key = did + '#' + cid
            row = indexed[key]
            before_path = HERE / 'BEFORE' / (did + '_' + cid + '.md')
            after_path = HERE / 'AFTER' / (did + '_' + cid + '.md')
            before_path.write_text(before)
            after_path.write_text(replacement)
            text = text[:match.start()] + replacement + text[match.end():]
            manifest.append({
                'ClaimKey': key, 'TargetPath': str(path.relative_to(ROOT)),
                'BlockID': cid, 'Execution': 'b',
                'GranularityBasis': 'Decision and interface; verification hooks named in repaired block',
                'Authority': 'D-GOV-43 (A2); D-APP-127; current Codex-only CONTRACT basis; current owner Agent0 R5/R6 delegation',
                'BeforePath': str(before_path.relative_to(ROOT)),
                'AfterPath': str(after_path.relative_to(ROOT)),
                'BeforeBlockSHA256': digest(before.encode()),
                'AfterBlockSHA256': digest(replacement.encode()),
                'SourceClaimKey': key,
                'SourceDisposition': row['Disposition'],
                'SourceImplementationEvidence': row['ImplementationEvidence'],
                'SourceVerificationEvidence': row['VerificationEvidence'],
                'SourceState': 'R3 evidence frozen at APP@00115c719; current documentary repair input separately hashed',
                'Outcome': 'TEXT_REPAIRED; no implementation result, lifecycle act or residual closure',
            })
        path.write_text(text)
        bindings.append({'Path': str(path.relative_to(ROOT)),
                         'BeforeSHA256': digest(original),
                         'AfterSHA256': digest(text.encode())})
    write_csv(HERE / 'REPAIR_MANIFEST.csv', list(manifest[0]), manifest)
    write_csv(HERE / 'SOURCE_BINDINGS.csv', list(bindings[0]), bindings)
    changed = {r['ClaimKey'] for r in manifest}
    preserved = [{
        'ClaimKey': r['ClaimKey'], 'R3Disposition': r['Disposition'],
        'Disposition': 'UNCHANGED_NOT_CLOSED',
        'Reason': 'Outside exact 12-block repair; source claim, controls and residuals preserved',
        'HumanDecisionNeeded': r['HumanDecisionNeeded'],
    } for r in package_rows if r['ClaimKey'] not in changed]
    write_csv(HERE / 'UNCHANGED_R3_CLAIMS.csv', list(preserved[0]), preserved)
    selected = [r for r in package_rows if r['ClaimKey'] in changed]
    write_csv(HERE / 'FROZEN_SOURCE_ROWS.csv', list(selected[0]), selected)
    print(json.dumps({'changed_blocks': len(manifest), 'changed_files': len(bindings),
                      'unchanged_R3_claims': len(preserved), 'all_R3_PKG04_claims': len(package_rows)}))

if __name__ == '__main__':
    main()
