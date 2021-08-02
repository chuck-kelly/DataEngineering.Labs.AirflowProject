from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

from package.graph_points_gained_during_season import script

with DAG('dag_1',start_date = datetime(2021, 7, 29), schedule_interval= timedelta(days = 1)) as dag:

    run_the_script = PythonOperator(
        task_id='running_script',
        python_callable=script
    )
    run_the_script
