from get_coeficientes import extrair_coeficientes
from pol_aux import transformar_expoentes
from test import array_para_polinomio

def mod_min(polinomio, n):
    coef = extrair_coeficientes(polinomio)
    vec = []
    for i in range(len(coef)):
        vec.append(abs(coef[i]))
    divisor = vec[-1]
    vec.remove(divisor)
    maior = max(vec)
    rMin = 1/(1+(maior/divisor))
    return rMin
