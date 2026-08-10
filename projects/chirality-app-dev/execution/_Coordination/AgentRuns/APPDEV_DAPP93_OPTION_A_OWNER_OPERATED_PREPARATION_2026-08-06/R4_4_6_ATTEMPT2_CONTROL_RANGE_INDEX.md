# R4.4.6 attempt-2 CONTROL range index

Status: `DERIVED — ZERO-BASED, END-EXCLUSIVE`

Transcript: `control-transcript.txt`, 80266 bytes, SHA-256
`ff78e462c81563c97ada775c590412ca9cc27e4ea474e68aea353873c323690a`.

| Step | Range | Marker exit |
|---|---:|---:|
| 01 | `[0,264)` | 0 |
| 02 | `[264,1137)` | 0 |
| 03 | `[1137,1867)` | 0 |
| 04 | `[1867,5182)` | 0 |
| 05 | `[5182,11707)` | 0 |
| 06 | `[11707,14030)` | 0 |
| 07 | `[14030,14853)` | 0 |
| 08 | `[14853,16289)` | 0 |
| 09 | `[16289,23028)` | 0 |
| 10 | `[23028,50335)` | 0 |
| 11 | `[50335,64537)` | 0 |
| 12 | `[64537,65530)` | 0 |
| 13 | `[65530,65973)` | 0 |
| 14 | `[65973,66675)` | 1 |
| 15 | `[66675,67664)` | 0 |
| 23 | `[67664,68635)` | 0 |
| 25 | `[68635,73872)` | 0 |
| 26 | `[73872,74721)` | 0 |
| 27 | `[74721,75397)` | 1 |
| 28 | `[75397,77785)` | 0 |
| 29 | `[77785,79738)` | 0 |
| 30 | `[79738,80156)` | 0 |

Exactly 22 markers occur once in this order. Steps 16-22 and 24 are honestly
absent. Bytes `[80156,80266)` are only the final rendered prompt/newline; no
CONTROL input follows C1146.30. STEP-14 exit 1 truthfully records absent
pre-GUI socket/owner paths. STEP-27 exit 1 truthfully records A1129.G's zero-row
observation after the GUI had exited; no inapplicable GUI KILL followed.
