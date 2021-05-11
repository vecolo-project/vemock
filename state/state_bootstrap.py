import time

from state import state_file


def loop_state(frequency_wait, history_path, state):
    while 1:
        state.next_state()
        print(f'State : {state.__dict__}')
        state_file.save_state(history_path, state)
        time.sleep(frequency_wait)
