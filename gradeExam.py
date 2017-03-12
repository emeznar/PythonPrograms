def examMark(x):
    if x < 60:
        return ("F")
    elif (x >=60 and x <70):
        return ("D")
    elif (x >=70 and x <80):
        return ("C")
    elif (x >=80 and x <90):
        return ("B")
    else:
        return ("A")

print (examMark(-100))

