from itertools import combinations
from pprint import pprint
from typing import NamedTuple

from AdventOfCode_2025_inputs.day_09_input import input_data

input_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


class Tile(NamedTuple):
    y: int
    x: int


def area_of_rectangle(point_a: Tile, point_b: Tile) -> int:

    left = min(point_a.x, point_b.x)
    right = max(point_a.x, point_b.x)
    top = min(point_a.y, point_b.y)
    bottom = max(point_a.y, point_b.y)

    width = right - left + 1
    height = bottom - top + 1

    result = width * height

    return result


points = [
    Tile(*tuple(map(int, one_point_spec.split(","))))
    for one_point_spec in input_data.splitlines()
]

pprint( points )

max_area = 0
for point_a, point_b in combinations(points, 2):
    area = area_of_rectangle(point_a, point_b)
    if area > max_area:
        max_area = area

print(max_area)
