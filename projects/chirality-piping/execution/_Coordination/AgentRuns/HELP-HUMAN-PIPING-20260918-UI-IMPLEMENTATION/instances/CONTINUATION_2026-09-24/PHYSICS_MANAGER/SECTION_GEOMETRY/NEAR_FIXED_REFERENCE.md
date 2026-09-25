# Independent fixed-transfer near-limit append

For both ends fully restrained, no thermal/mechanical loads and transferred closures, axial strain is exactly zero. Isotropic compliance gives Nw=2nuP; effective force is S=(2nu-1)P, and signed support-on-pipe axial reactions are R_left=(1-2nu)P and R_right=-R_left.

The source P/nu values are those already independently frozen in NEAR_INCOMPRESSIBLE_EXPECTATIONS.json. The new freeze_near_fixed.py uses their exact rational values; it does not subtract rounded published wall and cap forces to create an oracle. NEAR_FIXED_EXPECTATIONS.json retains all three cases. At the last valid nu below .5, S=-1.74393424900431578e-12 N and the reactions are +/-1.74393424900431578e-12 N, despite wall force near15708 N.

Every nonzero force retains relative1e-9. A wall-force-relative floor would hide the effective-force error and is not used. Both modes are required. This is an explicitly appended reference before source recovery repair; the earlier geometry/free-pressure freezes and existing six tests remain unchanged until the recorded append delta.
