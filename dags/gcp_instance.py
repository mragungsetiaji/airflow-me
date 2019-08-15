import os

import airflow
from airflow import models
from airflow.contrib.operators.gcp_compute_operator import GceInstanceStartOperator, \
    GceInstanceStopOperator, GceSetMachineTypeOperator

# [START howto_operator_gce_args_common]
GCP_PROJECT_ID = os.environ.get('GCP_PROJECT_ID', 'example-project')
GCE_ZONE = os.environ.get('GCE_ZONE', 'europe-west1-b')
GCE_INSTANCE = os.environ.get('GCE_INSTANCE', 'testinstance')
# [END howto_operator_gce_args_common]

default_args = {
    'start_date': airflow.utils.dates.days_ago(1),
}


with models.DAG(
    'example_gcp_compute',
    default_args=default_args,
    schedule_interval=None  # Override to match your needs
) as dag:
    # [START howto_operator_gce_start]
    gce_instance_start = GceInstanceStartOperator(
        project_id=GCP_PROJECT_ID,
        zone=GCE_ZONE,
        resource_id=GCE_INSTANCE,
        task_id='gcp_compute_start_task'
    )
    # [END howto_operator_gce_start]
    

    gce_instance_start 
