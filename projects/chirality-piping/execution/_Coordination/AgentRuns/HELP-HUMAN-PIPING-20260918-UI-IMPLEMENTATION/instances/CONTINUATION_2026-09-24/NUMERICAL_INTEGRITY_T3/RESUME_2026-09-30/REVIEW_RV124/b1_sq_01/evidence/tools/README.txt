RV124's own scripts (paths sanitized to placeholders: WT, R, T). The chain also used, unchanged and byte-identical
to I104's records (so not copied here): R/I104/b1_sq_01/_run_records/tools/{b1q_chain.py, i104_rules.py, decisions.py,
g7_linemap_crates.py, mk_looplog.py}, g6/tools/sq_n5_chain.py, g5/loop_inventory_b1_lines.json (as inv.json), and
I65's R/I65/u4_g7_06/_run_records/chain/ with g7_linemap.py's premise pins.
Order: text_base_rv.sh -> b1q_chain.py -> i104_rules.py -> sq_n5_chain.py -> chain_text.sh (run_point_rv.sh per point)
-> g5_profile.py on each tree; chain_reg_suite.sh; chain_wit.sh; chain_mut.sh (mutants.py); chain_py2.sh
(audit_controls_rv124.py, noncand); chain_probe2.sh (size_probe.py); chain_final.sh (rss_batch_rv.sh under t3_exclusive.sh).
