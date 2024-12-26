def read_poly(n):
    P = ''  # Inicializa P fora do loop
    for expoente in range(n, 0, -1):
        const = int(input(""))
        if const >= 0:
            if P:  # Se P não está vazio, adiciona o sinal de +
                P += f'+{const}*x**{expoente}'
            else:  # Se P está vazio, apenas adiciona o termo
                P += f'{const}*x**{expoente}'
        else:
            P += f'{const}*x**{expoente}'

    # Solicita o coeficiente para x^0 (termo constante)
    const = int(input(""))
    if const >= 0:
        if P:  # Se P não está vazio, adiciona o sinal de +
            P += f'+{const}'
        else:  # Se P está vazio, apenas adiciona o termo
            P += f'{const}'
    else:
        P += f'{const}'

    return P

