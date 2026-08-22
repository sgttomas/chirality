# Return — rejected interrupted attempt

Verdict: `REJECTED_PRECONDITION`

The manager interrupted this child before a terminal return because the App
project instruction requiring APP-HOLD-1 preflight before dispatch had not yet
been executed. No child output is accepted or used in fan-in. The child wrote
no source, deliverable, or evidence file before interruption.

The manager subsequently ran the required dispatch preflight and received
`ALLOW`; a fresh child attempt is required and separately briefed.
