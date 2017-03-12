def analyze_text(sentence):
    
    # your code here - count total characters
    total = 0
    for char in sentence:
        if char.isalpha() == True:
            total = total + 1
    #print (total)
    
    occurances = sentence.count('e') + sentence.count('E')
    #print(occurances)
    
    percent = int(occurances)/int(total)*100
    return "The text contains "+str(total)+" alphabetic characters, of which "+str(occurances)+" (" +str(percent)+"%) are 'e'."
    

# Don't copy these tests into Vocareum
from test import testEqual

sentence = "Eeeee"
expected = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(sentence), expected)

sentence = "Blueberries are tastee!"
expected = "The text contains 20 alphabetic characters, of which 6 (30.0%) are 'e'."
testEqual(analyze_text(sentence), expected)

sentence = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
expected = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(sentence), expected)

