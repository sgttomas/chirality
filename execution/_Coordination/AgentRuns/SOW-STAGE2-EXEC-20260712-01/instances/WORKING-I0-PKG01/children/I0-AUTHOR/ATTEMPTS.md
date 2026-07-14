# Attempts

Attempt 1 is the initial governed execution. Safe mechanical defects, if any, will be retained here with all affected bindings rebuilt.

## Mechanical remediation 1 — telemetry output anchoring

The first telemetry invocation supplied a run-relative path where the recorder expected a path relative to `--run-root`, creating a doubled derivative path beneath the run root. Containment detected it before freeze. The misplaced files were removed, telemetry was regenerated directly in the authorized child folder, and the runtime summary, containment check, and manifest were rebuilt. No candidate, live project, parent, Git, lifecycle, or semantic bytes were affected.
