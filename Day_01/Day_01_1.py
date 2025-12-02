from AdventOfCode_2025_inputs.day_01_input import input_data

# input_data = """
# L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""


counter = 0
current_dial_location = 50

for one_turn in input_data.splitlines():
    if one_turn.startswith('L'):
        current_dial_location = (current_dial_location - int(one_turn[1:])) % 100
    elif one_turn.startswith('R'):
        current_dial_location = (current_dial_location + int(one_turn[1:])) % 100

    if current_dial_location == 0:
        counter += 1

print(counter)
