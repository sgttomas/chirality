# PEC D-PEC-77 / D-PEC-78 orchestration plan

**RunID:** `PEC-DPEC77-78-20260802`

**Version:** 1

**SelectionAuthority:** HUMAN

**DescriptivePosture:** MIXED

## Accepted basis

- `origin/main@7249281e1f84ba5abee3c31c2fea3736b22000d3`
- owner rulings: `D-PEC-77: O-A; CON-002: G-A` and `D-PEC-78: O-A`
- D-PEC-77 presentation packet SHA-256
  `f848d55557d4b59d4c425e3924b850d634011a4a7db6c6fbd2eee9fc46cc5c31`
- D-PEC-78 presentation packet SHA-256
  `426dba045d63136937eec25af6e4842188ac402486f400391f1f30e1f33e5d17`

## Work graph

| Node | Manager | Scope | Dependencies | Write owner | Expected return | Human gate |
|---|---|---|---|---|---|---|
| N0 | HELP_HUMAN | record both rulings and freeze the graph | none | PEC decision/register/receipt integration owner | ruled decision records | none |
| N1 | WORKING_ITEMS | PKG-01 / DEL-01-05 phase-1 contract currency only | N0 | exact DEL-01-05 `ScopeOfWork.md` | repaired hash, unchanged AC-001..011, validation and containment | REVIEW type, review-from-INITIALIZED, findings, Gate 5, exact-hash SOW fitness |
| N2 | TASK_MANAGEMENT | PEC register effect for TM-PEC-010; verify TM-PEC-009 unchanged | N0 | PEC Task Management register home only | federation result and closure-ready proposal or lawful row return | explicit Task Management disposition if D-PEC-78 selection is not sufficient |
| N3 | SCOPE_CHANGE | SOFTWARE SOW-077/OI-003 propagation intake | N0 | read-only except managed instance return | parsed action, next SCA ID, baseline, Gate-1 decision interface | SCOPE_CHANGE Gate 1 then Gates 2–5 |
| N4 | HELP_HUMAN | validate manager fan-in and present remaining gates | N1,N2,N3 | shared coordination integration | cross-manager handoff | owner decisions only |

N1, N2, and N3 may run concurrently because their authorized writes are
disjoint. HELP_HUMAN alone updates the D-PEC decision register, packet
manifests, shared loop receipt, and final handoff. Source production under
D-PEC-77 phase 2 remains dormant.

## Failure isolation

- N1 failure holds only DEL-01-05 source production and the later DEL-01-06
  rerun.
- N2 uncertainty leaves TM-PEC-010 unchanged and does not affect the product
  decision or SCOPE_CHANGE intake.
- N3 uncertainty leaves accepted decomposition revision 1.3 unchanged and
  does not affect the PEC-local registry decision.

## Fan-in criteria

Every manager return must cite current files and hashes, remain inside its
write fence, disclose blockers and reruns, and avoid claiming acceptance or
closure outside an explicit owner act. No source, lifecycle, release, or
professional-reliance act is part of this graph.
