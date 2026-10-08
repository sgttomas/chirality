//! RV126: differential test of `assess_rigid_body`, the head (correct_norm) against the parent
//! (libm hypot), on generated bodies. Reports changed statuses (decisions) and changed bits.
use fk_new::rigid_body as new;
use fk_old::rigid_body as old;

struct Rng(u64);
impl Rng {
    fn next(&mut self) -> u64 {
        self.0 ^= self.0 << 13;
        self.0 ^= self.0 >> 7;
        self.0 ^= self.0 << 17;
        self.0
    }
    fn unit(&mut self) -> f64 {
        (self.next() >> 11) as f64 / (1u64 << 53) as f64
    }
    fn range(&mut self, n: u64) -> u64 {
        self.next() % n
    }
    fn signed(&mut self) -> f64 {
        2.0 * self.unit() - 1.0
    }
}

fn status_name_new(s: &new::RigidBodyStatus) -> &'static str {
    match s {
        new::RigidBodyStatus::Restrained => "Restrained",
        new::RigidBodyStatus::MechanismWitnessed => "MechanismWitnessed",
        new::RigidBodyStatus::NumericallyUnresolved => "NumericallyUnresolved",
        new::RigidBodyStatus::UnqualifiedFamily => "UnqualifiedFamily",
    }
}
fn status_name_old(s: &old::RigidBodyStatus) -> &'static str {
    match s {
        old::RigidBodyStatus::Restrained => "Restrained",
        old::RigidBodyStatus::MechanismWitnessed => "MechanismWitnessed",
        old::RigidBodyStatus::NumericallyUnresolved => "NumericallyUnresolved",
        old::RigidBodyStatus::UnqualifiedFamily => "UnqualifiedFamily",
    }
}
fn bits3(v: &[[f64; 6]]) -> Vec<u64> {
    v.iter().flatten().map(|x| x.to_bits()).collect()
}


/// Threshold hunt: nearly collinear bodies whose rotation about the line is held only through
/// offsets c_k * delta; bisect delta on the parent's Restrained decision, then compare both
/// decisions at the 801 consecutive doubles around the parent's transition.
fn hunt(configs: u64) {
    let mut rng = Rng(0x0126_0126_dead_beef);
    let (mut transitions, mut disagreements, mut examined) = (0u64, 0u64, 0u64);
    let (mut new_admits, mut new_refuses, mut old_flips, mut new_flips) = (0u64, 0u64, 0u64, 0u64);
    let (mut band_examined, mut band_dis, mut band_old_flips, mut widest_all, mut old_noisy_all) = (0u64, 0u64, 0u64, 0i64, 0i64);
    let mut band_hist = [0u64; 5];
    let mut shown = 0;
    for _ in 0..configs {
        let nodes = 2 + rng.range(3) as usize;
        let dir = [rng.signed(), rng.signed(), rng.signed()];
        let perp = [rng.signed(), rng.signed(), rng.signed()];
        let ts: Vec<f64> = (0..nodes).map(|k| k as f64 + rng.unit()).collect();
        let cs: Vec<f64> = (0..nodes).map(|k| if k == 0 { 0.0 } else { rng.signed() }).collect();
        let scale = [1.0, 1e-3, 1e3, 7.0][rng.range(4) as usize];
        let ground: Vec<usize> = (0..nodes).flat_map(|k| [6 * k, 6 * k + 1, 6 * k + 2]).collect();
        let body = |delta: f64| -> Vec<[f64; 3]> {
            (0..nodes).map(|k| {
                let (t, o) = (ts[k], cs[k] * delta);
                [scale * (t * dir[0] + o * perp[0]), scale * (t * dir[1] + o * perp[1]), scale * (t * dir[2] + o * perp[2])]
            }).collect()
        };
        let old_r = |d: f64| old::assess_rigid_body(&body(d), &ground, old::ObjectiveFamily::WeldedUnreleasedElasticFrames)
            .map(|r| r.status == old::RigidBodyStatus::Restrained).unwrap_or(false);
        let new_r = |d: f64| new::assess_rigid_body(&body(d), &ground, new::ObjectiveFamily::WeldedUnreleasedElasticFrames)
            .map(|r| r.status == new::RigidBodyStatus::Restrained).unwrap_or(false);
        let (mut lo, mut hi) = (1e-30_f64, 1.0_f64);
        if old_r(lo) || !old_r(hi) { continue; }
        for _ in 0..200 {
            let mid = (lo * hi).sqrt();
            let mid = if mid <= lo || mid >= hi { 0.5 * (lo + hi) } else { mid };
            if mid <= lo || mid >= hi { break; }
            if old_r(mid) { hi = mid } else { lo = mid }
        }
        transitions += 1;
        let mut prev: Option<(bool, bool)> = None;
        for k in -400i64..=400 {
            let d = f64::from_bits((hi.to_bits() as i64 + k) as u64);
            examined += 1;
            let (o, n) = (old_r(d), new_r(d));
            if o != n {
                disagreements += 1;
                if n { new_admits += 1 } else { new_refuses += 1 }
                if shown < 5 { shown += 1; println!("HUNT-DISAGREE delta={d:e} old_restrained={o} new_restrained={n} nodes={nodes}"); }
            }
            if let Some((po, pn)) = prev {
                if po != o { old_flips += 1 }
                if pn != n { new_flips += 1 }
            }
            prev = Some((o, n));
        }
        // relative band: delta* (1 + j 1e-6), j in -2000..=2000 (+-0.2 %)
        let mut widest = 0i64;
        let mut old_noisy = 0i64;
        let mut prev_o: Option<bool> = None;
        for j in -2000i64..=2000 {
            let d = hi * (1.0 + j as f64 * 1e-6);
            let (o, n) = (old_r(d), new_r(d));
            band_examined += 1;
            if o != n { band_dis += 1; widest = widest.max(j.abs()); }
            if let Some(po) = prev_o { if po != o { old_noisy = old_noisy.max(j.abs()); band_old_flips += 1; } }
            prev_o = Some(o);
        }
        widest_all = widest_all.max(widest);
        if widest > 0 { band_hist[(widest as f64).log10().floor().max(0.0) as usize] += 1; }
        old_noisy_all = old_noisy_all.max(old_noisy);
    }
    println!("hunt: configs={configs} transitions_found={transitions} deltas_examined={examined} decision_disagreements={disagreements} (new Restrained where old not: {new_admits}; old Restrained where new not: {new_refuses}); adjacent-ulp self-flips: old {old_flips}, new {new_flips}");
    println!("band (delta* x (1 + j 1e-6), |j| <= 2000): examined={band_examined} disagreements={band_dis} old_self_flips={band_old_flips}; widest |j| with a disagreement = {widest_all} (relative {:e}); histogram of per-transition widest |j| by decade [1-9,10-99,100-999,1000-2000]: {:?}; widest |j| where old itself flips = {old_noisy_all}", widest_all as f64 * 1e-6, band_hist);
}

fn main() {
    if std::env::args().nth(1).as_deref() == Some("hunt") {
        hunt(std::env::args().nth(2).map(|s| s.parse().unwrap()).unwrap_or(500));
        return;
    }
    let n: u64 = std::env::args().nth(1).map(|s| s.parse().unwrap()).unwrap_or(200_000);
    let mut rng = Rng(0x5eed_0126_0126_0126);
    let mut counts = std::collections::BTreeMap::<String, u64>::new();
    let mut bump = |k: String| *counts.entry(k).or_insert(0) += 1;
    let mut examples: Vec<String> = Vec::new();
    for case in 0..n {
        let class = case % 6;
        let nodes = 1 + rng.range(5) as usize;
        let scale = match rng.range(6) {
            0 => 1e-200,
            1 => 1e200,
            2 => 1e-8,
            3 => 1e8,
            _ => 1.0,
        };
        let dir = [rng.signed(), rng.signed(), rng.signed()];
        let perp = [rng.signed(), rng.signed(), rng.signed()];
        let delta = 10f64.powi(-(rng.range(18) as i32)) * (1.0 + rng.unit());
        let origin = [rng.signed() * 100.0, rng.signed() * 100.0, rng.signed() * 100.0];
        let mut coords = Vec::new();
        for k in 0..nodes {
            let p = match class {
                0 => [rng.signed() * 10.0, rng.signed() * 10.0, rng.signed() * 10.0],
                1 => {
                    // nearly collinear: along dir, offset delta along perp (except node 0)
                    let t = k as f64 + rng.unit();
                    let o = if k == 0 { 0.0 } else { delta * rng.signed() };
                    [t * dir[0] + o * perp[0], t * dir[1] + o * perp[1], t * dir[2] + o * perp[2]]
                }
                2 => [rng.range(21) as f64 - 10.0, rng.range(21) as f64 - 10.0, rng.range(21) as f64 - 10.0],
                3 => {
                    // nearly coplanar: plane z ~ 0 with delta out of plane
                    [rng.signed() * 10.0, rng.signed() * 10.0, if k == 0 { 0.0 } else { delta * rng.signed() }]
                }
                4 => {
                    // exactly collinear integer multiples along an oblique integer axis
                    let t = (rng.range(9) as f64) - 4.0;
                    [3.0 * t, 4.0 * t, 12.0 * t]
                }
                _ => [rng.signed(), rng.signed() * 1e-6, rng.signed() * 1e6],
            };
            coords.push([origin[0] + p[0] * scale, origin[1] + p[1] * scale, origin[2] + p[2] * scale]);
        }
        // ground dofs: random subset; bias toward translation-only grounds (rotation restrained via geometry)
        let mut ground = Vec::new();
        let translation_only = rng.range(2) == 0;
        let count = rng.range(10) as usize;
        for _ in 0..count {
            let node = rng.range(nodes as u64) as usize;
            let dof = if translation_only { rng.range(3) as usize } else { rng.range(6) as usize };
            let d = 6 * node + dof;
            if !ground.contains(&d) {
                ground.push(d);
            }
        }
        let a = new::assess_rigid_body(&coords, &ground, new::ObjectiveFamily::WeldedUnreleasedElasticFrames);
        let b = old::assess_rigid_body(&coords, &ground, old::ObjectiveFamily::WeldedUnreleasedElasticFrames);
        bump(format!("class{class}"));
        match (a, b) {
            (Ok(a), Ok(b)) => {
                let (sa, sb) = (status_name_new(&a.status), status_name_old(&b.status));
                bump(format!("status_new:{sa}"));
                if sa != sb {
                    bump(format!("DECISION_CHANGED class{class} old={sb} new={sa}"));
                    if examples.len() < 20 {
                        examples.push(format!("class{class} old={sb} new={sa} coords={:?} ground={:?} len_new={:e} len_old={:e} min_sv_new={:e} screen_new={:e}",
                            coords, ground, a.characteristic_length, b.characteristic_length,
                            a.singular_values.iter().cloned().fold(f64::INFINITY, f64::min), a.rank_screen));
                    }
                }
                if a.characteristic_length.to_bits() != b.characteristic_length.to_bits() {
                    bump("length_bits_changed".into());
                }
                if a.singular_values.map(f64::to_bits) != b.singular_values.map(f64::to_bits) {
                    bump("singular_bits_changed".into());
                }
                if a.rank_screen.to_bits() != b.rank_screen.to_bits() {
                    bump("screen_bits_changed".into());
                }
                if a.node_motion.as_ref().map(|v| bits3(v)) != b.node_motion.as_ref().map(|v| bits3(v)) {
                    bump(format!("node_motion_bits_changed (status new={sa})"));
                }
                if a.rigid_parameters.map(|p| p.map(f64::to_bits)) != b.rigid_parameters.map(|p| p.map(f64::to_bits)) {
                    bump("rigid_parameters_changed".into());
                }
                if a.iterations != b.iterations {
                    bump("iterations_changed".into());
                }
            }
            (Err(ea), Err(eb)) => {
                bump("both_err".into());
                if format!("{ea:?}") != format!("{eb:?}") {
                    bump("ERR_KIND_CHANGED".into());
                }
            }
            (a, b) => {
                bump("OK_ERR_MISMATCH".into());
                if examples.len() < 20 {
                    examples.push(format!("ok/err mismatch new={:?} old={:?} coords={coords:?}", a.map(|r| r.status), b.map(|r| r.status)));
                }
            }
        }
    }
    for (k, v) in &counts {
        println!("{k}: {v}");
    }
    for e in &examples {
        println!("EXAMPLE {e}");
    }
}
