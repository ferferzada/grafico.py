import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dados do problema
t = np.linspace(0, 1000, 100)  # Valores de tempo de 0 a 1000 minutos
Va = 200 + 3 * t
Vb = 5000 - 3 * t

# Criação do gráfico
fig, ax = plt.subplots()
line_a, = ax.plot([], [], label='Reservatório A')
line_b, = ax.plot([], [], label='Reservatório B')
ax.set_xlim(0, 1000)
ax.set_ylim(0, 5500)
ax.set_xlabel('Tempo (minutos)')
ax.set_ylabel('Volume (litros)')
ax.set_title('Volume dos Reservatórios A e B ao longo do tempo')
ax.legend()
ax.grid(True)

# Função de animação
def update(frame):
    if frame >= len(t):
        return
    line_a.set_data(t[:frame], Va[:frame])
    line_b.set_data(t[:frame], Vb[:frame])
    if t[frame] >= 800:
        anim.event_source.stop()
        ax.axhline(y=800, color='r', linestyle='--')  # Adiciona uma linha horizontal para indicar o valor de 800 minutos
        ax.text(800, 800, '800 min', ha='right', va='bottom')  # Adiciona um texto com o valor de 800 minutos

# Criação da animação
anim = animation.FuncAnimation(fig, update, frames=len(t), interval=50)

# Exibição da animação
plt.show()
