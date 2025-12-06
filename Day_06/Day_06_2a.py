from math import prod
from pprint import pprint

from AdventOfCode_2025_inputs.day_06_input import input_data

# input_data="""123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +
# """


# iterate in reverse
problem_lines = [
    reversed(one_line)
    for one_line in input_data.splitlines()
]
col_of_spaces = " " * (len(problem_lines) - 1)

# spaces are now significant in that they can affect the int values
# iterate over lines simultaneously, consuming one char at a time
# from each one.

# iterate in reverse and trigger on finding the operator
current_problem_values = []
result = 0
for one_col in zip(*problem_lines):
    col_str = "".join(one_col[:-1])
    if col_str != col_of_spaces:
        current_problem_values.append(int("".join(col_str)))
        match one_col[-1]:
            case "+":
                problem_answer = sum(current_problem_values)
                result += problem_answer
                current_problem_values = []
            case "*":
                problem_answer = prod(current_problem_values)
                result += problem_answer
                current_problem_values = []

print(result)
