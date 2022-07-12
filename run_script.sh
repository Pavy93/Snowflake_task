export AIRFLOW_HOME=/home/pavel/PycharmProjects/Snowflake_task
export PYTHONPATH=/home/pavel/PycharmProjects/Snowflake_task/configs
export PYTHONPATH=/home/pavel/PycharmProjects/Snowflake_task/data
export PYTHONPATH=/home/pavel/PycharmProjects/Snowflake_task/sql_queries
export PYTHONPATH=/home/pavel/PycharmProjects/Snowflake_task/utils
export PYTHONPATH=$AIRFLOW_HOME
export AIRFLOW__CORE__LOAD_EXAMPLES=False

airflow standalone
