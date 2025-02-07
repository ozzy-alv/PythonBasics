#make a buffet and store it in a tuple

buffet = ('sushi', 'pizza', 'fries', 'water', 'ice cream \n')

for food in buffet:
    print(food)

#buffet[1] = 'lasagna', failure cannot replace item in a tuple

buffet = ('sushi', 'lasagna', 'fries', 'chicken wings', 'ice cream')

for new_food in buffet:
    print(new_food)    