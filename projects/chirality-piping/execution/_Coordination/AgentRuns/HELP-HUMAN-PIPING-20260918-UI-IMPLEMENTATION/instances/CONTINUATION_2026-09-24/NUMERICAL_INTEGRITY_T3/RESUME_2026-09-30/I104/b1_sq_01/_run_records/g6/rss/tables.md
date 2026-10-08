| Input | Mode | Route | Outcome | Requested-heap peak, MiB (median / max) | Bound | Peak / bound | Max RSS, MiB | Peak footprint, MiB | Real, s | Call, s |
|---|---|---|---|---|---|---|---|---|---|---|
| b2_k1e3 | dense | direct | notices(1) | 12.6 / 12.6 | E_mov_max 9,339.0 | 0.00135 | 37.6 / 38.0 | 26.5 / 26.8 | 20.50 / 20.52 | 20.50 / 20.52 |
| b2_k1e3 | dense | ordinary | ordinary_route | 12.6 / 12.6 | W1_phase 4,890.9 | 0.00257 | 31.3 / 31.3 | 21.8 / 21.8 | 0.17 / 0.17 | 0.17 / 0.17 |
| b2_k1e3 | sparse | direct | notices(1) | 12.6 / 12.6 | E_mov_max 9,282.7 | 0.00136 | 35.4 / 36.2 | 24.2 / 25.1 | 20.69 / 20.71 | 20.69 / 20.71 |
| b2_k1e3 | sparse | ordinary | ordinary_route | 12.6 / 12.6 | W1_phase 4,834.5 | 0.00260 | 29.3 / 29.3 | 19.7 / 19.7 | 0.09 / 0.09 | 0.09 / 0.09 |
| c1 | dense | direct | successor(2177405 B) | 40.0 / 40.0 | E_mov_max 9,339.0 | 0.00428 | 72.4 / 73.2 | 54.3 / 54.4 | 17.21 / 17.23 | 17.15 / 17.17 |
| c1 | dense | ordinary | ordinary_route | 12.7 / 12.7 | W1_phase 4,890.9 | 0.00259 | 31.2 / 31.2 | 21.6 / 21.6 | 0.14 / 0.14 | 0.14 / 0.14 |
| c1 | sparse | direct | successor(2176063 B) | 39.9 / 39.9 | E_mov_max 9,282.7 | 0.00430 | 69.8 / 71.8 | 51.8 / 52.2 | 17.23 / 17.29 | 17.17 / 17.21 |
| c1 | sparse | ordinary | ordinary_route | 12.7 / 12.7 | W1_phase 4,834.5 | 0.00262 | 28.7 / 28.7 | 19.0 / 19.0 | 0.09 / 0.09 | 0.09 / 0.09 |
| i3_three_case | dense | direct | successor(6651380 B) | 113.3 / 113.3 | E_mov_max 9,339.0 | 0.01213 | 161.0 / 161.0 | 112.3 / 112.3 | 51.56 / 51.72 | 51.38 / 51.55 |
| i3_three_case | dense | ordinary | ordinary_route | 30.2 / 30.2 | W1_phase 4,890.9 | 0.00618 | 56.0 / 56.0 | 46.4 / 46.4 | 0.39 / 0.39 | 0.39 / 0.39 |
| i3_three_case | sparse | direct | successor(6647340 B) | 113.2 / 113.2 | E_mov_max 9,282.7 | 0.01220 | 159.1 / 160.8 | 111.1 / 112.3 | 51.83 / 51.84 | 51.66 / 51.66 |
| i3_three_case | sparse | ordinary | ordinary_route | 30.2 / 30.2 | W1_phase 4,834.5 | 0.00625 | 53.4 / 53.4 | 43.8 / 43.8 | 0.26 / 0.26 | 0.25 / 0.25 |
| milestone | dense | direct | successor(114894 B) | 3.4 / 3.4 | E_mov_max 9,339.0 | 0.00036 | 20.5 / 20.5 | 7.8 / 7.9 | 0.65 / 0.65 | 0.65 / 0.65 |
| milestone | dense | ordinary | ordinary_route | 0.5 / 0.5 | W1_phase 4,890.9 | 0.00011 | 12.5 / 12.5 | 3.1 / 3.1 | 0.00 / 0.00 | 0.00 / 0.00 |
| milestone | sparse | direct | successor(113733 B) | 3.4 / 3.4 | E_mov_max 9,282.7 | 0.00036 | 20.5 / 20.5 | 7.8 / 7.8 | 0.65 / 0.70 | 0.65 / 0.69 |
| milestone | sparse | ordinary | ordinary_route | 0.5 / 0.5 | W1_phase 4,834.5 | 0.00011 | 12.5 / 12.5 | 3.1 / 3.1 | 0.00 / 0.00 | 0.00 / 0.00 |
| w2 | dense | direct | no_w1_work | 1.9 / 1.9 | W1_phase 4,890.9 | 0.00038 | 11.7 / 11.7 | 5.2 / 5.2 | 0.02 / 0.02 | 0.02 / 0.02 |
| w2 | dense | ordinary | ordinary_route | 1.9 / 1.9 | W1_phase 4,890.9 | 0.00038 | 10.9 / 10.9 | 5.1 / 5.1 | 0.02 / 0.02 | 0.02 / 0.02 |
| w2 | sparse | direct | no_w1_work | 1.9 / 1.9 | W1_phase 4,834.5 | 0.00039 | 11.7 / 11.7 | 5.2 / 5.2 | 0.02 / 0.02 | 0.02 / 0.02 |
| w2 | sparse | ordinary | ordinary_route | 1.9 / 1.9 | W1_phase 4,834.5 | 0.00039 | 10.9 / 10.9 | 5.1 / 5.1 | 0.02 / 0.02 | 0.02 / 0.02 |
| w_c2 | dense | direct | successor(455479 B) | 9.4 / 9.4 | E_mov_max 9,339.0 | 0.00101 | 27.6 / 27.8 | 14.9 / 15.1 | 1.22 / 1.24 | 1.21 / 1.22 |
| w_c2 | dense | ordinary | ordinary_route | 2.6 / 2.6 | W1_phase 4,890.9 | 0.00053 | 15.2 / 15.2 | 5.7 / 5.7 | 0.02 / 0.02 | 0.02 / 0.02 |
| w_c2 | sparse | direct | successor(455001 B) | 9.4 / 9.4 | E_mov_max 9,282.7 | 0.00101 | 27.7 / 27.9 | 15.0 / 15.2 | 1.21 / 1.23 | 1.20 / 1.22 |
| w_c2 | sparse | ordinary | ordinary_route | 2.6 / 2.6 | W1_phase 4,834.5 | 0.00053 | 15.3 / 15.6 | 5.7 / 6.0 | 0.02 / 0.02 | 0.02 / 0.02 |
| w_c2_ac | sparse | direct | successor(342907 B) | 7.2 / 7.2 | E_mov_max 9,282.7 | 0.00077 | 25.5 / 25.6 | 12.8 / 12.9 | 1.17 / 1.19 | 1.16 / 1.18 |
| w_c2_ac | sparse | ordinary | ordinary_route | 1.7 / 1.7 | W1_phase 4,834.5 | 0.00035 | 14.4 / 14.4 | 4.8 / 4.8 | 0.01 / 0.01 | 0.01 / 0.01 |
| process floor | — | — | — | — | — | — | 2.7 / 2.7 | 1.6 / 1.6 | 0.00 / 0.02 | — |

| Input | Mode | Entry | Witness outcome | Max RSS, MiB (median / max) | Peak footprint, MiB | Real, s | Ordinary run (+ parse), s | W1, s |
|---|---|---|---|---|---|---|---|---|
| b2_k1e3 | dense | ordinary | — | 28.7 / 29.3 | 24.0 / 24.6 | 0.01 / 0.01 | 0.02 / 0.02 | — |
| b2_k1e3 | dense | witness | Fallback("Candidate") | 36.4 / 36.5 | 30.2 / 30.3 | 0.68 / 0.68 | 0.01 / 0.02 | 0.67 / 0.67 |
| b2_k1e3 | sparse | ordinary | — | 26.1 / 27.1 | 21.4 / 22.5 | 0.01 / 0.01 | 0.01 / 0.01 | — |
| b2_k1e3 | sparse | witness | Fallback("Candidate") | 33.3 / 34.3 | 27.2 / 28.1 | 0.68 / 0.68 | 0.01 / 0.01 | 0.67 / 0.67 |
| c1 | dense | ordinary | — | 29.3 / 29.3 | 24.6 / 24.6 | 0.01 / 0.01 | 0.01 / 0.01 | — |
| c1 | dense | witness | Successor | 83.9 / 83.9 | 62.4 / 62.4 | 0.59 / 0.60 | 0.01 / 0.01 | 0.58 / 0.58 |
| c1 | sparse | ordinary | — | 26.6 / 26.6 | 21.8 / 21.8 | 0.01 / 0.01 | 0.01 / 0.01 | — |
| c1 | sparse | witness | Successor | 81.2 / 81.3 | 59.7 / 59.8 | 0.58 / 0.59 | 0.01 / 0.01 | 0.57 / 0.58 |
| floor | — | floor | — | 2.8 / 2.8 | 1.7 / 1.7 | 0.00 / 0.01 | — | — |
| i3_three_case | dense | ordinary | — | 55.1 / 55.2 | 50.4 / 50.4 | 0.04 / 0.04 | 0.04 / 0.04 | — |
| i3_three_case | dense | witness | Successor | 206.3 / 206.5 | 134.3 / 134.4 | 1.74 / 1.76 | 0.04 / 0.04 | 1.69 / 1.72 |
| i3_three_case | sparse | ordinary | — | 51.2 / 52.2 | 46.5 / 47.5 | 0.03 / 0.03 | 0.03 / 0.03 | — |
| i3_three_case | sparse | witness | Successor | 201.8 / 203.8 | 131.4 / 133.0 | 1.73 / 1.77 | 0.03 / 0.03 | 1.69 / 1.73 |
| milestone | dense | ordinary | — | 7.8 / 7.8 | 3.2 / 3.2 | 0.00 / 0.00 | 0.00 / 0.00 | — |
| milestone | dense | witness | Successor | 16.0 / 16.2 | 8.5 / 8.7 | 0.03 / 0.03 | 0.00 / 0.00 | 0.03 / 0.03 |
| milestone | sparse | ordinary | — | 7.8 / 7.8 | 3.1 / 3.2 | 0.00 / 0.00 | 0.00 / 0.00 | — |
| milestone | sparse | witness | Successor | 16.2 / 16.2 | 8.6 / 8.6 | 0.03 / 0.03 | 0.00 / 0.00 | 0.03 / 0.03 |
| w2 | dense | ordinary | — | 8.3 / 8.3 | 5.3 / 5.3 | 0.00 / 0.00 | 0.00 / 0.00 | — |
| w2 | dense | witness | Fallback("Preparation") | 8.4 / 8.4 | 5.3 / 5.3 | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 |
| w2 | sparse | ordinary | — | 8.3 / 8.4 | 5.3 / 5.3 | 0.00 / 0.00 | 0.00 / 0.00 | — |
| w2 | sparse | witness | Fallback("Preparation") | 8.4 / 8.9 | 5.3 / 5.8 | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 |
| w_c2 | dense | ordinary | — | 10.5 / 10.6 | 5.9 / 5.9 | 0.00 / 0.00 | 0.00 / 0.00 | — |
| w_c2 | dense | witness | Successor | 24.6 / 24.8 | 16.9 / 17.1 | 0.11 / 0.12 | 0.00 / 0.00 | 0.06 / 0.06 |
| w_c2 | sparse | ordinary | — | 10.6 / 10.7 | 5.9 / 6.0 | 0.00 / 0.00 | 0.00 / 0.00 | — |
| w_c2 | sparse | witness | Successor | 24.5 / 24.6 | 16.8 / 16.9 | 0.12 / 0.12 | 0.00 / 0.00 | 0.06 / 0.06 |
| w_c2_ac | sparse | witness | Successor | 22.6 / 22.7 | 14.9 / 15.0 | 0.05 / 0.08 | 0.00 / 0.01 | 0.05 / 0.06 |
