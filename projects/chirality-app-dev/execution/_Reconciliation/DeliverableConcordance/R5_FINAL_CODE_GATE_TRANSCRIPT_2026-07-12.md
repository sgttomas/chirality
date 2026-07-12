# D-APP-55 R5 final-code full-repository gate transcript

**Gate date:** 2026-07-12  
**Source commit:** `cbef0aac2069b5edfe4ee35654e9d9bd652047d3`  
**Environment:** fresh disposable full-repository clone at
`/tmp/chirality-d55-code-gate`, detached at the source commit  
**Initial clone status:** clean (`git status --porcelain` count `0`)  
**Result:** PASS

This is a derivative gate record. It cites the accepted D-APP-55 run snapshot
but does not amend the immutable
`RUN_D55_CONCORDANCE_2026-07-11_1904Z` folder.

## Transcript

### Dependency installation

```text
$ cd projects/chirality-app-dev/frontend
$ npm ci
added 735 packages, and audited 737 packages
exit: 0
```

The installer reported the existing dependency-audit inventory (31 findings);
no dependency or lockfile was changed by this gate.

### Full typecheck

```text
$ npm run typecheck
> tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false
exit: 0
```

### Full Vitest

```text
$ npm test
> vitest run

Test Files  95 passed | 1 skipped (96)
Tests       680 passed | 4 skipped (684)
Duration    4.16s
exit: 0
```

The four skipped tests are the pre-existing opt-in PEC bridge integration
suite; all runnable tests passed.

## Raw capture integrity

The complete combined stdout/stderr capture contained 220 lines / 17,004 bytes
and had SHA-256:

```text
9c7f4aa9cd7af97725a6d4f243c564c73af4087c88c83f82302738f7217cd4c8
```

Terminal marker: `GATE_RESULT=PASS`.
