from operator import itemgetter
from math import prod
from pprint import pprint
from typing import NamedTuple

from AdventOfCode_2025_inputs.day_08_input import input_data, number_of_circuits, number_of_connections

# input_data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689
# """
# number_of_connections = 10
# number_of_circuits = 3


class ThreeDPoint(NamedTuple):
    x: int
    y: int
    z: int


def distance(point_a: ThreeDPoint, point_b: ThreeDPoint) -> float:

    result = ((point_a.x - point_b.x) ** 2 +
              (point_a.y - point_b.y) ** 2 +
              (point_a.z - point_b.z) ** 2
              ) ** 0.5
    return result


all_points = [
    ThreeDPoint(
        *(
            int(n)
            for n in one_line.split(",")
        )
    )
    for one_line in input_data.splitlines()
]

distance_matrix = {
    (point_a, point_b): distance(point_a, point_b)
    for point_a in all_points
    for point_b in all_points
    if point_a != point_b
}

distance_list = [
    one_item
    for one_item in distance_matrix.items()
]

distance_list.sort(key=itemgetter(1))

shortest_distances = [
    distance_list[i]
    for i in range(0, number_of_connections * 2, 2)
]

# connectedness
connected_segments = [
    set(one_segment[0])
    for one_segment in shortest_distances
]
print(connected_segments)

# check each one and merge if intersection is not empty
merge_happened = True
while merge_happened:
    merge_happened = False
    next_connected_segments = []
    for one_segment in connected_segments:
        connection_found = False
        for target_segment in connected_segments:
            if one_segment.isdisjoint(target_segment):
                continue
            if len(one_segment.symmetric_difference(target_segment)) > 0:
                merged_points = one_segment | target_segment
                if merged_points not in next_connected_segments:
                    next_connected_segments.append(merged_points)
                connection_found = True
                merge_happened = True
        if not connection_found:
            next_connected_segments.append(one_segment)
    connected_segments = next_connected_segments

    # pprint(connected_segments, width=120)

pprint(connected_segments, width=120)

circuit_lengths = [
    len(circuit)
    for circuit in connected_segments
]
circuit_lengths.sort(reverse=True)
pprint(circuit_lengths[:number_of_circuits])

print(prod(circuit_lengths[:number_of_circuits]))
