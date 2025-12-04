from pprint import pprint

from AdventOfCode_2025_inputs.day_04_input import input_data

# input_data="""..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

# pro tip - extend the map area so that you don't need to
# special case the edges

floor_array = [
    "." + one_line + "."
    for one_line in input_data.splitlines()
]
width = len(floor_array[0])
floor_array.insert(0, "."*width)
floor_array.append("."*width)


def remove_paper_rolls(floor_state: list[str]) -> int:

    num_accessible_rolls = 0
    accessible_rolls = []

    for y_coord in range(1,len(floor_state)-1):
        for x_coord in range(1, width-1):
            if floor_state[y_coord][x_coord] == "@":
                adjacent_count = -1     # start at -1 to account for the roll itself
                for y_delta in range(-1, 2):
                    for x_delta in range(-1, 2):
                        if floor_state[y_coord+y_delta][x_coord+x_delta] == "@":
                            adjacent_count += 1
                if adjacent_count < 4:
                    # print(y_coord, x_coord)
                    accessible_rolls.append((y_coord, x_coord))

    for one_roll in accessible_rolls:
        working_row = floor_state[one_roll[0]]
        new_row = working_row[0:one_roll[1]] + "." + working_row[one_roll[1]+1:]
        floor_state[one_roll[0]] = new_row

    return len(accessible_rolls)


total_rolls_removed = 0
for i in range(100):
    rolls_removed = remove_paper_rolls(floor_array)
    if rolls_removed == 0:
        break
    print(rolls_removed)
    total_rolls_removed += rolls_removed

print(f"i = {i}")
print(total_rolls_removed)
pprint(floor_array)
