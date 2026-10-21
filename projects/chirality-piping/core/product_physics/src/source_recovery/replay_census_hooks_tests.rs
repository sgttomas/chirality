//! The source-route replay census's finalization hooks (DEL-04-08, "Source-route replay
//! design"; scratch prototype, never merged). Compiled only under the opt-in
//! `census-probe` feature, in every build that enables it (the lib tests and the
//! census runner), and inert until `census_probe::replay`'s switches are set.
//! - `replay_or_bind`: the captured replay after `prepare_sources` (unchanged, same stage
//!   strings), as the full replay (`replay_against`) or the bind-only replay
//!   (`bind_against`), with the shadow full replay on a private ledger, the captured-rebuild
//!   mutants and the case-ledger marks.
//!
//! Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
use super::*;
use open_pipe_stress_frame_kernel::structural::retained_api::census_probe::replay::{self as probe, Mutant};

pub(super) fn mark(label: &'static str, budget: &AttemptBudget) {
    probe::mark(label, budget.report().charged);
}

pub(super) fn replay_or_bind(
    retained: &RetainedFunctionalSet,
    mut source: Sources,
    input: &Input<'_>,
    budget: &mut AttemptBudget,
) -> Result<(), RecoveryError> {
    mark("rebuild", budget);
    let switches = probe::switches();
    // The captured-rebuild mutants (the rebuild's output, before the replay sees it).
    if switches.mutant == Mutant::Desc {
        if let Some((i, d)) = source.descriptors.iter_mut().enumerate().find(|(_, d)| !d.terms.is_empty()) {
            let atom = &mut d.terms[0].products[0][0];
            *atom = atom.next_up();
            probe::applied(&format!("captured descriptor {i} term 0 product 0 atom 0"));
        }
    }
    let system = source.system(input);
    let force: Vec<f64>;
    let system = if switches.mutant == Mutant::Src {
        let mut f = system.force.to_vec();
        if let Some(i) = f.iter().position(|x| *x != 0.0) {
            f[i] = f[i].next_up();
            probe::applied(&format!("captured force {i}"));
        }
        force = f;
        StructuralSystem { force: &force, ..system }
    } else {
        system
    };
    let contacts: &[(usize, i8, f64)] = if switches.mutant == Mutant::ContactExp {
        probe::applied("captured expected contact on DOF 0");
        &[(0, 1, 0.0)]
    } else {
        &[]
    };
    let rule = |index: usize| source.hint(index);
    let result = if switches.bind {
        retained
            .bind_against(&system, &source.identity, exact::ForceBasis::IdentifiedContributions(&source.force_terms),
                &source.congruence, &source.descriptors, Some(&rule), contacts, RELATIVE_LIMIT, budget)
            .result
    } else {
        retained
            .replay_against(&system, &source.identity, exact::ForceBasis::IdentifiedContributions(&source.force_terms),
                &source.congruence, &source.descriptors, Some(&rule), contacts, RELATIVE_LIMIT, budget)
            .result
    };
    mark("replay", budget);
    // The shadow: after bind-only succeeds, the full replay's arithmetic on a private ledger,
    // judging the binding. In the full mode it runs whatever the replay's outcome, as a
    // self-check of the shadow's copy of the full replay: it must agree with the case-ledger
    // replay except where that replay refused for `Budget`.
    if switches.shadow && (!switches.bind || result.is_ok()) {
        let shadow = retained.shadow_replay(&system, &source.identity, exact::ForceBasis::IdentifiedContributions(&source.force_terms),
            &source.congruence, &source.descriptors, Some(&rule), contacts, RELATIVE_LIMIT);
        probe::shadow_private(shadow.clone());
        let verdict = match (&result, &shadow) {
            (_, Ok(_)) if switches.bind => Ok(()),
            (_, Err(e)) if switches.bind => Err(format!("bind-only passed; the full replay refuses: {e}")),
            (Ok(_), Ok(_)) => Ok(()),
            (Err(e), _) if matches!(e, exact::Error::Budget) => Ok(()),
            (Err(e), Err(s)) if format!("{e:?}") == *s => Ok(()),
            (r, s) => Err(format!("full-mode self-check: case replay {r:?}, shadow {s:?}")),
        };
        probe::shadow(verdict);
    }
    result?;
    Ok(())
}
