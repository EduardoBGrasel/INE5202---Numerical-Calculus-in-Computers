from read_poly import read_poly
from compute_best_quota import compute_best_quota
from get_coeficientes import extrair_coeficientes
from compute_root import compute_root




n = int(input(""))
P = read_poly(n)
extrair_coeficientes(P)
a_b = compute_best_quota(P, n)
print(f"Best quotas = [{(a_b[0]):.2f},{a_b[1]:.2f}]")
res = compute_root(P, a_b)
print(f"{res[0]:.6f}")





