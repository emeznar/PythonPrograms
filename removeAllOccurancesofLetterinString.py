from test import testEqual

def remove_letter(theLetter, theString):
    # your code here
    theString = theString.replace(theLetter,'')  
    return (theString)
    
testEqual(remove_letter('a', 'apple'), 'pple')
testEqual(remove_letter('a', 'banana'), 'bnn')
testEqual(remove_letter('z', 'banana'), 'banana')
