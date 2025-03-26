
import pandas as pd
from sqlalchemy import create_engine, text
import yaml
import psycopg2 
from psycopg2 import sql
from airflow.providers.postgres.hooks.postgres import PostgresHook



def load_config(file_path="/home/alejandro/Escritorio/AUTO_AIRFLOW/Dags/config.yaml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)



def extraction():
    # Crear conexión con SQLAlchede la conexión en Airflow
    conn_id = "postgres_proyecto"

    # Crear el hook de conexión
    hook = PostgresHook(postgres_conn_id=conn_id)

    # Obtener la conexión usando get_conn() en lugar de get_sqlalchemy_engine()
    conn = hook.get_conn()

    # Leer datos con pandas usando la conexión directamente
    df = pd.read_sql_query("SELECT * FROM public.tabla_proyecto_etl2", con=conn)

    # Mostrar las primeras filas
    print(df.head())

    # Cerrar la conexión
    conn.close()
    return(df)


def Transformations():
    
    df_eda = extraction()

    # Se cambia el tipo de dato de la columna "release_date" a un tipo de dato "date" con el fin de separar los dias, meses y años de estreno.
    df_eda["release_date"] = pd.to_datetime(df_eda["release_date"], errors="coerce")

    df_eda["release_year"] = df_eda["release_date"].dt.year
    df_eda["release_month"] = df_eda["release_date"].dt.month
    df_eda["release_day"] = df_eda["release_date"].dt.day
    df_eda.drop(columns=["release_date"], inplace=True)

    df_eda["release_year"] = df_eda["release_year"].fillna(0).astype(int)
    df_eda["release_month"] = df_eda["release_month"].fillna(0).astype(int) 
    df_eda["release_day"] = df_eda["release_day"].fillna(0).astype(int)

    df_eda = df_eda[df_eda["release_year"] != 0]

    df_eda = df_eda[df_eda["adult"] != True]

    df_eda.drop(columns=["id"], inplace=True)
    df_eda.drop(columns=["imdb_id"], inplace=True)
    df_eda.drop(columns=["overview"], inplace=True)
    df_eda.drop(columns=["tagline"], inplace=True)
    df_eda.drop(columns=["keywords"], inplace=True)
    df_eda.drop(columns=["production_countries"], inplace=True)
    df_eda.drop(columns=["original_title"], inplace=True)

    df_eda["vote_average"] = df_eda["vote_average"].round(1)

    df_eda = df_eda[df_eda["vote_average"] != 0.0]

    ##df_eda["runtime"] = df_eda["runtime"].apply(lambda x: f"{x // 60}:{x % 60:02d}")

    def formato_(valor):
        if valor >= 1_000_000_000:  # Billones (B)
            return f"{valor / 1_000_000_000:.1f}B"
        elif valor >= 1_000_000:  # Millones (M)
            return f"{valor / 1_000_000:.1f}M"
        elif valor >= 1_000:  # Miles (K)
            return f"{valor / 1_000:.1f}K"
        else:
            return str(valor)  # Número sin cambios

    df_eda["budget_formato"] = df_eda["budget"].apply(formato_)
    df_eda["reveneu_formato"] = df_eda["revenue"].apply(formato_)

    df_eda=df_eda[df_eda["status"] == "Released"]

    df_split = df_eda["genres"].str.split(",", expand=True).iloc[:,:5]


    df_split.columns = [f"genre_{i+1}" for i in range(df_split.shape[1])]


    df_try = df_eda.join(df_split)

    df_try = df_try[df_try["genre_1"] != "0"]
    df_try = df_try.dropna(subset=['genre_1'])

    df_split2 = df_try["spoken_languages"].str.split(",", expand=True).iloc[:,:5]


    df_split2.columns = [f"languaje_{i+1}" for i in range(df_split2.shape[1])]


    df_eda_F = df_try.join(df_split2)

    df_eda_F = df_eda_F[~df_eda_F["production_companies"].astype(str).isin(["0"])]
    df_eda_F.shape
   
    df_split3 = df_eda_F["production_companies"].str.split(",", expand=True).iloc[:,:5]


    df_split3.columns = [f"produces_{i+1}" for i in range(df_split3.shape[1])]


    df_eda_F2 = df_eda_F.join(df_split3)

    df_eda_F2["has_profit"] = (df_eda_F2["revenue"] - df_eda_F2["budget"]) > 0

    print("Se tiene el dataframe melo")

    print(df_eda_F2.dtypes)
    
    df_eda_F2.to_pickle("/tmp/dataset_clean.pkl")
