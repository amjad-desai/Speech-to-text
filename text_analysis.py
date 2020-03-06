import io
import os
import textwrap

f= open("ge-xd-progressbar.txt", "r", encoding="utf-8")
str = f.read(450);
position = f.tell()
str=textwrap.fill(str)
print ("Current file position : ", position)
with open('test.txt', 'w') as file:
    file.write(str)
