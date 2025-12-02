from AdventOfCode_2025_inputs.day_02_input import input_data

# input_data="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# """

ranges = input_data.split(',')
sum = 0
for one_range in ranges:
    range_start, range_end = one_range.split("-")
    for number in range(int(range_start), int(range_end)+1):
        num_string = str(number)
        if len(num_string) % 2 == 1:
            # if odd number of digits it can't be an invalid id
            continue
        if num_string[:len(num_string)//2] == num_string[len(num_string)//2:]:
            print(num_string)
            sum += number
print(sum)
