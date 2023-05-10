import numpy as np
import matplotlib.pyplot as plt

# Dados do problema
t = np.linspace(0, 1000, 100)  # Valores de tempo de 0 a 1000 minutos
Va = 200 + 3 * t
Vb = 5000 - 3 * t

# Criação do gráfico
plt.plot(t, Va, label='Reservatório A')
plt.plot(t, Vb, label='Reservatório B')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Volume (litros)')
plt.title('Volume dos Reservatórios A e B ao longo do tempo')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()
