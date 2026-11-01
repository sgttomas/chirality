# Existing tool support and current limits

Maturity: setup-use assessment, not full toolkit fulfillment. The adjacent
ScopeOfWork defines the utility claims. Source basis:
`fd847ac9ac68250b2f35d2e9c0087c16e86b510a`, plus this setup's local declarations.

## Current setup path

PR #1779 supplied the explicit `--current` scaffolding and checks, separating
structural preparation from real ScopeOfWork authoring. The accepted decomposition
§6.1 identifies its checked head, equal-tree merge and reported verification.
That evidence remains available for unchanged preservation/collision/legacy
compatibility behavior; no new implementation is needed merely to populate this
deliverable.

Agent 0 used that route to prepare all seven numeric localities. The Type 2
authors then exercised the authored-locality and contract checks on actual
ScopeOfWork files. These uses establish the selected setup behavior, not every
failure case, query capability or product criterion. No phase directories,
lifecycle files or blank contracts were required.

Some author sessions resolved a Python without PyYAML; the documented `PYTHON`
override to an existing Python 3.13 environment with PyYAML enabled the locality
check. No installation or tool change was needed. Portable instructions should
declare the dependency and interpreter selection, not a machine-specific path.

## Query use and an instruction discrepancy

`tools/deliverables/cli.py` requires `--project`; its README agrees. The selected
`workflows/dependency-extract/resources/tools.md` still says the CLI has an App v4
default. The safe current invocation is explicit `--project .` from Root, as the
guide itself prescribes. This discrepancy did not block setup; it is a bounded
direct-usage correction for later maintenance, not evidence of a missing query
implementation. Its governing source has not been edited in this setup.

The queries read live declarations, including uncommitted files. They report
path/source observations and unknown suitability; they do not execute pointers,
evaluate conditions or accept work. Native cycles are allowed and require a
use-specific reading. A named query is not a requirement for a global DAG.

## Remaining examination

Use maintained caller contracts and fixtures before any utility change. Reuse
applicable prior evidence and exercise only changed or uncovered claims. Named
external compatibility (Q-04) and publication/update claims (Q-05) still need
their own source bindings. No file-only adapter, namespace repair or bespoke
service has been selected. The native needs distinguish actual metadata/caller
inputs from these conditional claims.
