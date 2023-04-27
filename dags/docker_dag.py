from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 0
}

@dag(default_args=default_args, description='Run a docker image as a task', start_date=datetime(2023, 1, 1), schedule_interval='@daily')
def docker_dag():
    echo_task = BashOperator(
        task_id='say_hello',
        bash_command='echo about to run docker image'
    )

    docker_task = DockerOperator(
        task_id='docker_command',
        image='markusregistry.azurecr.io/simple-data-flow:fa6601b840efc70d96cb51e8d22cd8cc6dc65d4d',
        api_version='auto',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        do_xcom_push=False
    )

    echo_task >> docker_task

dag = docker_dag()
