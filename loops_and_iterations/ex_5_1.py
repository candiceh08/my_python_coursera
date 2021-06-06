# Write a program which repeatedly reads numbers until the user enters "done". Once the user enters done, print out the total
# count and average of the numbers. if user enters anything else other than a number, detect their mistake using try and except,
# print an error message and skip to the next number.


# average is the total divided by the count.
# so there is only two values to initialize: count and total

count = 0
tot = 0
while True: # this is a way to define an infinite loop
    sval = input("Enter a number:")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Error. Please enter a valid number.")
        continue
    print(fval)
    count += 1
    tot += fval
    print(count,tot,fval)

print("All done!")
print("The loop ran", count, "times, the sum of all the values entered is", tot,", and the average is", tot/count)

# Python doesn't store the values entered in sval at each loop.
# For each iteration, Python gets rid of the last value of sval and replaces it with the new user input.
