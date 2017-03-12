def sum_of_squares(xs):
    newlist = [item **2 for item in xs]
    #print (newlist)
    total = 0
    for i in range (len(newlist)):
        total = total + newlist[i]
    return (total)
    
    
print(sum_of_squares([1,2,2]))



