# CHANGE-H1-G Attempts and Mechanical Normalization

All attempts were retained. None wrote a project path or changed the prepared
candidate, prior evidence, status, lifecycle, integration state, or H2 state.

## Exact terminal-blank-line normalization

The initial scoped hygiene check found one extra terminal blank line in each
of two newly created evidence files. Each correction removed exactly one final
LF byte before the evidence manifest was frozen:

| Path | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `amendments/H1-APPROVAL-001.md` | `03b3278127ec1a22f5c6a10477b6194f053ad5b3f286ee4e6124ddd24c72b54d` | `aa60ef073ad22b3d4c1887319bb86d10d3ab67928c7bd622018db686b811942c` |
| `instances/CHANGE-H1-G/LAUNCH_BRIEF.md` | `e7a367b235f0f7f3867f31c65f0f850b699b41d66c474c34ed1f9ff59fa41954` | `d1b8e6f455ca723930cd674555af27f0d42bfaae7e4b3e72b4a07be365350482` |

The normalized files were rehashed and rebound in the final self-excluding
instance manifest. This was a mechanical evidence-only repair.
