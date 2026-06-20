# Validation Server/Build Isolation Follow-Up

**Date:** 2026-06-19
**Status:** OPEN
**Discovered during:** D-APP-28 loop-first pivot tranche `28c`

## Issue

During `28c` validation, the first `npm run harness:validate:premerge` attempt
failed on `regression.session_crud` while a Next dev server was still running
after browser verification and after build/package commands had rewritten
`.next`. The dev-server log showed a transient module-resolution failure for
`.next/server/vendor-chunks/next.js`; a rerun passed Section 8 8/8 and Section
9 report-only 13/13.

## Proposed Fix

Codify validation sequencing so agents stop the local dev server before running
`npm run build`, `npm run desktop:pack`, or `npm run harness:validate:premerge`
unless the command explicitly owns the server lifecycle. The closeout checklist
should call out this ordering to avoid treating a dev-server/build race as a
product regression.

## Acceptance

- The relevant coordination or validation guidance records the sequencing rule.
- Future browser-validation tranches stop the dev server before build/package
  and premerge validation.
- Harness failures caused by `.next` dev/build races are recorded as environment
  sequencing failures, not product failures, and are rerun after isolation.
