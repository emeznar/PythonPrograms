import math

# TODO: use def to define a function called areaOfCircle which takes an argument called r
def areaOfCircle(r):
    a = r**2 * math.pi 
    return a
#print (areaOfCircle (5))
    # TODO implment your function to return the area of a circle whose radius is r


# below are some tests so you can see if your code is correct. You should not include this part in Vocareum.
from test import testEqual

t = areaOfCircle(0)
testEqual(t, 0)
t = areaOfCircle(1)
testEqual(t,math.pi)
t = areaOfCircle(100)
testEqual(t, 31415.926535897932)
t = areaOfCircle(-1)
testEqual(t, math.pi)
t = areaOfCircle(-5)
testEqual(t, 25 * math.pi)
t = areaOfCircle(2.3)
testEqual(t, 16.61902513749)
