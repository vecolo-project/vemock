import os
import time

from dotenv import load_dotenv

from config import config_reader
from state import State, state_file, state_bootstrap

os.environ['TZ'] = 'Europe/Paris'  # set new timezone
time.tzset()

load_dotenv()

config_path = os.getenv('config_path')
history_path = 'history/' + os.getenv('history_path')
frequency_wait = float(os.getenv('frequency_wait'))

print(f"Loading conf ...")
config = config_reader.read_conf_from_env()
print(f'Loaded : {config.__dict__}')

state = state_file.get_state(history_path, State.State(50, config.auto_off, config.max_seats // 2, config.max_seats))

state_bootstrap.loop_state(frequency_wait, history_path, state)
