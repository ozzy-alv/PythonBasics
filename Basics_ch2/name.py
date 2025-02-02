#Practicing string manipulation

#Changing the upper case of names
name = "Ozzy alvarado"
print(name.title())

#all upper case
print(name.upper())

#all lower case
print(name.lower())

#Combining or concatenating

first_name = "ozzy "
last_name = "alvarado"
full_name = first_name + last_name

print("Hello, " + full_name.title() + "!")

#Removing spaces left, right, both

#right
favorite_language = " python "

favorite_language = favorite_language.rstrip()
print(favorite_language)

#left
favorite_language = favorite_language.lstrip()
print(favorite_language)

#right and left
favorite_language = favorite_language.strip()
print(favorite_language)