# Carrier formatting normalization

Status: `FORMATTING ONLY / ACCEPTED SEMANTICS UNCHANGED`

The owner-directed candidate-whitespace follow-up removed only trailing spaces,
Markdown hard-break pairs, and surplus terminal blank lines inside this carrier.
No semantic word, punctuation, ordering, authority, scope, or implementation
obligation changed.

| File | Pre-normalization SHA-256 | First normalized SHA-256 | Finding class |
|---|---|---|---|
| `ACCEPTANCE_RECORD.md` | `c0b91e3d87bb6d3a8580f47491d99feccd7e9b77c606eee60b9df596efffc217` | `ec51e7462bd5de912c5811bb5b1fc093760f3410ad46896805d2bebe0b5559dd` | four hard-break pairs; terminal blank line |
| `AUTHORITY_BINDING.json` | `ac2869678dd80e10c85353889e62f35625419c464a117a4a4037f1da3e862231` | `b053725358131ccd1ba84e48bd4d1f58dcda87e28eea2b0251826fc97c66d25d` | terminal blank line |
| `HANDOFF_STATE.md` | `cd697e92c64b2ede1d112784d57ff48424358ad5542894d7898c7d874da9d7b2` | `3679365f5f5e6a7b2ef3fe91cccd4e6523bcc310fde9e0fb79e74625ea578b4d` | terminal blank line |
| `IMPLEMENTATION_BRIEF.md` | `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218` | `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d` | two hard-break pairs; terminal blank line |
| `MANAGER_RETURN.md` | `1ffe898135df8ee196eaf21478757ccee9d7bd91722f91592280f90ece9a0db7` | `5336abe244b850f42503aa00bbf81ee669a583df79aba3203409de8a9efd9a03` | one hard-break pair; terminal blank line |
| `RUN_RECORD.md` | `7ff03c0458793e711b4766c981302e94731d3ce491d77895fedf5f2261e7db51` | `ef9cec611713c8abeac97099ae1f1f79e1831184d8f7269c0e50079050c9451e` | three hard-break pairs; terminal blank line |
| `VALIDATION.md` | `20188781ddff24abd804a2f8c416a36f87a1c34885b5b28704dfa02215d6c701` | `17eeffc9ad6c9cdbbeef5dabf6b13b6c3e82482a7f495f6a0e00499f0d8c489f` | one hard-break pair; terminal blank line |

Files subsequently refreshed to record these identities receive final hashes in
`BASIS_MANIFEST.sha256`. The implementation carrier must replace its prior
brief identity with
`617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`.

The signed transcript SHA, exact signed-block SHA, accepted pre/post clause
hashes, G2/C1/F1 selection, and N-STOP-1..7 semantics remain unchanged.
