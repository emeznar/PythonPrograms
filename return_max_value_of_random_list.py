import random
    
def find_highest(numberlist):
    #print(numberlist)
    return (numberlist[-1])
      
    
numberlist = []       
for i in range(100):
    numberlist.append(random.randrange(0,1001))
    numberlist.sort()
#print(numberlist)
        
    
print (find_highest(numberlist))
    

