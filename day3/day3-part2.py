import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
control_pattern = r"(do\(\)|don't\(\))"
full_pattern = rf"{mul_pattern}|{control_pattern}"

enabled = True
total_sum = 0

matches = re.findall(full_pattern, open("day3/input.txt").read())

for item in matches:
    print(item)

for mul_a, mul_b, control in matches:
    if control == "do()":
        enabled = True
    elif control == "don't()":
        enabled = False
    elif mul_a and mul_b and enabled:
        total_sum += int(mul_a) * int(mul_b)
        
print(total_sum)
