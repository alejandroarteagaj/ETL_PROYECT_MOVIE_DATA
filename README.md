# ETL Class Project

## Autor: Alejandro Arteaga Jaramillo

### Descripción del Proyecto

Este proyecto tiene como objetivo analizar la evolución de la industria cinematográfica mediante la extracción, transformación y carga (ETL) de datos del dataset "Full IMDb Movies Data", disponible en Kaggle. Se busca identificar patrones en el éxito de las películas, cambios en las preferencias del público y la influencia de factores como presupuesto, críticas y estrategias de lanzamiento.

### Problema y Contexto

La industria del cine ha cambiado significativamente debido a avances tecnológicos, la llegada de plataformas de streaming y cambios en la cultura del consumidor. Para entender estas transformaciones, el proyecto se enfoca en responder preguntas clave como:

- ¿Qué factores influyen en el éxito de una película?
- ¿Cómo han cambiado las preferencias del público?
- ¿Cómo afectan el presupuesto y la estrategia de lanzamiento al éxito comercial?
- ¿Cómo han evolucionado las críticas y la percepción del público?

### Descripción del Dataset

El dataset "Full IMDb Movies Data" contiene información detallada sobre películas desde 1990 hasta la actualidad, incluyendo:

- **Variables principales:**
  - id, title, vote_average, vote_count, status, release_date, revenue, runtime, adult, budget, imdb_id, original_language, original_title, overview, popularity, tagline, genres, production_companies, production_countries, spoken_languages, keywords.
- **Cantidad de registros:** 903,263 filas originales, reducidas a aproximadamente 98,000 para optimizar el análisis.

### Proceso ETL

1. **Extracción:**
   - Configuración de la API de Kaggle y descarga del dataset.
   - Descompresión de los archivos y carga en un DataFrame de Pandas.
2. **Transformación:**
   - Reducción del dataset a aproximadamente 98,000 registros para mejorar la eficiencia.
   - Ajuste de la longitud de columnas extensas (ej. Keywords) para evitar problemas en la carga de datos.
3. **Carga:**
   - Creación de una base de datos y tabla en PostgreSQL.
   - Inserción de datos procesados en la base de datos.
   - Validación de la carga mediante consultas en pgAdmin4.

### Herramientas Utilizadas

- **Python** (Pandas, NumPy, SQLAlchemy)
- **PostgreSQL** (pgAdmin4 para validación de datos)
- **Kaggle API** (Extracción del dataset)

### Resultados y Aplicaciones

Este análisis puede ser útil para:

- Identificar tendencias en la industria cinematográfica.
- Desarrollar sistemas de recomendación basados en géneros o valoraciones.
- Evaluar la rentabilidad de las películas según su presupuesto e ingresos.
- Visualizar tendencias en estrenos de películas a lo largo del tiempo.

### Cómo Ejecutar el Proyecto

1. Descargar el dataset desde Kaggle o ejecutar el script de extracción.
2. Descargar la api key de kaggle (Se puede encontrar en la seccion peril)
3. Cambiar las direcciones de ubicacion del archivo .json de kaggle y del directorio donde se desea almacenar el dataset (Celda 1 y 2) 
4. Instalar las dependencias necesarias con:
   ```bash
   pip install pandas numpy sqlalchemy psycopg2 kaggle
   ```
5. Configurar la conexión a PostgreSQL en el código.
6. Ejecutar los notebooks en el siguiente orden:
   - `002_EXTRACT.ipynb` (Extracción y transformación de datos)
7. Verificar los datos en pgAdmin4.
