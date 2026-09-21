## 8. Cross-package observations for R3 (hand-written by the PKG-01 manager; evidence, not rulings)

1. **The App DIRECTIVE was never amended for D-GOV-43, and this drives most PKG-01 R4 rows.**
   - There are 27 AUTHORITY_CONFLICT rows: DEL-01-01 4, 01-02 7, 01-03_A 4, 01-04 12. All four workers found
     independently that D-GOV-43 names Root DIRECTIVE §5/§7 but none of the following App clauses:
     - App DIRECTIVE §2.8 (Claude Agent SDK / Anthropic as the key-aware default; Chirality owns permission
       policy);
     - §2.10 (faithful vs translated events: R4-Q5);
     - §4.2 (no shipped bypass; no remote MCP);
     - CONTRACT K-PERM-1/K-PERM-6 (hard-deny precedence).
   - App DIRECTIVE §0 does not rank a Root ruling, so it cannot resolve these rows. The verifiers confirmed
     §1 handling on every checked conflict row.
   - The two material live-path cases are in DEL-01-04 (CLM-003.5 and others):
     - the live composer offers "Full access" (approval never plus danger-full-access) with no guard;
     - the live runtime links the user's whole `~/.codex` (config, plugins, MCP) unfiltered.
     D-GOV-43 items 3–4 permit both, and the unamended DIRECTIVE §4.2 / PRD §3.2 / K-PERM-6 / K-NET-1 forbid
     them.
   - These rows carry plain `R4` (14 in DEL-01-04), because no named question covers "D-GOV-43 items 3–4
     against unamended App DIRECTIVE/CONTRACT permission and network clauses". **Candidate R4-Q6**, framed
     for R3, not ruled.
   - Other packages' §2.8-based rows should cluster with these.
2. **The reliance boundary register (DEL-01-02) describes the legacy harness, not the shipped product.**
   - 12 of 13 indexed Section 9 IDs exercise legacy-only modules. Hooks, hard-deny, instruction-root and
     symlink protection, and `settingSources` exist only on the LEGACY_ONLY Claude path. R4-Q1 appears 32
     times in this ledger.
   - The live Codex-path controls have no register rows: approval/sandbox policy, effective Codex home
     sharing the user config, Electron renderer hardening and egress, packaged supply boundary, dynamic
     tools.
   - This is the package-level form of R0 §8 item 1. It bears on PKG-04/06/08/10 (HARNESS) and on PKG-09
     (release).
3. **The human-authority gate on the live path** (DEL-01-01, DEL-01-02 CLM-006.5/007.6, contested).
   - The served status-transition route requires `HUMAN` and an `approvalSha`, but the actor is
     caller-asserted and the SHA is checked for format only.
   - No live UI performs lifecycle transitions: the Workbench status form is unmounted
     (`woven-dialogue-route.tsx:18`).
   - Related to R4-Q3, which names only the legacy `status_transition` tool; R3 may widen it to the live
     route. Owner-side routing: PKG-02 (shell) or PKG-05.
4. **Corpus-wide DOC_HYGIENE, as in every earlier package.**
   - All 12 PKG-01 `_REFERENCES.md` MATCH hashes fail to reproduce.
   - REF-007 points to the deleted `agents/AGENT_SOFTWARE_DECOMP.md` (d1166698d, 2026-09-09) in DEL-01-01,
     01-03 and 01-04. Candidate R4-Q4 context: four-role adoption.
   - Dependency rows called "TBD" have all been SATISFIED since D-APP-53.
   - Project-local `.chirality/sessions/.../events.jsonl` is still named canonical, against amended K-EVENT-4
     (DEL-01-01, 01-02). This is R0 §8 item 8, now in two deliverables.
5. **Retired-engine copy is still reachable** (DEL-01-03).
   - A's erratum, which the verifier CONFIRMED, says the "Anthropic API Key" panel renders through the live
     404 page's legacy ShellFrame. B says it never renders, and CAP-SETTINGS-009 records STATE=DISABLED.
     R3 should settle this by a focused check.
   - B also lists `api.anthropic.com` in the renderer egress allowlist and a live "Anthropic API key is
     missing" error string.
   - No carrier covers Codex/OpenAI identity or disclosure copy (the "Codex" tab, ChatGPT sign-in).
6. **Release signing (for PKG-09).** DEL-01-04's reverse pass notes that CAP-BUILD-016 has signing off by
   default and no notarization step, while the docs describe a signed and notarized candidate.
7. **Default permission posture.** The live default is `workspaceWrite` with approval `never`, where D-GOV-43
   recommends on-request for new projects (DEL-01-04 reverse_notes). This belongs with observation 1.

### Coverage gaps: scope with no forward row a worker could own (from notes and reverse_notes)

- **DEL-01-01:**
  - App DIRECTIVE §8 (shared-runtime daemon direction) has no row and is unamended for A2.
  - No live lifecycle-transition UI (above).
- **DEL-01-02:**
  - No register rows for the live Codex-path controls listed in observation 2.
  - No reference-hash warning surface.
- **DEL-01-03:**
  - Codex/OpenAI disclosure copy is unreviewed.
  - Retired-engine copy remains on the live 404 path.
  - Update-check wording is not checked against checklist PB-08.
  - The layout metadata description still names PORTAL/PIPELINE/WORKBENCH.
  - Legacy shell brand copy remains.
  - `docs/BOUNDARY_REVIEW_CHECKLISTS.md` still has stale "REF-006 currently MATCH" and "Anthropic default
    stands" lines.
- **DEL-01-04:**
  - The post-release application-supplied dynamic tools API (`da95ec194`; RTCORE-033, RTCONTRACT-034/035)
    has no owning row.
  - No row covers the user's shared Codex configuration.
  - No row covers the default approval/sandbox posture.

### Method notes

- **Split ledger (DEL-01-02).**
  - Subset indexes and `cf.` cross-half references kept each half valid, but the halves disagreed on the
    same authority question (VERIFICATION §4 pattern 2).
  - For future splits, give both halves a shared list of the authority questions in play before they seal.
- **The REACH over-read persists.** 24 errata rows, mostly symbol-reach corrections, and 4 field refutations
  followed despite the dispatch warning. A symbol-level reach helper in the evidence pack, listing the
  symbols reached from each entry point, would cut this.
