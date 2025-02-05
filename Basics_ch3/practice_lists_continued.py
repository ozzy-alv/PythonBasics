#Guest list write a list of three people you would invite for dinner

guests = ['kobe', 'buffet', 'jayz']

print("Salutations, I personally want to invite you, " + guests[0].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[1].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[2].title() +  " for dinner tonight, join us for a wonderful meal!")

#something came up for one of my guest so I need to send a new set of invitations...

print("Quick update, it looks like " + guests[0].title() + " cannot make it, I've decided to extend an invitation to another guest, new set of invitations will be sent.")

#inviting a new guest
new_guest = 'kanye'

#removing the guest who cannot make it

del guests[0] #deleting guest index 0
guests.insert(0, new_guest) #inserting new guest

#sending new set of invitations

print("Salutations, I personally want to invite you, " + guests[0].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[1].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[2].title() +  " for dinner tonight, join us for a wonderful meal!")

#inviting more guests
print("I've just found a dinner table for three more guests, and I've reserved the restaurant for our privacy. I will be extending my invitations, new set of invitations will arrive my lovely guests.")

#insert your guest in different places in the list insert in beginning, middle, and end of the current guest list

#creating an array of guests to be inserted into the list of current guests
more_guests = ['Michael Jackson', 'Prince', 'Michael Jordan']

#inserting Michael Jackson in the beginning of the guest list

guests.insert(0, more_guests[0])

#inserting Prince in the middle of the guest list

guests.insert(len(guests) // 2, more_guests[1]) #to find the middle of the guest list, divide the length of the guest list by 2 then for the second arg specify guest

#inserting Michael Jordan in the end of the guest list

guests.append(more_guests[2])

#inviting the guests again, hopefully the last one

print("Salutations, I personally want to invite you, " + guests[0].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[1].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[2].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[3].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[4].title() +  " for dinner tonight, join us for a wonderful meal!")
print("Salutations, I personally want to invite you, " + guests[5].title() +  " for dinner tonight, join us for a wonderful meal!")

#oh no the table that I ordered for the restaurant wont get here in time, I have to extend my invitations to only two people now...

#I have to choose two people from the list to join us and let everyone know that something came up

print("My lovely guests, the table I ordered for the restaurant has been smashed to pieces by angry employees, I now only have a slot for two people.")

#use pop to remove the guest and let them know they cannot invite them to dinner

removed_guests = [guests.pop(0), guests.pop(1), guests.pop(2).title(), guests.pop(2)] #rm 1st idx M Jackson, rm 2nd idx Prince, rm 3rd idx Jayz, rm 3rd idx M Jordan

print("Sorry " + removed_guests[0] + ", I cannot invite you to our dinner tonight due to unfortunate circumstances.")
print("Sorry " + removed_guests[1] + ", I cannot invite you to our dinner tonight due to unfortunate circumstances.")
print("Sorry " + removed_guests[2] + ", I cannot invite you to our dinner tonight due to unfortunate circumstances.")
print("Sorry " + removed_guests[3] + ", I cannot invite you to our dinner tonight due to unfortunate circumstances.")

#print a message to the people still there
print("Hello " + guests[0].title() + " you are still invited to our dinner, see you tonight!")
print("Hello " + guests[1].title() + " you are still invited to our dinner, see you tonight!")

#delete the last two names to get an empty list

del guests[1]
del guests[0]

print(guests) #the list should be empty now
