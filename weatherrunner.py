import datetime
import os

from airflow import DAG
from airflow.operators import python_operator
from weatherrunner.pyweatherscraper.scraper import WeatherScraper

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())

default_dag_args = {
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5)
}


dag = DAG('weatherRunner',
schedule_interval=datetime.timedelta(minutes=15),
    default_args=default_dag_args,
    catchup=False
)

t1 = python_operator.PythonOperator(
    task_id='store_weather',
    python_callable=WeatherScraper().storeWeather,
    dag = dag
)
