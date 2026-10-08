//! I111 M07 probe: rigid-body and moment-equilibrium checks on the product's
//! `UserStiffnessElement` (frame_kernel `user_stiffness_local_matrix`), read-only.
//! It links the unchanged frame_kernel crate at NUM's HEAD and calls only its
//! public API (`UserStiffnessElement::{new, local_stiffness, global_stiffness}`).
use open_pipe_stress_frame_kernel::{FrameNode, Matrix12, UserStiffnessElement, DOF_PER_NODE};

fn cross(a: [f64; 3], b: [f64; 3]) -> [f64; 3] {
    [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
}

fn mul(k: &Matrix12, d: &[f64; 12]) -> [f64; 12] {
    let mut f = [0.0; 12];
    for r in 0..12 {
        for c in 0..12 {
            f[r] += k[r][c] * d[c];
        }
    }
    f
}

/// Rigid displacement of the two element nodes: translation t plus an
/// infinitesimal rotation w about the origin (u = t + w x x, theta = w).
fn rigid(xi: [f64; 3], xj: [f64; 3], t: [f64; 3], w: [f64; 3]) -> [f64; 12] {
    let mut d = [0.0; 12];
    for (node, x) in [(0usize, xi), (1usize, xj)] {
        let wx = cross(w, x);
        for a in 0..3 {
            d[node * DOF_PER_NODE + a] = t[a] + wx[a];
            d[node * DOF_PER_NODE + 3 + a] = w[a];
        }
    }
    d
}

/// Net force and net moment about the origin of the element end actions f.
fn resultant(xi: [f64; 3], xj: [f64; 3], f: &[f64; 12]) -> ([f64; 3], [f64; 3]) {
    let mut net_f = [0.0; 3];
    let mut net_m = [0.0; 3];
    for (node, x) in [(0usize, xi), (1usize, xj)] {
        let force = [f[node * 6], f[node * 6 + 1], f[node * 6 + 2]];
        let moment = [f[node * 6 + 3], f[node * 6 + 4], f[node * 6 + 5]];
        let lever = cross(x, force);
        for a in 0..3 {
            net_f[a] += force[a];
            net_m[a] += moment[a] + lever[a];
        }
    }
    (net_f, net_m)
}

fn max_abs(v: &[f64]) -> f64 {
    v.iter().fold(0.0_f64, |m, x| m.max(x.abs()))
}

fn main() {
    // The invented demo's C-150 on P-130: N-130 (7.6, 2.4, 0) -> N-140 (7.6, 2.4, 2.2),
    // y_reference (0, 1, 0); axial 3.2e6, lateral 9e5 N/m, angular 4.8e5, torsional 6.2e5 N*m/rad.
    // The product builds node_i = the pipe's other node (N-130), node_j = the joint node (N-140).
    let xi = [7.6, 2.4, 0.0];
    let xj = [7.6, 2.4, 2.2];
    let ni = FrameNode::new(0, xi).unwrap();
    let nj = FrameNode::new(1, xj).unwrap();
    let joint = UserStiffnessElement::new(ni, nj, [0.0, 1.0, 0.0], 3.2e6, 9.0e5, 4.8e5, 6.2e5).unwrap();
    let k = joint.global_stiffness().unwrap();

    // 1. Local matrix structure: the lateral rows couple only UY_i/UY_j (UZ_i/UZ_j);
    //    no UY-RZ or UZ-RY coupling terms exist (k[1][5], k[1][11], k[2][4], k[2][10]).
    let local = joint.local_stiffness();
    println!(
        "LOCAL lateral_y_row(UY_i)={:?}",
        local[1].iter().map(|v| *v).collect::<Vec<_>>()
    );
    println!(
        "LOCAL coupling UY_i-RZ_i={} UY_i-RZ_j={} UZ_i-RY_i={} UZ_i-RY_j={}",
        local[1][5], local[1][11], local[2][4], local[2][10]
    );

    // 2. Rigid-body modes on the global matrix (unit translations, then 1e-3 rad rotations about the origin).
    let mut worst_translation = 0.0_f64;
    for a in 0..3 {
        let mut t = [0.0; 3];
        t[a] = 1.0;
        let f = mul(&k, &rigid(xi, xj, t, [0.0; 3]));
        worst_translation = worst_translation.max(max_abs(&f));
    }
    println!("RIGID translation max|K d| = {worst_translation:e}");
    for (name, w) in [("x", [1e-3, 0.0, 0.0]), ("y", [0.0, 1e-3, 0.0]), ("z", [0.0, 0.0, 1e-3])] {
        let f = mul(&k, &rigid(xi, xj, [0.0; 3], w));
        println!("RIGID rotation about global {name} (1e-3 rad): max|K d| = {:e}; f = {:?}", max_abs(&f), f);
    }

    // 3. Moment equilibrium of the element's own end actions under a relative lateral
    //    displacement delta along global X (the demo's L-100 relative motion; 299.2894367 N
    //    spring force in the 2026-09-08 frozen record gives delta = 299.28943672347367 / 9e5).
    let delta = 299.28943672347367 / 9.0e5;
    let mut d = [0.0; 12];
    d[6] = delta; // UX at node j (global X is a local lateral axis of this element)
    let f = mul(&k, &d);
    let (net_f, net_m) = resultant(xi, xj, &f);
    println!("EQUILIBRIUM delta={delta:e} m: end actions {f:?}");
    println!("EQUILIBRIUM net force {net_f:?} N; net moment about origin {net_m:?} N*m");
    println!("EQUILIBRIUM k*delta*L = {} N*m", 9.0e5 * delta * 2.2);

    // 4. Control: the same element with lateral = 0 (struct literal; `new` refuses 0)
    //    passes the rigid rotation test, so the defect is exactly the lateral terms.
    let control = UserStiffnessElement { lateral_stiffness: 0.0, ..joint };
    let kc = control.global_stiffness().unwrap();
    let mut worst = 0.0_f64;
    for w in [[1e-3, 0.0, 0.0], [0.0, 1e-3, 0.0], [0.0, 0.0, 1e-3]] {
        worst = worst.max(max_abs(&mul(&kc, &rigid(xi, xj, [0.0; 3], w))));
    }
    println!("CONTROL lateral=0 rigid rotation max|K d| = {worst:e}");

    // 5. Null space: the element's zero-energy set is the tie u_i = u_j, theta_i = theta_j,
    //    which contains a common rotation WITHOUT the lever translation (a deformation).
    let mut tie = [0.0; 12];
    tie[4] = 1e-3;
    tie[10] = 1e-3; // common RY at both nodes, no translation
    println!("TIE common RY without translation: max|K d| = {:e}", max_abs(&mul(&k, &tie)));
}
