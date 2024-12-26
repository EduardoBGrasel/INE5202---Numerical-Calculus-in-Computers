import math

def compute_root(func, intervalo):
    # Avalia a função nos extremos do intervalo
    a = parse_polynomial(func, intervalo[0])
    b = parse_polynomial(func, intervalo[1])
    
    if a * b <= 0:  # Verifica se há uma raiz no intervalo
        valor = falsa_posicao(func, intervalo)
    else:
        # Define aproximações iniciais para o método das secantes
        x0 = (intervalo[0] + intervalo[1]) / 2
        x1 = x0 + 0.01
        valor = secantes(func, x0, x1)
    
    return valor

def parse_polynomial(pol, x):
    # Avalia o polinômio na variável x
    return eval(pol.replace("x", f"({x})"))

def falsa_posicao(pol, interval, erro=1e-6, max_interactions=10000):
    i = 0
    a, b = interval
    fa = parse_polynomial(pol, a)
    fb = parse_polynomial(pol, b)


    if fa * fb > 0:
        raise ValueError("O intervalo inicial não contém uma raiz.")

    while True:
        i += 1
        # Ponto de interseção
        xk = a - (fa * (b - a)) / (fb - fa)
        fk = parse_polynomial(pol, xk)

        # Atualiza o intervalo com base no sinal de fk
        if fa * fk < 0:
            b = xk
            fb = fk
        elif fb * fk < 0:
            a = xk
            fa = fk
        else:
            # Retorna xk e a avaliação da função nesse ponto
            return round(xk, 6), round(fk, 6)

        # Critérios de parada
        if abs(fk) < erro or i >= max_interactions:
            return round(xk, 6), round(fk, 6)

def secantes(pol, x0, x1, erro=1e-6, max_interactions=5000):
    i = 0
    while True:
        i += 1
        f0 = parse_polynomial(pol, x0)
        f1 = parse_polynomial(pol, x1)

        if f1 - f0 == 0:
            raise ValueError("Divisão por zero na fórmula das secantes.")
        xk = x1 - f1 * (x1 - x0) / (f1 - f0)
        fk = parse_polynomial(pol, xk)

        # Critérios de parada
        if abs(fk) < erro or i >= max_interactions:
            return round(xk, 6), round(fk, 6)

        # Atualiza x0 e x1
        x0, x1 = x1, xk

