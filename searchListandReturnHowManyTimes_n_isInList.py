def contains_n(numbers, number):
    # Your code here, to replace this non-working version
    count = 0
    for i in numbers:
        if number == i:
            count = count + 1
    return count          

# Be sure to test your function with various inputs
print (contains_n([1,1,2,3,4,4,4],1))