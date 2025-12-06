from pprint import pprint

from AdventOfCode_2025_inputs.day_05_input import input_data, input_data_2

# input_data="""3-5
# 10-14
# 16-20
# 12-18"""
#
# input_data_2 = """1
# 5
# 8
# 11
# 17
# 32
# """

ranges = [
    (int(one_range_line.split("-")[0]), int(one_range_line.split("-")[1]))
    for one_range_line in input_data.splitlines()
]

fresh_counter = 0
for one_ingredient in input_data_2.splitlines():
    for one_range in ranges:
        if one_range[0] <= int(one_ingredient) <= one_range[1]:
            fresh_counter += 1
            break

print(fresh_counter)
