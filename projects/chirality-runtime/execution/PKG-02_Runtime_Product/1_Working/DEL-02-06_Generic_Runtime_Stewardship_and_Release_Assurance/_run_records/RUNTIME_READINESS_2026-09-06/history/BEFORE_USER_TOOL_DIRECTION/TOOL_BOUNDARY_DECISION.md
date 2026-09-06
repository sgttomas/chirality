# Exact child tool-boundary decision — candidate v1

## Observed blocker

The current native descendant surface exposes exec_command and apply_patch orchestration, but no dedicated text-file read/write/hash tool. exec_command invokes a shell even when its payload only reads files. The accepted ScopeOfWork required-task table (lines 490–496 at hash c178211d4a6b43eee8773f664704d86db286d2a0e96cbe2bea7bfcca47a93b09) expressly says “no Bash or network” for every N0–N6 child. N0/N6 additionally allow only the two named Scope-of-Work tools. A versioned read amendment does not change those tool cells. Current execution is therefore blocked; no compliant executor has been demonstrated.

WORKING_ITEMS cannot solve this by giving its children its own shell permission, pretending an exec wrapper is a dedicated file tool, or running the whole graph as manager prose. Actual delegated children and fresh N5 verification remain required.

## Recommended exact owner ruling

The following is a proposed, single-run substantive exception to seven specified tool cells, not an approved read amendment or standing tool policy:

> For chirality-runtime::DEL-02-06, ScopeOfWork.md SHA256 c178211d4a6b43eee8773f664704d86db286d2a0e96cbe2bea7bfcca47a93b09, I authorize the Runtime-qualified DEL-02-06-RUNTIME-SPEC-001 specification activation in this readiness package. For that run only, I supersede the required-task table's N0–N6 “no Bash” restriction solely to permit exec_command as the shell transport for the bounded file and hash operations enumerated below. I permit apply_patch solely for each writing node's own declared output directory. N5 remains read-only and returns its findings to the manager. Network remains prohibited. This grants no product implementation, registered software check, profile adoption, client write, status promotion, semantic adoption, hold release or release act. All other accepted contract provisions remain effective. The explicit read amendment is accepted separately as part of this same bounded activation decision.

Permitted child operations under that exact exception:

1. Through exec_command, invoke python3 with inline source using only pathlib, hashlib, json and csv for reading exact declared files, inspecting their existence/type/size, hashing bytes, and parsing JSON/CSV. Before each read, resolve the path and require exact membership in the frozen permitted-input list; reject symlink escape or an undeclared path. No imports that provide subprocess, sockets, network, account access or dynamic module execution; no arbitrary project-module imports, evaluation, package management, test suites, daemons or account/credential reads.
2. Writing children may serialize plain text/JSON/CSV evidence through the same bounded standard-library operation, or use apply_patch to create/update only their assigned node output subtree. Resolve and check containment first; reject symlinks, traversal and any target outside that subtree. No shell file writes, shell substitutions, pipelines, redirections other than the literal Python input payload, directory-changing chains, Git commands or additional shell statements. apply_patch may not touch predecessor evidence or any production path. N5 gets neither write operation nor apply_patch.
3. N0/N6 alone may invoke the two already accepted tools, validate_scope_of_work.py and derive_review_checklist.py, with frozen exact arguments confined to declared accepted inputs and their own output subtree. This changes invocation transport, not the accepted checks. No additional deterministic/software checks are granted to children.

These restrictions are instruction-asserted and checked by manager review of tool-call transcripts and changed-path evidence, within the existing filesystem/network policy envelope. They are not a new mechanically restricted Python executor or per-child filesystem sandbox. If an owner requires mechanical per-operation enforcement, select the compliant-executor alternative instead. Any actual scope violation stops the node and holds dependants; preserve evidence and return the incident.

## Exact seven-cell replacement for this run only

The proposed ruling replaces the complete Allowed tools cell in each specified row with the following text for this run; all other cells are unchanged. “Bounded operations” refers exclusively to operations 1–3 above, whose exact accepted document hash must appear in each sealed brief.

| ScopeOfWork row | Proposed run-specific Allowed tools text |
|---|---|
| N0, line 490 | Bounded file read/write/hash via the accepted exec_command transport and output-only apply_patch; the two exact Python tools named in read item 6; only enumerated bounded operations; no network. |
| N1, line 491 | Bounded file read/write/hash via the accepted exec_command transport and output-only apply_patch; only enumerated bounded operations; no software checks or network. |
| N2, line 492 | Bounded file read/write/hash via the accepted exec_command transport and output-only apply_patch; only enumerated bounded operations; no software checks or network. |
| N3, line 493 | Bounded file read/write/hash via the accepted exec_command transport and output-only apply_patch; only enumerated bounded operations; no software checks or network. |
| N4, line 494 | Bounded file read/write/hash via the accepted exec_command transport and output-only apply_patch; only enumerated bounded operations; no software checks or network. |
| N5, line 495 | Bounded file read/hash via the accepted exec_command transport; read-only operations only, no writes or apply_patch; no software checks or network. |
| N6, line 496 | Bounded file read/write/hash via the accepted exec_command transport and output-only apply_patch; the two exact Python tools named in read item 6; only enumerated bounded operations; no network. |

This is reviewable proposed ruling text now, not a claim that preparation authority accepts it. The owner may rule this exact scoped exception and activation together. If instead the owner requires a permanent clean SOW replacement, first route that choice through the owning scoped contract-amendment workflow, validate/review its exact successor hash and obtain its acceptance; activation remains held until then. The current package proposes neither an unreviewed permanent rewrite nor an implicit waiver.

## Procedure and unchanged clauses

Record the actual owner ruling as a new Runtime-local decision with this exact accepted SOW hash, seven table cells and run identity before dispatch; bind its exact path/hash and published basis in the final activation. docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md §2 treats substantive reinterpretation as CONFLICT routed through SCOPE_CHANGE or a human ruling. The recommended route is the explicit human ruling above, limited to a method permission for this run; do not silently rewrite the accepted SOW or claim a format conversion. WORKING_ITEMS Phase 1 steps 3/5 and its accepted-activation invariant require surfacing and resolving the conflict before dispatch. Record the exception in all seven actual sealed briefs and the final work graph. No new REQ/AC/VER or decomposition scope is created.

REQ-027 specification-only scope, REQ-028 exact basis/authority, REQ-029 fixed run root, REQ-030 graph/nondelegation, REQ-052 and AC-016 profile-free candidate method, AC-010 exclusions, all nine holds and N5 freshness remain unchanged. The seven historical no-Bash table cells remain visible in immutable accepted history; the run consumes both that contract and the later exact ruling. A broader persistent method change or altered product requirement would instead require its own scoped amendment and accepted successor contract.

## Alternative

Use an actual executor exposing bounded read/write/hash tools that satisfies the current accepted table. Demonstrate it before dispatch, keep no-Bash intact and approve only the existing activation/read amendment. No such executor is currently identified. Deferring until one is available is lawful; inventing a tool or claiming the current shell is already compliant is not.
