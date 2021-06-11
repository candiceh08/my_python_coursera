#file to play around with list functions

#len function
numbers = [1,3,4,5]
print(len(numbers))

#range function
friends = ['Emily','Gina','Lauren']
lenlist = len(friends)
print(range(lenlist))
print('Em' in friends) #returns False because doesn't exactly match any element of the list
print('Emily' in friends) #returns True

# prints out 'range(0,3)' instead of [0,1,2] like I was expecting -> means the same and works the same

#build a string from scratch
stuff = list()
stuff.append('Hello')
print(stuff)
