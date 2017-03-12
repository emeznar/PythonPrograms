from test import testEqual

def reverse(text):
    # your code here
    x = ''
    for item in text:
        x = item + x
    return (x)
        
testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")
