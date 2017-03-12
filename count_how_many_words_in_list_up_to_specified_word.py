def total_word_sam(wordlist):
    total = 0 
    for i in wordlist:
        if i == 'sam':
            total = total + 1
            return (total)
    

print (total_word_sam(['rick','bob', 'sam','dale','sam']))

