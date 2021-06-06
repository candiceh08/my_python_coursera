zork = 0 #could also call is total but shows that it can be called anything
count = 0
for number in [34,54,2,14,78]:
    count += 1
    zork += number
    print(count,zork,number)
print("The sum of the values of the list is:",zork)
print("Number of times the loop was executed", count)
print ("The average of this list is:", zork/count)
