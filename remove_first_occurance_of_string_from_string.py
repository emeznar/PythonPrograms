from test import testEqual

def remove_all(substr,theStr):
    # your code here
    theStr = theStr.replace(substr,'',len(theStr))  
    return (theStr)

testEqual(remove_all('an', 'banana'), 'ba')
testEqual(remove_all('cyc', 'bicycle'), 'bile')
testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
testEqual(remove_all('eggs', 'bicycle'), 'bicycle')

