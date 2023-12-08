from dataclasses import dataclass


@dataclass
class FSMachine:
    states: list[dict[str:int]]
    start_state: int
    accepted_states: list[int]


def create_fs_machine(
    given_states: list[dict[str:int]], start_state: int, accepted_states: list[int]
):
    all_states = []
    for state in given_states:
        all_states.append(state)
    return FSMachine(all_states, start_state, accepted_states)


def validate_string(fsm: FSMachine, string: str):
    current_state = 0
    for symbol in string:
        current_state = fsm.states[current_state]
        transfer = list(
            map(
                lambda condition: current_state[condition]
                if symbol in condition
                else None,
                current_state,
            )
        )
        next_state = list(filter(lambda cond: cond is not None, transfer))
        if len(next_state) == 0:
            return False
        current_state = next_state[0]
    return current_state in fsm.accepted_states
