# Runtime Efficiency Amendment 001

Status: `ACTIVE — HUMAN-DIRECTED WORKFLOW HARDENING`
Date: 2026-07-13

## Direction and scope

After reviewing the App Stage-2 runtime analysis and the completed PKG-01
batch experiment, the human directed implementation of the remaining three
pre-resumption changes: make server-dependent project checks self-contained;
narrow but retain RECONCILIATION; and add lightweight runtime/remediation
telemetry. The human also confirmed that PKG-00 exclusion, the PKG-01 method-2
experiment, its sufficiency assessment, and deterministic portable closeout
were already complete and are not repeated here.

## Operating amendment

1. Registered checks may own one bounded loopback service through automatic
   port allocation, readiness, check execution, and guaranteed shutdown.
2. Remaining Piping representation-migration package work records run-local
   start/finish, attempts, checks, retries, remediations, failure categories,
   reason codes, and native context telemetry when available. Missing native
   token/context data is an explicit limitation, never an inferred value.
3. The fresh package verifier continues to review every member. The separate
   RECONCILIATION pass independently covers 100% of manifests, paths,
   aggregate populations/totals, replacement/rollback rows, containment, and
   apply/target/rollback simulations. Fresh member reproduction covers every
   exception plus at least the numerically final clean member per package.
4. Any aggregate or sample defect expands RECONCILIATION to full reproduction
   of the affected package. The initial finding and repair chain remain
   durable evidence.

## Non-effects

This amendment does not integrate a candidate, change a deliverable or
lifecycle state, authorize H1/H2, retire a legacy surface, alter PKG-00, or
resume Piping package execution. It changes workflow/runtime mechanics only.
