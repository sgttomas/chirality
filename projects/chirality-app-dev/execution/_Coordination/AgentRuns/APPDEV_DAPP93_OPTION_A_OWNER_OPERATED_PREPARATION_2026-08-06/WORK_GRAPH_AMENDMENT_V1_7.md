# Work-graph amendment v1.7 — rejected-freeze recovery

Parent: `HELP_HUMAN`

Integration owner: `WORKING_ITEMS`

Status: `ADOPTED METHOD RECOVERY — R4 SUCCESSOR REQUIRED`

HELP_HUMAN rejected `MANAGER_FREEZE_R4.md` SHA-256
`b741231bd7a5c7d589f5217c7f01b2a8a56843928b7bf8cbe3b6cb57c8a72bce`.
That object remains immutable rejected history and must not be used for
verifier dispatch or presentation.

The rejection found six in-scope defects: a step-31/transcript ordering cycle;
a form/manifest/completeness self-reference cycle; non-literal C1146 exit
markers; bundled unenumerated operations in C1146/C1149-C1151; missing
credential-screen evidence for C1148 sources; and the need to rerun all
accepted A01-A44/B01-B40 rows including failure paths.

Recovery remains inside the owner's exact R4 repair authority. It may allocate
additional contiguous command IDs after C1151, update only the previously
authorized affected prepared/control surfaces, and produce a successor
backcheck/freeze. It must:

- distinguish executable steps 1-30 from step 31's terminal
  `READY_TO_HANDOFF` disposition;
- move complete failure-preserving C1105-C1108 output/exit capture into those
  exact command rows;
- enumerate each capture, screen, copy, form, manifest, and completeness
  operation with literal shell or UI bytes and no hidden script;
- keep terminal manifest/completeness siblings outside the earlier finalized
  form to avoid self-reference;
- preserve C196/C197 exact bytes and the ordinary C1145→C1144→C1130 order;
- rerun both exhaustive matrices before a successor freeze.

No runtime, debugger, package, helper/GUI, signal, credential, product,
release, reliance, Git, Task Management, foreign-loop, or verifier action is
authorized or taken by this amendment.
