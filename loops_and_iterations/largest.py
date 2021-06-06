# Print the largest number of a list

largest_so_far = -1
for num in [3, 41, 12, 30, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print("The largest number of the list is:", largest_so_far)
