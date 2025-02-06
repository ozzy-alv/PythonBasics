#working with numerical lists

#using range() function to generate a series of numbers

#use a for loop to create a list from 1 - 5

for num in range(1, 6): #we use the number 6 because count starts at zero so the return would be off by one
    print (num)

#to make a list of numbers you can wrap the function list() within range() to create an array

numbers = list(range(1, 6))
print(numbers)    