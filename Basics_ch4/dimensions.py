#here we will be defining a tuple, which is an immutable list

#to define a tuple you must use parenthesis instead of brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250, remember that tuples cannot be mutated, meaning this creates an error
#print(dimensions[0]) 

#looping works similar to dimensions
for dimension in dimensions:
    print(dimension)

#parallel = dimension[:], you cannot subscript a dimension either, meaning this code creates an error
#print(parallel)

