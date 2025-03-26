import os
import zipfile
import subprocess
import pandas as pd

def download():
    download_path = "/home/alejandro/Escritorio/AUTO_AIRFLOW/Data"
    zip_path = os.path.join(download_path, "imdb-data.zip")
    extract_path = download_path

    os.makedirs(download_path, exist_ok=True)

    # Eliminar archivos previos
    if os.path.exists(zip_path):
        os.remove(zip_path)
    
    for file in os.listdir(extract_path):
        file_path = os.path.join(extract_path, file)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
    
    # Configurar API Key para Kaggle CLI
    os.environ["KAGGLE_CONFIG_DIR"] = "/home/alejandro/Escritorio/AUTO_AIRFLOW/Config"
    os.environ["PATH"] += os.pathsep + "/home/airflow/.local/bin"
    
    print("Usuario actual:", os.environ.get("USER") or os.environ.get("LOGNAME"))
    
    # Descargar dataset usando Kaggle CLI
    subprocess.run([
        "kaggle", "datasets", "download", "-d", "anandshaw2001/imdb-data", "-p", download_path, "--force"
    ], check=True)
    
    # Extraer el archivo ZIP    
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    
    extracted_files = [f for f in os.listdir(extract_path) if f.endswith(".csv")]
    
    if not extracted_files:
        raise FileNotFoundError("No se encontró ningún archivo CSV en el dataset extraído.")
    
    csv_path = os.path.join(extract_path, extracted_files[0])  # Tomar el primer CSV encontrado
    
    # Cargar el CSV en un DataFrame
    df = pd.read_csv(csv_path)
    
    num_filas_a_eliminar = 500000  
    filas_a_eliminar = df.sample(n=num_filas_a_eliminar, random_state=42).index
    df = df.drop(filas_a_eliminar).reset_index(drop=True)
    
    df['keywords'] = df['keywords'].astype(str).str[:1000]
    df['production_companies'] = df['production_companies'].astype(str).str[:1000]
    df['overview'] = df['overview'].astype(str).str[:1000]
    df['genres'] = df['genres'].astype(str).str[:1000]
    df['production_countries'] = df['production_countries'].astype(str).str[:1000]
    df['spoken_languages'] = df['spoken_languages'].astype(str).str[:1000]
    
    print(f"Dataset descargado, extraído y cargado desde: {csv_path}")
    df.to_pickle("/tmp/dataset_procesado.pkl")