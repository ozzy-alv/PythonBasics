#exercises to get comfortable with creating and implementing basic lists

#exercise, create a list of your friends names

friends = ['Bryam', 'Bella', 'Coco', 'Kiki']

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#now with the list of friends print a message to them, each message should be the same

#creating a unique variable for each friend
message_one = "Welcome, " + friends[0] + " everyone has been dying to meet you. Please make yourself at home."
message_two = "Welcome, " + friends[1] + " everyone has been dying to meet you. Please make yourself at home."
message_three = "Welcome, " + friends[2] + " everyone has been dying to meet you. Please make yourself at home."
message_four = "Welcome, " + friends[3] + " everyone has been dying to meet you. Please make yourself at home."

#printing the messages
print(message_one)
print(message_two)
print(message_three)
print(message_four)

#now think of your favorite mode of transportation and make a list that stores several examples then print a series of statements for each

#car lists
cars = ['tesla', 'mercedes', 'bmw', 'hyundai']

#car statements
car_one = cars[0].title() + "'s" + " are cool but the cybertruck looks like a roblox vehicle."
car_two = "I think in terms of class driving a " + cars[1].title() + " gives you a luxurious experience."
car_three = "My parents bought a brand new " + cars[2].title()
car_four = "I am emotionally attached to my " + cars[3].title() + " I don't think I'll ever let her go..."

#printing the car statements 
print(car_one)
print(car_two)
print(car_three)
print(car_four)
