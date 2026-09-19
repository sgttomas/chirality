# Owner direction — App loop amendment

Recorded 2026-09-19 from this session. Quotations below are owner words; SHA-256
is over each quoted text in UTF-8 without a trailing newline. Earlier messages
are retained without inventing individual message timestamps.

## app_state

> App has already been published as `v3.0.0` and I'm not doing further development work until a reconciliation phase.  I will take care of the steering instructions for that.  Does the App loop instructions offer anything you want to adopt in Piping?  Why or why not.

SHA-256: `238b8636dc4fc880c9fe425de095a0c240998383c9eea2ad75dd11da0abbeef6`

## phase_steering

> I dunno, I don't see that working well in the long run.  Until I figure out a stable pattern and put in the appropriate infrastructure, I think I need to just steer the model through phase transitions.

SHA-256: `82c72f9d56bf376f79906000a4a359c87140520abab08786a3b0ddc9e261b7d5`

## phase_dag_and_session_graph

> I agree.  I see the overall project DAG for App and Piping remaining relatively stable, but being rebuilt for each of the three phases.  However, it is not specific enough for each work session.  That's where the work graph comes into play.  It replaces what the work plan was previously doing.  Does that seem consistent with what you're describing to me?

SHA-256: `009ee2954961867bfeb6f1f2e2eb4a97bd637469e6b990724a0d07b51b07f527`

## separation

> you should not put specific handoff details into the LOOP instructions.  Those should be managed how the original LOOP architecture handled it: recurrent, stable instructions, plus specific state pointers to orient the agent's discover, plus steering instructions for specific direction priorities.

SHA-256: `9963085b01874cf5a37d0e12776ed2006394fc94d8af99efe65386f959f9fdb8`

## implementation

> Now make the recommended changes to the App project files, as you have indicated.

SHA-256: `c978da85bff90540c7eb5084fc5bd4f44c5b1f9038e9219fb53adb023581e26c`

## Agent application of the accepted recommendation

This is instruction maintenance only. Update project development AGENTS, the
recurrent LOOP_INIT and discovery pointer; archive their old bytes. Keep the
init launcher and packaged product instructions unchanged. App publication and
the development pause are owner-reported state, not a new release verification.
The owner will supply reconciliation steering. No product work, DAG rebuild,
deliverable reconciliation, hold lifting or release act is initiated here.

The session graph replaces the session workplan; the phase DAG remains its
traceable project basis. Uncertain deliverable mappings stay provisional.
Routine engineering and Git decisions use existing authority. Authoring and
integration are Agent 0 work; one direct fresh TASK reviewer uses gpt-6-astra /
high. No Type 1 layer or implementation delegation is needed for this bounded
amendment. The child has no write scope and may not delegate. This is a
same-model independent context, not model diversity.
