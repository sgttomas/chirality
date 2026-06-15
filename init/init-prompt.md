Read `/Users/ryan/ai-env/projects/chirality/agents/<insert agent instruction here>`.

Act in the `<insert agent name here>` persona for `/Users/ryan/ai-env/projects/chirality/domains/chirality`.

Then read `/Users/ryan/ai-env/projects/chirality/domains/_Coordination/NEXT_INSTANCE_PROMPT.md` and follow the instructions.

Stop when any further progress requires a human ruling. When the work is complete, validated, and the project closeout rules allow it, autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review. `CHANGE` should commit and push the validated tranche as the ordinary terminal action when git state allows closeout; do not require a per-run `APPROVE:` token for scoped closeout commit/push.


