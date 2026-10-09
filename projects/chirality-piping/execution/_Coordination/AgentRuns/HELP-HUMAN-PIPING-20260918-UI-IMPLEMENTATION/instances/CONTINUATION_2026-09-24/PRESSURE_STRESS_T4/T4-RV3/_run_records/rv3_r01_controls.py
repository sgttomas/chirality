"""T4-RV3 addendum 01: re-derive every listed wrong_result_discriminators row of T4-I7's round-01 file
(including the regenerated kink controls and the new U2-L-ANCH-PTW-K2 set) with the transfer-matrix
solver, by part 1 of rv3_controls.py (unchanged from round 00).

    python -I -B rv3_r01_controls.py <round-01 u2_reference_cases.json>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_controls as K  # noqa: E402

if __name__ == "__main__":
    K.part1(json.load(open(sys.argv[1])))
