# Amendment 02 — bounded stages through workflow selection and briefs

HELP_HUMAN clarified the shared design: do not implement `execution.stages` role-eligibility overrides. This supersedes Amendment 01's stage-interface paragraph. A manager workflow remains compatible with WORKING_ITEMS; TASK receives a separately bounded child workflow or a brief. Explicitly selected resources support staged loading without changing role eligibility. WORKING_ITEMS relayed this amendment to runtime_tools, project_workflows, and document_workflows before fan-in.

The two retired deterministic audit aliases resolve to TASK plus a tool path, with a bounded brief, rather than selecting evaluation-protocol as a TASK workflow.
