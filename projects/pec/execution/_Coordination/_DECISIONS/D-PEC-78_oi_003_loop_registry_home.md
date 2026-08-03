# D-PEC-78 — OI-003 loop-registry home and shape

**Status:** RULED O-A / PRODUCT DECISION SETTLED / SCOPE_CHANGE INTAKE REQUIRED

**DecisionID:** D-PEC-78

**Date presented:** 2026-08-02

**Owner:** Ryan Tufts

**Owning loop:** PEC

**Presentation basis:** `97678a841ef58345c73d3470ed8de57c9b1405d2`

**Decision packet:**
`../D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/PACKET.md`

**Task Management route:** `TM-PEC-010`

## Question

What is the long-term governed home and typed shape of the registry naming the
loops PEC serves, while preserving each loop's own authority and PEC's
graceful absence?

## Options

### O-A — PEC-local long-term service registry (recommended)

Confirm the existing PEC-owned JSON/schema paths and typed core port as the
long-term home and shape. PEC owns only its configured service set; every
listed loop remains authoritative for its own entrypoint and truth. Later row
changes remain owner-gated PEC configuration changes. No current source edit
is required; SOW-077/OI-003 propagation routes separately through
SCOPE_CHANGE.

### O-B — shared declaration contract plus loop-owned contributions

Select a two-layer direction: Root owns a prospective language-neutral shared
declaration schema; each loop may separately adopt its own declaration; PEC
retains a local list selecting which declarations it consumes. This requires
Root and loop-local rulings, compatibility/migration instruments, SCOPE_CHANGE,
and a later exact-path D-PEC adapter migration. This packet writes none of
those surfaces.

### O-C — retain replaceable default and defer

Keep the one-entry PEC-local default explicitly temporary. Retain SOW-077 and
OI-003 open, with a sharper trigger before the first non-PEC row proposal or
before a P2 consumer is authorized to rely on a stable long-term registry
home/shape, whichever comes first.

### O-D — amend

State a different owner, shape, path, contribution model, compatibility,
migration, absence, consumer, SCOPE_CHANGE, or Task Management disposition.

## Recommendation and boundary

O-A is recommended because “which loops PEC serves” is PEC-owned consumer
configuration; the existing typed core port already preserves adapter and
application replaceability without creating a cross-loop publication duty.
O-B is the stronger federation shape and is presented fully, but costs a
shared contract owner, five independent adoption decisions, and version-skew
handling.

No option is selected. The ruling itself changes no source or accepted
decomposition byte, activates no consumer, imposes no cross-loop duty, and
authorizes no lifecycle, artifact, release, or reliance act.

## Owner ruling

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> D-PEC-78: O-A

This confirms the existing PEC-owned JSON/schema paths and typed core port as
the long-term home and shape of PEC's service registry. PEC owns only which
loop locators it chooses to serve; each named loop remains authoritative for
its own entrypoint and governed truth. Schema version 1 remains strict and
versioned as stated in the packet. Listing or removing a loop creates no duty,
lifecycle effect, cadence, conformance obligation, or authority over that
loop, and no governed act may depend on PEC or the registry.

The ruling settles the upstream PRD §16.3 / OI-003 product decision. It changes
no source or accepted decomposition byte. SOW-077/OI-003 propagation must run
separately through SCOPE_CHANGE before downstream contracts rely on the issue
as closed. No current DEL-01-06 source edit is required. The exact ruling
supports `TM-PEC-010` closure as `RESOLVED_BY_DECISION`; Task Management owns
that register act and mechanical archive.
