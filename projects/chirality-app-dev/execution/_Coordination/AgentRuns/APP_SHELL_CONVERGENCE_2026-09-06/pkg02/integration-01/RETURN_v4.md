# Bounded remediation v4 return

Status: frozen for fresh full-diff review. Derivative source/evidence candidate against accepted e00238621db7a00b036245962c21e3fc6ed75452; no authoritative deliverable closure.

Assistant messages now capture local origin persona at creation, including the initial greeting. Retained labels/titles use origin metadata while newly created replies use the newly selected Agent. No persisted transcript/session truth was introduced.

The parent input-capture listener is removed. The actively wired onDraftCaptured callback restores expansion after ChatPanel captures the changed draft. Composing input updates draft without restoring layout; composition end captures its current value before restoring. Typing and paste share the draft-first change path. No textarea remount/key or focus operation was introduced. Prior binding and Settings repairs are unchanged.

Focused feedback: 2 files / 22 tests PASS in focused-remediation-v4.log. These include two-Agent historical attribution, first-character/paste preservation, composition deferral, stable textarea instance, and activated shell restoration callback. They are synthetic component regression tests; real ordinary keyboard/paste/IME browser proof remains required. An earlier append attempt used a root-relative path from frontend and failed without modifying a file; the subsequent preliminary tests passed 20 existing tests. The append was rerun correctly and final 22 tests passed. Registered frontend-typecheck PASS in typecheck-remediation-v4.json. Whitespace and scope checks PASS. No full suite, build or native execution performed.

Complete SOURCE_MANIFEST_v4.json SHA256 3ca05c1e6187478b345d658e0039ada1eedc0cdba862da9496ca592bd39a0c93, 25 members; SOURCE_DIFF_v4.patch contains the full candidate against accepted base. Four members changed since v3: chat-panel.tsx, woven-dialogue-shell.tsx, chat-panel-folder-binding.test.tsx, woven-dialogue-shell.test.tsx. Source held unchanged after freeze. All prior manifests/reviews/browser failures remain retained.

Fresh independent full-diff review, real browser regression, final registered tests and isolated native proof remain manager-owned. No lifecycle/publication/no-folder/T4/T6/per-chat Reveal/D121 completion claim. Agent2 TASK, no delegation; exact model identifier unavailable, not inferred.
