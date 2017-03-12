def mirror(text):
    return reverse(text)

def reverse(text):
    x = ''
    for item in text:
        x = item + x
    return (x)

print(mirror('good'))
print(mirror('Python'))
print(mirror(''))
print(mirror('a'))

