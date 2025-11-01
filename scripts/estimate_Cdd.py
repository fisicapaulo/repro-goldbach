
import json
import argparse

from src.hl_singular import singular_product, truncation_error
from src.archimedean import compute_C_infty
from src.arcs import build_windows
from src.type_constants import estimate_C_type_sum
from src.minors_gap import estimate_alpha0, estimate_cnorm
from src.audit import aggregate_report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=str, required=True)
    args = ap.parse_args()
    cfg = json.load(open(args.config))
    N = int(cfg["N"]); Qmaj = int(cfg["Qmaj"]); eta = float(cfg["eta"])
    P = int(cfg["P"]); weight_file = cfg["weight_file"]; window_file = cfg["window_file"]

    C_infty = compute_C_infty(weight_file, window_file)
    windows = build_windows(N=N, Qmaj=Qmaj, eta=eta, window_file=window_file)
    C_type_sum = estimate_C_type_sum(N=N, windows=windows, weight_file=weight_file)

    V_trunc = singular_product(P=P, variant="goldbach")
    err_trunc = truncation_error(P=P)

    alpha0 = estimate_alpha0(N=N, Qmaj=Qmaj, eta=eta, weight_file=weight_file, windows=windows)
    c_norm = estimate_cnorm(window_file=window_file)

    report = aggregate_report(C_infty, C_type_sum, err_trunc, alpha0, c_norm, V_trunc)
    report.update({"N": N, "Qmaj": Qmaj, "eta": eta, "P": P})
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
