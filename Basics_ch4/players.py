#slicing a list

#to slice a list you declare the idx you want to start at and then choose the index you want to end plus another index.

players = ['Charlie', 'Mindy', 'Cindy', 'Leo', 'Tom']

#to slice you declare the array and insert values brackets separated by a colon
print(players[0:3])

#you can also generate any subset in anyplace within the array
print(players[1:3])

#if you omit the first value of slice you automatically start from the beginning
print(players[:4])

#if you omit the second value then you start from the value and onward
print(players[3:])

#negative values print starting from the end of the list
print(players[-3:])

