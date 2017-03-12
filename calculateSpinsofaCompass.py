spins = int(input("How many times did you spin? (Enter a negative number for couter-clockwise spins) "))

degrees = (spins) % 360

print("You are facing", degrees, "degrees relative to north")
