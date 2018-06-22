import datetime
import os

from airflow import models
from airflow.operators import python_operator
from pyweatherscraper.scraper import WeatherScraper

default_dag_args = {
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': models.Variable.get('gcp_project')
}

with models.DAG(
    'weatherRunner',
    schedule_interval=datetime.timedelta(minutes=15),
    default_args=default_dag_args as dag:
    run_weather_script = python_operator.PythonOperator(
        WeatherScraper().storeWeather()
    )
    run_weather_script
)