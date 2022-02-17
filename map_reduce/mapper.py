#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    #strip white spaces at begining and end of line
    line = line.strip()
    #split each line up
    words = line.split()

    for word in words:
        word = re.findall(r"[A-Za-z]+|[^0-9]", word)
           
    for word in word:
        if word == '':
            pass
        else:
            print(word.lower() + "\t" + '1')



        


#mapper - breaking up words into units

#echo 'a quick brown fox jumps over a lazy dog'|./mapper.py