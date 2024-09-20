import scipy.io
import numpy as np

# Carregue o arquivo .mat
path = '/home/joselito/git/Sinais/118e00m.mat'
mat_data = scipy.io.loadmat(path)
duracao = 60  # segundos
fs = 360  # Frequência de amostragem em Hz
ganho = 200
base = 1024
limite = 60
# Acesse a variável 'val'
sinal = mat_data['val'][0, :]
sinal = (sinal-base)/ganho

# Calcule os valores máximo, mínimo e a média do sinal
max_sinal = np.max(sinal)
min_sinal = np.min(sinal)
media_sinal = np.mean(sinal)

# Exiba os resultados
print(f"Valor máximo do sinal: {max_sinal}")
print(f"Valor mínimo do sinal: {min_sinal}")
print(f"Média do sinal: {media_sinal}")

# Exibir os valores das 10 primeiras amostras
print("Primeiras 10 amostras do sinal:")
print(sinal[:100])