#[path = "../../../../../../../../../core/product_physics/src/pressure_sum.rs"]
mod pressure_sum;
use std::io::{self, BufRead};
fn main() {
 for line in io::stdin().lock().lines() {
  let line=line.unwrap();
  let values=line.split_whitespace().map(|s| f64::from_bits(u64::from_str_radix(s,16).unwrap()));
  match pressure_sum::exact_sum(values) {
   Ok(value)=>println!("OK {:016x}",value.to_bits()),
   Err(error)=>println!("ERR {error:?}"),
  }
 }
}
