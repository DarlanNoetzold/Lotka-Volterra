import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


y0 = [10,1] # Número de indivíduos na casa dos milhares

t = np.linspace(0,50,num=1000) # espaço de tempo

alpha = 1.1   # Crescimento da população de presas na ausência de predadores
beta = 0.4    # Taxa de decréscimo da população de presas ao encontrar um predador
delta = 0.1   # Taxa de crescimento da população de predadores ao encontrar uma presa
gamma = 0.4   # Decréscimo da população de predadores na ausência de presas


params = [alpha, beta, delta, gamma]

def sim(variables,t, params):
    x = variables[0] #presa
    y = variables[1] #predador

    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y

    return([dxdt, dydt])

y = odeint(sim, y0, t, args=(params,))

f,(ax1,ax2) = plt.subplots(2)

line1, = ax1.plot(t,y[:,0], color="b")
line2, = ax2.plot(t,y[:,1], color="r")

ax1.set_ylabel("Presa (hundreds)")
ax2.set_ylabel("Predador (hundreds)")
ax2.set_xlabel("Time")

plt.show()