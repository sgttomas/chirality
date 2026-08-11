# Required content — CAPTURE_TRACE_EVIDENCE.zsh

- Zsh script with `set -eu`; restricted `PATH=/usr/bin:/bin`.
- Require exactly two operands: an existing evidence directory and an existing transcript file inside that directory.
- Refuse broad or escaping paths; do not create/delete/move files.
- Hash the transcript with `/usr/bin/shasum -a 256` and append one descriptive row to a recording file inside the evidence directory.
- No network, process observation, attach, signal, kill, launch, build, install, or product/runtime/system mutation.
- Use descriptive fresh labels only.
