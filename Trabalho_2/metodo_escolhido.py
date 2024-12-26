import math

def metodo_escolhido(theta0, v0, g, L, h, T):

    # Função para derivadas de segunda ordem
    def f1(theta, v):
        return v

    def f2(theta, v):
        return -(g / L) * math.sin(theta)

    # Condições iniciais
    t = 0
    theta = theta0
    v = v0
    resultados = [(t, theta)]  # Lista para armazenar resultados (tempo, ângulo)

    # Iteração do método de Runge-Kutta
    while t < T:
        k1_theta = h * f1(theta, v)
        k1_v = h * f2(theta, v)

        k2_theta = h * f1(theta + 0.5 * k1_theta, v + 0.5 * k1_v)
        k2_v = h * f2(theta + 0.5 * k1_theta, v + 0.5 * k1_v)

        k3_theta = h * f1(theta + 0.5 * k2_theta, v + 0.5 * k2_v)
        k3_v = h * f2(theta + 0.5 * k2_theta, v + 0.5 * k2_v)

        k4_theta = h * f1(theta + k3_theta, v + k3_v)
        k4_v = h * f2(theta + k3_theta, v + k3_v)

        # Atualiza os valores de theta e v
        theta += (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
        v += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6

        # Incrementa o tempo
        t += h

        # Armazena o resultado atual
        resultados.append((t, theta))

    return resultados
