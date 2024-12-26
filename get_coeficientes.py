def extrair_coeficientes(polinomio):
    # Remove espaços em branco
    polinomio = polinomio.replace(' ', '')

    # Divide o polinômio em termos, considerando os sinais
    termos = []
    termo_atual = ''
    for char in polinomio:
        if char in '+-':
            if termo_atual:
                termos.append(termo_atual)
            termo_atual = char  # Adiciona o sinal ao novo termo
        else:
            termo_atual += char
    if termo_atual:  # Adiciona o último termo
        termos.append(termo_atual)

    # Cria uma lista de coeficientes
    grau_maximo = max(
        int(termo.split('**')[-1]) if '**' in termo else 1 for termo in termos
    )
    coeficientes = [0] * (grau_maximo + 1)

    for termo in termos:
        if 'x' in termo:
            # Separando coeficiente e grau
            partes = termo.split('x')
            coef_str = partes[0]
            grau = 1  # Grau padrão para x é 1
            
            # Verifica se há um grau definido
            if len(partes) > 1 and '**' in partes[1]:
                grau = int(partes[1].split('**')[1])
            
            # Tratando o coeficiente
            if coef_str == '' or coef_str == '+':
                coef = 1
            elif coef_str == '-':
                coef = -1
            else:
                coef = int(coef_str.split('*')[0])  # Ignora multiplicações

            # Atualiza o coeficiente na lista
            coeficientes[grau] += coef
        else:
            # Termo constante
            coeficientes[0] += int(termo)

    return coeficientes[::-1]  # Retorna a lista invertida
