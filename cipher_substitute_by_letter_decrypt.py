def implement_cipher(message, key):
    possible = "abcdefghijklmnopqrstuvwxyz"
    changedvalue = ''
    for char in message:
        if char == ' ':
            changedvalue = changedvalue + ' '
        else:
            x = possible.index(char)
            changedvalue = changedvalue + key[x]
    return (changedvalue)
    
answer_encrypted = (implement_cipher('hello world', 'badcfehgjilknmporqtsvuxwzy'))
print (answer_encrypted)

def decrypt_cipher(changedvalue,key):
    possible = "abcdefghijklmnopqrstuvwxyz"
    originalString = ''
    for char in changedvalue:
        if char == ' ':
            originalString = originalString + ' '
        else:
            x = key.index(char)
            originalString = originalString + possible[x]
    return (originalString)

originalString = decrypt_cipher(answer_encrypted, 'badcfehgjilknmporqtsvuxwzy')
print(originalString)

