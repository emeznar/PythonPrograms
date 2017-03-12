def implement_cipher(message, key):
    possible = "abcdefghijklmnopqrstuvwxyz"
    changedvalue = ''
    for char in message:
        if char == ' ':
            changedvalue = changedvalue + ' '
        else:
            pos = possible.index(char)
            changedvalue = changedvalue + key[pos]
    print (changedvalue)


implement_cipher('hello world', 'badcfehgjilknmporqtsvuxwzy')


