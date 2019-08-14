# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Example HTTP operator and sensor"""

import json
from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.sensors.http_sensor import HttpSensor

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '53 7 * *  1-5',
}

dag = DAG('email_report_a1', default_args=default_args)

dag.doc_md = __doc__

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = SimpleHttpOperator(
    task_id='daily_report_ws',
    http_conn_id='http_kubernetes_report_api',
    endpoint='/report-a1',
    data=json.dumps({"seller_name":"Toko Flamboyan", "entity_id":"E10AYAFLM", "receipt":"mragungsetiaji@gmail.com", "bcc":["agung.setiaji@larisin.id"], "filter_date":"today"}),
    headers={"Content-Type": "application/json"},
    #response_check=lambda response: len(response.json()) == 0,
    dag=dag,
)

t1
