from itertools import batched, pairwise
from typing import Generator

from AdventOfCode_2025_inputs.day_02_input import input_data

# input_data="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# """


def divisors_generator(x: int) -> Generator[int, None, None]:
    for n in range(1, int(x**0.5)+1):
        if x % n == 0:
            yield n
            if x // n != n:
                yield x // n


def check_one_string(s: str) -> bool:
    for one_divisor in divisors_generator(len(s)):
        if one_divisor == len(s):
            continue
        str_chunks = batched(s, one_divisor, strict=True)
        result = True
        for chunk1, chunk2 in pairwise(str_chunks):
            if chunk1 != chunk2:
                # found non-match mark as False and go on to the next divisor
                result = False
                break
        if result:
            # if we reach here, the chunks are all the same so this is a bad ID
            return True
    # None of the possible combos are matching so this is a good ID
    return False


ranges = input_data.split(',')
sum = 0
for one_range in ranges:
    range_start, range_end = one_range.split("-")
    for number in range(int(range_start), int(range_end)+1):
        num_string = str(number)
        if check_one_string(num_string):
            sum += number
            # print(number)

print(sum)
