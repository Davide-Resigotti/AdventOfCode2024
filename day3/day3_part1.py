import re


def multiply(row):

    # find all mul
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    all_mul = re.findall(pattern, row)

    return sum(int(x) * int(y) for x, y in all_mul)


with open("day3/input.txt") as file:
    tot = 0
    for row in file:
        tot += multiply(row)

    print(tot)
