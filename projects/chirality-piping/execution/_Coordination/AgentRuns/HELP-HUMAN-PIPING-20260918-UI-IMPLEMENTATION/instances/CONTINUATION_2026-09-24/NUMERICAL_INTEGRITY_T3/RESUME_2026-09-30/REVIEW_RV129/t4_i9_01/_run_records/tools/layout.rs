// RV129: size and alignment of FK load_ledger::Formation today, with T4-I9's
// proposed `Certified { intended: Vec<f64>, radius: f64 }` variant, and of the
// ledger's private Option<FormationRecord> slot, on this host's rustc.
#![allow(dead_code)]
use std::mem::{align_of, size_of};

#[derive(Debug, Clone, PartialEq)]
enum FormationToday {
    Exact { scale: f64, scaled_intended: Vec<f64> },
    RoundedProduct { k: f64, a: f64, b: f64 },
    Bounded { bound: f64 },
    CannotBound,
}

#[derive(Debug, Clone, PartialEq)]
enum FormationProposed {
    Exact { scale: f64, scaled_intended: Vec<f64> },
    RoundedProduct { k: f64, a: f64, b: f64 },
    Bounded { bound: f64 },
    CannotBound,
    Certified { intended: Vec<f64>, radius: f64 },
}

struct RecordToday { formation: FormationToday, operand_bound: f64, self_equilibrated: bool }
struct RecordProposed { formation: FormationProposed, operand_bound: f64, self_equilibrated: bool }

fn main() {
    println!("Formation today:    size {} align {}", size_of::<FormationToday>(), align_of::<FormationToday>());
    println!("Formation proposed: size {} align {}", size_of::<FormationProposed>(), align_of::<FormationProposed>());
    println!("Option<FormationRecord> today:    size {}", size_of::<Option<RecordToday>>());
    println!("Option<FormationRecord> proposed: size {}", size_of::<Option<RecordProposed>>());
}
