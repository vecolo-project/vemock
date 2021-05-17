import datetime
import json
import os
from time import strftime

from state import State


def save_state(filename, state_object):
    with open(filename, 'w') as fp:
        fp.write(json.dumps(state_object.__dict__, indent=2, sort_keys=True))


def append_state(state_object):
    with open("history/state.history", 'a') as fp:
        fp.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + " : ")
        json.dump(state_object.__dict__, fp)
        fp.write("\n")


def load_state(filename):
    try:
        if os.stat(filename).st_size > 0:
            print('Found history file, restoring previous state\n')
            with open(filename) as file:
                return State.State(**json.load(file))
        else:
            return
    except OSError:
        return


def print_state(state):
    print(f'{datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} : {state.__dict__}')


def get_state(history_filename,
              default_state=State.State(50, False, 6, 12)):
    state = load_state(history_filename)
    if not state:
        state = default_state
    else:
        state.max_seats = default_state.max_seats
        state.auto_off = default_state.auto_off
    return state
