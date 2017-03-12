from test import testEqual
import math

def findHypot(a,b):
    #math.hypot(x,Y)
    length = math.hypot(a,b)
    return length

#print  (findHypot (3,4)) 
testEqual(findHypot(12.0, 5.0), 13.0)
testEqual(findHypot(14.0, 48.0), 50.0)
testEqual(findHypot(21.0, 72.0), 75.0)
testEqual(findHypot(1, 1.73205), 1.999999)
