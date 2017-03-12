def total_neg_numbers(numberlist):
    total = 0
    for i in numberlist:
        if i < 0:
            total = total + i
    return (total)
    
print (total_neg_numbers([-1,2,3,-4,5,-6,7,8]))


