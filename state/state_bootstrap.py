from time import sleep

from state.state_file import save_state, print_state, append_state
from state.api_request import submit_state


def loop_state(frequency_wait, history_path, state, jwt_token, api_endpoint, debug=True):
    while True:
        state.next_state()
        submit_state(api_endpoint, state, jwt_token, debug)
        save_state(history_path, state)
        if debug:
            print_state(state)
            append_state(state)
        sleep(frequency_wait)
