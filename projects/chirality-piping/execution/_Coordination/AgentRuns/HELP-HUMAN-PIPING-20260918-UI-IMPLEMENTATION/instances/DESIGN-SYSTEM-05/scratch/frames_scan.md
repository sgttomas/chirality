# Scratch: the frames that draw a control boundary in border.strong (read-only scan of MOCKS/frames)

Output of `scratch/scripts/frames_scan.mjs`. A count is the number of occurrences in the frame's markup; a dot is none. The frames were not touched.

Rules of mocks.css that use border.strong: 19
  draw a control's boundary (move to border.control): .seg, .btn, .input, .combo, .switch i, .search, .lenfield, .tabs .tab.on, .maprow .m .sel, .pop .row .k, .tblhead .switch.off i, .iconbtn.raised, .sendrow
  frame a region and identify nothing (stay): .stage, .lights i, .bar b, .expand .block, .card .asked, .content .live

| Frame | .seg | .btn bordered | .input | .combo | switch off | .search | .lenfield | .tabs .tab.on | .maprow .m .sel | .pop .row .k empty | .iconbtn.raised | .sendrow | latched .btn | latched HUD tool | .iconbtn.on | .chip.outline.on | agent tab on | .outline div.on |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `index.html` | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · |
| `s1_both_light.html` | 2 | 7 | · | 1 | · | 1 | · | 1 | · | · | · | · | · | · | · | · | · | · |
| `s2_model_dark.html` | 2 | 11 | · | 1 | · | 1 | 1 | 1 | · | · | 3 | · | · | 1 | · | · | · | · |
| `s2_model_light.html` | 2 | 11 | · | 1 | · | 1 | 1 | 1 | · | · | 3 | · | · | 1 | · | · | · | · |
| `s3_table_light.html` | 2 | 7 | · | 1 | · | 1 | · | 1 | 11 | · | · | · | · | · | · | · | · | · |
| `s4_both_light.html` | 2 | 8 | · | 1 | · | 1 | · | 1 | · | · | · | · | 1 | · | · | · | · | · |
| `s4_both_light_column.html` | 2 | 8 | · | 1 | · | 1 | · | 1 | · | · | · | · | 1 | · | · | · | · | · |
| `s4_both_light_slideover.html` | 2 | 8 | · | 1 | · | 1 | · | 1 | · | · | · | 1 | 2 | · | · | · | 1 | · |
| `s4_table_light.html` | 2 | 5 | · | 1 | · | 1 | · | 1 | · | · | · | · | · | · | · | · | · | · |
| `s5_table_light.html` | 2 | 6 | · | 3 | · | 1 | · | 1 | · | · | · | · | · | · | · | · | · | · |
| `s6_both_light.html` | 2 | 9 | · | 1 | · | 1 | · | 1 | · | · | · | · | · | · | · | 1 | · | · |
| `s7_both_dark.html` | 2 | 5 | · | 2 | 1 | 1 | · | 1 | · | · | · | · | · | 1 | · | · | · | · |
| `s7_both_light.html` | 2 | 5 | · | 2 | 1 | 1 | · | 1 | · | · | · | · | · | 1 | · | · | · | · |
| `s7_both_light_historical.html` | 2 | 5 | · | 2 | 1 | 1 | · | 1 | · | · | · | · | · | · | 1 | · | · | · |
| `s7_table_light.html` | 2 | 5 | 1 | 2 | · | 1 | · | 1 | · | 3 | · | · | · | · | · | · | · | · |
| `s8_model_light.html` | 2 | 8 | · | 1 | · | 1 | · | 1 | · | · | · | · | · | · | · | · | · | · |
| `s8_table_light.html` | 2 | 6 | · | 1 | · | 1 | · | 1 | · | · | · | 1 | 1 | · | · | · | 1 | · |
| `s9_table_dark.html` | 2 | 12 | · | 4 | · | 1 | · | · | · | · | · | · | · | · | · | 1 | · | 1 |
| `s9_table_light.html` | 2 | 12 | · | 4 | · | 1 | · | · | · | · | · | · | · | · | · | 1 | · | 1 |
