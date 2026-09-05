# Semantic Lens: DEL-09-07 Two-Job Runtime-Control Installer Migration and Rollback

**Generated:** 2026-09-05
**DECOMP_VARIANT:** SOFTWARE
**Perspective:** This deliverable frames installer change as an observable, recoverable integration transaction across a separately owned runtime boundary. Its knowledge carries staging, state correspondence, preservation, recovery evidence, and limits of authority while retaining unresolved interface, provenance, and expected-outcome categories as uncertainties.
**Framework:** Chirality Semantic Algebra
**Audit:** PASS
**Phase 2.3 Ruling:** NO_STATUS_TOUCH; lifecycle remains untouched. This lens grants no implementation or release authority.
**Inputs Read:**
- _CONTEXT.md — _CONTEXT.md#description and #authority-boundaries
- _STATUS.md — _STATUS.md#history; OPEN
- _REFERENCES.md — _REFERENCES.md#applicable-references and #notes; pointers read, external contents not followed
- _DEPENDENCIES.md — _DEPENDENCIES.md#extracted-dependency-register-populated-by-taskdependency-extract and #consumer-handoff-notes-optional; final author freeze read
- MEMORY.md — not present
- ScopeOfWork.md — ScopeOfWork.md#deliverable-definition--ontology, #completion-and-reliance-basis--epistemology, #production-and-verification-method--praxeology, #governing-values-and-decisions--axiology; SOW_V1
- Datasheet.md — absent
- Specification.md — absent
- Guidance.md — absent
- Procedure.md — absent
- Decomposition — projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#deliverables; DEL-09-07, SOW-080, OI-003, DEC-024 excerpts read for traceability only

The frozen production contract SHA-256 is `0773d528d62e293443c08229f2933e3d50dcfa3de4d54abcaeb23fc1c2de6ebe`.
The historical declaration layer and later extracted dependency layer are distinguished; observed relationships do not establish satisfaction. Unresolved source states condition the lens without inventing interface details.

## Matrix A — Orientation (3x4) — Canonical

### Result

| | guiding | applying | judging | reviewing |
|---|---|---|---|---|
| normative | prescriptive direction | mandatory practice | compliance determination | regulatory audit |
| operative | procedural direction | practical execution | performance assessment | process audit |
| evaluative | value orientation | merit application | worth determination | quality appraisal |

## Matrix B — Conceptualization (4x4) — Canonical

### Result

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| data | essential fact | adequate evidence | comprehensive record | reliable measurement |
| information | essential signal | adequate context | comprehensive account | coherent message |
| knowledge | fundamental understanding | competent expertise | thorough mastery | coherent understanding |
| wisdom | essential discernment | adequate judgment | holistic insight | principled reasoning |

## Matrix C — Formulation (3x4)

### Construction: Dot product A · B

`L_C(i,j) = Σ_k (A(i,k) * B(k,j)); C(i,j) = I(row_i, col_j, L_C(i,j))`.
In each work row the resolved products are numbered t1 onward. The symbol a denotes that row's resolved axis anchor; each projection explicitly resolves a * tn.

| Cell | Intermediate collection | Step 1 - Axis anchor | Step 2 - Projected contributors | Step 3 - Centroid attractor |
|---|---|---|---|---|
| C[normative,necessity] | t1 = prescriptive direction * essential fact = ownership premise; t2 = mandatory practice * essential signal = control obligation; t3 = compliance determination * fundamental understanding = boundary rationale; t4 = regulatory audit * essential discernment = authority distinction | a = normative * necessity = binding prerequisite | p1 = a * t1 = binding prerequisite * ownership premise = owner mandate; p2 = a * t2 = binding prerequisite * control obligation = permitted control; p3 = a * t3 = binding prerequisite * boundary rationale = scoped obligation; p4 = a * t4 = binding prerequisite * authority distinction = permission boundary | centroid selects authority boundary |
| C[normative,sufficiency] | t1 = prescriptive direction * adequate evidence = mandate support; t2 = mandatory practice * adequate context = scoped procedure; t3 = compliance determination * competent expertise = conformance interpretation; t4 = regulatory audit * adequate judgment = bounded assurance | a = normative * sufficiency = warranted obligation | p1 = a * t1 = warranted obligation * mandate support = permission support; p2 = a * t2 = warranted obligation * scoped procedure = contract applicability; p3 = a * t3 = warranted obligation * conformance interpretation = contract interpretation; p4 = a * t4 = warranted obligation * bounded assurance = scoped warrant | centroid selects contract warrant |
| C[normative,completeness] | t1 = prescriptive direction * comprehensive record = mandate inventory; t2 = mandatory practice * comprehensive account = duty coverage; t3 = compliance determination * thorough mastery = boundary coverage; t4 = regulatory audit * holistic insight = authority overview | a = normative * completeness = exhaustive obligation | p1 = a * t1 = exhaustive obligation * mandate inventory = obligation inventory; p2 = a * t2 = exhaustive obligation * duty coverage = transaction duty span; p3 = a * t3 = exhaustive obligation * boundary coverage = ownership span; p4 = a * t4 = exhaustive obligation * authority overview = mandate scope | centroid selects obligation coverage |
| C[normative,consistency] | t1 = prescriptive direction * reliable measurement = stable rule observation; t2 = mandatory practice * coherent message = aligned instruction; t3 = compliance determination * coherent understanding = shared interpretation; t4 = regulatory audit * principled reasoning = rule coherence | a = normative * consistency = aligned obligation | p1 = a * t1 = aligned obligation * stable rule observation = repeatable boundary reading; p2 = a * t2 = aligned obligation * aligned instruction = unified mandate; p3 = a * t3 = aligned obligation * shared interpretation = common contract meaning; p4 = a * t4 = aligned obligation * rule coherence = authority agreement | centroid selects contract coherence |
| C[operative,necessity] | t1 = procedural direction * essential fact = staging premise; t2 = practical execution * essential signal = transition trigger; t3 = performance assessment * fundamental understanding = outcome interpretation; t4 = process audit * essential discernment = recovery distinction | a = operative * necessity = execution prerequisite | p1 = a * t1 = execution prerequisite * staging premise = staging input; p2 = a * t2 = execution prerequisite * transition trigger = transition condition; p3 = a * t3 = execution prerequisite * outcome interpretation = observable outcome; p4 = a * t4 = execution prerequisite * recovery distinction = recoverable state | centroid selects transaction precondition |
| C[operative,sufficiency] | t1 = procedural direction * adequate evidence = supported procedure; t2 = practical execution * adequate context = situated transition; t3 = performance assessment * competent expertise = outcome appraisal; t4 = process audit * adequate judgment = execution warrant | a = operative * sufficiency = supported execution | p1 = a * t1 = supported execution * supported procedure = procedure evidence; p2 = a * t2 = supported execution * situated transition = transition evidence; p3 = a * t3 = supported execution * outcome appraisal = outcome evidence; p4 = a * t4 = supported execution * execution warrant = bounded execution proof | centroid selects transaction evidence |
| C[operative,completeness] | t1 = procedural direction * comprehensive record = transition inventory; t2 = practical execution * comprehensive account = execution narrative; t3 = performance assessment * thorough mastery = outcome coverage; t4 = process audit * holistic insight = lifecycle overview | a = operative * completeness = end-to-end execution | p1 = a * t1 = end-to-end execution * transition inventory = transition span; p2 = a * t2 = end-to-end execution * execution narrative = transaction history; p3 = a * t3 = end-to-end execution * outcome coverage = recovery span; p4 = a * t4 = end-to-end execution * lifecycle overview = lifecycle coverage | centroid selects transaction coverage |
| C[operative,consistency] | t1 = procedural direction * reliable measurement = repeatable observation; t2 = practical execution * coherent message = trace alignment; t3 = performance assessment * coherent understanding = outcome correspondence; t4 = process audit * principled reasoning = reconciliation rationale | a = operative * consistency = repeatable execution | p1 = a * t1 = repeatable execution * repeatable observation = stable state observation; p2 = a * t2 = repeatable execution * trace alignment = journal alignment; p3 = a * t3 = repeatable execution * outcome correspondence = state correspondence; p4 = a * t4 = repeatable execution * reconciliation rationale = reconciliation coherence | centroid selects state correspondence |
| C[evaluative,necessity] | t1 = value orientation * essential fact = preservation stake; t2 = merit application * essential signal = recovery relevance; t3 = worth determination * fundamental understanding = preservation rationale; t4 = quality appraisal * essential discernment = loss distinction | a = evaluative * necessity = fundamental worth | p1 = a * t1 = fundamental worth * preservation stake = retained value; p2 = a * t2 = fundamental worth * recovery relevance = recovery purpose; p3 = a * t3 = fundamental worth * preservation rationale = continuity purpose; p4 = a * t4 = fundamental worth * loss distinction = preservation priority | centroid selects preservation purpose |
| C[evaluative,sufficiency] | t1 = value orientation * adequate evidence = supported value; t2 = merit application * adequate context = situated benefit; t3 = worth determination * competent expertise = informed appraisal; t4 = quality appraisal * adequate judgment = qualified confidence | a = evaluative * sufficiency = warranted worth | p1 = a * t1 = warranted worth * supported value = preservation support; p2 = a * t2 = warranted worth * situated benefit = bounded recovery benefit; p3 = a * t3 = warranted worth * informed appraisal = evidence-based appraisal; p4 = a * t4 = warranted worth * qualified confidence = limited confidence | centroid selects recovery confidence |
| C[evaluative,completeness] | t1 = value orientation * comprehensive record = value inventory; t2 = merit application * comprehensive account = benefit account; t3 = worth determination * thorough mastery = tradeoff comprehension; t4 = quality appraisal * holistic insight = consequence overview | a = evaluative * completeness = whole consequence | p1 = a * t1 = whole consequence * value inventory = preservation dimensions; p2 = a * t2 = whole consequence * benefit account = recovery effects; p3 = a * t3 = whole consequence * tradeoff comprehension = lifecycle tradeoffs; p4 = a * t4 = whole consequence * consequence overview = consequence coverage | centroid selects lifecycle consequence |
| C[evaluative,consistency] | t1 = value orientation * reliable measurement = stable appraisal basis; t2 = merit application * coherent message = value alignment; t3 = worth determination * coherent understanding = shared appraisal; t4 = quality appraisal * principled reasoning = principled valuation | a = evaluative * consistency = coherent worth | p1 = a * t1 = coherent worth * stable appraisal basis = comparable observations; p2 = a * t2 = coherent worth * value alignment = preservation alignment; p3 = a * t3 = coherent worth * shared appraisal = shared recovery meaning; p4 = a * t4 = coherent worth * principled valuation = sustained trust | centroid selects evidence trust |

### Result

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| normative | authority boundary | contract warrant | obligation coverage | contract coherence |
| operative | transaction precondition | transaction evidence | transaction coverage | state correspondence |
| evaluative | preservation purpose | recovery confidence | lifecycle consequence | evidence trust |

## Matrix F — Requirements (3x4)

### Construction: Dot product C · B

`L_F(i,j) = Σ_k (C(i,k) * B(k,j)); F(i,j) = I(row_i, col_j, L_F(i,j))`.

| Cell | Intermediate collection | Step 1 - Axis anchor | Step 2 - Projected contributors | Step 3 - Centroid attractor |
|---|---|---|---|---|
| F[normative,necessity] | t1 = authority boundary * essential fact = owner identity; t2 = contract warrant * essential signal = permission signal; t3 = obligation coverage * fundamental understanding = duty basis; t4 = contract coherence * essential discernment = boundary distinction | a = normative * necessity = binding prerequisite | p1 = a * t1 = binding prerequisite * owner identity = ownership prerequisite; p2 = a * t2 = binding prerequisite * permission signal = authority prerequisite; p3 = a * t3 = binding prerequisite * duty basis = scoped prerequisite; p4 = a * t4 = binding prerequisite * boundary distinction = permission limit | centroid selects authorized input |
| F[normative,sufficiency] | t1 = authority boundary * adequate evidence = boundary support; t2 = contract warrant * adequate context = warrant scope; t3 = obligation coverage * competent expertise = duty interpretation; t4 = contract coherence * adequate judgment = source adjudication | a = normative * sufficiency = warranted obligation | p1 = a * t1 = warranted obligation * boundary support = mandate evidence; p2 = a * t2 = warranted obligation * warrant scope = source applicability; p3 = a * t3 = warranted obligation * duty interpretation = source interpretation; p4 = a * t4 = warranted obligation * source adjudication = qualified source warrant | centroid selects source qualification |
| F[normative,completeness] | t1 = authority boundary * comprehensive record = owner inventory; t2 = contract warrant * comprehensive account = warrant account; t3 = obligation coverage * thorough mastery = obligation mastery; t4 = contract coherence * holistic insight = contract overview | a = normative * completeness = exhaustive obligation | p1 = a * t1 = exhaustive obligation * owner inventory = boundary inventory; p2 = a * t2 = exhaustive obligation * warrant account = authority trace; p3 = a * t3 = exhaustive obligation * obligation mastery = duty trace; p4 = a * t4 = exhaustive obligation * contract overview = contract span | centroid selects boundary traceability |
| F[normative,consistency] | t1 = authority boundary * reliable measurement = boundary observation; t2 = contract warrant * coherent message = warrant alignment; t3 = obligation coverage * coherent understanding = duty agreement; t4 = contract coherence * principled reasoning = authority rationale | a = normative * consistency = aligned obligation | p1 = a * t1 = aligned obligation * boundary observation = stable owner reading; p2 = a * t2 = aligned obligation * warrant alignment = source agreement; p3 = a * t3 = aligned obligation * duty agreement = duty alignment; p4 = a * t4 = aligned obligation * authority rationale = unified authority meaning | centroid selects authority alignment |
| F[operative,necessity] | t1 = transaction precondition * essential fact = initial state; t2 = transaction evidence * essential signal = outcome signal; t3 = transaction coverage * fundamental understanding = transition model; t4 = state correspondence * essential discernment = discrepancy distinction | a = operative * necessity = execution prerequisite | p1 = a * t1 = execution prerequisite * initial state = state prerequisite; p2 = a * t2 = execution prerequisite * outcome signal = observation prerequisite; p3 = a * t3 = execution prerequisite * transition model = transition basis; p4 = a * t4 = execution prerequisite * discrepancy distinction = unresolved-state distinction | centroid selects observable transition |
| F[operative,sufficiency] | t1 = transaction precondition * adequate evidence = starting-state support; t2 = transaction evidence * adequate context = trace context; t3 = transaction coverage * competent expertise = fixture interpretation; t4 = state correspondence * adequate judgment = reconciliation judgment | a = operative * sufficiency = supported execution | p1 = a * t1 = supported execution * starting-state support = initial-state proof; p2 = a * t2 = supported execution * trace context = bounded trace; p3 = a * t3 = supported execution * fixture interpretation = fixture proof; p4 = a * t4 = supported execution * reconciliation judgment = state proof limits | centroid selects outcome support |
| F[operative,completeness] | t1 = transaction precondition * comprehensive record = prerequisite inventory; t2 = transaction evidence * comprehensive account = transaction account; t3 = transaction coverage * thorough mastery = recovery comprehension; t4 = state correspondence * holistic insight = state overview | a = operative * completeness = end-to-end execution | p1 = a * t1 = end-to-end execution * prerequisite inventory = initial-condition span; p2 = a * t2 = end-to-end execution * transaction account = transition span; p3 = a * t3 = end-to-end execution * recovery comprehension = recovery span; p4 = a * t4 = end-to-end execution * state overview = resulting-state span | centroid selects lifecycle trace |
| F[operative,consistency] | t1 = transaction precondition * reliable measurement = repeatable initial state; t2 = transaction evidence * coherent message = aligned outcome trace; t3 = transaction coverage * coherent understanding = shared transition meaning; t4 = state correspondence * principled reasoning = reconciliation basis | a = operative * consistency = repeatable execution | p1 = a * t1 = repeatable execution * repeatable initial state = comparable starting state; p2 = a * t2 = repeatable execution * aligned outcome trace = trace agreement; p3 = a * t3 = repeatable execution * shared transition meaning = outcome agreement; p4 = a * t4 = repeatable execution * reconciliation basis = discrepancy accounting | centroid selects reconciliation basis |
| F[evaluative,necessity] | t1 = preservation purpose * essential fact = valued state; t2 = recovery confidence * essential signal = recovery indication; t3 = lifecycle consequence * fundamental understanding = consequence basis; t4 = evidence trust * essential discernment = claim distinction | a = evaluative * necessity = fundamental worth | p1 = a * t1 = fundamental worth * valued state = continuity stake; p2 = a * t2 = fundamental worth * recovery indication = recovery stake; p3 = a * t3 = fundamental worth * consequence basis = preservation stake; p4 = a * t4 = fundamental worth * claim distinction = bounded recovery claim | centroid selects continuity stake |
| F[evaluative,sufficiency] | t1 = preservation purpose * adequate evidence = preservation support; t2 = recovery confidence * adequate context = confidence context; t3 = lifecycle consequence * competent expertise = consequence appraisal; t4 = evidence trust * adequate judgment = calibrated trust | a = evaluative * sufficiency = warranted worth | p1 = a * t1 = warranted worth * preservation support = supported preservation claim; p2 = a * t2 = warranted worth * confidence context = contextual confidence; p3 = a * t3 = warranted worth * consequence appraisal = bounded consequence claim; p4 = a * t4 = warranted worth * calibrated trust = confidence limit | centroid selects claim calibration |
| F[evaluative,completeness] | t1 = preservation purpose * comprehensive record = preservation inventory; t2 = recovery confidence * comprehensive account = recovery account; t3 = lifecycle consequence * thorough mastery = consequence comprehension; t4 = evidence trust * holistic insight = assurance overview | a = evaluative * completeness = whole consequence | p1 = a * t1 = whole consequence * preservation inventory = retained-state span; p2 = a * t2 = whole consequence * recovery account = recovery-effect span; p3 = a * t3 = whole consequence * consequence comprehension = tradeoff span; p4 = a * t4 = whole consequence * assurance overview = claim-limit span | centroid selects consequence coverage |
| F[evaluative,consistency] | t1 = preservation purpose * reliable measurement = stable preservation observation; t2 = recovery confidence * coherent message = aligned confidence; t3 = lifecycle consequence * coherent understanding = shared consequence meaning; t4 = evidence trust * principled reasoning = trust rationale | a = evaluative * consistency = coherent worth | p1 = a * t1 = coherent worth * stable preservation observation = comparable preservation basis; p2 = a * t2 = coherent worth * aligned confidence = balanced confidence; p3 = a * t3 = coherent worth * shared consequence meaning = appraisal agreement; p4 = a * t4 = coherent worth * trust rationale = defensible appraisal | centroid selects appraisal coherence |

### Result

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| normative | authorized input | source qualification | boundary traceability | authority alignment |
| operative | observable transition | outcome support | lifecycle trace | reconciliation basis |
| evaluative | continuity stake | claim calibration | consequence coverage | appraisal coherence |

## Matrix D — Objectives (3x4)

### Construction: Resolution overlay

`L_D(i,j) = A(i,j) + (resolution * F(i,j)); D(i,j) = I(row_i, col_j, L_D(i,j))`.
Resolution means making the semantic obligation discriminable at the integration boundary, without choosing unresolved implementation particulars. Each collection has exactly two contributors, t1 from A and t2 from the resolved transformation of F.

| Cell | Intermediate collection | Step 1 - Axis anchor | Step 2 - Projected contributors | Step 3 - Centroid attractor |
|---|---|---|---|---|
| D[normative,guiding] | t1 = prescriptive direction; t2 = resolution * authorized input = bounded mandate; L = t1 + t2 | a = normative * guiding = mandated direction | p1 = a * t1 = mandated direction * prescriptive direction = authority orientation; p2 = a * t2 = mandated direction * bounded mandate = scoped authority | centroid selects authority orientation |
| D[normative,applying] | t1 = mandatory practice; t2 = resolution * source qualification = qualified contract use; L = t1 + t2 | a = normative * applying = enacted obligation | p1 = a * t1 = enacted obligation * mandatory practice = prescribed conformance; p2 = a * t2 = enacted obligation * qualified contract use = source-bound conformance | centroid selects contract conformance |
| D[normative,judging] | t1 = compliance determination; t2 = resolution * boundary traceability = inspectable ownership trace; L = t1 + t2 | a = normative * judging = obligation determination | p1 = a * t1 = obligation determination * compliance determination = boundary determination; p2 = a * t2 = obligation determination * inspectable ownership trace = ownership accounting | centroid selects boundary accounting |
| D[normative,reviewing] | t1 = regulatory audit; t2 = resolution * authority alignment = explicit mandate agreement; L = t1 + t2 | a = normative * reviewing = mandate scrutiny | p1 = a * t1 = mandate scrutiny * regulatory audit = authority examination; p2 = a * t2 = mandate scrutiny * explicit mandate agreement = mandate comparison | centroid selects authority scrutiny |
| D[operative,guiding] | t1 = procedural direction; t2 = resolution * observable transition = inspectable change model; L = t1 + t2 | a = operative * guiding = procedural orientation | p1 = a * t1 = procedural orientation * procedural direction = transition orientation; p2 = a * t2 = procedural orientation * inspectable change model = state-change framing | centroid selects transition framing |
| D[operative,applying] | t1 = practical execution; t2 = resolution * outcome support = source-bound observation; L = t1 + t2 | a = operative * applying = enacted procedure | p1 = a * t1 = enacted procedure * practical execution = transaction enactment; p2 = a * t2 = enacted procedure * source-bound observation = observed enactment | centroid selects observed transaction |
| D[operative,judging] | t1 = performance assessment; t2 = resolution * lifecycle trace = inspectable outcome chain; L = t1 + t2 | a = operative * judging = outcome assessment | p1 = a * t1 = outcome assessment * performance assessment = transition assessment; p2 = a * t2 = outcome assessment * inspectable outcome chain = outcome accounting | centroid selects outcome accounting |
| D[operative,reviewing] | t1 = process audit; t2 = resolution * reconciliation basis = explicit discrepancy relation; L = t1 + t2 | a = operative * reviewing = process scrutiny | p1 = a * t1 = process scrutiny * process audit = trace examination; p2 = a * t2 = process scrutiny * explicit discrepancy relation = discrepancy examination | centroid selects reconciliation scrutiny |
| D[evaluative,guiding] | t1 = value orientation; t2 = resolution * continuity stake = explicit preservation purpose; L = t1 + t2 | a = evaluative * guiding = worth orientation | p1 = a * t1 = worth orientation * value orientation = preservation orientation; p2 = a * t2 = worth orientation * explicit preservation purpose = continuity orientation | centroid selects preservation orientation |
| D[evaluative,applying] | t1 = merit application; t2 = resolution * claim calibration = bounded recovery appraisal; L = t1 + t2 | a = evaluative * applying = situated valuation | p1 = a * t1 = situated valuation * merit application = contextual appraisal; p2 = a * t2 = situated valuation * bounded recovery appraisal = bounded benefit appraisal | centroid selects recovery appraisal |
| D[evaluative,judging] | t1 = worth determination; t2 = resolution * consequence coverage = explicit effect span; L = t1 + t2 | a = evaluative * judging = value determination | p1 = a * t1 = value determination * worth determination = consequence appraisal; p2 = a * t2 = value determination * explicit effect span = effect accounting | centroid selects consequence accounting |
| D[evaluative,reviewing] | t1 = quality appraisal; t2 = resolution * appraisal coherence = comparable claim basis; L = t1 + t2 | a = evaluative * reviewing = value scrutiny | p1 = a * t1 = value scrutiny * quality appraisal = confidence examination; p2 = a * t2 = value scrutiny * comparable claim basis = claim comparison | centroid selects confidence scrutiny |

### Result

| | guiding | applying | judging | reviewing |
|---|---|---|---|---|
| normative | authority orientation | contract conformance | boundary accounting | authority scrutiny |
| operative | transition framing | observed transaction | outcome accounting | reconciliation scrutiny |
| evaluative | preservation orientation | recovery appraisal | consequence accounting | confidence scrutiny |

## Matrix K — Transpose of D (4x3)

`K(i,j) = D(j,i)`. Every cell is transferred unchanged.

### Result

| | normative | operative | evaluative |
|---|---|---|---|
| guiding | authority orientation | transition framing | preservation orientation |
| applying | contract conformance | observed transaction | recovery appraisal |
| judging | boundary accounting | outcome accounting | consequence accounting |
| reviewing | authority scrutiny | reconciliation scrutiny | confidence scrutiny |

## Matrix G — Truncation of B (3x4)

Remove the `wisdom` row from B; retain the remaining cells unchanged.

### Result

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| data | essential fact | adequate evidence | comprehensive record | reliable measurement |
| information | essential signal | adequate context | comprehensive account | coherent message |
| knowledge | fundamental understanding | competent expertise | thorough mastery | coherent understanding |

## Matrix X — Verification (4x4)

### Construction: Dot product K · G

`L_X(i,j) = Σ_k (K(i,k) * G(k,j)); X(i,j) = I(row_i, col_j, L_X(i,j))`.

| Cell | Intermediate collection | Step 1 - Axis anchor | Step 2 - Projected contributors | Step 3 - Centroid attractor |
|---|---|---|---|---|
| X[guiding,necessity] | t1 = authority orientation * essential fact = mandate premise; t2 = transition framing * essential signal = change indication; t3 = preservation orientation * fundamental understanding = continuity rationale | a = guiding * necessity = directional prerequisite | p1 = a * t1 = directional prerequisite * mandate premise = source prerequisite; p2 = a * t2 = directional prerequisite * change indication = transition prerequisite; p3 = a * t3 = directional prerequisite * continuity rationale = preservation prerequisite | centroid selects integration premise |
| X[guiding,sufficiency] | t1 = authority orientation * adequate evidence = source support; t2 = transition framing * adequate context = transition context; t3 = preservation orientation * competent expertise = preservation interpretation | a = guiding * sufficiency = supported direction | p1 = a * t1 = supported direction * source support = mandate support; p2 = a * t2 = supported direction * transition context = model support; p3 = a * t3 = supported direction * preservation interpretation = purpose support | centroid selects integration rationale |
| X[guiding,completeness] | t1 = authority orientation * comprehensive record = mandate inventory; t2 = transition framing * comprehensive account = transition account; t3 = preservation orientation * thorough mastery = preservation comprehension | a = guiding * completeness = whole orientation | p1 = a * t1 = whole orientation * mandate inventory = authority span; p2 = a * t2 = whole orientation * transition account = change span; p3 = a * t3 = whole orientation * preservation comprehension = preservation span | centroid selects integration horizon |
| X[guiding,consistency] | t1 = authority orientation * reliable measurement = stable mandate reading; t2 = transition framing * coherent message = aligned change model; t3 = preservation orientation * coherent understanding = shared continuity purpose | a = guiding * consistency = aligned direction | p1 = a * t1 = aligned direction * stable mandate reading = source alignment; p2 = a * t2 = aligned direction * aligned change model = model alignment; p3 = a * t3 = aligned direction * shared continuity purpose = purpose alignment | centroid selects integration alignment |
| X[applying,necessity] | t1 = contract conformance * essential fact = contract premise; t2 = observed transaction * essential signal = state indication; t3 = recovery appraisal * fundamental understanding = recovery basis | a = applying * necessity = enactment prerequisite | p1 = a * t1 = enactment prerequisite * contract premise = permission condition; p2 = a * t2 = enactment prerequisite * state indication = observation condition; p3 = a * t3 = enactment prerequisite * recovery basis = recovery condition | centroid selects transaction grounding |
| X[applying,sufficiency] | t1 = contract conformance * adequate evidence = conformance evidence; t2 = observed transaction * adequate context = situated trace; t3 = recovery appraisal * competent expertise = recovery interpretation | a = applying * sufficiency = supported enactment | p1 = a * t1 = supported enactment * conformance evidence = contract support; p2 = a * t2 = supported enactment * situated trace = outcome support; p3 = a * t3 = supported enactment * recovery interpretation = recovery support | centroid selects transaction warrant |
| X[applying,completeness] | t1 = contract conformance * comprehensive record = conformance inventory; t2 = observed transaction * comprehensive account = transaction narrative; t3 = recovery appraisal * thorough mastery = recovery comprehension | a = applying * completeness = whole enactment | p1 = a * t1 = whole enactment * conformance inventory = boundary coverage; p2 = a * t2 = whole enactment * transaction narrative = outcome coverage; p3 = a * t3 = whole enactment * recovery comprehension = recovery coverage | centroid selects transaction span |
| X[applying,consistency] | t1 = contract conformance * reliable measurement = repeatable conformance observation; t2 = observed transaction * coherent message = aligned trace; t3 = recovery appraisal * coherent understanding = shared recovery meaning | a = applying * consistency = aligned enactment | p1 = a * t1 = aligned enactment * repeatable conformance observation = stable boundary observation; p2 = a * t2 = aligned enactment * aligned trace = trace correspondence; p3 = a * t3 = aligned enactment * shared recovery meaning = recovery correspondence | centroid selects transaction correspondence |
| X[judging,necessity] | t1 = boundary accounting * essential fact = ownership fact; t2 = outcome accounting * essential signal = outcome indication; t3 = consequence accounting * fundamental understanding = effect rationale | a = judging * necessity = assessment prerequisite | p1 = a * t1 = assessment prerequisite * ownership fact = boundary basis; p2 = a * t2 = assessment prerequisite * outcome indication = observation basis; p3 = a * t3 = assessment prerequisite * effect rationale = consequence basis | centroid selects assessment grounding |
| X[judging,sufficiency] | t1 = boundary accounting * adequate evidence = ownership evidence; t2 = outcome accounting * adequate context = outcome context; t3 = consequence accounting * competent expertise = effect interpretation | a = judging * sufficiency = supported assessment | p1 = a * t1 = supported assessment * ownership evidence = boundary support; p2 = a * t2 = supported assessment * outcome context = outcome support; p3 = a * t3 = supported assessment * effect interpretation = consequence support | centroid selects assessment warrant |
| X[judging,completeness] | t1 = boundary accounting * comprehensive record = boundary inventory; t2 = outcome accounting * comprehensive account = outcome history; t3 = consequence accounting * thorough mastery = effect comprehension | a = judging * completeness = whole assessment | p1 = a * t1 = whole assessment * boundary inventory = ownership span; p2 = a * t2 = whole assessment * outcome history = observation span; p3 = a * t3 = whole assessment * effect comprehension = consequence span | centroid selects assessment coverage |
| X[judging,consistency] | t1 = boundary accounting * reliable measurement = stable owner observation; t2 = outcome accounting * coherent message = aligned outcome account; t3 = consequence accounting * coherent understanding = shared effect meaning | a = judging * consistency = aligned assessment | p1 = a * t1 = aligned assessment * stable owner observation = boundary comparability; p2 = a * t2 = aligned assessment * aligned outcome account = outcome comparability; p3 = a * t3 = aligned assessment * shared effect meaning = consequence comparability | centroid selects assessment comparability |
| X[reviewing,necessity] | t1 = authority scrutiny * essential fact = source premise; t2 = reconciliation scrutiny * essential signal = discrepancy indication; t3 = confidence scrutiny * fundamental understanding = claim rationale | a = reviewing * necessity = examination prerequisite | p1 = a * t1 = examination prerequisite * source premise = source provenance; p2 = a * t2 = examination prerequisite * discrepancy indication = discrepancy provenance; p3 = a * t3 = examination prerequisite * claim rationale = claim provenance | centroid selects scrutiny provenance |
| X[reviewing,sufficiency] | t1 = authority scrutiny * adequate evidence = authority support; t2 = reconciliation scrutiny * adequate context = discrepancy context; t3 = confidence scrutiny * competent expertise = claim interpretation | a = reviewing * sufficiency = supported examination | p1 = a * t1 = supported examination * authority support = source warrant; p2 = a * t2 = supported examination * discrepancy context = reconciliation warrant; p3 = a * t3 = supported examination * claim interpretation = calibrated warrant | centroid selects scrutiny warrant |
| X[reviewing,completeness] | t1 = authority scrutiny * comprehensive record = source inventory; t2 = reconciliation scrutiny * comprehensive account = discrepancy account; t3 = confidence scrutiny * thorough mastery = claim comprehension | a = reviewing * completeness = whole examination | p1 = a * t1 = whole examination * source inventory = source coverage; p2 = a * t2 = whole examination * discrepancy account = unresolved-state coverage; p3 = a * t3 = whole examination * claim comprehension = claim-limit coverage | centroid selects scrutiny coverage |
| X[reviewing,consistency] | t1 = authority scrutiny * reliable measurement = stable source observation; t2 = reconciliation scrutiny * coherent message = aligned discrepancy account; t3 = confidence scrutiny * coherent understanding = shared claim meaning | a = reviewing * consistency = aligned examination | p1 = a * t1 = aligned examination * stable source observation = source comparability; p2 = a * t2 = aligned examination * aligned discrepancy account = discrepancy comparability; p3 = a * t3 = aligned examination * shared claim meaning = claim comparability | centroid selects scrutiny coherence |

### Result

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| guiding | integration premise | integration rationale | integration horizon | integration alignment |
| applying | transaction grounding | transaction warrant | transaction span | transaction correspondence |
| judging | assessment grounding | assessment warrant | assessment coverage | assessment comparability |
| reviewing | scrutiny provenance | scrutiny warrant | scrutiny coverage | scrutiny coherence |

## Matrix T — Transpose of B (4x4)

`T(i,j) = B(j,i)`. Every cell is transferred unchanged.

### Result

| | data | information | knowledge | wisdom |
|---|---|---|---|---|
| necessity | essential fact | essential signal | fundamental understanding | essential discernment |
| sufficiency | adequate evidence | adequate context | competent expertise | adequate judgment |
| completeness | comprehensive record | comprehensive account | thorough mastery | holistic insight |
| consistency | reliable measurement | coherent message | coherent understanding | principled reasoning |

## Matrix E — Evaluation (4x4)

### Construction: Dot product X · T

`L_E(i,j) = Σ_k (X(i,k) * T(k,j)); E(i,j) = I(row_i, col_j, L_E(i,j))`.

| Cell | Intermediate collection | Step 1 - Axis anchor | Step 2 - Projected contributors | Step 3 - Centroid attractor |
|---|---|---|---|---|
| E[guiding,data] | t1 = integration premise * essential fact = boundary premise; t2 = integration rationale * adequate evidence = integration support; t3 = integration horizon * comprehensive record = integration inventory; t4 = integration alignment * reliable measurement = stable integration observation | a = guiding * data = orienting observation | p1 = a * t1 = orienting observation * boundary premise = source observation; p2 = a * t2 = orienting observation * integration support = supporting observation; p3 = a * t3 = orienting observation * integration inventory = observation inventory; p4 = a * t4 = orienting observation * stable integration observation = repeatable observation basis | centroid selects integration evidence |
| E[guiding,information] | t1 = integration premise * essential signal = boundary indication; t2 = integration rationale * adequate context = integration context; t3 = integration horizon * comprehensive account = integration account; t4 = integration alignment * coherent message = aligned integration narrative | a = guiding * information = orienting account | p1 = a * t1 = orienting account * boundary indication = boundary context; p2 = a * t2 = orienting account * integration context = source context; p3 = a * t3 = orienting account * integration account = lifecycle context; p4 = a * t4 = orienting account * aligned integration narrative = common integration context | centroid selects integration context |
| E[guiding,knowledge] | t1 = integration premise * fundamental understanding = boundary comprehension; t2 = integration rationale * competent expertise = integration interpretation; t3 = integration horizon * thorough mastery = lifecycle comprehension; t4 = integration alignment * coherent understanding = shared integration meaning | a = guiding * knowledge = informed orientation | p1 = a * t1 = informed orientation * boundary comprehension = ownership model; p2 = a * t2 = informed orientation * integration interpretation = transition model; p3 = a * t3 = informed orientation * lifecycle comprehension = lifecycle model; p4 = a * t4 = informed orientation * shared integration meaning = common integration model | centroid selects integration model |
| E[guiding,wisdom] | t1 = integration premise * essential discernment = premise distinction; t2 = integration rationale * adequate judgment = bounded integration judgment; t3 = integration horizon * holistic insight = integration consequence; t4 = integration alignment * principled reasoning = integration principle | a = guiding * wisdom = discerning orientation | p1 = a * t1 = discerning orientation * premise distinction = authority distinction; p2 = a * t2 = discerning orientation * bounded integration judgment = claim limitation; p3 = a * t3 = discerning orientation * integration consequence = preservation perspective; p4 = a * t4 = discerning orientation * integration principle = accountable stewardship | centroid selects integration stewardship |
| E[applying,data] | t1 = transaction grounding * essential fact = transaction premise; t2 = transaction warrant * adequate evidence = transaction support; t3 = transaction span * comprehensive record = transaction inventory; t4 = transaction correspondence * reliable measurement = repeatable state observation | a = applying * data = enacted observation | p1 = a * t1 = enacted observation * transaction premise = starting-state observation; p2 = a * t2 = enacted observation * transaction support = outcome observation; p3 = a * t3 = enacted observation * transaction inventory = trace inventory; p4 = a * t4 = enacted observation * repeatable state observation = comparable state trace | centroid selects transaction observations |
| E[applying,information] | t1 = transaction grounding * essential signal = transition indication; t2 = transaction warrant * adequate context = trace context; t3 = transaction span * comprehensive account = transition account; t4 = transaction correspondence * coherent message = aligned state account | a = applying * information = enacted account | p1 = a * t1 = enacted account * transition indication = transition narrative; p2 = a * t2 = enacted account * trace context = situated narrative; p3 = a * t3 = enacted account * transition account = lifecycle narrative; p4 = a * t4 = enacted account * aligned state account = reconciled narrative | centroid selects transaction narrative |
| E[applying,knowledge] | t1 = transaction grounding * fundamental understanding = transition basis; t2 = transaction warrant * competent expertise = transaction interpretation; t3 = transaction span * thorough mastery = recovery comprehension; t4 = transaction correspondence * coherent understanding = shared state meaning | a = applying * knowledge = informed enactment | p1 = a * t1 = informed enactment * transition basis = transition comprehension; p2 = a * t2 = informed enactment * transaction interpretation = outcome comprehension; p3 = a * t3 = informed enactment * recovery comprehension = recovery model; p4 = a * t4 = informed enactment * shared state meaning = correspondence model | centroid selects transaction comprehension |
| E[applying,wisdom] | t1 = transaction grounding * essential discernment = transaction distinction; t2 = transaction warrant * adequate judgment = bounded transaction judgment; t3 = transaction span * holistic insight = lifecycle insight; t4 = transaction correspondence * principled reasoning = reconciliation principle | a = applying * wisdom = discerning enactment | p1 = a * t1 = discerning enactment * transaction distinction = unresolved-outcome distinction; p2 = a * t2 = discerning enactment * bounded transaction judgment = qualified outcome claim; p3 = a * t3 = discerning enactment * lifecycle insight = preservation perspective; p4 = a * t4 = discerning enactment * reconciliation principle = accountable recovery | centroid selects recovery stewardship |
| E[judging,data] | t1 = assessment grounding * essential fact = appraisal premise; t2 = assessment warrant * adequate evidence = appraisal support; t3 = assessment coverage * comprehensive record = appraisal inventory; t4 = assessment comparability * reliable measurement = comparable observation | a = judging * data = assessed observation | p1 = a * t1 = assessed observation * appraisal premise = baseline observation; p2 = a * t2 = assessed observation * appraisal support = supporting observation; p3 = a * t3 = assessed observation * appraisal inventory = outcome inventory; p4 = a * t4 = assessed observation * comparable observation = repeatable appraisal basis | centroid selects outcome evidence |
| E[judging,information] | t1 = assessment grounding * essential signal = outcome indication; t2 = assessment warrant * adequate context = appraisal context; t3 = assessment coverage * comprehensive account = appraisal account; t4 = assessment comparability * coherent message = aligned appraisal narrative | a = judging * information = assessed account | p1 = a * t1 = assessed account * outcome indication = outcome interpretation; p2 = a * t2 = assessed account * appraisal context = qualified outcome context; p3 = a * t3 = assessed account * appraisal account = effect narrative; p4 = a * t4 = assessed account * aligned appraisal narrative = comparable outcome account | centroid selects outcome account |
| E[judging,knowledge] | t1 = assessment grounding * fundamental understanding = appraisal basis; t2 = assessment warrant * competent expertise = informed appraisal; t3 = assessment coverage * thorough mastery = consequence comprehension; t4 = assessment comparability * coherent understanding = shared appraisal meaning | a = judging * knowledge = informed assessment | p1 = a * t1 = informed assessment * appraisal basis = outcome model; p2 = a * t2 = informed assessment * informed appraisal = outcome interpretation; p3 = a * t3 = informed assessment * consequence comprehension = effect model; p4 = a * t4 = informed assessment * shared appraisal meaning = comparable interpretation | centroid selects outcome interpretation |
| E[judging,wisdom] | t1 = assessment grounding * essential discernment = claim distinction; t2 = assessment warrant * adequate judgment = qualified appraisal; t3 = assessment coverage * holistic insight = consequence perspective; t4 = assessment comparability * principled reasoning = appraisal principle | a = judging * wisdom = discerning assessment | p1 = a * t1 = discerning assessment * claim distinction = evidence-limit distinction; p2 = a * t2 = discerning assessment * qualified appraisal = bounded claim; p3 = a * t3 = discerning assessment * consequence perspective = balanced consequence claim; p4 = a * t4 = discerning assessment * appraisal principle = accountable claim | centroid selects outcome claim calibration |
| E[reviewing,data] | t1 = scrutiny provenance * essential fact = source fact; t2 = scrutiny warrant * adequate evidence = scrutiny support; t3 = scrutiny coverage * comprehensive record = source inventory; t4 = scrutiny coherence * reliable measurement = stable source observation | a = reviewing * data = examined observation | p1 = a * t1 = examined observation * source fact = provenance observation; p2 = a * t2 = examined observation * scrutiny support = support trace; p3 = a * t3 = examined observation * source inventory = provenance inventory; p4 = a * t4 = examined observation * stable source observation = comparable provenance trace | centroid selects provenance evidence |
| E[reviewing,information] | t1 = scrutiny provenance * essential signal = provenance indication; t2 = scrutiny warrant * adequate context = scrutiny context; t3 = scrutiny coverage * comprehensive account = source account; t4 = scrutiny coherence * coherent message = aligned scrutiny narrative | a = reviewing * information = examined account | p1 = a * t1 = examined account * provenance indication = source narrative; p2 = a * t2 = examined account * scrutiny context = qualified source context; p3 = a * t3 = examined account * source account = provenance narrative; p4 = a * t4 = examined account * aligned scrutiny narrative = comparable source account | centroid selects provenance account |
| E[reviewing,knowledge] | t1 = scrutiny provenance * fundamental understanding = source comprehension; t2 = scrutiny warrant * competent expertise = scrutiny interpretation; t3 = scrutiny coverage * thorough mastery = claim-limit comprehension; t4 = scrutiny coherence * coherent understanding = shared scrutiny meaning | a = reviewing * knowledge = informed examination | p1 = a * t1 = informed examination * source comprehension = source interpretation; p2 = a * t2 = informed examination * scrutiny interpretation = evidence interpretation; p3 = a * t3 = informed examination * claim-limit comprehension = uncertainty interpretation; p4 = a * t4 = informed examination * shared scrutiny meaning = comparable claim interpretation | centroid selects evidence interpretation |
| E[reviewing,wisdom] | t1 = scrutiny provenance * essential discernment = source distinction; t2 = scrutiny warrant * adequate judgment = qualified scrutiny; t3 = scrutiny coverage * holistic insight = claim-limit perspective; t4 = scrutiny coherence * principled reasoning = scrutiny principle | a = reviewing * wisdom = discerning examination | p1 = a * t1 = discerning examination * source distinction = authority distinction; p2 = a * t2 = discerning examination * qualified scrutiny = confidence limitation; p3 = a * t3 = discerning examination * claim-limit perspective = uncertainty perspective; p4 = a * t4 = discerning examination * scrutiny principle = accountable confidence | centroid selects evidence stewardship |

### Result

| | data | information | knowledge | wisdom |
|---|---|---|---|---|
| guiding | integration evidence | integration context | integration model | integration stewardship |
| applying | transaction observations | transaction narrative | transaction comprehension | recovery stewardship |
| judging | outcome evidence | outcome account | outcome interpretation | outcome claim calibration |
| reviewing | provenance evidence | provenance account | evidence interpretation | evidence stewardship |

---

## Matrix Z — Summary Boundary

This delimiter separates derivation from summary. It is not a semantic matrix.

## Matrix Summary

### C - Formulation

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| normative | authority boundary | contract warrant | obligation coverage | contract coherence |
| operative | transaction precondition | transaction evidence | transaction coverage | state correspondence |
| evaluative | preservation purpose | recovery confidence | lifecycle consequence | evidence trust |

### F - Requirements

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| normative | authorized input | source qualification | boundary traceability | authority alignment |
| operative | observable transition | outcome support | lifecycle trace | reconciliation basis |
| evaluative | continuity stake | claim calibration | consequence coverage | appraisal coherence |

### D - Objectives

| | guiding | applying | judging | reviewing |
|---|---|---|---|---|
| normative | authority orientation | contract conformance | boundary accounting | authority scrutiny |
| operative | transition framing | observed transaction | outcome accounting | reconciliation scrutiny |
| evaluative | preservation orientation | recovery appraisal | consequence accounting | confidence scrutiny |

### K - Transpose of D

| | normative | operative | evaluative |
|---|---|---|---|
| guiding | authority orientation | transition framing | preservation orientation |
| applying | contract conformance | observed transaction | recovery appraisal |
| judging | boundary accounting | outcome accounting | consequence accounting |
| reviewing | authority scrutiny | reconciliation scrutiny | confidence scrutiny |

### G - Truncation of B

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| data | essential fact | adequate evidence | comprehensive record | reliable measurement |
| information | essential signal | adequate context | comprehensive account | coherent message |
| knowledge | fundamental understanding | competent expertise | thorough mastery | coherent understanding |

### X - Verification

| | necessity | sufficiency | completeness | consistency |
|---|---|---|---|---|
| guiding | integration premise | integration rationale | integration horizon | integration alignment |
| applying | transaction grounding | transaction warrant | transaction span | transaction correspondence |
| judging | assessment grounding | assessment warrant | assessment coverage | assessment comparability |
| reviewing | scrutiny provenance | scrutiny warrant | scrutiny coverage | scrutiny coherence |

### T - Transpose of B

| | data | information | knowledge | wisdom |
|---|---|---|---|---|
| necessity | essential fact | essential signal | fundamental understanding | essential discernment |
| sufficiency | adequate evidence | adequate context | competent expertise | adequate judgment |
| completeness | comprehensive record | comprehensive account | thorough mastery | holistic insight |
| consistency | reliable measurement | coherent message | coherent understanding | principled reasoning |

### E - Evaluation

| | data | information | knowledge | wisdom |
|---|---|---|---|---|
| guiding | integration evidence | integration context | integration model | integration stewardship |
| applying | transaction observations | transaction narrative | transaction comprehension | recovery stewardship |
| judging | outcome evidence | outcome account | outcome interpretation | outcome claim calibration |
| reviewing | provenance evidence | provenance account | evidence interpretation | evidence stewardship |
