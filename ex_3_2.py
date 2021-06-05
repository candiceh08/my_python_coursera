#3.2 Use the try and except method to determine whether the user input can be turned into a float, and if not, 
#print an error message and quit the program.

hours = input("Hours:")
rate = input("Rate per hour:")
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

additionalhours = fhours - 40.0
if additionalhours > 0 :
    grosspay = 40 * frate + additionalhours*(frate*1.5)
else :
    grosspay = fhours * frate
print(grosspay)