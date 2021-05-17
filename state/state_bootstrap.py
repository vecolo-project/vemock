import datetime
import time

from state import state_file


def loop_state(frequency_wait, history_path, state):
    while 1:
        state.next_state()
        state_file.print_state(state)
        state_file.append_state(state)
        state_file.save_state(history_path, state)
        time.sleep(frequency_wait)
