import csv

def leer_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def obtener_columna(datos, columna):
    return [int(row[columna]) for row in datos if row[columna].isdigit()]

def calcular_percentil(valores, percentil):
    n = len(valores)
    k = (n - 1) * percentil / 100
    f = int(k)
    c = k - f
    if f + 1 < n:
        return valores[f] + (valores[f + 1] - valores[f]) * c
    else:
        return valores[f]

file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
datos = leer_csv(file_path)
columna = 'RecommendationCount'  # Nombre corregido de la columna
valores = obtener_columna(datos, columna)
valores.sort()

ultimo_cuartil = calcular_percentil(valores, 75)
percentil_80 = calcular_percentil(valores, 80)

print(f'Último cuartil (percentil 75) de la columna "{columna}": {ultimo_cuartil}')
print(f'Percentil 80 de la columna "{columna}": {percentil_80}')
