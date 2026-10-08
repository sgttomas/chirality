"""I101 addendum 01: TS mutants, one per clause of G8's sourced-case check as ROOT ruled (on b2-t 77aaaa61d1)."""
RP = "apps/desktop/src/features/results/retainedPrecision.ts"
OLD = "regions == null || (Array.isArray(regions) && regions.length === 0)"
M = [
 ("C1", "analysis_state admitted (both routes)", RP, " && !Object.hasOwn(c, 'analysis_state'));", ");"),
 ("C2", "preview pressure_regions read as falsy (the reading before the ruling)", RP, OLD, "!regions?.length"),
 ("C3", "preview pressure_regions: any list admitted", RP, OLD, "regions == null || Array.isArray(regions)"),
 ("C4", "a case-level pressure refused (the clause the ruling dropped)", RP, " && !Object.hasOwn(c, 'analysis_state'));", " && !Object.hasOwn(c, 'analysis_state') && c.pressure == null);"),
]
