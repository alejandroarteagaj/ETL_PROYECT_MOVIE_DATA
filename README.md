# 🎬 Análisis de la Industria Cinematográfica - Proyecto ETL con Apache Airflow

## 📀 Autor: Alejandro Arteaga Jaramillo

## 📚 Descripción del Proyecto

Este proyecto implementa un pipeline **ETL (Extracción, Transformación y Carga)** automatizado con **Apache Airflow** para analizar la evolución de la industria cinematográfica. Además, se realiza un **Análisis Exploratorio de Datos (EDA)** y se presentan visualizaciones en **Grafana**.

El objetivo es identificar patrones de éxito en las películas, analizar la evolución de preferencias del público y evaluar la influencia del presupuesto en el rendimiento comercial.

---

## 🎯 Problema y Contexto

La industria del cine ha cambiado significativamente debido a avances tecnológicos y el auge del streaming. Este proyecto busca responder preguntas clave:

✔️ ¿Qué factores influyen en el éxito de una película?  
✔️ ¿Cómo han cambiado las preferencias del público a lo largo del tiempo?  
✔️ ¿Cómo afectan el presupuesto y la estrategia de lanzamiento al rendimiento comercial?  
✔️ ¿Cómo han evolucionado las críticas y la percepción del público?  

---

## 📂 Descripción del Dataset

El dataset **"Full IMDb Movies Data"** contiene información detallada sobre películas desde 1990 hasta la actualidad.

📀 **Variables principales:**  
`id`, `title`, `vote_average`, `vote_count`, `status`, `release_date`, `revenue`, `runtime`, `adult`, `budget`, `imdb_id`, `original_language`, `genres`, `production_companies`, `keywords`, entre otros.

📀 **Registros:**  
903,263 filas originales, reducidas a ~98,000 para mejorar la eficiencia del análisis.

---

## 🔄 Proceso ETL con Apache Airflow

### 💡 Arquitectura

El proceso ETL se gestiona mediante **Apache Airflow**, utilizando DAGs para orquestar las tareas.

- **Extracción:** Descarga de datos desde Kaggle y APIs externas.
- **Transformación:** Limpieza de datos con Pandas y generación de nuevas variables.
- **Carga:** Inserción de datos en PostgreSQL para su análisis y visualización en Grafana.

### 🔹 Estructura del DAG

```plaintext
etl_movies_dag
|
|-- task_extract_data  (Extrae los datos de Kaggle)
|-- task_transform_data (Limpia y procesa los datos con Pandas)
|-- task_load_data (Carga los datos en PostgreSQL)
|-- task_validate_data (Ejecuta validaciones sobre los datos cargados)
```

### 🔹 Archivos clave

- `dags/etl_movies.py` - Define el DAG y sus tareas.
- `scripts/extract.py` - Maneja la extracción de datos.
- `scripts/transform.py` - Realiza la limpieza y transformación.
- `scripts/load.py` - Inserta los datos en PostgreSQL.

---

## 📊 Visualización con Grafana

Los datos procesados se visualizan en **Grafana**, permitiendo el análisis de:

- **Distribución de películas por género**.
- **Puntuaciones promedio por género**.
- **Presupuesto promedio por género**.
- **Comparación de rentabilidad de películas**.

Los dashboards se conectan a la base de datos PostgreSQL para extraer los datos en tiempo real.

---

## 🛠️ Instalación y Ejecución

### 👉 Prerrequisitos

- **Python 3.8+**
- **Apache Airflow 2.7+**
- **PostgreSQL 14+**
- **Grafana**

### 👉 Configuración de Carpetas y Rutas

Antes de ejecutar Airflow o los scripts, es necesario:

1. **Crear la carpeta `config/`** y colocar dentro el archivo `kaggle.json` para autenticar la descarga de datos.
2. **Crear la carpeta `data/`** donde se almacenará el dataset descargado y procesado.
3. **Configurar la ruta de trabajo** en Airflow y en los scripts ETL para que apunten a las carpetas correctas.

### 👉 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/alejandroarteagaj/ETL_PROYECT_MOVIE_DATA.git
cd ETL_PROYECT_MOVIE_DATA

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 👉 Ejecutar Apache Airflow

```bash
# Inicializar la base de datos de Airflow
airflow db init

# Crear un usuario administrador
airflow users create \
    --username admin \
    --firstname Alejandro \
    --lastname Arteaga \
    --role Admin \
    --email admin@example.com

# Iniciar el scheduler y webserver
airflow scheduler &
airflow webserver &
```

### 👉 Ejecutar el DAG ETL en Airflow

1. Abre Airflow en el navegador: [http://localhost:8080](http://localhost:8080).
2. Habilita y ejecuta el DAG `etl_movies_dag`.
3. Verifica la carga de datos en PostgreSQL.

---

## 📩 Contacto
📌 Alejandro Arteaga Jaramillo
🔗 LinkedIn | 🐙 GitHub | ✉️ Email


