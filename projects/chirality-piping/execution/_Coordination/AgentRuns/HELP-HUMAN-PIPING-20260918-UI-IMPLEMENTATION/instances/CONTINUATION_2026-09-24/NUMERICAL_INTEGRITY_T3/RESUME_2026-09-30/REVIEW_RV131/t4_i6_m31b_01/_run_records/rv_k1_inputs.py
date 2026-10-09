"""RV131: K1's stated literals (U1_REFERENCE.md B5.1/B5.2) against the JSON values; PP-form round trips.
usage: python -I rv_k1_inputs.py U1_JSON"""
import sys, json, math
doc = json.load(open(sys.argv[1]))
K = {k["model"]: k for k in doc["m31b_kill_and_mutant"]}
ip, sk = K["K1-IP-1E-8-X0"], K["K1-SK-1E-8-X0"]
ip5, sk5 = K["K1-IP-1E-8-X5e6"], K["K1-SK-1E-8-X5e6"]
print("K1-IP d:", [ip["nodes"][1][q] - ip["nodes"][0][q] for q in range(3)], "R", repr(ip["R"]), "phi", ip["phi"])
print("K1-SK d:", [sk["nodes"][1][q] - sk["nodes"][0][q] for q in range(3)], "R", repr(sk["R"]), "phi", sk["phi"])
stated = dict(ip_d=(0.25980762112885714, 0.15000000037252903, 0.0), ip_R=30000000.018065747,
              sk_d=(0.09999999962747097, 0.20000000018626451, 0.20000000018626451), sk_R=30000000.012417633,
              pp_x1=(5000000.259807621, 3500000.1500000004, 0.0))
print("IP d literal == JSON:", tuple(ip["nodes"][1][q] - ip["nodes"][0][q] for q in range(3)) == stated["ip_d"], "| R literal == JSON:", stated["ip_R"] == ip["R"])
print("SK d literal == JSON:", tuple(sk["nodes"][1][q] - sk["nodes"][0][q] for q in range(3)) == stated["sk_d"], "| R literal == JSON:", stated["sk_R"] == sk["R"])
print("PP x0, x1 (JSON X5e6):", ip5["nodes"][0], ip5["nodes"][1])
print("PP x1 literal == JSON x1:", tuple(stated["pp_x1"]) == tuple(ip5["nodes"][1]))
x0, x1 = ip5["nodes"]
print("PP d (binary64 x1 - x0) == X0 d:", [x1[q] - x0[q] for q in range(3)] == list(stated["ip_d"]))
print("repr round trip of x1 and R:", [repr(v) for v in x1], repr(ip["R"]))
# grid check
g = 2.0 ** -30
print("d on 2^-30 grid:", all((v / g).is_integer() for v in stated["ip_d"] + stated["sk_d"]))
print("u_int equal at X0 and X5e6 (IP, SK):", ip["u_int"] == ip5["u_int"], sk["u_int"] == sk5["u_int"])
print("mutant libm == correctly rounded (IP, SK):", ip["mutant_libm"]["ratio"], ip["mutant_correctly_rounded_trig"]["ratio"], sk["mutant_libm"]["ratio"], sk["mutant_correctly_rounded_trig"]["ratio"])
print("cos(phi_b) binary64 (IP):", repr(ip["mutant_libm"]["cos_phi_b"]), " half-ulp below 1 = 2^-54 =", 2.0**-54, " phi^2/2 =", float(ip["phi"]) ** 2 / 2)
print("cond1 equilibrated (IP, SK):", ip["cond1_equilibrated_exact"], sk["cond1_equilibrated_exact"], "| crK estimate:", ip["estimate_correctly_rounded_K_ratio"], sk["estimate_correctly_rounded_K_ratio"])
