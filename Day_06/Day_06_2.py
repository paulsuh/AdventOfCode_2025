from math import prod
from pprint import pprint

from AdventOfCode_2025_inputs.day_06_input import input_data

# input_data="""123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +
# """


# append a space to each line to remove special case
problem_lines = [
    one_line + " "
    for one_line in input_data.splitlines()
]

# spaces are now significant in that they can affect the int values
# iterate each line, consuming one char at a time

# could also iterate in reverse and trigger on finding the operator
current_problem_values = []
result = 0
for one_col in zip(*problem_lines):
    col_str = "".join(one_col)
    match one_col[-1]:
        case "+":
            func = sum
        case "*":
            func = prod

    try:
        current_problem_values.append(int(col_str[:-1]))
    except ValueError:
        # hit a column of spaces so solve the problem
        temp = func(current_problem_values)
        result += temp
        current_problem_values = []

print(result)
