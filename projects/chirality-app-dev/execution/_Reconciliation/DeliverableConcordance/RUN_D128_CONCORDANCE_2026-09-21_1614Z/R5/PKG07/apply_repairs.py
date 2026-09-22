"""Apply the bounded PKG07 R5 record repair; not a reusable workflow."""
from pathlib import Path
import re
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[7]
assert (ROOT/'AGENTS.md').is_file()
replacements={}
def add(d,c,title,body):
    replacements[(d,c)]=f'### {c} — {title}\n\n'+'\n'.join('> '+x if x else '>' for x in body.strip().splitlines())+'\n\n'
add(1,'CLM-005','Construction','''##### Construction

The deliverable must establish valid working roots, their separation from instruction resources, and the applicable protection of governed writes. Root validation must reject relative, missing, non-directory, unreadable, unwritable and instruction-root-contained candidates. Accepted roots must be consistently reused by downstream consumers; normalization must not silently broaden the project boundary.

| Obligation | Named verification hook and limit |
|---|---|
| Validate root input and instruction-root separation before use. | `frontend/src/__tests__/api/working-root/validate-route.test.ts` and `frontend/src/__tests__/lib/harness-instruction-root.test.ts`. Missing access-condition and downstream-reuse coverage remains open. |
| Preserve project containment, ordinary instruction-root protection, symlink policy and provenance requirements for governed writes. | `frontend/src/__tests__/lib/chirality-hooks.test.ts` exercise retained legacy helpers; they do not prove live Codex enforcement. |
| State the actual execution boundary. | D-GOV-43 item 4 and D-APP-127 require user-selected Codex sandbox/approval policy. Verification must record the chosen policy and actual allowed/denied paths, including failure cases. |

A user choosing Full access changes host enforcement, not the authority of a role or brief. Missing live protection, symlink rejection, fail-closed enforcement and protected domain-path evidence remain implementation/verification work. A sandbox label or a legacy test result cannot discharge those obligations. Code locations are evidence, not additional scope: root validation is represented by `frontend/src/app/api/working-root/validate/route.ts`, instruction-root resolution by `frontend/src/lib/harness/instruction-root.ts`, and retained hook policy by `frontend/src/lib/harness/chirality-hooks.ts`.''')
add(1,'CLM-013','Verification','''##### Verification

Verification records must bind the candidate, tested entry path, active instruction basis, Codex policy and actual result. No test of a retained helper proves its invocation on the live path.

| Requirement IDs | Required checks and named evidence |
|---|---|
| REQ-07-01-001, REQ-07-01-002 | Relative, missing, non-directory, unreadable, unwritable and valid root cases; `frontend/src/__tests__/api/working-root/validate-route.test.ts`. Uncovered cases remain open. |
| REQ-07-01-003, REQ-07-01-004, REQ-07-01-006 | Instruction-root overlap and ordinary write protection; `frontend/src/__tests__/lib/harness-instruction-root.test.ts`, the validate-route test above, and path-specific live negative evidence. |
| REQ-07-01-005, REQ-07-01-007 | Relative/absolute paths, traversal, normalized equivalents and symlink targets; `frontend/src/__tests__/lib/chirality-hooks.test.ts` are legacy evidence. Live-path coverage remains required. |
| REQ-07-01-008, REQ-07-01-009 | Applicable fail-closed and policy-denial behavior, distinguished from the user's D-GOV-43 policy choice. The legacy hook tests do not establish live enforcement; record the missing live guarantees explicitly. |
| REQ-07-01-010, REQ-07-01-011 | Review the complete acceptance matrix and check validation response consistency and downstream root reuse. The validate-route test is named evidence; it does not close the remaining reuse and failure-case gaps. |
| Source basis for all checks | Read `_REFERENCES.md` and record current source verification or the precise unresolved mismatch. D-APP-38's historical MATCH finding is not a current hash result; `execution/_Scripts/references_hash_tool.py` provides the named hash-check hook. |

Full access does not supply normative permission to change protected records. The surviving protection and domain obligations retain their own authority even when current host enforcement is insufficient. This verification contract does not waive them or claim a new test run.''')
add(1,'CLM-014','Documentation','''##### Documentation

The evidence package must identify the candidate, applicable decisions, root-validation and protection checks, and coverage of SOW-002 and SOW-027. Use the named tests in CLM-013 and preserve their actual result records and live/legacy reach. Root validation, instruction-root resolution and legacy hooks have the evidence locations named in CLM-005; their filenames need not become additional deliverable requirements.

Record the actual `_REFERENCES.md` source state using `execution/_Scripts/references_hash_tool.py`, rather than repeating a historical MATCH declaration. Record missing root cases, downstream normalized-root reuse, live write protection, fail-closed behavior and symlink fixtures as gaps until demonstrated. ResponsibleParty remains human-assigned. The held organisation-layer acceptance questions elsewhere in this deliverable are not settled by this documentation repair.''')
add(2,'CLM-005','Construction','''##### Construction

Scaffolding must turn the accepted decomposition into the prescribed execution-root, package and deliverable structure without inventing scope. It must create or validate `INIT.md` and `_Coordination/_COORDINATION.md`, preserve the accepted coordination vocabulary, place packages under `{PKG-ID}_{Sanitize(PackageName)}/`, and place deliverables under `1_Working/` with their required PREPARATION baseline. Undecided source content remains explicit; parser design and local function names are not scope decisions.

The operation must return validation/PREPARATION compatibility, issue and scaffold counts, created paths and actionable failure diagnostics including stage and target. Reruns must preserve existing directories, file contents and applicable metadata without duplication or corruption. Verification hook: `frontend/src/__tests__/lib/harness-scaffold.test.ts`, including the creation and idempotence fixtures, paired with a live App-to-Runtime scaffold invocation and result record.

D-GOV-43/D-APP-127 place the live service in the application-owned Runtime. The retained scaffold module's tests do not demonstrate that live operation: R3 records that the live scaffold route returns ENGINE_UNAVAILABLE/501 because no scaffold adapter is composed. The operation remains required; bounded implementation and live verification remain open. This lift neither retires scaffolding nor claims that a module test repairs the live gap.''')
add(3,'CLM-005','Construction','''##### Construction

The scanner must identify deliverables by the accepted ID/folder structure and `_STATUS.md`, report required metadata completeness, and expose the production-document representation selected by the applicable accepted basis. Preserve knowledge-bucket completeness and source/hash warnings; a file's presence alone must not turn an unaccepted representation into project authority. Legacy four-document detection remains compatibility evidence, and this lift does not settle held migration or organisation-layer decisions.

`MEMORY.md` remains the canonical optional memory file and `_MEMORY.md` is rejected under this project profile. Preserve `_SEMANTIC.md` baseline recognition and the optional status of `_SEMANTIC_LENSING.md`. The exact metadata, representation and containment obligations in the requirements remain in force.

Named verification hooks are `frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts` and `frontend/src/__tests__/api/project/deliverables-route.test.ts`. Their fixtures must demonstrate complete/incomplete metadata, representation validity and ambiguity, memory handling and additive findings. Test existence does not establish a new migration acceptance or close missing live containment evidence.''')
add(4,'CLM-005','Construction','''##### Construction

The status contract must read `_STATUS.md` as canonical lifecycle state, expose Current State, Last Updated and history, and reject transitions that lack the required actor authority or candidate-bound approval evidence. Apply the allowed transitions and explicit human-authorized reversal paths in SPEC §4.3; a generic forward-only rule must not erase those exceptions.

Named verification hooks are `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. They check parser and transition behavior through the status API. `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` is retained MCP compatibility evidence, not a live Codex tool qualification under D-GOV-43/D-APP-127.

Human gates remain human acts. A caller-supplied actor string and a correctly shaped SHA are not proof that a human approved the exact candidate. R3/P-07/P-14 identify this live enforcement gap; it remains a remedy and verification obligation even when the former transition UI is absent. No lifecycle change, approval refresh or acceptance follows from this text repair.''')
add(4,'CLM-014','Documentation','''##### Documentation

Maintain evidence for the canonical status parser, permitted and denied transitions, candidate-bound human approval, API responses, and applicable write protection. The parser and transition implementation evidence is `frontend/src/lib/lifecycle/status-parser.ts` and `frontend/src/lib/lifecycle/transition.ts`; named verification is `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`.

Request/response and actor-policy evidence must identify the accepted contract and exercised entry path. D-APP-56 R4-P19 supplies the recorded actor-alias mapping; copying current enum or payload fields is not a replacement for contract fixtures. Preserve unresolved schema-fixture and live permission/path-policy coverage. Retained MCP schema and `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` evidence applies to compatibility only.

A human gate requires actual human authority and the applicable approval evidence, not an agent-controlled actor label. Record the live authentication/candidate-binding limit and its remediation route. Read `_REFERENCES.md` for source state and obtain current verification or an authorized bypass before making source-dependent acceptance claims; historical hash declarations are not present verification.''')
add(5,'CLM-014','Verification','''##### Verification

Verification must identify the source revision and actual API, register or compatibility-tool path exercised. Preserve the full v3.1 requirement set; known fixtures are verification hooks rather than proof of untested behavior.

| Requirement IDs | Required checks and named verification hook |
|---|---|
| REQ-DEL-07-05-001 through -007 | Schema/version, valid and malformed headers, duplicate IDs, host identity, anchor and execution rows; `frontend/src/__tests__/lib/dependencies-register-contract.test.ts`. Missing or malformed-header coverage remains open. |
| REQ-DEL-07-05-008 through -012 | Retain retired rows and lifecycle fields, provenance, explicit unknowns and target resolution; the same register-contract test. Target-existence coverage remains open. |
| REQ-DEL-07-05-013 | GET/PUT contract, write failures and symlink handling; `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. |
| REQ-DEL-07-05-014, -015 | Applicable permission, path containment, instruction-root, symlink and provenance protection. `frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts` and `frontend/src/__tests__/lib/chirality-read-mcp.test.ts` are legacy tool evidence; they do not qualify live Codex enforcement. Dependency instruction-root and other missing live checks remain open. |
| REQ-DEL-07-05-016, -017 | Non-breaking extension columns and warning behavior for unknown options; register-contract and API tests above. Unknown-option coverage remains open. |
| REQ-DEL-07-05-018 | A candidate-bound scope-review record must confirm no retired graph generator, deliverable lock, staleness propagation or unified pipeline run-record scope is reintroduced; R3 found no such check. |

The evidence modules are `frontend/src/lib/dependencies/` and the dependency API route; their local names are not additional scope. D-GOV-43/D-APP-127 make Codex the live engine and leave sandbox choice to the user. That choice does not waive dependency integrity, human authority or the unresolved read-linter/live-protection gaps.''')
add(6,'CLM-006','Construction','''##### Construction

The deliverable must provide usable conventions for immutable snapshots, source verification and content-bound human approval, while preserving SOW-032/033/034 and the retired-scope boundary. Snapshot-producing workflows should use timestamped immutable folders; `_LATEST.md` may move only as the owning workflow permits, and accepted snapshots must not be overwritten. A hash bypass requires actual human approval and a durable record, using `HASH_VERIFICATION_BYPASS.jsonl` where applicable.

CHANGE/publication records must identify candidate content, the applicable authorization and action, and any required approval SHA. Recheck the candidate before execution; changed content cannot inherit approval of earlier bytes. Human lifecycle acceptance remains distinct from standing Git authorization. Deterministic tools/scripts should remain indexed and locally executable when present; registry membership is asserted only from verified ownership evidence.

Verification hooks: the candidate-bound convention review in CLM-019; `execution/_Scripts/references_hash_tool.py` and `execution/_Scripts/tests/test_references_hash_tool.py` for hash behavior. These hooks do not establish an App snapshot engine, authenticated human approval, lifecycle promotion or a new execution result.''')
# Targeted in-block edits preserve other established obligations.
for n in range(1,7):
    d=f'DEL-07-{n:02}'
    p=next((ROOT/'projects/chirality-app-dev/execution').glob(f'PKG-07*/1_Working/{d}*/ScopeOfWork.md'))
    before=p.read_text()
    saved=OUT/'before'/f'{d}.ScopeOfWork.md'
    if saved.exists():
        before=saved.read_text()
    else:saved.write_text(before)
    blocks={m[1]:m[0] for m in re.finditer(r'^### (CLM-\d{3})\b[^\n]*\n(?:(?!^### CLM-|^## ).)*',before,re.M|re.S)}
    if n==1:
        b=blocks['CLM-003'].replace('| Runtime enforcement surfaces | Path helpers, PreToolUse hooks, MCP tools, and Chirality hooks. | `docs/CONTRACT.md` K-PATH-2; `docs/CONTRACT.md` K-ROOT-2 |','| Runtime enforcement basis | User-selected Codex sandbox/approval policy governs actual host access under D-GOV-43/D-APP-127. Retained Chirality helpers and hooks are compatibility evidence; their presence does not prove live protection. The role/brief and protected-record obligations remain distinct. | D-GOV-43 item 4; D-APP-127; CLM-013 named verification hooks |')
        assert b!=blocks['CLM-003'];replacements[(n,'CLM-003')]=b
    if n==4:
        b=blocks['CLM-003'].replace('Transitions are forward-only and actor-authorized.','Transitions require authorized actors and follow the allowed forward and explicit human-authorized reversal paths in SPEC §4.3.').replace('`docs/SPEC.md` Section 13 |','`docs/SPEC.md` Section 17.2 |').replace('| MCP surface |','| Retained MCP compatibility surface |').replace('`mcp__chirality__status_read` reads `_STATUS.md`; `mcp__chirality__status_transition` applies authorized lifecycle transition with approval SHA where required.','`mcp__chirality__status_read` and `mcp__chirality__status_transition` are retained legacy interfaces. D-GOV-43/D-APP-127 do not make them live Codex tools.').replace('| MCP boundary | MCP is a transport, not a bypass; in-process Chirality MCP tools pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. |','| Transport boundary | A transport grants no lifecycle authority. Retained MCP policy is compatibility evidence; live API callers still require the applicable actor authority and candidate-bound approval. |')
        b=b.rstrip()+'\n>\n> Verification hooks: `frontend/src/__tests__/lib/lifecycle-status.test.ts` and `frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`. The live caller-supplied actor/SHA limit remains open under P-07/P-14; field validation does not authenticate a human act.\n\n'
        replacements[(n,'CLM-003')]=b
    if n==6:
        b=blocks['CLM-018'].replace('> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.','>    - Verify the source bytes relevant to the candidate using `execution/_Scripts/references_hash_tool.py`; record any mismatch or authorized bypass. D-APP-38 records a historical source state, not perpetual MATCH.').replace('>    - Confirm Datasheet attributes map to Specification requirements.\n>    - Confirm Specification verification rows have corresponding procedure steps.\n>    - Confirm Guidance source warnings match Datasheet and Specification warning language.\n>    - Leave unresolved values as `TBD` and list human rulings in Guidance.','>    - Confirm requirement, verification and production-method claims remain traceable across this ScopeOfWork and any retained legacy evidence.\n>    - Confirm source-state warnings agree with the candidate-bound verification result.\n>    - Leave unresolved values explicit and route reserved human decisions without inventing a ruling.\n>    - Record the CLM-019 convention review against the exact candidate and evidence used.')
        assert b!=blocks['CLM-018'];replacements[(n,'CLM-018')]=b
        b=blocks['CLM-019'].replace('| Source-state warning | REF-006 `docs/PRD.md` hash status: MATCH is visible anywhere PRD-derived requirements or examples are used. — reconciled under D-APP-38 |','| Source-state verification | Use `execution/_Scripts/references_hash_tool.py` to check the applicable reference bytes. Record the actual result or authorized bypass; a historical MATCH statement is not current evidence. |')
        b=b.rstrip()+'\n>\n> Retain this convention-review checklist with its candidate identity, checked evidence, reviewer and actual findings. Hash-tool tests are named in CLM-006; neither a format-valid approval token nor this documentary review proves a human acceptance act.\n\n'
        replacements[(n,'CLM-019')]=b
    after=before
    for (dn,c),new in replacements.items():
        if dn!=n:continue
        assert c in blocks and before.count(blocks[c])==1
        after=after.replace(blocks[c],new,1)
    assert after!=before,d
    p.write_text(after)
    (OUT/'after'/f'{d}.ScopeOfWork.md').write_text(after)
print('Applied',len(replacements),'blocks across six deliverables')
