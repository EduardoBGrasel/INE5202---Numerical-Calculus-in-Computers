from get_coeficientes import extrair_coeficientes
from pol_aux import transformar_expoentes
from test import array_para_polinomio

def cotas_de_kojima(polinomio, n):
    coef = extrair_coeficientes(polinomio)
    vec = []
    for i in range(n):
        vec.append(abs((coef[i + 1]) / coef[0]) ** (1 / (i + 1)))
    max1 = max(vec)
    vec2 = vec.copy()
    vec2.remove(max1)
    max2 = max(vec2)
    rMax = max1 + max2

    coef = extrair_coeficientes(transformar_expoentes(polinomio))
    vec = []
    a0 = coef[0]
    coef.remove(a0)
    for i in range(n):
        vec.append(abs((coef[i]) / a0) ** (1 / (i + 1)))
    max1 = max(vec)
    vec2 = vec.copy()
    vec2.remove(max1)
    max2 = max(vec2)
    rMax2 = round(max1 + max2, 2)
    rMin = 1 / rMax2
    print(rMin)
    return rMin + 0.1, rMax
