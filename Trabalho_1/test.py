def array_para_polinomio(arr):
    termos = []
    n = len(arr)  # Obtemos o tamanho da lista de coeficientes

    # Iteramos do maior grau (0) para o menor grau (n-1)
    for grau in range(n):
        coeficiente = arr[grau]
        if coeficiente == 0:  # Ignorar coeficientes nulos
            continue
        grau_atual = n - 1 - grau  # O grau atual deve ser n - 1 - grau
        if grau_atual == 0:
            termos.append(f"{coeficiente}")  # Para o termo constante
        elif grau_atual == 1:
            termos.append(f"{'-' if coeficiente < 0 else ''}{abs(coeficiente)}*x")  # Para x
        else:
            termos.append(f"{'-' if coeficiente < 0 else ''}{abs(coeficiente)}*x**{grau_atual}")  # Para x**grau

    # Juntar os termos com sinais corretos
    polinomio = ""
    for termo in termos:
        if not polinomio:  # Se for o primeiro termo
            polinomio += termo
        else:
            # Verifica o sinal do termo e adiciona corretamente
            if termo[0] == '-':
                polinomio += f" {termo}"
            else:
                polinomio += f" + {termo}"

    return polinomio.strip()  # Remove espaços desnecessários

