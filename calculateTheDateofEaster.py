user_Year = int(input("Please enter a year between 1900 and 2099"))

if user_Year > 2099:
    print("You have entered a date that is out of range")
elif user_Year < 1900:
    print("You have entered a date that is out of range")

if (user_Year == 1954 or user_Year == 1981 or user_Year == 2049 or user_Year == 2049 or user_Year == 2076):
    user_Year = user_Year - 7

a = user_Year % 19
b = user_Year % 4
c = user_Year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e
if dateofeaster > 31:
    dateofeaster = dateofeaster - 31
    print ("Easter Sunday is April " + str(dateofeaster) + " this year!")
else:
    print ("Easter Sunday is March " + str(dateofeaster) + " this year!")


           

