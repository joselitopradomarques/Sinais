import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, freqz

# Carregue o arquivo .mat
path = '/home/joselito/git/Sinais/118e00m.mat'
mat_data = scipy.io.loadmat(path)

# Acesse a variável 'val'
sinal = mat_data['val'][0, :]

# Parâmetros do sinal
duracao = 60  # segundos
fs = 360  # Frequência de amostragem em Hz
ganho = 200
base = 1024
limite = 10

# Converta o sinal de unidades brutas para unidades físicas (mV)
#sinal_fisico = (sinal-base)/ganho
sinal_fisico = sinal
# Exibir valores mínimo e máximo do sinal físico
min_sinal_fisico = np.min(sinal_fisico)
max_sinal_fisico = np.max(sinal_fisico)
print(f"Valor mínimo do sinal físico: {min_sinal_fisico}")
print(f"Valor máximo do sinal físico: {max_sinal_fisico}")

# a) Plotar o sinal original
plt.figure(figsize=(12, 6))
plt.plot(np.arange(len(sinal_fisico)) / fs, sinal_fisico)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (Unidade de ADC)')
plt.xlim(0, limite)  # Limitar a visualização a 3 segundos
plt.grid(True)
plt.show()

# b) Inserir ruído branco aditivo gaussiano com SNR de 12 dB
def awgn(signal, snr_db):
    snr = 10 ** (snr_db / 10)
    signal_power = np.mean(signal ** 2)
    noise_power = signal_power / snr
    noise = np.random.normal(0, np.sqrt(noise_power), signal.shape)
    return signal + noise

sinal_ruidoso = awgn(sinal_fisico, 12)

# Plotar o sinal ruidoso
plt.figure(figsize=(12, 6))
plt.plot(np.arange(len(sinal_ruidoso)) / fs, sinal_ruidoso)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (Unidade de ADC)')
plt.xlim(0, limite)  # Limitar a visualização a 3 segundos
plt.grid(True)
plt.show()

# c) Filtro de média móvel de duas amostras
filtro_2 = np.ones(2) / 2
sinal_filtrado_2 = convolve(sinal_ruidoso, filtro_2, mode='same')

# Plotar o sinal resultante da convolução de duas amostras
plt.figure(figsize=(12, 6))
plt.plot(np.arange(len(sinal_filtrado_2)) / fs, sinal_filtrado_2)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (Unidade de ADC)')
plt.xlim(0, limite)  # Limitar a visualização a 3 segundos
plt.grid(True)
plt.show()

# d) Filtro de média móvel de cinco amostras
filtro_5 = np.ones(5) / 5
sinal_filtrado_5 = convolve(sinal_ruidoso, filtro_5, mode='same')

# Plotar o sinal resultante da convolução de cinco amostras
plt.figure(figsize=(12, 6))
plt.plot(np.arange(len(sinal_filtrado_5)) / fs, sinal_filtrado_5)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (Unidade de ADC)')
plt.xlim(0, limite)  # Limitar a visualização a 3 segundos
plt.grid(True)
plt.show()

# e) Inferências sobre os resultados
# (Escreva suas observações aqui após executar o código)

# f) Plotar a magnitude dos filtros média móvel de duas e cinco amostras
# Magnitude dos filtros

# Filtro de duas amostras
w_2, h_2 = freqz(filtro_2)
plt.figure(figsize=(12, 6))
plt.plot(w_2 / np.pi, 20 * np.log10(abs(h_2)), 'b')
plt.xlabel('Frequência Normalizada (π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.show()

# Filtro de cinco amostras
w_5, h_5 = freqz(filtro_5)
plt.figure(figsize=(12, 6))
plt.plot(w_5 / np.pi, 20 * np.log10(abs(h_5)), 'r')
plt.xlabel('Frequência Normalizada (π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.show()

# f) Plotar a fase dos filtros média móvel de duas e cinco amostras
# Fase dos filtros

# Filtro de duas amostras
plt.figure(figsize=(12, 6))
plt.plot(w_2 / np.pi, np.angle(h_2), 'b')
plt.xlabel('Frequência Normalizada (π rad/sample)')
plt.ylabel('Fase (radianos)')
plt.grid()
plt.show()

# Filtro de cinco amostras
plt.figure(figsize=(12, 6))
plt.plot(w_5 / np.pi, np.angle(h_5), 'r')
plt.xlabel('Frequência Normalizada (π rad/sample)')
plt.ylabel('Fase (radianos)')
plt.grid()
plt.show()