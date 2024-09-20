import numpy as np
import matplotlib.pyplot as plt

# Sinais
x = np.array([3, 11, 7, 0, -1, 4, 2])
h = np.array([2, 3, 0, -5, 2, 1])

# Convolução x * h
y1 = np.convolve(x, h)

# Convolução h * x (ordem invertida)
y2 = np.convolve(h, x)

# Gráfico para y1 = conv(x, h)
plt.figure()
plt.stem(y1)
plt.tight_layout()
plt.show()

# Gráfico para y2 = conv(h, x)
plt.figure()
plt.stem(y2)
plt.tight_layout()
plt.show()

def convolute(x, h, nx, nh):
    nymin = nx[0] + nh[0]
    nymax = nx[-1] + nh[-1]
    ny = np.arange(nymin, nymax + 1)
    y = np.convolve(x, h)
    return y, ny

# Definição de nx e nh
nx = np.arange(-3, 4)  # [-3, -2, -1, 0, 1, 2, 3]
nh = np.arange(-1, 5)  # [-1, 0, 1, 2, 3, 4]

# Convolução com função modificada
y, ny = convolute(x, h, nx, nh)

# Gráfico do resultado
plt.figure()
plt.stem(ny, y)
plt.tight_layout()
plt.show()

# Criação do sinal x
nx = np.arange(0, 101)
x = np.sin(2 * np.pi * nx / 50) + np.sin(20 * np.pi * nx / 50)

# Visualização do sinal original
plt.figure()
plt.stem(nx, x)
plt.xlabel('Índices de Tempo')  # Nome do eixo X
plt.ylabel('Amplitude')          # Nome do eixo Y
#plt.title('Sinal x')            # Título do gráfico
plt.tight_layout()
plt.show()

# Definição de h2
nh2 = np.arange(0, 10)
h2 = 0.1 * np.ones(10)

# Gráfico do filtro h2
plt.figure()
plt.stem(nh2, h2)
plt.xlabel('Índices de Tempo')  # Nome do eixo X
plt.ylabel('Amplitude')          # Nome do eixo Y
#plt.title('Filtro h2')           # Título do gráfico
plt.tight_layout()
plt.show()

# Criação do sinal x para a convolução
nx = np.arange(0, 101)
x = np.sin(2 * np.pi * nx / 50) + np.sin(20 * np.pi * nx / 50)

# Convolução de x com h2
y = np.convolve(x, h2)

# Gráfico do resultado da convolução
plt.figure()
plt.stem(y)
plt.xlabel('Índices de Tempo')  # Nome do eixo X
plt.ylabel('Amplitude')          # Nome do eixo Y
#plt.title('Convolução de x com h2')  # Título do gráfico
plt.tight_layout()
plt.show()