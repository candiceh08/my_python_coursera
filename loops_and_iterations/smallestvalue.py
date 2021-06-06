# program that finds the smallest value in a list of numbers
# introduction to a new variable called None

smallest = None
for value in [4,45,35,83,2]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest,value)
print("The smallest value is: ", smallest)
