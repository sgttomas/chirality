# Attempts

1. Initial reproduction mechanically misparsed the registered source marker by expecting a colon. The false block-count failures were retained in the turn record; the owned parser was corrected and all 57 members passed.
2. Initial App test copy omitted repository-level fixtures. It produced 708 passing tests and four ENOENT failures. The failed log is retained as `checks/app_tests.txt`; the complete-layout rerun passed and is retained as `checks/app_tests_r1.txt`.
3. Initial rollback audit assumed one historical schema. The traceback was retained in the turn record; normalization for `D/A`, `DELETE/ADD`, `RESTORE`, and before/after hash fields passed all 730 rows.
