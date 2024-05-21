import pandas as pd
import numpy as np



# Cargar el archivo CSV en un DataFrame de pandas
file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
df = pd.read_csv(file_path)

# Seleccionar la columna 'RecommendationCount'
columna = 'RecommendationCount'

# Convertir la columna a valores numéricos, manejando valores faltantes o no numéricos
df[columna] = pd.to_numeric(df[columna], errors='coerce')
valores = df[columna].dropna()

# Calcular el último cuartil (percentil 75) y el percentil 80 usando numpy
ultimo_cuartil = np.percentile(valores, 75)
percentil_80 = np.percentile(valores, 80)

print(f'Último cuartil (percentil 75) de la columna "{columna}": {ultimo_cuartil}')
print(f'Percentil 80 de la columna "{columna}": {percentil_80}')



