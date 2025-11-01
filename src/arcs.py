
import json
import math

def build_windows(N, Qmaj, eta, window_file=None):
    # Gera metadados de janelas (sem geometria explícita) para auditoria e uso posterior
    cfg = {}
    if window_file:
        with open(window_file,"r") as f:
            cfg = json.load(f)
    C = cfg.get("width_C", 1.5)
    windows = {
        "N": N, "Qmaj": Qmaj, "eta": eta,
        "C": C,
        "definition": "major arcs by rationals a/q with q<=Qmaj and width Δ(q)=C/(q*N^{1-eta})"
    }
    return windows

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--Qmaj", type=int, required=True)
    ap.add_argument("--eta", type=float, required=True)
    ap.add_argument("--window_file", type=str, default=None)
    args = ap.parse_args()
    windows = build_windows(args.N, args.Qmaj, args.eta, args.window_file)
    print(json.dumps(windows, indent=2))

if __name__ == "__main__":
    main()
