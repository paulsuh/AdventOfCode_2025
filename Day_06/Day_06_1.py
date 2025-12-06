from math import prod
from pprint import pprint

from AdventOfCode_2025_inputs.day_06_input import input_data

# input_data="""123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +
# """


problems = [
    one_line.split()
    for one_line in input_data.splitlines()
]

pprint(problems)

result = 0
for one_problem in zip(*problems):
    match one_problem[-1]:
        case "+":
            prob_answer = sum(map(int, one_problem[:-1]))
        case "*":
            prob_answer = prod(map(int, one_problem[:-1]))
        case _:
            raise RuntimeError(f"failed on {one_problem}")
    result += prob_answer

print(result)
