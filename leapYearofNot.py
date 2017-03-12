def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
# Below is a set of tests so you can check if your code is correct.
# Do not copy this part into Vocareum.
from test import testEqual

testEqual(isLeap(1944), True)
testEqual(isLeap(2011), False)
testEqual(isLeap(1986), False)
testEqual(isLeap(1956), True)
testEqual(isLeap(1957), False)
testEqual(isLeap(1800), False)
testEqual(isLeap(1900), False)
testEqual(isLeap(1600), True)
testEqual(isLeap(2056), True)
