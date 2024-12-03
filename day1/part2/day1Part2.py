tot = 0
list1 = []
list2 = []
occurrences = 0
multipler = 0

with open("input.txt") as file:
    for row in file:
        num1, num2 = map(int, row.split())
        list1.append(num1)
        list2.append(num2)

for num1 in list1:
    print("num1: " + str(num1))
    occurrences = list2.count(num1)
    print("occurences: " + str(occurrences))

    multipler = num1 * occurrences

    print("multipler: " + str(multipler))

    tot += multipler

print(tot)
