from pprint import pprint
from typing import NamedTuple

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

# this is just to make it easier to think about the problem
class FreshRange(NamedTuple):
    min: int
    max: int

ranges = [
    FreshRange(int(one_range_line.split("-")[0]), int(one_range_line.split("-")[1]))
    for one_range_line in input_data.splitlines()
]
ranges.sort(reverse=True)

result = []
current_range = ranges.pop()

while len(ranges)>0:
    next_range = ranges.pop()
    if current_range.max <next_range.min:
        # no overlap, time to move on
        result.append(current_range)
        current_range = next_range
    else:
        # there is an overlap, coalesce
        current_range = FreshRange(current_range.min, max(current_range.max, next_range.max))

# add the final current_range
result.append(current_range)

print(sum([
    one_range.max - one_range.min + 1
    for one_range in result
]))
