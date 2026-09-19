# Scratch: the same pairs at V1.3 (tokens.json 1.2) and at V1.4 (tokens.json 1.3)

Output of `scratch/scripts/measure.mjs`, which uses the contrast tool's arithmetic (WCAG 2.x relative luminance; a translucent token composited over the surface named after the slash). Readings are light / dark. Scratch output of DESIGN-SYSTEM-05; the record is `DESIGN_SYSTEM_V1.md` §2.9 and §5.

### The control boundary on every surface and band

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| boundary, on `surface.panel` | `border.strong` | 2.00:1 / 2.09:1 | `border.control` | 4.11:1 / 4.95:1 |
| boundary, on `surface.base` | `border.strong` | 1.75:1 / 2.36:1 | `border.control` | 3.60:1 / 5.60:1 |
| boundary, on `surface.sunken` | `border.strong` | 1.86:1 / 2.23:1 | `border.control` | 3.83:1 / 5.28:1 |
| boundary, on `surface.header` | `border.strong` | 1.79:1 / 1.96:1 | `border.control` | 3.69:1 / 4.64:1 |
| boundary, on `surface.raised` | `border.strong` | 2.00:1 / 1.82:1 | `border.control` | 4.11:1 / 4.32:1 |
| boundary, on `surface.rowAlt` | `border.strong` | 1.91:1 / 2.03:1 | `border.control` | 3.93:1 / 4.82:1 |
| boundary, on `canvas.bg` | `border.strong` | 1.70:1 / 2.41:1 | `border.control` | 3.50:1 / 5.73:1 |
| boundary, on `selection.band` | `border.strong` | 1.70:1 / 1.53:1 | `border.control` | 3.50:1 / 3.64:1 |
| boundary, on `proposal.band` | `border.strong` | 1.74:1 / 1.73:1 | `border.control` | 3.59:1 / 4.11:1 |
| boundary, on `stale.band` | `border.strong` | 1.86:1 / 1.93:1 | `border.control` | 3.83:1 / 4.58:1 |

### The control boundary on its own fill under the washes

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| boundary, on `hover.wash/surface.panel` | `border.strong` | 1.78:1 / 1.74:1 | `border.control` | 3.68:1 / 4.12:1 |
| boundary, on `hover.wash/surface.sunken` | `border.strong` | 1.66:1 / 1.87:1 | `border.control` | 3.41:1 / 4.44:1 |
| boundary, on `hover.wash/surface.raised` | `border.strong` | 1.78:1 / 1.52:1 | `border.control` | 3.68:1 / 3.60:1 |
| boundary, on `pressed.wash/surface.panel` | `border.strong` | 1.65:1 / 1.52:1 | `border.control` | 3.39:1 / 3.60:1 |
| boundary, on `pressed.wash/surface.sunken` | `border.strong` | 1.54:1 / 1.64:1 | `border.control` | 3.17:1 / 3.88:1 |
| boundary, on `pressed.wash/surface.raised` | `border.strong` | 1.65:1 / 1.32:1 | `border.control` | 3.39:1 / 3.14:1 |

### Switch

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| off track, on `surface.panel` | `border.strong` | 2.00:1 / 2.09:1 | `border.control` | 4.11:1 / 4.95:1 |
| off track, on `surface.header` | `border.strong` | 1.79:1 / 1.96:1 | `border.control` | 3.69:1 / 4.64:1 |
| off track, on `surface.raised` | `border.strong` | 2.00:1 / 1.82:1 | `border.control` | 4.11:1 / 4.32:1 |

Thumb on the off track: V1.3 `surface.panel` on `border.strong` 2.00:1 / 2.09:1; V1.4 `surface.panel` on `border.control` 4.11:1 / 4.95:1.

### Segmented control, active segment

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| segment edge against the trough, on `surface.sunken` | `surface.panel` | 1.07:1 / 1.07:1 | `border.control` | 3.83:1 / 5.28:1 |

### Latched toggle: what marks its edge

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| edge, on `surface.base` | `pressed.fill` | 1.11:1 / 1.82:1 | `pressed.ink` | 6.63:1 / 10.31:1 |
| edge, on `surface.panel` | `pressed.fill` | 1.27:1 / 1.61:1 | `pressed.ink` | 7.57:1 / 9.12:1 |
| edge, on `surface.header` | `pressed.fill` | 1.14:1 / 1.51:1 | `pressed.ink` | 6.79:1 / 8.55:1 |
| edge, on `surface.raised` | `pressed.fill` | 1.27:1 / 1.40:1 | `pressed.ink` | 7.57:1 / 7.96:1 |

### A chip that is on or chosen: what marks it

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| chosen filter chip (specimen), on `surface.header` | `status.solvedFill` | 1.02:1 / 1.14:1 | `pressed.ink` | 6.79:1 / 8.55:1 |
| chosen filter chip (specimen), on `surface.panel` | `status.solvedFill` | 1.14:1 / 1.22:1 | `pressed.ink` | 7.57:1 / 9.12:1 |
| chip that is on (frames), on `surface.header` | `selection.band` | 1.05:1 / 1.27:1 | `pressed.ink` | 6.79:1 / 8.55:1 |
| chip that is on (frames), on `surface.panel` | `selection.band` | 1.17:1 / 1.36:1 | `pressed.ink` | 7.57:1 / 9.12:1 |

### Active tab (frames)

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| boundary, on `surface.panel` | `border.strong` | 2.00:1 / 2.09:1 | `border.control` | 4.11:1 / 4.95:1 |
| boundary against its fill, on `surface.header` | `border.strong` | 1.79:1 / 1.96:1 | `border.control` | 3.69:1 / 4.64:1 |

### Check box (frames)

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| outline, on `surface.raised` | `border.strong` | 2.00:1 / 1.82:1 | `border.control` | 4.11:1 / 4.32:1 |
| outline, on `surface.panel` | `border.strong` | 2.00:1 / 2.09:1 | `border.control` | 4.11:1 / 4.95:1 |

### Quiet inks on a hovered band, which V1.4 no longer draws (the wash is not added to a band)

| Part | V1.3 drew it in | V1.3 light / dark | V1.4 draws it in | V1.4 light / dark |
|---|---|---|---|---|
| origin glyph, on `hover.wash/selection.band` | `mark.origin` | 2.89:1 / 2.71:1 | `mark.origin` | 2.89:1 / 2.71:1 |
| origin glyph, on `hover.wash/proposal.band` | `mark.origin` | 2.95:1 / 3.06:1 | `mark.origin` | 2.95:1 / 3.06:1 |

V1.4 draws the same glyph on the band without the wash: `mark.origin` on `selection.band` 3.23:1 / 3.24:1, on `proposal.band` 3.30:1 / 3.66:1.

### The disabled ink

| On | 1.2 `#a6abb1` / `#5f6469` | 1.3 `#8f949a` / `#767b80` | `text.muted` there | `text.secondary` there |
|---|---|---|---|---|
| `disabled.fill` | 1.94:1 / 2.28:1 | 2.56:1 / 3.19:1 | 3.17:1 / 4.07:1 | 5.24:1 / 6.37:1 |
| `surface.panel` | 2.31:1 / 2.48:1 | 3.06:1 / 3.46:1 | 3.79:1 / 4.41:1 | 6.26:1 / 6.91:1 |
| `surface.base` | 2.03:1 / 2.80:1 | 2.68:1 / 3.92:1 | 3.32:1 / 4.99:1 | 5.48:1 / 7.81:1 |
| `surface.sunken` | 2.15:1 / 2.64:1 | 2.85:1 / 3.69:1 | 3.53:1 / 4.70:1 | 5.83:1 / 7.37:1 |
| `surface.header` | 2.07:1 / 2.32:1 | 2.74:1 / 3.25:1 | 3.40:1 / 4.14:1 | 5.62:1 / 6.48:1 |
| `surface.raised` | 2.31:1 / 2.16:1 | 3.06:1 / 3.02:1 | 3.79:1 / 3.85:1 | 6.26:1 / 6.03:1 |
| `surface.rowAlt` | 2.21:1 / 2.41:1 | 2.92:1 / 3.37:1 | 3.62:1 / 4.30:1 | 5.99:1 / 6.73:1 |
| beside `text.muted` (ink to ink) | 1.64:1 / 1.78:1 | 1.24:1 / 1.27:1 | | |
| beside `text.secondary` (ink to ink) | 2.71:1 / 2.79:1 | 2.05:1 / 2.00:1 | | |

### The options

| Option | Light | on `disabled.fill` | lowest on a surface | highest on a surface | beside `text.muted` | Dark | on `disabled.fill` | lowest on a surface | highest on a surface | beside `text.muted` |
|---|---|---|---|---|---|---|---|---|---|---|
| keep (1.2) | `#a6abb1` | 1.94:1 | 2.03:1 | 2.31:1 | 1.64:1 | `#5f6469` | 2.28:1 | 2.16:1 | 2.80:1 | 1.78:1 |
| lift, recommended (1.3) | `#8f949a` | 2.56:1 | 2.68:1 | 3.06:1 | 1.24:1 | `#767b80` | 3.19:1 | 3.02:1 | 3.92:1 | 1.27:1 |
| 3:1 everywhere in light | `#82878c` | 3.03:1 | 3.17:1 | 3.62:1 | 1.04:1 | `#767b80` | 3.19:1 | 3.02:1 | 3.92:1 | 1.27:1 |
| the product's present ink (B1-TOKENS) | `#667680` | 3.94:1 | 4.12:1 | 4.70:1 | 1.24:1 | `#9baab2` | 5.71:1 | 5.40:1 | 7.00:1 | 1.40:1 |
