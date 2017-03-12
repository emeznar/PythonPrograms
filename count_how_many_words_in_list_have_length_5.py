def total_word5(wordlist):
    total = 0 
    for i in wordlist:
        if len(i) == 5:
            total = total + 1
    print (total)
    
total_word5(['brian','joe','steve','jack','craig'])


