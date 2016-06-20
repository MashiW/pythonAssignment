#!/user/bin/python
from collections import Counter
import csv

input_file = 'OPTPF.csv'
output_file = 'uniquecount.csv'

#function for writing unique values
def csv_writer(newDictionary, output_file):
    wfile = open(output_file, 'w+')
    writer = csv.writer(wfile)
    writer.writerows(newDictionary.items())
    wfile.close()


rd_file = open(input_file, "r+")
csv_f = csv.reader(rd_file, delimiter='|')
myList = []

for row in csv_f:
    myList.append(row[0])
    csv_writer(Counter(myList), output_file)

rd_file.close()
