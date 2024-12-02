tot = 0
list1 = []
list2 = []

with open('input.txt') as file:
    for row in file:
        num1, num2 = map(int, row.split())
        list1.append(num1)
        list2.append(num2)
        
    list1.sort()    
    list2.sort()    
    
    for i in range(len(list1)):
        
        num1 = list1[i]
        num2 = list2[i]
            
        print("num1 " + str(num1) + " " +"num2 " + str(num2))
        
        # use abs to not use two if
        if num1 >= num2:
            tot += num1 - num2
            print("distance: " + str(num1-num2))
        else:
            tot += num2 - num1    
            print("distance: " + str(num2-num1))
            
print()
print(tot)
    


