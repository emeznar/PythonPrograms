
def is_palindrome(text):
    x = ''
    for item in text:
        x = item + x
    
    if text == x:
        return True
    else:
        return False
print(is_palindrome('abba'))
print(is_palindrome('abab'))
print(is_palindrome('straw warts'))
print(is_palindrome('a'))
print(is_palindrome(''))

