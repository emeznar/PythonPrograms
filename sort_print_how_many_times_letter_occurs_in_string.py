userstring = input('Please enter a string')

userstring = userstring.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

count = {}
for char in userstring:
    if char in alphabet:
        if char in count:
            count[char] = count[char] + 1
        else:
            count[char] = 1
            
keys = count.keys()
keys.sort()
for char in keys:
        print(char, count[char])



