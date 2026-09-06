# Expanded composer keyboard diagnosis

Confirmed ordinary first-keystroke loss on frozen v3. Normal click focused the textarea without restoring the expanded panel. Pressing a restored the panel but left the textarea empty. Typing b then c produced bc. The textarea remained the same DOM node throughout. Keyboard clear followed by ordinary non-expanded x, y, z produced xyz correctly. No fill, force click, source patch or synthetic handler invocation was used.

keyboard-result.json preserves every observation and native focus/keydown/beforeinput/input/keyup event. First input event reports data a but empty value; subsequent events retain their characters. Previous fill failure remains separate evidence and is not the basis for the ordinary keyboard claim.

All 25 source hashes match manifest v3 before/after. Browser closed in finally; server session86286 Ctrl-C exit0; host port3187 ECONNREFUSED61. Source released for repair. No account/runtime/native actions.
