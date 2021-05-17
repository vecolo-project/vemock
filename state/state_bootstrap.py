from time import sleep

from state.state_file import save_state, print_state, append_state
from state.api_request import submit_state


def loop_state(frequency_wait, history_path, state, jwt_token, api_endpoint):
    while 1:
        state.next_state()
        # print_state(state)
        # append_state(state)
        submit_state(api_endpoint, state, jwt_token)
        save_state(history_path, state)
        sleep(frequency_wait)
