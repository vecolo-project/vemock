import json
import os

from config.Config import Config


def read_conf(conf_str):
    return Config(**json.loads(conf_str))


def read_conf_from_env():
    return Config(os.getenv('auto_off'),
                  os.getenv('max_seats'),
                  os.getenv('station_id'),
                  os.getenv('frequency_wait'),
                  'history/' + os.getenv('history_path'),
                  os.getenv('jwt_token'),
                  os.getenv('api_endpoint'),
                  os.getenv('max_charge'),
                  os.getenv('debug'))
