
import json

def aggregate_report(C_infty, C_type_sum, Err_trunc, alpha0, c_norm, V_HL_trunc):
    delta = c_norm * max(0.0, (1.0 - alpha0))
    C_prime = C_infty + C_type_sum + Err_trunc
    C_dprime = max(C_prime, C_prime / max(delta, 1e-12))
    return {
        "C_infty": C_infty, "C_type_sum": C_type_sum, "Err_trunc": Err_trunc,
        "alpha0": alpha0, "c_norm": c_norm, "delta": delta,
        "C_prime": C_prime, "C_dprime": C_dprime, "V_HL_trunc": str(V_HL_trunc)
    }
