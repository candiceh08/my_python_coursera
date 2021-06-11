friends = ['Emily','Gina','Lauren']

#for x in friends:
#    print('Hello',x)

for i in range(len(friends)):
    friend = friends[i]
    if 'Em' in friend:
        print('The target was found at index:',i)
    #print('Hello',friend,i)