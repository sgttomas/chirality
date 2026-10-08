# RV122 addendum 01: mutants on I103's repair round 01 (head ea5625ad04). (id, file under PP/src, check, old, new)
M = [
 ("A1-SF1-a", "lib.rs", "the G8 precommit fallback publishes without its notice",
  "            ordinary.diagnostics.push(notice);\n", "            if !matches!(cause, W1Fallback::Precommit { gate: \"G8\", .. }) { ordinary.diagnostics.push(notice); }\n"),
 ("A1-SF2-a", "retained_memory.rs", "exact regions capacity check removed",
  "filter(|regions| regions.capacity() != 0)", "filter(|regions| regions.capacity() != 0 && false)"),
 ("A1-SF2-b", "retained_memory.rs", "exact regions capacity: only above 1 refuses",
  "filter(|regions| regions.capacity() != 0)", "filter(|regions| regions.capacity() > 1)"),
 ("A1-SF2-c", "retained_memory.rs", "exact regions capacity read on the first case only",
  "filter(|regions| regions.capacity() != 0)", "filter(|regions| regions.capacity() != 0 && case.id == m.load_cases[0].id)"),
]
