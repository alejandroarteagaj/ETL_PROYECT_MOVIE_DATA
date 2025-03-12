# 🎬 Análisis de la Industria Cinematográfica - Proyecto ETL y EDA

## 📌 Autor: Alejandro Arteaga Jaramillo

## 📖 Descripción del Proyecto

Este proyecto analiza la evolución de la industria cinematográfica mediante un proceso **ETL** (Extracción, Transformación y Carga) y un **Análisis Exploratorio de Datos (EDA)**. Utiliza el dataset **"Full IMDb Movies Data"** de Kaggle para identificar patrones de éxito en las películas, cambios en las preferencias del público y la influencia de factores como presupuesto y estrategias de lanzamiento.

---

## 🎯 Problema y Contexto

La industria del cine ha cambiado significativamente debido a avances tecnológicos y el auge del streaming. Este proyecto busca responder preguntas clave:

✔️ ¿Qué factores influyen en el éxito de una película?  
✔️ ¿Cómo han cambiado las preferencias del público a lo largo del tiempo?  
✔️ ¿Cómo afectan el presupuesto y la estrategia de lanzamiento al rendimiento comercial?  
✔️ ¿Cómo han evolucionado las críticas y la percepción del público?

---

## 🗂️ Descripción del Dataset

El dataset **"Full IMDb Movies Data"** contiene información detallada sobre películas desde 1990 hasta la actualidad.

📌 **Variables principales:**  
`id`, `title`, `vote_average`, `vote_count`, `status`, `release_date`, `revenue`, `runtime`, `adult`, `budget`, `imdb_id`, `original_language`, `genres`, `production_companies`, `keywords`, entre otros.

📌 **Registros:**  
903,263 filas originales, reducidas a ~98,000 para mejorar la eficiencia del análisis.

---

## 🔄 Proceso ETL

### 🔹 1. **Extracción**
- Se configura la API de Kaggle y se descarga el dataset.
- Se descomprime y carga en un DataFrame de Pandas.

### 🔹 2. **Transformación**
- Se reduce el dataset a ~98,000 registros optimizando su manejo.
- Se limpian valores nulos y se ajustan columnas extensas.
- Se convierten los valores textuales `"nan"` en valores adecuados para el análisis.
- Se crean nuevas variables como `has_profit` (si una película generó ganancias).

### 🔹 3. **Carga**
- Se crea una base de datos en PostgreSQL.
- Se inserta el dataset transformado en una tabla.
- Se validan los datos mediante consultas en **pgAdmin4**.

---

## 📊 Análisis Exploratorio de Datos (EDA)

Se realizan distintos análisis visuales y estadísticos para extraer insights de los datos. Algunos puntos clave incluyen:

📌 **Distribución de películas por género:** Identificación de los géneros más frecuentes.  
📌 **Puntuaciones promedio por género:** Evaluación de la percepción del público.  
📌 **Presupuesto promedio por género:** Relación entre inversión y éxito.  
📌 **Comparación de películas con y sin ganancias:** Evaluación de rentabilidad.  

---

## 🛠️ Herramientas Utilizadas

✅ **Lenguajes y Librerías:**  
Python (Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy)  

✅ **Base de Datos:**  
PostgreSQL + pgAdmin4  

✅ **Extracción de Datos:**  
Kaggle API  

✅ **Análisis y Visualización:**  
Jupyter Notebooks  

---

## 🚀 Cómo Ejecutar el Proyecto

1️⃣ **Descargar el dataset** desde Kaggle o ejecutar el script de extracción.  
2️⃣ **Instalar dependencias** con:
   ```bash
   pip install pandas numpy sqlalchemy psycopg2 kaggle matplotlib seaborn
```
3️⃣ Configurar la conexión a PostgreSQL en el código.

4️⃣ Ejecutar los notebooks en el siguiente orden:
- 002_EXTRACT.ipynb → Extracción y transformación de datos.
- EDA.ipynb → Análisis exploratorio de datos.
  
5️⃣ Verificar los resultados en gráficos y consultas SQL.

## 📈 Resultados y Aplicaciones

🔹 Identificar tendencias en la industria del cine.

🔹 Desarrollar sistemas de recomendación de películas.

🔹 Evaluar la rentabilidad de películas según su presupuesto.

🔹 Analizar el impacto del streaming y cambios en preferencias del público.

## 📩 Contacto
📌 Alejandro Arteaga Jaramillo
🔗 LinkedIn | 🐙 GitHub | ✉️ Email
