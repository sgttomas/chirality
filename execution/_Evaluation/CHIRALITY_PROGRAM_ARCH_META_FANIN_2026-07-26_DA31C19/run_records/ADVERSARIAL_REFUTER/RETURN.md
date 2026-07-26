# Adversarial Refutation Return

- **Run status:** `COMPLETE`
- **Engine:** Codex
- **Provider:** OpenAI
- **Model:** `UNKNOWN`
- **Write activity:** none
- **Basis:** `da31c19b5656dd74615e308c4215688971d33dc9`

## Findings

### RF-MAJ-001 — `.pyc` force-add not warranted by evidentiary reliance

The original OD-0 recommended force-adding two ignored bytecode caches solely
because the assembly claimed complete byte preservation. `.gitignore`
deliberately excludes these caches, and the upstream independent package's
own `ARTIFACT_HASHES.sha256` did not include them. The relied source,
validators, reports, manifests, and challenges are preserved independently.

Recommended correction: use a preservation exception, remove the cache bytes
from the durable corpus, retain their observed hashes, and recompute counts.

### RF-MAJ-002 — Option B not gate-ready

The original slate named neither exact carrier IDs nor a fixed expiry and did
not reconcile the deferral carrier with `APP-HOLD-1`.

Recommended correction: make OD-2 route selection only or attach an exact
deferral candidate enumerating carrier IDs, allowed writes, prohibited
reliance, responsibility allocation, fixed expiry, and held-contract
treatment.

### RF-MAJ-003 — Independence and engine disclosure incomplete

Meta-reviewer 1 previously managed the independent-managed package.
Meta-reviewer 2 previously supervised the excluded fourth pass. Root and PEC
source records also identify pass-1 reviewers as `opus-5`, contrary to one
meta-review's reported absence.

Recommended correction: use a per-instance role/engine register, disclose the
prior roles, and distinguish recorded, self-declared, and unknown identities.

### RF-MAJ-004 — `APP-HOLD-1` not enforceable from the slate

The original slate supplied prohibitions without an authoritative register,
required consumer, preflight, rejection condition, exception rule, or closure
tests.

Recommended correction: stage the exact hold mechanism before ruling.

### RF-MAJ-005 — OD-6 and OD-7 could pre-authorize writes

The original language did not explicitly retain separate owning gates for
repin, decision, register, profile, notice, and other file-state work.

Recommended correction: authorize preparation and evidence only and retain
all owning gates.

### RF-MIN-001 — Resource-governance optionality conflated statuses

PEC is an accepted optional product. Resource governance is an unadopted
candidate constrained to remain optional if later proposed.

### RF-MIN-002 — Package PASS needed an identity qualifier

The reproduced values were source-copy identity verdicts, not semantic
validation or lifecycle acceptance.

### RF-INFO-001 — Load-bearing factual layer reproduced

The refuter independently reproduced Root ownership, the Root standing-locus
gap, the App contradiction, the six absent-object pins, the D-APP-48 identity
conflict, twelve stale D-APP-48 source hashes, and the calibrated census
findings.

## Established-conclusion dispositions

| Conclusion | Disposition |
|---|---|
| EC-1 Root ownership ruled; stewardship undecomposed | CONFIRM |
| EC-2 App basis contradicts boundary | CONFIRM |
| EC-3 Runtime active, not dormant | CONFIRM |
| EC-4 PEC optional client; live use unproved | CONFIRM |
| EC-5 Version incompatibility unproved | CONFIRM |
| EC-6 Six App contracts not reliance-clean | CONFIRM |
| EC-7 D-APP-48 stale; D-APP-49 evidence-gated | CONFIRM |
| EC-8 Notice/detector failures specific | CONFIRM |
| EC-9 Positive program floor | NARROW |

## Owner-decision dispositions

| Decision | Disposition |
|---|---|
| OD-0 | REFUTE |
| OD-1 | NARROW |
| OD-2 | NARROW |
| OD-3 | CONFIRM |
| OD-4 | CONFIRM |
| OD-5 | CONFIRM |
| OD-6 | NARROW |
| OD-7 | NARROW |

## Residual unknowns

- Exact Option B carrier, writes, held-contract treatment, and expiry.
- Exact model identity for several historical instances.
- Live PEC use and Piping consumption.
- Protocol-version incompatibility behavior.
- Full deployment/login-start behavior.
- D-APP-49 obligations.
- Semantic consequences of D-APP-48 staleness.
- App SOW validation-era interpretation.

## Initial recommendation

`REFUSE_FANIN` pending correction of RF-MAJ-001 through RF-MAJ-005 and both
minor wording findings.

