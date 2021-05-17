import os
import time

from dotenv import load_dotenv

from config import config_reader
from state import state_file, state_bootstrap
from state.State import State

os.environ['TZ'] = 'Europe/Paris'  # set new timezone
time.tzset()

load_dotenv()

print(f"Loading conf ...")
config = config_reader.read_conf_from_env()
print(f'Loaded : {config.__dict__}')

default_state = State(50, config.auto_off, config.max_seats // 2, config.max_seats)

state = state_file.get_state(config.history_path, default_state)

state_bootstrap.loop_state(config.frequency_wait, config.history_path, state, config.jwt_token, config.api_endpoint)
