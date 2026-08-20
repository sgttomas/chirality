# Frozen work graph v1

Status: `FROZEN BEFORE DISPATCH`

Selection authority: supervising HELP_HUMAN launch brief plus D-APP-100 exact B1 ruling.

Posture: serialized terminal fan-out/fan-in. This activation contains one product engineering node; independent review is its mandatory validation stage, not a second engineering node.

1. `A2-DAPP100-IMPLEMENT-01` — `TASK + software-bounded-implementation`; inspect, implement, test, and produce an implementer return. Owns only the product/test/proof targets declared in its sealed brief.
2. `A2-DAPP100-REVIEW-01` — fresh `TASK + software-code-review`; runs only after the manager freezes the integrated diff and evidence; read-only over 100% of the diff.
3. Manager fan-in — validate the child returns, remediate through a new bounded implementation attempt if review finds actionable defects, rerun fresh review until PASS, execute/accept the registered and host proof surfaces, and write minimum deliverable/run closeout evidence.

Edges: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. Any remediation creates `IMPLEMENT-02 -> REVIEW-02` before fan-in. No concurrent writes and no shared writable file.

Checks by surface:

- In-session: focused app/CLI/daemon agreement regression; full Vitest; frontend typecheck; production build; applicable Section 9/release-quality scripts; unsigned desktop pack; packaged dependency and instruction-root integrity; repository self-check; practitioner pytest; authority-corpus status; APP-HOLD integrity; receipt validator; whitespace; containment.
- Host-capability: packaged-under-isolation Electron/daemon execution and any unsigned pack command blocked only by sandbox process-spawn or Mach restrictions. Request escalation for the exact command; never infer PASS.
- CI: additional evidence only unless a locally unavailable binding is explicitly classified by the registered premerge contract. CI does not replace packaged-under-isolation host proof.

Fan-in gates:

1. The manifest-resolved instruction root wins in packaged daemon mode and agrees with app and CLI resolution.
2. Packaged resources are consulted only if no manifest root can resolve, and that fallback is explicit in durable daemon logging.
3. The agreement regression would fail on the prior packaged-daemon behavior.
4. A freshly packed unsigned app passes the under-isolation proof without relying on a repository cwd, global Node, or ambient `CHIRALITY_INSTRUCTION_ROOT` override.
5. Fresh read-only review returns PASS with no actionable finding.
6. All changed paths stay within activation authority; lifecycle, Approval SHA, unrelated Remaining items, provider/network behavior, and release fences remain unchanged.

Escalation points: any need for root `runtime/**` source edits, manifest semantics changes, dependency/lockfile changes, signing/notarization/distribution, provider/network expansion, or owner-machine deployment returns to the parent rather than expanding this node.
