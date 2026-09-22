# Final publication title-label cleanup

Date: 2026-09-22
Authority: explicit parent `/root` instruction to change only the opening companion link label.

- Preimage SHA-256: `8e0782a12c9cd845d46b912c2c0dd34d90ea331b2cebd922add27fa356de86da`.
- Postimage SHA-256: `6739f5a559c5bae3efcdd8623457e48677fd92e21106410cba5e8e57310ddb1d`.
- Exactly one label occurrence changed, on line 5.
- The link target remains `Project_Management_for_Human_Agent_Teams_Consolidated_v4.md`.
- Companion Version 2 and source-basis metadata remain byte-identical.
- All operational content remains byte-identical; restoring the old label exactly reconstructs the preimage.
- Independent operational backcheck had passed the preimage. The reviewer is asked only to bind this one-label delta and regenerated HTML to the new hash.

```diff
--- UserManual_v2_before_title_label
+++ UserManual_v2_after_title_label
@@ -5 +5 @@
-An operational companion to [*Project Management for Human–Agent Teams, Consolidated v4*](Project_Management_for_Human_Agent_Teams_Consolidated_v4.md), for agents developing projects in the Chirality repository.
+An operational companion to [*Project Management for Human–Agent Teams*](Project_Management_for_Human_Agent_Teams_Consolidated_v4.md), for agents developing projects in the Chirality repository.
```
