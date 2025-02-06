#to square you can use the ** value you can also use loops to return a list of operands results

#establish an empty array

squares = []
for n in range(1, 11): #for loop to establish a list
    squared = n**2 #taking each iteration and squaring it then storing the value within a variable
    squares.append(squared) #adding the value to the list

#printing the array
print(squares)    

#lets make it more concise

#restart
squares = []

for n in range(1, 11):
    squares.append(n**2) #directly adding the squared numbers to the list

#printing the list    
print(squares)    