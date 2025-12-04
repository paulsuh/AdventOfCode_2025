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

num_accessible_rolls = 0

for y_coord in range(1,len(floor_array)-1):
    for x_coord in range(1, width-1):
        if floor_array[y_coord][x_coord] == "@":
            adjacent_count = -1     # start at -1 to account for the roll itself
            for y_delta in range(-1, 2):
                for x_delta in range(-1, 2):
                    if floor_array[y_coord+y_delta][x_coord+x_delta] == "@":
                        adjacent_count += 1
            if adjacent_count < 4:
                print(y_coord, x_coord)
                num_accessible_rolls += 1

print(num_accessible_rolls)
