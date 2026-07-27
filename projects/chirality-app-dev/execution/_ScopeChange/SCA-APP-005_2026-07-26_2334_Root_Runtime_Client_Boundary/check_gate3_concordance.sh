#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
decomp="$repo_root/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
matrix="$repo_root/projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/Gate_2_Exhaustive_Seam_Matrix.md"
dgov20="$repo_root/docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md"
context_root="$repo_root/projects/chirality-app-dev/execution"

modified_sows=(009 010 011 012 014 015 016 018 019 020 021 037 038 039 041 044 045 046 047 049 051 052 053 055 056 057 058 059 061 062 063)
modified_packages=(03 04 05 06 08)
modified_deliverables=(03-01 03-02 03-04 04-01 04-02 04-03 04-05 05-01 05-02 05-03 05-05 06-01 06-02 06-05 06-06 08-04 08-05)
modified_objectives=(002 003 004 005 007)

for id in "${modified_sows[@]}"; do
  count="$(rg -c "^\\| SOW-$id \\|" "$decomp")"
  [[ "$count" == "2" ]] || {
    echo "BLOCK: SOW-$id expected SSOW+Ledger rows, found $count"
    exit 1
  }
done

for id in "${modified_packages[@]}"; do
  rg -q "^\\| PKG-$id \\|" "$decomp" || {
    echo "BLOCK: missing PKG-$id"
    exit 1
  }
done

for id in "${modified_deliverables[@]}"; do
  rg -q "^\\| DEL-$id \\|" "$decomp" || {
    echo "BLOCK: missing DEL-$id"
    exit 1
  }
done

for id in "${modified_objectives[@]}"; do
  rg -q "^\\| OBJ-$id \\|" "$decomp" || {
    echo "BLOCK: missing OBJ-$id"
    exit 1
  }
done

rg -Fq 'One opt-in per-user headless daemon exclusively owns runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency.' "$dgov20"
rg -Fq 'Runtime state beneath user data is operational and non-authoritative. Governed project truth, manifests, instructions, AgentRuns, approvals, and acceptance evidence remain checkout-contained.' "$dgov20"
rg -Fq 'Project-specific tools and deterministic acts remain owned by their project/domain adapters and cannot be elevated by generic runtime transport.' "$dgov20"
rg -Fq 'Human acts, release acts, lifecycle transitions, professional reliance, and production-data authority are not delegated by this ruling.' "$dgov20"

rg -Fq 'Root owns the generic contracts, orchestration, daemon, client, CLI, and safe adapters.' "$decomp"
rg -Fq 'Consequential generic runtime changes activate Root `DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance`' "$decomp"
rg -Fq '| DEC-021 | 2026-07-27 |' "$decomp"
if rg -Fq 'app-dev deliverables retain semantic ownership' "$decomp"; then
  echo "BLOCK: stale App semantic-ownership sentence remains"
  exit 1
fi

for unresolved in U1 U2 U3 U4 U5; do
  rg -q "^\\| $unresolved \\|" "$matrix" || {
    echo "BLOCK: missing unresolved seam $unresolved"
    exit 1
  }
done

context_count="$(find "$context_root" -path '*/PKG-03_*/*/_CONTEXT.md' -o -path '*/PKG-04_*/*/_CONTEXT.md' -o -path '*/PKG-05_*/*/_CONTEXT.md' -o -path '*/PKG-06_*/*/_CONTEXT.md' -o -path '*/PKG-08_*/*/_CONTEXT.md' | wc -l | tr -d ' ')"
[[ "$context_count" == "25" ]] || {
  echo "BLOCK: expected 25 affected contexts, found $context_count"
  exit 1
}

root_owned_contexts="$(rg -l 'Root-owned|daemon-owned|daemon operational|Generic runtime|Generic adapters|Generic provider' \
  "$context_root"/PKG-03_*/*/*/_CONTEXT.md \
  "$context_root"/PKG-04_*/*/*/_CONTEXT.md \
  "$context_root"/PKG-05_*/*/*/_CONTEXT.md \
  "$context_root"/PKG-06_*/*/*/_CONTEXT.md \
  "$context_root"/PKG-08_*/*/*/_CONTEXT.md | wc -l | tr -d ' ')"
[[ "$root_owned_contexts" == "25" ]] || {
  echo "BLOCK: expected boundary wording in 25 contexts, found $root_owned_contexts"
  exit 1
}

rg -Fq '| ScopeItemCount | 78 |' "$decomp"
rg -Fq '| PackageCount | 10 |' "$decomp"
rg -Fq '| DeliverableCount | 51 |' "$decomp"
rg -Fq '| ObjectiveCount | 10 |' "$decomp"

echo "PASS: SCA-APP-005 Gate-3 source and entity concordance"
echo "PASS: 31 SOW; 5 PKG; 17 DEL; 5 OBJ; 25 contexts; U1-U5 preserved"
