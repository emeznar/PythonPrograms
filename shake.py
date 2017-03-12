Python 3.4.3 (default, Oct 14 2015, 20:33:09) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request


def get_text():
    """This retrieves text from Project Gutenburg
    """
    url = "http://www.gutenberg.org/cache/epub/1535/pg1535.txt"
    head = 103
    foot = 7
    body = ''
    with request.urlopen(url) as url_fh:
        body = url_fh.read().decode('UTF-8')
    body = body.split('\n', head)[-1]
    body = body.rsplit('\n', foot)[0]

    return body


def main():
    """This is what runs when you call `python word_count.py`.
    """
    text = get_text()
    # Your work goes here
    # To see the text, you can print it out like this:
    print(text)


# leave this code as it is
if __name__ == "__main__":
    main()
