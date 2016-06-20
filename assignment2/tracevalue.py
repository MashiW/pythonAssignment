#!/user/bin/python
from collections import Counter
import csv

input_file = 'OPTPF.csv'
output_file = 'traced_info.csv'
credit_file = 'creditfile.csv'

rfile = open(input_file, 'r')
reader = csv.reader(rfile, delimiter='|')

# open the file to write
writer = csv.writer(open(output_file, 'w+'))
crdt_writer = csv.writer(open(credit_file, 'w+'))

myList = []
creditList = []
for row in reader:
    myList = [row[0], row[1], row[3], row[8]]
    print(myList)
    writer.writerow(myList)

    creditList = [row[8], row[9]]
    for crd in creditList:
        if crd == 'C':
            for amt in creditList:
                if amt > str(15000):
                   crdt_writer.writerow(creditList)

rfile.close()
