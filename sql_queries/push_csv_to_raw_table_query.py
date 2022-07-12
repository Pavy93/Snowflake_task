from utils.config_manager_util import ConfigManager


data = ConfigManager().get_config()['data']

query_1 = [
    f"""put file://{data} @task_6_stage;""",
    """copy into RAW_TABLE from @task_6_stage file_format = 
    (format_name = 'csv_format', error_on_column_count_mismatch=false) force=true;"""
]
