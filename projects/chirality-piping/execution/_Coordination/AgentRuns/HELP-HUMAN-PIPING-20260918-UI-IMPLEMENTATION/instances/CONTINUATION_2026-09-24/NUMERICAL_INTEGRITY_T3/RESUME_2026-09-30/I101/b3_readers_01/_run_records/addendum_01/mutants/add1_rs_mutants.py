"""I101 addendum 01: RS mutants, one per clause of G8's sourced-case check as ROOT ruled (on b2-r c845e899da)."""
RP = "core/reporting/result_export/src/retained_precision.rs"
NEW = '''                case.get("pressure_regions")
                    .is_none_or(|r| r.is_null() || r.as_array().is_some_and(Vec::is_empty))'''
M = [
 ("C1", "analysis_state admitted (both routes)", RP,
  '''            } && case["equivalent_static"].is_null()
                && !case
                    .as_object()
                    .is_some_and(|o| o.contains_key("analysis_state")),''',
  '''            } && case["equivalent_static"].is_null(),'''),
 ("C2", "preview pressure_regions read as falsy (the reading before the ruling)", RP, NEW, '''                list(&case["pressure_regions"]).is_empty()'''),
 ("C3", "preview pressure_regions: any list admitted", RP, NEW, '''                case.get("pressure_regions")
                    .is_none_or(|r| r.is_null() || r.is_array())'''),
 ("C4", "a case-level pressure refused", RP,
  '''            } && case["equivalent_static"].is_null()
                && !case''',
  '''            } && case["equivalent_static"].is_null() && case["pressure"].is_null()
                && !case'''),
]
