import pandas as pd
from sqlalchemy import create_engine, text
import yaml
import psycopg2 
from psycopg2 import sql
import numpy as np 
def load_config(file_path="/home/alejandro/Escritorio/AUTO_AIRFLOW/Dags/config.yaml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def create_table_postgres2():
    config = load_config()
    db_config = config["database"]
    
    db_user = db_config["user"]
    db_password = db_config["password"]
    db_host = db_config["host"]
    db_port = db_config["port"]
    db_name = db_config["name"]

    conn = psycopg2.connect(
        dbname="postgres",
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    conn.autocommit = True
    df_clean = pd.read_pickle("/tmp/dataset_clean.pkl")

    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS tabla_clean (
                title VARCHAR(1000),
                vote_average FLOAT,
                vote_count BIGINT,
                status VARCHAR(255),
                revenue BIGINT,
                runtime BIGINT,
                adult BOOL,       
                budget BIGINT,
                original_language VARCHAR(1000),                    
                popularity FLOAT,
                genres VARCHAR(1000),
                production_companies VARCHAR(1000),
                spoken_languages VARCHAR(1000),
                release_year BIGINT,
                release_month BIGINT,
                release_day BIGINT,
                budget_formato VARCHAR(1000),
                reveneu_formato  VARCHAR(1000),
                genre_1 VARCHAR(255),
                genre_2 VARCHAR(255),                  
                genre_3 VARCHAR(255),
                genre_4 VARCHAR(255),
                genre_5 VARCHAR(255),
                languaje_1 VARCHAR(255),           
                languaje_2 VARCHAR(255),              
                languaje_3 VARCHAR(255),              
                languaje_4 VARCHAR(255),             
                languaje_5 VARCHAR(255),
                produces_1 VARCHAR(255),              
                produces_2 VARCHAR(255),              
                produces_3 VARCHAR(255),             
                produces_4 VARCHAR(255),              
                produces_5 VARCHAR(255),              
                has_profit BOOL                                                    
            );
        """))

        print("Tabla 'tabla_clean' creada exitosamente en PostgreSQL.")

     
        conn.execute(text("TRUNCATE TABLE tabla_clean;"))
        print("Datos antiguos eliminados antes de insertar los nuevos.")


        # Verificar si release_year está en df_clean
    if "release_year" not in df_clean.columns:
        raise ValueError("La columna 'release_year' no está presente en df_clean")

    # Reemplazar valores NaN con un valor por defecto (por ejemplo, -1 o NULL)
    df_clean = df_clean.fillna({"release_year": np.nan, "release_month": np.nan, "release_day": np.nan})


    # Verificar si hay valores nulos antes de la inserción
    print(df_clean.isnull().sum())

    with engine.connect() as conn:
        stmt = text("""
            INSERT INTO tabla_clean (
                title, vote_average, vote_count, status, revenue, runtime, adult, budget, 
                original_language, popularity, genres, production_companies, spoken_languages, 
                release_year, release_month, release_day, budget_formato, reveneu_formato, 
                genre_1, genre_2, genre_3, genre_4, genre_5, 
                languaje_1, languaje_2, languaje_3, languaje_4, languaje_5, 
                produces_1, produces_2, produces_3, produces_4, produces_5, 
                has_profit
            ) 
            VALUES (
                :title, :vote_average, :vote_count, :status, :revenue, :runtime, :adult, :budget, 
                :original_language, :popularity, :genres, :production_companies, :spoken_languages, 
                :release_year, :release_month, :release_day, :budget_formato, :reveneu_formato, 
                :genre_1, :genre_2, :genre_3, :genre_4, :genre_5, 
                :languaje_1, :languaje_2, :languaje_3, :languaje_4, :languaje_5, 
                :produces_1, :produces_2, :produces_3, :produces_4, :produces_5, 
                :has_profit
            )
        """)

        conn.execute(stmt, df_clean.to_dict(orient="records"))  

        print("Los datos se cargaron exitosamente")
