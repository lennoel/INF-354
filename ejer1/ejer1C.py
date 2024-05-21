import pandas as pd
import numpy as np
from scipy.stats import mode, gmean

# Cargar el archivo CSV en un DataFrame de pandas
file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
df = pd.read_csv(file_path)

# Seleccionar la columna 'RecommendationCount'
columna = 'RecommendationCount'

# Convertir la columna a valores numéricos, manejando valores faltantes o no numéricos
df[columna] = pd.to_numeric(df[columna], errors='coerce')
valores = df[columna].dropna()
# Calcular la media
media = np.mean(valores)

# Calcular la mediana
mediana = np.median(valores)

# Calcular la moda
resultado_moda = mode(valores)

# Verificar si el resultado es un array o un escalar
if np.isscalar(resultado_moda.mode):
    moda = resultado_moda.mode
else:
    moda = resultado_moda.mode[0]


# Calcular la media geométrica
media_geom = gmean(valores)

print(f'Media: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
print(f'Media geométrica: {media_geom}')