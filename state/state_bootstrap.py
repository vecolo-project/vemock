import datetime
import time

from state import state_file


def loop_state(frequency_wait, history_path, state):
    while 1:
        state.next_state()
        print(f'{datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} : {state.__dict__}')
        state_file.save_state(history_path, state)
        state_file.append_state(state)
        time.sleep(frequency_wait)
