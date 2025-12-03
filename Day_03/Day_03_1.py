from AdventOfCode_2025_inputs.day_03_input import input_data

# input_data="""987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """


def max_joltage(battery_bank: str) -> str:
    # find max digit d1 and position(s)
    # Note: can't be in last position, as it won't have any digits to the right
    # choose leftmost position of d1
    # find max digit d2 to right of d1
    # return 10*d1+d2
    d1_value = max(battery_bank[:-1])
    d1_value_location = battery_bank.find(d1_value)
    d2_value = max(battery_bank[d1_value_location+1:])
    return d1_value+d2_value


print(sum(
    int(max_joltage(one_bb))
    for one_bb in input_data.splitlines()
))
