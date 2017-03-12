def is_prime(n):
    x = 2
    for i in range (1,n):
        if n != x and n % 2 == 0:
            return False
        while x <= (n+1):
            if n>3 and n != x and n % (x) == 0:
                return False
            else:
                x = x + 1
        else:
            return True
        
        
print (is_prime(3))
            

