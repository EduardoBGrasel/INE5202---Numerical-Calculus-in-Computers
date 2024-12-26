from get_coeficientes import extrair_coeficientes
from pol_aux import transformar_expoentes
from test import array_para_polinomio

def mod_max(polinomio, n):
    coef = extrair_coeficientes(polinomio)
    vec = []
    for i in range(len(coef)):
        vec.append(abs(coef[i]))
    a0 = vec[0]
    vec.remove(a0)
    maior = max(vec)
    rMax = (maior/a0) + 1
    return rMax

