import pandas as pd
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import argparse

# Configura la conexión a la base de datos
DATABASE_URL = 'mysql+pymysql://root:root0000@127.0.0.1/expert_system'
engine = create_engine(DATABASE_URL)

# Consulta para extraer las columnas relevantes
query = """
SELECT city, city_fuel_economy, combine_fuel_economy, engine_cylinders, 
       engine_displacement, engine_type, fuel_tank_volume, fuel_type, 
       highway_fuel_economy, horsepower, price, torque, transmission, year
FROM used_cars_data
"""
df = pd.read_sql(query, engine)

# Preprocesar y limpiar los datos
def limpiar_datos(df):
    def convertir_a_float(valor):
        try:
            return float(valor)
        except (ValueError, TypeError):
            return None

    # Conversión y limpieza
    df['city_fuel_economy'] = df['city_fuel_economy'].apply(convertir_a_float)
    df['highway_fuel_economy'] = df['highway_fuel_economy'].apply(convertir_a_float)
    df['engine_displacement'] = df['engine_displacement'].apply(convertir_a_float)
    df['horsepower'] = df['horsepower'].apply(convertir_a_float)

    # Imputar valores faltantes para 'engine_displacement' y 'horsepower'
    df['engine_displacement'] = df['engine_displacement'].fillna(df['engine_displacement'].mean())
    df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())

    # Eliminación de filas con valores críticos faltantes
    df = df.dropna(subset=['price', 'year'])
    df['price'] = df['price'].apply(lambda x: float(x) if pd.notnull(x) else None)

    return df

df = limpiar_datos(df)

# Separar características y variable objetivo
X = df.drop(columns=['price'])
y = df['price']

# Definir columnas categóricas y numéricas
categorical_features = ['city', 'engine_cylinders', 'engine_type', 'fuel_type', 'transmission']
numerical_features = ['city_fuel_economy', 'highway_fuel_economy', 'engine_displacement', 'horsepower']

# Preprocesamiento de datos
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ]), numerical_features),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_features)
    ])

X_preprocessed = preprocessor.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dense(1)  # Salida continua para la predicción de precios
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=20, validation_split=0.2, verbose=1)

# Función de recomendación basada en el modelo entrenado
def inferir_recomendaciones(df, max_price, min_year=None, engine_type=None, fuel_type=None):
    filtrado = df[df['price'] <= max_price]

    if engine_type:
        filtrado = filtrado[filtrado['engine_type'].str.strip().str.lower() == engine_type.lower()]

    if fuel_type:
        filtrado = filtrado[filtrado['fuel_type'].str.strip().str.lower() == fuel_type.lower()]

    if min_year:
        filtrado = filtrado[filtrado['year'] >= min_year]

    # Preprocesar los datos del filtrado
    X_filtrado = filtrado.drop(columns=['price'])
    X_filtrado_preprocessed = preprocessor.transform(X_filtrado)

    # Realizar predicciones
    filtrado.loc[:, 'predicted_price'] = model.predict(X_filtrado_preprocessed)

    recomendaciones = filtrado.sort_values(by='predicted_price')
    return recomendaciones

# Interfaz de línea de comandos
def main():
    parser = argparse.ArgumentParser(description='Recomendador de Automóviles Usados')
    parser.add_argument('--max_price', type=float, required=True, help='Precio máximo')
    parser.add_argument('--min_year', type=int, help='Año mínimo')
    parser.add_argument('--engine_type', type=str, help='Tipo de motor')
    parser.add_argument('--fuel_type', type=str, help='Tipo de combustible')

    args = parser.parse_args()

    recomendaciones = inferir_recomendaciones(df, args.max_price, args.min_year, args.engine_type, args.fuel_type)
    print("Recomendaciones:")
    print(recomendaciones.to_string(index=False))

if __name__ == '__main__':
    main()