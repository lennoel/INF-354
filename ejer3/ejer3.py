import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, Normalizer, Binarizer
from sklearn.impute import SimpleImputer

# Cargar el archivo CSV en un DataFrame de pandas
file_path = 'C:/Users/Anarquia-87/Downloads/Nueva carpeta (51)/games-features-edit.csv'
df = pd.read_csv(file_path)

pd.set_option('display.max_columns', None)

# Estrategia 1: Imputación de valores faltantes
imputer = SimpleImputer(strategy='mean')
df[['Metacritic', 'RecommendationCount', 'PriceInitial']] = imputer.fit_transform(df[['Metacritic', 'RecommendationCount', 'PriceInitial']])

# Estrategia 2: OneHotEncoder para las columnas de género
genres = df[['GenreIsNonGame', 'GenreIsIndie', 'GenreIsAction', 'GenreIsAdventure',
             'GenreIsCasual', 'GenreIsStrategy', 'GenreIsRPG', 'GenreIsSimulation',
             'GenreIsEarlyAccess', 'GenreIsFreeToPlay', 'GenreIsSports',
             'GenreIsRacing', 'GenreIsMassivelyMultiplayer']]
encoder = OneHotEncoder(drop='first')
genres_encoded = encoder.fit_transform(genres).toarray()
genres_encoded_df = pd.DataFrame(genres_encoded, columns=encoder.get_feature_names_out(genres.columns))
df = pd.concat([df, genres_encoded_df], axis=1)
df.drop(columns=genres.columns, inplace=True)

# Estrategia 3: Escalado de las columnas numéricas
scaler = StandardScaler()
df[['Metacritic', 'RecommendationCount', 'PriceInitial']] = scaler.fit_transform(df[['Metacritic', 'RecommendationCount', 'PriceInitial']])

# Estrategia 4: Normalización de las características
normalizer = Normalizer()
df[['Metacritic', 'RecommendationCount', 'PriceInitial']] = normalizer.fit_transform(df[['Metacritic', 'RecommendationCount', 'PriceInitial']])

# Estrategia 5: Binarización de la columna 'PriceInitial' como ejemplo
binarizer = Binarizer(threshold=0.5)
df['PriceInitial_binarized'] = binarizer.fit_transform(df[['PriceInitial']])

# Mostrar el DataFrame resultante
print(df.head(18))
