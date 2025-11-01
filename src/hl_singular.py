
import argparse
import mpmath as mp

def singular_product(P=10**6, variant="goldbach"):
    # V_HL = 2 * Π_{p>2} (1 - 1/(p-1)^2)
    mp.mp.dps = 50
    if variant.lower() == "goldbach":
        prod = mp.mpf("1.0")
        # primos até P (simples: checagem primal ingênua; suficiente para P moderado)
        def is_prime(n):
            if n < 2: return False
            if n % 2 == 0:
                return n == 2
            r = int(mp.sqrt(n))
            for k in range(3, r+1, 2):
                if n % k == 0:
                    return False
            return True
        for p in range(3, int(P)+1):
            if is_prime(p):
                term = 1.0 - 1.0/((p-1)*(p-1))
                prod *= mp.mpf(term)
        return mp.mpf(2) * prod
    else:
        raise ValueError("variant não suportada: use 'goldbach'")

def truncation_error(P=10**6):
    # Bound elementar ~ 1/P
    return 1.0/float(P)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--P", type=int, default=10**6)
    ap.add_argument("--variant", type=str, default="goldbach")
    args = ap.parse_args()
    Vtr = singular_product(P=args.P, variant=args.variant)
    err = truncation_error(P=args.P)
    print({"V_HL_trunc": str(Vtr), "Err_trunc_bound": err})

if __name__ == "__main__":
    main()
