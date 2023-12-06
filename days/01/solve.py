import re


def solve_file(file):
    sum = 0
    for line in file:
        digits = re.findall("\d", line)
        number_str = "".join([digits[0], digits[-1]])
        number = int(number_str)
        sum += number
    return sum
