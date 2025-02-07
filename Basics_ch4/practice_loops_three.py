#create a list to be sliced

video_games = ['csgo', 'eldin ring', 'fifa', 'valorant', 'skyrim', 'botw']

#print a message using the first three items in a created list using slice
for game in video_games[0:3]:
    print(f"I've spent hundreds of hours on {game.title()}")

#print a message using the three items from the middle of the list using slice
for game in video_games[2:5]:
    print(f"I used to grind the heck out of {game.title()}")

#print a message using the three items that are last on the list
for game in video_games[-3:]:
    print(f"I think {game.title()} might've been the game of the year at it's peak")
    
#now think back to pizzas program and make the list and the copy it

pizzas = ['margarita', 'four cheese', 'pepperoni']
friends_pizza = pizzas[:]

pizzas.append('supreme')
friends_pizza.append('anchovies')

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")
    
for pizza in friends_pizza:    
    print(f"My friends favorite pizzas are: {pizza}")


    