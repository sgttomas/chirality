"""Apply the bounded PKG-08 R5 claim lifts. Not a reusable workflow."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[8]
OUT=Path(__file__).resolve().parent
assert (ROOT/'AGENTS.md').is_file(), ROOT
replacements={}
def add(d,c,title,body):
    replacements[(d,c)]=f'### {c} — {title}\n\n'+ '\n'.join('> '+line if line else '>' for line in body.strip().splitlines())+'\n\n'
add(1,'CLM-005','Construction','''##### Construction

The required outputs are evidence of conformance, packaging integrity and bounded execution. Their acceptance does not depend on a particular parser, fixture directory or function name. Apply the current App `AGENTS.md` role/context instructions; preserve the unresolved App SPEC §7 / CONTRACT K-WRITE-1 format-and-carrier question separately. This record repair does not accept D-GOV-42's exact bytes or amend the App corpus.

| Output | Requirement | Named verification hook and limit |
|---|---|---|
| Agent conformance evidence | Identify the supplied role, instruction origin and content, declared scope and applicable conformance contract; report missing or contradictory metadata. | `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts` is retained legacy-format evidence. Current-basis conformance still requires an applicable packaging/role test; a legacy parser pass does not prove it. |
| Integrity fixtures | Detect missing, changed and unexpected required instruction assets against the selected packaging basis. | `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`; D-APP-127's `instruction-root:integrity` check. |
| Source-completeness checklist | Identify incomplete required assets and carry remediation status, including SOW-073/OI-004. | `frontend/scripts/verify-instruction-root-integrity.mjs` checklist output and its named test above. |
| Governance fixtures | Verify child eligibility, explicit context and write scope, applicable approval gates, fail-closed admission and absence of authority expansion; distinguish instruction-asserted limits from mechanical enforcement. | `frontend/src/__tests__/lib/harness-subagent-governance.test.ts`, `agent-instruction-conformance.test.ts` and `chirality-hooks.test.ts` are legacy fixtures. Their coverage does not close missing invalid-write-scope or live-path enforcement evidence. |

D-GOV-43/D-APP-127 leave native sandbox and approval policy to the user's Codex configuration; declaring scope never proves host containment. The remaining evidence gaps above retain their owning implementation/governance route.''')
add(2,'CLM-005','Construction','''##### Construction

Construction must establish canonical role/session identity and preserve the user's navigation intent without granting execution authority. Current App `AGENTS.md` supplies the four-role operational basis; its use here is not a blanket D-GOV-42 exact-byte acceptance or an amendment of every older App clause.

| Contract | Required outcome | Named verification hook and limit |
|---|---|---|
| Alias resolution | Use only sourced aliases and resolve to an eligible canonical role; aliases must not create additional roles or grant TASK direct-entry authority. | `frontend/src/__tests__/lib/persona-resolution.test.ts` checks the current HELP/AGENTS aliases, HELP_HUMAN default and three direct-entry roles. |
| Persona identity | Preserve canonical role identity and the applicable instruction basis; missing or ineligible selections must not silently gain authority. | `frontend/src/__tests__/api/harness/routes.test.ts` and `frontend/src/__tests__/lib/persona-resolution.test.ts`; route and UI fallback subjects must be distinguished. |
| Legacy navigation | Preserve compatibility only within the accepted retirement boundary. A fixed matrix is not required in the active shell; D-APP-108 Q3 retains reachable, unlisted legacy routes. | `frontend/src/__tests__/lib/agent-matrix-cells.test.ts` is compatibility evidence, not an active matrix acceptance check. |
| Dialogue/session selection | Preserve exact selected identity, applicable query context and unknown parameters while guarding an in-flight primary session and retaining the adopted live/replay boundary. | `frontend/src/__tests__/lib/guarded-session-selection.test.ts` and `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`; the live query-preservation and resume/replay findings remain open. |
| Dispatch boundary | Navigation or selection may describe intent but must not grant dispatch, lifecycle or approval authority. Presentation-neutral dispatch remains owned by DEL-08-03. | `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts` and `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`. |

Implementation module names and query-key snapshots belong in those evidence records. The former F-001/D-001 implementation slots do not impose a recurring requirement to copy code paths or state keys into this deliverable. The older alias/default/route obligations elsewhere in this document and the App corpus retain the explicit P-06/P-22 amendment residual; this construction lift does not mark those rows closed.''')
add(3,'CLM-005','Construction','''##### Construction

| Required outcome | Named verification hook |
|---|---|
| Preserve the decision-bound DECOMP/PREP/TASK/AUDIT taxonomy and category options independently of presentation. | `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts`. |
| Disabled or unsupported options cannot initiate execution; admitted selection remains inert intent until separately authorized. | `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts`; `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`. |
| Scope identifies the active working root, a valid deliverable and, for knowledge-type scope, a valid target bucket; stale or disabled selections are rejected or cleared. | `frontend/src/__tests__/api/project/deliverables-route.test.ts`; `frontend/src/__tests__/lib/task-scope-selection.test.ts`. |
| Preserve child-governance and project-acceptance boundaries regardless of the component presenting intent. | `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`; the governance evidence owned by DEL-08-04. |

D-APP-108/SCA-APP-010 retired the active Pipeline presentation while retaining this semantic ownership. `frontend/src/__tests__/components/pipeline-surface.test.ts` is retained presentation/compatibility evidence; its existence does not establish an active shell consumer. No new consumer or execution authority is created by this lift.''')
add(3,'CLM-006','Implementation Evidence','''##### Implementation Evidence

The deliverable requires presentation-neutral, bounded dispatch intent, not a particular component or arrangement of option arrays. Verify that obligation through `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts`, including the exact taxonomy, disabled-option rejection and inert admitted intent; verify scoped target discovery through `frontend/src/__tests__/api/project/deliverables-route.test.ts` and `frontend/src/__tests__/lib/task-scope-selection.test.ts`.

The implementation evidence is `frontend/src/lib/pipeline/pipeline-dispatch-contract.ts`. The retained `frontend/src/components/pipeline/pipeline-surface.tsx` and its component tests provide compatibility presentation evidence under D-APP-108, not an active product-surface claim. Record revisions and actual results in the verification run; source filenames and local state layout are not additional scope obligations.''')
add(4,'CLM-003','Attributes','''##### Attributes

| Attribute | Requirement | Authority / verification hook |
|---|---|---|
| Managed admission | A managed child requires an eligible direct parent/child relation, a sealed bounded brief, declared context/cwd/tools/write targets, applicable approval references and fail-closed admission. | D-APP-68 disposition 4; SCA-APP-010 current contract; `frontend/src/__tests__/lib/managed-delegation.test.ts` (legacy evidence). |
| Current role relation | HELP_HUMAN may coordinate managers or dispatch bounded Type 2 work directly; HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an allowed ephemeral Type 2 instance; Type 2 does not delegate. | Current Root `AGENTS.md` Roles and App `AGENTS.md` Active Roles; role-basis evidence must identify origin and hash. |
| Delegation class | Chirality-managed execution and delegated-harness-native descent retain their distinct admission/evidence semantics; native descent alone assigns no Chirality role or approval. | D-GOV-35; SCA-APP-010; `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative). |
| Authority ceiling | Role instructions, the bounded brief and actual host enforcement jointly limit execution. A child cannot acquire authority from a UI label, model choice, parent narrative or a compatibility module. | Root/App `AGENTS.md`; D-GOV-43/D-APP-127; named managed/native verification must state enforcement limits. |
| Record handoff | Preserve actual parentage, supplied basis, scope, admission/approval evidence and return/artifact linkage for DEL-08-05. | DEL-08-05 CLM-037; `frontend/src/__tests__/lib/managed-delegation.test.ts` and Runtime native-event evidence. |

The former `evaluateSubagentGovernance` function and App-harness `delegate_agent` implementation are retained compatibility evidence. Neither is asserted to be the live Codex admission path. Missing live managed admission, scope enforcement and record integration remain work; this repair does not close them or accept D-GOV-42's exact bytes.''')
add(4,'CLM-005','Construction','''##### Construction

Required construction is a verifiable admission boundary and a class-aware handoff, not a named function call. It must preserve eligible parent/child relations, sealed context, required approval references, declared scope, restricted execution, managed sibling-overlap denial, cancellation/cleanup and the DEL-08-05 record interface. The record-less SDK `Agent` bridge remains retired; native Codex descendants are a distinct permitted class, not a revival of that bridge.

| Evidence surface | Use and limit |
|---|---|
| `frontend/src/__tests__/lib/managed-delegation.test.ts` | Managed-admission, hierarchy, context, scope and coordination compatibility evidence. |
| `frontend/src/__tests__/lib/sdk-options-builder.test.ts`; `frontend/src/__tests__/lib/permission-overlay.test.ts` | Evidence that the retired SDK Agent bridge is not exposed or used as a fallback. |
| `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative) | Native child identity and activity evidence; it does not prove managed sealed-brief admission. |
| DEL-08-05 class-aware record verification | Required return/artifact linkage; completeness must be checked against the actual delegation class. |

The legacy implementation lives under `frontend/src/lib/harness/`; its tests do not qualify the live Codex path.''')
add(4,'CLM-009','Scope','''##### Scope

DEL-08-04 owns the App's managed-delegation admission and project-authority interface: bounded parent-relative eligibility, sealed context, applicable approvals, context/cwd/tool/write limits, sibling-overlap denial, cancellation/cleanup and fail-closed outcomes. It consumes delegated-harness-native descent as a distinct Root-owned class under the controlling SCA-APP-010 contract. Native descent alone is neither managed admission evidence nor a Chirality role assignment.

The live App uses the Codex-hosted boundary under D-GOV-43/D-APP-127. The earlier App-harness function names and SDK bridge are compatibility/history evidence; the retired record-less SDK Agent bridge is not a permitted fallback. Preserve truthful `instruction-asserted` and `role not mechanically enforced` calibration where host evidence cannot prove a role constraint.

Verification hooks are the managed-delegation and retired-bridge tests in CLM-005, paired with class-specific live-path evidence. Any missing managed admission, approval, restriction or record guarantee stays open; a native-child event is insufficient to close it.

Excluded: general adapter implementation, DEL-08-05's full parent-child record/artifact persistence, dependency-register authoring and any change to Root native-delegation semantics. This carrier application does not grant lifecycle, release or D-GOV-42 exact-byte acceptance.''')
add(4,'CLM-013','Verification','''##### Verification

Verification must identify the actual delegation class, selected role/instruction basis, source revision, exercised path and result. Preserve the managed R01–R11 obligations; legacy tests are evidence of the compatibility implementation, not proof of live Codex enforcement.

| Obligation | Named evidence and required limit |
|---|---|
| R01–R05: pre-execution admission, sealed context, required approvals, allowlist/generalist policy and direct-parent eligibility | `frontend/src/__tests__/lib/managed-delegation.test.ts`. Record the current Root/App role basis; current HELP_HUMAN authority includes bounded direct Type 2 dispatch. Older Agent 0-to-Type 2 denial cases describe their historical policy, not the current role ceiling. |
| R06: retired SDK bridge cannot execute as a fallback | `frontend/src/__tests__/lib/sdk-options-builder.test.ts`; `frontend/src/__tests__/lib/permission-overlay.test.ts`. Native Codex descent is evaluated separately under D-GOV-35. |
| R07–R08: explicit scope, restricted execution, overlap denial, launch/policy failure, cancellation and cleanup | Managed-delegation fixtures plus actual live-path negative and allowed-path records are required. R3's missing launch-error/hook-failure and live-path coverage findings remain open. |
| R09–R10: truthful authority boundary and unknown values | Managed-admission negative fixtures must show no guessed allow decision; native evidence must retain stock Codex events and distinguish observed capability from granted authority. |
| R11: DEL-08-05 handoff | Class-aware record/replay evidence must preserve actual lineage, supplied basis and accepted artifact linkage. `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative) checks native identity/activity only, not full managed-record closure. |

Keep missing metadata, missing approval, unsealed context, ineligible child, non-allowlisted candidate, broad capability request, launch failure, audit-safe denial and allowed bounded execution as distinct checks. Do not infer mechanical sandbox/role enforcement from instructions or passing legacy fixtures.''')
add(5,'CLM-014','Verification','''##### Verification

Verification is class-specific and source-bound. A child activity notification, a written launch brief, managed admission and a persisted child return are different facts. Each verification run must identify the source revision, actual managed/native class, named claim/requirement and observed result.

| Requirement IDs | Named verification hook and acceptance limit |
|---|---|
| REQ-001–003 | `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` exercises the retained ChildRunRecord contract. The CLM-006 / REQ-001–002 schema authority conflict remains open; this test does not select a governing schema. |
| REQ-004–006 | Event writer/replay evidence must preserve actual lineage, event ordering, unique IDs and current/terminal status. `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative) verifies native identity and unmodified activity; it must not fabricate legacy `subagent.*` completion from a parent or tool-call completion. |
| REQ-007–008 | `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` verifies the retained 16 KiB inline / 512 KiB child-artifact policy and metadata. Those decision-bound limits are preserved; legacy tests do not demonstrate missing live child-output persistence. |
| REQ-009 | Redaction evidence must demonstrate secrets are absent before applicable persistence, not merely hidden on replay. `frontend/src/__tests__/lib/session-events.test.ts` and legacy mapper/artifact fixtures do not close the live native-child persistence finding. |
| REQ-010–011 | Replay/source review and `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts` must distinguish provider metadata from project authority and avoid reactivating retired pipeline scope. |
| REQ-012 | Preserve D-APP-40's denied-before-allocation / denied-after-allocation distinction. A schema fixture or lack of a native record cannot substitute for both applicable denial-path fixtures. |
| REQ-013 and CLM-037 | `frontend/src/__tests__/lib/managed-delegation.test.ts` supplies retained managed lineage/coordination evidence; native-event evidence covers observed native descent. Complete class-specific reconstruction must also establish supplied instructions/brief, scope, approvals, actual model, return, artifacts and enforcement limits where required. |

Record missing or unverified live controls as residual work. Do not infer that an off-code event never occurred from absence of a result artifact.''')
add(5,'CLM-032','Child-run Example Evidence','''###### Child-run Example Evidence

A child-run example must identify its actual delegation class and the schema/version it illustrates. Use the class-specific fixtures in `frontend/src/__tests__/lib/agent-runtime-contract.test.ts` for retained managed records and `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative) for native child activity. Record the tested source revision with the example's verification result.

The former inline JSON was an implementation-shape snapshot, not an additional schema authority. Its bytes are preserved in this run's R5/PKG08 before-block evidence and Git history. Removing that snapshot does not resolve the CLM-006 / REQ-001–002 schema conflict or retire the separately ruled artifact policy.

Examples and run records must not invent parentage, persona, model, approval, timestamps, completion, output paths or enforcement. A completed parent tool call does not establish a completed child. Required project records retain actual source-qualified instruction/brief identity, scope, class, direct parent and return/artifact evidence under CLM-037; absent evidence remains explicitly unknown.''')
# R06 was a single mechanism-exclusive row inside a broader block. Preserve all
# other R01-R11 text, while correcting current role eligibility and class scope.
for n in range(1,6):
    path=next((ROOT/'projects/chirality-app-dev/execution').glob(f'PKG-08*/1_Working/DEL-08-{n:02}*/ScopeOfWork.md'))
    baseline=(OUT/'before'/f'DEL-08-{n:02}.ScopeOfWork.md').read_text()
    t=baseline
    for (d,c),replacement in replacements.items():
        if d!=n:continue
        pat=rf'^### {c} — .*?\n(?:(?!^### CLM-|^## ).)*'
        t,count=re.subn(pat,lambda m:replacement,t,count=1,flags=re.M|re.S)
        assert count==1,(d,c)
    if n==4:
        old='A proposed child MUST be denied when its type is ineligible relative to the direct parent: Agent 0 admits only named Agent 1; Agent 1 admits only allowed Agent 2; Agent 2 cannot delegate.'
        new='A proposed managed child MUST be denied when ineligible under the supplied current role basis. HELP_HUMAN may coordinate managers or dispatch bounded Type 2 work directly; HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an allowed ephemeral Type 2 instance; Type 2 cannot delegate. Preserve the actual scope and enforcement limits in verification evidence.'
        assert old in t;t=t.replace(old,new)
        old='Managed child sessions invoked through `delegate_agent` MUST be the sole executable app-harness delegation path; the record-less SDK `Agent` bridge MUST remain disabled and not model-visible.'
        new='Chirality-managed child execution MUST satisfy managed admission; delegated-harness-native descent is a distinct class under D-GOV-35 and the controlling SCA-APP-010 contract. The record-less SDK `Agent` bridge MUST remain disabled and not model-visible. Neither native descent nor a compatibility implementation grants managed admission or a Chirality role.'
        assert old in t;t=t.replace(old,new)
        # Sources for the changed eligibility row are explicit, not code-derived.
        lines=t.splitlines(True)
        for i,l in enumerate(lines):
            if l.startswith('> | DEL-08-04-R05 |'):lines[i]=l.replace('| root `AGENTS.md`; D-APP-68 disposition 4 |','| Current Root `AGENTS.md` Roles; App `AGENTS.md` Active Roles; bounded R5 Agent 0 application |')
            if l.startswith('> | DEL-08-04-R06 |'):lines[i]=l.replace('| D-GOV-14 item 7; D-APP-68 disposition 4 |','| D-GOV-35; D-GOV-43/D-APP-127; SCA-APP-010; D-GOV-14 item 7 retirement boundary |')
        t=''.join(lines)
    assert t!=baseline,n
    assert path.read_text() in (baseline,t), f"Unexpected target drift: {path}"
    path.write_text(t)
    (OUT/'after'/f'DEL-08-{n:02}.ScopeOfWork.md').write_text(t)
print(f'Applied {len(replacements)+1} block repairs across five deliverables.')
