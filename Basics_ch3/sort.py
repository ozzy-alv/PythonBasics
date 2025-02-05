#printing a list in order 

cars = ['hyundai', 'honda', 'bmw', 'mercedes']
print(cars)

#sorting in order

cars.sort() #sort orders the list by alphabetical order
print(cars) #print sorted list

#reversing a list

cars.reverse()#reverses the list, in reverse alphabetical order
print(cars) 

#finding the length of a list

print(len(cars)) #prints the length of the list, len() returns an integer

#sorting a list temporarily

cars = ['hyundai', 'honda', 'bmw', 'mercedes']
print(cars) #print sorted list

print(sorted(cars)) #temporarily sorted list

print(cars) # prints original list again
