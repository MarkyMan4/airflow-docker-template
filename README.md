## Setup
`$ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env` \
`$ docker compose up airflow-init`

## Run Airflow
`$ docker compose up`
or 
`$ docker compose up -d # run in detached mode`

Go to `http://localhost:8080`

Default username and password are both `airflow`.

## Stop
`$ docker compose down`

## Stop and delete data
`$ docker compose down -v # removes volumes`

## Add a dag
Create files with DAGs in the `./dags` folder. These are attached as a volume in `/opt/airflow/dags`.

When running manually, make sure to flip switch on left side of UI to unpause the DAG.

## Python environment
Not necessary to create virtual environment and install from `requirements.txt`. This is helpful for code completion though when developing locally using VS Code.
