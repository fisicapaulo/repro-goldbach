
import json
import math

def estimate_C_type_sum(N, windows, weight_file=None):
    # Mock/placeholder auditável: estima perdas de borda e correções de tipo
    # Fórmula simples: Σ C_Type ≈ k1 * Qmaj * (C / N^{1-eta}) com calibração leve
    if isinstance(windows, str) and windows == "AUTO":
        raise ValueError("Passe o dicionário de janelas via src.arcs.build_windows.")
    Qmaj = windows["Qmaj"]; C = windows["C"]; eta = windows["eta"]
    k1 = 0.1  # constante de escala simbólica (ajustável)
    val = k1 * Qmaj * (C / (N**(1.0 - eta)))
    return float(val)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--windows_json", type=str, required=True)
    ap.add_argument("--weight_file", type=str, default=None)
    args = ap.parse_args()
    with open(args.windows_json,"r") as f:
        windows = json.load(f)
    s = estimate_C_type_sum(args.N, windows, args.weight_file)
    print({"C_type_sum": s})

if __name__ == "__main__":
    main()
