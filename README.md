# Sistema Experto de Recomendación de Automóviles Usados

Este sistema experto proporciona recomendaciones de automóviles usados basadas en varios criterios, como precio, año, tipo de motor y tipo de              combustible. Utiliza una base de datos MySQL para almacenar y consultar datos sobre automóviles usados.

## Requisitos

- Python 3.7 o superior
- Bibliotecas de Python: `pandas`, `sqlalchemy`, `pymysql`, `argparse`, `scikit-learn`, `tensorflow`, `keras`
- MySQL Server

## Instalación

1. **Clona el Repositorio**

   ```bash
   git clone https://github.com/ASPXE/ExpertSystemV2.git
   cd ExpertSystemV2
   ```
2. **Crea el entorno virtual de Python**
   ```bash
   python -m venv venv
   ```

4. **Activa el entorno virtual**
   
   En windows:
   ```bash
   venv\Scripts\activate
   ```
   En MacOS/Linux:
   ```bash
   source venv/bin/activate
   ```
5. **Instala las librerías de Python**
   ```bash
   pip install pymysql
   pip install pandas
   pip install sqlalchemy
   pip install argparse
   pip install scikit-learn
   pip install tensorflow
   pip install keras
   ```
   
6. **Configura la Base de Datos**
   
     En el siguiente link podrá encontrar la carpeta .zip que contiene el SQL necesario para crear la base de datos e insertar los registros.
  Link: https://drive.google.com/file/d/1YiVuK1DlCDJAHiYOYTFuFu791BWPWdTh/view?usp=drive_link
  Recuerde cambiar los datos de conexión del archivo main.py para que se conecte a su base de datos.

## Como ejecutar el sistema experto

Es necesario pasar los argumentos al ejecutar el script, use el siguiente ejemplo como referencia:

```bash
   python main.py --max_price 20000 --min_year 2015 --engine_type V6 --fuel_type Gasoline
```

## Vídeos del funcionamiento

Puede ver el funcionamiento del sistema experto en los siguientes vídeos.

Parte 1: https://youtu.be/4SlOshVV-Pw

Parte 2: https://youtu.be/6His0IGlT3k

## Conclusión

   Seleccionar las columnas que sean útiles para entrenar a la red neuronal es una tarea complicada, ya que podemos mejorar o empeorar los resultados de la predicción del precio del vehículo. La utilidad que tiene predecir el precio con base en las características que se han seleccionado de los vehículos nos da la posibilidad de evitar comprar un vehículo a precio inflado.

   Aumentar el número de epochs mejora sustancialmente los resultados de predicción de la red neuronal asi como el número de neuronas en la capa de entrada y las posteriores capas ocultas. Hay que tener en cuenta la capacidad de procesamiento de nuestra computadora ya que el entrenamiento de la red neuronal requiere de mucho poder de cómputo.

   La información con la que entrenamos la red neuronal debe de estar "limpia" de datos que no sean relevantes. Uno de los problemas con el que me encontré es que el dataset original tiene un peso de 9.20GB y muchos registros no tienen información en la mayoría de las columnas, y hacer el pre-procesamiento del CSV directamente con pandas no era viable ya que mi computadora no era capaz de funcionar con normalidad mientras se cargaba en CSV a la variables.
