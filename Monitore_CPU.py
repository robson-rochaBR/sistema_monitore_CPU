import matplotlib.pyplot as plt
import psutil
from matplotlib.animation import FuncAnimation

# Configurando o gráfico
fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('Uso da CPU e Memória', fontsize=20)
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Uso (%)')
cpu_linha, = ax.plot([], [], label='CPU', color='#007de5')
memoria_linha, = ax.plot([], [], label='Memória', color='#7be500')
ax.legend()

# Adicionando textos aos valores da CPU e Memória
cpu_texto = ax.text(0.77, 0.7, '', transform=ax.transAxes)
memoria_texto = ax.text(0.77, 0.7, '', transform=ax.transAxes)

#Função para atualizar o gráfico
def atualizar(frame):
    # Obtendo os dados de uso da CPU e Memória
    uso_cpu = psutil.cpu_percent()
    uso_memoria = psutil.virtual_memory().percent

    # Adicionando os dados ao gráfico
    cpu_linha.set_data(list(range(frame)), [uso_cpu] * frame)
    memoria_linha.set_data(list(range(frame)), [uso_memoria] * frame)

    # Atualizando os textos dos valores da CPU e Memória
    cpu_texto.set_text(f'CPU: {uso_cpu:.1f}%\n')
    memoria_texto.set_text(f'Memória: {uso_memoria:.1f}%')

    return cpu_linha, memoria_linha, cpu_texto, memoria_texto

# Animação o grafico
animacao = FuncAnimation(fig, atualizar, frames=100, interval=1000, blit=True)

# Estilizando as linhas do gráfico
for linha in [cpu_linha, memoria_linha]:
    linha.set_linewidth(4)
    linha.set_marker('_')
    linha.set_markersize(5)

# Estilizando o fundo do grafico
ax.set_facecolor('#F5F5F5')

plt.show()

""" Exemplos de marcadores
    Símbolo	 |   Descrição
    
    [ . ]	    ponto
    [ , ]	    pixel
    [ o ]	    círculo
    [ v ]	    triângulo para baixo
    [ ^ ]	    triângulo para cima
    [ < ]	    triângulo para esquerda
    [ > ]	    triângulo para direita
    [ 1 ]	    triângulo down
    [ 2 ]	    triângulo up
    [ 3 ]	    triângulo left
    [ 4 ]	    triângulo right
    [ s ]	    quadrado
    [ p ]	    pentágono
    [ * ]	    estrela
    [ h ]	    hexágono 1
    [ H ]	    hexágono 2
    [ + ]	    mais
    [ x ]	    cruz
    [ D ]	    diamante
    [ d ]	    diamante fino
    [ ` ]	    `
    [ _ ]	    linha horizontal
"""