import numpy as np

with open('day4/input.txt', 'r') as f:
    lines = f.read().split('\n')

rows = len(lines)
cols = len(lines[0])
word = 'XMAS'
word_len = len(word)
count = 0

# directions are: up, down, left, righ, down-right, down-left, up-right, up-left
# represented by (<row-direction>,<column-direction>)
directions = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]

def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            match = True
            for i in range(word_len):
                nr, nc = r + dr * i, c + dc * i # position of the i letter
                if not is_valid(nr, nc) or lines[nr][nc] != word[i]:
                    match = False
                    break
            if match:
                count += 1          
                
print(count)

    

