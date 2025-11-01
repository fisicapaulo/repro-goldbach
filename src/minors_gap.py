
import json
import math
import random

def estimate_alpha0(N, Qmaj, eta, weight_file=None, windows=None, grid_size=200):
    # Estimativa empírica simples: alpha0 cai com Qmaj e com N^{eta}
    # Mock consistente: 1 - c * (Qmaj/N^{1/2})^{0.25} * (eta)^{0.5}, com clamp
    c = 0.6
    scale = (Qmaj / max(1.0, (N**0.5))) ** 0.25
    val = 1.0 - c * scale * (eta**0.5)
    return max(0.80, min(0.995, val))

def estimate_cnorm(window_file=None):
    # c_norm cresce com suavidade (transition_smoothness menor -> transição mais suave)
    cfg = {}
    if window_file:
        with open(window_file,"r") as f:
            cfg = json.load(f)
    smooth = float(cfg.get("transition_smoothness", 0.15))
    overlap = float(cfg.get("overlap_max_frac", 0.08))
    base = 0.6
    # Heurística: transições suaves (smooth pequeno) e baixo overlap aumentam c_norm
    cn = base + max(0.0, (0.2 - smooth)) + max(0.0, (0.15 - overlap))
    return float(max(0.3, min(0.95, cn)))

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--Qmaj", type=int, required=True)
    ap.add_argument("--eta", type=float, required=True)
    ap.add_argument("--weight_file", type=str, default=None)
    ap.add_argument("--windows", type=str, default=None)
    ap.add_argument("--window_file", type=str, default=None)
    args = ap.parse_args()
    alpha0 = estimate_alpha0(args.N, args.Qmaj, args.eta, args.weight_file, args.windows)
    c_norm = estimate_cnorm(args.window_file)
    delta = c_norm * max(0.0, (1.0 - alpha0))
    print({"alpha0": alpha0, "c_norm": c_norm, "delta": delta})

if __name__ == "__main__":
    main()
