def transformar_expoentes(polinomio):
    # Remove espaços e divide o polinômio em termos
    termos = polinomio.replace(" ", "").replace("-", "+-").split("+")
    
    # Armazena coeficientes e expoentes
    coeficientes = []
    expoentes = []

    # Extrai coeficientes e expoentes
    for termo in termos:
        if termo:  # Evita termos vazios
            if '*x**' in termo:  # Formato: coef*x**exp
                coef, exp = termo.split('*x**')
                coeficientes.append(int(coef))  # Converte coeficiente para inteiro
                expoentes.append(int(exp))       # Converte expoente para inteiro
            elif '*x' in termo:  # Formato: coef*x
                coef = termo.split('*x')[0]
                coeficientes.append(int(coef) if coef else 1)  # Assume 1 se vazio
                expoentes.append(1)  # Expoente de x sem '^' é 1
            elif 'x**' in termo:  # Formato: x**exp (sem coeficiente explícito)
                coef, exp = termo.split('x**')
                coeficientes.append(int(coef) if coef else 1)  # Assume 1 se vazio
                expoentes.append(int(exp))       # Converte expoente para inteiro
            elif 'x' in termo:  # Formato: x (sem coeficiente explícito)
                coef = termo.split('x')[0]
                coeficientes.append(int(coef) if coef else 1)  # Assume 1 se vazio
                expoentes.append(1)  # Expoente de x sem '^' é 1
            else:  # Formato: constante
                coeficientes.append(int(termo))  # Adiciona constante
                expoentes.append(0)  # Terma constante tem expoente 0

    # Troca os expoentes conforme a nova ordem
    max_exp = max(expoentes)
    novos_expoentes = [max_exp - exp for exp in expoentes]

    # Monta o polinômio no novo formato
    termos_formatados = []
    for coef, exp in zip(coeficientes, novos_expoentes):
        if exp == 0:
            termos_formatados.append(f"{coef}")  # Apenas o coeficiente
        elif exp == 1:
            termos_formatados.append(f"{coef}*x")  # Coeficiente seguido de x
        else:
            termos_formatados.append(f"{coef}*x**{exp}")  # Coeficiente seguido de x^expoente

    # Inverte a ordem dos termos formatados para mostrar do maior expoente para o menor
    termos_formatados.reverse()

    # Junta os termos formatados com espaço, lidando com sinais negativos
    polinomio_formatado = ""
    for i, termo in enumerate(termos_formatados):
        if i > 0 and termo.startswith('-'):
            polinomio_formatado += f" {termo}"  # Adiciona espaço antes de coeficientes negativos
        else:
            if polinomio_formatado:  # Se já há termos, adiciona um +
                polinomio_formatado += " + "
            polinomio_formatado += termo

    return polinomio_formatado

