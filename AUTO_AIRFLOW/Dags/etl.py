from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from download import download
from load import create_table_postgres
from transformation import Transformations
from load_visual import create_table_postgres2
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 13),  # Update the start date to today or an appropriate date
    }

with DAG(
    'etl_dag',
    default_args=default_args,
    description='Dag for etl process',  
    schedule_interval='@daily'  # Set the schedule interval as per your requirements
) as dag:
    
    download_task = PythonOperator(
    task_id="download_dataset",
    python_callable=download
)
    load_task = PythonOperator(
        task_id='extract_task',
        python_callable=create_table_postgres
    )

    Tranfo_task = PythonOperator(
        task_id='tranfo_task',
        python_callable=Transformations
    )

    Clean_dataframe = PythonOperator(
        task_id='storage_clean_task',
        python_callable = create_table_postgres2
    ) 


    download_task >> load_task >> Tranfo_task >> Clean_dataframe