
# repro-goldbach

Repositório mínimo para auditoria do fator singular V_HL, estimativa de gap em minor (alpha0, delta) e agregação de constantes C', C''.

Uso rápido (Colab):
1) Produto singular:
   python -m src.hl_singular --P 1000000 --variant goldbach

2) Janelas e constantes de tipo:
   python -m src.arcs --N 100000000 --Qmaj 10000 --eta 0.02 --window_file data/windows/phi_default.json
   (opcional) chamar estimate_C_type_sum via Python.

3) Gap em minor:
   python -m src.minors_gap --N 100000000 --Qmaj 10000 --eta 0.02 --window_file data/windows/phi_default.json

4) Pipeline completo:
   python scripts/estimate_Cdd.py --config data/samples/config_N1e8.json
