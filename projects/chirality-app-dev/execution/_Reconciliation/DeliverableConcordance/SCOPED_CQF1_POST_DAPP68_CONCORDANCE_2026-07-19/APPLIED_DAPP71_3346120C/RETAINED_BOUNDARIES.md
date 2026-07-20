# D-APP-71 Retained Boundaries

## Applied physical lead

DEL-02-05 is the physical integration lead for
`projects/chirality-app-dev/frontend/electron/preload.ts`. Physical leadership
means coordination of the shared file only; it is not semantic ownership and
does not authorize source repair.

## Retained semantic boundaries

- DEL-02-03 retains `selectDirectory` semantics.
- DEL-02-05 retains `apiKey` semantics.
- DEL-09-06 retains `safeStorage`/security semantics.

These are three distinct semantic interests. The coordination lead must
preserve each boundary when sequencing any separately authorized future work.

## Unauthorized effects

No semantic responsibility transfers to DEL-02-05. No preload or runtime
source, ScopeOfWork, dependency, MEMORY, decomposition, authority,
decision/register, lifecycle, release/publication, hard-fence, waiver, or Git
state changes through this documentary mapping.
