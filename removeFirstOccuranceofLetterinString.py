from test import testEqual

def remove(substr,theStr):
    # your code here
    theStr = theStr.replace(substr,'', 1)  
    return (theStr)
testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
