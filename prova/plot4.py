import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
fs = 256  # Frequência de amostragem
N = 512   # Tamanho da FFT

# Criação do sinal x
nx = np.arange(0, 101)
x = np.sin(2 * np.pi * nx / 50) + np.sin(20 * np.pi * nx / 50)

# Plot do sinal x no domínio do tempo
plt.figure()
plt.stem(nx, x)
plt.xlabel('Índices de Tempo')
plt.ylabel('Amplitude')
plt.title('Sinal x no Domínio do Tempo')
plt.grid()
plt.tight_layout()
plt.show()

# FFT do sinal x
fx = np.fft.fft(x, N)
fxmag = np.abs(fx[:N//2])  # Magnitude da FFT

# Frequências correspondentes
freq = np.arange(0, fs/2, fs/N)

# Plot do espectro de magnitude de x
plt.figure()
plt.stem(freq, fxmag)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
#plt.title('Espectro de Magnitude de x')
plt.grid()
plt.tight_layout()
plt.show()

# Definição de h2
nh2 = np.arange(0, 10)
h2 = 0.1 * np.ones(10)

# Plot do filtro h2 no domínio do tempo
plt.figure()
plt.stem(nh2, h2)
plt.xlabel('Índices de Tempo')
plt.ylabel('Amplitude')
plt.title('Filtro h2 no Domínio do Tempo')
plt.grid()
plt.tight_layout()
plt.show()

# Convolução de x com h2
y = np.convolve(x, h2)

# FFT do sinal convoluído y
fy = np.fft.fft(y, N)
fymag = np.abs(fy[:N//2])  # Magnitude da FFT

# Plot do espectro de magnitude de y
plt.figure()
plt.stem(freq, fymag)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
#plt.title('Espectro de Magnitude de y (Convolução de x com h2)')
plt.grid()
plt.tight_layout()
plt.show()
