import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, Normalizer
from sklearn.impute import SimpleImputer

# Cargar el archivo CSV en un DataFrame de pandas
file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
df = pd.read_csv(file_path)

# Limpiar los nombres de las columnas
df.columns = df.columns.str.strip()

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
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Seleccionar las características y la variable objetivo
X = df.drop(columns=['ResponseName', 'ReleaseDate', 'IsFree'])
y = df['IsFree']

# Crear y entrenar el árbol de decisión
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

# Mostrar el árbol usando matplotlib
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=['Not Free', 'Free'], filled=True, rounded=True)
plt.title("Árbol de Decisión")
plt.show()
