from pprint import pprint
from functools import cache

from AdventOfCode_2025_inputs.day_11_input import input_data


# input_data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# """

cables={
    one_line.split(": ")[0]: one_line.split(": ")[1].split()
    for one_line in input_data.splitlines()
}

pprint(cables)


# depth-first search
@cache
def check_path(current_node: str) -> list[list[str]]:
    if current_node == "out":
        return [["out"]]
    else:
        downstream_paths = []
        for next_node in cables[current_node]:
            downstream_paths += check_path(next_node)
        result = [
            [current_node] + one_path
            for one_path in downstream_paths
        ]
        return result


paths = check_path("you")

pprint(paths)
print(len(paths))
