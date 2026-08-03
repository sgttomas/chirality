# Causal and alternative matrix

| Arm | Result | Interpretation |
|---|---|---|
| Real helper-local Frameworks copied with default `cpSync` symlink behavior | FAIL: nested children lost ICU; internal links became absolute | Non-relocatable link rewriting was causal for the ICU failures. |
| Same package with `verbatimSymlinks: true` and absolute-link rejection | PASS: stable nested GPU/network children, no ICU error | Relative framework links are required and sufficient for in-place child startup. |
| Helper-only `single-process` | PASS startup, FAIL preservation: SIGTERM path unreliable | Rejected because it changed graceful-stop behavior. |
| Distinct `CFBundleIdentifier`/`LSUIElement`, inherited Electron product/executable name | PASS startup/CLI/GUI coexistence; FAIL first graceful signal after coexistence | Working packaging candidate, blocked on recovery preservation. |
| Renamed copied Electron main plus renamed or conventional copied child | FAIL pre-JavaScript `Unable to find helper app` | This copied-main technique could not satisfy Electron 43.2 native child lookup when the main executable/product name changed. |
| Helper-only SIGUSR2 after GUI coexistence | FAIL: signal suppressed, socket retained | A simple signal-translating wrapper is not a demonstrated remedy. |
| Separately built full Electron helper target with its own product configuration | **UNTRIED LAWFUL ALTERNATIVE** | Not evaluated in this run. The failed copied-main rename arms do not prove D-APP-88 impossible; a separately built helper target may satisfy native lookup and warrants a separately authorized design/implementation tranche. |
| Non-Electron native/Node supervisor with explicit child lifecycle | **UNTRIED LAWFUL ALTERNATIVE** | Not authorized or evaluated; may change safeStorage/runtime integration and needs owner-governed scope. |
