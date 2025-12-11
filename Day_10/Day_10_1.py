from functools import reduce
from itertools import combinations
from pprint import pprint

from AdventOfCode_2025_inputs.day_10_input import input_data

# input_data="""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """


def parse_target_state(state_str: str) -> int:
    # returns a bit pattern 0 = off 1 = on
    # input will be [.#.#.#]
    result = 0
    for one_char in state_str[1:-1]:
        result = (result << 1) + (1 if one_char == "#" else 0)
    return result


def parse_button_bits(button_str: str, state_len: int) -> int:
    # returns a bit pattern
    # input will be (1,2,3) and 4
    result = 0
    for one_char in button_str[1:-1].split(","):
        result += 1 << (state_len - int(one_char))
    return result


def figure_out_presses(target_state: int, buttons: list[int]) -> list[int]:
    # start by assuming no more than one press is necessary. this may be wrong.
    for one_len in range(1, len(buttons)):
        result_state = 0
        for one_series in combinations(buttons, one_len):
            # print(one_series)
            result_state = reduce(lambda r, b: r ^ b, one_series)
            if result_state == target_state:
                return list(one_series)
    print( f"not found {target_state} {buttons}")
    return []


machines_list = []

all_buttons = 0
for one_machine_line in input_data.splitlines():
    elements_list = one_machine_line.split()
    target_state = parse_target_state(elements_list[0])
    # print(f"{target_state:b}")
    button_actions_list = [
        parse_button_bits(button_str, len(elements_list[0])-3)
        for button_str in elements_list[1:-1]
    ]
    # print(f"{button_actions_list}")
    one_buttons = figure_out_presses(target_state, button_actions_list)
    print(one_buttons)
    all_buttons += len(one_buttons)
    print("----------------")

print(all_buttons)
