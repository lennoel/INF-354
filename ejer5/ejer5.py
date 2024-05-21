import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, Normalizer, Binarizer
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import openpyxl
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Cargar el archivo CSV en un DataFrame de pandas
file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
df = pd.read_csv(file_path)

# Limpiar los nombres de las columnas
df.columns = df.columns.str.strip()

# Verificar las columnas cargadas
print(df.columns)
print(df.head())

# Imputación de valores faltantes
imputer = SimpleImputer(strategy='mean')
df[['Metacritic', 'RecommendationCount', 'PriceInitial']] = imputer.fit_transform(df[['Metacritic', 'RecommendationCount', 'PriceInitial']])

# OneHotEncoder para las columnas de género
genres = df[['GenreIsNonGame', 'GenreIsIndie', 'GenreIsAction', 'GenreIsAdventure',
             'GenreIsCasual', 'GenreIsStrategy', 'GenreIsRPG', 'GenreIsSimulation',
             'GenreIsEarlyAccess', 'GenreIsFreeToPlay', 'GenreIsSports',
             'GenreIsRacing', 'GenreIsMassivelyMultiplayer']]
encoder = OneHotEncoder(drop='first')
genres_encoded = encoder.fit_transform(genres).toarray()
genres_encoded_df = pd.DataFrame(genres_encoded, columns=encoder.get_feature_names_out(genres.columns))
df = pd.concat([df, genres_encoded_df], axis=1)
df.drop(columns=genres.columns, inplace=True)

# Escalado de las columnas numéricas
scaler = StandardScaler()
df[['Metacritic', 'RecommendationCount', 'PriceInitial']] = scaler.fit_transform(df[['Metacritic', 'RecommendationCount', 'PriceInitial']])

# Normalización de las características
normalizer = Normalizer()
df[['Metacritic', 'RecommendationCount', 'PriceInitial']] = normalizer.fit_transform(df[['Metacritic', 'RecommendationCount', 'PriceInitial']])
# Seleccionar las características y la variable objetivo
X = df.drop(columns=['ResponseName', 'ReleaseDate', 'IsFree'])
y = df['IsFree']

# Crear y entrenar el árbol de decisión
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

# Visualizar el árbol de decisión
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=['Not Free', 'Free'], filled=True)
plt.title("Árbol de Decisión")
plt.show()
# Extraer información del árbol
tree_info = clf.tree_

# Crear un DataFrame con la información de los nodos
nodes = []

for i in range(tree_info.node_count):
    node = {
        'node': i,
        'feature': X.columns[tree_info.feature[i]] if tree_info.feature[i] != -2 else 'Leaf',
        'threshold': tree_info.threshold[i],
        'impurity': tree_info.impurity[i],
        'n_samples': tree_info.n_node_samples[i],
        'n_samples_split': tree_info.weighted_n_node_samples[i],
        'value': tree_info.value[i],
        'class': y.unique()[tree_info.value[i].argmax()]
    }
    nodes.append(node)

# Crear un DataFrame de nodos
df_nodes = pd.DataFrame(nodes)

# Guardar el DataFrame en un archivo de Excel
output_file = 'C:/Users/Anarquia-87/Downloads/decision_tree_nodes.xlsx'
df_nodes.to_excel(output_file, index=False)

print(f"Árbol de decisión guardado en {output_file}")