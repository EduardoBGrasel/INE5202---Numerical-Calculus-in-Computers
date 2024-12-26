from get_coeficientes import extrair_coeficientes
from test import array_para_polinomio
from pol_aux import transformar_expoentes

def cotas_de_cauchy(polinomio, n):
    # Extrai os coeficientes do polinômio
    coef = extrair_coeficientes(polinomio)
    vec = []
    for i in range(n):
        vec.append(abs((coef[i + 1]) / coef[0]))
    cal = array_para_polinomio(vec)
    cal = f"({cal})**{1/n}"
    
    # Inicializa `x` com um valor inicial
    x = 1  
    for _ in range(10000):
        cal_com_x = cal.replace("x", str(x))  # Substituir `x` na expressão
        novo_x = eval(cal_com_x)  # Avaliar expressão com `x` atualizado
        x = novo_x  # Atualizar `x` para a próxima iteração
    rMax = round(x, 2)  # Arredondar rMax para 2 casas decimais

    # Extrai os coeficientes transformados do polinômio
    coef = extrair_coeficientes(transformar_expoentes(polinomio))
    vec = []
    for i in range(n):
        vec.append(abs((coef[i + 1]) / coef[0]))
    cal = array_para_polinomio(vec)
    cal = f"({cal})**{1/n}"
    
    # Inicializa `x` novamente
    x = 1  
    for _ in range(10000):
        cal_com_x = cal.replace("x", str(x))  # Substituir `x` na expressão
        novo_x = eval(cal_com_x)  # Avaliar expressão com `x` atualizado
        x = novo_x  # Atualizar `x` para a próxima iteração
    rMax2 = round(x, 2)  # Arredondar rMax2 para 2 casas decimais

    rMin = round(1 / rMax2, 2)  # Arredondar rMin para 2 casas decimais
    print(rMin)
    return rMin, rMax  # Retorna os valores finais arredondados
