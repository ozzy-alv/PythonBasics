#counting to twenty, create a loop that counts up to twenty

for n in range(1, 21):
    print(n)
    
#make a list for numbers one to one million

million = [n for n in range(1, 1000001)]
#print(million)    

#now see how quickly python can add a million numbers
total_of_mil = sum(million)
print(total_of_mil)

#taking the twenty program change it so it returns a list of odd number up to 20
odd_numbers = [n for n in range(1, 21, 2)]
print(odd_numbers)    

#make a list of multiples of 3 from 3 to 30

threes = [n*3 for n in range(1, 11)]
print(threes)

#make a list of the cubes from the numbers 1-10

cubes = [n**3 for n in range(1, 11)]
print(cubes)