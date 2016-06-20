#!/user/bin/python

__author__ = 'hsenid'

from random import randint

#get number or rows
rows = int(input('Enter number of rows: '))

#get number of columns
columns = int(input('Enter number of columns: '))

output = open("output.csv", "w+")

for rw in range(0,rows):
    yy=""
    for cl in range(0,columns):
        x = randint(0, 99)
        if(cl == columns-1):
            yy += str(x) + "\n"
        else:
            yy += str(x) + ","
    output.write(yy)


