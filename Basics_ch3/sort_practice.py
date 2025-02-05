#do a series of sorting test from a list of five places in the world you'd like to visit

#create a list of places then print

places = ['Tokyo', 'Osaka', 'Beijing', 'Florence', 'Banff']
print(places)

#sort using sorted and print

print(sorted(places))

#view the list again to make sure it's back to the original

print(places)

#use sorted to print in reverse order

print(sorted(places, reverse = True))

#print again to make sure it's back to the original

print(places)

# now use reverse() to reverse the list  then print the list to show that the order has changed

places.reverse()
print(places)

#use reverse again to change the list back to its original order

places.reverse()
print(places)

#use sort to change the list to alphabetical order and print to confirm the order

places.sort()
print(places)

#use sort to change the list to reverse alphabetical order and print to confirm the order

places.sort(reverse = True)
print(places)

#now refer to the previous exercise involving dinner guests use len() to indicate the number of people invited to dinner

invited_guests = ['Bob', 'Bill', 'Bernice', 'Bernie', 'Baxter']
print(len(invited_guests))

#now think of something else you can store in a list. Create it and use all the previous functions introduced in this chapter

misc = ['tokyo', 'sushi', 'switzerland', 'hyundai', 'chess']

#sort in alphabetical order and print to confirm
misc.sort()
print(misc)

#reverse the list and print to show the order has changed
misc.sort(reverse = True)
print(misc)

#reverse method
misc.reverse()
print(misc)

#replace 3rd element in list
misc[2] = 'burger'
print(misc)

#insert an element in front
misc.insert(0, 'osaka')
print(misc)

#store an element removed from list and use it in another print function
car = misc.pop(2)
print("I really love my " + car.title())

#remove an element from list
games = 'chess'
misc.remove(games)
print(misc)

#delete and element
del misc[2]
print(misc)

#append another element to the back of the list
misc.append('PC games')
print(misc)

#temporarily sort the list
print(sorted(misc))

#print to confirm
print(misc)

#print the new length of the list
print(len(misc))



