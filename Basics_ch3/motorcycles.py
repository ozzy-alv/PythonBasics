#creating an array of motorcycles then printing motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#replacing a value within the array

motorcycles[0] = 'ducati' #target the place in the array by using the brackets
print(motorcycles)

#adding elements to a list

motorcycles.append('honda') #append() is use to add elements to the back of the list, added honda back to the end of the list
print(motorcycles) #print

#Start from scratch by creating an empty array

motorcycles = [] #empty list

#add items to the list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#you can also choose where you want to insert the element into the list

motorcycles.insert(0, 'ducati') #insert() is used to choose where to place an element, inserting the element 'ducati' into index 0
print(motorcycles)

#deleting elements from the list

del motorcycles[0] #del statement is used to delete an element or elements from the list, in this case we are deleting the element we've inserted
print(motorcycles)

#you can use the del statement to delete any element as long as you choose its index in the list

del motorcycles[1] #del is now deleting the second element in the list, when you call the del statement you cannot access the value that was removed.
print(motorcycles)

#if you want to use the value of an item after you remove it from a list, you can use the pop() method, pop() removes the value from the list and keeps it.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#using pop method to extract value and store it in a variable in this case it is popped_motorcycle

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#the pop method also allows you to choose the index in which you want to remove an element for later use

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

first_motorcycle = motorcycles.pop(0) #to remove the element you choose from the list you must specify the index within the pop() method, we remove index one and store it
print(motorcycles)
print(first_motorcycle)

#if you do not know the position of the value you want to remove then the remove() method is used, this method will remove a matched element from the list
#note remove will only remove one instance of the element, to remove all instances of the element then you must loop the function until all elements are removed

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati' #we are assigning the name of the motorcycle we know exists in the list to a variable
motorcycles.remove(too_expensive) #then declare the variable within the remove() method to remove 'ducati'
print(motorcycles)




