# Sistema Experto de Recomendación de Automóviles Usados

Este sistema experto proporciona recomendaciones de automóviles usados basadas en varios criterios, como precio, año, tipo de motor y tipo de combustible. Utiliza una base de datos MySQL para almacenar y consultar datos sobre automóviles usados.

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
5. **Configura la Base de Datos**
   
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
  
   
