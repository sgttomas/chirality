# OD6-D-A — Degraded and failure semantics design-basis acceptance

**Status:** `APPLICATION_CANDIDATE_ONLY`
**Date:** 2026-07-27
**Record ID:** OD6-D-A
**Accepted repository basis:** `9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`
**AcceptedSourcePath:** `source_artifacts/D-A_DEGRADED_FAILURE_SEMANTICS_CANDIDATE.md`
**AcceptedSourceSHA256:** `f10b17f6ce6ce524efa82bf10b9e89eae8c91eb7a9bff39a79d277cf45d0bf7c`
**IntegralMatrixPath:** `source_artifacts/D-A_CODE_MATRIX.csv`
**IntegralMatrixSHA256:** `c2d13841e98179878df5fd8b772be66bb829c3c09c240d74d62ee552db5d0ea7`
**Predecessor:** OD6-V-A
**Successor:** OD6-R-A

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

The exact D-A source bytes and integral matrix are accepted as a later Root
runtime contract-design basis, ordered after V-A. They do not make V-A
effective, select a wire encoding, change error identifiers, migrate a client,
prove retained functions, authorize implementation, or establish live
degraded-mode behavior.

Later work may consume D-A only after consuming the exact accepted V-A design
basis, by citing both exact SHA-256 identities and this record. It must preserve
the unresolved mappings, evidence duties, affected-client gates, and
fail-closed boundaries in the accepted source.
