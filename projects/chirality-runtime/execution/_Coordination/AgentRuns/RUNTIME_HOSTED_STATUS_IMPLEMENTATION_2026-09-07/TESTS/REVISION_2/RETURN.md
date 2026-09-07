# Test fixture repair, revision 2

Parent relayed authorized validation: setup completed, typecheck passed, first test command 124/125 passed. The pure native-policy rendering fixture omitted required protectedPaths, so its positive path failed before policy creation.

The only live edit is tests/custody-config-status.test.ts. Its native-policy options now place private worker/home under a synthetic broker root disjoint from project root and immutable /usr reads. protectedPaths names the broker parent explicitly. Assertions check emitted broker and worker subtree denies (which cover the nested home), instead of expecting a separately emitted home key. The trusted-login rejection case now supplies its required empty protectedPaths field; it still rejects on purpose first.

Original TESTS packet a34d118da921a9273b1ef44b700e189aa6b7e273a9bf296d4357f7c99f4290f4 and all six members rehashed unchanged. No source changes, extra cases, test/build/dependency commands, real filesystem fixture execution, supplier or account operations. This child performed the exact edit and read-only inspection only. Manager owns rerun and validation evidence. Revision remains unvalidated until that rerun; no qualification is implied.
