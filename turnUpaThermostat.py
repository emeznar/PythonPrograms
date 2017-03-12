clicks = int(input("By how many clicks has the dial been turned?"+"\n"))

# TODO calculate the temperature, and report it back to the user
total = (((clicks) % 50) + 40)
print ("The temperature is " + str(total))

