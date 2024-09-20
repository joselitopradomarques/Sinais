import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

def plot_fft(signal, start_index):
    """
    Calcula a FFT de um sinal, centraliza o espectro, plota e salva a magnitude e a fase.

    Parâmetros:
    - signal: array contendo os valores do sinal a ser transformado
    - start_index: índice inicial para salvar os gráficos (incrementa de 2 em 2)
    """
    # Calcular a Transformada Discreta de Fourier do sinal
    X = fft(signal)
    X_shifted = fftshift(X)
    omega = np.linspace(-np.pi, np.pi, len(signal))

    # Plotar a Magnitude
    plt.figure(figsize=(12, 6))
    plt.plot(omega, np.abs(X_shifted))
    plt.xlabel('Ω')
    plt.ylabel('|X(Ω)|')
    plt.grid(True)
    plt.title(f'Transformada de Fourier (Magnitude) - fig{start_index:02d}.png')
    plt.savefig(f'fig{start_index:02d}.png')
    plt.close()

    # Plotar a Fase
    plt.figure(figsize=(12, 6))
    plt.plot(omega, np.angle(X_shifted))
    plt.xlabel('Ω')
    plt.ylabel('Phase(X(Ω))')
    plt.grid(True)
    plt.title(f'Transformada de Fourier (Fase) - fig{start_index+1:02d}.png')
    plt.savefig(f'fig{start_index+1:02d}.png')
    plt.close()

# Definir o intervalo de n
n = np.arange(500)  # 500 valores de n

# Definir o sinal original x[n]
x = np.exp(-0.1 * (n - 250)**2 / 2)  # Sinal gaussiano centrado em n=250
plot_fft(x, 9)  # Salvará fig09.png e fig10.png (Magnitude e Fase)

# Subamostrar x[2n] (Sinal subamostrado por 2)
x_2 = x[::2]  # Mantém 250 amostras
plot_fft(x_2, 11)  # Salvará fig11.png e fig12.png

# Subamostrar x[4n] (Sinal subamostrado por 4)
x_4 = x[::4]  # Mantém 125 amostras
plot_fft(x_4, 13)  # Salvará fig13.png e fig14.png

# Subamostrar x[5n] (Sinal subamostrado por 5)
x_5 = x[::5]  # Mantém 100 amostras
plot_fft(x_5, 15)  # Salvará fig15.png e fig16.png
