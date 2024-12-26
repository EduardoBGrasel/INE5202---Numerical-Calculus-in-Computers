import math
from metodo_escolhido import metodo_escolhido

T = float(input(""))
g = 9.81 # m/s^2
L = 0.1 # meters
theta0 = math.pi/4 # Initial angular position
v0 = 0 # Initial velocity 
t = 0
n = 1000; # Number of discretization steps
h = (T-t)/n
y = metodo_escolhido(theta0, v0, g, L, h, T)
print(f"{y[-1][-1]:.5f}\n")