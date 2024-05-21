import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de pandas
file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
df = pd.read_csv(file_path)

# Seleccionar la columna 'RecommendationCount'
columna = 'RecommendationCount'

# Convertir la columna a valores numéricos, manejando valores faltantes o no numéricos
df[columna] = pd.to_numeric(df[columna], errors='coerce')
valores = df[columna].dropna()

# Graficar un histograma de 'RecommendationCount'
plt.figure(figsize=(12, 6))
plt.hist(valores, bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribución de RecommendationCount')
plt.xlabel('RecommendationCount')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
