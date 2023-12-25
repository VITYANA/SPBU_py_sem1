from dataclasses import dataclass


@dataclass
class FSMachine:
    states: list[dict[str, int]]
    start_state: int
    accepted_states: list[int]


def create_fs_machine(
    given_states: list[dict[str, int]], start_state: int, accepted_states: list[int]
):
    return FSMachine(given_states, start_state, accepted_states)


def move_state(symbol, state, fsm):
    for key, value in fsm.states[state].items():
        if symbol in key:
            return value


def validate_string(fsm: FSMachine, string: str):
    current_state = fsm.start_state
    for symbol in string:
        current_state = move_state(symbol, current_state, fsm)
        if current_state is None:
            return False
    return current_state in fsm.accepted_states
