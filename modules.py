#a module is a file containing python file

#inbuilt module maths

import math
import datetime
import random
import os

print(math.pi)

print(math.sqrt(64))

print(os.getcwd())

#os.mkdir("Using OS module")

#help(os)

print(random.randint(0,12))

print(datetime.datetime.now())

print(datetime.date.today())

if os.path.exists("demo.txt"):
    print("file  found")
    
else:
    print("file does not exist")