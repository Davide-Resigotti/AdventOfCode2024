import re

def multiply(row):

    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"(do\(\)|don't\(\))"
    full_pattern = rf"{mul_pattern}|{control_pattern}"

    enabled = True
    total_sum = 0

    matches = re.findall(full_pattern, row)

    for mul_a, mul_b, control in matches:
        if control == "do()":
            enabled = True
        elif control == "don't()":
            enabled = False
        elif mul_a and mul_b and enabled:
            total_sum += int(mul_a) * int(mul_b)

    return total_sum

with open("day3/test2.txt") as file:
    result = 0
    for row in file:
        result += multiply(row)
        print(f"Total sum: {result}")