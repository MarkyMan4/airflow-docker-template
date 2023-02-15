from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='test_dag',
    default_args=default_args,
    description='An example DAG',
    start_date=datetime(2023, 2, 13, 2),
    schedule_interval='@daily'
) as dag:
    echo_task = BashOperator(
        task_id='say_hello',
        bash_command='echo hello'
    )

    sleep_task = BashOperator(
        task_id='sleep_task',
        bash_command='sleep 3',
        depends_on_past=True # cannot run unless echo_task completes successfully
    )

    date_task = BashOperator(
        task_id='date_task',
        bash_command='date',
        depends_on_past=False # can run even if sleep_task fails
    )

    echo_task >> sleep_task
    sleep_task >> date_task

    # if sleep_task and date_task should both run concurrently after echo_task, could do this
    # echo_task >> [sleep_task, date_task]
