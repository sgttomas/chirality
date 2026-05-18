# KTY Content Disposition Downstream Allowlist Plan

Status: Draft / follow-up after SCOPE_CHANGE remediation framework is accepted.

Purpose: define follow-up work to update KA-consuming agents so each derives a mandate-specific allowlist from the governed KTY content disposition state before reading KTY-local content.

This plan assumes the framework work has already introduced a root-local KTY content disposition artifact produced or referenced by SCOPE_CHANGE closure. This file intentionally scopes only downstream consumer alignment.

## Goal

Downstream agents should not scan KTY folders as factual authority by default. Each KA-consuming workflow should first locate the governed KTY content disposition state for the root, derive an allowlist appropriate to its mandate, and record that allowlist in its run evidence.

## Work Packages

### 1. Identify KA Consumers

Discover all agents and skills that read or may read KTY-local `Scoping.md` and `KA-*` files.

At minimum, review:

- publication workflows
- working-item and deliverable workflows
- aggregation workflows
- evaluation and audit workflows
- extraction workflows
- any task skills that consume KTY-local content

### 2. Classify Consumer Mandates

For each KA consumer, classify why it reads KTY content.

Expected mandate classes:

- factual publication or deliverable drafting
- extraction or structured data capture
- aggregation or synthesis
- audit / review / evaluation
- remediation / repair

Each class may require a different allowlist policy.

### 3. Update Agent Instructions

For each KA-consuming agent, add an explicit intake requirement:

- locate the active KTY content disposition artifact for the root
- derive a mandate-specific allowlist before reading KTY-local content as authority
- record the derived allowlist path or derivation evidence in the run report
- treat retired, archived, blocked, deferred, and non-authority content according to mandate

Publication and deliverable-writing agents should treat the allowlist as a hard factual-input gate. Audit and remediation agents may include blocked or retired rows only as inspection targets, not as factual authority.

### 4. Update Skills That Read KA Content

For each KA-consuming skill, add compatible intake parameters or runtime overrides for:

- root path
- disposition artifact path
- authority/consumer mode
- derived allowlist output path, where applicable

Skills should fail or clearly block when required disposition state is missing for workflows that depend on factual KA authority.

### 5. Add Evidence Requirements

Require each affected workflow to record:

- disposition artifact consumed
- allowlist derivation basis
- allowlisted paths or allowlist artifact path
- exclusions relevant to the workflow
- any blocked or deferred content encountered

### 6. Validate With Representative Consumers

Run at least one representative validation for each mandate class after instructions are updated.

Validation should prove:

- the consumer does not read retired or archived content as factual authority
- blocked or deferred content is handled according to mandate
- run evidence names the disposition source and allowlist basis

## Out Of Scope

- Current corpus remediation
- Creating or changing SCOPE_CHANGE remediation manifests
- Rewriting KA content
- Launching DBM publication production runs

## Completion Criteria

- All discovered KA-consuming agents and skills are either updated or explicitly documented as not requiring allowlist behavior.
- Factual-content workflows have hard intake gates tied to the disposition artifact.
- Audit/remediation workflows distinguish inspection targets from factual authority.
- Representative validations demonstrate that mandate-specific allowlists are derived and recorded.
