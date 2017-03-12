p = 10000
n = 12
r = .08

t = int(input("How many years are you planning to borrow?"))

answer = p * ( ((1 + (r/n)) ** (n*t)) )
print ("The final amount after", t, "years is", answer,"!")

