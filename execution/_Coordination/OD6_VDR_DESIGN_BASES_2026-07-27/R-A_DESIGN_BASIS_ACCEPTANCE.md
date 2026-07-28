# OD6-R-A — Release and rollback design-basis acceptance

**Status:** `APPLICATION_CANDIDATE_ONLY`
**Date:** 2026-07-27
**Record ID:** OD6-R-A
**Accepted repository basis:** `9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`
**AcceptedSourcePath:** `source_artifacts/R-A_RELEASE_ROLLBACK_CANDIDATE.md`
**AcceptedSourceSHA256:** `ff7850d5bf9db4d1ef7f25ac47a6b6522bd9c84eec8db8e1a0a28bbced1b4fae`
**IntegralSchemaPath:** `source_artifacts/R-A_RELEASE_MANIFEST_SCHEMA_CANDIDATE.json`
**IntegralSchemaSHA256:** `437c1d1131d2d2e9fb02d62aeecb84525266fad218ebf5cb9c42167d76133666`
**Predecessors:** OD6-V-A, OD6-D-A
**Successor:** none

## Owner direction

Ryan Tufts, in-session, 2026-07-27:

> ACCEPT V-A
> 79ea5982db946fda9e1c5356a471da4f3bb8509507a6648595abaf65e928eb5f,
> D-A
> f10b17f6ce6ce524efa82bf10b9e89eae8c91eb7a9bff39a79d277cf45d0bf7c
> with matrix
> c2d13841e98179878df5fd8b772be66bb829c3c09c240d74d62ee552db5d0ea7,
> and R-A
> ff7850d5bf9db4d1ef7f25ac47a6b6522bd9c84eec8db8e1a0a28bbced1b4fae
> with schema
> 437c1d1131d2d2e9fb02d62aeecb84525266fad218ebf5cb9c42167d76133666,
> as design bases only, ordered V → D → R. No live contract,
> implementation, migration, compatibility claim, or release is authorized.

## Recorded disposition

The exact R-A source bytes and integral schema are accepted as a later
release-assurance design basis, ordered after V-A and D-A. They select no
release instance, source, build, artifact, release ID, compatibility claim,
migration, rollback target, distribution, activation, publication, or
professional reliance.

Later work may consume R-A only after consuming the exact accepted V-A and
D-A design bases and their integral artifacts. A release manifest instance,
release identity, compatibility evidence, affected-client dispositions, and
accountable-human release act remain separate later gates.
