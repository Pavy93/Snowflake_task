import json
import logging


class ConfigManager:
    __path_dag_conf = "configs/config.json"

    @staticmethod
    def get_config():
        logging.info("Trying to load config")
        with open(ConfigManager().__path_dag_conf, encoding='utf-8') as data_file:
            data = json.load(data_file)
            return data
