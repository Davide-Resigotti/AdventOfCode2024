safe = 0
ascending = 0
descending = 0
distance = 0

with open("day2/input.txt") as file:
    for row in file:
        row = list(map(int, row.split()))
        print("element:" + str(row))
        for i in range(1,len(row)):
            if row[i-1] < row[i]:
                ascending += 1
            elif row[i-1] > row[i]:
                descending += 1
            # print("ascending "+ str(ascending))
            # print("descendoing " + str(descending))
        if ascending == len(row)-1 or descending == len(row)-1:
            for i in range(1,len(row)):
                if abs(row[i-1] - row[i]) > 0 and abs(row[i-1] - row[i]) < 4:
                    distance +=1
                    print(distance)
        if distance == len(row)-1:
            print("distance ok")
            safe += 1
        ascending = 0
        descending = 0
        distance = 0
                    
                    
print("safe: "+ str(safe))

                    
                
              
            
            
            
    