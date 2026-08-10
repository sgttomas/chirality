# N1 pre-dispatch allowlist and command validation

Verdict: `PASS`

- Frozen graph SHA-256: `4d5993c0ae4a3f5545de7747e986de205c45a57904a91a15575cea10d8499806`
- Exact read allowlist: 48 unique existing files, 7,367 bytes, SHA-256
  `52ac804af92d0e946099e70a8e9bfd269708a50a3d067d0618ba3b11dbbf8277`
- Command-forms file: 908 bytes, SHA-256
  `bcaddc80287d3a5724fbf463dd71e2acf62f29f3055b23cd83cc3e3713b67be4`
- Sealed brief SHA-256:
  `0a53473c4a881e693dceb953211c8440ad97b270d3e97b6ae8fb7b7921c0fdf9`
- Four-root baseline SHA-256:
  `fd7e681e74e996e72e9e6d5242c94f6722ed1df168b489924ee7362712352dcd`

Deterministic checks found zero missing paths, zero duplicate allowlist rows,
zero paths under any of the three wholly forbidden historical roots, and
exactly six allowlisted paths under the third root. Those six are the named
Stage 1 through Stage 6 salvage files and no others.

Every proposed search form requires explicit file arguments from the
allowlist. The forms contain no repository/project/AgentRuns directory search,
no unresolved glob, no implicit current-directory search, no exclusion
pattern, and no path-capable command substitution. The only permitted
directory traversal is a read of the new run's own taint-clearance output for
supervisory durable-progress measurement. Output writes are exactly the six
brief-listed paths.

The first checkpoint is scheduled for minute 4, matching the declared Stage 1
expectation. Subsequent checkpoint interval is 8 minutes. Native context
occupancy is not exposed by the child-session runtime and must be recorded as
unavailable at every event.
