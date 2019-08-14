# Daily WS Excel Report
# Note: for schedule_interval https://crontab.guru/

import json
import datetime
from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.sensors.http_sensor import HttpSensor

default_args = {
    'owner': 'agung.setiaji@larisin.id',
    'depends_on_past': False,
    'start_date':datetime.datetime(2019,8,14),
    'email': ['agung.setiaji@larisin.id'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '31 10 * * 1-6',
}

dag = DAG('http_email_report_a1', default_args=default_args)
dag.doc_md = __doc__

t1 = SimpleHttpOperator(
    task_id='task_indako',
    http_conn_id='http_kubernetes_report_api',
    endpoint='/report-a1',
    data=json.dumps({
        "seller_name":"Toko Indako", 
        "entity_id":"E10AYANDC", 
        "receipt":"bennywardana402@gmail.com", 
        "bcc":[
            "agung.setiaji@larisin.id", 
            "clarissa.tjoe@larisin.id",
            "hendry.lie@larisin.id", 
            "juanito.gunawan@larisin.id", 
            "adi.swandaru@larisin.id",
            "cahyo.listyanto@larisin.id"
        ],
        "filter_date":"today"
    }),
    headers={"Content-Type": "application/json"},
    dag=dag,
)

t2 = SimpleHttpOperator(
    task_id='task_flamboyan',
    http_conn_id='http_kubernetes_report_api',
    endpoint='/report-a1',
    data=json.dumps({
        "seller_name":"Toko Flamboyan", 
        "entity_id":"E10AYAFLM", 
        "receipt":"wi_vie@yahoo.co.id", 
        "bcc":[
            "agung.setiaji@larisin.id", 
            "clarissa.tjoe@larisin.id",
            "hendry.lie@larisin.id", 
            "juanito.gunawan@larisin.id", 
            "adi.swandaru@larisin.id",
            "cahyo.listyanto@larisin.id"
        ],
        "filter_date":"today"
    }),
    headers={"Content-Type": "application/json"},
    dag=dag,
)

t1 >> t2
