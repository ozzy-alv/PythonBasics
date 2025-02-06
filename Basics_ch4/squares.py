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

#printing a total of numbers in list    
total = sum(squares)
print(total)

#introduction to list comprehension used to create lists in one line of code

squares = [n**2 for n in range(1, 11)] #another concise way of generating a list, in this case of squared numbers
print(squares)

#trying it again

numbers = [n for n in range(1, 11)]
print(numbers)

