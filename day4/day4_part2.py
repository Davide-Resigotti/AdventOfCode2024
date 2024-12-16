import numpy as np


# i will move from A and check the corners
# corners can be only: MSS, SSM, SMM, MMS

#  M   S
#    A
#  M   S

with open('day4/myTest.txt', 'r') as f:
    file = f.read()



rows = len(file)
cols = len(file[0])
word = "MAS"
word_len = len(word)
count = 0

# only diagonal so: up-left, up-right, down-left, down-right
directions = [(-1,-1),(-1,1),(1,-1),(1,1)]

# A is in the middle so i'll start from position 1 right and down

print(rows)

for r in range (1, rows-1):
    # print(f"r {rows[r]}")
    for c in range(1, cols-1):
        print(file[r][c])
        if file[r][c] == "A": 
            print("yesss")
        else:
            print()
        


                

