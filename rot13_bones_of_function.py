def rot13(message):
    possible = "abcdefghijklmnopqrstuvwxyz"
    changedvalue = ''
    for char in message:
        if char == ' ':
            changedvalue = ' '
        else:
            pos = (possible.index(char)%26) +13
            changedvalue = ord(char) + pos
        print (changedvalue)

print (rot13('abcdefg'))

