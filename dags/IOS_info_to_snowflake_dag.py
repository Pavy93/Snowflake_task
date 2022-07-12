from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow import DAG
from utils.config_manager_util import ConfigManager
from datetime import datetime, timedelta
from sql_queries.push_csv_to_raw_table_query import query_1
from sql_queries.insert_and_process_data_in_stage_table_query import query_2
from sql_queries.insert_data_to_master_table_query import query_3

dag_config = ConfigManager().get_config()

with DAG(
    dag_config['dag_id'],

    default_args={
        'depends_on_past': False,
        'email': dag_config['email'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': dag_config['retries'],
        'retry_delay': timedelta(minutes=dag_config['retry_delay']),
    },

    description=dag_config['description'],
    schedule_interval=timedelta(days=dag_config['interval']),
    start_date=datetime(dag_config['start_year'], dag_config['start_month'], dag_config['start_day']),
    catchup=False,
    tags=dag_config['tags'],
        ) as dag:

    push_csv_to_raw_table = SnowflakeOperator(
        task_id="csv_to_RAW",
        sql=query_1,
        snowflake_conn_id="snowflake_conn"
    )

    insert_and_process_stage_table = SnowflakeOperator(
        task_id="STAGE_table_processing",
        sql=query_2,
        snowflake_conn_id="snowflake_conn"
    )

    insert_to_master_table = SnowflakeOperator(
        task_id="data_to_MASTER",
        sql=query_3,
        snowflake_conn_id="snowflake_conn"
    )

    push_csv_to_raw_table >> insert_and_process_stage_table >> insert_to_master_table
