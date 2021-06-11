file = open('hello.txt')
for sandwich in file: # the iterative value (sandwhich here) represents each line. the for loop automatically switch from one line to the next and executes the content of the loop
    print(sandwich[:5])

# each line is a string in the sequence

inp = file.read()
print(len(inp))
