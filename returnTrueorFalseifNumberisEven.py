from test import testEqual

def is_even(n):
    return n % 2 == 0
        
testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)
