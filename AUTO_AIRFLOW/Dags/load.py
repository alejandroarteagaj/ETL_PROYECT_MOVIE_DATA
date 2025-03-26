import os
from sqlalchemy import create_engine, text
import pandas as pd
import yaml
import psycopg2 
from psycopg2 import sql

def load_config(file_path="/home/alejandro/Escritorio/AUTO_AIRFLOW/Dags/config.yaml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def create_table_postgres():
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
    df = pd.read_pickle("/tmp/dataset_procesado.pkl")

    try:
        with conn.cursor() as cur:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            print(f"Base de datos '{db_name}' creada exitosamente.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"La base de datos '{db_name}' ya existe.")

    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS tabla_proyecto_ETL2 (
                id BIGINT,
                title VARCHAR(1000),
                vote_average FLOAT,
                vote_count BIGINT,
                status VARCHAR(255),
                release_date VARCHAR(1000),
                revenue BIGINT,
                runtime BIGINT,
                adult BOOL,       
                budget BIGINT,
                imdb_id VARCHAR(1000),
                original_language VARCHAR(1000),                    
                original_title VARCHAR(1000),
                overview VARCHAR(1000),
                popularity FLOAT,
                tagline VARCHAR(1000),
                genres VARCHAR(1000),
                production_companies VARCHAR(1000),
                production_countries VARCHAR(1000),
                spoken_languages VARCHAR(1000),
                keywords VARCHAR(1000)                              
            );
        """))

        print("Tabla 'tabla_proyecto_ETL2' creada exitosamente en PostgreSQL.")

     
        conn.execute(text("TRUNCATE TABLE tabla_proyecto_ETL2;"))
        print("Datos antiguos eliminados antes de insertar los nuevos.")

    with engine.connect() as conn:
        stmt = text("""
        INSERT INTO tabla_proyecto_ETL2 
        (id, title, vote_average, vote_count, status, release_date, revenue, runtime, adult, budget, imdb_id, 
        original_language, original_title, overview, popularity, tagline, genres, production_companies, 
        production_countries, spoken_languages, keywords)
        VALUES (:id, :title, :vote_average, :vote_count, :status, :release_date, :revenue, :runtime, :adult, 
        :budget, :imdb_id, :original_language, :original_title, :overview, :popularity, :tagline, :genres, 
        :production_companies, :production_countries, :spoken_languages, :keywords)
        """)

        conn.execute(stmt, df.to_dict(orient="records"))  
       
    print("Los datos se cargaron exitosamente")

    



