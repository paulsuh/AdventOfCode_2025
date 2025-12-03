from AdventOfCode_2025_inputs.day_03_input import input_data

# input_data="""987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """


def max_joltage(battery_bank: str, depth: int = 12) -> str:
    # with max depth of 12 recursion is feasible
    # len(battery_bank) is guaranteed to be at least depth
    if depth == 1:
        test_battery_bank = battery_bank
    else:
        test_battery_bank = battery_bank[:-depth+1]
    max_value = max(test_battery_bank)
    max_value_location = test_battery_bank.find(max_value)
    if depth == 1:
        return max_value
    else:
        return max_value + max_joltage(battery_bank[max_value_location+1:], depth-1)



print(sum(
    int(max_joltage(one_bb))
    for one_bb in input_data.splitlines()
))
