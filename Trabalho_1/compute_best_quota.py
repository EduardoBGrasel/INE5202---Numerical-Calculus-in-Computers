
from cauchy import cotas_de_cauchy
from kojima import cotas_de_kojima
from mod_max import mod_max
from mod_min import mod_min

def compute_best_quota(P, n):
    cauchy = cotas_de_cauchy(P, n)
    kojima = cotas_de_kojima(P, n)
    maior_mod = mod_max(P, n)
    menor_mod = mod_min(P, n)
    menor = 0
    maior = 0
    menores = [cauchy[0], kojima[0], menor_mod]
    maiores = [cauchy[1], kojima[1], maior_mod]
    menor = min(menores)
    maior = min(maiores)


    return menor, maior